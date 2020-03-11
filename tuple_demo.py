x_tuple = ('apple', 'cherry')
print(x_tuple[1])
y = list(x_tuple)

print(y)
y[1] = 'kiwi'
x_tuple = tuple(y)
print(x_tuple)

