"""Transcreve um áudio/vídeo para conferir a fala (com 1 s de silêncio na frente, senão o Whisper
costuma engolir a primeira palavra).

Uso: python transcribe_check.py arquivo.mp3 [--lang pt] [--start 0 --dur 6]
Tenta, nesta ordem: o skill `watch` local (~/.claude/skills/watch), o CLI `whisper` (openai-whisper)
e o `whisperx`. Se nenhum existir, avisa como instalar.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile

p = argparse.ArgumentParser()
p.add_argument("arquivo")
p.add_argument("--lang", default="pt")
p.add_argument("--start", type=float, default=None)
p.add_argument("--dur", type=float, default=None)
a = p.parse_args()

tmp = tempfile.mkdtemp(prefix="reels-tc-")
padded = os.path.join(tmp, "padded.mp3")
cut = []
if a.start is not None:
    cut += ["-ss", str(a.start)]
if a.dur is not None:
    cut += ["-t", str(a.dur)]
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *cut, "-i", a.arquivo, "-vn",
                "-af", "adelay=1000|1000", padded], check=True)

watch = os.path.expanduser("~/.claude/skills/watch/scripts/watch.py")
env = dict(os.environ, WATCH_WHISPERX_LANGUAGE=a.lang)
if os.path.exists(watch):
    out = subprocess.run([sys.executable, watch, padded, "--detail", "transcript", "--out-dir", tmp],
                         capture_output=True, text=True, env=env).stdout
    lines = [ln for ln in out.splitlines() if ln.startswith("[")]
    print("\n".join(lines) if lines else out[-2000:])
elif shutil.which("whisper"):
    subprocess.run(["whisper", padded, "--language", a.lang, "--model", "small", "--output_dir", tmp,
                    "--output_format", "txt"], check=True)
    print(open(os.path.join(tmp, "padded.txt"), encoding="utf-8").read())
elif shutil.which("whisperx"):
    subprocess.run(["whisperx", padded, "--language", a.lang, "--output_dir", tmp, "--output_format", "txt"],
                   check=True)
    print(open(os.path.join(tmp, "padded.txt"), encoding="utf-8").read())
else:
    sys.exit("Sem transcritor: instale `pip install openai-whisper` ou o skill `watch`.")
print("(tempos acima estão +1 s por causa do silêncio adicionado)")
