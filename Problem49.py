# Accept n number from user and display all such number which contain 3 digit in it
# threedigitno = lambda data:(data>99) and (data<1000)
def threedig(data):
    list1=[]
    for val in data:
        if(val>99 and val<1000):
            list1.append(val)
    return list1

data = []
size = int(input())
for val in range(size):
    val = int(input())
    data.append(val)
print(data)

# ans = list(filter(threedigitno,data))
# print(ans)
ans = threedig(data)
print(ans)