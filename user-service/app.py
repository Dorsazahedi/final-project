from flask import Flask, request, jsonify
<<<<<<< HEAD
import logging
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

=======
from flask_sqlalchemy import SQLAlchemy
import logging
>>>>>>> f44566b (Final project updates: added order-service, fixed DB, updated README, security)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

logging.basicConfig(filename='log.txt', level=logging.INFO)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 409
<<<<<<< HEAD
    users[username] = password
    logging.info(f"User {username} registered")
    return jsonify({"message": f"User {username} registered successfully! Congratulations!"}), 201
=======
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    logging.info(f"User registered successfully - username: {username}")
    return jsonify({"message": f"User {username} registered successfully!"}), 201
>>>>>>> f44566b (Final project updates: added order-service, fixed DB, updated README, security)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return jsonify({"message": f"Welcome back, {username}!"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"username": user.username}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
