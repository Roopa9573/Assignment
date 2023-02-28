import re

def is_password_safe(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if password contains only letters (lowercase and uppercase), numbers, and the specified symbols
    if not re.match(r'^[a-zA-Z0-9_@$]*$', password):
        return False

    # Check if password contains at least one uppercase letter, one number, and one symbol
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '_@$' for char in password):
        return False

    # If all checks passed, the password is safe
    return True

password = input("Enter your password: ")
if is_password_safe(password):
    print("Your password is safe.")
else:
    print("Your password is not safe.")




