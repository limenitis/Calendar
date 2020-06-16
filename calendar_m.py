# kivy libs
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

from options_m import rgb

from datetime import datetime
import configparser
import calendar

# Calendar window

def days_in_month (
    last_month = calendar.Calendar().monthdayscalendar(datetime.now().year, datetime.now().month),
    month      = calendar.Calendar().monthdayscalendar(datetime.now().year, datetime.now().month)  ):
    
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

    # change first week in current month
    c = 0 
    for i in month[0]:
        if i == 0:
            month[0][month[0].index(i)] = end_last_month[c]
            c += 1

    return month


class UCalendar(GridLayout):
    
    def init_days(self):
        
        config = configparser.ConfigParser()
        config.read("settings.ini")
        
        color = config['colors_calendar']

        month = days_in_month()     # (list days in month)

        row = 5
        col = 7

        # definition last day
        if month[0][0] != 1:
            highlight = bool(1)
            last_day = month[0][0]-1
        else:
            highlight = bool(0)
            last_day = 1

        for i in range(row):
            for j in range(col):
                # ++++ 'start' 
                # highlight last month and next month days
                if   (highlight == 1) & (last_day <= month[i][j]):
                    color_day = rgb(color['days_in_not_current_month'])
                elif (highlight == 1) & (last_day >= month[i][j]):
                    highlight = bool(0)
                    color_day = rgb(color['days_in_current_month'])

                elif (highlight == 0) & (last_day <= month[i][j]):
                    color_day = rgb(color['days_in_current_month'])
                elif (highlight == 0) & (last_day >= month[i][j]):
                    highlight = bool(1)
                    color_day = rgb(color['days_in_not_current_month'])
                last_day = month[i][j]
                # ++++ 'end'

                # highlight current day
                if month[i][j] == datetime.now().day:
                    color_day = rgb(color['current_day'])

                self.add_widget( Button(    text = str(month[i][j]),
                                            # on_press = 
                                            background_color = color_day,
                                            background_normal = '' ) )

Builder.load_file("design.kv")
