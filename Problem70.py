# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 4
# output : 1 2 3 4  
#          2 3 4 5
#          3 4 5 6   
#          4 5 6 7  

def display(rows, columns):
    n=1
    for i in range(1,rows+1):
        no =i
        for j in range(1,columns+1):
            print(no,end='  ')
            no = no +1
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)
