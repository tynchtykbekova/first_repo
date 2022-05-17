import sys
from m import base
import random

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# ls = []
# for i in range(4):
#     l = random.choice(names)
#     ls.append(l)

# print(ls)

# print(sys.platform)
# random.shuffle(l)
# print(l)
# print('hello {}'.format(sys.argv[1]))
il=['hello.py', 'bye.py','time.py', 'm.html', 'olaf.py']
for i in range(5):
f=random.choice(il)
il.remove(f)
open(f'/home/user/python_lessons')