'''
Name and handle the exception occured in the following program: 

a=3
 if a<4:
    a=a/(a-3)
     print(a)
'''

a = 3
try:
    if a < 4:
        a = a/(a-3)
        print(a)

except ZeroDivisionError as message:
    print(message)
