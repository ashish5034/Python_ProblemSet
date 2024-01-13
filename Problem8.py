class Test:
    def __init__(self,n):
        self.no = n;
    def check(self):
        if(self.no<10):
            print("Hello")
        else:
            print("Demo")
            
def main():
    number=int(input("Enter number: "))
    tobj=Test(number)
    tobj.check()
if __name__ == "__main__":
    main()