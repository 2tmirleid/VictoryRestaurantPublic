import sqlite3

class Reservation_Controller:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def reservation(self, name, phone, person, day, hour):
        try:
            sql = self.__cur.execute("""INSERT INTO reservation VALUES(NULL, ?, ?, ?, ?, ?)""",
                                     (name, phone, person, day, hour))
            result = self.__db.commit()
            if result:
                return result
                print('[SQLite] - - [Successful adding data]')


        except sqlite3.Error as err:
            print(f'[ERROR] - - [{err}]')
        return []
