from flask import Blueprint, render_template, request

from controllers.main_controller import Main_Controller
from controllers.reservation_controller import Reservation_Controller
from controllers.index_controller import Index_Controller

from SQLite.db import get_db

reservation_bp = Blueprint('reservation', __name__, template_folder='templates/pages')


@reservation_bp.before_request
def before_request():
    global dbase
    global db
    global main

    db = get_db()
    dbase = Index_Controller(db)
    main = Main_Controller(db)


@reservation_bp.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        Reservation_Controller(db).reservation(request.form['name'],
                                               request.form['phone'],
                                               request.form['person'],
                                               request.form['day'],
                                               request.form['hour'])

    return render_template('pages/index.html', menu=main.get_menu(),
                           banner=dbase.get_banner(),
                           cook_delecious=dbase.get_cook_delecious(),
                           services=dbase.get_services(),
                           food_menu=dbase.get_foood_menu(),
                           book_table=main.get_book_table(),
                           our_blog=dbase.get_our_blog(),
                           icons=main.get_icons())
