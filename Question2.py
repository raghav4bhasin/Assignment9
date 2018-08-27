'''
Name and handle the exception occurred in the following program: 
l=[1,2,3] 
print(l[3])
'''

try:
    l=[1,2,3] 
    print(l[3])
except IndexError as message:
    print("ERROR!!", message)
