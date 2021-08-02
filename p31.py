# Determine whether a given integer number is prime.

num = int(input("Enter any number:"))


def isPrime(number):
    if number == 2:
        return "T"
    elif number <= 1:
        return "F"
    else:
        for i in range(2, number):
            if number % i == 0:
                return "F"
        if i == number - 1:
            return "T"


result = isPrime(num)
print(result)
