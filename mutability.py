print('\n-----------Mutability-------------\n')
# Example of immutable: assign new value -> new object in memory
a = 1
b = 2
c = a
print(f'Memory address of a: {id(a)}')
print(f'Memory address of b: {id(b)}')
print(f'Memory address of c: {id(c)}')
b = 3
print(f'Update value of b')
print(f'Memory address of b: {id(b)}')


l = [1,2,3,4]
print(f'Memory address of l: {id(l)}')
l.append(5)
print(f'Change contents of l')
print(f'Memory address of l: {id(l)}')
