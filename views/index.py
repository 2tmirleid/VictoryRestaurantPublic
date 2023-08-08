from flask import Blueprint, render_template
from controllers.index_controller import Index_Controller

from SQLite.db import get_db
from controllers.main_controller import Main_Controller

index_bp = Blueprint('index', __name__, template_folder='templates/pages')


@index_bp.before_request
def before_request():
    global dbase
    global main

    db = get_db()
    dbase = Index_Controller(db)
    main = Main_Controller(db)


@index_bp.route('/')
@index_bp.route('/index')
@index_bp.route('/home')
def index():
    return render_template('pages/index.html', menu=main.get_menu(),
                           banner=dbase.get_banner(),
                           cook_delecious=dbase.get_cook_delecious(),
                           services=dbase.get_services(),
                           food_menu=dbase.get_foood_menu(),
                           book_table=main.get_book_table(),
                           our_blog=dbase.get_our_blog(),
                           icons=main.get_icons())