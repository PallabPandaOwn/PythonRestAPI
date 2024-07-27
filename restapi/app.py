from flask import Flask , request
from db import stores,items
import uuid
from flask_smorest import abort

app = Flask(__name__)


# Endpoint to all get stores
@app.get('/store')  
def get_all_store():
    return {"stores": list(stores.values())}


# Endpoint to create store with id
@app.post("/store") 
def insert_store():
    store_data = request.get_json()
    if "storename" not in store_data :
        abort(404,message="please give all details.")

    store_id = uuid.uuid4().hex # generate unique id 
    store = {**store_data,"id":store_id}
    stores[store_id]=store
    return store, 201 # 201 -: Accepted request

# Endpoint to create item in store
@app.post("/item") 
def insert_item():
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

# Endpoint to get all items
@app.get("/item")
def get_all_item():
    return {"items": list(items.values())},200

# Endpoint to search a store by id
@app.get("/store/<string:store_id>") 
def get_store_by_id(store_id):
    try:
        return stores[store_id],200
    except KeyError:
        # return {"message":"store not found."}, 404
        abort(404,message="store not found.")

# Endpoint to get item by id
@app.get("/item/<string:item_id>") 
def get_item_by_id(item_id):
    try:
        if items[item_id] in items:
            return items[item_id]
    except KeyError:
        return {"message":"item not found."}, 404    
    

# Endpoint to delete item by id
@app.delete("/item/<string:item_id>") 
def delete_item_by_id(item_id):
    try:
        if items[item_id] in items:
            del items[item_id]
            return {"message":"item deleted"}
    except KeyError:
        return {"message":"item not found."}, 404 
    
# Endpoint for update item by item id 
@app.put("/item/<string:item_id>")
def update_item_by_id(item_id):
    item_data = request.json()
    if "name" not in item_data or "price" not in item_data:
        abort(400,message="Bad request. Ensure 'price' and 'name' are included in the JSON payload.")

    try:
        item = items[item_id]
        item |= item_data
        return item
    except KeyError:
        abort(400,message="Item not found")
    