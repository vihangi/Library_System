"""
This class is mainly used to display the book details and mark the book as completd . It also calculate if the book length exceeds 500 pages which is then used for
color coding.
"""

class Book:
    def __init__(self,list):
        """
        This function loads a book and stores its details
        :param list: storees a single book
        """
        #displaying book details in status bar
        self.book=list
        self.title=self.book[0]
        self.author=self.book[1]
        self.pages=self.book[2]
        self.status = self.book[3]


    def __str__(self):
        """
        This book is used to display the details of the book
        :return: details of the book
        """
        return "{} by {}, {} pages".format(self.title,self.author,self.pages)

    def mark_complete(self):
        """
        This function is used to mark a book as completed
        :return: none
        """
        #marking the book as completed
        if self.status == "r":
            self.status = "c"


    def book_length(self,pages):
        """
        This function is used to check the number of pages in the book
        :param pages: stores the number of pages
        :return: it return true if the number of pages exceed 500 and return false if the number of pages is less than 500
        """
        self.book_long=pages
        self.pages=int(self.book_long[2])
        #checking the size of the book
        if(self.pages>500):

            return True
        else:
            return False

