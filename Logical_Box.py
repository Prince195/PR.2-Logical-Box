print("*** welocmeto the Pattern Genrator and Number Analyzer! ***")

while True:
    print("Select an opetion:")
    print("1.Generate a pattern:")
    print("2.Analyzer a Range of Numbers:")
    print("3.exit:")

    choice=input("Enter Your choice:")
    if choice=="1":
        rows=int(input("Enter a Number of Rows For the Pattern:"))
        if rows<=0:
            print("Invalid row count!")
            break
        print("\nPattern:")
        for i in range(1 ,rows + 1):
            print("*" * i)
        print()

    elif choice=="2":
        start=int(input("Enter the start of the range:"))
        end=int(input("Enter the end of the range:"))
        print()
        total = 0

        for num in range(start,end + 1):
            if num % 2 == 0:
                print("number is even")
            else:
                print("number is odd")
            total+=num
        print("\nsum of all numbers from start to end is",total)
        
    elif choice=="3":
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")

