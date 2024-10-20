# This recursive function takes a character string s and outputs its reverse. 
# For example, the reverse of pots&pans would be snap&stop.

def reverseChain(s):
    ''' Receives a string, and returns the string reversed
    ''' 
    l=len(s)
    if (l == 0):
        return ""
    else:
        return s[l-1] + reverseChain(s[:l-1])
           
def main():
    chain0 = ""
    chain1 = "a"
    chain2 = "hello"
    chain3 = "pots&pans"
    print(reverseChain(chain2))
         
main()