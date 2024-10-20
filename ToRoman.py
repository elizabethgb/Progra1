def toRoman(num):
    '''
    Converts any number between 1 and 3999 to roman
    '''
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    ch = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    i = 0
    while (num > 0):
        count = num // values[i]
        roman += ch[i] * count
        num -= values[i] * count
        i += 1   
    return roman

def toRoman2(num):
    m = num // 1000
    num = num - (m * 1000)
    c = num // 100
    num = num - (c * 100)
    d = num // 10
    num = num - (d * 10)
    u = num
    roman = ""
    roman += "M"*m
    if (c == 9):
        roman += "CM"
    elif (c > 4):
        roman += "D"+"C"*(c-5)
    elif (c == 4):
        roman += "CD"
    else:
        roman += "C"*c
        
    if (d == 9):
        roman += "XC"
    elif (d > 4):
        roman += "L"+"X"*(d-5)
    elif (d == 4):
        roman += "XL"
    else:
        roman += "X"*d
        
    if (u == 9):
        roman += "IX"
    elif (u > 4):
        roman += "V"+"I"*(u-5)
    elif (u == 4):
        roman += "IV"
    else:
        roman += "I"*u
        
    return(roman)

def main():
    num = int(input("Please enter a number between 1 and 3999: "))
    if (num < 1 or num > 3999):
        print("Incorrect number")
    else:
        print("Roman number: ", toRoman(num))
    
main()