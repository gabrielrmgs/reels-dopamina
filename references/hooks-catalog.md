# Catálogo de hooks (0–3 s)

Um hook bom tem três camadas sincronizadas: **visual** (funciona no mudo), **som** (corta o scroll
de quem está com áudio) e **fala** (a frase que a pessoa repete na cabeça). Varie o tipo de hook
entre vídeos da mesma série — o público se acostuma.

## 1. Alerta / sirene — "PARE!"
- **Visual:** fundo vermelho-escuro, sirene SVG girando com feixes de luz (conic-gradient), flash
  vermelho piscando, "PARE!" gigante batendo (scale 2.4→1) com tremida, depois "AGORA".
- **Som:** sirene curta (≤1,5 s, gerada no ElevenLabs SFX) + impacto grave. Sirene ~10 dB abaixo
  da voz, senão mascara o "Pare!".
- **Fala:** "Pare! Pare agora! Esse carro que você vendeu… deu lucro mesmo?"
- **Use quando:** a dor é perda de dinheiro escondida.

## 2. Rajada de notificações + corte seco
- **Visual:** 10 notificações de cliente caindo uma atrás da outra, contador vermelho 1→47.
  Em ~0,85 s tudo congela, desfoca e escurece (corte seco).
- **Som:** "plim" genérico (não usar o som de marca do WhatsApp) acelerando + silêncio de 0,3 s +
  impacto grave.
- **Fala:** "Seu cliente acabou de comprar… no concorrente."
- **Use quando:** a dor é lentidão/atendimento.

## 3. Quiz de game show
- **Visual:** fundo roxo de auditório com raios girando, "VALENDO!" dourado, cartão com a
  pergunta, cronômetro circular esvaziando 3…2…1, tela vermelha + carimbo "TEMPO ESGOTADO".
- **Som:** tique-taque + buzina de "errou".
- **Fala:** "Valendo! Quantos carros estão prontos pra venda no seu pátio… agora? Três, dois, um…"
- **Use quando:** a dor é desorganização/falta de informação (a pessoa não sabe a resposta).

## 4. Foto do celular + prejuízo
- **Visual:** UI da câmera do celular, flash do disparo, foto realista do produto/objeto; etiqueta
  de preço bate em cima; número de prejuízo em vermelho pulsando ("+R$ 7 mil").
- **Som:** clique de câmera + caixa registradora seguida de arranhão de disco.
- **Fala:** "Você acabou de pagar sete mil a mais nesse carro."
- **Use quando:** a dor é uma decisão de compra/avaliação mal feita.

## 5. Pergunta acusatória com objeto
- **Visual:** objeto (carro) entra, carimbo "VENDIDO" bate com tremida, "?" gigante balançando.
- **Som:** impacto + whoosh.
- **Fala:** "Esse carro que você vendeu… deu lucro mesmo?"

## Ideias ainda não usadas (para variar)
- **Contagem de dinheiro ao contrário:** contador de R$ descendo rápido, "isso foi o que você perdeu
  esse mês".
- **Tela rachando:** print de planilha/caderno trincando com som de vidro.
- **"POV:" de humor:** "POV: o cliente pergunta o km e você vai olhar no carro".
- **Comparação lado a lado:** loja A (bagunça) × loja B (organizada) com placar.
- **Erro de digitação ao vivo:** valor sendo digitado errado e o prejuízo aparecendo.

## Regras
- O hook visual começa no frame 0 (nada de logo ou fade-in lento antes).
- A fala começa em até 0,9 s. Se houver efeito sonoro, a fala entra logo depois do pico dele.
- A frase do hook tem até ~10 palavras e um elemento concreto (número, objeto, cena).
