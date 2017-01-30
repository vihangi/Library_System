"""
(incomplete) Tests for Book class
"""
from booklist import BookList
from book import Book

h=BookList()
print(h)
h.mark_completed("Developing the Leader Within You")
q=h.search_by_title("In Search of Lost Time")
print(q)
print(h.mark_completed(q))
print(h.add_book("aa","ss","22"))
h.save_Books()
print(h.pages_required_books())


#print(m)

#h.save_Books()








