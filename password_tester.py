import os
import re
import random
import string
from datetime import datetime

# -------------------------------
# Configuration
REQUEST_FILE = "request.txt"
LOG_DIR = "logs"
# -------------------------------

def is_strong(password):
    return (
        len(password) >= 8 and
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "!@#$%^&*()-_=+[{]}|;:',<.>/?`~" for c in password)
    )

def generate_strong_passwords(count=3):
    suggestions = []
    while len(suggestions) < count:
        pwd = ''.join(random.choices(
            string.ascii_letters + string.digits + "!@#$%^&*()", k=12
        ))
        if is_strong(pwd):
            suggestions.append(pwd)
    return suggestions

def extract_password_and_url(request_path):
    try:
        with open(request_path, "r") as f:
            raw = f.read()
    except FileNotFoundError:
        print("❌ Error: request.txt not found.")
        return None, None

    # Extract URL from request line
    first_line = raw.splitlines()[0]
    try:
        method, path, _ = first_line.split()
    except ValueError:
        return None, None

    # Extract Host header
    host_match = re.search(r"Host:\s*(.+)", raw)
    host = host_match.group(1).strip() if host_match else "localhost"
    url = f"http://{host}{path}"

    # Extract password from body
    body_match = re.search(r"\r?\n\r?\n(.+)", raw, re.DOTALL)
    if body_match:
        body = body_match.group(1)
        pwd_match = re.search(r"password=([^&\s]+)", body)
        password = pwd_match.group(1) if pwd_match else None
    else:
        password = None

    return url, password

def save_report(url, password, suggestions):
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

    existing_logs = [f for f in os.listdir(LOG_DIR) if f.startswith("log_") and f.endswith(".txt")]
    log_number = len(existing_logs) + 1
    log_filename = f"{LOG_DIR}/log_{log_number}.txt"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"""🛡️ Password Policy & Strength Report
Timestamp: {timestamp}
Target URL: {url}

Password Analyzed: {password}

🔍 Strength Check:
- Length >= 8: {"✅" if len(password) >= 8 else "❌"}
- Uppercase: {"✅" if any(c.isupper() for c in password) else "❌"}
- Lowercase: {"✅" if any(c.islower() for c in password) else "❌"}
- Number: {"✅" if any(c.isdigit() for c in password) else "❌"}
- Special Character: {"✅" if any(c in "!@#$%^&*()-_=+[{]}|;:',<.>/?`~" for c in password) else "❌"}

🏁 Final Verdict: {"✅ Strong Password" if is_strong(password) else "❌ Weak Password"}

💡 Suggested Strong Passwords:
- {suggestions[0]}
- {suggestions[1]}
- {suggestions[2]}
"""

    with open(log_filename, "w") as f:
        f.write(report)

    print(f"\n✅ Report saved to: {log_filename}")


# -------------------------------
# Main Execution
# -------------------------------
def main():
    print("🔐 Password Strength Tester (Burp Suite mode)\n")

    url, password = extract_password_and_url(REQUEST_FILE)

    if not url or not password:
        print("❌ Could not extract password or URL from request.txt.")
        return

    suggestions = generate_strong_passwords()
    save_report(url, password, suggestions)

if __name__ == "__main__":
    main()
