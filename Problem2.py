class Problem2:
    
    def loop(num):
        count=0
        for i in range (num):
            print("Jay Ganesh...")
            count=count+1
        print("Number of iterations are: ",count)

def main():
    
    no = int(input("How many times do you want to print string : "))
    obj1 = Problem2
    obj1.loop(no)
    
if __name__ == "__main__":
    main()