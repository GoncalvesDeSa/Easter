from calc import DayCalculator

def main():

    while True:
        print("Choose one operation:")
        print("1. Know the day of the week of a date")
        print("2. Exit")

        option = input("Insert the option: ")

        if option == "1":
            print("Day of the week calculation")
        if option == "2":
            print("Exit...")
            break
        if option != "1" and option != "2":
            print("Invalid option. Please, choose a valid option.")
            continue

        try:
            day = int(input("insert day: "))
            month = int(input("insert month: "))
            year = int(input("insert year: "))
        except ValueError:
            print("Error: Invalid Entry, choose a valid option.")
            continue

        if option == "1":
            calc = DayCalculator(year, month, day)
            print("The weekday was:", calc.day_of_the_week())
        else:
            print("Invalid Option: Please select a valid option.")

if __name__ == "__main__":
    main()