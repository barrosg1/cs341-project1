"""
Run from standard input using pipe:
    cat test_cases.txt | python p1_18s.py -

    -> use (-) at the end

Run from user input:
    python p1_18s.py

Display output to output.txt
cat test_cases.txt | python p1_18s.py - > output.txt

"""

import sys
import string


def read_user_input():
    """
    function to read from standard input from user
    :return:
    """
    while True:
        user_input = raw_input("Would you like to enter a string? \n")

        if user_input == 'y':
            aString = raw_input("Enter a string:\n")
            process_string(aString)

        elif user_input == "n":
            break

        else:
            print "Invalid option."


def read_stdin():
    """
    function to read from standard input from the tests_cases.txt file
    :return:
    """
    infile = sys.stdin
    for line in infile:
        stdin = line.lower().strip('\n')

        print "Would you like to enter a string?"

        if stdin == 'y':
            print stdin
            print "Enter a string: "
            aString = next(infile)
            print aString
            process_string(aString)

        elif stdin == 'n':
            print stdin
            break

        else:
            print "Invalid option"


def process_string(aString):
    aString = aString.lower().translate( None, string.whitespace)

    roman_letters = string.ascii_lowercase

    # accept states: 8, 9, 11, 14, 15
    # trap states: 16, 17

    state = 0
    accept = False

    print aString

    print "Initial state q" + str(state)

    for s in aString:
        accept = False

        if state == 0:
            if s == 'w':
                state = 1
            elif s in roman_letters:
                state = 2
            else:
                state = 16

        elif state == 1:
            if s == 'w':
                state = 4
            elif s in roman_letters:
                state = 2
            elif s == '.':
                state = 3
            else:
                state = 16

        elif state == 2:
            if s == '.':
                state = 3
            elif s in roman_letters:
                state = 2
            else:
                state = 16

        elif state == 3:
            if s == 'c':
                state = 5
            else:
                state = 16

        elif state == 4:
            if s == 'w':
                state = 6
            elif s in roman_letters:
                state = 2
            elif s == '.':
                state = 3
            else:
                state = 16

        elif state == 5:
            if s == 'o':
                accept = True
                state = 8
            else:
                state = 16

        elif state == 6:
            if s == '.':
                state = 7
            elif s in roman_letters:
                state = 2
            else:
                state = 16

        elif state == 7:
            if s == 'c':
                state = 10
            elif s in roman_letters:
                state = 2
            else:
                state = 16

        elif state == 8:
            if s == 'm':
                accept = True
                state = 9
            else:
                state = 16

        elif state == 9:
            if s == '.':
                state = 12
            else:
                state = 17

        elif state == 10:
            if s == 'o':
                accept = True
                state = 11
            elif s in roman_letters:
                state = 2
            else:
                state = 16

        elif state == 11:
            if s == 'm':
                accept = True
                state = 15
            elif s in roman_letters:
                state = 2
            elif s == '.':
                state = 3
            else:
                state = 16

        elif state == 12:
            if s == 'c':
                state = 13
            else:
                state = 17

        elif state == 13:
            if s == 'o':
                accept = True
                state = 14
            else:
                state = 17

        elif state == 14:
                state = 17

        elif state == 15:
            if s == '.':
                state = 3
            elif s in roman_letters:
                state = 2
            elif s == '.':
                state = 12
            else:
                state = 16

        print s + " ---> state q" + str(state)

    if accept is True:
        print "Accepted!\n"
    else:
        print "Rejected!\n"


if __name__ == '__main__':
    if sys.argv[-1] == '-':
        read_stdin()
    else:
        read_user_input()
