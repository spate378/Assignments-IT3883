# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Shiv Patel
# Assignment Number: 1
# Due Date: 09/05/2025
# Purpose: Write a python program which applies a text based menu that gives users 4 choices. The 4 choices are to append the data, clearing the input buffer, displaying the input buffer, and exiting the program.
# Resources: Module slides 1-1, 1-2, and Lecture videos

UserText = ""

# Print a menu for user
while True:
    print("\n--- Text Based Menu ---")
    print("1. Save data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Collect the user input
    userInput = input("Select an option from menu (1-4): ")

    # 1: Save data to the input buffer
    if userInput == "1":
        saveData = input("Please enter text you would like to save:  ")
        UserText += saveData
        print("Your input has been successfully saved in the program. ")

    # 2: Clear the input buffer
    elif userInput == "2":
        UserText = ""
        print("Your input has been cleared.")

    # 3: Display the input buffer
    elif userInput == "3":
        if UserText:
            print("Your currently saved input: ", UserText)
        # Inform the user if there no saved input
        else:
            print("There are currently no saved texts. Please visit option #1 on the menu and enter a text to be saved.")

    # 4: Exit the program
    elif userInput == "4":
        print("You have now exited the program.")
        # Exit the loop
        break

    # Print an error message in case user enters a value outside of 1-4
    else:
        print("Invalid choice. Please select an option between 1 and 4. ")
