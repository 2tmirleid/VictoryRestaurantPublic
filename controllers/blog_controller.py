import sqlite3

class Blog_Controller:
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

    def get_blog_page(self):
        try:
            self.__cur.execute("""SELECT * FROM blog_page""")
            result = self.__cur.fetchall()
            if result:
                return result
                print('[SQLite] - - [Successful get blog_page]')
        except sqlite3.Error as err:
            print(f'[ERROR] - - [{err}]')