from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, premium = argv
    time_work = int(time_work)
    rate = int(rate)
    premium = int(premium)
    print((time_work * rate) + premium)
else:
    time_work = int(input("Inpute time work: "))
    rate = int(input("Inpute ratet: "))
    premium = int(input("Inpute premium: "))
    print((time_work * rate) + premium)