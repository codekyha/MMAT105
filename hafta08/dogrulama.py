# MMAT105 Hafta 8 -- Ara Sınav Denemesi doğrulaması
# Her sorunun cevabı burada BAĞIMSIZ olarak (mümkünse brute force ile) hesaplanır;
# sorular.py'deki doğru şıkkın değeriyle eşleştiği ve diğer 4 şıkkın farklı olduğu kontrol edilir.
import os
import sys
from fractions import Fraction as F
from math import gcd
from itertools import permutations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sorular import S  # noqa: E402

HARF = 'ABCDE'


def lcm(a, b):
    return a * b // gcd(a, b)


def bolen_say(n):
    return sum(1 for k in range(1, n + 1) if n % k == 0)


def asal(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def fakt(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def tek_cozum(f, aralik):
    """aralik içinde f(x) doğru olan TEK değeri döndürür (birden fazla/hiç yoksa hata)."""
    c = [x for x in aralik if f(x)]
    assert len(c) == 1, c
    return c[0]


def kesirli_aralik(a, b, payda=12):
    return [F(k, payda) for k in range(a * payda, b * payda + 1)]


H = {}

# 1
H[1] = 18 - F(4 * (7 - 10), 2) + (-3) ** 2
# 2: ardışık 6 çift sayı, toplam 150
H[2] = max(tek_cozum(lambda a: a % 2 == 0 and sum(a + 2 * i for i in range(6)) == 150,
                     range(-200, 200)) + 2 * i for i in range(6))
# 3
H[3] = tek_cozum(lambda n: F(fakt(n + 1) - fakt(n), fakt(n - 1)) == 49, range(1, 60))
# 4
H[4] = bolen_say(600)
# 5: A=9B+5, B mod 4 = 3 -> A mod 36 (tüm B'ler için aynı olmalı)
kal = {(9 * B + 5) % 36 for B in range(0, 2000) if B % 4 == 3}
assert len(kal) == 1
H[5] = kal.pop()
# 6
H[6] = tek_cozum(lambda x: bolen_say(2 ** x * 125) - sum(1 for k in range(2, 2 ** x * 125 + 1)
                                                        if (2 ** x * 125) % k == 0 and asal(k)) == 22,
                 range(1, 12))
# 7
H[7] = tek_cozum(lambda a: (500 + 10 * a + 6) % 9 == 0, range(10))
# 8
H[8] = tek_cozum(lambda y: gcd(36, y) == 6 and lcm(36, y) == 180, range(1, 5000))
# 9: aralık d | 84, d | 126, 1 <= d < 10 tam sayı; fidan sayısı = çevre/d (kapalı çevre); en az
H[9] = min(2 * (84 + 126) // d for d in range(1, 10) if 84 % d == 0 and 126 % d == 0)
# 10
H[10] = F(5, 6) - F(1, 3) / F(2, 3)
# 11
H[11] = F('0.12') / F('0.04') + F('1.5') / F('0.03') - F('0.2') * 15
# 12
deg = {'a': F(7, 9), 'b': F(5, 6), 'c': F(11, 14)}
H[12] = ''.join(sorted(deg, key=deg.get))
assert len(set(deg.values())) == 3
# 13
H[13] = tek_cozum(lambda x: 4 * (x - 3) - 3 * (x + 2) == 4 - x, kesirli_aralik(-50, 50))
# 14
H[14] = tek_cozum(lambda x: (x + 1) / F(3) - (x - 2) / F(4) == x / F(6), kesirli_aralik(-50, 50))
# 15: (a x - 2)/3 = x + b/6 her x için doğru olacak (a, b) -> a*b
#     her x için doğru <=> x = 0 ve x = 1 için doğru (doğrusal ifadeler)
ab = [(a, b) for a in kesirli_aralik(-20, 20, 2) for b in kesirli_aralik(-20, 20, 2)
      if all((a * x - 2) / F(3) == x + b / F(6) for x in (0, 1, 7))]
assert len(ab) == 1
H[15] = ab[0][0] * ab[0][1]
# 16
xy = [(x, y) for x in kesirli_aralik(-20, 20, 6) for y in kesirli_aralik(-20, 20, 6)
      if 2 * x + 3 * y == 17 and 3 * x - y == 9]
assert len(xy) == 1
H[16] = xy[0][0] * xy[0][1]
# 17
xy = [(x, y) for x in kesirli_aralik(-20, 20, 6) for y in kesirli_aralik(-20, 20, 6)
      if x / F(3) + y / F(4) == 5 and x / F(4) + y / F(3) == F(11, 2)]
assert len(xy) == 1
H[17] = sum(xy[0])
# 18
H[18] = sum(1 for x in range(-1000, 1000) if -2 <= 4 - x < 3)
# 19: kökler (tüm rasyonel adaylar taranır)
kok = [x for x in kesirli_aralik(-50, 50, 2) if abs(2 * x - 5) == 7]
assert len(kok) == 2
H[19] = kok[0] * kok[1]
# 20
H[20] = sum(x for x in range(-1000, 1000) if abs(3 - x) <= 4)


def esit(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return a == b
    return F(a) == F(b)


assert len(S) == 20
hata = 0
for i, q in enumerate(S, 1):
    vals = [v for _, v in q['sec']]
    k = HARF.index(q['dogru'])
    assert esit(vals[k], H[i]), 'Soru %d: doğru şık %s=%s, hesap=%s' % (i, q['dogru'], vals[k], H[i])
    for j in range(5):
        if j != k:
            assert not esit(vals[j], H[i]), 'Soru %d: %s şıkkı da doğru değere eşit' % (i, HARF[j])
    for a in range(5):
        for b in range(a + 1, 5):
            assert not esit(vals[a], vals[b]), 'Soru %d: %s ve %s şıkları aynı' % (i, HARF[a], HARF[b])
    print('Soru %2d (H%d, %s): cevap %s = %s  -- OK' % (i, q['h'], q['z'], q['dogru'], H[i]))

# Dağılım kontrolleri
harf = {h: sum(q['dogru'] == h for q in S) for h in HARF}
print('\nDoğru şık dağılımı:', harf)
assert all(3 <= c <= 6 for c in harf.values())
haf = {}
for q in S:
    haf[q['h']] = haf.get(q['h'], 0) + 1
print('Hafta dağılımı:', haf)
assert haf == {1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 3}
zor = {z: sum(q['z'] == z for q in S) for z in 'KOZ'}
print('Düzey dağılımı (K/O/Z):', zor)
assert zor == {'K': 6, 'O': 10, 'Z': 4}
# her hafta bölümünde kolaydan zora sıralı
sira = {'K': 0, 'O': 1, 'Z': 2}
for h in haf:
    zz = [sira[q['z']] for q in S if q['h'] == h]
    assert zz == sorted(zz), 'Hafta %d sıralama' % h
assert [q['h'] for q in S] == sorted(q['h'] for q in S)
print('\nTÜM KONTROLLER GEÇTİ (%d soru).' % len(S))
