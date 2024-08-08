from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import items
import uuid


blp = Blueprint("items",__name__ ,description="Operations on Items")

# Endpoints for "/item"

@blp.route("/item")
class Item(MethodView):
    def get(self):
        return {"items": list(items.values())},200
    
    def post(self):
        item_data = request.get_json()
        if ("price" not in item_data
            or "store_id" not in item_data
            or "name" not in item_data
        ):
            abort(400,message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.")

        for item in items.values:
            if  item_data["name"]==item["name"] and item_data["store_id"]:
                abort(400,message="Item name and Store id  exists")

        if item_data["store_id"] not in stores:
            return {"message": "store not found."},404
        
        item_id = uuid.uuid4().hex
        item = {**item_data,"id":item_id}
        items[item_id]=item
        return {"item": item},201

# Endpoint  for "/item/<item_id>"

@blp.route("/item/<string:item_id>")
class ItemList(MethodView):
    def get(self,item_id):
        try:
            if items[item_id] in items:
                return items[item_id]
        except KeyError:
            return {"message":"item not found."}, 404
    
    def delete(self,item_id):
        try:
            if items[item_id] in items:
                del items[item_id]
                return {"message":"item deleted"}
        except KeyError:
            return {"message":"item not found."}, 404 
        
    def put(self,item_id):
        item_data = request.get_json()
        if "name" not in item_data or "price" not in item_data:
            abort(400,message="Bad request. Ensure 'price' and 'name' are included in the JSON payload.")

        try:
            item = items[item_id]
            item |= item_data
            return item , 200
        except KeyError:
            abort(400,message="Item not found")

    