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
    print(f"\nGenerated password: {password}")

    save = input("Would you like to save this password to a file? (y/n): ").lower()
    if save == 'y':
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")
        print("Password saved to passwords.txt")               

if __name__ == "__main__":
    main()   
