# Simple rule-based analysis (Simulating an AI Agent)
def analyze_logs(filename):
    suspicious_keywords = ['password', 'login', 'bank', 'credit card', 'admin']
    
    print(f"--- Analyzing {filename} for threats ---")
    
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
            # Count triggers
            risk_score = 0
            found_threats = []
            
            for word in suspicious_keywords:
                if word in content:
                    risk_score += 10
                    found_threats.append(word)
            
            print(f"Risk Score: {risk_score}/100")
            if risk_score > 0:
                print(f"⚠️  ALERT: Suspicious keywords detected: {found_threats}")
            else:
                print("✅ No immediate threats detected.")
                
    except FileNotFoundError:
        print("Log file not found. Run the monitor script first.")

if __name__ == "__main__":
    analyze_logs("app_log.txt")