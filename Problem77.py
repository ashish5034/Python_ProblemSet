# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 4
# output : * * * *   
#          * * *
#          * * 
#          * 

def display(rows, columns):
    for i in range(rows,0,-1):
        for j in range(1, i + 1):
            print('*',end=' ')
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)

