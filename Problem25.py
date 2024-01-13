# // write a program which accept number from user and count of less than 6
def lessthanSix(ino):
    idigit = ino % 10
    count = 0
    while(ino != 0):
        idigit = ino % 10
        if(idigit < 6):
            count=count+1
        ino = ino // 10
    print(count)
def main():
    print("Enter Number: ")
    ivalue = int(input())
    lessthanSix(ivalue)
if __name__ == "__main__":
    main()