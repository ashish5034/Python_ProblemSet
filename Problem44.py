# Accept n number from user and accept range, display all element from that range
def ele(data,strpt, endpt):
    list = []
    for val in data:
        if(val>strpt and val < endpt):
            list.append(val)
    return list

dta = []
sz = int(input())
for val in range(sz):
    val = int(input())
    dta.append(val)
print(dta)
startpoint = int(input("Enter start point: "))
endpoint = int(input("Enter end point: "))

print(ele(dta, startpoint, endpoint))