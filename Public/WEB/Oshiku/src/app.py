from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
jwt = JWTManager(app)

# Database connection
DATABASE = "database.db"
def query_database(name):
    query = 'sqlite3 database.db "SELECT biography FROM oshi WHERE name=\'' + str(name) +'\'\"'
    command = ['sqlite3', 'database.db', query]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return f"Error: {result.stderr.strip()}"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "guest" and password == "guest":
            role = "guest"
        else:
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity={"username": username, "role": role})
        return jsonify(access_token=access_token), 200

    return render_template("login.html")

@app.route("/index", methods=["GET", "POST"])
@jwt_required()
def index():
    claims = get_jwt_identity()

    if claims["role"] != "admin":
        return jsonify({"msg": "Access forbidden: Admins only"}), 403

    if request.method == "POST":
        selected_name = request.form.get("oshi_name")
        biography = query_database(selected_name)
        return render_template("index.html", biography=biography)
    return render_template("index.html", biography="")

@app.route("/guest", methods=["GET", "POST"])
@jwt_required()
def guest():
    claims = get_jwt_identity()

    if claims["role"] != "guest":
        return jsonify({"msg": "Access forbidden: Guests only"}), 403

    return render_template("guest.html")

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
