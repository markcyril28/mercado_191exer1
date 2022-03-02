#!/usr/bin/python3

#Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
#https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
#or like sw.PNG

def print_matrix1(a,x,y):
	mrows = len(x)
	ncols = len(y)
	print("Query sequences: ")
	for base in x:
		print(base, end=" ")
	print()
	for base in y:
		print(base, end=" ")
	print()
	
	print("\nMatrix: ")
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


a = gen_matrix(x,y)


print_matrix1(a,x,y)

print()

num_traceback =[]
x_seq = []
bars = []
y_seq = []


def seq_alignment(a,x,y):
	# Locating the max_number in the matrix
	mrows = len(x)
	ncols = len(y)
	max_num = 0
	max_num_row = 0
	max_num_column = 0
	for row in range(mrows):
		for column in range(ncols):
			if max_num <= a[row][column]:
				max_num = a[row][column]
				max_num_row = row
				max_num_column = column


	num_traceback.append(max_num)
	row = max_num_row
	column = max_num_column

	# Tracing back the global alignment
	while row > 0 and column > 0:
		upper = a[row - 1][column]
		left = a[row][column - 1]
		diagonal = a[row - 1][column - 1]
		greater_num = max(upper, left, diagonal, 0)

		if greater_num > 0:
			num_traceback.append(greater_num)

		if greater_num == diagonal:
			x_seq.append(x[row-1])
			bars.append("|")
			y_seq.append(y[column-1])
			row -= 1
			column -= 1
		elif greater_num == upper:
			x_seq.append(x[row-1])
			bars.append(" ")
			y_seq.append("-")
			row -= 1
		elif greater_num == left:
			x_seq.append("-")
			bars.append(" ")
			y_seq.append(y[column-1])
			column -= 1
	print("Maximum Number: ")
	print(max_num)

	# Reversing the Lists
	num_traceback.reverse()
	x_seq.reverse()
	bars.reverse()
	y_seq.reverse()

def print_seq_alignment(num_traceback,x, y, x_seq, bars, y_seq):
	print("\nQuery sequences: ")
	for base in x:
		print(base, end=" ")
	print()
	for base in y:
		print(base, end=" ")
	print()

	print("\nSequence alignment with corresponding Traceback number: ")
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

seq_alignment(a,x,y)


print_seq_alignment(num_traceback, x, y, x_seq, bars, y_seq)
