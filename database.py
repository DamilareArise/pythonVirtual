import mysql.connector as sql
import random

mycon = sql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'password',
    database = 'bank_db'
)

mycursor = mycon.cursor()
mycon.autocommit = True

# SQL Query categories
'''
1. DDL -> Data defination language e.g CREATE, ALTER, DROP
2. DML -> Data manipulation language e.g INSERT, UPDATE, DELETE
3. DQL -> Data query language e.g SELECT 
'''

# DDL
# 1. creating a database
# query = 'CREATE DATABASE bank_db'
# query = 'SHOW DATABASES'
# mycursor.execute(query)
# for db in mycursor:
#     print(db)

# 2. Creating Table
# query = 'CREATE TABLE user_table(id INT PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), email VARCHAR(50) UNIQUE, account_no VARCHAR(10) UNIQUE, account_bal FLOAT, date_created DATETIME DEFAULT CURRENT_TIMESTAMP)'

# query = 'ALTER TABLE user_table CHANGE account_bal account_balance FLOAT'
# query = 'ALTER TABLE user_table ADD COLUMN password VARCHAR(50) AFTER account_balance'
# query = "ALTER TABLE user_table DROP COLUMN password" 

# mycursor.execute(query)

# mycursor.execute('SHOW TABLES')
# for table in mycursor:
#     print(table)


# ASSIGNMENT
# 1. Create a Account creation

def create_account():
    fullname = input('Fullname: ').strip()
    email = input('Email: ')
    password = input('Password: ')
    account_no = random.randint(2000000000, 2999999999)
    account_bal = 0
    
    query = "INSERT INTO user_table(fullname, email, account_no, account_balance, password) VALUES(%s, %s, %s, %s, %s)"
    values = (fullname, email, account_no, account_bal, password)
    mycursor.execute(query, values)
    
  
    print('Account created successfully')

# create_account()

def delete_account(email):
    query = 'DELETE FROM user_table WHERE email=%s'
    value = (email,)
    mycursor.execute(query, value)
    if mycursor.rowcount > 0:
        print('Account deleted successfully')
    else:
        print('Account not found')

# delete_account('dami@gmail.com')

def change_password(email, prev_pass, new_pass):
    query = "UPDATE user_table SET password=%s WHERE email=%s and password=%s"
    values = (new_pass, email, prev_pass)
    mycursor.execute(query, values)
    if mycursor.rowcount > 0:
        print("password change successfully")
    else:
        print("Unable to change password. Account not found.")

# change_password('dami@gmail.com', '1234', 'Password123')

    
def login(email, password):
    # query = 'SELECT * FROM user_table'
    query = 'SELECT fullname, account_no, account_balance FROM user_table WHERE email=%s and password=%s'
    values = (email, password)
    mycursor.execute(query, values)
    # infos = mycursor.fetchall()
    detail = mycursor.fetchone()
    if detail:
        print('Login successful')
    else:
        print('Incorrect email or password')
    
# login('dami@gmail.com', 'Password12')