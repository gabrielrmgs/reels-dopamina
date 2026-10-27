# ElevenLabs: conectores, cotas e armadilhas

## Conectores
Existem dois conectores MCP do ElevenLabs:
- **Completo** (`https://api.elevenlabs.io/v1/mcp`): voz, efeitos, música e imagem.
- **Restrito**: só voz/fala; recusa imagem, vídeo e música.

Antes da Fase 2, descubra qual está ativo (lista de conectores da sessão / ferramentas
disponíveis). Se só houver o restrito, avise que trilha, efeitos e imagens precisarão do completo
(Settings → Connectors → Add custom connector) ou de arquivos fornecidos pela pessoa.

## Fluxo das ferramentas
- `creative_list_voices` (filtre `languages:["pt"]`, `gender`, `use_cases`) → escolha a voz.
- `creative_generate_speech` (2 takes) / `creative_generate_in_flow` com `node_type: "sfx"` ou
  `"music"` / `creative_generate_image` → retornam na hora e geram em segundo plano.
- Pegue as URLs com `creative_get_generations` (conector completo) ou
  `creative_get_flow_run_status` (restrito) e baixe com `curl -o`. As URLs assinadas expiram em ~2 h.
- Não chame a geração de novo para "tentar outra vez": cada chamada cobra de novo.

## Cotas e limites (descobertos na prática)
- Cada narração de ~40 s em `eleven_v4` custa ~760 créditos por take; trilha ~900; SFX ~50;
  imagem (`bytedance-seedream-5-pro`) ~820.
- Falha por cota aparece como geração `failed`; o motivo só vem em `creative_get_flow_run_status`
  (`error_message: "This request exceeds your quota…"`). Verifique antes de concluir que "falhou".
- O plano free tem **limite diário de imagens** (`free_tier_image_limit_reached`), mesmo com
  créditos sobrando.
- **Trocar de conta no site do ElevenLabs não troca a conta do conector.** O id do workspace aparece
  no `oobCode` das URLs; se não mudou, a pessoa precisa desconectar e conectar de novo o conector
  com a conta nova.
- Imagens do seedream saem **horizontais (2048x1152)** mesmo pedindo vertical. Planeje como
  card/foto dentro da tela + fundo desfocado, e gere recortes de detalhe com
  `ffmpeg -vf crop=w:h:x:y`.

## Ao final
Reporte os créditos gastos (soma dos `credit_costs`) e o que ficou pendente por cota/limite.
