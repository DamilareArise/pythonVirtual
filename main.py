# import task
from task import deposit, withdraw

def dashboard():
    user = input('''
    1. Deposit
    2. Withdraw 
          
    choice: ''')
    
    if user == '1':
        deposit()
    elif user == '2':
        withdraw()
        
dashboard()