# Accept the number from user and display below pattern
# input = 4
# output = A B C D
def display(n):
    for i in range(n):
        # Convert ASCII value to get the corresponding alphabet letter
        char = chr(ord('A') + i)
        print(char, end=' ')

n = int(input("Enter a number: "))
display(n)
