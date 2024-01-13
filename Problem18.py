class Test:
    def __init__(self,no):
        self.ino = no
    def factors(self):
        mult = 1
        for i in range(1,self.ino):
            if(self.ino%i==0):
                print(i)

def main():
    ival = int(input("Enter Number: "))
    tobj = Test(ival)
    tobj.factors()
if __name__ == "__main__":
    main()