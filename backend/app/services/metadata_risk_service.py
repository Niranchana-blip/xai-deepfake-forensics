def analyze_metadata_risk(metadata):

    findings = []

    # Missing device information
    if "Make" not in metadata and "Model" not in metadata:
        findings.append("Camera/device information missing")

    # Editing software detected
    if "Software" in metadata:
        findings.append(
            f"Editing software detected: {metadata['Software']}"
        )

    # Determine risk level
    if len(findings) == 0:
        risk = "LOW"
    elif len(findings) <= 2:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return {
        "risk_level": risk,
        "findings": findings
    }