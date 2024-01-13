class Test:
    def check(num):
        if (num%5 == 0):
            return True
        else:
            return False
        
def main():
    number =int(input("Enter number: "))
    tobj = Test
    ret = tobj.check(number)
    if(ret==True):
        print("Number is divisible by five")
    else:
        print("Number is not divisible by five ")
        
if __name__ == "__main__":
    main();