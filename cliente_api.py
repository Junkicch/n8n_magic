import requests
import json

URL_WEBHOOK = "https://n8n.incluc0de.com.br/webhook-test/chat-agente"

def consultar_juiz_mtg(pergunta: str, session_id: str = "app-externo-python"):
    payload = {
        "sessionId": session_id,
        "pergunta": pergunta
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    print(f"Enviando pergunta ao MTG Virtual Judge: '{pergunta}'...\n")
    response = requests.post(URL_WEBHOOK, json=payload, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    resultado = consultar_juiz_mtg(
        pergunta="Como funciona a Zona de Comando e a taxa de comandante?",
        session_id="teste-ea2-001"
    )
    print("=== RESPOSTA DA API (JSON) ===")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))