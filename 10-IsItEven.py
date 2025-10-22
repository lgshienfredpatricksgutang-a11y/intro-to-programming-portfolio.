
# this program checks if a number is even or odd

def check_even_odd(number):
    if number % 2 == 0: # if the number is divisible by 2 with no remainder
        return "Even"
    else:
        return "Odd"
    
    # main function to execute the program
def main():
    num = int(input("Enter an number: ")) # get user input
    result = check_even_odd(num) # call the function to check even or odd
    print(f"The number {num} is {result}.") # print the result

# start the program
if __name__ == "__main__":
    main()

