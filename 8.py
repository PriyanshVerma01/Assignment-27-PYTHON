try:
    a=int(input("Enter the value of a: "))
    b=int(input("Enter the value of b: "))
    c=a/b

except ZeroDivisionError:
    print("Enter variables correctly!")
except ValueError:
    print("You Can Pass Only int Type Value!")    

else:
    print(c)
    
finally:
    print("i'm always execute")