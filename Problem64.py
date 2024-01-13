# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 3
# output : 4 4 4 
#          3 3 3 
#          2 2 2 
#          1 1 1

def display(rows, columns):
    for i in range(rows,0,-1):
        for j in range(0, columns):
            print(i, end='  ')
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)
