from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_quiz(text: str) -> str:
    """
    Tozalangan text qabul qiladi,
    10 ta quizni JSON formatda qaytaradi
    """

    with open("prompts/quiz_prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{{TEXT}}", text[:6000])  # token safety

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        max_output_tokens=1200
    )

    return response.output_text
