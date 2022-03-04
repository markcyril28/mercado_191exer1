#!/usr/bin/python3

# Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
# https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
# or like sw.PNG

def print_matrix1(a, x, y):
    print("\nGeneral Matrix: ")
    mrows = len(x)
    ncols = len(y)

    x_list = [" "]  # Adds the bases in x and y to the General Matrix
    y_list = [" ", " "]
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
    mrows = len(x)
    ncols = len(y)

    # initialize matrix to zeroes
    a = [0] * (mrows + 2)
    for i in range(mrows + 2):
        a[i] = [0] * (ncols + 2)
    # print_matrix(a,x,y)

    for i in range(1, mrows + 1):
        for j in range(1, ncols + 1):
            match = a[i - 1][j - 1] - match_score
            if (x[i - 1] == y[j - 1]):
                match = a[i - 1][j - 1] + match_score
            delete = a[i - 1][j] - gap_cost
            insert = a[i][j - 1] - gap_cost
            a[i][j] = max(match, delete, insert, 0)
    # print_matrix(a,x,y)
    return a


num_traceback = []
x_seq = []
bars = []
y_seq = []



def seq_alignment(a, x, y):
    # Locating the max_number in the matrix
    mrows = len(x)
    ncols = len(y)
    max_num = 0
    max_num_row = 0
    max_num_column = 0

    for row in range(mrows+1):      # Finding the max number
        for column in range(ncols+1):
            if max_num <= a[row][column]:
                max_num = a[row][column]
                max_num_row = row
                max_num_column = column
    num_traceback.append(max_num)
    row = max_num_row
    column = max_num_column

    while row > 0 or column > 0:  # Tracing back the  alignment
        upper = a[row - 1][column]
        left = a[row][column - 1]
        diagonal = a[row - 1][column - 1]
        greater_num = max(upper, left, diagonal)


        # Diagonal, Upper, or Left
        # Aligning x and y sequence
        if x[row-1] == y[column-1]:     # Matched
            num_traceback.append(greater_num)
            x_seq.append(x[row - 1])
            bars.append("|")
            y_seq.append(y[column - 1])
            row -= 1
            column -= 1
        elif greater_num == diagonal:   # Mismatched
            num_traceback.append(diagonal)
            x_seq.append(x[row - 1])
            bars.append(" ")
            y_seq.append(y[column - 1])
            row -= 1
            column -= 1
        elif greater_num == upper: # Insert in x_seq
            num_traceback.append(upper)
            x_seq.append(x[row - 1])
            bars.append(" ")
            y_seq.append("-")
            row -= 1
        elif greater_num == left: # Insert in y_seq
            num_traceback.append(left)
            x_seq.append("-")
            bars.append(" ")
            y_seq.append(y[column - 1])
            column -= 1
    num_traceback.pop(-1)
    # Reversing the lists
    num_traceback.reverse()
    x_seq.reverse()
    bars.reverse()
    y_seq.reverse()
    return num_traceback, x_seq, bars, x_seq


def print_seq_alignment(num_traceback, x_seq, bars, y_seq):
    for num in num_traceback:
        print(num, end="	")
    print()
    for base in y_seq:
        print(base, end="	")
    print()
    for bar in bars:
        print(bar, end="	")
    print()
    for base in x_seq:
        print(base, end="	")
    print()

"""
x = "TAGGTTGACTAGACATATATTA"
y = "GGTGTTACGGGAATATTATTA"


x = "GGTTGACTA" # nine rows
y = "TGTTACGG"	# eight columns

x = "GGGTTGACTAGGTTGACTA"
y = "GTGTTACGGTGTTACGG"

"""
x = "GGGGTTGACTATGTTTTGHHHHHHAGGGGGGGGGGGGGGGTTTTTTTTTGACGACGACTTTTTTTTTTT"
y = "GGGGTTGACGACGACGACTATGTTGGTJJJJJJJJJJJJJJJJJJJJGACACTGGTTTTTTTTTTTTTTT"


a = gen_matrix(x, y)
seq_alignment(a, x, y)
print_matrix1(a, x, y)

print("\nSequence Alignment with corresponding Traceback number: ")
print_seq_alignment(num_traceback, x_seq, bars, y_seq)

# working