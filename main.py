# ++++++++++++++++++++++++++++++++++++++++++++
# config window
from kivy.config import Config
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')
# ++++++++++++++++++++++++++++++++++++++++++++
# kivy libs
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import Button
from kivy.lang import Builder
from kivymd.app import MDApp
# ++++++++++++++++++++++++++++++++++++++++++++
# python libs
import configparser
# ++++++++++++++++++++++++++++++++++++++++++++
# modules programm
from calendar_module import*
# ++++++++++++++++++++++++++++++++++++++++++++

class DB_API(object):
    """docstring for DB_API"""
    def __init__(self, arg):
        super(DB_API, self).__init__()
        
        self.arg = arg
        



class Options():

    def new_event(self):
        print('new_event work')
        
    def new_task(self):
        print('new_task work')
        
    def change_layout_calendar(self):
        print('change_layoyt_calendar work')

    def change_layout_tasks(self):
        print('change_layoyt_tasks work')

    def delete_task(self):
        print('delete_task work')

    def update_task(self):
        print('update_task work')


class Main_menu(BoxLayout):
    """docstring for Menu"""
    def __init__(self, **kwargs):
        super(Main_menu, self).__init__(**kwargs)

        Opt = Options()

        config = configparser.ConfigParser()
        config.read("settings.ini")
        name_interface = config['language']
        color_interface = config['colors']

        option = {
            0: lambda x: Opt.new_event(),
            1: lambda x: Opt.new_task(),
            2: lambda x: Opt.change_layout_calendar(),
            3: lambda x: Opt.change_layout_tasks()
        }
        name_options = {
            0: name_interface['new_event'],
            1: name_interface['new_task'],
            2: name_interface['change_layout_calendar'],
            3: name_interface['change_layout_tasks']
        }

        for i in range(len(name_options)):
            self.add_widget( Button(text = name_options[i],
                                    on_press = option[i],
                                    background_color = rgb(color_interface['menu_options']),
                                    background_normal = '' ) )


class Root(BoxLayout):
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
    
        Menu = Main_menu( orientation = 'vertical', size_hint = (.1, 1), spacing = 1 )
        Calendar = UCalendar( cols = 7, rows = 5, spacing = 1 )

        self.add_widget(Menu)
        self.add_widget(Calendar)


class MyCalendarApp(MDApp):

    def build(self):

        self.icon = 'cal.ico'

        config = configparser.ConfigParser()
        config.read("settings.ini")
        color_interface = config['colors']
        
        root = Root(padding = 10)

        return root

if __name__ == "__main__":
    MyCalendarApp().run()

