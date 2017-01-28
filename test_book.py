"""
(incomplete) Tests for Book class
"""
from booklist import BookList
"""

from operator import itemgetter
#defining the variables
FILENAME = "books.csv"
required_books=[]
add_books=[]
completed_books =[]
marked_books=[]

def read():
    datum = []
    all_books = []
    required = "r"
    completed = "c"
    file_pointer= open(FILENAME, "r")
        #reading the file
    for index, data in enumerate(file_pointer.readlines()):
            data = data.strip()
            datum = data.split(",")
            all_books.append(datum)
    all_books.sort(key=itemgetter(1,2))
        #distrubuting the data into required_books and completed_books
    for i in range(len(all_books)):
            index_value = str(i)
            all_books[i].append(index_value)
    for i in range(len(all_books)):
            if all_books[i][3] == "r":
                required_books.append(all_books[i])

            if all_books[i][3] == "c":
                completed_books.append(all_books[i])

    file_pointer.close()
    print(all_books)
    for i in range(len(all_books)):
        print(BookList(all_books[i]))
    f="Devloping the Leader Within You"
    """
    #print(BookList.search_by_title(f))

    # test mark_completed()

h=BookList()
print(h)
q=h.search_by_title("In Search of Lost Time")
print(q)
print(h.add_book("aa","ss","22"))
h.pages_required_books_()
h.total_completed_books()
