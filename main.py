"""
Name: Vihangi Vagal
Date: 31st January 2017
Brief Project Description: This project uses two classes which is loaded in the main file. The books are segregated
as required and completed. The required books are displayed with color coding accroding to their length , and can
be marked as completed. The completed books are displayed and details for each book is displayed. The user can also
add a new book.
GitHub URL:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'



from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from booklist import BookList
from book import Book
# Create your main program in this file, using the ReadingListApp class






class ReadingListApp(App):


    def build(self):
        """
        This function is used to call the kivi file
        :return:
        """
        self.title = "Reading List 2.0"
        #loading kivy file
        self.root = Builder.load_file('app.kv')
        self.book = BookList()
        self.books_required = self.book.required_books
        self.books_completed = self.book.completed_books
        self.handle_required()
        return self.root

    def handle_required(self):
        """
        This is used to list the required books and create a button for each required book.
        Through this function the user can mark a book as completed
        :return: none
        """
        #loading class book list
        self.book=BookList()
        self.books_required = self.book.required_books
        self.books_completed = self.book.completed_books
        self.root.ids.status_text.text = "Click Books to mark them as completed"
        #loading the total pages of the required books
        self.pages = self.book.pages_required_books()
        self.root.ids.pages.text = "Total pages to read: {} ".format(str(self.pages))
        #reloading file
        self.root.ids.entries.clear_widgets()


        #creating buttons for required books
        for i in range(len(self.books_required)):

            temp_button = Button(text=self.books_required[i][0])

            self.total=Book(self.books_required[i])
            self.total_pages = self.total.book_length(self.books_required[i])

            temp_button.bind(on_release=self.press_entry)
            #color coding according to the length of the book
            if self.total_pages == True:
                temp_button.background_color =(0.4,0.1,0.7,0.9)

            else:

                temp_button.background_color =(0.6,0.9,0.7,0.9)


            self.root.ids.entries.add_widget(temp_button)



    def handle_completed(self):
        """
        This is used to list the completed books and create a button for each completed book.
        Through this function the user can access details of a book which is completed.
        :return: none
        """
        self.book=BookList()
        self.books_required = self.book.required_books
        self.books_completed = self.book.completed_books
        self.root.ids.status_text.text = "Click on a book to get information"
        #the total pages of the completed books
        self.pages = self.book.total_completed_books()
        self.root.ids.pages.text = "Total pages completed: {} ".format(str(self.pages))

        self.root.ids.entries.clear_widgets()
        for i in range(len(self.books_completed)):
            temp_button = Button(text=self.books_completed[i][0])
            #assigning a color for the button
            temp_button.background_color = (0.4, 0.13, 0.9, 0.8)
            #action when the button is pressed
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries.add_widget(temp_button)


    def press_entry(self, instance):
        """
        This function is used to display details of the completed books and mark books as completed
        :param instance: name of the button
        :return: none
        """
        #storing the name of the button
        self.name_book = instance.text
        self.bo=BookList()
        #searching the book details using the name of the button
        self.g = self.bo.search_by_title(self.name_book)
        #the book is completed
        if self.g[3]=="c":
            self.bo = self.bo.display(self.name_book)
            self.root.ids.status_text.text = "{} (completed)".format(str(self.bo))
        #the book needs to be completed or to mark it as completed
        if self.g[3]=="r":
            print("hello")
            self.h = self.bo.mark_book(self.g)
            self.bo.save_Books()
            self.handle_completed()





    def book_to_be_added(self,title,author,pages):
        """
        This function is used to add a new book and error checking of the details entered by the user

        :param title: stores book name
        :param author: stores book author
        :param pages: stores book pages
        :return:
        """
        #storing the book details
        self.title = title.text
        self.author = author.text
        self.pages = pages.text

        #error checking
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
        Clear all of the text inputs used for adding a new book
        :return:none
        """
        self.root.ids.input_title.text = ""
        self.root.ids.input_author.text = ""
        self.root.ids.input_pages.text = ""



ReadingListApp().run()

