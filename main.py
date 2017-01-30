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

        self.root.ids.status_text.text = "Click Books to mark them as completed"
        self.pages = self.book.pages_required_books()
        self.root.ids.pages.text = "Total pages to read: {} ".format(str(self.pages))
        self.root.ids.entries.clear_widgets()


        for i in range(len(self.books_required)):

            temp_button = Button(text=self.books_required[i][0])
            #temp_button.bind(on_release=self.mark(self.books_required[i][0]))
            self.total=Book(self.books_required[i])
            self.total_pages = self.total.book_length(self.books_required[i])


            if self.total_pages == True:
                temp_button.background_color =(0.4,0.1,0.7,0.9)

            else:

                temp_button.background_color =(0.6,0.9,0.7,0.9)

            #temp_button.bind(on_release=self.mark(temp_button.text))
            self.root.ids.entries.add_widget(temp_button)


    def handle_completed(self):

        self.root.ids.status_text.text = "Click on a book to get information"
        self.pages = self.book.total_completed_books()
        self.root.ids.pages.text = "Total pages completed: {} ".format(str(self.pages))

        self.root.ids.entries.clear_widgets()
        for i in range(len(self.books_completed)):
            temp_button = Button(text=self.books_completed[i][0])
            temp_button.background_color = (0.4, 0.1, 0.7, 0.6)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries.add_widget(temp_button)


    def press_entry(self, instance):
        # update status text

        self.name_book = instance.text
        print(self.name_book)

        self.book=self.book.display(self.name_book)
        self.root.ids.status_text.text = str(self.book)

    def mark(self,name=""):

        print(name)
        self.b=self.book.search_by_title(name)
        self.h=self.book.mark_complete(self.b)
        self.root.ids.status_text.text = str(self.h)

    def book_to_be_added(self,title,author,pages):
        self.title = title.text
        print("title={}".format(self.title))
        self.author = author.text
        self.pages = pages.text

        if self.title == "" :
            self.root.ids.status_text.text = "All fields must be completed"
            print("blank")

        elif self.author == "":
            self.root.ids.status_text.text = "All fields must be completed"

        elif self.pages.isdigit()== False:
            print("wrong")
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

    def book_length(self):
        print("hello")


ReadingListApp().run()

