from analyzer.parser import parse_failed_attempts
from analyzer.detector import detect_suspicious_ips
from analyzer.rule_engine import generate_block_rules

LOG_PATH ="logs/auth.log"

failed = parse_failed_attempts(LOG_PATH)
suspicious = detect_suspicious_ips(failed, threshold=3)
rules_file = generate_block_rules(suspicious)

print("Failed Attempts:", failed)
print("Suspicious IPs:", suspicious)
print(f"Rules generated in: {rules_file}")