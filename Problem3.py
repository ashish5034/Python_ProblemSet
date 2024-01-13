# program to print n to 1 numbers on screen 
class Test:
    def display(num):
        for i in range(num,0,-1):
            print(i)
            


def main():
    no = int(input("Enter number of iteration: "))
    tobj = Test
    tobj.display(no)
if __name__ == "__main__":
    main();