def main_part2():
    # Get input from the user
    num1 = float(input("Enter the first number (num1): "))
    num2 = float(input("Enter the second number (num2): "))

    # Check for division by zero
    if num2 == 0:
        print("Error: Division by zero!")
        return

    # Calculate multiplication and division
    multiplication = num1 * num2
    division = num1 / num2

    # Display the results
    print(f"\nThe multiplication of {num1} and {num2} is: {multiplication}")
    print(f"The division of {num1} by {num2} is: {division}")

if __name__ == "__main__":
    main_part2()