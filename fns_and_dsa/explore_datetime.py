from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the current date and time
    print(f"Current date and time: {formatted_current_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt the user to enter the number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date by adding the number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date in "YYYY-MM-DD" format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

# Main function to run the script
def main():
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()

