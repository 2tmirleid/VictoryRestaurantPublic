import sqlite3

class Menu_Controller:
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

    def get_breakfast_menu(self):
        try:
            self.__cur.execute("""SELECT * FROM breakfast_menu""")
            result = self.__cur.fetchall()
            if result:
                return result
                print('[SQLite] - - [Successful get breakfast_menu]')
        except sqlite3.Error as err:
            print(f'[ERROR] - - [{err}]')

    def get_lunch_menu(self):
        try:
            self.__cur.execute("""SELECT * FROM lunch_menu""")
            result = self.__cur.fetchall()
            if result:
                return result
                print('[SQLite] - - [Successful get lunch_menu]')
        except sqlite3.Error as err:
            print(f'[ERROR] - - [{err}]')

    def get_dinner_menu(self):
        try:
            self.__cur.execute("""SELECT * FROM dinner_menu""")
            result = self.__cur.fetchall()
            if result:
                return result
                print('[SQLite] - - [Successful get dinner_menu]')
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