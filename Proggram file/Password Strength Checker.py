import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc).")

    # Determine strength
    if score == 5:
        strength = "Very Strong 💪"
    elif score >= 4:
        strength = "Strong ✅"
    elif score >= 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, feedback

# --- Example Usage ---
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for f in feedback:
            print("-", f)
