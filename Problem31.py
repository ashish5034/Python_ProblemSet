# accept n number from user and return diff between summation of even elements and summation of odd elemlis
def evenno(no):
    evenno = []
    for val in no:
        if val % 2 == 0:
            evenno.append(val)
    return evenno

chkeven = lambda no:(no%2==0)

def oddno(no):
    oddno = []
    for val in no:
        if(val % 2 != 0):
            oddno.append(val)
    return oddno

def addeven(even):
    sum = 0
    for val in even:
        sum =sum+val
    return sum

def addodd(odd):
    sum = 0
    for val in odd:
        sum = sum + val
    return sum

def diff(no1,no2):
    diff = 0
    diff = no1 - no2
    return diff
        
data = []
print("Enter number of elements want to add in list")
sizeoflist = int(input())
for i in range(sizeoflist):
    num = int(input())
    data.append(num)
print("Input List is = ",data)
res1 = evenno(data)
print(res1)
res2 = oddno(data)
print(res2)
sumre1 = addeven(res1)
print(sumre1)
sumre2=addodd(res2)
print(sumre2)
difference = diff(sumre1,sumre2)
print(difference)