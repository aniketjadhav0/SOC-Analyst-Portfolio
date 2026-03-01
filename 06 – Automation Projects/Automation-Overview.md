# SOC Automation Projects  
## Improving Analyst Efficiency Through Scripting

---

# 🔹 Objective

The purpose of this section is to demonstrate automation skills that improve SOC operations by reducing manual effort, speeding up investigation, and summarizing security data.

Even simple automation significantly enhances operational efficiency in real-world SOC environments.

---

# 🔹 Automation Project 01  
## Failed Login Analyzer

### Purpose
Automatically analyze Windows Security logs and count failed login attempts to quickly identify potential brute-force activity.

### Problem (Manual Process)
- Analyst manually checks logs
- Counts failed attempts
- Correlates IP addresses
- Time-consuming and repetitive

### Automated Solution
A Python script that:
- Parses log file
- Extracts failed login entries
- Counts occurrences per IP
- Displays suspicious IPs above threshold

### SOC Benefit
- Faster triage
- Reduces manual counting
- Improves detection speed
- Helps identify brute-force patterns

---

# 🔹 Future Automation Plans

- IOC Extractor (auto-extract IPs, hashes, domains from logs)
- Alert Summary Generator
- Threat Intelligence Enrichment Script
- Suspicious Account Activity Reporter
- Automated MITRE Technique Tagging
- SOAR-style automated response simulation

---

# 🔹 Long-Term Automation Goal

Transition from:
Manual investigation support

To:
Semi-automated SOC workflow enhancement

This builds foundation toward Detection Engineering and Security Automation roles.
