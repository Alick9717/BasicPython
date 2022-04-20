a = abs(int(input("Enter a positive integer \n")))
max = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > max:
        max = a % 10
    if a > 9:
        continue
    else:
        print("largest number ", max)
        break