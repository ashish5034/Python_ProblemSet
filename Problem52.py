# Accept the nuber from user and display below pattern 
# input = 5
# Output = 5 # 4 # 3 # 2 # 1 #
def display(n):
    # i=1
    for i in range(n,0,-1):
        print(i, '#',end=' ')
n = int(input())
display(n)