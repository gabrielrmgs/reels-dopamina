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
objetivo (orgânico ou anúncio; público frio, morno ou quente), provas reais disponíveis (depoimentos,
nº de clientes, notas), principal objeção, voz (feminina/masculina, ou sem narração) e formato
(Reels 9:16 é o padrão). Duração: versão principal de 35–45 s; para anúncio, também uma versão curta
de ~20 s. Se a pessoa disser "você decide", decida e explique a escolha em uma linha.

### 2. Escolher a dor
Uma dor por vídeo. Prefira a dor que (a) o público sente no bolso ou no orgulho, (b) dá para mostrar
visualmente, (c) o produto resolve de verdade com uma tela que existe, (d) acontece com frequência
(toda semana dói mais que uma vez por ano). Evite repetir dores de vídeos anteriores da mesma série —
liste as já feitas antes de escolher. Defina também o nível de consciência do público e o mecanismo
(do problema e da solução) — veja `references/copywriting.md`.

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
**Para quem:** <decisor> · **Objetivo:** <orgânico | anúncio frio/morno/quente> · **Consciência:** <nível>
**Mecanismo:** problema <causa que tira a culpa> → solução <por que o produto resolve>
**Prova:** <prova real com fonte, ou "sem prova social disponível">
**Voz:** <nome da voz> · **Duração:** ~XX s (+ versão curta ~20 s se for anúncio)

### Hooks para testar (0–3 s, mesmo corpo)
| # | Tipo | Visual (quadro 0) | Som | Fala |
|---|---|---|---|---|
| 1 | ... | ... | ... | "..." |
| 2 | ... | ... | ... | "..." |
| 3 | ... | ... | ... | "..." |
Hook principal: <#> — por que prende: ...

### Roteiro
| Tempo | Fala | Texto na tela (mudo) | Visual e efeitos | Passo no cérebro |
|---|---|---|---|---|
| 0–3 s · Hook | ... | ... | ... | orientação + "é comigo" |
| ... · Agitação | ... | ... | ... | tensão crescente |
| ... · Golpe | ... | ... | ... | aversão à perda |
| ... · Virada | ... | ... | ... | alívio (pico) |
| ... · Solução | ... | ... | ... | crença |
| ... · Prova | ... | ... | ... | prova social |
| ... · Fechamento + CTA | ... | ... | ... | decisão |

### Copy do anúncio (só se for anúncio)
- Texto principal (o gancho nos primeiros ~125 caracteres): ...
- Título (até 40): ... · Botão: ... · Destino: <página com a mesma dor>

### Teste
- Hipótese: ... · Métrica: hook rate / hold rate / CTR · Critério de corte: ...

### Para você decidir
- <só decisões reais: voz, hook principal, promessa que precisa ser suavizada, prova que falta>
```

Pare e espere aprovação. Ajustes no roteiro são baratos; aplique e reapresente só o que mudou.

## Fase 2 — Produção (só depois do "pode produzir")

Crie a pasta do projeto (ex.: `marketing/videos/<slug>/` com `assets/`), copie
`templates/base.html` para `<slug>/index.html` e `templates/fx.js` para `<slug>/fx.js`, e crie
`<slug>/meta.json` com `{"id":"<slug>","name":"<nome>"}`.

### 5. Assets
Leia `references/audio.md` e `references/elevenlabs.md` antes de gerar qualquer coisa.
- **Narração:** 2 takes no ElevenLabs (`eleven_v4`, tags como `[urgent]`, `[short pause]`),
  com o nome da marca escrito como se pronuncia (ex.: VEHIRO → "Verriro"). Hooks alternativos:
  gere só a frase de cada hook e emende no corpo com `scripts/splice_phrase.py`.
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
Regras que mais importam: quadro 0 já legível; algo novo a cada ~2 s, variando tipo e intensidade,
com a energia subindo até a virada; picos grandes só na virada, no resultado/prova e no CTA; corte
seco no tempo da música dentro do ato e transição fluida na troca de ato; barra de progresso no topo;
texto que carrega o argumento sem som; tudo que importa entre y 270 e y 1250 (áreas seguras de
anúncio: ~270 px do topo, ~670 px da base, ~65 px das laterais). Hooks alternativos trocam só a
primeira cena (`<slug>-g1`, `-g2`…). A versão curta reaproveita as cenas de gancho, virada, uma
tela e CTA.

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
Envie os MP4 (principal, variantes de hook e versão curta) e diga em prosa: o hook, o que cada cena
faz, os efeitos usados, e os pontos de atenção honestos (pronúncia que a transcrição ouviu
diferente, números ilustrativos, créditos gastos, o que não foi verificado de ouvido).
Se for anúncio, inclua como ler o teste (referências de mercado; compare com a média da conta):
hook rate = views de 3 s ÷ impressões (~30%+ é bom) → baixo: troque o hook, mantenha o corpo;
hold rate = views de 15 s ÷ views de 3 s (25%+ é forte) → baixo: o corpo não cumpre o hook;
CTR baixo com retenção boa → prova, oferta ou CTA.

## Referências
- `references/copywriting.md` — caminho da compra em 8 atos, consciência, mecanismo, regras, gatilhos.
- `references/hooks-catalog.md` — hooks validados (visual + som + fala) e quando usar cada um.
- `references/dopamine-fx.md` — catálogo de efeitos, ritmo e transições fluidas.
- `references/audio.md` — voz, pronúncia, mixagem, drop, emendas.
- `references/elevenlabs.md` — conectores, cotas, limites e armadilhas.
- `references/hyperframes.md` — esqueleto da composição, áudio, lint, snapshot, render.
- `references/pitfalls.md` — bugs já resolvidos e a correção de cada um.
- `examples/` — roteiros aprovados de uma série real (VEHIRO) para calibrar tom e formato.
