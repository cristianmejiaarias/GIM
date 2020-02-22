from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

class WorkoutBanner(GridLayout):
    rows= 1
    def __init__(self, **kwargs):
        super(WorkoutBanner, self).__init__()
        print(kwargs['workout_image'])
        print(kwargs['description'])
        #NEED LEFT FLOATLAYOUT

        left = FloatLayout()

        left_image = Image(source="icons/workouts/" + kwargs['workout_image'], size_hint=(1,0.8), pos_hint={"top": 1, "left": 1})
        left_label = Label(text=kwargs['description'], size_hint=(1,.2), pos_hint={"top": .2, "left": 1})
        left.add_widget(left_image)
        left.add_widget(left_label)

        #NEED MIDDLE FLOATLAYOUT
        middle_image = Image(source="icons/" + kwargs['type_image'], size_hint=(1, 0.8),
                          pos_hint={"top": 1, "left": 1})
        #middle_image = Label(text=kwargs['description'], size_hint=(1, .2), pos_hint={"top": .2, "left": 1})
        left.add_widget(middle_image)

        self.add_widget(left)


