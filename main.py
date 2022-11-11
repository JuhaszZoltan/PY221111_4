from module import *

sorozat:list[int] = [7, 9, 3, 2, 1, 4, 8]

print('for:  ', end=' ')
for n in sorozat:
    if n%2 == 0:
        print('van benne páros szám')
        break
else: print('nincs benne páros szám')

print('while:', end=' ')
i:int = 0
while i < len(sorozat):
    if sorozat[i]%2 == 0:
        print('van benne páros szám')
        break
    i += 1
else: print('nincs benne páros szám')

print('func: ', end=' ')
if van_benne_paros(sorozat):
    print('van benne páros szám')
else: print('nincs benne páros szám')


ker_val = int(input('keresett érték: '))

print('for:  ', end=' ')
for i in range(len(sorozat)):
    if sorozat[i] == ker_val:
        print(f'keresett érték indexe: {i}')
        break
else: print('a keresett érték nincs benne a sorozatban')

print('while:', end=' ')
i:int = 0
while i < len(sorozat):
    if sorozat[i] == ker_val:
        print(f'keresett érték indexe: {i}')
        break
    i += 1
else: print('a keresett érték nincs benne a sorozatban')

print('func: ', end=' ')
ker_ind = lin_kereses(sorozat, ker_val)
if ker_ind == -1: print(f'a keresett érték nincs benne a sorozatban')
else: print(f'keresett érték indexe: {i}')
