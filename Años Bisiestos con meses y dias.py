def days_in_month(year, month):
        if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            print(year, months[month] )
        else:
            months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            print(year, months[month] )
days_in_month(2019, 2)
