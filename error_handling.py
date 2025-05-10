#  runtime error
#  Compile type error

# print(x)
li = list(range(10))
# x = 34
try: 
    # print(li[6])
    x
except Exception as e:
    print('error: ', e)
    
# except IndexError as I:
#     print('error1: ', I)

# except NameError as N:
#     print('Error2: ', N)

else:
    print(x) # This shows when no error occurrs 

finally:
    print('I dey here') # It show even if there is an error or not
