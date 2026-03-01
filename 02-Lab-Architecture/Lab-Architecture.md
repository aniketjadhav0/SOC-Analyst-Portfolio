# SOC Home Lab Architecture  
## Advanced Blue Team Simulation Environment

---

## 🔹 Objective

This lab environment is designed to simulate real-world SOC operations including attack simulation, log collection, detection engineering, incident investigation, and threat hunting.  

The architecture replicates enterprise-style log flow and alert lifecycle for hands-on detection and response practice.

---

## 🔹 Lab Components Overview

### 🖥 Attacker Machine
- OS: Kali Linux
- Purpose: Simulate real-world attacks
- Activities:
  - Port scanning (Nmap)
  - Brute force attempts (SSH/RDP)
  - DDoS traffic simulation (DNS/SMB)
  - Exploitation testing
  - Suspicious PowerShell execution testing

---

### 🖥 Victim Machine
- OS: Windows 10
- Purpose: Generate logs for investigation
- Log Sources:
  - Windows Security Logs
  - System Logs
  - PowerShell Logs
  - Event ID monitoring (4625, 4672, etc.)

---

### 🧠 SIEM Platform
- Wazuh (Log Management & Alerting)
- Splunk (Correlation & Query-based detection)

Purpose:
- Centralized log collection
- Alert generation
- Correlation analysis
- Incident validation
- Detection rule tuning

---

## 🔹 Network Design

- Virtualization Platform: VirtualBox / VMware
- Network Mode: Host-Only / Internal Network
- Communication: All machines communicate within isolated lab environment

### Example IP Scheme

| Machine | IP Address | Role |
|----------|------------|------|
| Kali Linux | 192.168.56.10 | Attacker |
| Windows 10 | 192.168.56.20 | Victim |
| SIEM Server | 192.168.56.30 | Log Collector |

---

## 🔹 Log Flow Architecture

1. Attack initiated from Kali Linux
2. Windows machine generates security events
3. Wazuh Agent installed on Windows collects logs
4. Logs forwarded to Wazuh Manager
5. Alerts generated based on detection rules
6. Splunk used for advanced correlation queries
7. Analyst investigates and validates incident

---

## 🔹 Event Sources Configured

### Windows Security Events
- Event ID 4625 – Failed Login
- Event ID 4624 – Successful Login
- Event ID 4672 – Special Privileges Assigned
- Event ID 4720 – User Account Creation
- Event ID 7045 – Service Installation

### Network & Traffic Monitoring
- Port activity monitoring
- DNS traffic observation (UDP 53)
- SMB traffic monitoring (Port 445)
- Outbound suspicious traffic analysis

---

## 🔹 Detection Simulation Scenarios

The lab supports simulation of:

- DNS-based DDoS attack (UDP 53 flood)
- SMB-based DDoS attack (Port 445 spike)
- SSH/RDP brute force attempts
- Suspicious PowerShell encoded command execution
- Malware execution detection (EDR telemetry simulation)
- Suspicious outbound botnet-like traffic behavior

Each simulation is followed by:
- Log correlation
- MITRE ATT&CK mapping
- False positive analysis
- Incident documentation

---

## 🔹 Alert Lifecycle Model (SOC Workflow Simulation)

1. Alert Generated (SIEM)
2. Initial Triage (L1 Simulation)
3. Log Correlation (L2 Investigation)
4. IOC Enrichment
5. Impact Assessment
6. Escalation (if required)
7. Documentation & Closure

---

## 🔹 Detection Engineering Approach

For each simulated attack:

- Detection rule logic is documented
- Threshold conditions defined
- False positive scenarios analyzed
- Tuning adjustments recorded
- MITRE ATT&CK technique mapped

This helps simulate real SOC L2 responsibilities.

---

## 🔹 Security Controls Simulated

- Firewall traffic inspection
- IDS/IPS alert validation
- EDR telemetry investigation
- Email security alert review
- Threat intelligence enrichment (IP/ASN/TOR lookup)

---

## 🔹 Lab Limitations (Transparency Section)

- Isolated environment (not full enterprise scale)
- Simulated attack patterns
- Limited endpoint count
- No real production traffic

---

## 🔹 Future Lab Expansion Plan

Planned upgrades:

- Sysmon advanced logging integration
- Linux log ingestion
- Centralized multi-source correlation
- Sigma rule testing
- Cloud log ingestion (AWS / Azure)
- Automated alert summarization scripts
- SOAR-style workflow automation

---

## 🔹 Purpose of This Lab

This environment is designed not just for L1 monitoring practice but for:

- Advanced investigation
- Log correlation
- Detection tuning
- False positive reduction
- Multi-stage attack analysis
- SOC L2 readiness development
