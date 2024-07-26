from flask import Flask, render_template, request, render_template_string, redirect, url_for, session
import mysql.connector
from Crypto.Cipher import AES
import string
import random
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
das = string.ascii_letters + string.digits

app.secret_key = os.getenv("APP_SECRET_KEY")
aes_key = os.getenv("AES_KEY").encode()
aes_iv = os.getenv("AES_IV").encode()
seed = os.getenv("SEED").encode()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

def filtering(mess):
    for i in mess:
        if(i not in das):
            return False
    return True

def filteringLevel2(mess):
    blacklist = ["flask", "mysql", "Crypto", "string", "random", "def", "commands", "subprocess", "sys", "pty", "imp", "exec", "dict", "request", "config", ".", "class", "name", "built", "module", "item", "os", "open", "read", "flag"]
    for i in blacklist:
        if i in mess:
            return False
    return True

def xor(a, b):
    return b''.join([int.to_bytes(i^j, 1, byteorder="big") for i,j in zip(a, b)])

def pad(message, x):
    return message+b'\x00'*(x-(len(message)%x))

def unpad(message, x):
    return message.rstrip(b'\x00')

def SecureFunctionEncrypt(plaintext):
    pt = pad(plaintext, 16)
    cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
    ciphertext = cipher.encrypt(pt)
    rand = random.Random()
    rand.seed(int.from_bytes(seed, byteorder="big"))
    ciphertext = xor(rand.randbytes(len(ciphertext)), ciphertext)
    return ciphertext.hex()

def SecureFunctionDecrypt(ciphertext):
    ct = bytes.fromhex(ciphertext)
    rand = random.Random()
    rand.seed(int.from_bytes(seed, byteorder="big"))
    ct = xor(rand.randbytes(len(ct)), ct)
    cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
    plaintext = unpad(cipher.decrypt(ct),16)
    return str(plaintext)[2:-1]

@app.route('/', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
            cursor = db.cursor()
            cursor.execute(query)
            user = cursor.fetchone()
            
            cursor.fetchall() 
            if user:
                session['username'] = username
                return redirect(url_for('index'))
            else:
                error_message = "Invalid credentials."
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor is not None:
                cursor.close() 
    return render_template('login.html', error_message=error_message)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/home', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        message = request.form['message']
        action = request.form['action']
        if(not filtering(message)):
            result = "Prohibited using injection LLzz"+str(filtering(message))
        elif action == 'Encrypt':
            ciphertext = SecureFunctionEncrypt(message.encode())
            fdata = filteringLevel2(ciphertext)
            try:
                if(fdata): result = render_template_string(ciphertext)
                else: result = "Prohibited using injection LLzz"
            except: 
                result = ciphertext
        else:
            plaintext = SecureFunctionDecrypt(message)
            try:
                fdata = filteringLevel2(plaintext) | True
                if(fdata): result = render_template_string(plaintext)
                else: result = "Prohibited using injection LLzz"
            except: 
                result = plaintext
        return render_template('index.html', result=result, message=message, action=action)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port="5000",host="0.0.0.0")


