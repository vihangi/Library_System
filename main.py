"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


from kivy.app import App

# Create your main program in this file, using the ReadingListApp class


class ReadingListApp(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('app.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_reset(self):
        self.root.ids.output_label.text=""
        self.root.ids.input_name.text=""


ReadingListApp().run()

