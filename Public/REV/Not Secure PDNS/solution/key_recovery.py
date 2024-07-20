from pwn import *
from Crypto.Util.number import *
from sage.rings.factorint import factor_trial_division
from sympy.ntheory.modular import crt 
import time
from math import gcd
import requests

url = 'http://localhost:8080/encrypt'

hasil = []
for coun in range(50):
    try:
        def sendMessage(arr_x):
            sendata = b''
            for i in arr_x:
                sendata+=i.encode()+b'\n'
            sendata = sendata[:-1]
            filedata = {'file': sendata}
            resp = requests.post(url, files=filedata)
            result = []
            for i in resp.content.split(b'--START--')[1:]:
                respdata = i.split(b'--END--\n')[0]
                result.append(int(respdata.decode(),16))
            return result

        init_message = "plays"
        arrInp = [init_message]

        init_message = bytes_to_long(init_message.encode())
        for x in range(35, 40):
            arrInp+=['x:'+str(x)]

        out_ret= sendMessage(arrInp)
        print("Getting out_ret")
        initiation = out_ret[0]

        test = []
        for x in range(35, 40):
            plain = bytes_to_long(b'x:'+str(x).encode())
            mess = pow(plain,x)
            assert mess.bit_length() > 1024
            test.append([plain, mess, out_ret[x-34]])

        p = test[0][1]-test[0][2]
        for i in test[1:]:
            p = gcd(i[1]-i[2], p)
        assert isPrime(p)
        limitNum = 100000
        fact = factor_trial_division(p-1, limitNum)

        def solvePoligh(arr, pr):
            res = []
            for i in arr:
                for j in range(1, i[2]):
                    if(pow(i[1], j, pr)==pow(i[0], 1, pr)):
                        res.append([j, i[2]])
                        break
            return res
        
        # format list for poligh solve
        # [(g, h, pe)]
        lp = []
        count = [init_message, initiation]
        for i,j in fact:
            if pow(i,j)<limitNum:
                pe = pow(i, j)
                g = pow(count[1],((p-1)//pe), p)
                h = pow(count[0],((p-1)//pe), p)
                if(g==1 or h==1): break
                lp.append([g,h,pe])

        result = solvePoligh(lp, p)
        hasil += result
        # print(count,":",result)
        # io.close()
    except Exception as error:
        print("An error occurred:", error)

m = []
v = []
for i,j in hasil:
    m.append(i)
    v.append(j)

crt_m = crt(v,m)
print(crt_m[0])


