def my_func(x,y):
    n1 = x ** y
    n2 = 1
    i = 1
    while i <= abs(y):
        n2 *= x
        i += 1

    return n1, 1 / n2

print(
    my_func(
        int(input("Enter positive number: \n")),
        int(input("Enter negative number: \n"))
    )
)