FLAG = b'WRECKIT50{##secret##!-----___-------******()^_^()******-------___-----!##sharing##}'

def tets(k, p, p1, q1, n):
    set1 = p1.degree()
    set2 = q1.degree()
    teta = (p**set1-1)*(p**set2-1)
    return teta