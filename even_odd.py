def check_even_odd(number):
    # Constraint: Ensure input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"


if __name__ == "__main__":
    try:
        number = int(input("Enter a whole number: "))
        print(check_even_odd(number))
    except ValueError:
        print("Please enter a valid whole number.")
