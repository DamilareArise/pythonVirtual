# MODES
# r -> read only
# w -> write
# x -> create
# a -> append

# file = open(r"E:\Datasets\instagram_reach.csv", mode='r', encoding='Latin-1')
# # print(file.read())

# file.close()
# file.read()

# with open('task.py','r') as file:
#     print(file.read())
       
# file.write('sdddsdsldms')

# with open('note.csv', 'a') as file:
#     file.write('How are you?')

# open('note.pdf', 'x')

# with open('note.csv') as file:
#     # print(file.read(5))
#     print(file.readlines())
    
    
import os
# os.remove('note.pdf')
# os.mkdir('newFolder')
# os.remove('newFolder')

# try: 
#     os.rmdir('newFolder')
# except Exception as e:
#     print(e)

# is the function to remove a folder with content?

# print(os.path.exists('newFolder'))
# os.rename('newFolder', 'NewFolder')



names = []
heights = []

presidents = {}

with open('president_height.csv') as file:
    pres_height = file.readlines()
    # pres_height.pop(0)
    
    pres_height = pres_height[1:]
    # print(pres_height)
    
    for item in pres_height:
        item = item.split(',')
        name = item[1]
        height = int(item[2].strip('\n'))
        presidents[name] = height


# print(names)
# print(heights)
print(presidents)

# ASSIGNMENT
# 1. Find the tallest president 
# 2. Find the shortest president
# 3. Find the average height of all presidents