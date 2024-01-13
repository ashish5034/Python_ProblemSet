# Accept the number from user and return difference of the largest and smallest number 
small = lambda data:min(data)
big = lambda data:max(data)
diff = lambda n1,n2:(n1-n2)        

numbers = []
size = int(input("Enter the size of the list : "))
for val in range (size):
    val = int(input())
    numbers.append(val)
print(numbers)

ans1 = small(numbers)
ans2 = big(numbers)
ans3 = diff(ans1,ans2)
print(ans3)