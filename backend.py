import sqlite3


class Database:
    def __init__(self):
        self.conn= sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author,year, isbn))
        self.conn.commit()
       

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title = "", author = "", year = "", isbn = ""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()
        

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id =?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        






#insert("Music Box", "Cakic Miroslav", 2010, 76428734)
#insert("Patrola","Milan Vignjevic", 2000, 984394332937)
#print(view())
#print(search("Music Box"))
#delete(10)
#update(1, "Patrola", "Mica Vignjevic", 2010, 876387 )
#update(9, "Music Box", "Mirosalv Cakic", 2010, 8768768 )
#print(view())