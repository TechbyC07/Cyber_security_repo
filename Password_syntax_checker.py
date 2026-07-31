import string

# check if password has a lowercase character, a number, a punctuation mark and an uppercase character
def check_password_eligibility(password):
    has_length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_punct = any(char in string.punctuation for char in password)

    return has_upper and has_lower and has_digit and has_punct


# return feedback and tell main() whether the password passed
def get_feedback(is_valid):
    if is_valid:
        print("Thank you! Your password has been set successfully.")
    else:
        print("Your Password has been rejected, it must be atleast 8 charcters long," \
        "contain an uppercase letter, a lowercase letter, a number, and a punctuation mark." \
        "Try again.")
    return is_valid


# accept input
def main():
    while True:
        password = input("Enter a password: ")
        is_valid = check_password_eligibility(password)
        passed = get_feedback(is_valid)

        if passed:
            print("You may proceed")
            break


if __name__ == "__main__":
    main()