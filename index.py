# print(50+50)
# print("Hello world")

# Python commentting
# 1. comment is used for debugging
# 2. to make set codes not to be executed
# 3. for documentation
'''
block comment / doc string 

ajsbasas
masaknalsa
djahshashlahas
ajsbaksaslda
'''

# Python variable 

# name = "Shola"
# print(name)

bottle = "water"

# 1. Variable name
# 2. Assignment operator (=)
# 3. Value

# Rules guiding variable declaration
'''
1. A variable name can only begin with an alphabet or underscore
2. A variable name can only contain alphabet, number, and underscore. no special character and space instead you can use;
    i. pascal casing e.g PascalCasing
    ii. camel casing e.g camelCasing
    iii. snake casing e.g snake_casing
3. A variable name cannot be a keyword
4. A variable name must be descriptive
'''

# firstName = 'Damilare'

# Types of variable declaration
# 1. single variable single value
name = 'Dami'
# 2. single variable multiple value
names = 'Damilare', 'Shola', 'Tosin'
# print(names)
# 3. multiple variable single value
x = y = z = 30
# print(x, y, z)
# 4. multiple variable multiple value
x, y, z = 30, 40, 50


product_name = 'LG TV'
manufacturer = 'LG'
price = 50.45
quantity = 10

# print(product_name, manufacturer, price, quantity)
# Concatenation -> The ability to joining two or more strings together

# print("The name of the product is", product_name )
# print("The name of the product is " + product_name )
# print("The price is " + str(price))

name = 'Adeshola okunola'
age = 30
nationality = 'Nigerian'
study = 'data analysis'

# print('My name is '+name+'. I am '+str(age)+'years old.'+' I am a '+nationality+' currently studying '+study)

# f-string
# print(f'My name is {name}. I am {age}years old. I am a {nationality}, currently studying {study}.')

# Python DATATYPES
'''
1. Number Types; 
    i. Integers int() e.g 12, 345, 1234
    ii. Float float() e.g 12.5, 3.14, 0.0
    iii. Complex complex() e.g 3+4j, 5-6j
2. Text type; 
    i. String str()

3. Sequence Type:
    i. List list() [] e.g [1, 2, 3], ['a', 'b', 'c']
    ii. tuple tuple() () e.g (1, 2, 3), ('a', 'b', 'c')
    iii. Range range() e.g range(1, 10)
4. boolean bool(); True , False
5. Mapping type: dict(), {key:value} e.g {"name": "Damilare", "age": 30}
6. Set Type: set(), {} e.g {12, 44, 45}
'''

# number = 12.6 + 2j
# print(type(number))

# students = ('Ade', 'Ola', 'Femi')
# print(type(students))

# number = list(range(2, 10, 2))
# print(number)

# isMarried = False
# print(type(isMarried))


# Assignment
'''
1. Read up on Python Operators
2. Read up on Conditional statement
3. Build a simple caculator
'''

# student = {
#     "name": "Damilare",
#     "age": 30,
#     "course": 'Data science'
# }
# # print(type(student))
# print(student['name'])

# numbers = {2, 4, 5, 2, 3, 6, 1}
# print(type(numbers))
# print(numbers)

# students = {'Femi', 'Ade', 'Ola', 'Ojo'}
# print(students)


# Python Operators

'''
1. Arithmetic Operators: +, -, *, /, //, %, **
2. Assignment Operators: =, +=, -=, *=, /=, %=, **=
3. Comparison Operators: ==, !=, >, <, >=, <=
4. Logical Operator: and, or, not
5. Identity Operator: is, is not
6. Membership Operator: in, not in
7. Bitwise Operator: &, |, ^, ~, <<, >>
    & => and
    | => or
    ^ => xor
    ~ => not
    << => left shift
    >> => right shift
'''

# x = 10
# print(type(bin(x)))

# 10 => 1010
# 5 =>   100

print(f'5 => {bin(5)}')
print(f'10 => {bin(10)}')


# print(bin(10 ^ 5))

print(bin(5 >> 1))


# print(5 // 2) # 2
# print(5 % 2) # 1 (remainder)

# x = 5
# x -= 1 # x = x + 1
# print(x)

# print(x >= 5)

"""
    AND Operator
A ----- B ----- C
0 ----- 0 ----- 0
0 ----- 1 ----- 0
1 ----- 0 ----- 0
1 ----- 1 ----- 1

    OR Operator
A ----- B ----- C ---- A XOR(^) B
0 ----- 0 ----- 0 ----- 0
0 ----- 1 ----- 1 ----- 1
1 ----- 0 ----- 1 ----- 1
1 ----- 1 ----- 1 ----- 0

 NOT Operator
 A ----- not A 
 0 ----- 1
 1 ----- 0
"""

# Python if else statement

# x = 5

# if x == 5 or x > 5:
#     print('x is equal to or greater than 5')
# else:
#     print('x is less than 10')


# number = int(input('Number: '))
# if number % 2 == 0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')

# beans = True
# rice = False
# bread = False

# if beans and rice:
#     print('I will buy beans and rice')
    
# elif beans:
#     if bread:
#         print('I will buy beans and bread')
#     else:
#         print('I dont eat my beans without bread. Thank you')

# elif rice:
#     print('I will buy rice')
    
# else:
#     print('I am not interested')


# print('My Calculator....')

# value1 = float(input('First value: '))
# value2 = float(input('Second value: '))
# print("""
#     1. Addition
#     2. Subtraction
#     3. Multiplication
#     #. Exit
# """)
# choice =  input('Choice: ')
# if choice == '1':
#     res = value1 + value2
#     print(f'{value1} + {value2} = {res}')

# elif choice == '2':
#     res = value1 - value2
#     print(f'{value1} - {value2} = {res}')

# elif choice == '3':
#     res = value1 * value2
#     print(f'{value1} x {value2} = {res}')
    
# elif choice == '#':
#     print('Thank you')
#     exit()
# else:
#     print('Invalid choice')
    
    

# print('I am still running')

# Assignment 
# 1. Build a simple ussd application



x = 5
y = 5
# print(x is not y)


# fruits = ['Apple', 'Orange', 'Mango']

# print('Apple' not in fruits)