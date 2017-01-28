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
h.pages_required_books_()
h.total_completed_books()
h.sort_books()
h.save_Books()


h.display()






