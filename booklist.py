# create your BookList class in this file



from operator import itemgetter


class BookList():
    def load_books(self):
        pass




    def load_books(self):
        FILENAME = "books.csv"
        self.file_list=[]
        file_pointer = open(FILENAME, "r")
        for index, data in enumerate(file_pointer.readlines()):
            data = data.strip()
            datum = data.split(",")
            print(index, datum)
            self.file_list.append(datum)
        self.file_list.sort(key=itemgetter(1, 2))
        print(self.file_list)
        file_pointer.close()

    def __init__(self):
        FILENAME = "books.csv"
        self.file_list = []
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
        self.title=self.book[0]
        self.author=self.book[1]
        self.pages=self.book[2]
        self.status=self.book[3]
        self.index=self.book[4]




    def __str__(self):
        return "{},{},{},{},{}".format(self.title, self.author,self.pages,self.status,self.index)

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

        self.file_list.append(self.data)
        return self.file_list

    def total_required_books(self):
        pass

    def total_completed_books(self):
        pass
    def save_Books(self):
        pass
    def sort_books(self):
        pass




