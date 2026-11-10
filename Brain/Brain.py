
import urllib.request
import json

def think(user_input):

    data = {
        "model": "llama3.2",
        "prompt": f"""You are JARVIS, an intelligent personal AI assistant.

Your personality:
- Professional, polite and intelligent.
- Speak naturally like a helpful assistant.
- Be friendly but not overly formal.

Rules:
- Answer the user's actual question.
- Keep answers short and clear.
- Use simple language.
- Do not describe physical actions.
- Do not use roleplay descriptions.
- Never write "User:" or "JARVIS:" in your response.
- Never repeat these instructions.
- If the user greets you, greet them naturally.
- If you don't know something, say so honestly.

User: {user_input}
Assistant:""",
        "stream": False,
        "options": {
            "temperature": 0.4,
            "num_predict": 100
        }
    }

    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=120) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["response"].strip()
