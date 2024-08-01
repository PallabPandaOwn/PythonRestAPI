from flask import request
from flask.views import MethodView
from flask.smorest import Blueprint,abort
from db import stores
import uuid


blp = Blueprint("stores",__name__ ,description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    
    def get(self,store_id):
        try:
            return stores[store_id],200
        except KeyError:
            abort(404,message="store not found.")

    def delete(self,store_id):
        try:
            del stores[store_id]
            return stores,200
        except KeyError:
            abort(404,message="store not found.")

@blp.route("/store")
class StoreList(MethodView):

    def get(self):
        return {"stores": list(stores.values())}
    

    def post(self):
        store_data = request.get_json()
        if "storename" not in store_data :
            abort(404,message="please provide storename.")

        store_id = uuid.uuid4().hex # generate unique id 
        store = {**store_data,"id":store_id}
        stores[store_id]=store
        return store, 201 # 201 -: Accepted request







        
        