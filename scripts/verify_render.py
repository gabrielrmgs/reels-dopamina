"""Confere o MP4 final: resolução, duração, volume e a fala transcrita.

Uso: python verify_render.py video.mp4 [--expect-duration 40.6] [--no-transcribe]
"""
import argparse
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _audio import run  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("video")
p.add_argument("--expect-duration", type=float, default=None)
p.add_argument("--no-transcribe", action="store_true")
a = p.parse_args()

info = run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height",
            "-of", "compact", a.video]).stdout
print(info.strip())
ok = True
if "width=1080|height=1920" not in info:
    print("⚠ resolução diferente de 1080x1920"); ok = False
dur = float(re.search(r"duration=([\d.]+)", info).group(1))
if a.expect_duration and abs(dur - a.expect_duration) > 0.2:
    print(f"⚠ duração {dur:.2f}s (esperado {a.expect_duration})"); ok = False
if "codec_type=audio" not in info:
    sys.exit("⚠ sem faixa de áudio: todo <audio> precisa de id e estar escrito no HTML")

vol = run(["ffmpeg", "-hide_banner", "-i", a.video, "-vn", "-af", "volumedetect", "-f", "null", "-"]).stderr
mean = float(re.search(r"mean_volume: (-?[\d.]+)", vol).group(1))
peak = float(re.search(r"max_volume: (-?[\d.]+)", vol).group(1))
print(f"volume médio {mean} dB · pico {peak} dB")
if not -20 <= mean <= -18:
    print("⚠ volume médio fora de -20..-18 dB"); ok = False
if peak > -1:
    print("⚠ pico acima de -1 dB"); ok = False

if not a.no_transcribe:
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "transcribe_check.py"), a.video])
    print("Compare com o roteiro: a fala do hook precisa aparecer (se não, o efeito sonoro está mascarando a voz).")
print("OK" if ok else "Revise os avisos acima.")
