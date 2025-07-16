# 🔐 Password Strength & Policy Tester (Burp Suite Powered)

A simple but powerful cybersecurity tool to test password strength and policy compliance using intercepted HTTP login requests from **Burp Suite**.  
Ideal for penetration testers and developers auditing password policies in web applications.

---

## 🚀 Features

- ✅ Parses raw HTTP login requests from Burp Suite
- ✅ Extracts password and target URL automatically
- ✅ Performs detailed strength analysis:
  - Length check
  - Uppercase/lowercase/digit/special char checks
- ✅ Flags weak or commonly used passwords
- ✅ Generates strong password suggestions
- ✅ Saves full analysis in numbered log reports

---

## 📂 Project Structure

password-policy-tester/
├── password_tester.py          # Password analysis
├── wordlist.txt                # some commonly used password
├── requirements.txt            #Prerequisites for project
├── README.md                   # explains projects
└── logs/                       # saves report



---

📖 Step-by-Step Guide (For README)

## 📖 How to Use This Project (Step-by-Step)

Follow these simple steps to test password strength using intercepted login requests:

---

### 🔹 Step 1: Clone or Download the Project

```bash
git clone https://github.com/yourusername/password-policy-tester.git
cd password-policy-tester


---

🔹 Step 2: Intercept a Login Request with Burp Suite

1. Open Burp Suite → Go to Proxy > Intercept → Make sure Intercept is ON.


2. Open any web app with a login form (e.g., DVWA, test page).


3. Enter any credentials and click login.


4. In Burp, right-click the intercepted request → Copy to file or Copy raw request.


5. Paste it into a file named request.txt inside the project folder.



> 📌 Make sure the request includes something like password=... in the body.




---

🔹 Step 3: Run the Python Script

python3 password_tester.py

The script will:

Read the intercepted request

Automatically extract the password and URL

Check if the password follows good security practices

Suggest 3 strong passwords if the input is weak

Save a full report in a logs/log_1.txt, log_2.txt, etc.




---

🔹 Step 4: View the Report

Open the generated log file:

cat logs/log_1.txt

You will see a complete analysis like this:

Password Analyzed: test123

🔍 Strength Check:
- Length >= 8: ❌
- Uppercase: ❌
- Lowercase: ✅
- Number: ✅
- Special Character: ❌

🏁 Final Verdict: ❌ Weak Password

💡 Suggested Strong Passwords:
- Ab7!xLp90Qt#
- Tr3$Zmn42Kp@
- Gp#Lk7Wyq@8%


---

✅ That's It!

You've now tested a password from a real intercepted login request and generated a detailed cybersecurity report.
You can repeat this with different intercepted requests and passwords.
