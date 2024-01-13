# write a program which accept number from user and return the diff between even digit and odd digit
def countdiff(ino):
    isum1 = 0
    isum2 = 0
    if(ino < 0):
        ino = -ino
    while(ino != 0):
        idigit = ino %10
        if(idigit % 2 == 0):
            isum1 = isum1 + idigit
        else:
            isum2 = isum2 + idigit
        ino = ino // 10
    return isum1 - isum2
def main():
    print("Enter number: ")
    ival = int(input())
    iret = countdiff(ival)
    print(iret)
if __name__ == "__main__":
    main()