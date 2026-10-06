# Especificação de Comunicação: MTG Virtual Judge como Serviço

## 1. Visão Geral
Este documento especifica a interface de comunicação HTTP (API) para o **MTG Virtual Judge**, nosso Agente de IA especialista em *Magic: The Gathering* construído no n8n. O objetivo é permitir que aplicações externas, especialmente **Bots do Telegram** ou clientes compatíveis, consumam o agente como um serviço independente.

**Função do Agente:** Atuar como um árbitro oficial e mentor experiente, explicando mecânicas, regras e interações de cartas.
**Integrações Nativas do Agente:** O agente consulta ativamente ferramentas externas para formular a resposta:
1. `consultar_carta_scryfall`: Para obter o Oracle Text atualizado de cartas.
2. `Supabase Vector Store`: Base de conhecimento para Comprehensive Rules, IPG, MTR, etc.

---

## 2. Operações e Rotas

| Método | Rota | Objetivo |
| :--- | :--- | :--- |
| **POST** | `/webhook/chat` | Enviar uma dúvida para o Juiz Virtual e receber a explicação formatada. |
| **GET** | `/webhook/health` | Verificar a disponibilidade do webhook no n8n. |

---

## 3. Estrutura das Requisições e Respostas

### 3.1. Envio de Mensagem (`POST /webhook/chat`)

**Contrato de Entrada (Requisição):**
*Formato:* `application/json`

| Campo | Tipo | Obrigatoriedade | Descrição |
| :--- | :--- | :--- | :--- |
| `message` | String | Obrigatório | O texto da dúvida do jogador. |
| `session_id` | String | Opcional | Identificador único da conversa. Mantém o contexto de cartas já citadas ou do andamento de uma partida. |

**Exemplo de Requisição:**
```json
{
  "message": "Se eu conjurar um Lightning Bolt numa criatura 3/3 e em resposta o oponente der Giant Growth nela, o que acontece?",
  "session_id": "telegram-chat-id-987654321"
}
```
**Exemplo de Resposta (Processada)**
```json
{
  "status": "success",
  "response_parts": [
    "A criatura sobreviverá e terminará o turno como 6/6 com 3 de dano marcado nela.\n\n<b>A Pilha e a Prioridade:</b>\nQuando o <i>Giant Growth</i> é conjurado em resposta, ele entra no topo da pilha, acima do <i>Lightning Bolt</i>. Portanto, ele resolve primeiro.\n\n<i>Fonte consultada:</i> Comprehensive Rules - The Stack (Section 405)"
  ],
  "session_id": "telegram-chat-id-987654321"
}
  "message": "Se eu conjurar um Lightning Bolt numa criatura 3/3 e em resposta o oponente der Giant Growth nela, o que acontece?",
  "session_id": "telegram-chat-id-987654321"
}
