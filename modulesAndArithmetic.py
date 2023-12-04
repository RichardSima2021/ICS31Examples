import math # <- require this import statement
print('\n-----------Arithmetic------------\n')
a = 5
b = 3
result = a + b
print("Addition:", result)
result = a - b
print("Subtraction:", result)
result = a * b
print("Multiplication:", result)
result = a / b
print("Division:", result)
result = a // b
print("Floor Division:", result)
result = a % b
print("Modulus:", result)
result = a ** b
print("Exponentiation:", result)

print('\n-----------Compound operators------------\n')
a += b
print(f"a += b -> {a}")

print('\n-----------Importing the math module------------\n')
print('Must first call import math at the top of the program')
print(f'Square root of 169 -> sqrt(169): {math.sqrt(169)}')
