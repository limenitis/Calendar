# ++++++++++++++++++++++++++++++++++++++++++++
# components
from options_m import *
from calendar_m import *
from datetime import datetime
# ++++++++++++++++++++++++++++++++++++++++++++
# config window
from kivy.config import Config
Config.set('graphics', 'resizable', '1');
Config.set('graphics', 'width', '900');
Config.set('graphics', 'height', '400');
# ++++++++++++++++++++++++++++++++++++++++++++
# kivy libs
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup # всплывающее окно
from kivy.uix.bubble import Bubble # context menu
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner # выпадающий список
from kivy.uix.dropdown import DropDown # выпадающий список
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.screenmanager import ScreenManager # экраны/screens
# from kivy.uix.tabbedpanel import TabbedPanel # табы/вкладки  
# ++++++++++++++++++++++++++++++++++++++++++++

# remove_widget

class MyCalendarApp(App):

    def build(self):

        self.icon = 'cal.ico'

        # Main window
        root = BoxLayout(spacing = 3)

        # Context menu
        # context_menu = Bubble()
        
        # Calendar window
        row = 5
        col = 7
        GridL = GridLayout(rows = row, cols = col, spacing = 3)
        month = days_in_month()     # (list days in month)

        color_interface = {
        'days_in_last_month'    : (168/255,  99/255, 213/255, 1),
        'days_in_current_month' : (204/255, 127/255, 255/255, 1),
        'current_day'           : (255/255,   0/255, 179/255, 1)
        }

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
                    color_button = color_interface['days_in_last_month']
                elif (highlight == 1) & (last_day >= month[i][j]):
                    highlight = bool(0)
                    color_button = color_interface['days_in_current_month']

                elif (highlight == 0) & (last_day <= month[i][j]):
                    color_button = color_interface['days_in_current_month']
                elif (highlight == 0) & (last_day >= month[i][j]):
                    highlight = bool(1)
                    color_button = color_interface['days_in_last_month']
                last_day = month[i][j]
                # ++++ 'end'

                # highlight current day
                if month[i][j] == datetime.now().day:
                    color_button = color_interface['current_day']

                GridL.add_widget( 
                    Button  (
                    background_color = color_button,
                    background_normal = '',
                    text = str(month[i][j])
                    # on_press = 
                            )   
                                )
                

        # Menu window
        Menu = BoxLayout(size_hint = (.2, 1), )
        Opt = Options()
        option = {
            1 : lambda x: Opt.new_event(),
            2 : lambda x: Opt.new_task(),
            3 : lambda x: Opt.change_layoyt_calendar(),
            4 : lambda x: Opt.change_layoyt_tasks()
        }
        name_options = {
            1 : 'Новое событие',
            2 : 'Новое дело',
            3 : 'Окно с календарем',
            4 : 'Окно с делами'
        }

        Menu_options = GridLayout(cols = 1, spacing = 3)
        for i in range(1, len(name_options)+1):
            Menu_options.add_widget( Button(text = name_options[i], on_press = option[i]) )
        Menu.add_widget(Menu_options)


        root.add_widget(Menu)
        root.add_widget(GridL)
        return root


if __name__ == "__main__":
    MyCalendarApp().run()

