# Define a function named 'main'
def main():
    # Prompt the user for input and store it in the 'response' variable
    response = input("What time is it? ")
    
    # Call the 'convert' function to convert the user's input to a numeric value
    time = convert(response)

    # Check if 'time' falls within specific time ranges and print corresponding messages
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")

# Define a function named 'convert' to convert a time string into a numeric value
def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")
    
    # Convert minutes to a fraction of an hour and add it to the hours
    new_minutes = float(minutes) / 60
    
    # Return the total time as a floating-point number
    return float(hours) + new_minutes

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the 'main' function if the script is executed as the main program
    main()
