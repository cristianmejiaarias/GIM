from kivy.app import App
from kivy.factory import FactoryException
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from workoutbanner import WorkoutBanner

import requests
import json




class HomeScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass
class ImageButton(ButtonBehavior, Image):
    pass

GUI =Builder.load_file("main.kv")
class MainApp(App):
    my_friend_id = 1
    def buil(self):
        return GUI
    def on_start(self):
        #GET DATABASE DATA
        result = requests.get("https://friendly-fitness-bd93c.firebaseio.com/"+ str(self.my_friend_id)+ ".json")
        data = json.loads(result.content.decode())
        #GET AND UPDATE AVATAR IMAGE
        ########################## ID DE LA PANTALA Y ID DEL OBJETO QUE ESTA EN LA PANTALLA ######
        avatar_image = self.root.ids['home_screen'].ids['avatar_image']
        avatar_image.source = "icons/avatars/"+ data['avatar']
        #GET AN UPDATE STREAK LABEL
        streak_label = self.root.ids['home_screen'].ids['streak_label']
        streak_label.text = str(data['streak'])+ ' Day streak'

        banner_grid = self.root.ids['home_screen'].ids['banner_grid']
        workouts = data['workouts'][1:]
        for workout in workouts:
            # POPULTE WORKOUT GRID IN HOME SCREEN
            #print(workout['workout_image'])
            #print(workout['type_image'])
            v = WorkoutBanner(workout_image=workout['workout_image'], description=workout['description'],
                              type_image=workout['type_image'])
            banner_grid.add_widget(v)





    def change_screen(self, screen_name):
        screen_manager =self.ids['screen_manager']
        screen_manager.transition
        screen_manager.current = screen_name

MainApp().run()

