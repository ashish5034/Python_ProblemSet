# Accept n number from user and return product of all odd numbers
def product(data):
    x=1
    for val in data:
        if(val%2!=0):
            x = x*val
    return x

# product = lambda data:data%2!=0

data =[]
sz = int(input("Enter size of data : "))
for val in range(sz):
    val = int(input(f"Enter {val+1} th value: "))
    data.append(val)
print(f"Product of all odd number in list are {product(data)}")
# ans = list(filter(product,data))
# print(ans)