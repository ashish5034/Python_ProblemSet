# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 3
# output : 1 2 3
#          1 2 3
#          1 2 3
#          1 2 3

def display (row,column):
    for i in range(row):
        for j in range(column):
            print(j,end='  ')
        print()
r1 = int(input("Number of Rows : "))
c1 = int(input("Number of Columns : "))
display(r1,c1)