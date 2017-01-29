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

    def build(self):
        self.title = "Reading List 2.0"
        self.root = Builder.load_file('app.kv')
        return self.root

    def handle_required(self):
        self.book=BookList()
        self.root.ids.status_text.text = "Click Books to mark them as completed"
        self.pages = self.book.pages_required_books()
        self.root.ids.pages.text = "Total pages to read: {} ".format(str(self.pages))
        self.books_required = self.book.required_books
        self.root.ids.entries.clear_widgets()
        for i in range(len(self.books_required)):

            temp_button = Button(text=self.books_required[i][0])
            #temp_button.bind(on_release=self.book.mark_completed(self.books_required[i][0]))
            self.root.ids.entries.add_widget(temp_button)


    def handle_completed(self):
        self.book = BookList()
        self.root.ids.status_text.text = "Click on a book to get information"
        self.pages = self.book.total_completed_books()
        self.root.ids.pages.text = "Total pages completed: {} ".format(str(self.pages))
        self.books_required = self.book.completed_books
        self.root.ids.entries.clear_widgets()
        for i in range(len(self.books_required)):
            temp_button = Button(text=self.books_required[i][0])
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries.add_widget(temp_button)


    def press_entry(self, instance):
        # update status text
        self.name_book = instance.text
        print(self.name_book)

        self.book=BookList()
        self.book=self.book.display(self.name_book)
        self.root.ids.status_text.text = str(self.book)

    def mark(self,name):
        self.mark_book=name
        print(self.mark_book)
        self.book=BookList()
        self.book=self.book.mark_completed(self.mark_book)

    def add_book(self,title,author,pages):
        self.title = title
        self.author=author
        self.pages=pages
        
        # change the number of columns based on the number of entries (no more than 5 rows of entries)
        self.root.ids.entries.cols = len(self.phonebook)
        # add button for new entry (same as in create_entry_buttons())
        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)

    def clear_all(self):
        """
        Clear all of the widgets that are children of the "entriesBox" layout widget
        :return:
        """
        self.root.ids.input_title.text = ""
        self.root.ids.input_author.text = ""
        self.root.ids.input_pages.text = ""

ReadingListApp().run()

