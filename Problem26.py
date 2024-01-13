# write a program which accept number from user and return the count of even digits
def evenCount(ino):
    count = 0
    while(ino != 0):
        idigit = ino %10
        if(idigit % 2 == 0):
            count = count + 1
        ino = ino //10
    return count
def main():
    print("Enter number: ")
    ival = int(input())
    iret = evenCount(ival)
    print(iret)
if __name__ == "__main__":
    main()