# create your simple Book class in this file


class Book:
    def __init__(self,list):
        #displaying book details in status bar
        self.book=list
        self.title=self.book[0]
        self.author=self.book[1]
        self.pages=self.book[2]
        self.status = self.book[3]


    def __str__(self):
        return "{} by {}, {} pages".format(self.title,self.author,self.pages)

    def mark_complete(self):
        if self.status == "r":
            self.status = "c"


    def book_length(self,pages):
        self.book_long=pages
        self.pages=int(self.book_long[2])
        if(self.pages>500):

            return True
        else:
            return False

