# Calculate Euler's totient function phi(m)

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


def is_coprime(number1, number2):
    """
    Check whether given numbers are coprime

    Parameters
    __________
    number1: int
        First number
    number2: int
        Second number

    Returns
    _______
    bool
        is numbers coprime (True) or not (False)
    """
    result = gcd(number1, number2)

    if result == 1:
        return True
    else:
        return False


def totient_phi(m):
    """
    Calculate euler's totient function phi(m)

    Parameters
    __________
    m: int
        number on which to calculate euler's totient 

    Returns
    _______
    int
        euler's totient phi(m)
    """
    if m == 1:
        return 1
    else:
        count = 0
        i = 1
        while i < m:
            if is_coprime(m, i):
                count += 1
            i += 1
        return count


def main():
    m = int(input("Enter M:"))

    result = totient_phi(m)
    print(result)


if __name__ == "__main__":
    main()
