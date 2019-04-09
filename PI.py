from decimal import *
getcontext().prec = 998

PI = ""
pi = 0

n = 6
nlen = 1

for i in range(1000):
    a = Decimal(Decimal(Decimal(1)**Decimal(2) - (Decimal(Decimal(nlen) / Decimal(2))**Decimal(2)))).sqrt()
    b = Decimal(1) - Decimal(a)
    Umkreis = Decimal(n) * Decimal(nlen)
    pi = Decimal(Umkreis) / Decimal(2)
    PI = str(Decimal(pi))
    nlen = Decimal((Decimal(nlen)/Decimal(2))**Decimal(2) + Decimal(b)**Decimal(2)).sqrt()
    n = Decimal(n) * Decimal(2)

print(PI)
