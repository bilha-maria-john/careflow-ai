from datetime import datetime


def generate_visit_report(caregiver_name: str, client_name: str, notes: str) -> dict:
    """
    Very simple heuristic 'AI‑like' logic for demo.
    In a real app, this would call an LLM.
    """

    lower = notes.lower()

    medication_taken = "yes" if "took medication" in lower or "meds taken" in lower else "unclear"
    appetite = "reduced" if "half" in lower or "ate little" in lower else "normal/unclear"
    swelling = "present" if "swelling" in lower else "not mentioned"
    mood = "low" if "mood low" in lower or "sad" in lower else "not mentioned"

    red_flags = []
    if swelling == "present":
        red_flags.append("Swelling observed – monitor and consider escalation.")
    if mood == "low":
        red_flags.append("Low mood – consider mental health or social support check‑in.")

    return {
        "type": "visit_report",
        "timestamp": datetime.utcnow().isoformat(),
        "caregiver": caregiver_name,
        "client": client_name,
        "raw_notes": notes,
        "structured": {
            "medication_taken": medication_taken,
            "appetite": appetite,
            "swelling": swelling,
            "mood": mood,
        },
        "red_flags": red_flags,
        "recommended_actions": [
            "Review red flags and decide if nurse/clinician follow‑up is required.",
            "Log this visit in the client’s care record.",
        ],
    }
