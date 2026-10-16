import library.db as lib

name = input("Enter your name = ")

print(f"Hello , {name}..!")


while(True):
    print("1.Insert book")
    print("2.Display books")
    print("3.Display books which has more than five copies")
    print("4.Update book")
    print("5.Delete book")
    print("6.Exit")

    ch = input("Enter choice (1/2/3/4/5/6) = ")
    if ch == "1":
        book_title = input("Enter book name = ")
        book_author = input("Enter author name = ")
        book_stock = int(input("Enter no.of.copies = "))

        lib.insert_book(book_title , book_author , book_stock)

    elif ch == "2":
        lib.display_book()

    elif ch == "3":
        lib.display_book_five_copies()

    elif ch == "4":
        book_id = int(input("Enter book id = "))
        stock = int(input("Enter no.of.copies = "))

        lib.update_copies(book_id , stock)
    elif ch == "5":
        book_id = int(input("Enter book id = "))
        lib.delete_book(book_id)
    elif ch == "6":
        break;
    else:
        break;
        print("Thank you using our system..!")

