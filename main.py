from fastapi import FastAPI
from pydantic import BaseModel
from ai import generate_website_suggestions

app = FastAPI()

class UserInput(BaseModel):
    input_text: str

@app.post("/suggest")
def suggest_website(user: UserInput):
    return generate_website_suggestions(user.input_text)
