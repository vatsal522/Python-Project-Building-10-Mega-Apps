import sqlite3
def connect():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('create table if not exists book (id INTEGER primary key, title text, author text, year int, isbn int)')
    conn.commit()
    conn.close()

connect()

def insert(title,author,year,isbn):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('insert into book values(NULL,?,?,?,?)',(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('select * from book')
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('select * from book where title=? or author=? or year=? or isbn=?',(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows



def delete(idno):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('delete from book where id=?',(idno,))
    conn.commit()
    conn.close()


def update(idno,title,author,year,isbn):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('update book set title=?, author=?, year=?, isbn=? where id=?',(title,author,year,isbn,idno))
    conn.commit()
    conn.close()



update(1,'Moon','NASA',2011,2025513)
print(view())
"""
print(view())
print("")
insert('Mayaoo','Nikita',1550,92514626262)
print("")
print(search(title='Smith'))
print("")
print("")

print("")
print(view())
print("")
delete(3)

print("")
print(view())
"""
