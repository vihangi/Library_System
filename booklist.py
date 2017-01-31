"""
This file is used to perform all the functions and is called in the main class.
"""



from operator import itemgetter
from book import Book

class BookList():

    def __init__(self):
        """
        The csv file is loaded in this file and stored into lists .
        """

        self.file_list = []
        self.required_books=[]
        self.completed_books=[]
        file_pointer = open("books.csv", "r")
        #storing file details onto a list
        for index, data in enumerate(file_pointer.readlines()):
            data = data.strip()
            datum = data.split(",")
            self.file_list.append(datum)

        for i in range(len(self.file_list)):
            self.index_value = str(i)
            self.file_list[i].append(self.index_value)
        #closing the file
        file_pointer.close()
        self.book=self.file_list

        #dividing the list onto a list which stores required and completed books respectively
        for i in range(len(self.book)):
            if self.book[i][3] == "r":
                self.required_books.append(self.book[i])

            if self.book[i][3] == "c":
                self.completed_books.append(self.book[i])



    def __str__(self):
        """
        details of the book
        :return: details of the book
        """
        return "{}".format(self.book)

    def search_by_title(self,title):
        """
        This is used to search a book by its title
        :param title: stores the name of the book
        :return: returns the book details when the book is found
        """

        self.search_title = title
        #searching the book by its title
        for i in range(len(self.file_list)):
            if(self.search_title ==self.file_list[i][0]):
                return self.file_list[i]
                break


    def mark_book(self,book):
        """
        This function is used to mark the book as completed
        :param book: used to pass the details of the book
        :return:
        """
        self.search_title=book

        for i in range(len(self.required_books)):
            if(self.search_title[0] ==self.required_books[i][0]):
                #marking the book as completed
                self.required_books[i][3] = "c"
                self.completed_books.append(self.required_books[i])
                self.required_books.pop(i)
                break






    def add_book(self,title,author,pages):
        """
        THis function is used to add a new book
        :param title: stores the name of the book
        :param author: stores the author of the book
        :param pages: stores the total number of pages of the book
        :return: the required book list
        """
        self.title = title
        self.author= author
        self.pages= pages
        #storing the details onto a list
        self.data=[]
        self.data.append(self.title)
        self.data.append(self.author)
        self.data.append(self.pages)
        self.data.append("r")
        self.index_value=int(self.index_value)+1
        self.data.append(self.index_value)
        self.book.append(self.data)
        #appending the required books list
        self.required_books.append(self.data)
        return self.required_books

    def pages_required_books(self):
        """
        This function is used to calculate the total number of pages of the required book
        :return: total pages of the required book
        """
        self.total= 0
        #calculating the pages
        for i in range(len(self.required_books)):
            self.total_pages=int(self.required_books[i][2])
            self.total = self.total_pages + self.total
        self.t = str(self.total)
        return self.t


    def total_completed_books(self):
        """
        This function is used to calculate the total number of pages of the completed book
        :return: total pages of the completed book
        """
        self.total_pages = 0
        for i in range(len(self.completed_books)):
            self.total_pages = int(self.completed_books[i][2]) + self.total_pages

        return self.total_pages

    def save_Books(self):
        """
        This function is used to save the changes onto the csv file
        :return: none
        """
        self.list_books = []

        # stores all the books in one single list
        for i in range(len(self.required_books)):
            self.list_books.append(self.required_books[i])
        for i in range(len(self.completed_books)):
            self.list_books.append(self.completed_books[i])
        self.list_books.sort(key=itemgetter(1, 2))

        # opens the file to rewrite
        outFile = open("books.csv", "w")

        for i in range(len(self.list_books)):
            # slicing the data to remove the index number
            data = self.list_books[i][:4]
            # writing in the file
            for j in range(4):
                dataValue = data[j]
                outFile.write(dataValue)
                if j < 3:
                    outFile.write(",")
                else:
                    outFile.write("\n")
        outFile.close()


    def sort_books_required(self):
        """
        This is used to sort the required books
        :return: none
        """
        self.required_books.sort(key=itemgetter(1, 2))

    def sort_books_completed(self):
        """
        This is used to sort the completed books
        :return: none
        """
        self.completed_books.sort(key=itemgetter(1, 2))


    def display(self,name):
        """
        This is used to display the details of the book
        :param name: store book name
        :return: book details
        """
        self.name=name
        for i in range(len(self.book)):
            if self.name== self.book[i][0]:
                self.h=Book(self.book[i])
                return self.h
