# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 4
# output : A B C  D
#          A B C  D
#          A B C  D
#          A B C  D

def display(rows, columns):
    for i in range(1, rows + 1):
        for j in range(0, columns):
            char = chr(ord('A') + j)
            print(char, end='  ')
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)
