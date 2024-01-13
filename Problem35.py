# accept n number from user and display such elements wich are multiple by 11
divby11 = lambda no:(no%11==0)
def div(no):
    dta = []
    for val in no:
        if val%11==0:
            dta.append(val)
    return dta
data = []
size=int(input())
for val in range (size):
    val=int(input())
    data.append(val)
print(data)
ans = list(filter(divby11,data))
print(ans)
res = div(data)
print(res)