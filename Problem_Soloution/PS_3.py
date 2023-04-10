# 3. Write a Python program to check whether a number is divisible by 5 and 50 or not.

num1 = int(input())

if num1 % 5 == 0 and num1 % 50 == 0:
    print("number is divisible by 5 and 50")
else:
    print("number is not divisible by 5 and 50")