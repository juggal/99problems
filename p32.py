# Determine the greatest common divisor of two positive integer numbers

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))


def gcd(number1, number2):
    if (number1 == 0):
        return number2
    else:
        return gcd(number2 % number1, number1)


result = gcd(num1, num2)
print(result)
