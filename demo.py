# Any copyright is dedicated to the Public Domain.
# https://creativecommons.org/publicdomain/zero/1.0/

from random import randint
from time import time

from rularev import trans_to, trans_from, silly_trans_to, silly_trans_from

fTo   = silly_trans_to
fFrom = silly_trans_from

fTo   = trans_to
fFrom = trans_from

for el in [
    "Экс-граф? Плюш изъят. Бьём чуждый цен хвощ!"
    ,"Съешь ещё этих мягких французских булок, да выпей же чаю."
    ,"Шалящий фавн прикинул объём горячих звезд этих вьюжных царств."
    ,"Эх, взъярюсь, толкну флегматика: \"Дал бы щец жарчайших, Пётр!\""
    ,"Пиши: зять съел яйцо, ещё чан брюквы... эх! Ждем фигу!"
    ,"В чащах юга жил-был цитрус... — да, но фальшивый экземпляр!"
    ]:

    a = ''
    for symb in el:
        if randint(0, 1) == 0:
            a = a + symb.lower()
        else:
            a = a + symb.upper()

    print('исходный :', a)
    a = fTo(a)
    print('транслит :', a)
    b = fFrom(a)
    print('восстановлено :', b)
    b = ''
    for symb in a:
        if randint(0, 1) == 0:
            b = b + symb.lower()
        else:
            b = b + symb.upper()
    print('перемешано: ', b)
    b = fFrom(b)
    print('восстановлено: ', b)
    print()

    #break

print(time())
for i in range(100000):
#for i in range(1):
    b = fTo(b)    
    b = fFrom(b)
print(time())

a = ''
print(time())
for i in range(100000):
#for i in range(1):
    a = a + b
a = fTo(a)    
a = fFrom(a)
print(time())

True
