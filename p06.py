# Find out whether a list is a palindrome

values = input("Enter elements:").split()
rev_values = list(reversed(values))

if values == rev_values:
    print('Palindrome')
else:
    print('Not Palindrome')
