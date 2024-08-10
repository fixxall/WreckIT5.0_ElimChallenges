from Crypto.Util.number import *
import math

def read_values_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Variabel untuk menyimpan nilai n, e, c
    n = None
    e = None
    c = None
    
    for line in lines:
        # Hapus whitespace ekstra
        line = line.strip()
        if line.startswith('n ='):
            n = int(line.split('=')[1].strip())
        elif line.startswith('e ='):
            e = int(line.split('=')[1].strip())
        elif line.startswith('c ='):
            c = int(line.split('=')[1].strip())
    
    # Pastikan nilai n, e, c diambil dengan benar
    if n is None or e is None or c is None:
        raise ValueError("Tidak semua nilai (n, e, c) ditemukan dalam file.")
    
    return n, e, c

n,e,c = read_values_from_file('hasil.txt')
X = 3^1024
M = matrix(ZZ,[[1,0,0,0,4*X^4],[0,1,0,0,4*X^3],[0,0,1,0,4*X^2],[0,0,0,1,4*X^1],[0,0,0,0,-4*n]])
for eq in M.LLL():
	x = PolynomialRing(ZZ, 'x').gen()
	pol = eq[0]*x^4+eq[1]*x^3+eq[2]*x^2+eq[3]*x+(eq[4]//-4)
	if '(' in str(pol.factor()) and '^4' not in str(pol.factor()):
		lop=pol.factor()
u2,u1,u0 = list(lop[0][0])[2],list(lop[0][0])[1],list(lop[0][0])[0]
v2,v1,v0 = list(lop[1][0])[2],list(lop[1][0])[1],list(lop[1][0])[0]


ap = (X^2)*u2+(X^1)*u1+u0
bq = (X^2)*v2+(X^1)*v1+v0
p=math.gcd(ap,n)
q=math.gcd(bq,n)
tot = (p-1)*(q-1)
e = 65537
d = pow(e,-1,tot)
print(long_to_bytes(pow(int(c),int(d),int(p*q))))