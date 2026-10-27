# reels-dopamina

Skill para Claude que cria Reels/Shorts verticais de alta retenção para vender apps e produtos:
roteiro persuasivo para aprovação → narração (ElevenLabs, opcional) → animação em HTML + GSAP
(HyperFrames) com efeitos dopaminérgicos → MP4 1080x1920.

## O que tem aqui
| Pasta | Conteúdo |
|---|---|
| `SKILL.md` | O fluxo completo (roteiro → aprovação → produção → verificação) |
| `references/` | Copywriting, catálogo de hooks, efeitos, áudio, ElevenLabs, HyperFrames, armadilhas |
| `templates/` | `base.html` (esqueleto do reel) e `fx.js` (biblioteca de efeitos) |
| `scripts/` | Mapa de tempos da voz, drop da trilha, extensão de trilha, alinhamento/emenda de narração, transcrição e verificação do render |
| `brands/` | Perfis de marca (`_modelo.md` para copiar; `vehiro.md` de exemplo) |
| `examples/` | Roteiros aprovados de uma série real |

## Instalação
Copie a pasta para `~/.claude/skills/reels-dopamina/` (Claude Code) ou empacote como `.skill`.

```bash
git clone <este-repo> ~/.claude/skills/reels-dopamina
```

## Requisitos
- Node.js ≥ 22 e `npm i hyperframes` na pasta onde os vídeos serão montados
- FFmpeg/ffprobe no PATH
- Python 3.10+ (scripts usam só biblioteca padrão)
- Transcrição (para validar a fala): skill `watch`, `openai-whisper` ou `whisperx`
- Opcional: conector MCP do ElevenLabs (completo: `https://api.elevenlabs.io/v1/mcp`) para voz,
  trilha, efeitos e imagens

## Uso
Peça algo como "faz um reel do meu app atacando a dor X" ou "crie um vídeo pro Instagram com um
hook forte". A skill entrega primeiro o roteiro; só gera áudio/vídeo depois do seu ok.

## Créditos
Efeitos sonoros genéricos vêm da biblioteca do HyperFrames (Pixabay, uso comercial livre) e não são
redistribuídos aqui.
