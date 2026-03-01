# Threat Hunting Case Study 01  
## Hypothesis-Based Hunt: Suspicious PowerShell Activity

---

# 🔹 Objective

Conduct proactive threat hunting to identify potentially malicious PowerShell execution that may bypass traditional alert-based detection.

This hunt is hypothesis-driven and aligned with MITRE ATT&CK.

---

# 🔹 Hunting Hypothesis

"If an attacker gains initial access, they may use encoded PowerShell commands to execute malicious payloads."

---

# 🔹 Log Sources Used

- Windows Security Logs
- PowerShell Operational Logs
- Process Creation Logs
- SIEM Correlation Search

---

# 🔹 Hunting Methodology

## Step 1: Identify Encoded PowerShell Usage

Search for:

- "-EncodedCommand"
- Base64 strings
- Suspicious command-line arguments

Example logic (conceptual):

index=windows process_name="powershell.exe" AND command_line="*EncodedCommand*"

---

## Step 2: Parent Process Analysis

Investigate:

- Was PowerShell launched by:
  - Word?
  - Excel?
  - Browser?
  - Unknown process?

Abnormal parent processes increase suspicion level.

---

## Step 3: Network Activity Correlation

Check if PowerShell execution triggered:

- Outbound connections
- DNS queries
- Suspicious IP communication

---

## Step 4: Account Context Validation

Validate:

- User account executing PowerShell
- Time of execution (business hours vs off-hours)
- Administrative privileges involved

---

# 🔹 MITRE ATT&CK Mapping

- T1059.001 – PowerShell
- T1027 – Obfuscated/Encoded Files or Information
- T1105 – Ingress Tool Transfer

Framework: MITRE ATT&CK

---

# 🔹 Findings

In this lab simulation:

- Encoded PowerShell command detected
- Executed by local administrator account
- Triggered outbound network connection
- Occurred outside business hours

---

# 🔹 Conclusion

The activity was classified as malicious simulation due to:

- Encoded command usage
- Suspicious parent process
- Outbound traffic correlation
- Time anomaly

Severity: HIGH

---

# 🔹 False Positive Considerations

- IT automation scripts
- Software deployment tools
- Admin remote maintenance

Proper validation required before escalation.

---

# 🔹 Lessons Learned

- Not all PowerShell is malicious
- Context determines threat level
- Parent process analysis is critical
- Correlation across logs increases confidence

---

# 🔹 Skills Demonstrated

✔ Hypothesis-based hunting  
✔ Cross-log correlation  
✔ Behavior analysis  
✔ MITRE mapping  
✔ Contextual investigation  

---

# 🔹 Future Hunting Expansions

Planned hunts:

- Lateral movement via SMB anomaly
- Suspicious service creation hunt
- DNS tunneling behavior detection
- Abnormal login time analysis
- Large outbound data transfer hunt
