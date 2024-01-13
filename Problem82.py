# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 4
# output : * * * # 
#          * * # @
#          * # @ @
#          # @ @ @

def display(rows, columns):
    for i in range(1,rows+1,1):
        for j in range(1, columns + 1):
            if i+j==rows+1:
                print('#',end='  ')
            elif i+j<=rows:
                print('*',end='  ')
            else:
                print('@',end='  ')
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)

