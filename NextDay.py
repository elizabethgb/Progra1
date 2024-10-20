# This function receives three natural numbers (day, month, year) 
# and calculates the next day, returning three natural numbers (day, month, year). 

import ValidDate

def nextDay(day, month, year):
    'Calculates the next day of the received date'
    if (ValidDate.isValidDate(day + 1, month, year)):
        day = day + 1
    elif (ValidDate.isValidDate(1, month + 1, year)):
        day = 1
        month = month + 1
    else:
        day = 1
        month = 1
        year = year + 1    
    return day, month, year

def main():
    #Adding days to a date
    print("Please enter the date")
    day = ValidDate.enterPositiveNumber("Please enter the day: ")
    month = ValidDate.enterPositiveNumber("Please enter the month: ")
    year = ValidDate.enterPositiveNumber("Please enter the year: ")
    if (ValidDate.isValidDate(day, month, year)):
        days = ValidDate.enterPositiveNumber("Please enter the days to add: ")
        for i in range(days):
            day, month, year = nextDay(day, month, year)
        print("The new date is: ", end=" ")
        print(day, month, year, sep="/")
    else:
        print("Date isn't correct")

main()