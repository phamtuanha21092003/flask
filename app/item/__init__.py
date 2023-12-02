from flask import Blueprint
from models import ItemModel

bp = Blueprint('main', __name__)

@bp.route('/add', methods=['GET'])
def add():
    return 'pham ha'