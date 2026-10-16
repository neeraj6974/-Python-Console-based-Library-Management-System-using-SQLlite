import sqlite3

db = "./library.db"
con = sqlite3.connect(db)
cur = con.cursor()


def insert_book(book_title , book_author , stock):
    cur.execute("CREATE TABLE IF NOT EXISTS books(book_id INTEGER PRIMARY KEY AUTOINCREMENT , book_title TEXT NOT NULL , book_author TEXT NOT NULL , stock INTEGER NOT NULL)")
    cur.execute("INSERT INTO books(book_title , book_author , stock)VALUES(? , ? , ?)",(book_title , book_author , stock))

    print("Book Added Successfully..!")
    con.commit()


def display_book():
    choice = input("want to show all books ?(y/n) ")
    if(choice == "n"):
        book_author = input("Enter the name of the author")
        
        cur.execute("SELECT * FROM books WHERE book_author = ?" , (book_author,))
        record = cur.fetchall()
        
        for row in record:
            print(row)
    elif(choice == "y"):
        cur.execute("SELECT * FROM books")
        record = cur.fetchall()
        
        for row in record:
            print(row)
    else:
        print("Invalid Choice")

def display_book_five_copies():
    cur.execute("SELECT * FROM books WHERE stock > 5")

    record = cur.fetchall()

    for row in record:
        print(row)


def update_copies(book_id , stock):
    cur.execute("SELECT * FROM books WHERE book_id = ?" , (book_id,))
    record = cur.fetchall()

    new_stock = stock
    
    for row in record:
        new_stock += row[3]

    cur.execute("UPDATE books SET stock = ? WHERE book_id = ?" , (new_stock,book_id))
    print("Copies Updated")
    con.commit()

def delete_book(book_id):
    cur.execute("DELETE FROM books WHERE book_id = ?" , (book_id,))
    print("Book Deleted..!")
    con.commit()






