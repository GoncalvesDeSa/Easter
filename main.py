from calc import DayCalculator
from easter import EasterCalculator

def main():

    while True:
        print("Choose one operation:")
        print("1. Know the day of the week of a date")
        print("2. Know the Easter date")
        print("3. Know the Easter date in a given year interval")
        print("4. Exit")

        option = input("Insert the option: ")

        if option == "1":
            print("Day of the week calculation")
        if option == "2":
            print ("Easter date calculation")
        if option == "3":
            print("Easter date year interval")
        if option == "4":
            print("Exit...")
            break

        # if option != "1" or option != "2" or option != "3" or option != "4":
        #     print("Invalid option. Please, choose a valid option.")
        #     continue



        if option == "1":
            try:
                day = int(input("insert day: "))
                month = int(input("insert month: "))
                year = int(input("insert year: "))
            except ValueError:
                print("Error: Invalid Entry, choose a valid option.")
                continue
            calc = DayCalculator(year, month, day)
            print("The weekday was:", calc.day_of_the_week())
        if option == "2":
            try:
                year = int(input("insert year: "))
            except ValueError:
                print("Error: Invalid Entry, choose a valid option.")
                continue
            calc = EasterCalculator(year)
            date = calc.easter_date()
            print(f"The Easter date in {year} was:", date)
            day = DayCalculator(*date)
            print("weekday:", day.day_of_the_week())
        if option == "3":
            try:
                year = int(input("insert year ro begin: "))
                year2 = int(input("insert year to end: "))
            except ValueError:
                print("Error: Invalid Entry, choose a valid option.")
                continue
            while year <= year2:
                calc = EasterCalculator(year)
                day = DayCalculator(*calc.easter_date())
                print("The Easter date was:" + str(calc.easter_date()) + ". It's a " + day.day_of_the_week())
                year += 1
        else:
            print("Invalid Option: Please select a valid option.")

if __name__ == "__main__":
    main()