import re
import tkinter as tk


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


def check_password_requirements(password):
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

    return errors


def check_password():
    password = entry.get()

    requirements_errors = check_password_requirements(password)
    if requirements_errors:
        error_text = "Password does not meet the following requirements:\n"
        for error in requirements_errors:
            error_text += "- " + error + "\n"
        result_label.config(text=error_text)
    else:
        password_strength = check_password_strength(password)
        rating = rate_password_strength(password_strength)
        result_label.config(text="Password Strength: " + rating)


# Create the main window
window = tk.Tk()
window.title("Password Strength Checker")

# Create and place the password entry field
entry = tk.Entry(window, width=30, show="*")
entry.pack(pady=10)

# Create and place the check button
check_button = tk.Button(window, text="Check Password", command=check_password)
check_button.pack()

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the main GUI event loop
window.mainloop()
