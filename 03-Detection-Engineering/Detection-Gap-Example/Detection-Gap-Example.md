# Detection Gap Analysis Example

## Current Detection Coverage

✔ Brute Force
✔ Privilege Escalation
✔ DNS DDoS

## Missing Coverage

✖ No detection for lateral movement via SMB
✖ No detection for persistence via registry run keys

## Improvement Plan

- Add detection for Event ID 7045 (Service Creation)
- Monitor registry modification logs
- Add SMB session anomaly detection

## Objective
Improve coverage across MITRE ATT&CK matrix.
