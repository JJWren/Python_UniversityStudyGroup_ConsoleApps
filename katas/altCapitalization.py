'''
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.
'''


def altCapital(string):
    string = string.lower()
    alt1 = []
    alt2 = []
    index = 0

    for char in string:
        if index % 2 == 0:
            alt1.append(char.upper())
            alt2.append(char.lower())
        else:
            alt2.append(char.upper())
            alt1.append(char.lower())
        index += 1

    strAlt1 = ""
    strAlt2 = ""
    for letter in alt1:
        strAlt1 += letter
    for letter in alt2:
        strAlt2 += letter
    return strAlt1, strAlt2


print(altCapital("abcdef"))
