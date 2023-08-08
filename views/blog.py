from flask import Blueprint, render_template
from controllers.blog_controller import Blog_Controller
from controllers.main_controller import Main_Controller

from SQLite.db import get_db

blog_bp = Blueprint('blog', __name__, template_folder='templates/pages')

@blog_bp.before_request
def before_request():
    global main
    global dbase
    global db

    db = get_db()
    dbase = Blog_Controller(db)
    main = Main_Controller(db)


@blog_bp.route('/blog')
def blog():
    return render_template('pages/blog.html',
                           title='Our Blog',
                           menu=main.get_menu(),
                           icons=main.get_icons(),
                           blog_page=dbase.get_blog_page())