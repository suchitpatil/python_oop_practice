class Book():
    def __init__(self,book_id,book_category):
        self.book_id = book_id  #which book
        self.book_category=book_category #which book category
        self.issued_to = -1 #which user has book

    def update_book(self , user_id , action = "issue"):
        '''

        :param user_id: which user is doing the action
        :param action: what is the action(can be issue or return)
        :return: none
        '''
        if (action=="issue"):   #if book has issued
            self.issued_to=user_id  #record current user of book
        elif (action=="return"): #if book has return
            self.issued_to=-1 #indicate book is free and can issued by anyone
        else:
            print("Invalid Action")

class User():
    def __init__(self, user_id, user_category):
        self.user_id = user_id #who is the user
        self.user_category = user_category #what is category type
        self.book_issued = -1 #which book has been issued by user

    def update_user(self, book_id, action = "issue"):
        '''

        :param book_id: action is done for which book by user
        :param action: wether book is issued or return by user
        :return: none
        '''
        if(action=="issue"):
            self.book_issued = book_id #record which book is being issued by user
        elif(action == "return"):
            self.book_issued = -1 #user has no books after returning
        else:
            print("Invalid Action")
print("Adding Harry Potter Book")
harry_potter = Book(book_id=1, book_category="fiction")
print(harry_potter.book_id)
print(harry_potter.book_category)
print(harry_potter.issued_to)

print("Adding User")
suchit =User(user_id=1, user_category="student")
print(suchit.user_id)
print(suchit.user_category)
print(suchit.book_issued)

print("Suchit issues harry potter")
suchit.update_user(book_id = harry_potter.book_id,action="issue")
harry_potter.update_book(user_id= suchit.user_id,action="issue")
print(harry_potter.book_id)
print(harry_potter.book_category)
print(harry_potter.issued_to)
print(suchit.user_id)
print(suchit.user_category)
print(suchit.book_issued)

print("Suchit return harry potter")
suchit.update_user(book_id = harry_potter.book_id,action="return")
harry_potter.update_book(user_id= suchit.user_id,action="return")
print(harry_potter.book_id)
print(harry_potter.book_category)
print(harry_potter.issued_to)
print(suchit.user_id)
print(suchit.user_category)
print(suchit.book_issued)