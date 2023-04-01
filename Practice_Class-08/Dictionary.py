"""
-key:Value pairs
-Unordered
-{}
[0]:"python"
[1]:"python"
"""
#Empty Dictionary
my_dict = {}
print(type(my_dict))
my_dict2 = dict()
print(type(my_dict2))

# With value
my_dict = {
    "name": "Joy Mitra",
    "fav_language": "Python",
    "one": 1,
    "two": 2.5,
    "lst":[1, 2, 3, 4]
}
print(my_dict)

my_dict_3 ={
    1: 1,
    2: 4.4
}
print(my_dict_3)

# Access
print(my_dict["name"])
print(my_dict["one"])
print(my_dict_3[1])
print(my_dict_3[2])

# Update / add
print(my_dict_3)
my_dict_3[1] = "one"
print(my_dict_3)
my_dict_3[3] = "three"
print(my_dict_3)

# Remove
print(my_dict_3.pop(1))
print(my_dict_3)

my_dict_3.clear()
print(my_dict_3)