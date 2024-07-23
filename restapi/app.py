from flask import Flask , request
from db import stores,items
import uuid
from flask_smorest import abort


app = Flask(__name__)

# stores = [
#     {
#         "storename": "mystore1",
#         "items": 
#         [
#             {
#                 'name': 'chair', 'price': 100
#             },
#             {
#                 'name': 'table', 'price': 500
#             }
#         ]
#     },
#     {
#         "storename": "mystore2",
#         "items": 
#         [
#             {
#                 'name': 'chair', 'price': 200
#             },
#             {
#                 'name': 'table', 'price': 400
#             }
#         ]
#     }
# ]

# endpoint to all get stores
@app.get('/store')  
def get_all_store():
    return {"stores": list(stores.values())}


# endpoint to create store with id
@app.post("/store") 
def insert_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex # generate unique id 
    store = {**store_data,"id":store_id}
    stores[store_id]=store
    return store, 201 # 201 -: Accepted request


@app.post("/item") # endpoint to create item in store
def insert_item():
    item_data = request.get_json()
    # if item_data["store_id"] not in items or:
    #     abort(404,message="store not found.")

    if item_data["store_id"] not in stores:
        return {"message": "store not found."},404
    
    item_id = uuid.uuid4().hex
    item = {**item_data,"id":item_id}
    items[item_id]=item
    return {"item": item},201

# endpoint to get all items
@app.get("/item")
def get_all_item():
    return {"items": list(items.values())},200

# endpoint to search a store by id
@app.get("/store/<string:store_id>") 
def get_store_by_id(store_id):
    try:
        return stores[store_id],200
    except KeyError:
        # return {"message":"store not found."}, 404
        abort(404,message="store not found.")

# endpoint to get item by id
@app.get("/item/<string:item_id>") 
def get_item_by_id(item_id):
    try:
        if items[item_id] in items:
            return items[item_id]
    except KeyError:
        return {"message":"item not found."}, 404    