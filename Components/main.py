# ++++++++++++++++++++++++++++++++++++++++++++
# components
from options_m import *
from calendar_m import *
# from datetime import datetime
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
        # self.icon = 'mycalendar.png'

        # Main window
        root = BoxLayout(spacing = 3)

        # Calendar window
        row = 6
        col = 7
        GridL = GridLayout(rows = row, cols = col, spacing = 3)
        month = days_in_month()         # (list days in month)
        for i in range(row-1):
            for j in range(col):
                GridL.add_widget( 
                    Button  (
                    text = str(month[i][j])
                    #on_press = Cal.day_on_display() 
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

