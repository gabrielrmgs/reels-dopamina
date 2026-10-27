# Áudio: voz, efeitos e trilha

## Narração
- Modelo `eleven_v4` com tags de direção: `[urgent, firm]`, `[dramatic, punchy]`,
  `[conversational]`, `[serious]`, `[energetic, upbeat]`, `[confident]`, `[short pause]`,
  `[fast]`, `[excited, game show host]`.
- Gere **2 takes** e escolha pela transcrição (um take costuma errar uma palavra).
- Escreva números por extenso quando a pronúncia importa ("sessenta e dois mil").
- **Nome da marca:** escreva como se pronuncia. VEHIRO → "Verriro"; site → "verriro ponto com
  ponto br". Registre isso no perfil da marca.
- Voz rápida retém mais: se o take passar de ~48 s, acelere 5–8% com
  `ffmpeg -i voz.mp3 -af atempo=1.07 voz-final.mp3` (mantém o tom).
- Vozes que funcionaram em PT-BR (biblioteca ElevenLabs): "Ana Alice – Friendly and Clear"
  (feminina, `ORgG8rwdAiMYRug8RJwR`) e "Marcio – Viral Hook Narrator" (masculina,
  `plASsyS7JE6GCAvx9uIc`). Confirme com `creative_list_voices` — IDs podem mudar.

## Validação da fala
O Whisper local engole a primeira palavra se o áudio começa sem silêncio: transcreva com 1 s de
silêncio na frente (`scripts/transcribe_check.py` já faz isso). Diferenças como "vem demais" ×
"vende mais" ou "Onyx" × "Onix" costumam ser do reconhecimento — mas "Palha agora" × "Pare agora"
no hook foi erro real da voz e precisou regravar o trecho.

**Regravar só o começo** (ex.: o hook): gere apenas a frase, corte com `atrim`, e emende com
`scripts/splice_phrase.py` deixando ~0,4 s de pausa natural antes da frase seguinte.

**Trocar uma palavra mantendo o vídeo pronto** (ex.: pronúncia da marca): regere o take inteiro com
a correção e rode `scripts/align_phrases.py antiga.mp3 nova.mp3 saida.mp3` — cada frase nova começa
no mesmo instante da antiga (acelera de leve só se não couber). Requer o mesmo número de frases.

## Efeitos sonoros
- Gere os do hook no ElevenLabs SFX (`eleven_text_to_sound_v2`): "short punchy digital alarm…",
  "TV game show wrong answer buzzer…", "cash register cha-ching followed by a vinyl record
  scratch…", "single short clean smartphone notification ping, generic (not any brand's sound)".
- Biblioteca grátis do HyperFrames (Pixabay, uso comercial livre):
  `node_modules/hyperframes/dist/skills/media-use/audio/assets/sfx/` — whoosh, pop, click, chime,
  impact-bass, glitch, riser, sparkle, typing, ping, notification. Copie para `assets/` do projeto;
  não versione esses arquivos no repositório da skill.
- Volumes de referência (`data-volume`): voz 1.0 · trilha 0.16–0.17 · whoosh 0.35 · pop 0.4 ·
  impacto 0.35–0.45 · sirene 0.22 · chime 0.25–0.35.
- **Mascaramento:** se o efeito toca junto com a fala, ele precisa ficar ~10 dB abaixo da voz.
  Meça: `ffmpeg -i voz.mp3 -t 2 -af volumedetect -f null -` vs. o efeito com o volume aplicado.

## Trilha
- Peça ao ElevenLabs Music (`eleven_music_v2_5`, ~40–44 s): "0–N s tensão (…), em N s riser e drop
  animado (…), 112–120 BPM, minimal para a voz, final resolvido em X s, instrumental".
- O drop raramente cai onde você pediu. Meça com `scripts/music_drop.py` (energia de graves;
  já considera a taxa de amostragem real — trilhas vêm em 48 kHz).
- Posicione: `data-start` da trilha = `(início da frase da virada + V) - drop`. Antes disso, só
  efeitos do hook (o silêncio musical deixa o hook mais forte).
- Trilha curta: `scripts/extend_music.py` repete compassos da parte animada com crossfade de 0,5 s
  (use múltiplos de compasso: 4 tempos = 60/BPM×4 s). Ou estique 5% com `atempo=0.95`.
- `data-fade-out="1.2"` na trilha.

## Mix final
Volume médio do MP4 entre -18 e -20 dB, pico ≤ -1 dB. `scripts/verify_render.py` mede.
