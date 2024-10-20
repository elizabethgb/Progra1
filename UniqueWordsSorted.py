# This function receives a phrase and removes the repeted words, 
# leaving just one of them, and sorts them by length 

def operatesChain(chain):
    chainList=chain.lower().split() #chainList list
    listSet=set(chainList) #listSet set
    setList=list(listSet) #setjList list
    setList.sort(key=len)
    resp = " ".join(setList)
    return resp

def main():
    phrase=input("Please enter a phrase: ")
    print("Response: ", operatesChain(phrase))

main()