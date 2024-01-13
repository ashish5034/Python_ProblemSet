# accept number from user and disply such elements which are divisible by 3 and 5 
divby3 = lambda no:(no%3==0)
divby5 = lambda no:(no%5==0)
divbyboth = lambda no:(no%3==0 and no%5==0)

data = []
size = int(input())
for val in range (size):
    val = int(input())
    data.append(val)
print(data)

ans1 = list(filter(divby3,data))
ans2 = list(filter(divby5,data))
ans3 = list(filter(divbyboth,data))

print(ans1,ans2,ans3)