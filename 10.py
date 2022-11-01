x = int(input("Enter first Value: "))
y = int(input("Enter Second Value: "))

try:
    print("outer try block")
    try:
        print("nested try block")
        print(x / y)
    except TypeError as te:
        print("nested except block")
        print(te)
except ZeroDivisionError as ze:
    print("outer except block")
    print(ze)
    
finally:
    print("GoodBye")