# create your BookList class in this file




from operator import itemgetter
# defining the variables
FILENAME = "books.csv"
required_books = []
add_books = []
completed_books = []
marked_books = []
class BookList():
    def load_file(self):
            """
            This function loads the file and reads all the data. It stores the data onto a list. The list is then sorted and
            appended with index numbers according to the authors name . It also seperates the data into required_books and
            completed_books list based on whether its third index is "r" or "c" respectively.
            :return: null
            """
            # defining these variables as global so that they can be called in any function
            global required_books
            global completed_books
            global index_value
            datum = []
            self.all_books = []
            self.required = "r"
            self.completed = "c"
            self.file_pointer = open(FILENAME, "r")
            # reading the file
            for index, data in enumerate(self.file_pointer.readlines()):
                self.data = self.data.strip()
                selfdatum = self.data.split(",")
                self.all_books.append(datum)
            self.all_books.sort(key=itemgetter(1, 2))
            # distrubuting the data into required_books and completed_books
            for i in range(len(self.all_books)):
                index_value = str(i)
                self.all_books[i].append(index_value)
            for i in range(len(self.all_books)):
                if self.all_books[i][3] == "r":
                    required_books.append(self.all_books[i])
                if self.all_books[i][3] == "c":
                    completed_books.append(self.all_books[i])

            self.file_pointer.close()
            print(self.all_books)

    def search_by_title(self,title):
        self.title = title
        for i in range(len(self.all_books)):
            if self.title == self.all_books[i]:
                #display
                self.book= self.all_books[i]
                break
        return self.book

    def add_book(self,title,author,pages):
        self.title = title
        self.author= author
        self.pages= pages

    def total_required_books(self):

    def total_completed_books(self):

    def save_Books(self):

    def sort_books(self):





load_file()
