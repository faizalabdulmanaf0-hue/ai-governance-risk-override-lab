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

    # Rule 3 — Bias detected
    # Aturan 3 — Bias terdeteksi pada sistem AI
    if system["bias_detected"] == True:
        # Add 20 risk points
        # Tambahkan 20 poin risiko
        risk_score += 20

    # Rule 4 — No human oversight
    # Aturan 4 — Tidak ada pengawasan manusia
    if system["human_oversight"] == False:
        # Add 25 risk points
        # Tambahkan 25 poin risiko
        risk_score += 25

    return risk_score

    # Rule 5 — High-impact decision
    # Aturan 5 — Sistem mengambil keputusan yang berdampak tinggi
    if system["high_impact_decision"] == True:
        # Add 15 risk points
        # Tambahkan 15 poin risiko
        risk_score += 15