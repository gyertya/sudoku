import time
import sys
import copy
import os


def print_table():  # ez printeli ki a tablat
    os.system('clear')
    print("     ", end='')
    for i in range(0, 9):
        print('\033[1m\033[93m%2s' % str(xsorozat[i])+' \033[0m', end='')
        if i % 3 - 2 == 0 and i < 7:
            print('\033[1m|\033[0m', end='')
    print('\n', '\n', '\n', end='')

    for i in range(0, 9):
        print('\033[1m\033[93m%2s' % str(yoszlop[i])+'   \033[0m', end='')
        for j in range(0, 9):
            if elements[i][j] == 0:
                print('%3s' % ' \033[41m_\033[0m '+'', end='')
            if elements_original[i][j] != 0:
                print('\033[92m%2s' % str(elements[i][j])+' \033[0m', end='')
            elif elements_original[i][j] == 0 and elements[i][j] != 0:
                print('\033[31m%2s' % str(elements[i][j])+' \033[0m', end='')
            if j % 3 - 2 == 0 and j < 7:
                print('\033[1m|\033[0m', end='')
        print('\n''\n', end='')
        if i % 3 - 2 == 0:
            print('\033[1m\n\033[0m', end='')


def input_new_element():
    global elements  # watch out!
    new_ok = True
    try_again = ''
    while new_ok:
        new_ok = False
        new_element = input(
            try_again +
            'Please add your number and a row, colomn number (eg: 111). (\033[1mE\033[0mxit, \033[1mC\033[0mlearAll): ')
        try_again = ''
        if new_element.upper() == 'E':
            sys.exit('User quit. Oh, no! Why did you give up? :(')
        if new_element.upper() == 'C':
            if input('Are you sure (\033[1mY\033[0mes)? ').upper() == 'Y':
                elements = copy.deepcopy(elements_original)  # the reason why elements is global
                print_table()
            else:
                new_ok = False
                try_again = ''
        try:
            int(new_element)
        except ValueError:
            new_ok = True
        if not new_ok:
            if (int(new_element) < 11) or (int(new_element) > 999):
                try_again = 'Try again! '
                new_ok = True
            else:
                return new_element


def small_check(new_ERC):
    if int(new_ERC[0]) == 0:
        return True
    non_zero = [0] * 9
    row_nr = int(new_ERC[1])
    colomn_nr = int(new_ERC[2])
    if row_nr % 3 == 0:
        first_row_in_small = (row_nr // 3 - 1) * 3
    else:
        first_row_in_small = (row_nr // 3) * 3
    if (colomn_nr % 3) == 0:
        first_colomn_in_small = (colomn_nr // 3 - 1) * 3
    else:
        first_colomn_in_small = (colomn_nr // 3) * 3
    for i in range(first_row_in_small, first_row_in_small + 3):
        for j in range(first_colomn_in_small, first_colomn_in_small + 3):
            if elements[i][j] != 0:
                non_zero[elements[i][j] - 1] = 1
    if (non_zero[int(new_ERC[0]) - 1]) == 0:
        return True
    else:
        return False


def row_colomn_check(new_ERC):
    if int(new_ERC[0]) == 0:
        return True
    row_nr = int(new_ERC[1])
    colomn_nr = int(new_ERC[2])

    for j in range(0, 9):
        if (str(elements[row_nr - 1][j])) == new_ERC[0]:
            return False
    for i in range(0, 9):
        if (str(elements[i][colomn_nr - 1])) == new_ERC[0]:
            return False
    return True


def modify_element(change):
    if elements_original[int(change[1]) - 1][int(change[2]) - 1] == 0:
        elements[int(change[1]) - 1][int(change[2]) - 1] = int(change[0])
    else:
        print("You can't modify that number! Try again!")
        time.sleep(3)


def steps_left():
    x = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if elements[i][j] == 0:
                x += 1
    return x


# elements_original = [
#     [5,3,0,0,7,0,0,0,0],
#     [6,0,0,1,9,5,0,0,0],
#     [0,9,8,0,0,0,0,6,0],
#     [8,0,0,0,6,0,0,0,3],
#     [4,0,0,8,0,3,0,0,1],
#     [7,0,0,0,2,0,0,0,6],
#     [0,6,0,0,0,0,2,8,0],
#     [0,0,0,4,1,9,0,0,5],
#     [0,0,0,0,8,0,0,7,9]]

# DEMO LINE====================================================
# 511 248 645 277 492

elements_original = [
    [0, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 0, 1, 4, 0, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 0, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 5, 2, 8, 6, 1, 7, 9]]
# ==============================================================
elements = copy.deepcopy(elements_original)

xsorozat = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
yoszlop = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print_table()

while steps_left() != 0:
    new_tip = input_new_element()
    if small_check(new_tip) and row_colomn_check(new_tip):
        modify_element(new_tip)
    else:
        print('Something not okay...')
        time.sleep(3)
    print_table()

print('Congrats, you did it!')
