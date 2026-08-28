# AI Governance Risk Override Analysis Lab

A Python-based security research project for analyzing AI governance risk through rule-based risk scoring and critical-condition detection.

## Objective

The project evaluates governance risks associated with AI systems using multiple security and governance indicators.

The engine analyzes:

- Model confidence
- Sensitive data processing
- Bias detection
- Human oversight
- High-impact decisions

The goal is to demonstrate how multiple governance risk factors can be translated into a structured risk assessment.

## Risk Scoring

| Risk Indicator | Score |
|---|---:|
| Model confidence below 70% | +20 |
| Sensitive data processing | +20 |
| Bias detected | +20 |
| No human oversight | +25 |
| High-impact decision | +15 |

The maximum risk score is capped at 100.

## Risk Classification

| Risk Score | Level |
|---:|---|
| 0–29 | LOW |
| 30–59 | MEDIUM |
| 60–79 | HIGH |
| 80–100 | CRITICAL |

## Critical Governance Condition

The project separately detects a critical governance condition when all three conditions are present:

```text
Sensitive data
      +
No human oversight
      +
High-impact decision
      ↓
Critical condition detected
```

This condition is analyzed separately from the numerical risk score.

## Example Scenario

Example AI system:

```text
Model confidence: 0.60
Sensitive data: TRUE
Bias detected: TRUE
Human oversight: FALSE
High-impact decision: TRUE
```

Risk calculation:

```text
Low model confidence       +20
Sensitive data             +20
Bias detected              +20
No human oversight         +25
High-impact decision       +15
                           ---
                            100
```

Result:

```text
Risk Score: 100
Risk Level: CRITICAL
```

## Testing

The project includes an automated test using `pytest` to verify the governance risk calculation.

The test checks whether a high-risk governance scenario produces the expected score of `100`.

Run the tests with:

```bash
python -m pytest
```

## Continuous Integration

GitHub Actions automatically runs the test suite when changes are pushed to the repository.

The test suite is validated through automated CI.

## Security Research Focus

This project focuses on the relationship between AI system characteristics and governance risk.

The analysis demonstrates how security and governance indicators can be converted into structured risk scores and severity levels.

The project also separates numerical risk scoring from critical governance condition detection.

## Limitations

This is an educational security research project.

The risk weights and thresholds are illustrative and should not be treated as universal AI governance standards.

The engine does not represent a complete production AI governance framework or regulatory compliance assessment.

## Technologies

- Python
- pytest
- GitHub Actions

## Security Workflow

```text
AI System
    ↓
Risk Indicators
    ↓
Risk Scoring
    ↓
Risk Classification
    ↓
Critical Condition Detection
    ↓
Automated Testing
    ↓
CI Validation
```