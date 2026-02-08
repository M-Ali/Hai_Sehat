# app/config.py

APP_NAME = "SehatSathi"
APP_MODE = "Health Education Only"

# Core disclaimer shown in all responses
DISCLAIMER = (
    "This information is provided for general health education only. "
    "It is not medical advice and should not be used for diagnosis, "
    "treatment, or emergency care. Please consult a qualified healthcare professional."
)

# Tone guidelines for all responses
RESPONSE_STYLE = {
    "language": "plain",
    "tone": "calm",
    "avoid_urgency": True,
    "avoid_medical_authority": True,
}

# Hard limits
MAX_INPUT_LENGTH = 1000
MAX_OUTPUT_LENGTH = 500

# Scope statement (used in UI / logs / write-up)
SCOPE_STATEMENT = (
    "SehatSathi is designed to support NGOs with general health education "
    "and awareness. It does not provide clinical decisions or personalized medical advice."
)