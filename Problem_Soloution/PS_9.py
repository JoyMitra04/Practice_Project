# 9. Write a Python program to input any character and check whether it is alphabet, digit or special character.

cha = input()
if cha.isalpha():
    print("it's alphabet")
elif cha.isdigit():
    print("it's digit")
else:
    print("special character")