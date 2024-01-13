# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 3
# output : 3 2 1 
#          3 2 1 
#          3 2 1 
#          3 2 1 

def display (row,column):
    for i in range(row):
        for j in range(column,0,-1):
            print(j,end='  ')
        print()
r1 = int(input("Number of Rows : "))
c1 = int(input("Number of Columns : "))
display(r1,c1)