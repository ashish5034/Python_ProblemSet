# Accept number from user and check whether that number is contains 11 in it or not
def chk(no):
    count = 0
    for val in no:
        if(val==11):
            count =count+1
    if(count>0):
        print("11 is present ")
    else:
        print("11 is not present")
            
data = []
size = int(input())
for val in range(size):
    val =int(input())
    data.append(val)
    
chk(data)