import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("This is a password generator.")
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print(f"\Generated password: {password}")

if __name__ == "__main__":
    main()   