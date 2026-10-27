"""Acha o drop da trilha: o ponto onde a energia de graves salta e se mantém alta.

Uso: python music_drop.py trilha.mp3 [--after 8] [--before 30]
Imprime a curva resumida e o drop estimado (segundos reais, já considerando 44,1/48 kHz).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _audio import rms_curve  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("trilha")
p.add_argument("--after", type=float, default=6.0, help="ignora drops antes deste segundo")
p.add_argument("--before", type=float, default=35.0)
a = p.parse_args()

curve = rms_curve(a.trilha, step=0.25, lowpass=110)
print(" ".join(f"{t:.1f}:{v:.0f}" for t, v in curve[::2]))

best, best_t = -1e9, None
for i in range(4, len(curve) - 8):
    t = curve[i][0]
    if not (a.after <= t <= a.before):
        continue
    before = sum(v for _, v in curve[i - 4:i]) / 4      # 1 s antes
    after = sum(v for _, v in curve[i:i + 8]) / 8       # 2 s depois
    score = after - before
    if score > best:
        best, best_t = score, t
if best_t is None:
    sys.exit("não achei drop no intervalo; ajuste --after/--before")
print(f"drop ≈ {best_t:.2f}s (salto de {best:.1f} dB nos graves)")
print("data-start da trilha = (início da frase da virada + V) - drop")
