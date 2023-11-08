# Define a function named 'main'
def main():
    # Prompt the user to enter a CamelCase string and store it in 'camelCase'
    camelCase = input("CamelCase: ")
    
    # Print "SnakeCase: " without a newline character
    print("SnakeCase: ", end="")

    # Iterate through each letter in the CamelCase string
    for letter in camelCase:
        # Check if the letter is uppercase
        if letter.isupper():
            # If it's uppercase, print an underscore followed by the lowercase letter
            print("_" + letter.lower(), end="")
        else: 
            # If it's not uppercase, print the letter as is
            print(letter, end="")

    # Print a newline character to move to the next line
    print()

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if the script is executed as the main program
    main()
