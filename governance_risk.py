def calculate_governance_risk(system):
    risk_score = 0

    # Rule 1 — Low model confidence
    if system["model_confidence"] < 0.70:
        risk_score += 20

    # Rule 2 — Sensitive data processing
    if system["sensitive_data"] is True:
        risk_score += 20

    # Rule 3 — Bias detected
    if system["bias_detected"] is True:
        risk_score += 20

def detect_critical_condition(system):
    # Detect a critical governance condition
    if (
        system["sensitive_data"] is True
        and system["human_oversight"] is False
        and system["high_impact_decision"] is True
    ):
        return True

    return False

    # Rule 4 — No human oversight
    if system["human_oversight"] is False:
        risk_score += 25

    # Rule 5 — High-impact decision
    if system["high_impact_decision"] is True:
        risk_score += 15

    # Return the final risk score
    return min(risk_score, 100)


def classify_governance_risk(risk_score):
    # Classify the risk score
    if risk_score >= 80:
        return "CRITICAL"
    elif risk_score >= 60:
        return "HIGH"
    elif risk_score >= 30:
        return "MEDIUM"
    else:
        return "LOW"

def assess_governance(system):
    # Calculate the governance risk score
    risk_score = calculate_governance_risk(system)

    # Classify the risk level
    risk_level = classify_governance_risk(risk_score)

    return {
        "risk_score": risk_score,
        "risk_level": risk_level
    }