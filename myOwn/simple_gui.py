import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label


class FirstApp(App):

    def build(self):
        return Label(text='Welcome to amazing')


if __name__ == '__main__':
    FirstApp().run()
