import re


def check_password_strength(password):
    score = 0

    # Check the length of the password
    if len(password) >= 8:
        score += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check for digits
    if re.search(r"\d", password):
        score += 1

    # Check for special characters
    if re.search(r"\W", password):
        score += 1

    return score


def rate_password_strength(score):
    if score <= 1:
        return "Very Weak"
    elif score == 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"



# Example usage
password = input("Enter your password: ")
password_strength = check_password_strength(password)
rating = rate_password_strength(password_strength)
print("Password Strength: " + rating)
