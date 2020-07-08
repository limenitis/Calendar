import configparser
from calendar import weekday
from datetime import datetime
from kivymd.uix.button import Button
from kivymd.uix.gridlayout import GridLayout


def convert_str_to_int(string):
    r = ''
    g = ''
    b = ''
    invis = ''

    switch = 0

    for symbol in string:
        if (symbol != ','):
            if symbol == ' ':
                continue

            elif switch == 0:
                r = r + symbol

            elif switch == 1:
                g = g + symbol

            elif switch == 2:
                b = b + symbol

            elif switch == 3:
                invis = invis + symbol
        
        elif(symbol == ','):
            switch += 1

    r = int(r)
    g = int(g)
    b = int(b)
    
    if invis != '':
        invis = float(invis)
    else:
        invis = 1

    return r, g, b, invis


def rgb(r = None, g = None, b = None, invis = 1):

    if (type(r) == str):
       r, g, b, invis = convert_str_to_int(r)

    return (r/255,g/255,b/255,invis)


def div_to(in_list, n = 7):
    out_list = []
    for i in range(0, len(in_list), 7):
        new_list = []
        for j in range(n):
            new_list.append( in_list[i+j] )
        out_list.append(new_list)
    return out_list


def isleap(year = datetime.now().year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year = datetime.now().year, month = datetime.now().month):

    config = configparser.ConfigParser()
    config.read("settings.ini")

    color = config['colors_calendar']

    maxdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isleap(year) == True:
        maxdays[2] = 29

    days = []
    colors = []
    # for end last month
    for j in range(weekday(year, month, 1), 0, -1): 
        days.append(maxdays[month] - j)
        colors.append( rgb(color['days_in_last_month']) ) 

    # for current month
    for j in range(1, maxdays[month]+1):
        days.append(j)
        if j == datetime.now().day:
            colors.append( rgb(color['current_day']) )
        else:
            colors.append( rgb(color['days_in_current_month']) )

    # for next month
    # for j in range(maxdays[month], maxdays[month] - 1 + 6):
    for j in range(maxdays[month], maxdays[month] - weekday(year, month, maxdays[month]) + 6 ):
        days.append(j + 1 - maxdays[month])
        colors.append( rgb(color['days_in_next_month']) )

    days  = div_to(days)
    colors = div_to(colors)

    return days, colors


class UCalendar(GridLayout):

    def __init__(self, **kwargs):
        super(UCalendar, self).__init__(**kwargs)

        config = configparser.ConfigParser()
        config.read("settings.ini")
        
        wdays = config['weekdays']

        month, color = days_in_month()     # (list days in month)

        col = 7
        row = 5

        for i in range(row):
            for j in range(col):

                self.add_widget( Button(    text = str(month[i][j]),
                                            # on_press = 
                                            background_color = color[i][j],
                                            background_normal = '' ) )

        # years = []
        # for i in range(datetime.now().year-25, datetime.now().year+25):
        #     years.append(i)
        # return years


