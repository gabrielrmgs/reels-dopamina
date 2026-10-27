# Catálogo de hooks (0–3 s)

Um hook bom tem três camadas sincronizadas: **visual** (funciona no mudo), **som** (corta o scroll
de quem está com áudio) e **fala** (a frase que a pessoa repete na cabeça). E precisa fazer três
coisas: gerar reação emocional, chamar quem compra (e afastar quem não compra) e se ligar à história
de venda em até 3 s. Hook chamativo sem ligação com a dor ou o produto é "hook slop": prende e não
vende.

**Variação:** no orgânico, varie o tipo de hook entre vídeos da série (o público se acostuma). No
anúncio, entregue **3–5 hooks de tipos diferentes sobre o mesmo corpo** — o hook é a variável que mais
pesa no resultado. A narração do corpo é gravada uma vez; cada hook é um trecho emendado com
`scripts/splice_phrase.py`.

Fórmula curta (Hormozi): **chamado** ("é comigo") + **condição de valor** ("se [público] fizer
[ação], consegue [recompensa]").

## 1. Alerta / sirene — "PARE!" (use como variante)
- **Visual:** fundo vermelho-escuro, sirene SVG girando com feixes de luz (conic-gradient), flash
  vermelho piscando, "PARE!" gigante batendo com tremida, e já o objeto da dor (o carro, o número).
- **Som:** sirene curta (≤1,5 s, ElevenLabs SFX) + impacto grave. Sirene ~10 dB abaixo da voz.
- **Fala:** "Pare! Esse carro vendido por 85 mil… deu lucro mesmo?"
- **Use quando:** a dor é perda de dinheiro escondida. Cuidado: o comando genérico gasta ~1 s, o
  público já ficou cego a ele, e a sirene some no mudo e associa a marca a incômodo. Prefira abrir
  direto pelo concreto (objeto + número) e teste este como alternativa.

## 2. Rajada de notificações + corte seco
- **Visual:** 10 mensagens de cliente caindo dentro de um celular (mockup, não banner de sistema em
  tela cheia), contador vermelho 1→47. Em ~0,85 s tudo congela, desfoca e escurece (corte seco).
- **Som:** "plim" genérico (não usar o som de marca do WhatsApp) acelerando + silêncio de 0,3 s +
  impacto grave.
- **Fala:** "O cliente pediu foto às 9h. Às 11h, comprou na loja da frente."
- **Use quando:** a dor é lentidão/atendimento.

## 3. Quiz de game show
- **Visual:** fundo roxo de auditório com raios girando, "VALENDO!" dourado, cartão com a
  pergunta, cronômetro circular esvaziando 3…2…1, tela vermelha + carimbo "TEMPO ESGOTADO".
- **Som:** tique-taque + buzina de "errou".
- **Fala:** "Valendo! Quantos carros estão prontos pra venda no seu pátio… agora? Três, dois, um…"
- **Use quando:** a dor é desorganização/falta de informação (a pessoa não sabe a resposta). A
  participação (tentar responder) prende até o fim da contagem.

## 4. Foto do celular + prejuízo
- **Visual:** foto realista do objeto dentro de uma moldura de câmera de celular, flash do disparo;
  etiqueta de preço bate em cima; número do prejuízo em vermelho pulsando ("+R$ 7 mil").
- **Som:** clique de câmera + caixa registradora seguida de arranhão de disco.
- **Fala:** "Esse HB20 entrou na troca por 62 mil. A FIPE? 54.900."
- **Use quando:** a dor é uma decisão de compra/avaliação mal feita.

## 5. Pergunta incômoda com objeto
- **Visual:** objeto (carro) entra, carimbo "VENDIDO" bate com tremida, "?" gigante balançando.
- **Som:** impacto + whoosh.
- **Fala:** "Esse carro vendido por 85 mil… deu lucro mesmo?"

## 6. Chamado de identidade
- **Visual:** texto grande com o público ("LOJISTA QUE AVALIA TROCA NO OLHO") sobre a cena do pátio;
  a palavra-chave pisca em destaque.
- **Som:** impacto grave seco.
- **Fala:** "Lojista que avalia troca no olho: essa conta é pra você."
- **Use quando:** público frio; ensina o algoritmo para quem entregar.

## 7. Resultado como isca
- **Visual:** a tela real do produto já com o número final ("Lucro líquido R$ 5.850") dá zoom; o
  número pisca; aparece a lacuna: "de onde sumiram os outros 4 mil?".
- **Som:** whoosh + "ding" de revelação.
- **Fala:** "Esse carro deu 10 mil de lucro. Só que não."
- **Use quando:** você quer marca e produto no primeiro segundo sem fechar a curiosidade — o "como"
  só vem depois da virada.

## 8. Resposta a comentário (nativo)
- **Visual:** balão no estilo de comentário do Instagram ("Como eu sei o lucro de cada carro?"),
  depois a cena. Parece conteúdo, não propaganda.
- **Som:** pop.
- **Fala:** "Me perguntaram como saber o lucro real de cada carro. Olha."
- **Use quando:** quer um hook nativo de baixa resistência; ótimo em anúncio para público frio.

## Ideias ainda não usadas (para variar)
- **Contraintuitivo:** "Vender mais carro pode estar diminuindo seu lucro."
- **Mito × verdade:** "Mito: FIPE é o preço da troca."
- **"3 erros":** "3 erros que todo lojista comete na troca."
- **Contagem de dinheiro ao contrário:** contador de R$ descendo rápido.
- **Tela rachando:** print de planilha/caderno trincando com som de vidro.
- **"POV:" de humor:** "POV: o cliente pergunta o km e você vai olhar no carro".
- **Comparação lado a lado:** loja A (bagunça) × loja B (organizada) com placar.
- **Nativo:** post-it, bloco de notas, print de conversa genérica (sem marca de terceiros).
- **Rosto:** foto realista de um lojista olhando para o celular com o número (requer imagem gerada).

## Regras
- O **quadro 0 já é legível**: o objeto/texto principal aparece visível desde o primeiro quadro e
  anima a partir dali (punch, zoom). Nada de logo, fade-in ou tela vazia antes — o quadro 0 vira capa
  e miniatura.
- A fala começa em até 0,9 s. Se houver efeito sonoro, a fala entra logo depois do pico dele.
- A frase do hook tem até ~10 palavras e um elemento concreto (número, objeto, cena).
- Perguntas em "você" valem; afirmar a perda ou o erro de quem assiste não (ver
  `references/copywriting.md`).
- Interface simulada (notificação, câmera, chat) fica dentro de um celular ou balão, nunca imitando um
  botão ou alerta clicável do sistema.
