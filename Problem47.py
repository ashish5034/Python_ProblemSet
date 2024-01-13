# Accept number from user and return difference of the largest and smallest number 
# def smallNo(data):
    # smallest = data[0]
    # for val in data:
    #     if val < smallest:
    #         smallest = val
    # return smallest
    # return min(data)

small = lambda data:min(data)

big = lambda data:max(data)

# def bigno(data):
    # largest = data[0]
    # for val in data:
    #     if val > largest:
    #         largest = val
    # return largest
    # return max(data)
def main():
    data=[]
    siz = int(input("Enter list size: "))
    for val in range (siz):
        val =int(input(f"Enter {val+1}th value: "))
        data.append(val)
    print(data)
    # print(smallNo(data))
    # print(bigno(data))
    ans=small(data)
    print(ans)
    ans2=big(data)
    print(ans2)
if __name__ == "__main__":
    main()