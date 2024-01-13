class Test:
    def __init__(self, no1):
        self.no=no1
        
    def display(self):
        i=1
        while(i<=self.no):
            print("*\t")
            i=i+1
            
def main():
    number =int(input("Enter Number: "))
    tobj = Test(number)
    tobj.display();
if __name__ == "__main__":
    main()