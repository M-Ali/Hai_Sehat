# app/core/model.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from app.core.postprocess import postprocess_response

MODEL_NAME = "google/gemma-2-2b-it"

# Lazy-loaded global model (loaded once)
_tokenizer = None
_model = None


def _load_model():
    """
    Load MedGemma model and tokenizer locally (CPU-only).
    This is done once per session.
    """
    global _tokenizer, _model

    if _tokenizer is None or _model is None:
        _tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True
        )

        _model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            device_map="cpu",
            torch_dtype=torch.float32,
            trust_remote_code=True
        )

        _model.eval()


def generate_educational_response(user_query: str) -> str:
    """
    Generate a health education response using MedGemma.
    Safety and scope are enforced BEFORE this function is called.
    """

    _load_model()

    prompt = (
        "You are a health education assistant supporting NGOs.\n"
        "Provide general, non-diagnostic health information only.\n"
        "Do not give medical advice, diagnosis, or treatment.\n\n"
        f"Question: {user_query}\n\n"
        "Educational response:"
    )

    inputs = _tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = _model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=False,
            temperature=0.0
        )

    raw_text = _tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Remove the prompt part if echoed
    if "Educational response:" in raw_text:
        raw_text = raw_text.split("Educational response:", 1)[-1]

    return postprocess_response(raw_text.strip())