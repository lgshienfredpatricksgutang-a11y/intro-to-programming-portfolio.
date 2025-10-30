
# A very Simple password system

correct_password = "Sigma1230"

# welcome message

print("Welcome to the Sigma Secure System")

# This keeps asking for the password until the correct one is entered
while True:
    password = input("Please enter your Sigma password: ")
    
# Check if the entered password is correct
    if password == correct_password:
        print("Access Granted. Welcome Alpha!")
        break
    
# If the password is incorrect, inform the user
    else:
        print("Access Denied. Incorrect password, please try again.")

    


# Note: This is a simple demonstration and should not be used in real security systems.
