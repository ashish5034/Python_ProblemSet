# Accept n  umber from user and return frequency of 11 from it
def count11(no):
    count =0
    for val in no:
        if(val==11):
            count = count +1
    return count            
data = []
size = int(input())
for val in range (size):
    val = int(input())
    data.append(val)
print(count11(data))