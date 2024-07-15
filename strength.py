import re
import getpass

def check_password_strength(password):
    # Define the criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate the strength
    strength = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Determine the strength level
    if strength == 5:
        strength_text = 'Very Strong'
    elif strength >= 4:
        strength_text = 'Strong'
    elif strength >= 3:
        strength_text = 'Fair'
    else:
        strength_text = 'Weak'

    # Provide feedback
    feedback = f"""
    Password Strength: {strength_text}
    Criteria:
    - Length (8+ characters): {"✔️" if length_criteria else "❌"}
    - Uppercase Letter: {"✔️" if uppercase_criteria else "❌"}
    - Lowercase Letter: {"✔️" if lowercase_criteria else "❌"}
    - Number: {"✔️" if number_criteria else "❌"}
    - Special Character: {"✔️" if special_char_criteria else "❌"}
    """
    return feedback


password = getpass.getpass("Enter your password: ")
reveal_password = input("Would you like to reveal the entered password? (yes/no): ").strip().lower()

if reveal_password == 'yes':
    print(f"Entered Password: {password}")

feedback = check_password_strength(password)
print(feedback)

