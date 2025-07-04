import google.generativeai as genai
import os
from dotenv import load_dotenv
import re
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")
for m in genai.list_models():
    print(m.name)


def generate_website_suggestions(user_input: str) -> dict:
    prompt = f"""
    You are a helpful assistant for a website builder platform.
    Given a user’s description of their website goal, respond ONLY in this format:

    Template: <Template Name>
    Layout: <Layout Recommendation>
    Homepage: <2–3 line homepage content>

    User input: {user_input}
    """

    response = model.generate_content(prompt)

    text = response.text or ""
    lines = text.strip().split("\n")

    # Safely extract lines or use default fallback
    def extract_field(lines, label, default):
        pattern = rf"{label}:\s*(.+)"
        for line in lines:
            match = re.match(pattern, line.strip(), re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return default

    return {
        "template_name": extract_field(lines, "Template", "Default Template"),
        "layout": extract_field(lines, "Layout", "Default Layout"),
        "homepage_content": extract_field(lines, "Homepage", "Default Homepage content")
    }

