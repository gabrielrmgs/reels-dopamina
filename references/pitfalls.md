# Armadilhas já resolvidas

| Sintoma | Causa | Correção |
|---|---|---|
| Confete aparece como um retângulo parado antes de explodir | `fromTo` com `opacity:1` no "from" aplica o estado na criação (`immediateRender`) e os papéis ficam empilhados e visíveis no ponto de origem | `tl.set(d, {opacity:0, scale:0}, 0)` e animar com `tl.to` + keyframes que começam invisíveis (já no `confetti()` do `fx.js`) |
| Ponteiro de relógio em SVG não gira / gira no lugar errado | `transform-origin` CSS em elemento SVG | `rotation` + `svgOrigin: "cx cy"` no GSAP |
| Áudio mudo no MP4 | `<audio>` sem `id` ou criado por JS | `id` único e tag estática no HTML |
| Asteriscos aparecendo no texto (`*troca*…`) | Regex de destaque exige que a palavra inteira esteja entre `*` | Escreva `*troca…*` |
| Emoji vira quadrado/transparente | Fonte de emoji sem o glifo (ex.: 🪙) | Use emojis comuns (💰 💵 ❤️ ✅ 🔧) |
| Área branca no fim da tela do celular | Rolar print com altura exata da tela | Zoom leve em vez de rolagem |
| Sirene cobre o "Pare!" | Efeito a -2,5 dB da voz | Efeito ~10 dB abaixo da voz (volume 0.22) |
| Drop da trilha fora do lugar | Analisar como 44,1 kHz uma trilha de 48 kHz | Use `music_drop.py` (lê a taxa real) |
| Texto ilegível sobre fundo rabiscado | Contraste baixo | `text-shadow` com a cor do fundo em 3 camadas |
| Cena "pisca" no início ou cobre a anterior | Overlay de tela cheia visível antes do primeiro tween | `tl.set(cena, {opacity:0}, 0)` |
| Selo laranja reprovado no contraste | Branco sobre `#f59e0b` (2,15:1) | `#c2410c` |
| `transform: translateX(-50%)` some ao animar `scale` | GSAP sobrescreve o transform inline | Centralize com `left:0;right:0;margin:0 auto;width:fit-content` |
| `.dataset.text` com `<b>` quebrando palavras | Split por espaço | Envolva cada palavra separadamente: `<b>no</b> <b>concorrente.</b>` |
| Transcrição ignora a 1ª palavra | Áudio começa sem silêncio | 1 s de silêncio na frente antes de transcrever |
| Geração "failed" sem motivo | Cota estourada | Ler `error_message` em `creative_get_flow_run_status` |
| Narração continua cobrando da conta antiga | Conector ainda autenticado na conta antiga | Reconectar o conector (workspace no `oobCode` da URL mostra qual conta) |
| PowerShell `ReadAllText('index.html')` lê arquivo errado | .NET usa o diretório do processo, não o `cd` | Caminho absoluto ou ferramenta de edição |
