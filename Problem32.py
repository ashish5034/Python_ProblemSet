# accept n  umber from user and display such elements which are divisible by 5

divbyfive = lambda no:(no%5==0)

def div5(list):
    l1 = []
    for val in list:
        if(val%5==0):
            l1.append(val)
            
    return l1

dta = []
print("Enter size of list")
size = int(input())
for val in range (size):
    val =int(input())
    dta.append(val)
print(dta)

ans = list(filter(divbyfive,dta))
print(ans)

res = div5(dta)
print(res)