from flask import Blueprint, request
from models import ItemModel, StoreModel
from db import db
from schemas import item_schemas

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    items = ItemModel.query.all()
    
    items_data = item_schemas.dump(items)
    return {"item": items_data}

@bp.route('/add', methods=['POST'])
def add():
    item_id = request.get_json()['id']
    name = request.get_json()['name']
    price = request.get_json()['price']
    store_id = request.get_json()['store_id']
    store = StoreModel.query.get_or_404(store_id)
    
    item = ItemModel(id=item_id, name=name, price=price, store_id=store_id, store=store)
    
    
    db.session.add(item)
    db.session.commit()
    return {"status": 'add successfully'}, 201