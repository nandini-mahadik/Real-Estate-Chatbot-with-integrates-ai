import os
from groq import Groq
from dotenv import load_dotenv
import time

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# You can override which model to try by setting GROQ_MODEL in .env
# Recommended: "mistral-saba-24b" or "mixtral-8x7b" (older short id)
DEFAULT_MODELS = [
    os.getenv("GROQ_MODEL", "mistral-saba-24b"),
    "mixtral-8x7b",            # try shorter id as a fallback
    "mixtral-8x7b-32768",     # last-resort (will likely fail if decommissioned)
]

client = Groq(api_key=GROQ_API_KEY)


def _try_create_completion(model: str, prompt: str):
    """Attempt a single Groq chat completion call; return result or raise."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert real estate analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=400,
    )
    return response


def create_ai_summary(prompt: str) -> str:
    """
    Generate a summary using Groq. Tries several model IDs (configurable via .env).
    Returns the text or an error string that is safe to show in the UI.
    """
    if not GROQ_API_KEY:
        return "[AI Summary Error: No Groq API key configured]"

    last_err = None
    for model in DEFAULT_MODELS:
        try:
            resp = _try_create_completion(model, prompt)
            # Response shape may vary slightly; handle both styles
            choice = resp.choices[0]
            if hasattr(choice, "message") and "content" in choice.message:
                text = choice.message["content"]
            elif hasattr(choice, "message") and hasattr(choice.message, "content"):
                text = choice.message.content
            else:
                # Try common dict access
                text = choice.get("message", {}).get("content", "")
            return text.strip()
        except Exception as e:
            # store the exception and try next model
            last_err = e
            # small delay to avoid rapid-fire quota problems
            time.sleep(0.2)
            continue

    # If we reach here, every model attempt failed
    return f"[AI Summary Error: All Groq models failed. Last error: {str(last_err)}]"
