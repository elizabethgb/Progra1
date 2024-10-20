# This recursive function checks if a string s has more vowels than consonants

def moreVowThanCons(chain, i=0): #i is the counting of the vowels minus the counting of the consonants
    '''Receives chain, returns if it has more vowels than consonants
    '''
    if (len(chain)==0):
        return (i>0)    
#        if (i>0):
#            resp=True
#        else:
#            resp=False
#        return resp
    else:
        vowels=["a", "e", "i", "o", "u"]
        count=i
        if chain[0].lower() in vowels:
            count += 1
        elif chain[0].isalpha():
            count -= 1
        return moreVowThanCons(chain[1:], count)
   
def main():
    chain0=""
    chain="buildings"
    chain2="houses"
    print(moreVowThanCons(chain))
    
main()