from governance_risk import calculate_governance_risk


def test_critical_governance_risk():
    system = {
        "model_confidence": 0.60,
        "sensitive_data": True,
        "bias_detected": True,
        "human_oversight": False,
        "high_impact_decision": True
    }

    result = calculate_governance_risk(system)

    assert result == 100