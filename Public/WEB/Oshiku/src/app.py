from flask import Flask, render_template, request
import sqlite3
import subprocess

app = Flask(__name__)

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



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_name = request.form.get("oshi_name")
        biography = query_database(selected_name)
        return render_template("index.html", biography=biography)
    return render_template("index.html", biography="")

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')