---
name: reels-dopamina
description: Cria Reels/Shorts/TikTok verticais (1080x1920) de alta retenção para vender um app, SaaS ou produto — do roteiro persuasivo ao MP4 renderizado. Primeiro entrega o ROTEIRO (hook visual + sonoro + falado, dor, virada, solução com telas reais, CTA) para aprovação; só depois gera narração (ElevenLabs, opcional), trilha, efeitos e anima tudo em HTML + GSAP com HyperFrames, com efeitos dopaminérgicos fluidos (barra de progresso, zoom punch, confete, contadores, transições contínuas). Use SEMPRE que o vídeo curto for para vender ou explicar um app, SaaS ou produto, em pedidos como "faz um reel do meu app", "vídeo pro Instagram/TikTok do produto", "vídeo explicativo do app", "anúncio em vídeo", "vídeo tocando na dor do cliente", "hook que prenda nos 3 primeiros segundos", "vídeo estilo app explainer", ou quiser transformar uma dor/funcionalidade do produto em vídeo curto vertical — mesmo sem citar a skill. Não use para reel de conteúdo sem produto a vender (dica, lista, aula), para editar vídeo gravado com pessoas (talking head), thumbnails ou carrosséis estáticos.
---

# Reels dopaminérgicos para apps

Esta skill produz vídeos verticais curtos que vendem um produto atacando **uma dor** do público,
com retenção alta do primeiro ao último segundo. O processo tem duas fases separadas por uma
aprovação humana, porque gerar voz, trilha e imagens custa créditos e tempo — errar o roteiro e
descobrir só no render é o desperdício mais caro do processo.

```
Fase 1 (barata)  briefing → checar a verdade no produto → ROTEIRO → aprovação
Fase 2 (cara)    assets → mapa de tempos → composição → revisão visual → render → verificação
```

## Antes de tudo: perfil de marca

Procure um perfil em `brands/<marca>.md` (cores, fontes, logo SVG, pronúncia do nome, CTA, oferta,
@ do Instagram, onde ficam as telas do app). Se não existir, crie um a partir de
`brands/_modelo.md` com o que a pessoa disser ou com o que você achar no código/site do produto
(tokens de cor no CSS, logo no componente de marca, página de preços). `brands/vehiro.md` é um
exemplo completo.

## Fase 1 — Roteiro

### 1. Briefing curto
Pergunte só o que faltar: produto/marca, público (quem decide a compra), a dor (ou "escolhe você"),
voz (feminina/masculina, ou sem narração), duração alvo (30–50 s), formato (Reels 9:16 é o padrão).
Se a pessoa disser "você decide", decida e explique a escolha em uma linha.

### 2. Escolher a dor
Uma dor por vídeo. Prefira a dor que (a) o público sente no bolso ou no orgulho, (b) dá para mostrar
visualmente, (c) o produto resolve de verdade com uma tela que existe. Evite repetir dores de vídeos
anteriores da mesma série — liste as já feitas antes de escolher.

### 3. Checar a verdade no produto
Para cada promessa do roteiro, confirme no código, nas telas ou no site que a funcionalidade existe
e se comporta como você vai dizer. Isto evita propaganda enganosa e retrabalho. Exemplos reais do
que essa checagem pegou: o painel não separava carros por status (só o filtro da lista separava);
"em tempo real" virou "sempre atualizado" porque o status muda quando alguém atualiza; o teste
grátis era de 7 dias (constante no código); a mensagem do WhatsApp gerada pelo app tinha um texto
exato que virou a fala do vídeo. Se algo não existir, mude a promessa, não invente.

### 4. Escrever o roteiro
Leia `references/copywriting.md` (estrutura e regras de copy) e `references/hooks-catalog.md`
(hooks validados). Use `references/dopamine-fx.md` para escolher os efeitos de cada cena.

Entregue SEMPRE neste formato, em texto no chat:

```markdown
## Reels N — "<nome da dor>"
**Dor:** <uma frase>. **O que o produto tem de verdade:** <bullets com onde conferiu>.
**Voz:** <nome da voz> · **Duração:** ~XX s

### Hook (0–3 s)
- **Visual:** ...   - **Som:** ...   - **Fala:** "..."
- Por que prende: ...

### Roteiro
| Tempo | Fala | Visual e efeitos |
|---|---|---|
| 0–3 s · Hook | ... | ... |
| ... · Agitação | ... | ... |
| ... · Golpe | ... | ... |
| ... · Virada | ... | ... |
| ... · Solução | ... | ... |
| ... · CTA | ... | ... |

### Para você decidir
- <só decisões reais: voz, hook alternativo, promessa que precisa ser suavizada>
```

Pare e espere aprovação. Ajustes no roteiro são baratos; aplique e reapresente só o que mudou.

## Fase 2 — Produção (só depois do "pode produzir")

Crie a pasta do projeto (ex.: `marketing/videos/<slug>/` com `assets/`), copie
`templates/base.html` para `<slug>/index.html` e `templates/fx.js` para `<slug>/fx.js`, e crie
`<slug>/meta.json` com `{"id":"<slug>","name":"<nome>"}`.

### 5. Assets
Leia `references/audio.md` e `references/elevenlabs.md` antes de gerar qualquer coisa.
- **Narração:** 2 takes no ElevenLabs (`eleven_v4`, tags como `[urgent]`, `[short pause]`),
  com o nome da marca escrito como se pronuncia (ex.: VEHIRO → "Verriro").
- **Trilha:** instrumental com tensão até a virada e drop animado depois.
- **Efeitos do hook:** sirene, buzina de game show, caixa registradora etc. (curtos, ~1 s).
- **Imagens realistas** (opcional): "foto de celular do vendedor" — veja `references/elevenlabs.md`
  sobre limite diário e formato horizontal.
- **Telas reais do app:** prints mobile 3x (1170x2532) ficam ótimos dentro do mockup de celular.
Sem ElevenLabs ou sem créditos: ofereça versão sem narração (tipografia cinética carrega a mensagem)
ou espere a pessoa liberar créditos — não troque de voz/provedor sem perguntar.

### 6. Validar a voz
Rode `python scripts/transcribe_check.py <voz.mp3>` (usa o skill `watch` local se existir, senão
Whisper) e compare com o texto. Escolha o take sem erros de palavra; se só o começo errar (ex.: o
hook saiu "Palha agora" em vez de "Pare agora"), regere só esse trecho e emende com
`scripts/splice_phrase.py` (ele só troca o começo). Erro no meio da narração: regere o take
inteiro; se o vídeo já estiver pronto, use `scripts/align_phrases.py` para manter o encaixe.

### 7. Mapa de tempos
- `python scripts/timing_map.py voz.mp3` → lista de frases com início/fim (silêncios).
- `python scripts/music_drop.py trilha.mp3` → segundo exato do drop (energia de graves).
- Defina `V` (atraso da voz, 0,25–0,9 s) e posicione a trilha para o drop cair na frase da virada:
  `inicio_trilha = (inicio_virada + V) - drop`.
- Se a trilha for curta, `python scripts/extend_music.py trilha.mp3 trilha-ext.mp3 --cut <s> --bars 2 --bpm <bpm>`
  (repete compassos da parte animada com crossfade).
- Se a voz passar de ~48 s, acelere 5–8% com `atempo` (mantém o tom).
Cada animação de fala entra no tempo da frase: `tempo_video = tempo_voz + V`.

### 8. Composição
Monte as cenas no `index.html` seguindo `references/dopamine-fx.md` e `references/hyperframes.md`.
Regras que mais importam: cenas se sobrepõem 0,2–0,5 s com transição em movimento; uma "recompensa"
visual a cada ~2 s; barra de progresso no topo; textos importantes fora das faixas cobertas pela UI
do Reels (topo ~220 px e base ~380 px).

### 9. Revisão visual
`npx hyperframes lint .` (0 erros) e
`npx hyperframes snapshot . --at <tempos-chave> --no-end -o snapshots`. Olhe o contact sheet:
texto cortado, sobreposição ilegível, cena vazia, elemento que não animou. Corrija e repita só nos
tempos afetados. Consulte `references/pitfalls.md` quando algo não aparecer ou aparecer antes da hora.

### 10. Render e verificação
`npx hyperframes render . -o ../renders/<slug>-9x16.mp4 -f 30 -q delivery`, depois
`python scripts/verify_render.py ../renders/<slug>-9x16.mp4`: confere duração, 1080x1920, volume
médio (~-18 a -20 dB) e transcreve. Se o hook não aparecer na transcrição, o efeito sonoro está
mascarando a voz — baixe o efeito (veja `references/audio.md`).

### 11. Entrega
Envie o MP4 e diga em prosa: o hook, o que cada cena faz, os efeitos usados, e os pontos de atenção
honestos (pronúncia que a transcrição ouviu diferente, números ilustrativos, créditos gastos, o que
não foi verificado de ouvido).

## Referências
- `references/copywriting.md` — estrutura em 7 atos, regras de copy, gatilhos.
- `references/hooks-catalog.md` — hooks validados (visual + som + fala) e quando usar cada um.
- `references/dopamine-fx.md` — catálogo de efeitos, ritmo e transições fluidas.
- `references/audio.md` — voz, pronúncia, mixagem, drop, emendas.
- `references/elevenlabs.md` — conectores, cotas, limites e armadilhas.
- `references/hyperframes.md` — esqueleto da composição, áudio, lint, snapshot, render.
- `references/pitfalls.md` — bugs já resolvidos e a correção de cada um.
- `examples/` — roteiros aprovados de uma série real (VEHIRO) para calibrar tom e formato.
