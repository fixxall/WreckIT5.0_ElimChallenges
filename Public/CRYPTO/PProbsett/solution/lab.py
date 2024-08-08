from sage.all import *
import random

# p = random_prime(2**10)
# message = random.randint(0,p)
# print('p:',p)
# print('message:',message)
# R = GF(p)['x']

# p1 = R.irreducible_element(Integer(5), algorithm="random")
# q1 = R.irreducible_element(Integer(7), algorithm="random")

# print(p1.degree())
# print(q1)
# n = p1*q1

# print(n)
# teta = (p**5-1)*(p**7-1)
# print('teta:',teta)
# e = random.randint(0,teta)
# # e = 2
# while gcd(e, teta) != 1:
#     e+= 1
# d = pow(e, -1, teta)
# mess = R('x + '+str(message))
# print('mess:',mess[0])
# print('e:',e)
# print('d:',d)
# temp = pow(mess, e, n)
# print(temp)
# retu = pow(temp, d, n)
# print(retu)

# SOLVED Theorema 1

# p = random_prime(2**512)
# k = random.randint(0,p)
# print('k:',k)

# rep = 60

# Zn = Zmod(p)
# t = [random.getrandbits(512) for _ in range(rep)]
# a = [-(random.getrandbits(500)+k*t[_]+random.getrandbits(256)*888)%p for _ in range(rep)]
# B = 2**500
# m = [[0]*i+[p]+[0]*(rep-1-i)+[0,0] for i in range(rep)]
# m += [t+[B/p,0]]
# m += [a+[0,B]]
# Mat = matrix(m)
# lll = Mat.LLL()
# for row in lll:
#     if row[-1] == B:
#         print(Zn(row[-2]*p/B))
#         break
# SOLVED Theorema 2


