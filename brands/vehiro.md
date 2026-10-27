# Perfil de marca — VEHIRO

## Identidade
- **Nome falado na narração:** "Verriro". Site falado: "verriro ponto com ponto br".
- **Cores (tokens CSS, de `client/src/index.css`):** primária `#2563eb` (hsl 221 83% 53%),
  navy `#0b1b4d` / `#0f2a6b`, fundo claro `#f4f6fa`, texto `#0f172a`, sucesso `#059669` / menta
  `#34d399`, perigo `#f43f5e`, alerta `#dc2626`, dourado `#fbbf24`.
- **Fontes:** Outfit (títulos, 700–900) e Inter (texto/UI).
- **Logo (LogoMark):** SVG abaixo; `--tile` = fundo do quadrado, `--car` = carro.

```html
<symbol id="logo" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="8" style="fill:var(--tile)" />
  <g style="fill:var(--car)"><path d="M9.4 15.4 11.7 9.9c.2-.5.7-.8 1.2-.8h6.2c.5 0 1 .3 1.2.8l2.3 5.5z"/><path d="M5.2 21.2v-3.3c0-1.5 1-2.7 2.5-2.7h16.6c1.5 0 2.5 1.2 2.5 2.7v3.3c0 .9-.6 1.5-1.5 1.5H6.7c-.9 0-1.5-.6-1.5-1.5z"/><rect x="7.2" y="21.8" width="4.4" height="3.2" rx="1.1"/><rect x="20.4" y="21.8" width="4.4" height="3.2" rx="1.1"/></g>
  <g style="fill:var(--tile)"><path d="M12.1 14.6l.9-3.5h6l.9 3.5z"/><path d="M7.2 16.7h5.4l-1.5 2.3H7.9c-.5 0-.7-.4-.7-.8z"/><path d="M24.8 16.7h-5.4l1.5 2.3h3.2c.5 0 .7-.4.7-.8z"/></g>
  <path d="M13.6 17.3 16 20.9l2.4-3.6" fill="none" style="stroke:var(--tile)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
</symbol>
```

- **Tom:** direto, informal, jargão de loja de veículos.

## Público
- **Decide a compra:** dono de loja/revenda de veículos seminovos (pequena e média).
- **Inimigo comum:** planilha, caderno, avaliação "no olho", fotos espalhadas no WhatsApp.
- **Jargão:** pátio, troca, FIPE, avaliação, repasse, consignado, comissão de intermediário,
  vendedor, preparação, funilaria, documentação.
- **Dores (✓ = já tem vídeo):**
  - ✓ Visão geral do app (explainer) — `explainer-reels`
  - ✓ Lucro real escondido por despesas não somadas — `lucro-real`
  - ✓ Cliente perdido por demorar a responder / caçar fotos — `cliente-perdido`
  - ✓ Pátio desorganizado, ninguém sabe o status dos carros — `patio-organizado`
  - ✓ Troca mal avaliada, paga acima da FIPE e entra sem custo — `troca-avaliada`
  - ☐ Comissão de intermediário esquecida / briga por comissão
  - ☐ Equipe vendo o que não deve (acesso por função)
  - ☐ Fechamento do mês no caderno/planilha

## Produto (fonte da verdade)
- **Repo:** AutoManager (`client/src`, `server/routes`, `shared/schema.ts`).
- **Fatos conferidos:**
  - Status do veículo: Disponível, Vendido, Em Manutenção, Aguardando Preparação, Reservado
    (`VEHICLE_STATUS`); filtro por status e busca por placa/modelo/marca na lista.
  - Painel "No Pátio" mostra só a contagem de disponíveis (não separa por status).
  - Venda com troca e FIPE na hora (`SellVehicleDialog`); a troca entra no estoque como
    "Aguardando Preparação" com custo = valor da troca.
  - Fotos por QR code (link vale 2 h); vitrine pública com botão "Tenho interesse" que abre o
    WhatsApp com: "Olá! Vi o {marca} {modelo} {ano} no catálogo e tenho interesse."
  - Resumo financeiro por venda (venda − compra − despesas − comissão = lucro líquido) e
    relatório mensal.
- **Telas reais:** `marketing/videos/screens/m-*.png` (1170x2532): dashboard, fipe, qr, resumo,
  vitrine. Frames de relatório em `marketing/videos/raw/`.

## Oferta e CTA
- **Teste grátis de 7 dias** (`TRIAL_DAYS = 7` em `shared/models/tenancy.ts`).
- **Endereço:** vehiro.com.br · **Instagram:** @vehiroapp

## Produção
- **Vozes:** "Ana Alice – Friendly and Clear" (fem., `ORgG8rwdAiMYRug8RJwR`) e
  "Marcio – Viral Hook Narrator" (masc., `plASsyS7JE6GCAvx9uIc`, voz atual da série).
- **Projetos:** `marketing/videos/<slug>/` · renders em `marketing/videos/renders/`.
