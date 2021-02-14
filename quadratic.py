"""
Joshua Wren
26 January 2021
Quadratic Equation Solver
"""

# A program that calculates the real roots of a quadratic equation.
# Uses the Python Math library.

import math


def main():
    print("\n***** Quadratic Equation Calculator *****\n")
    print("This program finds the real solutions to a quadratic.")

    nonreal = True
    while nonreal == True:
        a = float(input("\nEnter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))

        discrim = b * b - 4 * a * c
        if discrim > 0:
            discRoot = math.sqrt(discrim)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b - discRoot) / (2 * a)

            print(f"\nThe solutions are: {root1}, {root2}")
            nonreal = False
        elif discrim == 0:
            root = -b / (2 * a)

            print(f"\nThere is a double root at {root}.")
            nonreal = False
        else:
            print("\nThe inputs lead to a non-real root.")

            tryagain = input(
                "Enter anything to try again. Otherwise, press 'Enter' to quit: ")
            if tryagain == '':
                nonreal = False
    print("\n***** End of Program *****")


if __name__ == '__main__':
    main()
