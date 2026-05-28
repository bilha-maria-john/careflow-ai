from datetime import datetime


def generate_incident_report(notes: str) -> dict:
    """
    Simple incident report generator.
    """

    lower = notes.lower()
    incident_type = "fall" if "fall" in lower or "fell" in lower else "general incident"

    severity = "high" if "hospital" in lower or "bleeding" in lower else "medium"
    if "minor" in lower or "no injury" in lower:
        severity = "low"

    return {
        "type": "incident_report",
        "timestamp": datetime.utcnow().isoformat(),
        "incident_type": incident_type,
        "description": notes,
        "severity": severity,
        "recommended_actions": [
            "Document incident in official log.",
            "Notify supervisor and family if required.",
            "Review care plan and risk assessment.",
        ],
    }


def generate_medication_log(notes: str) -> dict:
    """
    Simple medication log generator.
    """

    lower = notes.lower()
    missed = "missed" in lower or "skipped" in lower
    delayed = "delayed" in lower or "late" in lower

    status = "taken as prescribed"
    if missed and delayed:
        status = "missed and delayed doses"
    elif missed:
        status = "missed dose(s)"
    elif delayed:
        status = "delayed dose(s)"

    return {
        "type": "medication_log",
        "timestamp": datetime.utcnow().isoformat(),
        "raw_notes": notes,
        "status": status,
        "flags": [
            "Review medication adherence with caregiver and client.",
            "Consider reminder system or medication support tools.",
        ]
        if (missed or delayed)
        else [],
    }
