class Test:
    def __init__(self,iNo):
       self.no = iNo
    def EvenFactors(self):
        for i in range (1,self.no//2+1,1):
            if(self.no%i==0):
                if(i%2==0):
                    print(i)

def main():
    num = int(input())
    tobj = Test(num)
    tobj.EvenFactors()
if __name__ == "__main__":
    main()