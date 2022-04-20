profit = float(input("Enter the company's revenue: \n"))
Expenses = float(input("Enter the firm's costs: \n "))
if profit > Expenses:
    print(f"The company is operating at a profit. Return on revenue amounted to {profit / Expenses:.2f} \n")
    workers = int(input("Enter the number of company employees: \n"))
    print(f"Profit per employee was {profit / workers:.2f}")
elif profit == Expenses:
    print("The company is running at zero: \n")
else:
    print("The company is operating at a loss: \n")

