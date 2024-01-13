# Accept n number from user and accept one another number as no, return frequency of no from it 
def freq(dta,no):
    count=0
    for val in dta:
        if(val==no):
            count=count+1
    return count

data =[]
sz =int(input())
for val in range(sz):
    val = int(input())
    data.append(val)
no=int(input())
print(freq(data,no))