from random import randint

def listGenerated():
    'Generates a list with 5 numbers between 1 and 100'
    lst=[]
    for i in range(5):
        lst.append(randint(1,100))
    return lst

# This function normalizes a received list, to 1.0 
# Example: [1, 1, 2] -> [0.25, 0.25, 0.50]
def normalizedlist(lst):
    add = sum(lst)
    for i in range(len(lst)):
        lst[i] = lst[i]/add

def main():
    lst = listGenerated()
    print("List: ", lst)
    normalizedlist(lst)
    print("Normalized list: ", lst)

main()