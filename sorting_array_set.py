list1 = [4, 8, 9, 1, 10, 1]
#list1.insert(2,9)
print(list1)
list2= []
input_array = []
for i in list1:
    if i not in list2:
        list2.append(i)
        # To to Sort
print(list2)

# measure time

input_array = []

for i in range(100):
    input_array.append(i)

print(input_array)


#m_dict = {}

"""
m_set = {""}

for i in list:
    m_set.add(i)
    print(i)

print("printing set:",m_set)

"""

"""
for i in list:
    if i not in m_dict.keys():
        m_dict[i] = 0

print(m_dict.keys())
"""


