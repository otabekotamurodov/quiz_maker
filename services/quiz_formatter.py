import json


def parse_quiz_json(quiz_json: str) -> list[dict]:
    quiz_json = quiz_json.strip()
    data = json.loads(quiz_json)

    if not isinstance(data, list):
        raise ValueError("Quiz JSON list bo‘lishi kerak")

    return data


def format_quiz_item(i: int, item: dict) -> str:
    q = item.get("question", "").strip()
    opts = item.get("options", {}) or {}
    a = opts.get("A", "").strip()
    b = opts.get("B", "").strip()
    c = opts.get("C", "").strip()
    d = opts.get("D", "").strip()

    # Correct answer hozircha userga ko'rsatmaymiz (xohlasangiz ko'rsatamiz)
    # correct = item.get("correct_answer")

    return (
        f"🧩 *Savol {i}*\n"
        f"{q}\n\n"
        f"A) {a}\n"
        f"B) {b}\n"
        f"C) {c}\n"
        f"D) {d}\n"
    )


def parse_quiz_json(quiz_json: str) -> list[dict]:
    """
    OpenAI ba'zida bosh/oxiriga whitespace qo'shadi.
    JSON bo'lmasa exception beradi.
    """
    quiz_json = quiz_json.strip()
    data = json.loads(quiz_json)

    if not isinstance(data, list):
        raise ValueError("Quiz JSON list bo‘lishi kerak")

    return data
