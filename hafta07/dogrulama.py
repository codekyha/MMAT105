#!/usr/bin/env python3
"""MMAT105 Hafta 7 -- sunum ve ders notundaki tüm sayısal cevapların doğrulaması.

Eşitsizlik / mutlak değer çözüm kümeleri iki yolla kontrol edilir:
  (1) sympy.solveset (reel sayılarda),
  (2) rasyonel sayı taraması (adım 1/8, [-40, 40]) ve tam sayı taraması.
"""
from fractions import Fraction as F
import itertools
import math
import random

import sympy as sp

x = sp.symbols('x', real=True)
R = sp.S.Reals
BOS = sp.S.EmptySet
Iv = sp.Interval
oo = sp.oo

GECEN = 0


def ok(kosul, etiket):
    global GECEN
    assert kosul, etiket
    GECEN += 1


# ---------------------------------------------------------------- yardımcılar
IZGARA = [F(k, 8) for k in range(-320, 321)]          # [-40, 40], adım 1/8
TAM = list(range(-200, 201))


def icinde(kume, q):
    return bool(kume.contains(sp.Rational(q.numerator, q.denominator) if isinstance(q, F) else q))


def tara(pred, kume, etiket):
    """Rasyonel ızgarada pred(q) <=> q in kume."""
    for q in IZGARA:
        ok(pred(q) == icinde(kume, q), f"{etiket}: tarama q={q}")


def cozum(ifade_listesi, etiket, beklenen, pred):
    """ifade_listesi: sympy ilişkilerinin listesi (hepsi birlikte sağlanmalı)."""
    k = R
    for rel in ifade_listesi:
        k = k.intersect(sp.solveset(rel, x, R))
    ok(k == beklenen, f"{etiket}: sympy {k} != {beklenen}")
    tara(pred, beklenen, etiket)


def tamlar(pred, lo=-200, hi=200):
    return [n for n in range(lo, hi + 1) if pred(n)]


def aralik_1(f, alan, beklenen, etiket):
    """f doğrusal/sürekli; alan: sympy aralığı. imageset + ızgara kontrolü."""
    im = sp.imageset(sp.Lambda(x, f(x)), alan)
    ok(im == beklenen, f"{etiket}: imageset {im} != {beklenen}")
    vals = [f(sp.Rational(q.numerator, q.denominator)) for q in IZGARA if icinde(alan, q)]
    ok(all(bool(beklenen.contains(v)) for v in vals), f"{etiket}: değer aralık dışında")
    ok(abs(min(vals) - beklenen.inf) <= 1, f"{etiket}: alt sınıra yaklaşılmıyor")
    ok(abs(max(vals) - beklenen.sup) <= 1, f"{etiket}: üst sınıra yaklaşılmıyor")


def aralik_2(f, ax, ay, beklenen, etiket, adim=20):
    """İki değişkenli ifade; ax, ay: (alt, üst, alt_dahil, üst_dahil)."""
    def noktalar(a):
        lo, hi, ld, hd = a
        n = int((hi - lo) * adim)
        pts = [F(lo) + F(k, adim) for k in range(n + 1)]
        return [p for p in pts if (p > lo or ld) and (p < hi or hd)]
    X, Y = noktalar(ax), noktalar(ay)
    vals = [f(p, q) for p in X for q in Y]
    lo, hi, ld, hd = beklenen
    ok(all((v > lo or (ld and v == lo)) and (v < hi or (hd and v == hi)) for v in vals),
       f"{etiket}: aralık dışı değer")
    ok(min(vals) - lo <= F(1, 2) and hi - max(vals) <= F(1, 2), f"{etiket}: sınıra yaklaşılmıyor")
    # köşe (sınır) değerlerinin gerçekten sup/inf olduğu: sınırlar üzerindeki değerler
    kose = [f(F(a), F(b)) for a in (ax[0], ax[1]) for b in (ay[0], ay[1])]
    ok(min(kose) == lo and max(kose) == hi, f"{etiket}: köşe değerleri {kose}")


def ornek_al(kosul, n=4000, lo=-20, hi=20):
    """kosul(*değerler) sağlayan rastgele rasyonel örnekler."""
    random.seed(7)
    out = []
    while len(out) < n:
        v = [F(random.randint(lo * 8, hi * 8), 8) for _ in range(kosul.__code__.co_argcount)]
        if kosul(*v):
            out.append(v)
    return out


def denklem(ifade, beklenen, etiket):
    k = sp.solveset(ifade, x, R)
    ok(k == beklenen, f"{etiket}: sympy {k} != {beklenen}")
    # rasyonel tarama: kökler ızgarada ise tam eşitlik ile bul
    f = sp.lambdify(x, ifade, modules=[{'Abs': abs}])
    bulunan = {q for q in IZGARA if f(q) == 0}
    beklenen_izgara = {q for q in IZGARA if icinde(beklenen, q)}
    ok(bulunan == beklenen_izgara, f"{etiket}: tarama {bulunan}")


# ============================================================ SUNUM
# --- Geçen hafta hatırlatma
X, Y = sp.symbols('X Y')
ok(sp.solve([X + Y - 10, X - Y - 4], [X, Y]) == {X: 7, Y: 3}, "GH1")
ok(sp.solve([2 * X + 3 * Y - 12, X - Y - 1], [X, Y]) == {X: 3, Y: 2}, "GH2")
s = sp.solve([3 * X + 2 * Y - 16, X + 2 * Y - 8], [X, Y]); ok(s == {X: 4, Y: 2} and s[X] * s[Y] == 8, "GH3")

# --- Ders 1
# Örnek 1: aralık gösterimleri
tara(lambda q: -2 < q <= 5, Iv.Lopen(-2, 5), "S1a")
tara(lambda q: q >= 3, Iv(3, oo), "S1b")
tara(lambda q: q < -1, Iv.open(-oo, -1), "S1c")
tara(lambda q: 0 <= q < 4, Iv.Ropen(0, 4), "S1d")
tara(lambda q: -1 <= q < 4, Iv.Ropen(-1, 4), "S1e")
# Örnek 2
tara(lambda q: -2 < q <= 3, Iv.Lopen(-2, 3), "S2a")
cozum([x < 1], "S2b", Iv.open(-oo, 1), lambda q: q < 1)
# Örnek 3: a<b için I, III, IV her zaman doğru; II her zaman yanlış
orn = ornek_al(lambda a, b: a < b)
ok(all(a - 5 < b - 5 for a, b in orn), "S3-I")
ok(not any(-2 * a < -2 * b for a, b in orn), "S3-II yanlış olmalı")
ok(all(a / 3 < b / 3 for a, b in orn), "S3-III")
ok(all(4 - a > 4 - b for a, b in orn), "S3-IV")
# Örnek 4
ok(5 + 1 < 6 + 4 and not (5 - 1 < 6 - 4), "S4")
# Örnek 5
aralik_1(lambda t: 1 / t, Iv.open(2, 5), Iv.open(sp.Rational(1, 5), sp.Rational(1, 2)), "S5a")
aralik_1(lambda t: 1 / t, Iv.open(-4, -2), Iv.open(-sp.Rational(1, 2), -sp.Rational(1, 4)), "S5b")
ok(F(-1, 2) < F(-1, 3) < F(-1, 4), "S5 kontrol")
# Örnek 6-11
cozum([3 * x - 5 < 7], "S6", Iv.open(-oo, 4), lambda q: 3 * q - 5 < 7)
cozum([-2 * x + 3 >= 11], "S7", Iv(-oo, -4), lambda q: -2 * q + 3 >= 11)
cozum([5 - 3 * x > 2 * x - 10], "S8", Iv.open(-oo, 3), lambda q: 5 - 3 * q > 2 * q - 10)
ok(max(tamlar(lambda n: 5 - 3 * n > 2 * n - 10)) == 2, "S8 en büyük tam sayı")
cozum([(x - 1) / 2 - (x + 2) / 3 <= 1], "S9", Iv(-oo, 13), lambda q: (q - 1) / 2 - (q + 2) / 3 <= 1)
cozum([2 * x + 1 > -3, 2 * x + 1 <= 7], "S10", Iv.Lopen(-2, 3), lambda q: -3 < 2 * q + 1 <= 7)
cozum([(5 - x) / 2 >= -1, (5 - x) / 2 < 3], "S11", Iv.Lopen(-1, 7), lambda q: -1 <= (5 - q) / 2 < 3)
# Örnek 12
cozum([3 * x - 2 < 3 * x + 1], "S12a", R, lambda q: 3 * q - 2 < 3 * q + 1)
cozum([2 * x + 5 < 2 * (x + 1)], "S12b", BOS, lambda q: 2 * q + 5 < 2 * (q + 1))
# Ders 1 siz çözün
cozum([4 * x - 7 >= 9], "D1-1", Iv(4, oo), lambda q: 4 * q - 7 >= 9)
cozum([2 - 5 * x < 17], "D1-2", Iv.open(-3, oo), lambda q: 2 - 5 * q < 17)
cozum([3 * x - 2 > 1, 3 * x - 2 <= 10], "D1-3", Iv.Lopen(1, 4), lambda q: 1 < 3 * q - 2 <= 10)
tara(lambda q: -3 <= q < 2, Iv.Ropen(-3, 2), "D1-4")
aralik_1(lambda t: 1 / t, Iv.open(3, 6), Iv.open(sp.Rational(1, 6), sp.Rational(1, 3)), "D1-5")

# --- Ders 2
# Örnek 13
cozum([2 * x - 3 < 11], "S13", Iv.open(-oo, 7), lambda q: 2 * q - 3 < 11)
ok(max(tamlar(lambda n: 2 * n - 3 < 11)) == 6, "S13 en büyük")
ok(min(n for n in range(0, 50) if 2 * n - 3 < 11) == 0, "S13 en küçük doğal")
# Örnek 14
cozum([3 * x + 1 >= -5, 3 * x + 1 < 13], "S14", Iv.Ropen(-2, 4), lambda q: -5 <= 3 * q + 1 < 13)
T = tamlar(lambda n: -5 <= 3 * n + 1 < 13); ok(len(T) == 6 and sum(T) == 3, "S14 sayma")
# Örnek 15
cozum([2 * x - 1 > -7, 2 * x - 1 < 8], "S15", Iv.open(-3, sp.Rational(9, 2)), lambda q: -7 < 2 * q - 1 < 8)
T = tamlar(lambda n: -7 < 2 * n - 1 < 8)
ok((min(T), max(T), sum(T), len(T)) == (-2, 4, 7, 7), "S15 sayma")
# Örnek 16
cozum([x / 3 + 2 > x - 4], "S16", Iv.open(-oo, 9), lambda q: q / 3 + 2 > q - 4)
ok(len([n for n in range(1, 200) if F(n, 3) + 2 > n - 4]) == 8, "S16 pozitif tam sayı")
# Örnek 17
aralik_1(lambda t: 3 * t - 1, Iv.open(-2, 5), Iv.open(-7, 14), "S17")
ok(len([m for m in TAM if -7 < m < 14]) == 20, "S17 tam değer sayısı")
ok(all(-2 < F(m + 1, 3) < 5 for m in range(-6, 14)), "S17 her tam değer alınır")
# Örnek 18
aralik_1(lambda t: 5 - 2 * t, Iv.Lopen(-3, 2), Iv.Ropen(1, 11), "S18")
# Örnek 19
aralik_2(lambda a, b: a + b, (2, 6, False, False), (-3, 1, False, False), (-1, 7, False, False), "S19 x+y")
aralik_2(lambda a, b: a - b, (2, 6, False, False), (-3, 1, False, False), (1, 9, False, False), "S19 x-y")
# Örnek 20
XS, YS = [n for n in TAM if 2 < n < 6], [n for n in TAM if -3 < n < 1]
ok(max(a - b for a in XS for b in YS) == 7, "S20 max x-y")
ok(min(a + b for a in XS for b in YS) == 1, "S20 min x+y")
# Örnek 21
aralik_2(lambda a, b: a * b, (2, 6, False, False), (-3, 1, False, False), (-18, 6, False, False), "S21")
# Örnek 22
for (lo, hi, ust) in [(-3, 2, 9), (-1, 4, 16)]:
    im = sp.imageset(sp.Lambda(x, x ** 2), Iv.open(lo, hi))
    ok(im == Iv.Ropen(0, ust), f"S22 imageset {im}")
    vals = [q * q for q in IZGARA if lo < q < hi]
    ok(min(vals) == 0 and max(vals) < ust and ust - max(vals) < 1, f"S22 tarama ({lo},{hi})")
# Örnek 23
XS, YS = [n for n in TAM if -4 < n < 3], [n for n in TAM if -2 < n < 5]
V = [a * a - b for a in XS for b in YS]
ok((max(V), min(V)) == (10, -4), "S23")
# Ders 2 siz çözün
ok(len(tamlar(lambda n: -4 <= 2 * n + 2 < 9)) == 7, "D2-1")
aralik_1(lambda t: 2 - 3 * t, Iv.open(-1, 4), Iv.open(-10, 5), "D2-2")
aralik_2(lambda a, b: a - b, (1, 5, False, False), (-2, 3, False, False), (-2, 7, False, False), "D2-3")
ok(sp.imageset(sp.Lambda(x, x ** 2), Iv.open(-5, 2)) == Iv.Ropen(0, 25), "D2-4")
XS, YS = [n for n in TAM if -2 < n < 4], [n for n in TAM if 1 < n < 6]
ok(min(a * b for a in XS for b in YS) == -5, "D2-5")
ok((-1) * 5 == -5 and -1 in XS and 5 in YS, "D2-5 değerler")

# --- Ders 3
ok(abs(-7) + abs(3) - abs(-2 - 4) == 4 and abs(5 - 8) - abs(8 - 5) == 0, "S24")
denklem(sp.Abs(x - 3) - 4, sp.FiniteSet(-1, 7), "S25")
# Örnek 26: a<0<b => |a-b|+|b|-|a| = 2b
ok(all(abs(a - b) + abs(b) - abs(a) == 2 * b for a, b in ornek_al(lambda a, b: a < 0 < b)), "S26")
ok(abs(-1 - 2) + abs(2) - abs(-1) == 4, "S26 kontrol")
# Örnek 27: x<-2 => |x+2|-|3-x| = -5
ok(all(abs(t + 2) - abs(3 - t) == -5 for t in IZGARA if t < -2), "S27")
# Örnek 28: 1<x<4 => |x-1|+|x-4| = 3
ok(all(abs(t - 1) + abs(t - 4) == 3 for t in IZGARA if 1 < t < 4), "S28")
# Örnek 29-31
denklem(sp.Abs(2 * x - 3) - 7, sp.FiniteSet(-2, 5), "S29"); ok(-2 + 5 == 3, "S29 toplam")
denklem(sp.Abs(x + 1) + 3, BOS, "S30a")
denklem(sp.Abs(3 * x - 6), sp.FiniteSet(2), "S30b")
denklem(sp.Abs(x - 2) + 5 - 3, BOS, "S30c")
denklem(sp.Abs(x - 1) - sp.Abs(2 * x + 4), sp.FiniteSet(-5, -1), "S31")
# Örnek 32-36
cozum([sp.Abs(x - 3) < 5], "S32", Iv.open(-2, 8), lambda q: abs(q - 3) < 5)
ok(len(tamlar(lambda n: abs(n - 3) < 5)) == 9, "S32 sayma")
cozum([sp.Abs(2 * x + 1) <= 7], "S33", Iv(-4, 3), lambda q: abs(2 * q + 1) <= 7)
T = tamlar(lambda n: abs(2 * n + 1) <= 7); ok(len(T) == 8 and sum(T) == -4, "S33 toplam")
cozum([sp.Abs(x + 2) > 3], "S34", sp.Union(Iv.open(-oo, -5), Iv.open(1, oo)), lambda q: abs(q + 2) > 3)
cozum([sp.Abs(3 * x - 1) < -4], "S35a", BOS, lambda q: abs(3 * q - 1) < -4)
cozum([sp.Abs(x + 7) >= 0], "S35b", R, lambda q: abs(q + 7) >= 0)
cozum([sp.Abs(x - 2) <= 0], "S35c", sp.FiniteSet(2), lambda q: abs(q - 2) <= 0)
cozum([sp.Abs(x - 1) >= 2, sp.Abs(x - 1) < 5], "S36",
      sp.Union(Iv.Lopen(-4, -1), Iv.Ropen(3, 6)), lambda q: 2 <= abs(q - 1) < 5)
T = tamlar(lambda n: 2 <= abs(n - 1) < 5); ok(T == [-3, -2, -1, 3, 4, 5], "S36 sayma")
# Ders 3 siz çözün
ok(abs(-4) - abs(2 - 9) + abs(0) == -3, "D3-1")
ok(all(abs(a) + abs(b - a) - abs(b) == -2 * a for a, b in ornek_al(lambda a, b: a < 0 < b)), "D3-2")
denklem(sp.Abs(2 * x - 1) - 9, sp.FiniteSet(-4, 5), "D3-3")
ok(len(tamlar(lambda n: abs(n + 1) <= 4)) == 9, "D3-4")
cozum([sp.Abs(x - 2) > 6], "D3-5", sp.Union(Iv.open(-oo, -4), Iv.open(8, oo)), lambda q: abs(q - 2) > 6)

# ============================================================ DERS NOTU (örnekler)
A_, B_ = Iv.Ropen(-2, 3), Iv.Lopen(0, 5)
ok(A_.intersect(B_) == Iv.open(0, 3) and A_.union(B_) == Iv(-2, 5), "N1")
tara(lambda q: -2 <= q < 3 and 0 < q <= 5, Iv.open(0, 3), "N1 tarama kesişim")
tara(lambda q: -2 <= q < 3 or 0 < q <= 5, Iv(-2, 5), "N1 tarama birleşim")
orn = ornek_al(lambda a, b: a < b < 0)
ok(all(a * a > b * b and 1 / a > 1 / b for a, b in orn), "N2")
cozum([(2 * x + 1) / 3 - (x - 2) / 4 >= 2], "N3", Iv(sp.Rational(14, 5), oo),
      lambda q: (2 * q + 1) / 3 - (q - 2) / 4 >= 2)
ok(min(tamlar(lambda n: F(2 * n + 1, 3) - F(n - 2, 4) >= 2)) == 3, "N3 en küçük tam sayı")
cozum([2 * (x - 3) - 5 > 4 * x + 1], "N4", Iv.open(-oo, -6), lambda q: 2 * (q - 3) - 5 > 4 * q + 1)
ok(max(tamlar(lambda n: 2 * (n - 3) - 5 > 4 * n + 1)) == -7, "N4 en büyük tam sayı")
cozum([5 - 3 * x > -4, 5 - 3 * x <= 11], "N5", Iv.Ropen(-2, 3), lambda q: -4 < 5 - 3 * q <= 11)
cozum([3 * x - 1 > 5, 2 * x + 3 <= 15], "N6", Iv.Lopen(2, 6), lambda q: 3 * q - 1 > 5 and 2 * q + 3 <= 15)
ok(tamlar(lambda n: 3 * n - 1 > 5 and 2 * n + 3 <= 15) == [3, 4, 5, 6], "N6 sayma")
aralik_1(lambda t: 4 - 2 * t, Iv.Ropen(-1, 3), Iv.Lopen(-2, 6), "N7")
ok(len([m for m in TAM if -2 < m <= 6]) == 8, "N7 tam değer sayısı")
aralik_2(lambda a, b: 2 * a - 3 * b, (1, 4, False, False), (2, 5, False, False), (-13, 2, False, False), "N8")
XS, YS = [n for n in TAM if 1 < n < 4], [n for n in TAM if 2 < n < 5]
V = [2 * a - 3 * b for a in XS for b in YS]; ok((max(V), min(V)) == (-3, -8), "N8 tam sayı")
aralik_2(lambda a, b: a * b, (-2, 3, False, False), (1, 4, False, False), (-8, 12, False, False), "N9")
a, b = -3, 5; ok(abs(a) - abs(b) + abs(a - b) - abs(b - a) == -2, "N10")
ok(all(abs(a - b) + abs(c - a) - abs(b - c) == 2 * b - 2 * a
       for a, b, c in ornek_al(lambda a, b, c: a < b < 0 < c)), "N11")
ok(abs(-3 - (-1)) + abs(2 - (-3)) - abs(-1 - 2) == 4, "N11 kontrol")
ok(all(abs(t - 2) + abs(t - 5) - abs(t) == 3 - t for t in IZGARA if 2 < t < 5), "N12")
denklem(sp.Abs(3 * x - 4) - 5, sp.FiniteSet(-sp.Rational(1, 3), 3), "N13")
ok(sp.Rational(-1, 3) * 3 == -1, "N13 çarpım")
denklem(sp.Abs(2 * x - 1) - sp.Abs(x + 4), sp.FiniteSet(-1, 5), "N14"); ok(-1 + 5 == 4, "N14 toplam")
denklem(sp.Abs(x - 2) + 2 * x - 7, sp.FiniteSet(3), "N15")
cozum([sp.Abs(x - 4) <= 3], "N16", Iv(1, 7), lambda q: abs(q - 4) <= 3)
T = tamlar(lambda n: abs(n - 4) <= 3); ok(len(T) == 7 and sum(T) == 28, "N16 sayma")
ok(len([n for n in range(-10, 11) if not abs(2 * n + 3) > 5]) == 6, "N17")
cozum([sp.Abs(2 * x + 3) > 5], "N17 çk", sp.Union(Iv.open(-oo, -4), Iv.open(1, oo)), lambda q: abs(2 * q + 3) > 5)
T = tamlar(lambda n: 1 < abs(n + 2) <= 4); ok(T == [-6, -5, -4, 0, 1, 2] and sum(T) == -12, "N18")
cozum([sp.Abs(x + 2) > 1, sp.Abs(x + 2) <= 4], "N18 çk",
      sp.Union(Iv.Ropen(-6, -3), Iv.Lopen(-1, 2)), lambda q: 1 < abs(q + 2) <= 4)
cozum([sp.Abs(x - 3) < 6], "N19", Iv.open(-3, 9), lambda q: abs(q - 3) < 6)

# ============================================================ ALIŞTIRMALAR
tara(lambda q: -3 <= q < 5, Iv.Ropen(-3, 5), "A1a"); tara(lambda q: q <= 2, Iv(-oo, 2), "A1b")
cozum([5 * x - 3 <= 2 * x + 9], "A2", Iv(-oo, 4), lambda q: 5 * q - 3 <= 2 * q + 9)
cozum([7 - 2 * x > 3 * (x - 1)], "A3", Iv.open(-oo, 2), lambda q: 7 - 2 * q > 3 * (q - 1))
cozum([(x + 1) / 2 - (x - 3) / 5 < 2], "A4", Iv.open(-oo, 3), lambda q: (q + 1) / 2 - (q - 3) / 5 < 2)
ok(max(tamlar(lambda n: F(n + 1, 2) - F(n - 3, 5) < 2)) == 2, "A4 en büyük")
cozum([2 * x + 3 > -5, 2 * x + 3 <= 11], "A5", Iv.Lopen(-4, 4), lambda q: -5 < 2 * q + 3 <= 11)
T = tamlar(lambda n: -5 < 2 * n + 3 <= 11); ok(len(T) == 8 and sum(T) == 4, "A5 sayma")
cozum([4 - x >= 2 * x - 11, x > -3], "A6", Iv.Lopen(-3, 5), lambda q: 4 - q >= 2 * q - 11 and q > -3)
ok(len(tamlar(lambda n: 4 - n >= 2 * n - 11 and n > -3)) == 8, "A6 sayma")
aralik_1(lambda t: 5 - 2 * t, Iv.open(-1, 3), Iv.open(-1, 7), "A7")
aralik_2(lambda a, b: a + b, (3, 7, False, False), (-2, 4, False, False), (1, 11, False, False), "A8 x+y")
aralik_2(lambda a, b: a - b, (3, 7, False, False), (-2, 4, False, False), (-1, 9, False, False), "A8 x-y")
ok(sp.imageset(sp.Lambda(x, x ** 2), Iv.open(-4, 3)) == Iv.Ropen(0, 16), "A9")
XS, YS = [n for n in TAM if -3 < n < 2], [n for n in TAM if -1 < n < 5]
V = [a * b for a in XS for b in YS]; ok((min(V), max(V)) == (-8, 4), "A10")
ok(abs(-6) - abs(4 - 9) + abs(-2) * abs(3) == 7, "A11")
ok(all(abs(a - b) - abs(b) - abs(2 * a) == a for a, b in ornek_al(lambda a, b: a < 0 < b)), "A12")
denklem(sp.Abs(4 * x - 2) - 10, sp.FiniteSet(-2, 3), "A13")
denklem(sp.Abs(x + 2) - sp.Abs(x - 6), sp.FiniteSet(2), "A14")
cozum([sp.Abs(x - 5) < 3], "A15", Iv.open(2, 8), lambda q: abs(q - 5) < 3)
T = tamlar(lambda n: abs(n - 5) < 3); ok(len(T) == 5 and sum(T) == 25, "A15 sayma")
cozum([sp.Abs(3 * x - 1) >= 8], "A16 çk", sp.Union(Iv(-oo, -sp.Rational(7, 3)), Iv(3, oo)),
      lambda q: abs(3 * q - 1) >= 8)
ok([n for n in range(-5, 6) if abs(3 * n - 1) >= 8] == [-5, -4, -3, 3, 4, 5], "A16 sayma")
T = tamlar(lambda n: 2 <= abs(n - 3) <= 5)
ok(T == [-2, -1, 0, 1, 5, 6, 7, 8] and sum(T) == 24, "A17")

# ============================================================ KARMA TEKRAR
ok(5 - 2 * (3 - 7) + F((-2) ** 3, 4) == 11, "K1")
ok(math.factorial(8) // (math.factorial(6) * math.factorial(2)) + math.factorial(0) == 29, "K2")
ok(len([d for d in range(1, 361) if 360 % d == 0]) == 24 and sp.factorint(360) == {2: 3, 3: 2, 5: 1}, "K3")
ok(max(n for n in range(0, 200) if n // 7 == 12) == 90, "K4")
aa = sorted({a for a in range(10) for b in range(10) if int(f"3{a}5{b}") % 45 == 0})
ok(aa == [1, 5] and sum(aa) == 6, "K5")
ok(min(n for n in range(10, 100) if n % 18 == 5 and n % 24 == 5) == 77, "K6")
ok((F(6, 10) + F(2, 5)) / (F(125, 100) - F(3, 4)) == 2, "K7")
ok(sorted([("a", F(3, 4)), ("b", F(5, 7)), ("c", F(7, 9))], key=lambda t: t[1]) ==
   [("b", F(5, 7)), ("a", F(3, 4)), ("c", F(7, 9))], "K8")
ok(sp.solve((x - 2) / 3 + (x + 1) / 2 - 4, x) == [5], "K9")
s = sp.solve([2 * X + Y - 11, X - Y - 1], [X, Y]); ok(s == {X: 4, Y: 3} and s[X] * s[Y] == 12, "K10")
cozum([2 * x - 5 > -3, 2 * x - 5 <= 7], "K11 çk", Iv.Lopen(1, 6), lambda q: -3 < 2 * q - 5 <= 7)
ok(len(tamlar(lambda n: -3 < 2 * n - 5 <= 7)) == 5, "K11")
cozum([sp.Abs(2 * x - 3) <= 5], "K12 çk", Iv(-1, 4), lambda q: abs(2 * q - 3) <= 5)
ok(sum(tamlar(lambda n: abs(2 * n - 3) <= 5)) == 9, "K12")

# ======================================================================
# SÜRÜM 2 EKLERİ
# ---------------- SUNUM: yıldızlı alıştırma çözüm çerçeveleri ----------------
# Ders 1 Soru 2: -5x<15 -> x>-3
cozum([-5 * x < 15], "S2-D1-2 ara adım", Iv.open(-3, oo), lambda q: -5 * q < 15)
# Ders 1 Soru 3: 3<3x<=12 -> 1<x<=4
cozum([3 * x > 3, 3 * x <= 12], "S2-D1-3 ara adım", Iv.Lopen(1, 4), lambda q: 3 < 3 * q <= 12)
# Ders 1 Soru 5: kontrol x=4
ok(F(1, 6) < F(1, 4) < F(1, 3), "S2-D1-5 kontrol")
# Ders 2 Soru 1: -6<=2x<7 -> -3<=x<3,5 ; tam sayılar -3..3
ok(tamlar(lambda n: -6 <= 2 * n < 7) == [-3, -2, -1, 0, 1, 2, 3], "S2-D2-1")
# Ders 2 Soru 3: -3<-y<2 ; 1+(-3)=-2, 5+2=7
aralik_1(lambda t: -t, Iv.open(-2, 3), Iv.open(-3, 2), "S2-D2-3 -y")
ok(1 + (-3) == -2 and 5 + 2 == 7, "S2-D2-3 toplam")
# Ders 2 Soru 5: x in {-1..3}, y in {2..5}
XS, YS = [n for n in TAM if -2 < n < 4], [n for n in TAM if 1 < n < 6]
ok(XS == [-1, 0, 1, 2, 3] and YS == [2, 3, 4, 5] and [a for a in XS if a < 0] == [-1], "S2-D2-5 kümeler")
ok(min(a * b for a in XS for b in YS) == -5, "S2-D2-5")
# Ders 3 Soru 2: kontrol a=-1, b=2
ok(abs(-1) + abs(2 - (-1)) - abs(2) == 2 == -2 * (-1), "S2-D3-2 kontrol")
# Ders 3 Soru 4: [-5,3] -> 3-(-5)+1 = 9
ok(tamlar(lambda n: abs(n + 1) <= 4) == list(range(-5, 4)) and 3 - (-5) + 1 == 9, "S2-D3-4")
# Ders 3 Soru 5: iki parça
cozum([x - 2 > 6], "S2-D3-5a", Iv.open(8, oo), lambda q: q - 2 > 6)
cozum([x - 2 < -6], "S2-D3-5b", Iv.open(-oo, -4), lambda q: q - 2 < -6)

# ---------------- ALIŞTIRMA GÖVDESİ (sürüm 2 numaralandırması) ----------------
# Çözümlü (eski no -> yeni): 4->Ç1, 6->Ç2, 8->Ç3, 10->Ç4, 12->Ç5, 14->Ç6, 16->Ç7, 17->Ç8
cozum([(x + 1) / 2 - (x - 3) / 5 < 2], "Ç1", Iv.open(-oo, 3), lambda q: (q + 1) / 2 - (q - 3) / 5 < 2)
ok(sp.expand(10 * ((x + 1) / 2 - (x - 3) / 5)) == 3 * x + 11, "Ç1 10 ile çarpma")
ok(max(tamlar(lambda n: F(n + 1, 2) - F(n - 3, 5) < 2)) == 2, "Ç1 en büyük")
cozum([4 - x >= 2 * x - 11, x > -3], "Ç2", Iv.Lopen(-3, 5), lambda q: 4 - q >= 2 * q - 11 and q > -3)
ok(tamlar(lambda n: 4 - n >= 2 * n - 11 and n > -3) == list(range(-2, 6)) and 5 - (-3) == 8, "Ç2 sayma")
aralik_2(lambda a, b: a + b, (3, 7, False, False), (-2, 4, False, False), (1, 11, False, False), "Ç3 x+y")
aralik_1(lambda t: -t, Iv.open(-2, 4), Iv.open(-4, 2), "Ç3 -y")
aralik_2(lambda a, b: a - b, (3, 7, False, False), (-2, 4, False, False), (-1, 9, False, False), "Ç3 x-y")
XS, YS = [n for n in TAM if -3 < n < 2], [n for n in TAM if -1 < n < 5]
ok(XS == [-2, -1, 0, 1] and YS == [0, 1, 2, 3, 4], "Ç4 kümeler")
V = [a * b for a in XS for b in YS]
ok((min(V), max(V)) == (-8, 4) and (-2) * 4 == -8 and 1 * 4 == 4, "Ç4")
ok(all(abs(a - b) - abs(b) - abs(2 * a) == a for a, b in ornek_al(lambda a, b: a < 0 < b)), "Ç5")
ok(abs(-1 - 2) - abs(2) - abs(-2) == -1, "Ç5 kontrol")
denklem(sp.Abs(x + 2) - sp.Abs(x - 6), sp.FiniteSet(2), "Ç6")
ok(sp.solve(sp.Eq(x + 2, x - 6), x) == [] and F(-2 + 6, 2) == 2 and abs(2 + 2) == abs(2 - 6), "Ç6 adımlar")
ok([n for n in range(-5, 6) if abs(3 * n - 1) >= 8] == [-5, -4, -3, 3, 4, 5] and abs(3 * (-2) - 1) == 7, "Ç7")
ok(F(-7, 3) < -2 and F(-7, 3) > -3, "Ç7 -7/3")
cozum([sp.Abs(x - 3) <= 5, sp.Abs(x - 3) >= 2], "Ç8 çk", sp.Union(Iv(-2, 1), Iv(5, 8)),
      lambda q: 2 <= abs(q - 3) <= 5)
T = tamlar(lambda n: 2 <= abs(n - 3) <= 5)
ok(T == [-2, -1, 0, 1, 5, 6, 7, 8] and len(T) == 8 and sum(T) == 24 and 5 + 6 + 7 + 8 == 26, "Ç8")
# Kendiniz Çözün (yeni no: kaynak): 1:A1, 2:A2, 3:A3, 4:YENİ, 5:A5, 6:A7, 7:A9, 8:A11, 9:YENİ, 10:A13, 11:A15, 12:YENİ
tara(lambda q: -3 <= q < 5, Iv.Ropen(-3, 5), "KÇ1a"); tara(lambda q: q <= 2, Iv(-oo, 2), "KÇ1b")
cozum([5 * x - 3 <= 2 * x + 9], "KÇ2", Iv(-oo, 4), lambda q: 5 * q - 3 <= 2 * q + 9)
cozum([7 - 2 * x > 3 * (x - 1)], "KÇ3", Iv.open(-oo, 2), lambda q: 7 - 2 * q > 3 * (q - 1))
# YENİ KÇ4: -2x+7>=1 -> x<=3 ; doğal sayılar 0,1,2,3
cozum([-2 * x + 7 >= 1], "KÇ4 (yeni)", Iv(-oo, 3), lambda q: -2 * q + 7 >= 1)
ok([n for n in range(0, 500) if -2 * n + 7 >= 1] == [0, 1, 2, 3], "KÇ4 (yeni) doğal sayılar: 4 tane")
cozum([2 * x + 3 > -5, 2 * x + 3 <= 11], "KÇ5", Iv.Lopen(-4, 4), lambda q: -5 < 2 * q + 3 <= 11)
T = tamlar(lambda n: -5 < 2 * n + 3 <= 11); ok(len(T) == 8 and sum(T) == 4, "KÇ5 sayma")
aralik_1(lambda t: 5 - 2 * t, Iv.open(-1, 3), Iv.open(-1, 7), "KÇ6")
ok(sp.imageset(sp.Lambda(x, x ** 2), Iv.open(-4, 3)) == Iv.Ropen(0, 16), "KÇ7")
ok(abs(-6) - abs(4 - 9) + abs(-2) * abs(3) == 7, "KÇ8")
# YENİ KÇ9: x<-1 -> |x+1|+|x-3| = 2-2x
ok(all(abs(t + 1) + abs(t - 3) == 2 - 2 * t for t in IZGARA if t < -1), "KÇ9 (yeni)")
ok(abs(-3 + 1) + abs(-3 - 3) == 8 == 2 - 2 * (-3), "KÇ9 (yeni) örnek x=-3")
denklem(sp.Abs(4 * x - 2) - 10, sp.FiniteSet(-2, 3), "KÇ10")
cozum([sp.Abs(x - 5) < 3], "KÇ11", Iv.open(2, 8), lambda q: abs(q - 5) < 3)
T = tamlar(lambda n: abs(n - 5) < 3); ok(len(T) == 5 and sum(T) == 25, "KÇ11 sayma")
# YENİ KÇ12: |x-a|<=b çözüm kümesi [-1,7] -> a=3, b=4, a*b=12 (tam sayı a, b>0 taraması + sympy)
bulunan = [(A, B) for A in range(-20, 21) for B in range(1, 21)
           if sp.solveset(sp.Abs(x - A) <= B, x, R) == Iv(-1, 7)]
ok(bulunan == [(3, 4)] and 3 * 4 == 12, "KÇ12 (yeni)")
cozum([sp.Abs(x - 3) <= 4], "KÇ12 (yeni) çk", Iv(-1, 7), lambda q: abs(q - 3) <= 4)

# ---------------- KARMA TEKRAR: çözümlü olanların ara adımları ----------------
# K5
ok(sorted({b for a in range(10) for b in range(10) if int(f"3{a}5{b}") % 5 == 0}) == [0, 5], "K5 b")
ok([a for a in range(10) if (8 + a) % 9 == 0] == [1] and [a for a in range(10) if (13 + a) % 9 == 0] == [5], "K5 a")
ok(3150 == 45 * 70 and 3555 == 45 * 79, "K5 sayılar")
ok(sorted(int(f"3{a}5{b}") for a in range(10) for b in range(10) if int(f"3{a}5{b}") % 45 == 0) == [3150, 3555], "K5 brute")
# K6
ok(sp.ilcm(18, 24) == 72 and sp.factorint(18) == {2: 1, 3: 2} and sp.factorint(24) == {2: 3, 3: 1}, "K6 EKOK")
ok(77 == 18 * 4 + 5 == 24 * 3 + 5 and 72 * 0 + 5 < 10, "K6 kontrol")
# K8
ok((1 - F(3, 4), 1 - F(5, 7), 1 - F(7, 9)) == (F(2, 8), F(2, 7), F(2, 9)) and F(2, 9) < F(2, 8) < F(2, 7), "K8 adımlar")
ok((F(3, 4), F(5, 7), F(7, 9)) == (F(189, 252), F(180, 252), F(196, 252)), "K8 kontrol 252")
# K12
ok(tamlar(lambda n: abs(2 * n - 3) <= 5) == [-1, 0, 1, 2, 3, 4], "K12 liste")
# K7 cevap anahtarı yazımı
ok((F(6, 10) + F(4, 10)) / (F(125, 100) - F(75, 100)) == 2 and F(2, 5) == F(4, 10) and F(3, 4) == F(75, 100), "K7 adımlar")

print(f"Tüm kontroller geçti: {GECEN} assert.")
