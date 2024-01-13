class Test:
    def __init__(self, no):
        self.no1 = no
    def reverse(self,ino):
        idigit = 0
        while ino != 0:
            idigit = ino % 10
            print(idigit,end="")
            ino = ino // 10  # Use // for floor division

def main():
    print("Enter value: ")
    ivalue = int(input())
    tobj = Test(ivalue)
    tobj.reverse(ivalue)

if __name__ == "__main__":
    main()
