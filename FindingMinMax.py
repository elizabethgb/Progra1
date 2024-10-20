# This recursive function finds the minimum and maximum
# values in a sequence without using any loops.

def findingMinMax(values):
    ''' Receives a list of integers, returns the min and max values as a tuple
    '''
    l=len(values)
    if (l==0):
        raise ValueError("Empty list")
    elif (l==1):
        return(values[0],values[0])
    else:
        (min,max)=findingMinMax(values[1:])
        if (values[0]<min):
            min=values[0]
        if (values[0]>max):        
            max=values[0]
    return (min,max)

def main():
    values = [4,3,5,7,2]
    values1 = [1]
    values0 = []
    try:
        print(findingMinMax(values))
    except ValueError as mensaje:
       print(mensaje)
       
main()