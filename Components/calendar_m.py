from datetime import datetime

class Calendar():
    year_on_display = datetime.now().year

    month_on_display = datetime.now().month

    day_on_display = datetime.now().day

    highlight_day = datetime.now().day

    def current_year(self):
        return datetime.now().year
    
    def current_month(self):
        return datetime.now().month
    
    def current_day(self):
        return datetime.now().day
    
    # every 400 -> 29 days feb
    # every 100 -> not 29 days feb

    def count_days(self, month = datetime.now().month, year = datetime.now().year)
        if (month < 8)&(month != 2):
            days = 30 + (month % 2) # 365//12 = 30
        elif month > 7:
            days = 30 + int( not(month % 2) )
        else: #feb
            if (year % 400 == 0):
                days = 29
            elif (year % 4 == 0)&(year % 100 != 0):
                days = 29
            else:
                days = 28

        return days
