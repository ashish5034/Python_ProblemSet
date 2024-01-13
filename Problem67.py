# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 3
# output : 1  2  3  
#          4  5  6  
#          7  8  9 
#          1  2  3

def display(rows, columns):
    n= 1
    for i in range(rows):
        for j in range(columns):
            if n>9:
                n =1
            
            print(n, end='  ')
            n= n+1
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)
