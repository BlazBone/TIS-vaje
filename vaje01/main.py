from tkinter import N
from numpy import true_divide


a = 12
a += 5
print('biba')
print(a)
print(type(a))
# int nima omejitve oziroma je omejen z pomnilnikom
# float je ubistvu double in je omejen na 64 bitov
# complex numbers
c = 2 + 3j
c.real
c.imag

nic = None  # isto ku null
t = True
f = False  # tip bool

s0 = 'biba leskava'
s0 = "biba leskav"
s1 = 'biba "something" se neki'
s3 = ''' tle pa lahko kar cmo " ' " """ '' '''
print(s1, s3, s0)


x = z = y = 9
print(x, z, y)
a, b, c = 1, 2 + 3j, "something"  # terka tuple
a, b = b, a

print(a, b)

# Razpakiranje zaporedji
ena, dva, tri = "TIS"
print(ena, dva, tri)
prvi, *ostali = "beseda"
*ostali2, zadnji = "beseda"
print(prvi, ostali)
# lahko odpremo konzolo in pole imamo tm interaktivno s spremeljivkami naprimer napisemo del in ime spremenljivke d jo zbrise


print(int("789432"))
print(int(False))
print(int(True))
bool(0)  # prazne terke mnozice stringi stevilo 0 use je false None.....
int("123", 4)  # lahko v base 4
float("22e4")  # 22 * 10^4

# llogicni operatorji not, and, or, xor,
l2 = 'python' or 'matlab'  # ti da prvo ker ko vidi or nerabi gledt
# vrne dobesedno vrednost izraza ne vrne samo logicne valda lohko pole transferas
l3 = 'python' and 'matlab'  # pa vrne matlab isto ko prej smo da gleda do konca
print("python" and "")

# primerjanja
# ==, !=, <=, >=, >, <
# nizanje pogojev
5 < b < 15

# aritmeticni operatorji
# +
# -
# / deljenje float 3/2 1.5
# // celostevlisko deljenje 3/2 1
# %
# abs()
# -n negacija
# ** potenca lahko tudi funkcija pow()

# nema i++ lahko samo i+=1

# bitne operacije
# | ali
# & in
# ^ xor
# ~ negacija
5 | 3  # 7
~5  # -6
5 << 3  # bit shift

# stavek if
if "condition":
    print("hej")
    # do something
elif "another condition":
    print('elif')
    # do something else
else:
    print("else")
    # no shit

# terniry operator
# ? __:__
x = 22 if 23 > 89 else print("WATAFAK")

for crka in "ALJAZ IN LEON":
    print(crka)
# print(type(range(5)))
for i, crka in enumerate("ALJAZ IN LEON"):
    print(i, crka)

range(1, 5)  # 1,2,3,4 ni zadnje cifre
