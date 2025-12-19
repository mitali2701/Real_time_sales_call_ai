def sales_prompt(customer_text):
    return f"""
You are a professional Sales AI assistant.

Customer message:
"{customer_text}"

Return ONLY valid JSON:
{{
  "sentiment": {{
    "label": "positive | neutral | negative",
    "score": 0.0
  }},
  "intent": "",
  "entities": {{
    "product": [],
    "price": [],
    "feature": []
  }},
  "ai_reply": "",
  "next_questions": ["", "", ""],
  "objection_handling": "",
  "product_recommendation": ""
}}
"""
