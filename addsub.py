def main_part1():
    # Get input from the user
    num1 = float(input("Enter the first number (num1): "))
    num2 = float(input("Enter the second number (num2): "))

    # Calculate addition and subtraction
    addition = num1 + num2
    subtraction = num1 - num2

    # Display the results
    print(f"\nThe addition of {num1} and {num2} is: {addition}")
    print(f"The subtraction of {num1} from {num2} is: {subtraction}")

if __name__ == "__main__":
    main_part1()