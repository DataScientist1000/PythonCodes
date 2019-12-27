def add2num(a, b):
    return a + b


a = int(input("Enter the first element = "))
b = int(input("Enter the second element = "))

print("The sum of two numbers = ", add2num(a, b))

name, company = input("Enter the name and the company = ").split()

print(add2num(name, company))

x, y = input("Enter the x and y with comma sep = ").split(",")

print(add2num(x, y))
