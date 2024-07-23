from flask import Flask, render_template, request, render_template_string, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sistem_integration"
)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vulnerable SQL query
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor = db.cursor()
        cursor.execute(query)
        user = cursor.fetchone()
        
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "Invalid credentials. <a href='/'>Try again</a>"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        action = request.form['action']
        if action == 'Encrypt':
            result = render_template_string(message)
        else:
            result = render_template_string(message)
        return render_template('index.html', result=result, message=message, action=action)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


