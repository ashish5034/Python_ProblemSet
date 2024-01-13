class Test:
    def __init__(self, char):
        self.cval = char

    def DisplayConversion(self):
        if 'a' <= self.cval <= 'z':
            
            self.cval = chr(ord(self.cval) - 32)
            print(self.cval)
        elif 'A' <= self.cval <= 'Z':
            self.cval = chr(ord(self.cval) + 32)
            print(self.cval)

def main():
    name = input("Enter a character: ")
    if len(name) == 1:  # Ensuring the input is a single character
        tobj = Test(name)
        tobj.DisplayConversion()
    else:
        print("Please enter a single character.")

if __name__ == "__main__":
    main()
