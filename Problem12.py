class Test:
    def __init__(self, no):
        self.num = no

    def factors(self):
        if self.num <= 0:
            self.num = -self.num
        for i in range(1, self.num // 2+1, 1):
            if self.num % i == 0:
                print(i)
        # print(self.num)  # Include the number itself as a factor

def main():
    number = int(input("Enter a number: "))
    tobj = Test(number)
    tobj.factors()

if __name__ == "__main__":
    main()
