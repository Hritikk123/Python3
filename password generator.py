import random
import string

def generate_password(length):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired length of the password: "))
        
        # Check if length is valid
        if length <= 0:
            print("Password length must be a positive integer.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print("Generated password:", password)
        
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()


