from openai import OpenAI
from config import OPENAI_API_KEY
import logging
from pathlib import Path

# ✅ LOGGING CONFIG (shuni qo‘shish shart)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

client = OpenAI(api_key=OPENAI_API_KEY)
PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "quiz_prompt.txt"


def generate_quiz(text: str) -> str:
    """
    Tozalangan text qabul qiladi,
    10 ta quizni JSON formatda qaytaradi
    """
    prompt_template = PROMPT_PATH.read_text(encoding="utf-8")
    prompt = prompt_template.replace("{{TEXT}}", text[:6000])
    logger.info(f"Generating quiz")
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        max_output_tokens=1200
    )

    return response.output_text
