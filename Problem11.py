class Test:
    def __init__(self,num):
        self.no = num
    def check(self):
        if(self.no%2==0):
            print(f"{self.no} is even: ",end=" ")
            # return self.no
        else:
            print(f"{self.no} is odd: ",end=" ")
            # return self.no
def main():
    number = int(input("Enter Number: "))
    tobj = Test(number)
    ret = tobj.check()
    
if __name__=="__main__":
    main()