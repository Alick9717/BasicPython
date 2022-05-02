def my_func(*args):
    args1 = int(input("Enter number: \n"))
    args2 = int(input("Enter number: \n"))
    args3 = int(input("Enter number: \n"))

    if args1 >= args2 > args3:
        return args1 + args2
    elif args3 >= args2 > args1:
        return args3 + args2
    elif args1 >= args3 > args1:
        return args1 + args3
    else:
        exit(-1)

print('Result: ', my_func())