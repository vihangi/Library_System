# create your BookList class in this file




from operator import itemgetter
# defining the variables
FILENAME = "books.csv"
required_books = []
add_books = []
completed_books = []
marked_books = []
class BookList():
    def load_books(self):
        pass
    def __init__(self, books=[]):
        self.book=books
        self.title=self.book[0]
        self.author=self.book[1]
        self.pages=self.book[2]
        self.status=self.book[3]
        self.index=self.book[4]




    def __str__(self):
        return "{},{},{},{},{}".format(self.title, self.author,self.pages,self.status,self.index)

    def search_by_title(self,title):
        self.search_title = title
        for i in range(len(self.book)):
            if(self.search_title == self.all_books[i][0]):
                #display
                print(self.book[i])
                break
            else:
                print("not found")
        return self.book

    def add_book(self,title,author,pages):
        self.title = title
        self.author= author
        self.pages= pages

    def total_required_books(self):
        pass

    def total_completed_books(self):
        pass
    def save_Books(self):
        pass
    def sort_books(self):
        pass




