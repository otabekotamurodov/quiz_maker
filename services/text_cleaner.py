import re

def clean_text(text: str) -> str:
    """
    OpenAI uchun textni optimallashtiradi
    """
    # ortiqcha bo‘sh joylar
    text = re.sub(r"\s+", " ", text)

    # sahifa raqamlari (1, 2, - 3 -)
    text = re.sub(r"\b\d+\b", "", text)

    # keraksiz belgilar
    text = re.sub(r"[•●■]", "", text)

    return text.strip()
