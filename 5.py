string = input("Enter A String: ")

try:
    num = int(input("Enter A Number: "))
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)