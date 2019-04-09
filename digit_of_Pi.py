from decimal import *
getcontext().prec = 999

run = 1
while run:
    digit = int(input("Which digit of Pi you want to know? "))
    if digit <= 999:
        run = 0
    elif digit > 999:
        print("Only the digit up to 999")

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

PI = PI.replace(".", "")
print(PI[digit - 1])
