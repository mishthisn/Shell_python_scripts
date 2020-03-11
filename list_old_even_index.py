#class old_even:

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

"""
Element at odd-index positions from list one
[6, 12, 18]
list[1::2]

oddElements = listOne[1::2]
print("Element at odd-index positions from list one")
print(oddElements)
"""

for i in range(len(listOne)):
    if i % 2 == 1:
        print("Odd-index position List 1",listOne[i])

"""
Element at odd-index positions from list two
[4, 12, 20, 28]

EvenElement = listTwo[0::2]
print("Element at odd-index positions from list two")
print(EvenElement)
"""

for i in range(len(listTwo)):
    if i % 2 == 0:
        print("Odd-index position",listTwo[i])

"""
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]

print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)
"""
