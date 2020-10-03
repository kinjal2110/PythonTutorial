# create a library class
# define method for display book- displaybook()
# if customer  want to land book then land method call- landbook()
# if customer want to donate book then add function call.- addbook()
# if customer to return book- returnbook()
# you can maintain dictionary in landbook, who owns book if not present
# dictionary - key=book, value=nameofperson
# create a main function and run an infinite while loop asking users for their input
# kslibrary = Library(listofbook, library_name)

class Library:
    def __init__(self, listofbook, library_name):
        # creating dictionary of all books
        self.lend_data = {}
        self.listofbook = listofbook
        self.library_name = library_name

        # adding books to dictionary
        for books in self.listofbook:
            # None means no reader have lend this book.
            self.lend_data[books] = None

    def display_book(self):
        for index, books in enumerate(self.listofbook):
            print(f"{index}:{books}")

    def lend_book(self, book, reader):
        if book in self.listofbook:
            if self.lend_data[book] is None:
                self.lend_data[book] = reader
            else:
                print(f"Sorry this book lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self, book, reader):
        if book in self.listofbook:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry but this book is not lend")
        else:
            print("You written wrong book name")

    def add_book(self, book_name):
        self.listofbook.append(book_name)       #using append we can add book
        self.lend_data[book_name] = None

    def delete_book(self, book_name):
        self.listofbook.remove(book_name)   #also using remove we can remove it
        self.lend_data.pop(book_name)       #using pop we can delete


def main():
    # by default variables
    list_book = ['c++', 'java', 'android', 'balagurusamy']
    library_name = "GEC Bhavnagar"
    secret_key = 654321

    KsLibrary = Library(list_book, library_name)

    print(f"Welcome to {KsLibrary.library_name} library")
    print("0 for exit")
    print("'d' using display the books")
    print("'l' using lend the books")
    print("'r' using return the books")
    print("'a' using add the books")
    print("'del' using delete the books")

    Exit = False
    while(Exit is not True):
        _in = input("\noptions: ")

        if _in == 0:
            Exit = True

        elif _in == 'd':
            KsLibrary.display_book()

        elif _in == 'l':
            _in2 = input("What is your name: ")
            _in3 = input("Which book do you want to lend: ")
            KsLibrary.lend_book(_in2,_in3)

        elif _in == 'a':
            _in2 = input("Book name: ")
            KsLibrary.add_book(_in2)

        elif _in == 'del':
            _in_secret = int(input("Write the secret key to delete book: "))
            if (_in_secret == secret_key):
                _in2 = input("Which book you want to delete: ")
                KsLibrary.delete_book(_in2)
            else:
                print("Sorry we can't delete book")

        elif _in == 'r':
            _in2 = input("What's your name: ")
            _in3 = input("Which book do you want to return: ")
            KsLibrary.return_book(_in2, _in3)

if __name__ == "__main__":
     main()