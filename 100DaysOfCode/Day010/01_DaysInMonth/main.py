def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = None
    if month == 2: # February
        if is_leap_year(year):
            days = month_days[month-1] + 1
        else:
            days = month_days[month-1]
    else:
        days = month_days[month-1]
    return days


if __name__ == "__main__":
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)











