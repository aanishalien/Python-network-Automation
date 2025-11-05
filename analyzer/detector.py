def detect_suspicious_ips(failed_attempts, threshold=3):
    suspicious = {}

    for ip, count in failed_attempts.items():
        if count >= threshold:
            suspicious[ip] = count
    return suspicious