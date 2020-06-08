# ++++++++++++++++++++++++++++++++++++++++++++
# components
import calendar
from datetime import datetime
from options_m import *
# from calendar_m import *
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

class CalendarApp(App):

    def build(self):

        #self.icon = 'myicon.png'

        # Main window
        root = BoxLayout(spacing = 3)

        row = 6
        col = 7
        months = calendar.Calendar().monthdayscalendar(datetime.now().year, datetime.now().month)
        GridL = GridLayout(rows = row, cols = col, spacing = 3)
        for i in range(row-1):
            for j in range(col):
                GridL.add_widget( 
                    Button  (
                    text = str(months[i][j])
                    #on_press = Cal.day_on_display() 
                            )   
                                )

        # Menu window
        Menu = BoxLayout(size_hint = (.2, 1), )
        Opt = Options()
        options = {
            1 : Opt.new_event(),
            2 : Opt.new_task(),
            3 : Opt.change_layoyt_calendar(),
            4 : Opt.change_layoyt_tasks()
        }
        name_options = {
            1 : 'Новое событие',
            2 : 'Новое дело',
            3 : 'Окно с календарем',
            4 : 'Окно с делами'
        }

        Menu_options = GridLayout(rows = 10, cols = 1, spacing = 3)
        for i in range(1, len(name_options)+1):
            Menu_options.add_widget( Button(text = name_options[i]) )
            # Menu_options.add_widget( Button(text = ' ', on_press = lambda x: Opt.test() ) )
        Menu.add_widget(Menu_options)


        root.add_widget(Menu)
        root.add_widget(GridL)
        return root


if __name__ == "__main__":
    CalendarApp().run()

