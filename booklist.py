# create your BookList class in this file



from operator import itemgetter


class BookList():

    def __init__(self):
        FILENAME = "books.csv"
        self.file_list = []
        self.required_books=[]
        self.completed_books=[]
        file_pointer = open(FILENAME, "r")
        for index, data in enumerate(file_pointer.readlines()):
            data = data.strip()
            datum = data.split(",")
            #print(index, datum)
            self.file_list.append(datum)
        self.file_list.sort(key=itemgetter(1, 2))
        #print(self.file_list)




        file_pointer.close()

        self.book=self.file_list


        for i in range(len(self.book)):

            if self.book[i][3] == "r":
                self.required_books.append(self.book[i])

            if self.book[i][3] == "c":
                self.completed_books.append(self.book[i])
        print("required{}".format(self.required_books))
        print("completed{}".format(self.completed_books))


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
        pass
    def sort_books(self):
        pass




