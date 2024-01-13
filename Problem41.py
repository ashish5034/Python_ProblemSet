# Accept n number from user and accept no number from user and check whether no is present in it or not

def freq(data,no):
    count = 0
    for val in data:
        if(val==no):
            count=count+1
    if(count>0):
        print("Present")
    else:
        print("Not present")
dta = []
sz=int(input())
for i in range (sz):
    i=int(input())
    dta.append(i)
no = int(input())
freq(dta,no)