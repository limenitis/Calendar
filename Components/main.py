# ++++++++++++++++++++++++++++++++++++++++++++
# components
from options_m import *
from calendar_m import *
import calendar
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
        BoxL = BoxLayout(spacing = 3)

        # Board window
        BoardL = BoxLayout(size_hint = (.2, 1), )
        
        # Calendar window
        Cal = Calendar()
        GridL = GridLayout(rows = 6, cols = 7, spacing = 3)
        count_days = Cal.count_days(Cal.current_month()) + 1
        for i in range(1, count_days):
            GridL.add_widget( 
                Button  (
                text = str(i),
                #on_press = Cal.day_on_display() 
                        )   
                            )

        # Menu window
        Opt = Options()
        Menu_options = GridLayout(rows = 10, cols = 1, spacing = 3)
        for opt in list_opt:
            Menu_options.add_widget( Button(text = ' ') )
            # Menu_options.add_widget( Button(text = ' ', on_press = lambda x: Opt.test() ) )


        BoardL.add_widget(Menu_options)
        BoxL.add_widget(BoardL)
        BoxL.add_widget(GridL)
        return BoxL


if __name__ == "__main__":
    CalendarApp().run()

