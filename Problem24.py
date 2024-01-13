# // write a program which accept number from user and count 4
def countfour(ino):
    idigit = ino % 10
    count = 0
    while(ino != 0):
        idigit = ino % 10
        if(idigit == 4):
            count=count+1
        ino = ino // 10
    print(count)
def main():
    print("Enter Number: ")
    ivalue = int(input())
    countfour(ivalue)
if __name__ == "__main__":
    main()