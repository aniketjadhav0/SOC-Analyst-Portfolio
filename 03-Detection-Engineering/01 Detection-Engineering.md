# Detection Engineering Portfolio  
## SOC L2 – Alert Logic, Correlation & Rule Tuning

---

## 🔹 Objective

This section demonstrates practical detection engineering capabilities including rule creation, threshold logic, correlation design, false-positive reduction, and MITRE ATT&CK mapping.

The focus is not just alert monitoring, but improving detection quality and investigation depth.

---

# 🛡 Detection Case 1: Brute Force Attack (T1110)

## Scenario
Multiple failed login attempts detected against Windows system via RDP/SSH simulation.

## Log Source
- Windows Security Logs  
- Event ID 4625 (Failed Login)

## Detection Logic

- Count failed login attempts
- Threshold: 10 failed attempts within 5 minutes
- Same source IP or same target account

### Example Correlation Concept (Splunk-style logic)

index=security EventCode=4625
| stats count by src_ip, user
| where count > 10


## MITRE Mapping
- T1110 – Brute Force

## False Positive Considerations
- User forgetting password
- Misconfigured service authentication
- Password spray testing in internal lab

## Tuning Strategy
- Add time-window filtering
- Exclude internal vulnerability scan IPs
- Exclude service accounts

## Investigation Steps (L2 Level)
1. Validate source IP reputation
2. Check if login eventually succeeded (Event ID 4624)
3. Review privilege escalation attempts
4. Check lateral movement signs
5. Determine impact level

---

# 🛡 Detection Case 2: Suspicious PowerShell Execution

## Scenario
Encoded or suspicious PowerShell command execution detected.

## Log Source
- Windows PowerShell Logs
- Process Creation Logs

## Detection Indicators
- Use of "-EncodedCommand"
- Base64 patterns
- Unusual parent process
- Execution outside business hours

## MITRE Mapping
- T1059.001 – PowerShell

## False Positive Considerations
- Legitimate IT automation scripts
- Admin maintenance tasks

## Tuning Strategy
- Exclude known admin accounts
- Exclude signed scripts
- Validate command context

## L2 Investigation Approach
1. Decode PowerShell command
2. Check network connection logs
3. Validate file creation behavior
4. Check persistence mechanisms

---

# 🛡 Detection Case 3: Privilege Escalation Attempt

## Scenario
User account granted elevated privileges unexpectedly.

## Log Source
- Event ID 4672 (Special Privileges Assigned)
- Event ID 4728/4732 (Added to Security Group)

## Detection Logic
Monitor unexpected admin group additions.

## MITRE Mapping
- T1078 – Valid Accounts
- T1068 – Privilege Escalation

## False Positive Considerations
- Scheduled IT access changes
- Approved access request tickets

## Tuning Strategy
- Cross-check with change management logs
- Monitor after-hours privilege changes

## L2 Investigation Approach
1. Validate ticket approval
2. Check login source
3. Review prior suspicious activity
4. Assess potential lateral movement

---

# 🛡 Detection Case 4: DNS-Based DDoS Detection

## Scenario
Spike in UDP Port 53 traffic targeting internal DNS server.

## Log Source
- Firewall Logs
- Network Traffic Logs

## Detection Logic
- Traffic threshold spike detection
- High packet rate from single or multiple IPs
- Time-based anomaly

## MITRE Mapping
- T1498 – Network Denial of Service

## False Positive Considerations
- Legitimate traffic spike
- Patch/update servers
- Backup DNS synchronization

## Tuning Strategy
- Compare baseline traffic
- Add threshold smoothing
- Check geolocation patterns

## L2 Investigation Approach
1. Validate packet volume trend
2. Identify source ASN and reputation
3. Confirm service disruption
4. Recommend firewall rate limiting

---

# 🔹 Detection Engineering Principles Applied

- Log correlation across multiple sources
- Threshold-based detection
- Time-window analysis
- False positive reduction
- Contextual enrichment
- MITRE ATT&CK alignment

---

# 🔹 Future Detection Enhancements

Planned Improvements:

- Sigma rule creation
- Multi-stage attack correlation rules
- Lateral movement detection logic
- Persistence mechanism monitoring
- Data exfiltration pattern detection
- Cloud log detection (AWS CloudTrail / Azure AD)
- Detection coverage gap analysis

---

# 🔹 Goal

Transition from reactive alert handling (L1)  
To proactive detection tuning and advanced correlation (L2-level capability).
