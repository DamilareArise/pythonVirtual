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

# print(f'5 => {bin(5)}')
# print(f'10 => {bin(10)}')


# print(bin(10 ^ 5))

# print(bin(5 >> 1))


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



# PYTHON STRINGS
text = "I am happy to be here.!" # ['I', ' ', 'a', 'm', ' '... ]
# name = '<h1>Damilare</h1>'

# print(type(text))

# print(text[-3])

# slicing
# print(text[0:5])
# print(text[5:10])

# print(len(text))

# print(ord('i'))
# print(chr(73))

# print(text.lower())
# print(text.upper())
# print(text.capitalize())
# print(text.title())

# print(text.strip())
# print(name.lstrip('</h1>'))
# print(name.rstrip('</h1>'))

# print(text.startswith('I'))
# print(text.endswith('.!'))

# print(text.find('Happy'))

# email verification
# email = input('Email: ')
# if email.find('@') != -1 and email.find('.') != -1 and email[0].isalpha() and email[-1].isalpha():
#     print('Valid Email')
# else:
#     print('Invalid Email')
    
# print(text.split('to'))

# splited = ['I', 'am', 'happy', 'to', 'be', 'here.!']
# joined = ' '.join(splited)
# print(joined)


# address = 'No 23|Ajala Estate|Abeokuta|Ogun State|Nigeria'
# splited = address.split('|')
# # print(splited[3])
# address = {
#     "house_no": splited[0],
#     'street': splited[1],
#     'city': splited[2],
#     'state': splited[3],
#     'country': splited[4],
# }
# print(address['house_no'])

# ussd = input('ussd: ')
# if ussd.strip() == '*312#':
#     print('''
#         1. Buy Data
#         2. Data Balance  
#     ''')
# else:
#     print('Invalid USSD Code')

# Assignment 
# Develop a simple Quiz App that asks the user a series of questions and keeps track of the score.
# Develop a palindrome checker


# ques = input('Is Nigeria a country? (yes/no): ').strip().upper()
# if ques == 'YES':
#     print('Correct')
# else:
#     print('wrong')


# drt = r'C:\\python_work\next'
# print(drt)
# r -> rawstring 
# \ -> escape chr 
# \n -> new line
# \t  ->  tab
# print('it\'s')
# print('How are you?\\t\\tFine')
# print(r'How are you?\t\tFine')


# python collections/array 
# 1. list 
# 2. tuple
# 3. dict
# 4. set

# 1. list: A list is ordered, mutable/changeable, indexable, and it allows duplicate values
# myList = ['Tosin', 'Olumide', 'Peace', True, 12, 45.3, None, 'Peace']
# print(type(myList))
# print(len(myList))

# print(myList[0])
# print(myList[-1])

# print(myList[1:4])
# myList[-2] = 'Damilare'
# print(myList)

# myList.append('Jacob')
# myList.extend(['Jacob', 'Mary'])
# myList.insert(3, 'Victor')
# myList.pop(2)
# myList.remove('olumide')
# myList.reverse()
# print(myList.index('Olumide'))
# print(myList)

numbers = [3, 5, 7, 8, 6, 1, 2]
# numbers.sort(reverse=True)
# print(numbers)

# alp = ['ade', 'Lola', 'Cephas', 'Kola']
# alp.sort(key=str.lower)
# print(alp)

# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))

# 2. tuple: indexed, ordered, allows duplicate value, but it is immutable/unchangeable
myTuple = ('Ade', 'Kola', 'Lola', 'Cephas', 'Kola')
# print(myTuple)
# print(myTuple[0:2])

# myTuple[3] = 'Segun'
# li = list(myTuple)
# li[3] = 'Segun'
# myTuple = tuple(li)
# print(myTuple)

# unpacking
# (*li,) = myTuple
# print(li)
# x, y, *z = myTuple
# z, *x, y = myTuple
# print(z)

# print(myTuple.count('Kola'))
# print(myTuple.index('Kola', 2))

# print(sorted(myTuple))

# 3. set: unordered, unindexed, no duplicate value, unchangeable
mySet = {'Ade', 'Kola', 'Lola', 'Cephas', 'Kola'}
# print(mySet)
# mySet[0] = 'Damilare'

# mySet.add('Damilare')
# mySet.update(['Damilare', 'Segun'])
# mySet.remove('Ade') # remove() method will raise a KeyError if the item is not found
# mySet.discard('ade') # discard() method will not raise a KeyError if the item is not found
# print(mySet)

setA = {4,2,1,3,5,9,6,7,8}
setB = {3,4,6,11,12}
setC = {1, 3, 5}

# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setA.difference(setB)) # setA - setB
# print(setA.symmetric_difference(setB))

# setA.intersection_update(setB)
# print(setA)

# print(setA.issuperset(setC))
# print(setA.issubset(setB))
# print(setA.isdisjoint(setB))


# 4. Dictionary: 
# myDreamCar = {
#     'brand': 'Lambo',
#     'model': 'Aventador',
#     'color': 'Red',
#     'year': 2025,
#     'owner':{
#         'name': 'Mr Olumide',
#         'address': {
#             'street': 'Olumide Street',
#             'city': 'Ikeja',
#             'state': 'Lagos',
#             'country': 'Nigeria'
#         }
#     }
# }

# print(myDreamCar['owner']['address']['country'])

person = {
    'name':'Ojo Ade',
    'age': 23
}

# print(person.keys())
# print(person.values())
# print(person.items())

# print(person['age'])
# print(person.get('ages', 'Not Found'))
# person['marital status'] = 'Single'
# person.update({'marital status': 'Single', 'country': 'Nigeria'})
# person.popitem()
# print(person)

# PYTHON LOOPS
# 1. For loop 
# 2. While Loop

# sequence => string, list, tuple, set, dictionary

# name = 'Damilare' 
# for letter in name:
    
#     print(letter)
#     print('_________')

# names = ['Olumide', 'Peace', 'Tosin']
# for name in names:
#     print(f'Welcome {name}')


# score = 0
# quest1 = '1. What is the capital of Nigeria?\na.) Abuja b.) Lagos '
# print(quest1)
# answer = input('Enter your answer: ')
# if answer.strip().lower() == 'a':
#     print('Correct')
#     score += 1
# else:
#     print('Incorrect')
    
# quest2  = '2. What is the capital of Lagos?\na.) Ikeja b.) Lekki '
# print(quest2)
# answer = input('Enter your answer: ')
# if answer.strip().lower() == 'a':
#     print('Correct')
#     score += 1
# else:
#     print('Incorrect')
    
# print(f'Your total score is {score}')


# Using the Zip class 

# score = 0
# questions = [
#     '1. What is the capital of Nigeria?\na.) Abuja b.) Lagos',
#     '2. What is the capital of Lagos?\na.) Lekki  b.)Ikeja  '
# ]

# anwers = ['a', 'b']
# answer_mark = [10, 5]

# for ques, ans, mark in zip(questions, anwers, answer_mark) :
#     print(ques)
#     answer = input('Enter your answer: ')
#     if answer.strip().lower() == ans:
#         print('Correct')
#         score += mark
#     else:
#         print('Incorrect')
        
# print(f'Your total score is {score}')


# Using List of tuples

# ques_ans_mark = [
#     ('1. What is the capital of Nigeria?\na.) Abuja b.) Lagos', 'a', 10),
#     ('2. What is the capital of Lagos?\na.) Lekki  b.) Ikeja', 'b', 5) 
# ]

# for ques, ans, mark in ques_ans_mark:
#     print(mark)

# using Dictionary
# ans_ques = {
#     'a': '1. What is the capital of Nigeria?\na.) Abuja b.) Lagos',
#     'b': '2. What is the capital of Lagos?\na.) Lekki b.) Ikeja '
# }
# for ans, ques in ans_ques.items():
#     print(ques)

# Assignment
'''
1. Ask the user/admin/principal how students is taking the test and register them.
2. Call the students one after the other to take the test,
3. Print out the students and their score
4. Print out the student with the highest and lowest score
5. Print out the avarage score of the students

'''

# for x in range(1, 6):
#     print(f'{x} Times Table')
#     for y in range(1, 6):
#         print(f'{x} x {y} = {x * y}')


# API
# WHILE LOOP
# FUNCTIONS
# OOP


# API -> Application progromming interface

# [
#     {
#     "name": "John Doe",
#     "class": "JSS 1",
#     },
#     {   
#      "name": "Jane Doe",
#      "class": "JSS 2",
#     }
# ]

# WHILE LOOP
# x = 10
# while x > 0:
#     print(x)
#     x -= 1
    
# x = 0
# while x < 10:
#     print(x)
#     x +=1

# user = input('USSD: ')
# while user != '*312#':
#     print('Invalid USSD code')
#     user = input('USSD: ')

# else:
#     print('Welcome....')

# slot = 3
# students = []
# while slot > 0:
#     info = {
#         "name": input('Name: '),
#         "email": input('Email: ')
#     }
#     students.append(info)
#     slot -= 1

# print(students)



# tickets = 10
# while tickets > 0:
#     age = int(input('Age: '))
    
#     if tickets == 3:
#         break
    
#     elif age >= 18:
#         print('You are old enough')
    
#     else:
#         print('You are too young')
#         continue
    
#     tickets -= 1
#     print(f'Tickets remaining: {tickets}')  
    
# print('Sold out', tickets)


# while True:
#     user = input('press enter to continue or 1 to exit')
#     if user == '1':
#         break


# Python Function

'''
Stages of function creation in python
1. function declaration
2. function definition
3 function invocation

function categories
1. parametized func
2. non parametized func

'''

def greet():
    print('Hello')
    
# greet()

# def greet(name):
#     print(f'Hello {name}')

# greet(name='Damilare')


def greet(name:str|None, status:bool =False) -> str:
    '''
    This is a function that greets the user with a name and status
    '''
    if status:
        print(f'Hello {name}, you are verified✅')
    else:
        print(f'Hello {name}, you are not verified❌')
        

# greet('Damilare', True)


def evaluate(num:int):
    return num * 10 ** 2

# print(evaluate(2))

def calc():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    res = num1 + num2 
    print(evaluate(res))

# calc()


# recurssive function


def home():
    print('Welcome to home page')
    user = input('Ussd: ')
    # while user != '*312#':
    #     print('Invalid USSD code')
    #     user = input('Ussd: ')
    
    if user != '*312#':
        print('Invalid USSD code, Try again')
        home()  #recurssive
         
    else:
        dashboard()
        
def dashboard():
    print('Welcome to dashboard')
    user = input('''
        1. Buy Data
        2. Check Balance 
        #. Exit
        
    Choice: ''')
    if user == '1':
        buyData()
    elif user == '2':
        checkBalance()
    elif user == '#':
        exit()
    else:
        print('Invalid choice')
        dashboard()  #recurrsive
        
def buyData():
    print('Welcome to data purchase page')
    
def checkBalance():
    print('Welcome to balance check page')

# home()


# Local and Global variable

# val1 = 10
# val2 = 5
# val = 0

# def add():
#     global val
#     # global val1
#     # val1 = 2  * val1  # 20 (local variable)
#     val = 10
#     print(val1 + val2 + val)

# def sub():
#     print(val1 - val2 + val)


# add() 
# sub()


balance = 0

def dashboard():
    user = input('''
         1. withdraw
         2. Deposit
         3. check balance        
    choice: ''')
    
    if user == '1':
        withdraw()
    elif user == '2':
        deposit()
    elif user == '3':
        checkBalance()
    else:
        print('Invalid')
        dashboard()
        
def withdraw():
    global balance
    
    amount= int(input('Amount: '))
    if balance > amount:
        balance -= amount
        
    dashboard()
        
def deposit():
    global balance
    
    amount= int(input('Amount: '))
    balance += amount
    
    dashboard()
    
def checkBalance():
    print(balance)


dashboard()
    