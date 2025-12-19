import subprocess, json, textwrap
from ai_reasoning.prompt_templates import sales_prompt

OLLAMA_PATH = r"C:\Users\ASUS\AppData\Local\Programs\Ollama\ollama.exe"
MODEL = "phi3:mini"   # ✅ you have this installed

def run_ollama(prompt: str) -> str:
    result = subprocess.run(
        [OLLAMA_PATH, "run", MODEL],
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="ignore"
    )
    return result.stdout.strip()

def analyze_customer(customer_text: str) -> dict:
    prompt = sales_prompt(customer_text)
    output = run_ollama(prompt)

    try:
        json_text = output[output.find("{"): output.rfind("}") + 1]
        return json.loads(json_text)
    except:
        return {
            "sentiment": {"label": "unknown", "score": 0},
            "intent": "unknown",
            "entities": {},
            "ai_reply": "Could you please clarify?",
            "next_questions": [],
            "objection_handling": "",
            "product_recommendation": ""
        }
