# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 3
# output : A B C  
#          A B C  
#          A B C  
#          A B C  

def display(rows, columns):
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            char = chr(ord('A') + j - 1)
            print(char, end=' ')
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)
