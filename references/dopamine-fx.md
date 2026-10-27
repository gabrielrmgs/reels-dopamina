# Efeitos dopaminérgicos e retenção

Todos os helpers estão em `templates/fx.js` (prontos, determinísticos e seguros para o seek do
HyperFrames). Este arquivo diz **quando** usar cada um.

## Como a dopamina prende (e o que isso muda na edição)
A dopamina dispara com **antecipação** e com **surpresa** (o que vem é melhor ou diferente do
esperado), não com recompensa previsível. Por isso:
- **Estímulo constante, mas nunca igual.** Mantenha algo novo a cada ~2 s (palavra que salta,
  contador, carimbo, corte, troca de cor), variando tipo e intensidade. Um ritmo fixo do mesmo efeito
  vira rotina e o cérebro para de reagir.
- **Escalada.** A energia sobe da agitação até a virada; cada pico é um pouco maior que o anterior.
- **Picos grandes reservados:** a **virada** (alívio, maior pico, no drop da trilha), o **resultado/
  prova** (número final, confete) e o **CTA** (final em alta). Eles ficam por cima do fluxo contínuo.
- **Anuncie antes de entregar.** "Olha o que aparece quando…", contagem regressiva, número subindo:
  a espera é onde a dopamina trabalha. Um meio segundo de pausa ou silêncio antes do pico aumenta o
  contraste.
- **Lacuna aberta.** Mostre o resultado ou a pergunta cedo e só feche depois da virada.
- **Efeito com significado.** Cada efeito sublinha a palavra ou o número dito naquele instante.
  Efeito sem ligação com a mensagem vira "efeito vampiro": a pessoa lembra do confete e esquece a
  marca.
- **Nada fica parado:** drift lento (escala 1→1,03, y ±20 px, `sine.inOut`) em fotos, cards e
  celulares enquanto a fala acontece.

## Contínuos (o vídeo todo)
| Efeito | Helper | Nota |
|---|---|---|
| Barra de progresso no topo | `progress(total)` | 10 px, cor de destaque; dá sensação de "falta pouco". Padrão; teste sem ela quando medir retenção. |
| Drift / parallax | `drift(sel, at, dur)` | Fundo e frente em velocidades diferentes. |

## Impacto (gancho, dor, golpe)
| Efeito | Helper | Nota |
|---|---|---|
| Tremida | `shake(sel, at, amp)` | Determinística (keyframes), 0,3 s. |
| Zoom punch | `punch(sel, at, s)` | Texto/elemento entra maior e assenta. Ideal para o quadro 0 (já visível). |
| Flash | `flash(at, opacity)` | Branco 0,5–0,9; use nas trocas de ato. |
| Carimbo | `stamp(sel, at)` | Scale 2.6→1 com `power4.in` + tremida logo depois. |
| Vinheta vermelha | CSS `box-shadow: inset` + yoyo | Para "perigo". |
| Glitch no número | keyframes de `x`/`skewX` | Para o golpe ("R$ 5.850"). |

## Recompensa (virada, solução, prova, CTA)
| Efeito | Helper | Nota |
|---|---|---|
| Confete natural | `confetti(boxId, at, cx, cy, n, power)` | Só nos picos grandes; nasce invisível, sai em leque, gira 3D, cai balançando. |
| Raios de luz | `rays(boxId, at, n, dur, spin)` | Explosão radial atrás do texto. |
| Contador | `count(el, from, to, at, dur, fmt)` | Dinheiro, km, quantidade — antecipação embutida. |
| Check | `checkIn(sel, at)` | Bolinha verde com ✓ girando. |
| Ripple de toque | `.ripple` + scale 0.5→5 | Com cursor tocando um botão. |
| Chuva de ícones | `rain(boxId, at, glyphs)` | Use emojis comuns (💰 💵 ❤️ 😍); 🪙 não renderiza. |

## Texto cinético
- `words(sel, at, stagger)`: cada palavra entra com blur 10→0 + y 50→0 (`expo.out`).
- Marcação no `data-text`: `*palavra*` destaque, `<b>palavra</b>` vermelho, `_palavra_` sublinhado.
  A marcação precisa envolver a palavra inteira com a pontuação: `*troca…*`, não `*troca*…`.
- Máximo ~8 palavras por bloco; troque o bloco (sai com blur para cima) em vez de empilhar.
- O texto carrega o argumento para quem assiste sem som: cada frase da fala tem uma versão curta na
  tela.

## Cortes e transições
- **Dentro do ato: corte seco no tempo da música.** É o reset de atenção mais barato — cada corte
  dispara de novo a resposta de orientação.
- **Na troca de ato: transição fluida** (abaixo). Transição fluida em tudo dá cara de vídeo
  institucional e acende o alarme de "isto é propaganda".

| Transição | Como |
|---|---|
| Zoom-through | Cena atual `scale 1→1.6 + opacity 0` enquanto a próxima vem de `scale 0.7→1`. Ou um elemento (balão, card) cresce até virar a próxima cena. |
| Wipe diagonal | Painel gigante com gradiente da marca entra com `x: -2600 → 0` (`power4.inOut`). Ótimo para a virada. |
| Círculo expandindo | `clipPath: circle(0%) → circle(150%)` a partir do ponto de interesse. |
| Cortina | `clipPath: inset(0 0 100% 0) → inset(0)` (de cima ou de baixo). |
| Match cut | O mesmo objeto (card do carro, foto) atravessa duas cenas: some de uma e reaparece na outra na mesma posição. |
| Reorganizar lista | Cards absolutos; filtrar = mover `y` para o novo slot com `expo.out` e esconder os outros com `opacity/scale/x`. |

## Áreas seguras (anúncio é o padrão)
Em 1080x1920, deixe livres de texto, número, logo e CTA: **~270 px do topo, ~670 px da base e ~65 px
de cada lateral** (zona coberta pela interface do anúncio em Reels/Stories). Ou seja, tudo que
importa fica entre y 270 e y 1250. No orgânico a base coberta é menor (~380 px), mas use o padrão
de anúncio para o mesmo vídeo servir aos dois.

## Celular e telas
- Mockup 600x1261 com tela 568x1229; prints 1170x2532 encaixam com `width:568px`.
- Não "role" o print dentro do celular se ele tiver a altura exata da tela: aparece área vazia.
  Use zoom leve (`scale 1→1.06`, `transformOrigin` no ponto de interesse).
- "Cards que saltam da tela" (pop-outs) com valores grandes destacam o benefício; mantenha-os acima
  de y 1250.

## Fotos realistas ("do celular do vendedor")
- Moldura de câmera (VÍDEO · FOTO · RETRATO, botão de disparo) + flash no frame 0.
- Fundo: a mesma foto desfocada (`blur 40px`, `brightness .45`) cobrindo a tela.
- Detalhes da avaliação: recortes da foto principal virando polaroids (`.snap`) caindo na tela.
- Fitas de isolamento ("SEM CADASTRO ⚠") correndo em diagonal sobre a foto dessaturada = perigo.
- Rosto humano olhando para o celular/produto ajuda a parar o polegar — gere como variante.

## Variante nativa (para testar em anúncio)
Além do motion graphics padrão, teste uma versão com cara de conteúdo: post-it, bloco de notas, print
de conversa genérica, balão de resposta a comentário. Tudo isso sai em HTML. O argumento e o ritmo são
os mesmos; muda só a "roupa".
