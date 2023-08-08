import sqlite3

class Contact_Controller:
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

    def get_contact_form(self):
        try:
            self.__cur.execute("""SELECT * FROM contact_form""")
            result = self.__cur.fetchall()
            if result:
                return result
                print('[SQLite] - - [Successful get contact_form]')
        except sqlite3.Error as err:
            print(f'[ERROR] - - [{err}]')