import logging

# Configure logging
logging.basicConfig(filename='password_strength_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')


# Function to evaluate password strength
def check_password_strength(password):
    # Criteria checks
    is_length_valid = len(password) >= 8
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special_char = any(c in "!@#$%^&*()_+[]{}|;:,.<>?/`~" for c in password)

    # Determine the strength based on the checks
    if is_length_valid and has_uppercase and has_lowercase and has_number and has_special_char:
        strength = 'Strong'
    elif is_length_valid and (has_uppercase or has_lowercase) and (has_number or has_special_char):
        strength = 'Moderate'
    else:
        strength = 'Weak'

    # Provide feedback
    feedback = {
        "length_valid": is_length_valid,
        "uppercase": has_uppercase,
        "lowercase": has_lowercase,
        "number": has_number,
        "special_char": has_special_char,
        "strength": strength
    }

    # Log the result
    logging.info(f"Password: {password} | Strength: {strength} | Criteria: {feedback}")

    return feedback


# Main function to take password input and evaluate
def main():
    password = input("Enter a password to evaluate its strength: ")
    feedback = check_password_strength(password)

    print(f"Password Strength: {feedback['strength']}")
    if feedback['strength'] == 'Weak':
        print(
            "Password is weak. Make sure it has at least 8 characters, an uppercase letter, a lowercase letter, a number, and a special character.")
    elif feedback['strength'] == 'Moderate':
        print("Password is moderate. Try to make it stronger by adding more diverse character types.")
    else:
        print("Password is strong. Good job!")


if __name__ == "__main__":
    main()
