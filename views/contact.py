from flask import Blueprint, render_template
from controllers.contact_controller import Contact_Controller

from SQLite.db import get_db
from controllers.main_controller import Main_Controller

contact_bp = Blueprint('contact', __name__, template_folder='templates/pages')

@contact_bp.before_request
def before_request():
    global dbase
    global main

    db = get_db()
    dbase = Contact_Controller(db)
    main = Main_Controller(db)


@contact_bp.route('/contact')
def contact():
    return render_template('pages/contact.html',
                           title='Contact Us',
                           menu=main.get_menu(),
                           icons=main.get_icons(),
                           contact_form=dbase.get_contact_form())