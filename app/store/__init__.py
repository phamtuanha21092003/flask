from flask import Blueprint, request
from models import StoreModel
from db import db
from schemas import  store_schemas

bp = Blueprint('store', __name__)

@bp.route('/', methods=['GET'])
def index():
    stores = StoreModel.query.all()

    stores_data = store_schemas.dump(stores)
    return {"stores": stores_data}
    
    # print(stores)
    # name = request.args['name']

    # user = User(name)

    # user = user_schema.dump(user)
    return {"store": stores}
    
    # return {"abc": [
    #     {
    #         "id": row.id,
    #         "name": row.name
    #     } for row in stores
    # ]}

@bp.route('/add', methods=['POST'])
def add():
    name = request.get_json()['name']
    id_store = request.get_json()['id']
    item = StoreModel(name=name, id=id_store)
    db.session.add(item)
    db.session.commit()
    return {"status": 'add successfully'}, 201
