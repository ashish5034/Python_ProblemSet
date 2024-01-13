# Accept number from user and print below pattern
# Input = 8
# Output = 2 4 6 8 10 12 14 16
def dis(n):
    for i in range(2,n*2+1,2):
        print(i, end=' ')
def display(n):
    for i in range(1,n+1):
        print(i*2, end=' ')
n = int(input())
dis(n)
print()
display(n)