a = int(input("Enter your first day's run in km: \n "))
b = int(input("Enter the total desired result in km: \n"))
c = 1
while a < b:
    a *= 1.1
    c += 1
print('You will reach the required indicators in ', c , 'days.')