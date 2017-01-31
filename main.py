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
from book import Book
# Create your main program in this file, using the ReadingListApp class






class ReadingListApp(App):
    status_text = StringProperty()

    def build(self):
        self.title = "Reading List 2.0"
        self.root = Builder.load_file('app.kv')
        self.book = BookList()
        self.books_required = self.book.required_books
        self.books_completed = self.book.completed_books
        self.handle_required()
        return self.root

    def handle_required(self):
        self.book=BookList()
        self.books_required = self.book.required_books
        self.books_completed = self.book.completed_books
        self.root.ids.status_text.text = "Click Books to mark them as completed"
        self.pages = self.book.pages_required_books()
        self.root.ids.pages.text = "Total pages to read: {} ".format(str(self.pages))
        self.root.ids.entries.clear_widgets()
        self.book=BookList()


        for i in range(len(self.books_required)):

            temp_button = Button(text=self.books_required[i][0])

            self.total=Book(self.books_required[i])
            self.total_pages = self.total.book_length(self.books_required[i])

            temp_button.bind(on_release=self.press_entry)
            if self.total_pages == True:
                temp_button.background_color =(0.4,0.1,0.7,0.9)

            else:

                temp_button.background_color =(0.6,0.9,0.7,0.9)


            self.root.ids.entries.add_widget(temp_button)



    def handle_completed(self):
        self.book=BookList()
        self.books_required = self.book.required_books
        self.books_completed = self.book.completed_books
        self.root.ids.status_text.text = "Click on a book to get information"
        self.pages = self.book.total_completed_books()
        self.root.ids.pages.text = "Total pages completed: {} ".format(str(self.pages))

        self.root.ids.entries.clear_widgets()
        for i in range(len(self.books_completed)):
            temp_button = Button(text=self.books_completed[i][0])
            temp_button.background_color = (0.4, 0.13, 0.9, 0.8)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries.add_widget(temp_button)


    def press_entry(self, instance):
        # update status text

        self.name_book = instance.text
        self.bo=BookList()

        self.g = self.bo.search_by_title(self.name_book)
        print(self.g)
        if self.g[3]=="c":
            self.bo = self.bo.display(self.name_book)
            self.root.ids.status_text.text = "{} (completed)".format(str(self.bo))

        if self.g[3]=="r":
            print("hello")
            self.h = self.bo.mark_book(self.g)
            self.bo.save_Books()
            self.handle_completed()





    def book_to_be_added(self,title,author,pages):
        self.title = title.text

        self.author = author.text
        self.pages = pages.text

        if self.title == "" :
            self.root.ids.status_text.text = "All fields must be completed"


        elif self.author == "":
            self.root.ids.status_text.text = "All fields must be completed"

        elif self.pages.isdigit()== False:

            self.root.ids.status_text.text = "Please enter a valid number"

        else:
            self.page =str(pages.text)
            self.list=self.book.add_book(self.title,self.author,self.page)
            self.save=self.book.save_Books()
            self.handle_required()
            self.clear_all()


    def clear_all(self):
        """
        Clear all of the widgets that are children of the "entriesBox" layout widget
        :return:
        """
        self.root.ids.input_title.text = ""
        self.root.ids.input_author.text = ""
        self.root.ids.input_pages.text = ""



ReadingListApp().run()

