from flask import Flask, request, jsonify, send_file
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import os
from io import BytesIO

app = Flask(__name__)

# Initialize the encryption parameters
env_key = ('a' * 16).encode()
x = bytes_to_long(env_key)
p = getPrime(1024)

@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_bytes = file.read()
    if(file_bytes.split(":")[0].strip()=='x'): x=int(file_bytes.split(":")[1].strip())
    enc_message = long_to_bytes(pow(bytes_to_long(file_bytes.encode()), x, p))

    # Use BytesIO to send the encrypted file
    output = BytesIO(enc_message_bytes)
    output.seek(0)

    return send_file(output, as_attachment=True, download_name='enc', mimetype='application/octet-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
