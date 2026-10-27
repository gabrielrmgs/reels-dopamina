# Efeitos dopaminérgicos e fluidez

Todos os helpers estão em `templates/fx.js` (prontos, determinísticos e seguros para o seek do
HyperFrames). Este arquivo diz **quando** usar cada um.

## Ritmo
- Uma "recompensa" visual a cada ~2 s: pop de card, contador, confete, check, carimbo, troca de cor.
- Nada fica parado: use drift lento (escala 1→1,03, y ±20 px, `sine.inOut`) em fotos, cards e
  celulares enquanto a fala acontece.
- Fala e imagem andam juntas: cada palavra-chave aparece no momento em que é dita.

## Contínuos (o vídeo todo)
| Efeito | Helper | Nota |
|---|---|---|
| Barra de progresso no topo | `progress(total)` | 10 px, cor de destaque. Aumenta a sensação de "falta pouco". |
| Drift / parallax | `drift(sel, at, dur)` | Fundo e frente em velocidades diferentes. |

## Impacto (dor, golpe, hook)
| Efeito | Helper | Nota |
|---|---|---|
| Tremida | `shake(sel, at, amp)` | Determinística (keyframes), 0,3 s. |
| Zoom punch | `punch(sel, at, s)` | Texto/elemento entra maior e assenta. |
| Flash | `flash(at, opacity)` | Branco 0,5–0,9; use nas trocas de ato. |
| Carimbo | `stamp(sel, at)` | Scale 2.6→1 com `power4.in` + tremida logo depois. |
| Vinheta vermelha | CSS `box-shadow: inset` + yoyo | Para "perigo". |
| Glitch no número | keyframes de `x`/`skewX` | Para o golpe ("R$ 5.850"). |

## Recompensa (virada, solução, CTA)
| Efeito | Helper | Nota |
|---|---|---|
| Confete natural | `confetti(boxId, at, cx, cy, n, power)` | Nasce invisível, sai em leque, gira 3D, cai balançando. |
| Raios de luz | `rays(boxId, at, n, dur, spin)` | Explosão radial atrás do texto. |
| Contador | `count(el, from, to, at, dur, fmt)` | Dinheiro, km, quantidade. |
| Check | `checkIn(sel, at)` | Bolinha verde com ✓ girando. |
| Ripple de toque | `.ripple` + scale 0.5→5 | Com cursor tocando um botão. |
| Chuva de ícones | emojis caindo | Use emojis comuns (💰 💵 ❤️ 😍); 🪙 não renderiza. |

## Texto cinético
- `words(sel, at, stagger)`: cada palavra entra com blur 10→0 + y 50→0 (`expo.out`).
- Marcação no `data-text`: `*palavra*` destaque, `<b>palavra</b>` vermelho, `_palavra_` sublinhado.
  A marcação precisa envolver a palavra inteira com a pontuação: `*troca…*`, não `*troca*…`.
- Máximo ~8 palavras por bloco; troque o bloco (sai com blur para cima) em vez de empilhar.

## Transições fluidas (evite corte seco fora do hook)
| Transição | Como |
|---|---|
| Zoom-through | Cena atual `scale 1→1.6 + opacity 0` enquanto a próxima vem de `scale 0.7→1`. Ou um elemento (balão, card) cresce até virar a próxima cena. |
| Wipe diagonal | Painel gigante com gradiente da marca entra com `x: -2600 → 0` (`power4.inOut`). Ótimo para a virada. |
| Círculo expandindo | `clipPath: circle(0%) → circle(150%)` a partir do ponto de interesse. |
| Cortina | `clipPath: inset(0 0 100% 0) → inset(0)` (de cima ou de baixo). |
| Match cut | O mesmo objeto (card do carro, foto) atravessa duas cenas: some de uma e reaparece na outra na mesma posição. |
| Reorganizar lista | Cards absolutos; filtrar = mover `y` para o novo slot com `expo.out` e esconder os outros com `opacity/scale/x`. |

## Celular e telas
- Mockup 600x1261 com tela 568x1229; prints 1170x2532 encaixam com `width:568px`.
- Não "role" o print dentro do celular se ele tiver a altura exata da tela: aparece área vazia.
  Use zoom leve (`scale 1→1.06`, `transformOrigin` no ponto de interesse).
- "Cards que saltam da tela" (pop-outs) com valores grandes são o recurso que mais lembra os
  explainers profissionais.

## Fotos realistas ("do celular do vendedor")
- Moldura de câmera (VÍDEO · FOTO · RETRATO, botão de disparo) + flash no frame 0.
- Fundo: a mesma foto desfocada (`blur 40px`, `brightness .45`) cobrindo a tela.
- Detalhes da avaliação: recortes da foto principal virando polaroids (`.snap`) caindo na tela.
- Fitas de isolamento ("SEM CADASTRO ⚠") correndo em diagonal sobre a foto dessaturada = perigo.
