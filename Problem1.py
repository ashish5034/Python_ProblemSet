# program to divition of two numbers
def division(ino1,ino2):
    # if(ino2<0):
    #     return -1
    Ans=0
    Ans = ino1/ino2
    return Ans

def main():
    ivalue1 = int(input("Enter ivalue1: "))
    ivalue2 = int(input("Enter ivalue2: "))
    
    ret = 0
    ret = division(ivalue1,ivalue2)
    print("Divison is : ",ret)
    
if __name__ =="__main__":
    main()