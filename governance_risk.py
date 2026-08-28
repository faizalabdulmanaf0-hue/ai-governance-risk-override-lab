def calculate_governance_risk(system):
    risk_score = 0

    # Rule 1 — Low model confidence
    # Aturan 1 — Confidence model AI rendah
    if system["model_confidence"] < 0.70:
        risk_score += 20

    # Rule 2 — Sensitive data processing
    # Aturan 2 — Sistem memproses data sensitif
    if system["sensitive_data"] == True:
        risk_score += 20

    # Rule 3 — Bias detected
    # Aturan 3 — Bias terdeteksi
    if system["bias_detected"] == True:
        risk_score += 20

    # Rule 4 — No human oversight
    # Aturan 4 — Tidak ada pengawasan manusia
    if system["human_oversight"] == False:
        risk_score += 25

    # Rule 5 — High-impact decision
    # Aturan 5 — Keputusan berdampak tinggi
    if system["high_impact_decision"] == True:
        risk_score += 15

    # Return the final risk score
    # Mengembalikan skor risiko akhir
    return min(risk_score, 100)