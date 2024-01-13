class Test:
    def __init__ (self,no1,no2):
        self.num = no2;
        self.no = no1;
    def display(self):     
        for i in range (self.num):
            print(self.no)
            
def main():
    number1=int(input("Enter no1:"))
    number2=int(input("Enter no2:"))
    
    tobj = Test(number1,number2)
    tobj.display()
    
if __name__ == "__main__":
    main()