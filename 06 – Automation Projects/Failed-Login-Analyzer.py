import re
from collections import defaultdict

# Path to exported Windows log file
log_file = "security_log.txt"

# Dictionary to store failed login count per IP
failed_logins = defaultdict(int)

# Regex pattern for failed login entries (Event ID 4625 simulation)
ip_pattern = re.compile(r"Source Network Address:\s*(\d+\.\d+\.\d+\.\d+)")

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        if "4625" in line:  # Failed login event
            match = ip_pattern.search(line)
            if match:
                ip = match.group(1)
                failed_logins[ip] += 1

print("\n--- Failed Login Summary ---\n")

threshold = 5  # Suspicious threshold

for ip, count in failed_logins.items():
    if count >= threshold:
        print(f"[ALERT] Suspicious IP: {ip} | Failed Attempts: {count}")

print("\nAnalysis Completed.\n")
