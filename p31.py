# Determine whether a given integer number is prime.

def is_prime(number):
    """
    Check whether given number is prime or not

    Parameters
    ----------
    number: int
        number to check for prime or not

    Returns
    -------
    bool
        is number prime (True) or not (False)
    """
    if number == 2:
        return True
    elif number <= 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def main():
    num = int(input("Enter any number:"))

    result = is_prime(num)
    print(result)


if __name__ == "__main__":
    main()
