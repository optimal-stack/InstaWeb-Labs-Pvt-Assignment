import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")
for m in genai.list_models():
    print(m.name)

def generate_website_suggestions(user_input: str) -> dict:
    prompt = f"""
    You are a website design assistant.
    Based on the following user input, suggest:
    1. A suitable website template name.
    2. Layout recommendation (1-page, multi-section, etc.).
    3. 2–3 lines of homepage content.

    User input: {user_input}
    """
    response = model.generate_content(prompt)

    text = response.text or ""
    lines = text.strip().split("\n")

    # Safely extract lines or use default fallback
    def safe_extract(index, label):
        try:
            return lines[index].split(":", 1)[1].strip()
        except (IndexError, ValueError):
            return f"Default {label}"

    return {
        "template_name": safe_extract(0, "Template"),
        "layout": safe_extract(1, "Layout"),
        "homepage_content": safe_extract(2, "Homepage content")
    }
