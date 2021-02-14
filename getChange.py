"""
Joshua Wren
26 January 2021
Cash Counter
"""

# A program to calculate the total value of a user's USD


def main():
    print("\n***** Cash Counter *****\n")
    print("Please enter the count of each type.")
    hundreds = int(input("Hundreds: "))
    fifties = int(input("Fifties: "))
    twenties = int(input("Twenties: "))
    tens = int(input("Tens: "))
    fives = int(input("Fives: "))
    ones = int(input("Ones: "))
    halfdollars = int(input("Half-Dollars: "))
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    billTotal = 100*hundreds + 50*fifties \
        + 20*twenties + 10*tens + 5*fives + ones
    changeTotal = .50*halfdollars + .25*quarters \
        + .10*dimes + .05*nickels + .01*pennies
    total = billTotal + changeTotal
    print(f"\nThe total value of your cash is ${total}.")


main()
