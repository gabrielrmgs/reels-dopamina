"""Funções comuns dos scripts (só biblioteca padrão + ffmpeg/ffprobe no PATH)."""
import re
import subprocess


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).stdout
    return float(out.strip())


def sample_rate(path):
    out = run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=sample_rate",
               "-of", "csv=p=0", path]).stdout
    return int(out.strip().split(",")[0])


def phrases(path, noise="-35dB", min_silence=0.15):
    """Frases = trechos entre silêncios. Retorna [(inicio, fim), ...] em segundos."""
    err = run(["ffmpeg", "-hide_banner", "-i", path, "-af", f"silencedetect=noise={noise}:d={min_silence}",
               "-f", "null", "-"]).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    total = duration(path)
    segs, cur = [], 0.0
    for s, e in zip(starts, ends):
        if s > cur + 0.05:
            segs.append((cur, s))
        cur = e
    if total > cur + 0.05:
        segs.append((cur, total))
    return segs


def rms_curve(path, step=0.25, lowpass=None):
    """RMS (dB) a cada `step` segundos, usando a taxa de amostragem real do arquivo."""
    sr = sample_rate(path)
    n = max(1, int(sr * step))
    af = (f"lowpass=f={lowpass}," if lowpass else "") + \
        f"asetnsamples={n},astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level"
    err = run(["ffmpeg", "-hide_banner", "-i", path, "-af", af, "-f", "null", "-"]).stderr
    vals = []
    for m in re.findall(r"RMS_level=(-?[\d.]+|-inf)", err):
        vals.append(-120.0 if m == "-inf" else float(m))
    return [(i * n / sr, v) for i, v in enumerate(vals)]
