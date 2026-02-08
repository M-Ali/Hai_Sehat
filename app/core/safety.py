# app/core/safety.py

from typing import Tuple

# Keywords that indicate unsafe medical intent
UNSAFE_KEYWORDS = [
    "diagnose",
    "diagnosis",
    "treatment",
    "medicine",
    "medication",
    "dose",
    "dosage",
    "prescribe",
    "emergency",
    "urgent",
    "heart attack",
    "stroke",
    "cancer",
    "surgery",
]

SAFE_REFUSAL_MESSAGE = (
    "I can help with general health education and information, "
    "but I cannot provide medical advice, diagnosis, or treatment. "
    "For personal medical concerns, please consult a qualified healthcare professional."
)


def is_safe_query(user_input: str) -> bool:
    """
    Check whether the user's query stays within
    general health education boundaries.
    """
    text = user_input.lower()
    return not any(keyword in text for keyword in UNSAFE_KEYWORDS)


def handle_query_safety(user_input: str) -> Tuple[bool, str]:
    """
    Returns:
    - (True, original_input) if safe
    - (False, refusal_message) if unsafe
    """
    if is_safe_query(user_input):
        return True, user_input

    return False, SAFE_REFUSAL_MESSAGE