# HyperFrames: o essencial para estes reels

Instalação: `npm i hyperframes` na pasta de vídeos (requer Node ≥ 22 e FFmpeg). Comandos rodam
dentro da pasta do projeto do vídeo (a que tem `index.html` e `meta.json`).

## Esqueleto
- Raiz: `<div id="root" data-composition-id="<id>" data-start="0" data-duration="<total>"
  data-width="1080" data-height="1920">`.
- Cada cena: `<section class="scene clip" data-start="s" data-duration="d">`. A visibilidade é
  controlada pelo runtime a partir de `data-start`/`data-duration`; cenas podem se sobrepor.
- Uma timeline GSAP pausada registrada em `window.__timelines["<id>"] = tl`, com tempos absolutos
  (segundos do vídeo). Termine com `tl.seek(0)`.
- Só lógica determinística: nada de `Math.random()`/`Date.now()` — use o gerador com semente do
  `fx.js` (`rnd()`).
- GSAP via CDN `https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js`; fontes Google.
- `meta.json`: `{"id":"<slug>","name":"<nome>"}`.

## Áudio
- `<audio id="..." src="assets/x.mp3" data-start="s" data-duration="d" data-volume="v">`.
- **Todo `<audio>` precisa de `id`** (senão fica mudo no render) e deve estar **escrito no HTML**
  (áudio criado via JS não é detectado).
- `data-fade-out="1.2"` para a trilha.

## Ciclo
```bash
npx hyperframes lint .                       # 0 erros; avisos de "sub-composition" podem ser ignorados
npx hyperframes snapshot . --at 0.5,3,8 --no-end -o snapshots   # gera contact-sheet-*.jpg
npx hyperframes render . -o ../renders/<slug>-9x16.mp4 -f 30 -q delivery
```
Leia os `contact-sheet-*.jpg` para revisar. O render de ~45 s leva 1,5–2,5 min (rode em
segundo plano se a ferramenta permitir).

## Avisos de lint que importam
- `media_missing_id` → falta `id` no `<audio>`.
- `gsap_fullscreen_overlay_starts_visible` → adicione `tl.set("#cena", {opacity: 0}, 0)` para a
  cena que começa com `fromTo` de opacidade.
- `gsap_repeated_fromto_without_baseline` → use `immediateRender: false` no segundo `fromTo` do
  mesmo alvo.
- Contraste WCAG → escureça a cor de fundo do selo (ex.: laranja `#c2410c` em vez de `#f59e0b`).
