def div():
    try:
        num1 = int(input("Enter the first number\n"))
        num2 = int(input("Enter the second number\n"))
        res = num1 / num2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong number! You cannot use zero as a divisor."

    return res


print(f'result  {div()}')
