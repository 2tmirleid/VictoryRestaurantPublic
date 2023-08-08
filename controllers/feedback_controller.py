from flask import Flask
from flask_mail import Mail, Message
from config import *
import sqlite3

app = Flask(__name__)

app.config['MAIL_SERVER'] = SERVER
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = USERNAME
app.config['MAIL_PASSWORD'] = PASSWORD

mail = Mail(app)


class Feedback_Controller:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def feedback(self, name, email, phone, msg):
        try:
            sql = self.__cur.execute("""INSERT INTO feedback VALUES(NULL, ?, ?, ?, ?)""",
                                     (name, email, phone, msg))
            result = self.__db.commit()

            msg = Message(
                f"test",
                sender=USERNAME,
                recipients=[TESTUSERNAME])
            mail.connect()
            mail.send(msg)

            if result:
                return result
                print('[SQLite] - - [Successful adding data]')


        except sqlite3.Error as err:
            print(f'[ERROR] - - [{err}]')
        return []

