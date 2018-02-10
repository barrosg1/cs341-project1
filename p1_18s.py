"""
Name: Gabriel Barros
NJIT UCID: 31248845


Run from standard input using pipe:
    cat test_cases.txt | python p1_18s_31248845.py -

    -> use (-) at the end

Run from user input:
    python p1_18s_31248845.py

Display output to output.txt
cat test.txt | python p1_18s_31248845.py - >> output.txt

"""

import sys
import string

print "Project 1 for CS 341"
print "Written by: Gabriel Barros, 31248845"
print "Instructor: Marvin Nakayama, marvin@njit.edu \n"


def read_user_input():
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
    infile = sys.stdin
    for line in infile:
        stdin = line.lower().strip('\n')

        if stdin == 'y':
            aString = next(infile)
            process_string(aString)

        elif stdin == 'n':
            print stdin
            break

        else:
            print "Invalid option"


def process_string(aString):
    aString = aString.translate( None, string.whitespace)
    print aString

    roman_letters = string.ascii_lowercase

    state = 0
    print "Initial state q" + str(state)

    accept = False

    # accept states: 8, 9, 11, 14, 15
    # Trap states: 16, 17

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
            elif s == '.':
                state = 12
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
                state = 12
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
            if s == 'm':
                accept = True
                state = 9
            else:
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
