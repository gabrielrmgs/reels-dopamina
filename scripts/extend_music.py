"""Estende uma trilha repetindo compassos da parte animada, com crossfade.

Uso: python extend_music.py trilha.mp3 saida.mp3 --cut 38 --bars 2 --bpm 120
Mantém 0→cut e emenda a partir de (cut - bars*compasso) até o fim, com crossfade de 0,5 s.
Ganha `bars` compassos de duração (compasso = 4 tempos = 240/bpm s). Corte dentro da parte
animada e antes do final, para o final resolvido continuar no fim.
"""
import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _audio import duration  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("trilha")
p.add_argument("saida")
p.add_argument("--cut", type=float, required=True)
p.add_argument("--bars", type=int, default=2)
p.add_argument("--bpm", type=float, default=120)
a = p.parse_args()

bar = 240.0 / a.bpm
back = a.cut - a.bars * bar
if back <= 0:
    sys.exit("cut muito cedo para essa quantidade de compassos")
fc = (f"[0:a]atrim=0:{a.cut},asetpts=PTS-STARTPTS[a];"
      f"[0:a]atrim=start={back},asetpts=PTS-STARTPTS[b];"
      f"[a][b]acrossfade=d=0.5:c1=tri:c2=tri[out]")
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", a.trilha, "-filter_complex", fc,
                "-map", "[out]", "-b:a", "192k", a.saida], check=True)
print(f"{duration(a.trilha):.2f}s → {duration(a.saida):.2f}s ({a.saida})")
