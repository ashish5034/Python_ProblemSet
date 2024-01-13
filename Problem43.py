# Accept n number from user and accept one another number as no. , return index of its last occurence of that number 
def last_occurrence_index(numbers, target):
    try:
        index = len(numbers) - 1 - numbers[::-1].index(target)
        return index
    except ValueError:
        return -1  # Return -1 if the target number is not found in the list

def main():
    try:
        n = int(input("Enter the number of elements in the list: "))
        numbers = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
        
        target_number = int(input("Enter the number to find its last occurrence index: "))

        result = last_occurrence_index(numbers, target_number)

        if result != -1:
            print(f"The last occurrence of {target_number} is at index {result}.")
        else:
            print(f"{target_number} is not present in the list.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()