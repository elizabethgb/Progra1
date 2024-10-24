# The function removes from a list the elements of another list
def removeRepeated(lst1, lst2):
    'Removes from lst1, the numbers in lst2'   
    for i in lst2:
        while i in lst1:
            lst1.remove(i)

def main():
    lst1=[2,7,3,4,6,7,1,0,8]
    lst2=[2,7,9]
    print("List 1: ", lst1)
    print("List 2 (numbers to remove from List 1): ", lst2)
    removeRepeated(lst1, lst2)
    print("New List 1: ", lst1)

main()