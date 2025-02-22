#week4
def calculate_bmi(weight_pounds, height_feet, height_inches):
    """
    Calculates BMI using the formula: BMI = (weight in pounds / (height in inches)^2) * 703
    
    Parameters:
    weight_pounds (float): Weight of the person in pounds.
    height_feet (int): Height in feet.
    height_inches (int): Height in inches.
    
    Returns:
    float: The BMI of the person.
    """
    total_height_inches = (height_feet * 12) + height_inches
    bmi = (weight_pounds / (total_height_inches ** 2)) * 703
    return bmi


def get_bmi_category(bmi):
    """
    Determines the BMI category based on the BMI value.
    
    Parameters:
    bmi (float): The BMI of the person.
    
    Returns:
    str: The BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def display_bmi_legend():
    """
    Displays BMI category ranges based on WHO recommendations.
    """
    print("\nBMI Category Ranges (Source: World Health Organization):")
    print(" Underweight: BMI < 18.5")
    print(" Normal weight: 18.5 <= BMI < 24.9")
    print(" Overweight: 25 <= BMI < 29.9")
    print(" Obese: BMI >= 30")


def get_valid_input(prompt, value_type, min_value, max_value=None):
    """
    Ensures input is of correct type and within an acceptable range.
    Displays an error message on invalid input and keeps asking for valid input until received.
    
    Parameters:
    prompt (str): The message to display for user input.
    value_type (type): The type the input should be converted to (e.g., int, float).
    min_value (int/float): The minimum valid value.
    max_value (int/float, optional): The maximum valid value.
    
    Returns:
    The valid user input as the specified type.
    """
    while True:
        try:
            user_input = value_type(input(prompt))
            if user_input < min_value:  
                raise ValueError(f"Value must be at least {min_value}.")
            if max_value is not None and user_input > max_value:
                raise ValueError(f"Value must not exceed {max_value}.")
            return user_input
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def display_bmi_table():
    """
    Displays a BMI table with height from 58 to 76 inches in 2-inch increments and
    weight from 100 to 250 pounds in 10-pound increments.
    """
    print("\nBMI Table:")
    print("Height (inches) | Weight (pounds) | BMI")
    for height in range(58, 77, 2):  # Height from 58 to 76 inches, in 2-inch increments
        for weight in range(100, 251, 10):  # Weight from 100 to 250 pounds, in 10-pound increments
            bmi = calculate_bmi(weight, height // 12, height % 12)  # Convert height to feet/inches
            bmi_category = get_bmi_category(bmi)
            print(f"{height:<17} | {weight:<15} | {bmi:.1f} ({bmi_category})")


def main():
    """
    Main function to handle user input, exception handling, display results,
    and allow the user to choose whether to calculate BMI for another person
    or display the BMI table.
    """
    print("Welcome to the BMI Calculator!")
    
    while True:
        # Get user input with validation
        weight_pounds = get_valid_input("Enter your weight in pounds: ", float, 1, 1000)
        height_feet = get_valid_input("Enter your height (feet): ", int, 1, 8)
        height_inches = get_valid_input("Enter your height (inches): ", int, 0, 11)
        
        # Calculate BMI
        bmi = calculate_bmi(weight_pounds, height_feet, height_inches)
        bmi_category = get_bmi_category(bmi)
        
        # Display results
        print(f"\nYour BMI is: {bmi:.1f}")
        print(f"You are classified as: {bmi_category}")
        
        # Ask user if they want to calculate BMI again
        user_choice = input("\nWould you like to calculate BMI for another person? (Y/N): ").strip().lower()
        if user_choice != 'y':
            break
    
    # Ask if the user wants to display the BMI table
    show_table = input("\nWould you like to see a BMI table (height 58 to 76 inches and weight 100 to 250 pounds)? (Y/N): ").strip().lower()
    if show_table == 'y':
        display_bmi_table()

    # Display BMI legend
    display_bmi_legend()


if __name__ == "__main__":
    main()