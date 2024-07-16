from flask import Flask , request


app = Flask(__name__)

stores = [
    {
        "storename": "mystore1",
        "items": 
        [
            {
                'name': 'chair', 'price': 100
            },
            {
                'name': 'table', 'price': 500
            }
        ]
    },
    {
        "storename": "mystore2",
        "items": 
        [
            {
                'name': 'chair', 'price': 200
            },
            {
                'name': 'table', 'price': 400
            }
        ]
    }
]


@app.get('/store')  # endpoint to get store
def get_store():
    return {"stores": stores}


@app.post("/store") # endpoint to create store
def create_store():
    request_data = request.get_json()
    new_store = {"storename": request_data["storename"], "items": []}
    stores.append(new_store)
    return new_store, 201 # 201 -: Accepted request


@app.post("/store/<string:storename>/item") # endpoint to create item in store
def create_item(storename):
    request_date = request.get_json()
    for store in stores:
        if store["storename"] == storename:
            new_item = {"name": request_date["name"], "price": request_date["price"]}
            store["items"].append(new_item)
            return new_item , 201
    return "Store not found", 404

@app.get("/store/<string:storename>") # endpoint to search a store
def search_store(storename):
    for store in stores:
        if store["storename"] == storename:
            return {"message":"store found."} , 200
        
    return {"message":"store not found."}, 404

@app.get("/store/<string:storename>/item") # endpoint to get all item in a store
def search_item_in_store(storename):
    for store in stores:
        if store["storename"] == storename:
            return {"items":store["items"]} , 200
        
    return {"message":"store not found."}, 404    