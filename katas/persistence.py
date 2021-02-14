'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.
'''

'''
Examples:
persistence(39) => 3 Because 3*9=27, 2*7=14, 1*4=4
persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126
persistence(4) => 0   # Because 4 is already a one-digit number.
'''


def persistence(integer):
    # simple input check
    if integer != int(integer):
        return f"{integer} is not a valid input."
    else:
        # if negative, remove negative for string conversion; result is same
        if integer < 0:
            integer *= -1

        # covert to string (to find length)
        intToStr = str(integer)
        # count to track persistence
        count = 0

        while len(intToStr) > 1:
            # inc count for each while loop iteration
            count += 1

            numArr = []
            for num in intToStr:
                numArr.append(int(num))

            # get product of integer
            arrProduct = 1
            for num in numArr:
                arrProduct *= num

            # reset intToStr
            intToStr = str(arrProduct)

        return count


# Given Tests:
print(persistence(39))
print(persistence(999))
print(persistence(4))

# Extra Tests:
print(persistence('500'))
print(persistence(5.2))
print(persistence(-521))
