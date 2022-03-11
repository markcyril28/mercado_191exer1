#!/usr/bin/python3

# Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
# https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
# or like sw.PNG

def print_matrix1(a, x, y):
    print("\nGeneral Matrix: ")
    mrows, ncols = len(x), len(y)

    x_list, y_list = [" "], [" ", " "]  # Adds the bases in x and y to the General Matrix
    for base in x:
        x_list.append(base)
    for base in y:
        y_list.append(base)

    a.insert(0, y_list)  # Add the bases in y in the first row
    for i, base in zip(range(1, mrows + 2), x_list):  # Add the bases in x every row and in every first item
        a[i].insert(0, base)

    for i in range(mrows + 2):
        for j in range(ncols + 2):
            print(a[i][j], end='	')
        print()


def gen_matrix(x, y, match_score=3, gap_cost=2):
    mrows, ncols = len(x), len(y)

    a = [0] * (mrows + 1)  # initialize matrix to zeroes
    for i in range(mrows + 1):
        a[i] = [0] * (ncols + 1)

    for i in range(1, mrows + 1):  # print_matrix(a,x,y)
        for j in range(1, ncols + 1):
            match = a[i - 1][j - 1] - match_score
            if x[i - 1] == y[j - 1]:
                match = a[i - 1][j - 1] + match_score
            delete = a[i - 1][j] - gap_cost
            insert = a[i][j - 1] - gap_cost
            a[i][j] = max(match, delete, insert, 0)
    return a


num_traceback = []
x_seq = []
bars = []
y_seq = []


def local_align(a, x, y):
    mrows, ncols = len(x), len(y)
    max_score, max_score_row, max_score_column = 0, 0, 0

    for row in range(mrows+1):  # Finding the max num
        for column in range(ncols+1):
            if max_score <= a[row][column]:
                max_score = a[row][column]
                max_score_row, max_score_column = row, column

    row, column = max_score_row, max_score_column

    while a[row][column] != 0:  # Tracing back the global alignment
        num_current = a[row][column]
        upper = a[row - 1][column]
        left = a[row][column - 1]
        diagonal = a[row - 1][column - 1]
        greater_num = max(upper, left, diagonal, 0)

        if x[row - 1] == y[column - 1]:  # Matched
            num_traceback.append(num_current)
            x_seq.append(x[row - 1])
            bars.append("|")
            y_seq.append(y[column - 1])
            row -= 1
            column -= 1
        elif greater_num == diagonal:  # Mismatched
            num_traceback.append(num_current)
            x_seq.append(x[row - 1])
            bars.append(" ")
            y_seq.append(y[column - 1])
            row -= 1
            column -= 1
        elif greater_num == upper:  # Insert in x_seq
            num_traceback.append(num_current)
            x_seq.append(x[row - 1])
            bars.append(" ")
            y_seq.append("-")
            row -= 1
        elif greater_num == left:  # Insert in y_seq
            num_traceback.append(num_current)
            x_seq.append("-")
            bars.append(" ")
            y_seq.append(y[column - 1])
            column -= 1

    num_traceback.reverse()  # Reversing the Lists
    x_seq.reverse()
    bars.reverse()
    y_seq.reverse()
    print("\nLocal Alignment with corresponding Traceback number: ")
    print_seq_align(num_traceback, x_seq, bars, y_seq)
    print()

def global_align(a, x, y):
    mrows, ncols = len(x), len(y)

    max_score, max_score_row, max_score_column = 0, 0, 0
    for row in range(mrows+1):  # Finding the max num
        for column in range(ncols+1):
            if max_score <= a[row][column]:
                max_score = a[row][column]
                max_score_row, max_score_column = row, column


    row, column = mrows, ncols

    while row > 0 or column > 0:  # Tracing back the global alignment
        num_current = a[row][column]
        upper = a[row - 1][column]
        left = a[row][column - 1]
        diagonal = a[row - 1][column - 1]
        greater_num = max(upper, left, diagonal, 0)

        if x[row - 1] == y[column - 1]:  # Matched
            num_traceback.append(num_current)
            x_seq.append(x[row - 1])
            bars.append("|")
            y_seq.append(y[column - 1])
            row -= 1
            column -= 1
        elif greater_num == diagonal:  # Mismatched
            num_traceback.append(num_current)
            x_seq.append(x[row - 1])
            bars.append(" ")
            y_seq.append(y[column - 1])
            row -= 1
            column -= 1
        elif greater_num == upper:  # Insert in x_seq
            num_traceback.append(num_current)
            x_seq.append(x[row - 1])
            bars.append(" ")
            y_seq.append("-")
            row -= 1
        elif greater_num == left:  # Insert in y_seq
            num_traceback.append(num_current)
            x_seq.append("-")
            bars.append(" ")
            y_seq.append(y[column - 1])
            column -= 1

    num_traceback.reverse()  # Reversing the Lists
    x_seq.reverse()
    bars.reverse()
    y_seq.reverse()

    print("\nGlobal Alignment with corresponding Traceback number: ")
    print_seq_align(num_traceback, x_seq, bars, y_seq)
    print()


def print_seq_align(num_traceback, x_seq, bars, y_seq):
    for num in num_traceback:
        print(num, end="	")
    print()
    for base in x_seq:
        print(base, end="	")
    print()
    for bar in bars:
        print(bar, end="	")
    print()
    for base in y_seq:
        print(base, end="	")


x = "GGTTGACTA"
y = "TGTTACGG"

a = gen_matrix(x, y)
print_matrix1(a, x, y)

a = gen_matrix(x, y)
local_align(a, x, y)

num_traceback.clear()
x_seq.clear()
bars.clear()
y_seq.clear()

global_align(a, x, y)


