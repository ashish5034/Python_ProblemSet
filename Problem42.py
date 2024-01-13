# Accept n number from user and accept one another number as no. , return index of its first occurence of that number 
def occurance(dta,n):
    index = dta.index(n)
    return index
            
data =[]
sz=int(input())
for val in range(sz):
    val = int(input())
    data.append(val)
no =int(input())
try:
    print(occurance(data,no))
except ValueError:
    print(f"{no} is not in list")