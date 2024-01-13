# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 3
# output : * * *
#          * * *
#          * * *
#          * * *

def display (row,column):
    for i in range(row):
        for j in range(column):
            print('*',end='  ')
        print()
r1 = int(input())
c1 = int(input())
display(r1,c1)