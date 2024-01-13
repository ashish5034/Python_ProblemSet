# Accept n numbers from user and display summation of digit of each number
def sumofalldigit(data):
    summation = []
    for val in data:
        sum = 0
        while(val!=0):
            digit = val%10
            sum = sum + digit
            val = val//10
        summation.append(sum)
    return summation


data = []
size = int(input())
for val in range(size):
    val = int(input())
    data.append(val)
print(data)
addition = sumofalldigit(data)
print(addition)