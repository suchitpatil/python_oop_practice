from library import *

# print("Adding Harry Potter Book")
# harry_potter = Book(book_id=1, book_category="fiction")
# print(harry_potter.book_id)
# print(harry_potter.book_category)
# print(harry_potter.issued_to)
#
# print("Adding User")
# suchit = User(user_id=1, user_category="student")
# print(suchit.user_id)
# print(suchit.user_category)
# print(suchit.book_issued)
#
# print("Suchit issues harry potter")
# suchit.update_user(book_id=harry_potter.book_id, action="issue")
# harry_potter.update_book(user_id=suchit.user_id, action="issue")
# print(harry_potter.book_id)
# print(harry_potter.book_category)
# print(harry_potter.issued_to)
# print(suchit.user_id)
# print(suchit.user_category)
# print(suchit.book_issued)
#
# print("Suchit return harry potter")
# suchit.update_user(book_id=harry_potter.book_id, action="return")
# harry_potter.update_book(user_id=suchit.user_id, action="return")
# print(harry_potter.book_id)
# print(harry_potter.book_category)
# print(harry_potter.issued_to)
# print(suchit.user_id)
# print(suchit.user_category)
# print(suchit.book_issued)

library = Library()  # making library object
for i in range(5):  # added 5 books
    library.add_book(i, "Fiction")
for i in range(5):  # added 5 users
    library.add_user(i, "Student")
library.add_book(0, "Fiction")  # testing add_book exception
library.add_user(0, "Student")  # testing add_user exception

for i in range(5):  # issuing book
    library.book_issue(i, i, "Student")

library.book_issue(
    book_id=0, user_id=5, user_category="Student"
)  # testing issuing book
library.book_return(user_id=0)  # return book
library.book_issue(
    book_id=0, user_id=5, user_category="Student"
)  # testing issuing book
