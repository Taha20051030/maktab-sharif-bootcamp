books = {}
while True:
    inp = input("Please enter the desired command: add, search, show, exit\n")
    if inp == 'add':
        name = input("please enter name of book\n")
        author = input("please enter name of author\n")
        books[name] = author
    elif inp == 'search':
        name = input("Please enter the name of the book.\n")
        if name not in books:
            print("Unfortunately, this book is not available.")
        else:
            print(f"The author's name is {books[name]}.")
    elif inp == 'show':
        print("List of books:")
        for i in books:
            print(i)
    else:
        break