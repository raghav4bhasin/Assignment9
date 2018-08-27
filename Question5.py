try:
    x = int(input('Enter First Number: '))
    y = int(input('Enter Second Number: '))
    print(x/y)
    
    
except ValueError:
    print("Please enter integer value only")

except IndexError:
    print("Index Out of Scope")
    
except ImportError:
    print("An Import Error.")
