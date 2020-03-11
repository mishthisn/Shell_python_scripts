import copy

old_dict = {'A':45, 'B':23, 'C':45, 'E':12}
old_dict.update({'D':65})

print("Original dictionary is:")
print(id(old_dict))


copy_dictionary = old_dict.copy()
print(id(copy_dictionary))
print(copy_dictionary)

new_dict = {'s':45, 'n':34}
new_dict.update({'r':23})
deepcopy_dictionary = copy.deepcopy(new_dict)

print(id(new_dict))
print(id(deepcopy_dictionary))

print(deepcopy_dictionary)