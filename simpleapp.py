import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childapp(GridLayout):
    def _init_(self,**kwargs):
        super(childapp, self)._init_()
        self.cols = 2
        self.add_widget(Label(text = 'Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Student Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text='Student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = "Click Me")
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Name of Student is " + self.s_name.text )
        print("Marks of Student is " + self.s_marks.text)
        print("Gender of Student is " + self.s_gender.text)
        print("")


class parentapp(App):
    def build(self):
        return childapp()

if _name_ == "_main_":
    parentapp().run()
