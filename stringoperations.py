

print('\n-----------Indexing and slicing-------------\n')
#    01234
s = 'Hello'
print(f'Length of s: {len(s)}')

print(f'First char of s: {s[0]}')
print(f'Last char of s: {s[-1]}')

print(f's[0:3]: {s[0:3]}')

s2 = 'Welcome_To_ICS31'
print(f'Start: 0, End: 10, Stride: 2: {s2[0:14:2]}')


print('\n-----------replace-------------\n')
original_string = "apple, banana, cherry, banana"
new_string = original_string.replace("banana", "orange")

print("Original String:", original_string)
print("New String:", new_string)

print('\n-----------find and rfind-------------\n')
my_string = "Hello, World!"
index = my_string.find("World")

print("Index of 'World':", index)

my_string = "Hello, World! World!"
index = my_string.rfind("World")

print("Last Index of 'World':", index)

print('\n-----------count-------------\n')
my_string = "apple, banana, cherry, banana"
count = my_string.count("banana")

print("Number of occurrences of 'banana':", count)

print('\n-----------Formatting-------------\n')
name = "Bob"
relation = "Friend"
print('print(f"{name} is my {relation}") -> ', end='')
print(f'{name} is my {relation}')

num = 3
print('print(f’{num:f}’’) -> ', end='')
print(f'{num:f}')
print('print(f’{num:.3f}’’) -> ', end='')
print(f'{num:.3f}')
