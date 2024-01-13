class Test:
    def __init__(self,n):
        self.no = n
        
    def check(self):
        if(self.no%2==0):
            return True
        else:
            return False

def main():
    num = int(input("Enter Number: "))
    tobj = Test(num)
    ret = tobj.check()
    if(ret == True):
        print("Even Number")
    else:
        print("Odd Number")       
if __name__=="__main__":
    main()    