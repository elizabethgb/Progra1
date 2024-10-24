import random

def randomList():
    'This function generates a list with random methods between 0 and 100'
    'the quantity of elements would be also a random even number between 10 and 50'
    lst = []
    count = random.randint(5,25) * 2
    for i in range(count):
        num = random.randint(0,100)
        lst.append(num)
    return lst


def main():
    lst = randomList()
    # Splitting the list in two halves
    lst1 = lst[0:len(lst)//2]
    lst2 = lst[len(lst)//2:len(lst)]
    print(lst)
    print()
    print(lst1, lst2, sep="")

main()