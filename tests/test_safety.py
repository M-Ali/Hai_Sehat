from app.core.safety import handle_query_safety

def test_safe_query():
    safe, _ = handle_query_safety("What is high blood pressure?")
    assert safe is True

def test_unsafe_query():
    safe, response = handle_query_safety("What medicine should I take for chest pain?")
    assert safe is False
    assert "cannot provide medical advice" in response