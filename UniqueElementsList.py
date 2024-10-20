# This function receives a list and returns a new list 
# with the unique elements of the original list, order is not important 

def printList(list):
    for i in list:
        print(i, end= " ")

def uniqueElements(originalList):
    uniqueList = []
    for i in originalList:
        if i not in uniqueList:
            uniqueList.append(i)               
    return uniqueList

def inputList():
    print("Please enter the list (enter -1 to finish): ")
    list = []
    num = 0
    while num != -1:
        num = int(input())
        list.append(num)
    return list

def main():
    originalList = inputList()
    uniqueList = uniqueElements(originalList)
    printList(uniqueList)
    
main()