def averagenum(a, b, c):
    count = 3.0
    return (a + b + c) / count


a, b, c = input("Enter three numbers with comma sep = ").split(",")

print(averagenum(int(a), int(b), int(c)))
