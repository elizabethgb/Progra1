# This function receives three natural numbers (day, month, year) 
# and checks if they represent a gregorian valid date

def isLeap(year):
    '''Checks if it's a leap year
    '''
    resp = False
    if (year % 100 == 0) and (year % 400 == 0):
        resp = True
    elif (year % 4 == 0):
        resp = True
    return resp

isLeap2 = lambda year : (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
'Also checks if it is a leap year'

def isValidDate(day, month, year):
    '''Checks if it's a valid date
    '''
    resp = True
    if (day < 1) or (month < 1) or (year < 1):
        resp = False
    if (month > 12) :
        resp = False    
    if (day > 31):
        resp = False
    if (month == 4) or (month == 6) or (month == 9) or (month == 11):
        if (day > 30):
            resp = False
    if (month == 2):
        if isLeap(year):
            if (day > 29):
                resp = False
        else:
            if (day > 28):
                resp = False
    return resp

def enterPositiveNumber(text):
    num = int(input(text))
    while num < 1:
        print("Number not valid. Try again.")
        num = int(input(text))   
    return num

def main():
    day = enterPositiveNumber("Please enter the day: ")
    month = enterPositiveNumber("Please enter the month: ")
    year = enterPositiveNumber("Please enter the year: ")
    
    if isValidDate(day, month, year):
        print("Date is correct")
    else:
        print("Date isn't correct")

main()