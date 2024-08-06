# Creating a counter for input chances and setting the user password
counter = 3
password = "Jimmy"

# Loop for validating user input-password by comparing to set-password
while True:
    input_psswd = input("Welcome to BubbleOS! Enter your password to continue: ")
    if input_psswd == password:
        print("Welcome Jimmy!")
        # stop if the same
        break
    elif input_psswd != password:
        print("Incorrect Password")
        # Decrease the amount of choices and let the user know how many chances they have left
        counter = counter - 1
        print(f"Number of chances left: {counter}")
        if counter == 0:
            print("Incorrect password...try again later")
            # Stop everything if correct a third time
            break
