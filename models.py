from pydantic import BaseModel

class UserInput(BaseModel):
    input_text: str


class WebsiteSuggestion(BaseModel):
    template_name: str
    layout: str
    homepage_content: str
