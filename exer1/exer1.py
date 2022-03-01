#!/usr/bin/python3

#Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
#https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
#or like sw.PNG

def print_matrix1(a,x,y):
	mrows = len(x)
	ncols = len(y)

	for i in range(mrows):
		for j in range(ncols):
			print("%2d" % a[i][j], end=' ')
		print()


def gen_matrix(x, y, match_score=3, gap_cost=2):
	mrows = len(x)
	ncols = len(y)

	#initialize matrix to zeroes
	a = [0] * (mrows + 1)
	for i in range(mrows + 1):
		a[i] = [0] * (ncols + 1)
	
	#print_matrix(a,x,y)
	
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			match = a[i-1][j-1] - match_score
			if(x[i-1] == y[j-1]):
				match = a[i-1][j-1] + match_score
			delete = a[i - 1][j] - gap_cost
			insert = a[i][j - 1] - gap_cost
			a[i][j]=max(match,delete,insert,0)

	#print_matrix(a,x,y)	
	return(a)




x = "GGTTGACTA"	
y = "TGTTACGG"

a=gen_matrix(x,y)

print_matrix1(a,x,y)

print("")

mrows = len(x)
ncols = len(y)
max_num = 0
x_seq = []
bar_line = []
y_seq = []

for row in range(mrows):
	for column in range(ncols):
		if max_num <= a[row][column]:
			max_num = a[row][column]

			max_num_row = row
			max_num_column = column

			upper = a[row-1][column]
			left = a[row][column-1]
			diagonal = a[row-1][column-1]

# The list of sequence
x_seq.append(x[max_num_row-1])
bar_line.append("|")
y_seq.append(y[max_num_column-1])
print("")
print(x_seq)
print(bar_line)
print(y_seq)

# Finding the max number
print(max_num)

# Printing the aligned nucleotide based on the max number
print("")
print(str(max_num_row) + " " + str(max_num_column))


print(x[max_num_row-1])
print(y[max_num_column-1])

# Comparing the Upper, Left, and Diagonal

print("")
print(upper)
print(left)
print(diagonal)

