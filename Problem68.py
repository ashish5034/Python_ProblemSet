# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 4
# output : a b c d
#          1 2 3 4
#          a b c d  
#          1 2 3 4

def display(rows, columns):
    
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            if(i%2!=0):
                ch = chr(ord('a')+j-1)
                print(ch,end='  ')
            elif(i%2==0):
                print(j,end='  ')
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)
