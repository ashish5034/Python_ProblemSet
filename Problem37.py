# Accept n number from user and return difference between frequency of even number and odd number
even = lambda list:(list%2==0)
odd=lambda list:(list%2!=0)


data = []
size = int(input())
for val in range (size):
    val = int(input())
    data.append(val)
    
ans1 = list(filter(even,data))
ans2 = list(filter(odd,data))

diff = len(ans1)-len(ans2)
print(diff)