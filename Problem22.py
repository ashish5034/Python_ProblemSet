# // write a program which accept number from user and check whether it contain 0 in it or not
def countZero(ino):
    idigit = ino % 10
    count = 0
    while(ino != 0):
        idigit = ino % 10
        if(idigit == 0):
            count=count+1
        ino = ino // 10
    print(count)
def main():
    print("Enter Number: ")
    ivalue = int(input())
    countZero(ivalue)
if __name__ == "__main__":
    main()