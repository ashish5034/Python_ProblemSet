# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 3
# output : A A A 
#          B B B
#          C C C
#          D D D

def display(rows, columns):
    for i in range(0, rows):
        for j in range(0, columns):
            char = chr(ord('A') + i)
            print(char, end='  ')
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)
