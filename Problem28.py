# write a program which accept number from user and return the count of inbetween 3 and 7
def evenCount(ino):
    count = 0
    while(ino != 0):
        idigit = ino %10
        if(idigit>3 and idigit<7):
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