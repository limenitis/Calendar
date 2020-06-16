# ++++++++++++++++++++++++++++++++++++++++++++
# components
from options_m import Options
from options_m import rgb
from calendar_m import UCalendar
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
# from kivy.uix.popup import Popup # всплывающее окно
# from kivy.uix.bubble import Bubble # context menu
# from kivy.uix.widget import Widget
from kivy.uix.button import Button
# from kivy.uix.spinner import Spinner # выпадающий список
# from kivy.uix.dropdown import DropDown # выпадающий список
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.screenmanager import ScreenManager # экраны/screens
# from kivy.uix.tabbedpanel import TabbedPanel # табы/вкладки  
# ++++++++++++++++++++++++++++++++++++++++++++

# remove_widget

class MyCalendarApp(App):

    def build(self):

        self.icon = 'cal.ico'

        config = configparser.ConfigParser()
        config.read("settings.ini")
        
        # Main window
        root = BoxLayout(spacing = 1)

        # Context menu
        # context_menu = Bubble()
        
        # Calendar window

        Calendar = UCalendar()
        Calendar.init_days()

        # Menu window
        Menu = BoxLayout( size_hint = (.2, 1) )
        Opt = Options()
        option = {
            0 : lambda x: Opt.new_event(),
            1 : lambda x: Opt.new_task(),
            2 : lambda x: Opt.change_layoyt_calendar(),
            3 : lambda x: Opt.change_layoyt_tasks()
        }
        name_interface = config['language']
        name_options = {
            0 : name_interface['new_event'],
            1 : name_interface['new_task'],
            2 : name_interface['change_layoyt_calendar'],
            3 : name_interface['change_layoyt_tasks']
        }

        color_interface = config['colors']
        Menu_options = GridLayout(cols = 1, spacing = 2)
        for i in range(len(name_options)):
            Menu_options.add_widget( Button(    text = name_options[i], 
                                                on_press = option[i], 
                                                background_color = rgb(color_interface['menu_options']),
                                                background_normal = '' ) )
        Menu.add_widget(Menu_options)

        

        root.add_widget(Menu)
        root.add_widget(Calendar)
        return root

Builder.load_file("design.kv")

if __name__ == "__main__":
    MyCalendarApp().run()

