# Accept n number from user and return frequency of even number
# even = lambda no:(no%2==0)

def even(no):
    d =[]
    count = 0
    for val in no:
        if(val%2==0):
            count = count +1
            # d.append(val)
    return count
data =[]
size = int(input())
for val in range (size):
    val = int(input())
    data.append(val)
# evenno = list(filter(even,data))

# print(len(evenno))
print(even(data))