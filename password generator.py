import string
import secrets

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    # Base set includes lowercase letters
    char_set = string.ascii_lowercase
    if use_upper:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_special:
        char_set += string.punctuation

    if not char_set:
        print("Error: No characters selected, defaulting to lowercase letters.")
        char_set = string.ascii_lowercase
    
    password = ''.join(secrets.choice(char_set) for _ in range(length))
    return password

def password_strength(pw):
    length = len(pw)
    categories = sum([
        any(c.islower() for c in pw),
        any(c.isupper() for c in pw),
        any(c.isdigit() for c in pw),
        any(c in string.punctuation for c in pw)
    ])
    score = length + categories * 5
    if score < 15:
        return "Weak"
    elif score < 25:
        return "Moderate"
    else:
        return "Strong"

def main():
    print("==== Python Password Generator ====")
    length = int(input("Enter password length (e.g. 12): "))

    print("\nInclude character types? (y/n)")
    use_upper = input("Uppercase letters? ").lower() == 'y'
    use_digits = input("Digits? ").lower() == 'y'
    use_special = input("Special characters? ").lower() == 'y'

    pw = generate_password(length, use_upper, use_digits, use_special)

    print("\nGenerated password:", pw)
    print("Password strength:", password_strength(pw))

if __name__ == "__main__":
    main()