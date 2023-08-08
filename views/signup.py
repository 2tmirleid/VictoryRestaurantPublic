from flask import Blueprint, render_template, request

from controllers.main_controller import Main_Controller
from controllers.signup_controller import Signup_Controller
from controllers.index_controller import Index_Controller

from SQLite.db import get_db

signup_bp = Blueprint('signup', __name__, template_folder='templates/pages')


@signup_bp.before_request
def before_request():
    global dbase
    global db
    global main

    db = get_db()
    dbase = Index_Controller(db)
    main = Main_Controller(db)


@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        Signup_Controller(db).signup(request.form['email'])

    return render_template('pages/index.html', menu=main.get_menu(),
                           banner=dbase.get_banner(),
                           cook_delecious=dbase.get_cook_delecious(),
                           services=dbase.get_services(),
                           food_menu=dbase.get_foood_menu(),
                           book_table=main.get_book_table(),
                           our_blog=dbase.get_our_blog(),
                           icons=main.get_icons())
