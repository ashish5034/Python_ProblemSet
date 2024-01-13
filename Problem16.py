class Test:
    def __init__(self,no):
        self.ino = no
    def multfactors(self):
        mult = 1
        for i in range(1,self.ino//2+1):
            if(self.ino%i==0):
                mult = mult*i
        return mult

def main():
    ival = int(input("Enter Number: "))
    tobj = Test(ival)
    print(tobj.multfactors())
if __name__ == "__main__":
    main()