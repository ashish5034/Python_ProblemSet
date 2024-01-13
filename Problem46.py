# Accept n number from user and return the largest number
def largnum(data):
    num = data[0]  # Initialize num with the first element in the list
    # for index in range(len(data) - 1):
    for val in data:
        # if data[index] > data[index + 1]:
        if num < val:
            num=val
            # num = data[index]
    return num

data = []
sz = int(input("Enter size of the list: "))
for val in range(sz):
    val=int(input(f"Enter {val+1}th element: "))
    data.append(val)
print(f"largest number in list is {largnum(data)}")