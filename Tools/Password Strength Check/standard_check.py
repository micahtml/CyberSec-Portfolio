import re
from getpass import getpass
import zxcvbn
import bcrypt
import json
import datetime


def load_password_policy():
    # Load password policy from a configuration file or database
    with open("D:\CyberSec-Portfolio\Tools\Password Strength Check\password_policy.json") as file:
        return json.load(file)


def check_password_strength(password):
    result = zxcvbn.zxcvbn(password)
    score = result['score']
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


def check_password_requirements(password, policy):
    errors = []

    # Check for uppercase letter
    if not re.search(r"[A-Z]", password):
        errors.append("Password must include an uppercase letter.")

    # Check for lowercase letter
    if not re.search(r"[a-z]", password):
        errors.append("Password must include a lowercase letter.")

    # Check for digit
    if not re.search(r"\d", password):
        errors.append("Password must include a digit.")

    # Check for special character
    if not re.search(r"\W", password):
        errors.append("Password must include a special character.")

    # Check for minimum number of unique characters
    if len(set(password)) < policy["min_unique_chars"]:
        errors.append(f"Password must include at least {policy['min_unique_chars']} unique character(s).")

    # Check for disallowed patterns
    if policy["disallowed_patterns"] and any(re.search(pattern, password) for pattern in policy["disallowed_patterns"]):
        errors.append("Password contains a disallowed pattern.")

    return errors


def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def verify_password(password, hashed_password):
    # Verify the password against the hashed password
    return bcrypt.checkpw(password.encode(), hashed_password)


def check_password_expiry(last_password_change, max_password_age):
    # Check if the password has expired based on the maximum password age
    expiry_date = last_password_change + datetime.timedelta(days=max_password_age)
    current_date = datetime.datetime.now()
    return current_date > expiry_date


# Example usage
password = getpass("Enter your password: ")

policy = load_password_policy()

requirements_errors = check_password_requirements(password, policy)
if requirements_errors:
    print("Password does not meet the following requirements:")
    for error in requirements_errors:
        print("- " + error)
else:
    password_strength = check_password_strength(password)
    rating = rate_password_strength(password_strength)
    print("Password Strength: " + rating)

hashed_password = hash_password(password)
print("Hashed Password:", hashed_password)

# Verify a password against a hashed password
is_valid = verify_password(password, hashed_password)
print("Password Verification:", is_valid)

# Example password expiry check
last_password_change = datetime.datetime(2022, 1, 1)  # Example last password change date
max_password_age = 90  # Example maximum password age in days

if check_password_expiry(last_password_change, max_password_age):
    print("Password has expired. Please change your password.")
else:
    print("Password is within the valid period.")
