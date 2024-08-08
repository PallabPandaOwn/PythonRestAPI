from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.0"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)  # register flask app

api.register_blueprint(ItemBlueprint) # register blueprint of items
api.register_blueprint(StoreBlueprint) # register blueprint of store





# ### STORE API

# # Endpoint to all get stores

# @app.get('/store')  
# def get_all_store():
#     return {"stores": list(stores.values())}


# # Endpoint to insert new store

# @app.post("/store") 
# def insert_store():
#     store_data = request.get_json()
#     if "storename" not in store_data :
#         abort(404,message="please provide storename.")

#     store_id = uuid.uuid4().hex # generate unique id 
#     store = {**store_data,"id":store_id}
#     stores[store_id]=store
#     return store, 201 # 201 -: Accepted request


# # Endpoint to a store by id

# @app.get("/store/<string:store_id>") 
# def get_store_by_id(store_id):
#     try:
#         return stores[store_id],200
#     except KeyError:
#         abort(404,message="store not found.")

# # Endpoint delete a store by id

# @app.delete("/store/<string:store_id>") 
# def delete_store_by_id(store_id):
#     try:
#         del stores[store_id]
#         return stores,200
#     except KeyError:
#         abort(404,message="store not found.")

# # Endpoints to update a store

# @app.put("/store/<string:store_id>") 
# def update_store_by_id(store_id):
#     store_data = request.get_json()
#     if "storename" not in store_data:
#         abort(400,message="Bad request. Ensure 'storename' are included in the JSON payload.")
#     try:
#         store =  stores[store_id]
#         store |= store_data
#         return store , 200
#     except KeyError:
#         abort(404,message="store not found.")


# ### ITEMS API ###

# # Endpoint to get all items

# @app.get("/item")
# def get_all_item():
#     return {"items": list(items.values())},200


# # Endpoint to get item by id

# @app.get("/item/<string:item_id>") 
# def get_item_by_id(item_id):
#     try:
#         if items[item_id] in items:
#             return items[item_id]
#     except KeyError:
#         return {"message":"item not found."}, 404    
    
    

# # Endpoint to insert item in store

# @app.post("/item") 
# def insert_item():
#     item_data = request.get_json()
#     if ("price" not in item_data
#         or "store_id" not in item_data
#         or "name" not in item_data
#     ):
#         abort(400,message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.")

#     for item in items.values:
#         if  item_data["name"]==item["name"] and item_data["store_id"]:
#             abort(400,message="Item name and Store id  exists")

#     if item_data["store_id"] not in stores:
#         return {"message": "store not found."},404
    
#     item_id = uuid.uuid4().hex
#     item = {**item_data,"id":item_id}
#     items[item_id]=item
#     return {"item": item},201


# # Endpoint to delete item by id

# @app.delete("/item/<string:item_id>") 
# def delete_item_by_id(item_id):
#     try:
#         if items[item_id] in items:
#             del items[item_id]
#             return {"message":"item deleted"}
#     except KeyError:
#         return {"message":"item not found."}, 404 
    
# # Endpoint for update item by item id 

# @app.put("/item/<string:item_id>")
# def update_item_by_id(item_id):
#     item_data = request.get_json()
#     if "name" not in item_data or "price" not in item_data:
#         abort(400,message="Bad request. Ensure 'price' and 'name' are included in the JSON payload.")

#     try:
#         item = items[item_id]
#         item |= item_data
#         return item , 200
#     except KeyError:
#         abort(400,message="Item not found")
    