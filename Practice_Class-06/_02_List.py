"""
List
1.Ordered
2.Element access by Index
3.Mutable type data Structure
4.Various type data- integer/float/List/others
"""
#Declare-empty

lst = []
print(type(lst))
lst2 = list()
print(type(lst2))

#Declare-empty
lst_3 = [1, 2, 5.6, "python", [1, 3, "Java"]]
print(lst_3)
print(type(lst_3))

#Access Element
print(lst_3[0])
print(lst_3[1])
print(lst_3[2])
print(lst_3[3])
print(lst_3[4])
print(lst_3[4][1:])
print(lst_3[-1])

#Lengthe
print(len(lst_3))

#Adding
lst_3.append(4)
print(lst_3)

lst_3.insert(0, "C++")
print(lst_3)

lst_4 = [1, 2, 3, 4]
lst_3.extend(lst_4)
print(lst_3)

#Value Updatee
lst_3[0] = "Javascript"
print(lst_3)

# Remove
lst_3.pop(0) # Pop remove index
print(lst_3)

lst_3.remove(1) # remove work is remove value
print(lst_3)
