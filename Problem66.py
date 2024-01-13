# Accept number of rows and number of columns from user and display below pattern
# imput : rows = 4 & column = 4
# output : 2 4 6 8   
#          1 3 5 7 
#          2 4 6 8  
#          1 3 5 7 

def display(rows, columns):
    
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            if(i%2!=0):
                print(j*2,end='  ')
            elif(i%2==0):
                print((j*2-1),end='  ')
        print()

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))
display(rows, columns)
