def calculate_governance_risk(system):
    risk_score = 0

    # Rule 1 — Low model confidence
    # Aturan 1 — Confidence model AI rendah
    if system["model_confidence"] < 0.70:
        # Add 20 risk points
        # Tambahkan 20 poin risiko
        risk_score += 20

    # Rule 2 — Sensitive data processing
    # Aturan 2 — Sistem memproses data sensitif
    if system["sensitive_data"] == True:
        # Add 20 risk points
        # Tambahkan 20 poin risiko
        risk_score += 20

    return risk_score