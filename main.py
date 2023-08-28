
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        button = Button(text='Click Me!')
        return button

if __name__ == '__main__':
    MyApp().run()