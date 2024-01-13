class Test:
    def __init__(self, no1):
        self.no=no1;
    def display(self):
        count = 0
        for i in range(self.no):
            print("*")
            count = count +1
        print(f"{count} Number of time * repeated")
            
def main():
    number=int(input("Enter Number: "))
    tobj = Test(number);
    tobj.display()
if __name__ == "__main__":
    main()
    