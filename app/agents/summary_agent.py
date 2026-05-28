from datetime import datetime


def generate_family_summary(notes: str, family_name: str = "Family") -> str:
    """
    Generates a simple, human‑readable weekly summary.
    """

    intro = f"Dear {family_name},\n\nHere is a brief summary of this week’s care:\n\n"
    body = notes.strip()
    outro = (
        "\n\nIf you have any questions or would like to discuss the care plan further, "
        "please contact the care team.\n\nWarm regards,\nCareFlow AI"
    )

    return intro + body + outro
