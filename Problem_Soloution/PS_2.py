# 2. Write a Python program to find maximum between three numbers.

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    print("num1 is greater than num2 and num3")
elif num2 > num1 and num2 > num3:
    print("num2 greater than num1 and num3")
else:
    print("num3 is greater than num1 and num2")
