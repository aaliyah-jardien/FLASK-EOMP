import hmac
import sqlite3
import datetime

from flask import Flask, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


# CREATES TABLE
def init_user_table():
    conn = sqlite3.connect('aj_store.db')
    print("Opened database successfully")

    conn.execute("CREATE TABLE IF NOT EXISTS user(user_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "first_name TEXT NOT NULL,"
                 "last_name TEXT NOT NULL,"
                 "username TEXT NOT NULL,"
                 "email TEXT NOT NULL UNIQUE,"
                 "phone TEXT NOT NULL UNIQUE,"
                 "password TEXT NOT NULL)")
    print("user table created successfully")
    conn.close()


init_user_table()


def init_item_table():
    with sqlite3.connect('aj_store.db') as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "item_name TEXT NOT NULL,"
                     "description TEXT NOT NULL,"
                     "item_price TEXT NOT NULL,"
                     "item_barcode TEXT NOT NULL)")
    print("blog table created successfully.")


def fetch_users():
    with sqlite3.connect('aj_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        users = cursor.fetchall()

        new_data = []

        for data in users:
            new_data.append(User(data[0], data[1], data[4]))
    return new_data


users = fetch_users()


init_user_table()
init_item_table()

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and hmac.compare_digest(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)


@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity


@app.route('/user-registration/', methods=["POST"])
def user_registration():
    response = {}

    if request.method == "POST":

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        with sqlite3.connect("aj_store.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user("
                           "first_name,"
                           "last_name,"
                           "username,"
                           "email,"
                           "phone,"                   
                           "password) VALUES(?, ?, ?, ?, ?, ?)", (first_name, last_name, username, email, phone, password))
            conn.commit()
            response["message"] = "success"
            response["status_code"] = 201
        return response


@app.route('/create-blog/', methods=["POST"])
def create_blog():
    response = {}

    if request.method == "POST":

        item_name = request.form['item_name']
        description = request.form['description']
        item_price = request.form['item_price']
        item_barcode = request.form['item_barcode']

        with sqlite3.connect('aj_store.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO item("
                           "item_name,"
                           "description,"
                           "item_price,"
                           "item_barcode) VALUES(?, ?, ?, ?)", (item_name, description, item_price, item_barcode))
            conn.commit()
            response["status_code"] = 201
            response['description'] = "Blog post added successfully"
        return response


@app.route('/get-blogs/', methods=["GET"])
def get_blogs():
    response = {}
    with sqlite3.connect("aj_store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM item")

        posts = cursor.fetchall()

    response['status_code'] = 200
    response['data'] = posts
    return response


@app.route("/delete-post/<int:post_id>")
def delete_post(post_id):
    response = {}
    with sqlite3.connect("aj_store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM item WHERE id=" + str(post_id))
        conn.commit()
        response['status_code'] = 200
        response['message'] = "blog post deleted successfully."
    return response


@app.route('/edit-post/<int:post_id>/', methods=["PUT"])
@jwt_required()
def edit_post(post_id):
    response = {}

    if request.method == "PUT":
        with sqlite3.connect('aj_store.db') as conn:
            incoming_data = dict(request.json)
            put_data = {}

            if incoming_data.get("") is not None:
                put_data["item_name"] = incoming_data.get("item_name")
                with sqlite3.connect('aj_store.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE item SET item_name =? WHERE id=?", (put_data["item_name"], post_id))
                    conn.commit()
                    response['message'] = "Update was successfully"
                    response['status_code'] = 200

            if incoming_data.get("description") is not None:
                put_data['description'] = incoming_data.get('description')

                with sqlite3.connect('aj_store.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE item SET description =? WHERE id=?", (put_data["description"], post_id))
                    conn.commit()

                    response["description"] = "Content updated successfully"
                    response["status_code"] = 200

            if incoming_data.get("item_price") is not None:
                put_data['item_price'] = incoming_data.get('item_price')

                with sqlite3.connect('aj_store.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE item SET item_price =? WHERE id=?", (put_data["item_price"], post_id))
                    conn.commit()

                    response["item_price"] = "Content updated successfully"
                    response["status_code"] = 200

            if incoming_data.get("item_barcode") is not None:
                put_data['item_barcode'] = incoming_data.get('item_barcode')

                with sqlite3.connect('aj_store.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE item SET item_price =? WHERE id=?", (put_data["item_barcode"], post_id))
                    conn.commit()

                    response["item_barcodes"] = "Content updated successfully"
                    response["status_code"] = 200
    return response


@app.route('/get-post/<int:post_id>/', methods=["GET"])
def get_post(post_id):
    response = {}

    with sqlite3.connect("aj_store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM post WHERE id=" + str(post_id))

        response["status_code"] = 200
        response["description"] = "Blog post retrieved successfully"
        response["data"] = cursor.fetchone()

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

