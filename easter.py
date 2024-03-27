class EasterCalculator:

    def __init__(self, year):
        self.year = year

    
    #determnation of the date of Easter using Meeus/Jones/Butcher algorithm
    #https://en.wikipedia.org/wiki/Date_of_Easter#Meeus.2FJones.2FButcher_Gregorian_algorithm
    
    def easter_date(self):
        a = self.year % 19
        b = self.year // 100
        c = self.year % 100
        d = b // 4
        e = b % 4
        #f = (b + 8) // 25
        g = (8 * b + 13) // 25
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a+ 11 * h + 19 * l) // 433
        #m = (a + 11 * h + 22 * L) // 451
        month = (h + l - 7 * m + 90) // 25
        day = ((h + l - 7 * m + 33 * month +19) % 32)
        return self.year, month, day
    