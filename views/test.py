from flask import Flask, Blueprint

test_bp = Blueprint('test', __name__)


@test_bp.route('/test', methods=['GET'])
def menu():
    return 'test'
