from datetime import datetime


def suggest_schedule_adjustment(current_schedule: str, constraints: str = "") -> dict:
    """
    Very lightweight 'AI‑style' suggestion engine.
    """

    suggestions = []

    text = (current_schedule + " " + constraints).lower()

    if "conflict" in text or "double" in text:
        suggestions.append(
            "Detected mention of conflicts. Consider reassigning overlapping visits to another caregiver."
        )
    if "cannot work" in text or "unavailable" in text:
        suggestions.append(
            "Detected availability constraints. Ensure those days are removed from that caregiver’s rota."
        )
    if "daily" in text or "every day" in text:
        suggestions.append(
            "Some clients require daily visits. Prioritise them in morning slots and lock them first."
        )

    if not suggestions:
        suggestions.append(
            "No explicit issues detected in the text. Consider running a full rota optimisation in a future version."
        )

    return {
        "type": "schedule_suggestion",
        "timestamp": datetime.utcnow().isoformat(),
        "input_schedule": current_schedule,
        "constraints": constraints,
        "suggestions": suggestions,
    }
