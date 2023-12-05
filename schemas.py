from flask_marshmallow import Marshmallow
from models import StoreModel, ItemModel

ma = Marshmallow()

class StoreSchema(ma.SQLAlchemySchema):
    class Meta:
        model = StoreModel

    id = ma.auto_field()
    name = ma.auto_field()
    items = ma.Nested(lambda: ItemSchema(), many=True)

class ItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ItemModel

    id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()
    store_id = ma.auto_field(load_only=True)
    store = ma.Nested(lambda: StoreSchema())

store_schema = StoreSchema()
store_schemas = StoreSchema(many=True)

item_schema = ItemSchema()
item_schemas = ItemSchema(many=True)
