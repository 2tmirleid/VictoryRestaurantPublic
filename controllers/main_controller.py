import sqlite3
class Main_Controller:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        try:
            self.__cur.execute("""SELECT * FROM menu""")
            result = self.__cur.fetchall()
            if result:
                return result
                print('[SQLite] - - [Successful get menu]')
        except sqlite3.Error as err:
            print(f'[ERROR] - - [{err}]')

    def get_icons(self):
        try:
            self.__cur.execute("""SELECT * FROM icons""")
            result = self.__cur.fetchall()
            if result:
                return result
                print('[SQLite] - - [Successful get icons]')
        except sqlite3.Error as err:
            print(f'[ERROR] - - [{err}]')

    def get_book_table(self):
        try:
            self.__cur.execute("""SELECT * FROM book_table""")
            result = self.__cur.fetchall()
            if result:
                return result
                print('[SQLite] - - [Successful get book_table]')
        except sqlite3.Error as err:
            print(f'[ERROR] - - [{err}]')