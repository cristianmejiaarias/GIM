from kivy.app import App
from kivy.factory import FactoryException
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen




class HomeScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass


GUI =Builder.load_file("main.kv")
class MainApp(App):

    def buil(self):
        return GUI

    def change_screen(self, screen_name):
        screen_manager =self.ids['screen_manager']
        screen_manager.current = screen_name

MainApp().run()

