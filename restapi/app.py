from flask import Flask
from flask import request


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


@app.get('/store')  # endpoint
def get_store():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"storename": request_data["storename"], "items": []}
    stores.append(new_store)
    return new_store, 201 # 201 -: Accepted request


@app.post("/store/<string:storename>/item")
def create_item(storename):
    request_date = request.get_json()
    for store in stores:
        if store["storename"] == storename:
            new_item = {"name": request_date["name"], "price": request_date["price"]}
            store["items"].append(new_item)
            return new_item , 201
    return "Store not found", 404