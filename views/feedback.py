from flask import Blueprint, render_template, request
from controllers.feedback_controller import Feedback_Controller
from controllers.contact_controller import Contact_Controller

from SQLite.db import get_db
from controllers.main_controller import Main_Controller

feedback_bp = Blueprint('feedback', __name__, template_folder='templates/pages')


@feedback_bp.before_request
def before_request():
    global db
    global main

    db = get_db()
    main = Main_Controller(db)


@feedback_bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        Feedback_Controller(db).feedback(request.form['name'],
                                         request.form['email'],
                                         request.form['phone'],
                                         request.form['message'])

    return render_template('pages/contact.html',
                           title='Contact Us',
                           menu=main.get_menu(),
                           icons=main.get_icons(),
                           contact_form=Contact_Controller(db).get_contact_form())
