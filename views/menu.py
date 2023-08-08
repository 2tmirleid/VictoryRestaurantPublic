from flask import Blueprint, render_template

from controllers.main_controller import Main_Controller
from controllers.menu_controller import Menu_Controller

from SQLite.db import get_db


menu_bp = Blueprint('menu', __name__, template_folder='templates/pages')

@menu_bp.before_request
def before_request():
    global dbase
    global main

    db = get_db()
    dbase = Menu_Controller(db)
    main = Main_Controller(db)


@menu_bp.route('/menu')
def menu():
    return render_template('pages/menu.html',
                           title='Our Menus',
                           menu=main.get_menu(),
                           icons=main.get_icons(),
                           breakfast_menu=dbase.get_breakfast_menu(),
                           lunch_menu=dbase.get_lunch_menu(),
                           dinner_menu=dbase.get_dinner_menu(),
                           book_table=main.get_book_table())