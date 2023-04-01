"""
1.Nums of scenario
2. Comparison/Membership/Identity Operator
"""
#01 if statement
office_time = 9
current_time = 9
if office_time == current_time:
    print("Go to office")
print(office_time == current_time)

#02 if else Statement

num = 100
if num > 10:
    print("Num is greater than 10")

else:
    print("Num is greater than or equal")

#03 Nested if Statement [Multiple condition]
num = 1000
if num > 10:
    print(">")
if num < 10:
    print("<")
if num == 10:
    print("==")
else:
    print("=")

# if elif else [Multiple condition]
num = 5
if num == 5:
    print("=")
elif num > 10:
    print(">")
elif num < 10:
    print("<")
else:
    print("5")
