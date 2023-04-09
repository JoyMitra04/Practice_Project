"""
Set:
1. Unordered
2. Unindexed
3. Duplicate not allow

Tuple:
1.Ordered
2.Unchangeable
3.Allow duplicate data

List:
1.Ordered
2.changeable
3.Allow duplicate data
"""
my_set = {}
print(type(my_set))

my_set2 = set("python")
print(my_set2)
print(type(my_set2))


a = {1, 2, 3, 4}
print(type(a))
print(a)

my_set_3 = {1, 2, 3, 1, 2, 3}
print(my_set_3)

my_set_3 = set("1")
print(my_set_3)

# Union Operation
A = {1, 2, 3, 4, 5, 6}
B = {1, 6, 7, 8, 9, 10}
print(A|B)
print(A.union(B))

# Intersection
print(A & B)
print(A.intersection(B))
