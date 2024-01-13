# Accept the nuber from user and display below pattern 
# input = 5
# Output = 1 * 2 * 3 * 4 * 5 *
def display(n):
    # i=1
    for i in range(1,n+1,1):
        print(i, '*',end=' ')
n = int(input())
display(n)