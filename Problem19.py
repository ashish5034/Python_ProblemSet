class Test:
    def __init__(self,no):
        self.ino = no
    def sumnoffactors(self):
        sum = 0
        for i in range(1,self.ino//2+1):
            if(self.ino%i!=0):
                sum = sum+i
        return sum

def main():
    ival = int(input("Enter Number: "))
    tobj = Test(ival)
    print(tobj.sumnoffactors())
if __name__ == "__main__":
    main()