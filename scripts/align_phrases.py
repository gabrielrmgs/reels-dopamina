"""Alinha uma narração regravada à antiga, frase a frase, para não mexer no vídeo pronto.

Uso: python align_phrases.py antiga.mp3 nova.mp3 saida.mp3
Cada frase nova começa no mesmo instante da antiga; se for mais longa que o espaço até a próxima,
é acelerada (atempo) só o necessário. Exige o mesmo número de frases nos dois arquivos — se der
diferente, tente outro take ou ajuste --noise/--min-silence.
"""
import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _audio import phrases  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("antiga")
p.add_argument("nova")
p.add_argument("saida")
p.add_argument("--noise", default="-35dB")
p.add_argument("--min-silence", type=float, default=0.18)
a = p.parse_args()

old = phrases(a.antiga, a.noise, a.min_silence)
new = phrases(a.nova, a.noise, a.min_silence)
print(f"antiga {len(old)} frases · nova {len(new)} frases")
for i, (o, n) in enumerate(zip(old, new)):
    print(f"{i:2d} antiga {o[0]:6.2f}-{o[1]:6.2f} ({o[1]-o[0]:.2f})  nova {n[1]-n[0]:.2f}")
if len(old) != len(new):
    sys.exit("número de frases diferente: escolha outro take")

filters, labels = [], []
for i, ((os_, oe), (ns, ne)) in enumerate(zip(old, new)):
    slot = (old[i + 1][0] - 0.06 if i + 1 < len(old) else oe + 3.0) - os_
    tempo = max(1.0, (ne - ns) / slot)
    f = f"[0:a]atrim={ns:.3f}:{ne:.3f},asetpts=PTS-STARTPTS"
    if tempo > 1.0:
        f += f",atempo={tempo:.4f}"
        print(f"   frase {i} acelerada x{tempo:.3f}")
    ms = int(os_ * 1000)
    f += f",adelay={ms}|{ms}[s{i}]"
    filters.append(f)
    labels.append(f"[s{i}]")
filters.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0[out]")
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", a.nova, "-filter_complex",
                ";".join(filters), "-map", "[out]", "-ar", "44100", "-b:a", "192k", a.saida], check=True)
print("ok", a.saida)
