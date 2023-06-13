# A simple introduction.
print("Welcome to the interest and loan calculator")


# Calculates the return on investment based on the users input.
def investment():
    x = 1
    money = int(input("\nHow much is being invested in pounds?: "))
    apr = float(input("Using decimals, What is the apr rate?: "))
    time = int(input("How many years deposited?: "))
    print()
    for i in range(time):
        money = money * (1 + apr)
        money = round(money, 2)
        print("year", x, f"£{money:.2f}")
        x = x + 1
    print("\nThank you for using the interest and loan calculator.")


# calculates total debt cost and the yearly and monthly repay amounts.
def loan():
    borrowing = int(input("\nIn pounds, how much money are you borrowing?: "))
    interest = float(input("Using decimals, how much is the interest?: "))
    years = int(input("How many years to pay off?: "))
    total = borrowing * (1 + interest)
    yearly_repay = borrowing * (1 + interest) / years
    monthly_repay = yearly_repay / 12
    print(f"\nTotal amount to repay: £{total:.2f}")
    print(f"Amount to repay yearly: £{yearly_repay:.2f}")
    print(f"Amount to repay monthly: £{monthly_repay:.2f}")
    print("\nThank you for using the interest and loan calculator.")


# prints options for the user to choose.
choice = int(input("\nType (1) for investing\nType (2) for borrowing\nPlease choose an option: "))


# asks the user to choose either investing oe borrowing.
if choice == 1:
    investment()
if choice == 2:
    loan()
