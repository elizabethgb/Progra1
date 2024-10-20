# It removes requested elements from an initialized set with the numbers [0, 9]

def main():
    set={num for num in range(10)}
    print("Initial set: ", set)
    while True:
        try:
            elem=int(input("Please enter a value to remove (-1 to finish): "))
        except ValueError:
            print("A not integer number was entered")
        else:
            if (elem==-1):
                break
            try:
                set.remove(elem)
                print("Updated set: ", set)
            except KeyError:
                print("The number entered doesn't belong to the set")

main()