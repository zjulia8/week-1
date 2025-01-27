#BMI group project 

def calculate_bmi(weight_pounds, height_feet, height_inches):
    # Convert height to inches
    total_height_inches = (height_feet * 12) + height_inches

    # Calculate BMI using the formula: BMI = (weight in pounds / (height in inches)^2) * 703
    bmi = (weight_pounds / (total_height_inches ** 2)) * 703

    return bmi

def get_bmi_category(bmi):
    # Determine the BMI category based on the BMI value
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def display_bmi_legend():
    # Display BMI category ranges based on WHO recommendations
    print("\nBMI Category Ranges (Source: World Health Organization):")
    print(" Underweight: BMI < 18.5")
    print(" Normal weight: 18.5 <= BMI < 24.9")
    print(" Overweight: 25 <= BMI < 29.9")
    print(" Obese: BMI >= 30")

def main():
    # Ask the user for their weight and height
    print("Welcome to the BMI Calculator!")
    weight_pounds = float(input("Enter your weight in pounds: "))
    height_feet = int(input("Enter your height (feet): "))
    height_inches = int(input("Enter your height (inches): "))

    # Calculate BMI
    bmi = calculate_bmi(weight_pounds, height_feet, height_inches)

    # Get the BMI category
    bmi_category = get_bmi_category(bmi)

    # Display the result
    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"You are classified as: {bmi_category}")

    # Display the BMI category ranges (legend)
    display_bmi_legend()

# Run the program
if __name__ == "__main__":
    main()

# Elvina Shaimukhametova, Annika Singh, Julia Zurek