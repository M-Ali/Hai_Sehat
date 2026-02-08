# app/core/postprocess.py

from app.config import DISCLAIMER, MAX_OUTPUT_LENGTH


def postprocess_response(text: str) -> str:
    """
    Final cleanup and safety normalization for model responses.
    Ensures calm tone, reasonable length, and consistent formatting.
    """

    if not text:
        return ""

    # Normalize whitespace
    cleaned = " ".join(text.split())

    # Enforce maximum length (defensive)
    if len(cleaned) > MAX_OUTPUT_LENGTH:
        cleaned = cleaned[:MAX_OUTPUT_LENGTH].rsplit(" ", 1)[0] + "..."

    # Avoid authoritative phrasing
    replacements = {
        "you should": "it is generally recommended to",
        "you must": "it may be important to",
        "this will": "this may",
        "always": "often",
        "never": "rarely",
    }

    lowered = cleaned.lower()
    for phrase, replacement in replacements.items():
        if phrase in lowered:
            cleaned = cleaned.replace(phrase, replacement)

    return cleaned