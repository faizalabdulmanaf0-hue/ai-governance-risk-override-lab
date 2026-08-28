def calculate_governance_risk(system):
    risk_score = 0

    # Rule 1 — Low model confidence
    if system["model_confidence"] < 0.70:
        risk_score += 20

    return risk_score