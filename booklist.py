# create your BookList class in this file



from operator import itemgetter
from book import Book

class BookList():

    def __init__(self):

        self.file_list = []
        self.required_books=[]
        self.completed_books=[]
        file_pointer = open("books.csv", "r")
        for index, data in enumerate(file_pointer.readlines()):
            data = data.strip()
            datum = data.split(",")

            #print(index, datum)
            self.file_list.append(datum)

        #self.file_list.sort(key=itemgetter(1, 2))
        #print(self.file_list)

        for i in range(len(self.file_list)):
            self.index_value = str(i)
            self.file_list[i].append(self.index_value)


        file_pointer.close()

        self.book=self.file_list


        for i in range(len(self.book)):

            if self.book[i][3] == "r":
                self.required_books.append(self.book[i])

            if self.book[i][3] == "c":
                self.completed_books.append(self.book[i])
        #print("required{}".format(self.required_books))
        #print("completed{}".format(self.completed_books))


    def __str__(self):
        return "{}".format(self.book)

    def search_by_title(self,title):
        count=0
        self.search_title = title
        for i in range(len(self.file_list)):


            if(self.search_title==self.file_list[i][0]):
                #display

                print("found")
                count=count+1
                return self.book[i]
                break
            else:
                continue
        if count==0:
            print("not found")


    def add_book(self,title,author,pages):
        self.title = title
        self.author= author
        self.pages= pages
        self.data=[]
        self.data.append(self.title)
        self.data.append(self.author)
        self.data.append(self.pages)
        self.data.append("r")
        self.index_value=int(self.index_value)+1
        self.data.append(self.index_value)
        self.book.append(self.data)


        self.required_books.append(self.data)


        return self.file_list

    def pages_required_books_(self):

        self.total_pages=0
        for i in range(len(self.required_books)):
            self.total_pages=int(self.required_books[i][2])+self.total_pages

        print(self.total_pages)


    def total_completed_books(self):
        self.total_pages = 0
        for i in range(len(self.completed_books)):
            self.total_pages = int(self.completed_books[i][2]) + self.total_pages

        print(self.total_pages)

    def save_Books(self):
        self.list_books = []
        dataValue = ""
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
        print("{} books saved to {} \nHave a nice day :)".format(len(self.list_books) - 1, "books.csv"))


    def sort_books(self):
        self.book.sort(key=itemgetter(1, 2))
        print(self.book)

    def display(self):
        h=Book(self.book[1])
        q=h.mark_completed(self.required_books[1])
        self.required_books[1]=q
        print(self.required_books)
        h.book_length(self.book[1])



