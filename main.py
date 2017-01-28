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
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from booklist import BookList
# Create your main program in this file, using the ReadingListApp class






class ReadingListApp(App):
    status_text = StringProperty()

    def __init__(self):


        self.list_book = BookList()

    def handle_reset(self):
        self.root.ids.output_label.text=""
        self.root.ids.input_name.text=""


ReadingListApp().run()

