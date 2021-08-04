# Calculate Euler's totient function phi(m)

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


def totient_phi(m):
    """
    Calculate euler's totient function phi(m)

    Parameters
    ----------
    m: int
        number on which to calculate euler's totient 

    Returns
    -------
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
