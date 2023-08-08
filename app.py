from flask import Flask, render_template

from views.signup import signup_bp
from views.menu import menu_bp
from views.blog import blog_bp
from views.contact import contact_bp
from views.reservation import reservation_bp
from views.index import index_bp
from views.feedback import feedback_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(reservation_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(feedback_bp)

if __name__ == '__main__':
    app.run(debug=True)
