"""
(incomplete) Tests for Book class
"""
from booklist import BookList
from book import Book

h=BookList()
print(h)
q=h.search_by_title("In Search of Lost Time")
print(q)
print(h.add_book("aa","ss","22"))

h.display()

#h.save_Books()








