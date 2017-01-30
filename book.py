# create your simple Book class in this file


class Book:
    def __init__(self,list):
        #displaying book details in status bar
        self.book=list
        self.title=self.book[0]
        self.author=self.book[1]
        self.pages=self.book[2]


    def __str__(self):
        return "{} by {}, {} pages".format(self.title,self.author,self.pages)

    def mark_complete(self,name):
        self.completed_book=name
        self.new_book = []
        self.new_book.append(self.completed_book[0])
        self.new_book.append(self.completed_book[1])
        self.new_book.append(self.completed_book[2])
        self.new_book.append("c")
        self.new_book.append(self.completed_book[4])

        return self.new_book

    def book_length(self,pages):
        self.book_long=pages
        self.pages=int(self.book_long[2])
        if(self.pages>500):
            print("pages is more than 500")
            return True
        else:
            print("pages is les than 500")
            return False

