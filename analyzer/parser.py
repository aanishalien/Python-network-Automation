import re
from collections import defaultdict

def parse_failed_attempts(log_path):
    failed_attempts = defaultdict(int)

    pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")



    with open(log_path,"r") as log_file:
        for line in log_file:
            match = pattern.search(line)
            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1

    print("Failed Attempts:",dict(failed_attempts))

    threshold = 1
    suspicious_ips = {ip: count for ip, count in failed_attempts.items() if count >= threshold}


    print("Suspicious IPs:", suspicious_ips)

    with open("rules.txt","w") as rule_file:
        for ip in suspicious_ips:
            rule_file.write(f"utw deny from {ip}\n")

    print("Rules generated in: rules.txt")


    return failed_attempts

    

    