class Test:
    def __init__(self, no):
        self.ino = no

    def sumfactors(self):
        total_sum = 0
        sum1 = 0
        for i in range(1, self.ino):
            if self.ino % i != 0:
                sum1 = sum1 + i
            else:
                total_sum = total_sum + i
        return total_sum - sum1

def main():
    ival = int(input("Enter Number: "))
    tobj = Test(ival)
    print(tobj.sumfactors())

if __name__ == "__main__":
    main()
