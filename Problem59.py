# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 3
# output : * # *
#          * # *
#          * # *
#          * # *

def display (row,column):
    for i in range(row):
        for j in range(1,column+1):
            if(j%2==0):
                print('#',end='  ')
            else:
                print('*',end='  ')
        print()
r1 = int(input("Number of Rows : "))
c1 = int(input("Number of Columns : "))
display(r1,c1)