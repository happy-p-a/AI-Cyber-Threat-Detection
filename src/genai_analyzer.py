import os
from typing import Dict, Optional

from groq import Groq


DEFAULT_MODEL = "openai/gpt-oss-120b"


def get_groq_client() -> Optional[Groq]:
    """Create a Groq client when an API key is available."""

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    return Groq(api_key=api_key)


def generate_threat_analysis(
    prediction: str,
    confidence: float,
    total_flows: int,
    threat_flows: int,
    benign_flows: int,
    top_threats: Dict[str, int],
    top_features: Optional[Dict[str, float]] = None,
) -> str:
    """
    Generate a human-readable cybersecurity analysis.

    Random Forest performs the detection.
    Generative AI explains the detection results.
    """

    client = get_groq_client()

    if client is None:
        return (
            "Generative AI analysis is unavailable.\n\n"
            "GROQ_API_KEY has not been configured."
        )

    threat_percentage = 0.0

    if total_flows > 0:
        threat_percentage = (
            threat_flows / total_flows
        ) * 100

    threat_distribution = ", ".join(
        f"{name}: {count}"
        for name, count in top_threats.items()
    )

    feature_information = "Not available"

    if top_features:
        feature_information = ", ".join(
            f"{name}: {value:.4f}"
            for name, value in top_features.items()
        )

    prompt = f"""
You are a cybersecurity threat-analysis assistant.

The machine-learning model has already classified the
network traffic.

Do not change the machine-learning prediction.

Do not invent IP addresses, malware names, vulnerabilities,
network events, or evidence that was not provided.

Clearly distinguish between observed model results and
recommended defensive actions.

Machine-learning results:

Predicted attack class:
{prediction}

Model confidence:
{confidence:.2f}%

Total network flows:
{total_flows}

Threat flows:
{threat_flows}

Benign flows:
{benign_flows}

Threat percentage:
{threat_percentage:.2f}%

Threat distribution:
{threat_distribution}

Important model features:
{feature_information}

Generate the following sections:

1. Threat Assessment
2. Evidence From Model Results
3. Risk Level
4. Recommended Defensive Actions
5. Limitations

Keep the response concise and suitable for a BTech
cybersecurity project demonstration.
"""

    try:
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a cybersecurity analysis "
                        "assistant. Explain machine-learning "
                        "results without changing the original "
                        "prediction."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
            max_completion_tokens=800,
        )

        return response.choices[0].message.content

    except Exception as exc:
        return (
            "Generative AI analysis could not be generated.\n\n"
            f"Technical error: {exc}"
        )