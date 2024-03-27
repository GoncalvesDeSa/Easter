class DayCalculator:


    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    

    #Detemination of the day of the week using Gauss algorithm
    def day_of_the_week(self):
        #d is the day of the month
        d = self.day
        #M is the month
        M = self.month
        #m is the shifted month
        m = M - 2 if  M > 2 else M + 10
        #Y is the year minus 1 for january and february ,and the year for the other months
        Y = self.year
        Y = Y - 1 if M < 3 else Y
        #y is the last two digits of the year
        y = Y % 100
        #c is the first two digits of the year
        c = Y // 100
        #W is the day of the week
        W = (d + (int)(2.6*m - 0.2) + y + (y//4) + (c//4) - 2*c)%7
        #if W is negative, we add 7 to it
        x = (W + 7) % 7

        #return the day of the week
        match x:
            case 0:
                return "Sunday"
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case _:
                return "Invalid day"


        
