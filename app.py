# FLASK IMPORTS
import hmac
import sqlite3
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_cors import CORS

from flask import Flask, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity

# USER NAME AND PASSWORD IN CLASS
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


# CREATES TABLE
def init_user_table():
    conn = sqlite3.connect('aj_store.db')
    print("Opened database successfully")

    conn.execute("CREATE TABLE IF NOT EXISTS user1(user_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "first_name TEXT NOT NULL,"
                 "last_name TEXT NOT NULL,"
                 "username TEXT NOT NULL,"
                 "email TEXT NOT NULL,"
                 "phone TEXT NOT NULL,"
                 "password TEXT NOT NULL)")
    print("user table created successfully")
    conn.close()


init_user_table()


def init_product_table():
    with sqlite3.connect('aj_store.db') as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "product_name TEXT NOT NULL,"
                     "description TEXT NOT NULL,"
                     "product_price TEXT NOT NULL,"
                     "product_barcode TEXT NOT NULL)")
    print("item table created successfully.")


def fetch_users():
    with sqlite3.connect('aj_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user1")
        users = cursor.fetchall()

        new_data = []

        for data in users:
            new_data.append(User(data[0], data[3], data[6]))
    return new_data


users = fetch_users()


init_product_table()

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


# AUTHENTICATION & IDENTITY
def authenticate(username, password):
    user = username_table.get(username, None)
    if user and hmac.compare_digest(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


# CREATING APP
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aaliyahjardien4@gmail.com'
app.config['MAIL_PASSWORD'] = 'icecream2002%'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

jwt = JWT(app, authenticate, identity)


@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

# ROUTE FOR EDIT PRODUCTS IN DATABASE
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
            cursor.execute("INSERT INTO user1("
                           "first_name,"
                           "last_name,"
                           "username,"
                           "email,"
                           "phone,"
                           "password) VALUES(?, ?, ?, ?, ?, ?)", (first_name, last_name, username, email, phone, password))
            conn.commit()
            msg = Message('Hello Message', sender='aaliyahjardien4@gmail.com', recipients=[email])
            msg.body = "Thanks for shopping at my business."
            mail.send(msg)
            response["message"] = "success"
            response["status_code"] = 201
        return response

# ROUTE FOR CREATING PRODUCTS IN DATABASE
@app.route('/create-product/', methods=["POST"])
def create_product():
    response = {}

    if request.method == "POST":

        product_name = request.form['product_name']
        description = request.form['description']
        product_price = request.form['product_price']
        product_barcode = request.form['product_barcode']

        with sqlite3.connect('aj_store.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO item("
                           "product_name,"
                           "description,"
                           "product_price,"
                           "product_barcode) VALUES(?, ?, ?, ?)", (product_name, description, product_price, product_barcode))
            conn.commit()
            response["status_code"] = 201
            response['description'] = "Blog post added successfully"
        return response

# ROUTE FOR GETTING PRODUCTS IN DATABASE
@app.route('/get-product/', methods=["GET"])
def get_product():
    response = {}
    with sqlite3.connect("aj_store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM item")

        posts = cursor.fetchall()

    response['status_code'] = 200
    response['data'] = posts
    return response

# ROUTE FOR DELETING PRODUCTS IN DATABASE
@app.route("/delete-product/<int:post_id>")
def delete_product(post_id):
    response = {}
    with sqlite3.connect("aj_store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM item WHERE id=" + str(post_id))
        conn.commit()
        response['status_code'] = 200
        response['message'] = "product post deleted successfully."
    return response

# ROUTE FOR EDIT PRODUCTS IN DATABASE
@app.route('/edit-post/<int:post_id>/', methods=["PUT"])
@jwt_required()
def edit_product(post_id):
    response = {}

    if request.method == "PUT":
        with sqlite3.connect('aj_store.db') as conn:
            incoming_data = dict(request.json)
            put_data = {}

            if incoming_data.get("") is not None:
                put_data["product_name"] = incoming_data.get("product_name")
                with sqlite3.connect('aj_store.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE item SET product_name =? WHERE id=?", (put_data["product_name"], post_id))
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

            if incoming_data.get("product_price") is not None:
                put_data['product_price'] = incoming_data.get('product_price')

                with sqlite3.connect('aj_store.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE item SET product_price =? WHERE id=?", (put_data["product_price"], post_id))
                    conn.commit()

                    response["product_price"] = "Content updated successfully"
                    response["status_code"] = 200

            if incoming_data.get("item_barcode") is not None:
                put_data['product_barcode'] = incoming_data.get('product_barcode')

                with sqlite3.connect('aj_store.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE item SET item_price =? WHERE id=?", (put_data["product_barcode"], post_id))
                    conn.commit()

                    response["product_barcodes"] = "Content updated successfully"
                    response["status_code"] = 200
    return response

# ROUTE FOR VIEWING PRODUCTS IN DATABASE
@app.route('/view-product/<int:post_id>/', methods=["GET"])
def view_product(post_id):
    response = {}

    with sqlite3.connect("aj_store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM item WHERE id=" + str(post_id))

        response["status_code"] = 200
        response["description"] = "Product retrieved successfully"
        response["data"] = cursor.fetchone()

    return jsonify(response)


# RUNNING APP
if __name__ == '__main__':
    app.run(debug=True)

