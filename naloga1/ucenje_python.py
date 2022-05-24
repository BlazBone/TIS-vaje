from typing import Counter


seznam = [1, 2, 3, "biba", False, True]
print(seznam[1])
print(seznam[-1])
print(seznam[1:4])
print(seznam[-1:])
print(seznam[::2])

seznam.append('500')
print(seznam)
seznam.insert(1, [1, 2, 3])
print(seznam)
a = Counter("seznam")
print(a)

# lahko castamo
a = (1, 2, 3)  # terka
b = list(a)

c = tuple(b)

print('a' + 12*"BIBA")

# map
something = {'biba': 12, 'a': 4, "nevem": "karkoli je lahko tukaj"}

for k, v in something.items():
    print("kljuc", k, "vrednost:", v)

# set isto ko array samo da so {}
a = {1, 2, 1, 2, 3, 4, 5, 1, 2, 3, 5, 3, 2}
print(a)
