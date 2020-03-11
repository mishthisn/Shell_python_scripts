list = [3, 6, 44, 12, 1, 44]
list2 = []

for i in list:
    if i not in list2:
        list2.append(i)
print("Printing list",list2)

set = {""}

m_set = {""}

for i in list:
    if i not in set:
        m_set.add(i)

print("printing set:",m_set)

my_dict = {}

for i in list:
    if i not in my_dict.keys():
        my_dict[i] = 0

print(my_dict.keys())

