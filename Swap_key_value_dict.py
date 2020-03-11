old_dict = {'A':45, 'B':23, 'C':46, 'E':12}
#print("printing items in the dictionaty:",old_dict.items())
#print("printing items in the dictionaty:",old_dict.keys())
#print("printing items in the dictionaty:",old_dict.values())
#old_dict[45] = ['A']
#  :A

#print("old_dict", old_dict)

new_dict = {}
#print(new_dict)

for k, v in old_dict.items():
    if v in new_dict:
        new_dict[v].append(k)
        #print(new_dict)
    else:
        new_dict[v] = k
print(new_dict)




