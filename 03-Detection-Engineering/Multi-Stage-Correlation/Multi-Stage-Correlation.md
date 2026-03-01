# Multi-Stage Attack Correlation Example

## Scenario
Detect if the same IP performs:

1. Port Scan
2. Brute Force
3. Privilege Escalation

## Correlation Logic

If:
- Port scan detected from IP X
AND
- More than 10 failed logins from IP X
AND
- Privileged login success occurs

Within 30 minutes

Then:
Trigger HIGH severity alert

## Purpose
Instead of detecting single alerts,
this detects attack chain behavior.

## MITRE Mapping
- T1046 – Network Service Scanning
- T1110 – Brute Force
- T1068 – Privilege Escalation
