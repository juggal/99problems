# Determine the greatest common divisor of two positive integer numbers


def gcd(number1, number2):
    """
    Calculate given numbers greatest common division

    Parameters
    __________
    number1: int
        First number
    number2: int
        Second number

    Returns
    _______
    int
        greatest common divisor of given numbers
    """
    if (number1 == 0):
        return number2
    else:
        return gcd(number2 % number1, number1)


def main():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    result = gcd(num1, num2)
    print(result)


if __name__ == "__main__":
    main()
