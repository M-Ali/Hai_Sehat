# app/ui/cli.py

from app.core.safety import handle_query_safety
from app.core.model import generate_educational_response
from app.config import APP_NAME, DISCLAIMER, SCOPE_STATEMENT


def run_cli():
    print("=" * 60)
    print(f"{APP_NAME} — Health Education Assistant")
    print(SCOPE_STATEMENT)
    print("=" * 60)

    while True:
        user_input = input("\nEnter your question (or type 'exit' to quit): ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("\nThank you for using SehatSathi.")
            break

        is_safe, result = handle_query_safety(user_input)

        print("\n--- Response ---")

        if not is_safe:
            # Unsafe query → refusal message
            print(result)
        else:
            # Safe query → pass to model layer (stub for now)
            response = generate_educational_response(result)
            print(response)

        print("\n--- Disclaimer ---")
        print(DISCLAIMER)


if __name__ == "__main__":
    run_cli()