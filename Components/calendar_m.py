from datetime import datetime
import calendar

def days_in_month():
    last_month = calendar.Calendar().monthdayscalendar(datetime.now().year, datetime.now().month)
    month = calendar.Calendar().monthdayscalendar(datetime.now().year, datetime.now().month)    

    # change end current month
    c = 1
    for i in month[-1]:
        if i == 0:
            month[-1][month[-1].index(i)] = c
            c += 1

    # find end last month
    c = 0
    end_last_month = []
    for i in last_month[-1]:
        if i != 0:
            end_last_month.append(i)
            print(end_last_month)

    # change first week in current month
    c = 0 
    for i in month[0]:
        if i == 0:
            month[0][month[0].index(i)] = end_last_month[c]
            c += 1

    return month

