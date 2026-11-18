list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(list)

def check_number(): 
    x = input ("Enter a number to check if it is in the list: ")
    if int(x) in list:
        print(f"{x} is in the list.")
    else:
        print(f"{x} is not in the list.")


def filter_even():
    filtered = [x for x in list if x % 2 == 0]
    print(filtered)

def filter_odd():
    filtered_odd = [x for x in list if x % 2 != 0]
    print(filtered_odd)


def filter_divisible_by_5():
    filtered_5 = [x for x in list if x % 5 == 0]
    print(filtered_5)


def filter_divisible_by_3():
    filtered_3 = [x for x in list if x % 3 == 0]
    print(filtered_3)

def filter_divisible_by_10():
    filtered_10 = [ x for x in list if x % 10 == 0]
    print(filtered_10)  

    
print("1. Check if a number is in the list")
print("2. Filter even numbers")
print("3. Filter odd numbers")
print("4. Filter numbers divisible by 5")
print("5. Filter numbers divisible by 3")
print("6. Filter numbers divisible by 10")
print("7. Count the amount of numbers in the list")
choice = input("pick a function: ")

if choice == "1":
    check_number()
elif choice == "2":
        filter_even()
elif choice == "3":
        filter_odd()
elif choice == "4":
        filter_divisible_by_5()
elif choice == "5":
        filter_divisible_by_3()
elif choice == "6":
        filter_divisible_by_10()
elif choice == "7":
        amount = len(list)
        print(f"The amount of numbers in the list is: {amount}")