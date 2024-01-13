# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 4
# output : *  * *  *  
#          *  @ @  *
#          *  @ @  *
#          *  * *  *

def display(rows, columns):
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if i==1 or i==rows or j==1 or j==columns:
                print('*', end='   ')
            else:
                print('@', end='   ')
        print()
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)

