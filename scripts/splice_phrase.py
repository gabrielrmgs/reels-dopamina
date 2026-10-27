"""Troca o começo da narração por um trecho regravado (ex.: o hook saiu com a palavra errada).

Uso: python splice_phrase.py base.mp3 trecho.mp3 saida.mp3 --keep-from 1.40 [--trecho-ate 1.75] [--gap 0.30]
- --keep-from: segundo da base a partir do qual o áudio original continua (início da frase seguinte,
  um pouco antes dela; veja timing_map.py).
- --trecho-ate: corta o trecho novo nesse segundo (padrão: inteiro).
- --gap: silêncio entre o trecho novo e o resto.
Depois da emenda os tempos mudam: rode timing_map.py de novo no arquivo de saída.
"""
import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _audio import duration  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("base")
p.add_argument("trecho")
p.add_argument("saida")
p.add_argument("--keep-from", type=float, required=True)
p.add_argument("--trecho-ate", type=float, default=None)
p.add_argument("--gap", type=float, default=0.30)
a = p.parse_args()

end = a.trecho_ate if a.trecho_ate else duration(a.trecho)
fc = (f"[0:a]atrim=0:{end},asetpts=PTS-STARTPTS,apad=whole_dur={end + a.gap}[h];"
      f"[1:a]atrim=start={a.keep_from},asetpts=PTS-STARTPTS[r];[h][r]concat=n=2:v=0:a=1[out]")
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", a.trecho, "-i", a.base,
                "-filter_complex", fc, "-map", "[out]", "-ar", "44100", "-b:a", "192k", a.saida], check=True)
print(f"ok {a.saida} ({duration(a.saida):.2f}s); deslocamento do resto: {end + a.gap - a.keep_from:+.2f}s")
