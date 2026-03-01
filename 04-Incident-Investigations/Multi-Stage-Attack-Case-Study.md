# Advanced Incident Investigation  
## Case Study: Multi-Stage Attack Simulation

---

# 🔹 Executive Summary

A multi-stage attack was simulated within the SOC lab environment to replicate real-world attacker behavior. The attack chain included reconnaissance, brute force attempts, privilege escalation, and persistence establishment.

The objective was to investigate correlated alerts, validate attacker progression, and assess impact using L2-level investigation methodology.

---

# 🔹 Attack Timeline Overview

| Stage | Technique | Evidence |
|--------|-----------|----------|
| 1 | Port Scan | High connection attempts from single IP |
| 2 | Brute Force | Multiple Event ID 4625 failures |
| 3 | Privilege Escalation | Event ID 4672 triggered |
| 4 | Persistence | Service creation (Event ID 7045) |

---

# 🔹 Stage 1: Reconnaissance (Port Scan)

## Observed Activity
High number of connection attempts across multiple ports from a single IP.

## Log Source
Firewall / Network Logs

## Investigation Steps
1. Verified source IP consistency
2. Checked ASN and geolocation
3. Reviewed baseline traffic comparison

## MITRE Mapping
- T1046 – Network Service Scanning
- MITRE ATT&CK Framework

---

# 🔹 Stage 2: Brute Force Attempt

## Observed Activity
Multiple failed login attempts against Windows machine.

## Log Evidence
- Event ID 4625 (Failed Login)
- Same source IP as port scan

## Analysis
- 15 failed attempts within 5 minutes
- Target account: Local Administrator

## L2 Validation
- Checked if login eventually succeeded (Event ID 4624)
- Correlated with prior reconnaissance stage

## MITRE Mapping
- T1110 – Brute Force

---

# 🔹 Stage 3: Privilege Escalation

## Observed Activity
Special privileges assigned after successful login.

## Log Evidence
- Event ID 4672

## Analysis
- Account granted admin privileges
- Login occurred shortly after brute force attempts

## Correlation Finding
Indicates attacker gained valid access.

## MITRE Mapping
- T1078 – Valid Accounts
- T1068 – Privilege Escalation

---

# 🔹 Stage 4: Persistence Establishment

## Observed Activity
New service installed on system.

## Log Evidence
- Event ID 7045

## Analysis
- Service created under suspicious name
- Occurred within 10 minutes of privilege escalation

## Impact Assessment
Potential long-term backdoor access.

## MITRE Mapping
- T1543 – Create or Modify System Process

---

# 🔹 Correlation Analysis

All stages originated from the same IP address within 30-minute window.

Attack progression pattern:

Recon → Access Attempt → Access Success → Persistence

This confirms multi-stage compromise simulation.

---

# 🔹 Indicators of Compromise (IOCs)

- Source IP: 192.168.56.10
- Target Account: Administrator
- Suspicious Service Name: UpdateHelperService
- Time Window: 30 minutes

---

# 🔹 Impact Assessment

- Unauthorized administrative access
- Persistence mechanism established
- Potential full system compromise

Risk Level: HIGH

---

# 🔹 Containment & Remediation

- Disabled compromised account
- Removed malicious service
- Reset administrator password
- Blocked attacker IP at firewall
- Implemented account lockout policy

---

# 🔹 Lessons Learned

- Single alerts do not show full attack story
- Correlation across logs is critical
- Threshold tuning improves detection speed
- Early reconnaissance detection can prevent compromise

---

# 🔹 L2-Level Investigation Skills Demonstrated

✔ Multi-source log correlation  
✔ Timeline reconstruction  
✔ MITRE ATT&CK mapping  
✔ Root cause validation  
✔ Business impact assessment  
✔ Remediation recommendation  

---

# 🔹 Future Improvements

- Add automated correlation rule
- Implement threshold-based chaining alerts
- Deploy advanced PowerShell logging
- Add threat intelligence auto-enrichment
