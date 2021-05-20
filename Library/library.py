class Book:
    def __init__(self, book_id, book_category):
        self.book_id = book_id  # which book
        self.book_category = book_category  # which book category
        self.issued_to = -1  # which user has book

    def update_book(self, user_id, action="issue"):
        """

        :param user_id: which user is doing the action
        :param action: what is the action(can be issue or return)
        :return: none
        """
        if action == "issue":  # if book has issued
            self.issued_to = user_id  # record current user of book
        elif action == "return":  # if book has return
            self.issued_to = -1  # indicate book is free and can issued by anyone
        else:
            print("Invalid Action")


class User:
    def __init__(self, user_id, user_category):
        self.user_id = user_id  # who is the user
        self.user_category = user_category  # what is category type
        self.book_issued = -1  # which book has been issued by user

    def update_user(self, book_id, action="issue"):
        """

        :param book_id: action is done for which book by user
        :param action: wether book is issued or return by user
        :return: none
        """
        if action == "issue":
            self.book_issued = book_id  # record which book is being issued by user
        elif action == "return":
            self.book_issued = -1  # user has no books after returning
        else:
            print("Invalid Action")


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


class Library:
    def __init__(self):
        self.book_dict = {}  # initially there will be no books
        self.user_dict = {}  # intitally there will be no users

    def add_book(self, book_id, book_category):
        if str(book_id) in self.book_dict:
            print("Book_id Already in use!")
        else:
            self.book_dict[str(book_id)] = Book(
                book_id=book_id, book_category=book_category
            )  # add new book.
            print("Added Book id ", book_id, book_category)

    def add_user(self, user_id, user_category):
        if str(user_id) in self.user_dict:
            print("User_Id Already exist!")
        else:
            self.user_dict[str(user_id)] = User(
                user_id=user_id, user_category=user_category
            )  # add new user.
            print("Added User id ", user_id, user_category)

    def book_issue(self, book_id, user_id, user_category):
        # check library owns then book
        if str(book_id) in self.book_dict:
            #   check wether user is registered in library
            if str(user_id) in self.user_dict:
                # check if book is avilable or not
                if self.book_dict[str(book_id)].issued_to == -1:
                    # check if user has return the book
                    if self.user_dict[str(user_id)].book_issued == -1:
                        # then lend book is user
                        # set user's book issued to book id
                        self.user_dict[str(user_id)].book_issued = book_id
                        # set book's isued to user id
                        self.book_dict[str(book_id)].issued_to = user_id
                        print("Issued book {} to user {}".format(book_id, user_id))
                    else:
                        print("Return previous Book!")
                        self.return_book(user_id)
                else:
                    print("Book is Already issued to somebody else!")
            else:
                print("Registering new user ....")
                self.add_user(user_id=user_id, user_category=user_category)
                self.book_issue(
                    book_id=book_id, user_id=user_id, user_category=user_category
                )
        else:
            print("library does not own the book")

    def book_return(self, user_id):
        current_book_id = self.user_dict[str(user_id)].book_issued
        self.user_dict[str(user_id)].book_issued = -1
        self.book_dict[str(current_book_id)].issued_to = -1
        print("Returned book {} from user {} ".format(current_book_id, user_id))


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
library.book_issue(book_id=0, user_id=5, user_category="Student")  # testig issuing book
