# Determine whether two positive integer numbers are coprime


def gcd(number1, number2):
    """
    Calculate given numbers greatest common division

    Parameters
    ----------
    number1: int
        First number
    number2: int
        Second number

    Returns
    -------
    int
        greatest common divisor of given numbers
    """
    if (number1 == 0):
        return number2
    else:
        return gcd(number2 % number1, number1)


def is_coprime(number1, number2):
    """
    Check whether given numbers are coprime

    Parameters
    ----------
    number1: int
        First number
    number2: int
        Second number

    Returns
    -------
    bool
        is numbers coprime (True) or not (False)
    """
    result = gcd(number1, number2)

    if result == 1:
        return True
    else:
        return False


def main():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    result = is_coprime(num1, num2)
    print(result)


if __name__ == "__main__":
    main()
