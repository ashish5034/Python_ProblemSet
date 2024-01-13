# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 3
# output : 1 1 1  
#          2 2 2 
#          3 3 3 
#          4 4 4 

def display (row,column):
    for i in range(1,row+1,1):
        for j in range(1,column+1,1):
            print(i,end='  ')
        print()
r1 = int(input("Number of Rows : "))
c1 = int(input("Number of Columns : "))
display(r1,c1)