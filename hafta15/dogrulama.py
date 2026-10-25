# MMAT105 Hafta 15 -- Final Sınavı Denemesi doğrulaması
# Her sorunun cevabı burada BAĞIMSIZ olarak (mümkünse brute force ile) hesaplanır;
# sorular.py'deki doğru şıkkın değeriyle eşleştiği ve diğer 4 şıkkın farklı olduğu kontrol edilir.
import os
import sys
from fractions import Fraction as F
from math import gcd
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sorular import S  # noqa: E402

HARF = 'ABCDE'
x = sp.Symbol('x')


def lcm(a, b):
    return a * b // gcd(a, b)


def asal(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def tek_cozum(f, aralik):
    c = [t for t in aralik if f(t)]
    assert len(c) == 1, c
    return c[0]


def kesirli_aralik(a, b, payda=12):
    return [F(k, payda) for k in range(a * payda, b * payda + 1)]


H = {}
# 1
H[1] = (-2) ** 3 - (-3) ** 2 + 4 * 5 - F(12, 3)
# 2
H[2] = sum(p for p in range(2, 85) if 84 % p == 0 and asal(p))
# 3: 08.00'den sonra ilk ortak kalkış (dakika)
H[3] = next(t for t in range(1, 10000) if t % 15 == 0 and t % 20 == 0 and t % 25 == 0)
# 4
H[4] = 2 - 1 / (1 - F(1, 3))
# 5: Ayşe a, Ali 3a
a = tek_cozum(lambda a: 3 * a - 40 == a + 40, kesirli_aralik(0, 1000, 1))
H[5] = 3 * a
# 6
H[6] = tek_cozum(lambda d: 4 * d - (30 - d) == 70, range(0, 31))
# 7
H[7] = sum(1 for t in range(-1000, 1000) if 2 < abs(t - 1) <= 5)
# 8
H[8] = F(2 ** 5 * 4 ** 3, 8 ** 4)
# 9: x'ten bağımsız olmalı
vals9 = {F(2 ** (t + 4) - 2 ** t, 2 ** (t + 1) + 2 ** t) for t in range(0, 8)}
assert len(vals9) == 1
assert sp.simplify((2 ** (x + 4) - 2 ** x) / (2 ** (x + 1) + 2 ** x) - list(vals9)[0]) == 0
H[9] = vals9.pop()
# 10
deg = {'a': 2 ** 48, 'b': 3 ** 36, 'c': 5 ** 24}
assert len(set(deg.values())) == 3
H[10] = ''.join(sorted(deg, key=deg.get))
# 11
H[11] = sp.sqrt(98) + sp.sqrt(8) - sp.sqrt(32)
# 12
H[12] = 6 / (sp.sqrt(7) - 1) - sp.sqrt(7)
# 13
H[13] = sp.sqrt(11 + sp.sqrt(72))
assert sp.expand((3 + sp.sqrt(2)) ** 2) == 11 + sp.sqrt(72)
# 14: y = 12 - x
xs = [t for t in kesirli_aralik(-50, 50) if t ** 2 - (12 - t) ** 2 == 48]
assert len(xs) == 1
H[14] = xs[0] * (12 - xs[0])
# 15: a+b=10, ab=21 olan tüm (rasyonel) çiftler aynı a^2+b^2'yi vermeli
ab = [(p, 10 - p) for p in kesirli_aralik(-50, 50) if p * (10 - p) == 21]
assert ab and len({p * p + q * q for p, q in ab}) == 1
H[15] = ab[0][0] ** 2 + ab[0][1] ** 2
# 16
H[16] = sp.simplify((x ** 2 - x - 6) / (x ** 2 - 9) / ((x + 2) / x))
# 17
b = tek_cozum(lambda b: F(91 - b, b) == F(5, 8), range(1, 91))
H[17] = b
# 18: iş = kişi * saat * gün
H[18] = tek_cozum(lambda g: 8 * 6 * 5 == 6 * 4 * g, kesirli_aralik(0, 100))
# 19
H[19] = tek_cozum(lambda k: F(24 * 65 + 80 * k, 24 + k) == 70, range(0, 500))
# 20
H[20] = tek_cozum(lambda t: F(2, 5) * t + 3 == 15, kesirli_aralik(-100, 100))
# 21: annenin yaşı a, kızın 50-a; 4 yıl önce a-4 = 5*(50-a-4); yaşlar pozitif
H[21] = tek_cozum(lambda a: a - 4 == 5 * (50 - a - 4) and 50 - a - 4 > 0, range(0, 51))
# 22
H[22] = tek_cozum(lambda t: t - F(1, 3) * t - F(1, 4) * (t - F(1, 3) * t) == 300, range(1, 10000))
# 23: basit faiz, süre ay
H[23] = F(40000 * 24 * 9, 1200)
# 24: maliyet 1250, etiket = %140, satış = etiketin %80'i; kâr = satış - maliyet
H[24] = F(1250 * 140, 100) * F(80, 100) - 1250
# 25
H[25] = tek_cozum(lambda m: F(20, 100) * 300 + F(35, 100) * m == F(30, 100) * (300 + m), range(0, 5000))


def sym(v):
    if isinstance(v, F):
        return sp.Rational(v.numerator, v.denominator)
    return sp.sympify(v)


def esit(p, q):
    if isinstance(p, str) or isinstance(q, str):
        return p == q
    return sp.simplify(sym(p) - sym(q)) == 0


assert len(S) == 25
for i, q in enumerate(S, 1):
    vals = [v for _, v in q['sec']]
    kk = HARF.index(q['dogru'])
    assert esit(vals[kk], H[i]), 'Soru %d: doğru şık %s=%s, hesap=%s' % (i, q['dogru'], vals[kk], H[i])
    for j in range(5):
        if j != kk:
            assert not esit(vals[j], H[i]), 'Soru %d: %s şıkkı da doğru değere eşit' % (i, HARF[j])
    for p_ in range(5):
        for r_ in range(p_ + 1, 5):
            assert not esit(vals[p_], vals[r_]), 'Soru %d: %s ve %s şıkları aynı' % (i, HARF[p_], HARF[r_])
    print('Soru %2d (H%-2d, %s): cevap %s = %s  -- OK' % (i, q['h'], q['z'], q['dogru'], H[i]))

harf = {h: sum(q['dogru'] == h for q in S) for h in HARF}
print('\nDoğru şık dağılımı:', harf)
assert all(3 <= c <= 6 for c in harf.values())
haf = {}
for q in S:
    haf[q['h']] = haf.get(q['h'], 0) + 1
print('Hafta dağılımı:', haf)
assert sum(c for h, c in haf.items() if h <= 7) == 7
assert all(haf.get(h) == 3 for h in range(9, 15))
zor = {z: sum(q['z'] == z for q in S) for z in 'KOZ'}
print('Düzey dağılımı (K/O/Z):', zor)
assert zor == {'K': 8, 'O': 12, 'Z': 5}
# Bölümler: Hafta 1-7 tek bölüm; 9..14 her hafta ayrı bölüm. Her bölümde kolaydan zora.
sira = {'K': 0, 'O': 1, 'Z': 2}
bolumler = [[q for q in S if q['h'] <= 7]] + [[q for q in S if q['h'] == h] for h in range(9, 15)]
for bl in bolumler:
    zz = [sira[q['z']] for q in bl]
    assert zz == sorted(zz), 'sıralama: hafta %s' % bl[0]['h']
assert [q['h'] for q in S] == sorted(q['h'] for q in S)
print('\nTÜM KONTROLLER GEÇTİ (%d soru).' % len(S))
