"""Mapa de tempos da narração: lista cada frase (trecho entre pausas) com início e fim.

Uso: python timing_map.py voz.mp3 [--offset 0.3] [--noise -35dB] [--min-silence 0.15]
--offset soma o atraso da voz no vídeo (V), imprimindo já o tempo do vídeo.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _audio import duration, phrases  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("voz")
p.add_argument("--offset", type=float, default=0.0)
p.add_argument("--noise", default="-35dB")
p.add_argument("--min-silence", type=float, default=0.15)
a = p.parse_args()

segs = phrases(a.voz, a.noise, a.min_silence)
print(f"duração {duration(a.voz):.2f}s · {len(segs)} frases · offset {a.offset:+.2f}s")
for i, (s, e) in enumerate(segs):
    print(f"{i:2d}  {s + a.offset:6.2f} → {e + a.offset:6.2f}  ({e - s:4.2f}s)")
print("Associe cada linha à frase do roteiro (na ordem) e use o início como tempo da animação.")
