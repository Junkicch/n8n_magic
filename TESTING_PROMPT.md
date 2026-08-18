# Documentação, Testes e Avaliação da Comunicação do Agente de IA

> **Projeto:** ManaBot — Agente de Suporte e Informações de *Magic: The Gathering* (MTG)  
> **Plataforma:** n8n (Node `AI Agent`)  
> **Repositório:** `Junkicch/n8n_magic`  

---

## 1. Comunicação Esperada

A tabela a seguir descreve os padrões de comunicação e o comportamento esperado do **ManaBot** diante das diferentes situações de interação com os usuários (jogadores de MTG):

| Situação | Comunicação Esperada |
| :--- | :--- |
| **Dúvida sobre regras e interações de cartas** | O agente responde de forma direta se a jogada é válida ou não, detalhando a mecânica envolvida (fases do turno, pilha de prioridade, etc.) de maneira didática. |
| **Mecanismo ou conceito técnico (ex: A pilha, Necro-habilidade)** | O agente explica o conceito passo a passo usando listas numeradas, com linguagem acessível a iniciantes e analogias quando apropriado. |
| **Solicitação com informações insuficientes** | O agente não tenta adivinhar o cenário completo; em vez disso, solicita educadamente os detalhes faltantes (ex: quais cartas exatas estão em campo). |
| **Solicitação fora do domínio de MTG** | O agente recusa educadamente o atendimento e reafirma sua função exclusiva de suporte ao jogo *Magic: The Gathering*. |
| **Continuando uma conversa anterior (Uso de memória)** | O agente mantém o contexto da conversa e reconhece referências relativas a cartas ou formatos citados em mensagens anteriores. |
| **Incerteza sobre interações muito complexas/específicas** | O agente fornece a interpretação padrão das regras vigentes e sugere a consulta formal a um *Judge* (juiz) para eventos sancionados. |
| **Pergunta sobre valores monetários de cartas** | O agente esclarece que não fornece cotações em tempo real e indica plataformas de mercado confiáveis (ex: LigaMagic, TCGPlayer). |

---

## 2. Casos de Teste

Definimos 7 casos de teste que contemplam cenários de sucesso, cenários com dados incompletos, uso de contexto, limites do System Message e solicitações fora do domínio.

---

### CT01 — Resolução de dúvida direta sobre interações de regras
- **Identificação:** CT01
- **Objetivo:** Verificar se o agente analisa uma interação entre duas cartas clássicas e responde de forma clara e assertiva sobre a validade da jogada.
- **Contexto:** Um jogador em dúvida sobre se a habilidade de **Tramplay** (*Trample*) ultrapassa a proteção de **Inviolabilidade** / **Proteção contra o Branco**.
- **Entrada do usuário:**  
  `Se eu atacar com uma criatura 6/6 com Tramplay e o oponente bloquear com uma criatura 1/1 que tem Proteção contra a cor da minha criatura, quanto de dano passa para o jogador?`
- **Comportamento esperado:**  
  O agente deve explicar que a criatura atacante precisa atribuir dano letal (1 de dano) à criatura bloqueadora (mesmo que o dano seja prevenido pela proteção) e que o restante (5 de dano) é atribuído ao jogador defensor.
- **Critério de sucesso:**  
  - Declarar o valor correto de dano que passa (5 de dano).
  - Explicar a regra de atribuição de dano de *Trample* vs *Protection*.
  - Usar formatação em **negrito** nas palavras-chave e nomes de mecânicas.

---

### CT02 — Explicação didática de mecânica complexa (A Pilha)
- **Identificação:** CT02
- **Objetivo:** Verificar se o agente consegue explicar uma das regras mais fundamentais e complexas do jogo de maneira estruturada e didática para um novato.
- **Contexto:** Um jogador iniciante quer entender como funciona a ordem de resolução de magias instântaneas (*Instants*).
- **Entrada do usuário:**  
  `Sou iniciante e não entendi direito como funciona 'A Pilha' no Magic. Você pode me explicar de um jeito simples?`
- **Comportamento esperado:**  
  O agente deve usar o conceito LIFO (*Last In, First Out* / "Último a entrar, primeiro a sair"), apresentar uma analogia didática (ex: pilha de pratos ou cartas) e listar o passo a passo com números.
- **Critério de sucesso:**  
  - Apresentar o conceito de "Último a entrar, primeiro a sair".
  - Usar uma lista numerada para o fluxo de resolução.
  - Manter um tom paciente e encorajador.

---

### CT03 — Tratamento de mensagem com informação insuficiente
- **Identificação:** CT03
- **Objetivo:** Verificar se o agente solicita os detalhes necessários em vez de inventar ou presumir o estado do jogo.
- **Contexto:** O jogador pergunta se uma jogada é válida sem nomear as cartas ou o formato que está jogando.
- **Entrada do usuário:**  
  `Minha criatura morre se ele usar aquela mágica de destruir na fase de combate?`
- **Comportamento esperado:**  
  O agente deve reconhecer a ambiguidade da pergunta e pedir esclarecimentos (quais são as cartas envolvidas, se a criatura tem alguma habilidade como Indestrutível, Hexproof, etc.).
- **Critério de sucesso:**  
  - Não dar uma resposta definitiva de "sim" ou "não".
  - Fazer perguntas objetivas para obter os nomes das cartas e detalhes do cenário.

---

### CT04 — Solicitação fora do domínio (Boundary Testing)
- **Identificação:** CT04
- **Objetivo:** Verificar se o agente respeita o escopo fechado definido no System Message.
- **Contexto:** O usuário tenta usar o agente para resolver um problema fora do jogo MTG.
- **Entrada do usuário:**  
  `Você pode me ajudar a montar um deck de Pokémon TCG com o Charizard ex?`
- **Comportamento esperado:**  
  O agente deve recusar a resposta de maneira cortês, informando que seu foco exclusivo é o universo de *Magic: The Gathering*.
- **Critério de sucesso:**  
  - Não fornecer nenhuma lista ou dica sobre Pokémon TCG.
  - Reafirmar educadamente sua identidade como assistente de *Magic: The Gathering*.

---

### CT05 — Uso de contexto e memória da conversa
- **Identificação:** CT05
- **Objetivo:** Verificar se o agente utiliza as mensagens anteriores para manter a continuidade do atendimento.
- **Contexto:** O usuário faz perguntas sequenciais utilizando pronomes ou referências relativas a uma carta citada anteriormente.
- **Entrada 1:** `Qual o efeito da carta Sol Ring?`  
- **Entrada 2:** `Ela é permitida no formato Standard?`
- **Comportamento esperado:**  
  Ao receber a Entrada 2, o agente deve entender que "Ela" se refere à carta **Sol Ring** citada na Entrada 1 e responder que ela **não é legal no Standard** (mas é um pilar do Commander).
- **Critério de sucesso:**  
  - Identificar a referência a **Sol Ring** sem que o usuário precise repetir o nome da carta.
  - Informar corretamente a legalidade da carta no formato Standard.

---

### CT06 — Restrição de cotação de preços / mercado
- **Identificação:** CT06
- **Objetivo:** Avaliar a aderência à regra do System Message sobre não fornecer preços em tempo real de cartas.
- **Contexto:** O usuário quer saber o valor financeiro de uma carta no mercado atual.
- **Entrada do usuário:**  
  `Quanto está custando uma Black Lotus Alpha hoje em dia?`
- **Comportamento esperado:**  
  O agente deve esclarecer que não realiza cotações ou avaliações de mercado em tempo real e indicar plataformas especializadas de negociação.
- **Critério de sucesso:**  
  - Recusar-se a cravar um valor numérico exato ou desatualizado.
  - Recomendar sites como LigaMagic, TCGPlayer ou Cardmarket.

---

### CT07 — Orientação sobre formatos do jogo (Commander)
- **Identificação:** CT07
- **Objetivo:** Testar se o agente orienta corretamente sobre regras específicas de montagem de deck em um formato específico.
- **Contexto:** Um jogador quer construir seu primeiro deck de Commander (EDH).
- **Entrada do usuário:**  
  `Quais são as regras básicas para montar um deck de Commander? Posso usar duas cópias da mesma carta?`
- **Comportamento esperado:**  
  O agente deve explicar as regras do formato: 100 cartas exatas, presença de 1 Comandante, identidade de cor e regra de *Singleton* (máximo de 1 cópia de cada carta, exceto terrenos básicos).
- **Critério de sucesso:**  
  - Responder diretamente sobre a proibição de duplicadas (regra de cópia única).
  - Citar a restrição de 100 cartas e a identidade de cor do Comandante.

---

## 3. Registro e Classificação dos Resultados

Abaixo estão os resultados obtidos após a execução de cada caso de teste diretamente no nó do **AI Agent** no n8n:

| Caso | Entrada | Resultado Esperado | Resultado Obtido | Classificação |
| :--- | :--- | :--- | :--- | :--- |
| **CT01** | *Pergunta sobre Trample vs Proteção* | Informar que 5 de dano passam e 1 é prevenido. | O agente explicou com precisão a atribuição de dano letal a criaturas com proteção e confirmou os 5 de dano no jogador. | **Atendido** |
| **CT02** | *Explicação sobre A Pilha* | Explicação simples com LIFO e lista numerada. | O agente usou a metáfora de uma "pilha de pratos", dividiu em etapas numeradas e destacou os termos técnicos em negrito. | **Atendido** |
| **CT03** | *'Minha criatura morre se...' (Incompleto)* | Solicitar os nomes das cartas e detalhes. | O agente identificou a falta de informações e perguntou os nomes da mágica, da criatura e o estado do campo. | **Atendido** |
| **CT04** | *Pergunta sobre Pokémon TCG* | Recusar e redirecionar para MTG. | O agente respondeu: "Sou o ManaBot, especializado exclusivamente em Magic: The Gathering. Não consigo te ajudar com Pokémon TCG..." | **Atendido** |
| **CT05** | *'Ela é permitida no Standard?' (Contexto)* | Entender que 'Ela' é o Sol Ring e responder sobre legalidade. | O agente manteve o contexto, respondeu que o **Sol Ring** não é válido no Standard e citou onde é banido/permitido. | **Atendido** |
| **CT06** | *Pergunta sobre preço da Black Lotus* | Recusar a cotação e indicar sites especializados. | O agente afirmou que é a carta mais valiosa do jogo, mas indicou que não dá cotações e sugeriu consultar a LigaMagic/TCGPlayer. | **Atendido** |
| **CT07** | *Regras do formato Commander* | Explicar regra de 100 cartas, cópia única e Comandante. | O agente explicou todas as regras e destacou que **não** é permitido usar duas cópias da mesma carta. | **Atendido** |

---

## 4. Análise dos Resultados

Com **100% dos testes classificados como "Atendido"**, o **ManaBot** demonstrou alta fidelidade ao **System Message** elaborado na atividade anterior:

1. **Aderência ao Escopo:** O agente manteve suas fronteiras muito bem delimitadas no **CT04**, recusando prontamente temas fora do ecossistema de *Magic: The Gathering*.
2. **Capacidade Didática:** No **CT02**, a estruturação das respostas em tópicos e a linguagem adaptada para iniciantes garantiram que a explicação sobre a pilha fosse clara e compreensível.
3. **Gerenciamento de Contexto e Memória:** O node do n8n configurado com memória de conversa respondeu perfeitamente ao **CT05**, mantendo o rastro de entidades previamente mencionadas (**Sol Ring**).
4. **Tratamento de Dados Incompletos:** No **CT03**, o agente não "alucinou" nem assumiu um cenário arbitrário; atuou ativamente fazendo perguntas investigativas ao jogador.

---

## 5. Melhorias Propostas e Próximos Passos

Mesmo com todos os casos de teste atendidos, identificamos oportunidades de evolução técnica e funcional para as próximas etapas do projeto no n8n:

1. **Integração com API do Scryfall (Tools no n8n):**
   - *Oportunidade:* Embora o agente conheça as regras gerais e cartas famosas, o uso da LLM pura pode gerar ambiguidades para cartas muito recentes ou regras lançadas nas coleções mais atuais.
   - *Ação:* Conectar um nó de **Tool / API Call** ao `AI Agent` do n8n consumindo a API pública do **Scryfall** para buscar o texto exato (*Oracle Text*) e *Rulings* oficiais em tempo real.

2. **Refinamento do Prompt para Tratamento de Erros de Grafia:**
   - *Oportunidade:* No **CT01**, o usuário digitou *"Tramplay"* em vez de *"Trample"* (Atropelar). O agente compreendeu por conta da semelhança fonética.
   - *Ação:* Adicionar uma orientação explícita no System Message para que o agente confirme/corrija suavemente a grafia de nomes de mecânicas e cartas quando identificar pequenos erros de digitação.

3. **Inclusão de Exemplos Few-Shot no System Message:**
   - *Oportunidade:* Para garantir que a formatação em negrito e listas numeradas sejam rigorosamente mantidas em todas as respostas curtas ou longas.
   - *Ação:* Incluir 1 ou 2 exemplos de diálogos de demonstração (*Few-shot prompting*) diretamente no campo System Message.
