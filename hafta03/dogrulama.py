#!/usr/bin/env python3
"""MMAT105 Hafta 3 -- sunum ve ders notundaki tüm sayısal cevapların doğrulaması.
Mümkün olan her yerde kaba kuvvet (tarama) kullanılır."""
from math import gcd
from functools import reduce

sayac = 0


def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1


def ebob(*s):
    return reduce(gcd, s)


def ekok(*s):
    return reduce(lambda a, b: a * b // gcd(a, b), s)


def sayi(desen, **r):
    """desen: '3a5b' gibi; harfler rakamlarla doldurulur."""
    return int("".join(str(r[c]) if c.isalpha() else c for c in desen))


def tara(desen, kosul):
    """Desendeki harfler için tüm rakam atamalarını tarar; ilk rakam 0 olamaz.
    Koşulu sağlayan atamaları (sözlük) listeler."""
    harfler = sorted(set(c for c in desen if c.isalpha()))
    from itertools import product
    sonuc = []
    for deg in product(range(10), repeat=len(harfler)):
        r = dict(zip(harfler, deg))
        s = "".join(str(r[c]) if c.isalpha() else c for c in desen)
        if s[0] == "0":
            continue
        if kosul(int(s)):
            sonuc.append(r)
    return sonuc


def bolen_sayisi(n):
    return sum(1 for d in range(1, n + 1) if n % d == 0)


def kural11(n):
    """Sağdan +-+- toplamı."""
    rs = [int(c) for c in str(n)][::-1]
    return sum(d if i % 2 == 0 else -d for i, d in enumerate(rs))


# ================= SUNUM =================
# Geçen hafta hatırlatma
ok(2**3 * 3**2 * 5 == 360, "H1")
ok(bolen_sayisi(360) == 24, "H2")
ok(7 * 12 + 5 == 89 and 89 // 7 == 12 and 89 % 7 == 5, "H3")

# Örnek 1: 47a, 2 ile bölünür, 5 ile bölünmez
r = tara("47a", lambda n: n % 2 == 0 and n % 5 != 0)
ok(sorted(x["a"] for x in r) == [2, 4, 6, 8], "S1")
# Örnek 2: 5a72, 3
r = tara("5a72", lambda n: n % 3 == 0)
ok(sorted(x["a"] for x in r) == [1, 4, 7] and sum(x["a"] for x in r) == 12, "S2")
# Örnek 3: 6a3, 9
r = tara("6a3", lambda n: n % 9 == 0)
ok(sorted(x["a"] for x in r) == [0, 9] and 603 == 9 * 67 and 693 == 9 * 77, "S3")
# Örnek 4
ok(sum(map(int, "4738526")) == 35 and 4738526 % 9 == 8 and 4738526 % 3 == 2, "S4")
# Örnek 5: 2a7, 9 ile kalan 4
r = tara("2a7", lambda n: n % 9 == 4)
ok([x["a"] for x in r] == [4] and 247 == 9 * 27 + 4, "S5")
# Örnek 6: 35a6, 4
r = tara("35a6", lambda n: n % 4 == 0)
ok(sorted(x["a"] for x in r) == [1, 3, 5, 7, 9], "S6")
# Örnek 7
ok(7253164 % 4 == 0 and 7253164 % 8 == 4 and 164 == 8 * 20 + 4, "S7")
# Örnek 8: 7a42, 11
r = tara("7a42", lambda n: n % 11 == 0)
ok([x["a"] for x in r] == [9] and 7942 == 11 * 722 and kural11(7942) == 0, "S8")
# Örnek 9
ok(kural11(3052) == -6 and 3052 % 11 == 5 and 3052 == 11 * 277 + 5, "S9")
# Örnek 10: 3a5b, 5 ve 9
r = tara("3a5b", lambda n: n % 5 == 0 and n % 9 == 0)
ok(sorted(x["a"] for x in r) == [1, 5] and sum(x["a"] for x in r) == 6, "S10")
ok(sorted(sayi("3a5b", **x) for x in r) == [3150, 3555], "S10b")
# Örnek 11: 4ab, 10 ile bölünür, 3 ile kalan 2
r = tara("4ab", lambda n: n % 10 == 0 and n % 3 == 2)
ok(sorted(x["a"] for x in r) == [1, 4, 7], "S11")
# Ders 1 siz çözün
ok(sorted(x["a"] for x in tara("7a4", lambda n: n % 3 == 0)) == [1, 4, 7], "D1-1")
ok(58347 % 9 == 0, "D1-2")
ok(2358614 % 8 == 6, "D1-3")
ok([x["a"] for x in tara("3a52", lambda n: n % 11 == 0)] == [6], "D1-4")
ok(4173 % 11 == 4 and kural11(4173) == -7, "D1-5")

# Örnek 12: 30 ve 12 tuzağı; 18 örneği
ok(30 % 2 == 0 and 30 % 6 == 0 and 30 % 12 == 6 and 30 % 4 != 0, "S12")
ok(18 % 2 == 0 and 18 % 6 == 0 and 18 % 12 != 0, "S12b")
# Örnek 13: 5a4, 6
r = tara("5a4", lambda n: n % 6 == 0)
ok(sorted(x["a"] for x in r) == [0, 3, 6, 9] and sum(x["a"] for x in r) == 18, "S13")
# Örnek 14: 2a5, 6 ile kalan 1
r = tara("2a5", lambda n: n % 6 == 1)
ok(sorted(x["a"] for x in r) == [0, 3, 6, 9] and 205 == 6 * 34 + 1, "S14")
# Örnek 15: 41a8, 12
r = tara("41a8", lambda n: n % 12 == 0)
ok(sorted(x["a"] for x in r) == [2, 8] and 4128 % 12 == 0 and 4188 % 12 == 0, "S15")
# Örnek 16: 2a4b, 15, max a+b
r = tara("2a4b", lambda n: n % 15 == 0)
ok(max(x["a"] + x["b"] for x in r) == 12 and 2745 == 15 * 183, "S16")
ok(max(x["a"] + x["b"] for x in r if x["b"] == 0) == 9, "S16b")
# Örnek 17: a37b, 45
r = tara("a37b", lambda n: n % 45 == 0)
ok(sorted(x["a"] for x in r) == [3, 8] and sorted(sayi("a37b", **x) for x in r) == [3375, 8370], "S17")
# Örnek 18: 5a3b, 36
r = tara("5a3b", lambda n: n % 36 == 0)
ok(sorted(sayi("5a3b", **x) for x in r) == [5436, 5832], "S18")
# Örnek 19: a1b6, 72
r = tara("a1b6", lambda n: n % 72 == 0)
ok(sorted(sayi("a1b6", **x) for x in r) == [4176, 8136] and {x["a"] + x["b"] for x in r} == {11}, "S19")
ok([k for k in range(100, 200) if k % 8 == 0 and k % 10 == 6 and k // 100 == 1] == [136, 176], "S19b")
# Örnek 20-22
ok(ebob(24, 36) == 12 and 24 == 2**3 * 3 and 36 == 2**2 * 3**2, "S20")
ok(ebob(84, 126, 210) == 42, "S21")
ok(ebob(2**3 * 3**2 * 5, 2**2 * 3**4 * 7) == 36, "S22")
# Ders 2 siz çözün
ok(len(tara("8a6", lambda n: n % 6 == 0)) == 3, "D2-1")
r = tara("a2b", lambda n: n % 18 == 0)
ok(max(x["a"] + x["b"] for x in r) == 16 and 828 % 18 == 0, "D2-2")
ok(ebob(60, 90) == 30, "D2-3")
ok(ebob(48, 72, 120) == 24, "D2-4")
ok(ebob(2**4 * 3 * 5**2, 2**2 * 3**3 * 7) == 12, "D2-5")

# Örnek 23-24
ok(ekok(12, 18) == 36, "S23")
ok(ekok(8, 12, 15) == 120, "S24")
# EBOB·EKOK uyarısı (2,4,8)
ok(ebob(2, 4, 8) * ekok(2, 4, 8) == 16 and 2 * 4 * 8 == 64, "U1")
ok(ebob(8, 15) == 1, "U2")
# Örnek 25: çarpım 540, EBOB 6
ok(540 // 6 == 90 and ebob(6, 90) == 6 and ekok(6, 90) == 90, "S25")
# Çarpımı 540, EBOB'u 6 olan her çift için EKOK = 90
ciftler = [(a, 540 // a) for a in range(1, 541) if 540 % a == 0 and ebob(a, 540 // a) == 6]
ok(ciftler and all(ekok(a, b) == 90 for a, b in ciftler), "S25b")
# Örnek 26
ok(12 * 180 // 36 == 60 and ebob(36, 60) == 12 and ekok(36, 60) == 180, "S26")
# Örnek 27: aralarında asal, EKOK 72, min a+b
r = [(a, b) for a in range(1, 73) for b in range(1, 73) if ebob(a, b) == 1 and ekok(a, b) == 72]
ok(min(a + b for a, b in r) == 17 and {frozenset(p) for p in r} == {frozenset({1, 72}), frozenset({8, 9})}, "S27")
# Örnek 28: teller (brute force: parça uzunluğu L tüm telleri bölmeli, parça sayısı en az)
L = max(d for d in range(1, 73) if 72 % d == 0 and 96 % d == 0 and 120 % d == 0)
ok(L == 24 and 72 // L + 96 // L + 120 // L == 12, "S28")
# Örnek 29
k = ebob(180, 240)
ok(k == 60 and (180 // k) * (240 // k) == 12, "S29")
# Örnek 30: kapalı çevre
k = ebob(90, 150)
ok(k == 30 and 2 * (90 + 150) // k == 16, "S30")
# Kenar kenar sayım: köşeler bir kez
ok(2 * (90 // k) + 2 * (150 // k) == 16, "S30b")
# Örnek 31
ok(ekok(12, 18, 30) == 180, "S31")
# Örnek 32: en küçük x>1, x%4=x%5=x%6=1
ok(next(x for x in range(2, 10**4) if x % 4 == 1 and x % 5 == 1 and x % 6 == 1) == 61, "S32")
# Örnek 33
ok(next(x for x in range(1, 10**4) if x % 6 == 5 and x % 8 == 7 and x % 9 == 8) == 71, "S33")
# Örnek 34
ok(next(x for x in range(100, 1000) if x % 4 == 3 and x % 6 == 3 and x % 10 == 3) == 123, "S34")
# Ders 3 siz çözün
ok(ekok(18, 24) == 72, "D3-1")
ok(4 * 120 // 24 == 20 and ebob(24, 20) == 4 and ekok(24, 20) == 120, "D3-2")
ok(ebob(60, 84) == 12 and 60 // 12 + 84 // 12 == 12, "D3-3")
ok(ekok(15, 20) == 60, "D3-4")  # 08:00 + 60 dk = 09:00
ok(next(x for x in range(100, 1000) if x % 3 == 2 and x % 4 == 2 and x % 5 == 2) == 122, "D3-5")

# ================= DERS NOTU =================
# Ö1: a3b, 10 ve 3
r = tara("a3b", lambda n: n % 10 == 0 and n % 3 == 0)
ok(sorted(x["a"] for x in r) == [3, 6, 9], "N1")
# Ö2
ok(sum(map(int, "7256814")) == 33 and 7256814 % 3 == 0 and 7256814 % 9 == 6, "N2")
# Ö3: 4a3b, 9 -> a+b değerleri
r = tara("4a3b", lambda n: n % 9 == 0)
ok({x["a"] + x["b"] for x in r} == {2, 11}, "N3")
# Ö4: 12a4, 8
r = tara("12a4", lambda n: n % 8 == 0)
ok(sorted(x["a"] for x in r) == [2, 6] and 1224 == 8 * 153 and 1264 == 8 * 158, "N4")
# Ö5: 5a17, 11 ile kalan 3
r = tara("5a17", lambda n: n % 11 == 3)
ok([x["a"] for x in r] == [2] and 5217 == 11 * 474 + 3, "N5")
# Ö6: a5b, 12 -> kaç sayı
r = tara("a5b", lambda n: n % 12 == 0)
ok(sorted(sayi("a5b", **x) for x in r) == [156, 252, 456, 552, 756, 852], "N6")
# Ö7: 3a16, 24
r = tara("3a16", lambda n: n % 24 == 0)
ok(sorted(x["a"] for x in r) == [2, 8] and 3216 == 24 * 134 and 3816 == 24 * 159, "N7")
ok([a for a in range(10) if (100 * a + 16) % 8 == 0] == [0, 2, 4, 6, 8], "N7b")
# Ö8
ok(ebob(90, 120, 150) == 30, "N8")
# Ö9
e = ebob(2**5 * 3**2 * 7, 2**3 * 3**4 * 5)
ok(e == 72 and bolen_sayisi(e) == 12, "N9")
# Ö10
ok(ekok(20, 24, 30) == 120, "N10")
# Ö11
ok(8 * 96 // 32 == 24 and ebob(32, 24) == 8 and ekok(32, 24) == 96, "N11")
# Ö12: EBOB 6, a+b=48, sıralı ikili sayısı
r = [(a, 48 - a) for a in range(1, 48) if ebob(a, 48 - a) == 6]
ok(r == [(6, 42), (18, 30), (30, 18), (42, 6)], "N12")
# Ö13
k = ebob(150, 210, 270)
ok(k == 30 and 150 // k + 210 // k + 270 // k == 21, "N13")
# Ö14: 24x36 kartonlardan en küçük kare (brute force kenar)
s = next(s for s in range(1, 1000) if s % 24 == 0 and s % 36 == 0)
ok(s == 72 and (s // 24) * (s // 36) == 6, "N14")
# Ö15
k = ebob(42, 56, 70)
ok(k == 14 and (42 + 56 + 70) // k == 12 and 42 // k + 56 // k + 70 // k == 12, "N15")
# Ö16
ok(next(x for x in range(1, 10**4) if x % 5 == 3 and x % 6 == 4 and x % 8 == 6) == 118, "N16")
# Ö17: 50<x<100, 6,9,12 ile hep 2 kalan (tek çözüm)
r = [x for x in range(51, 100) if x % 6 == 2 and x % 9 == 2 and x % 12 == 2]
ok(r == [74], "N17")

# ---- Alıştırmalar ----
r = tara("5a8", lambda n: n % 3 == 0)
ok(sum(x["a"] for x in r) == 15, "A1")
ok(9876543 % 9 == 6 and 9876543 % 5 == 3 and sum(map(int, "9876543")) == 42, "A2")
ok(sorted(x["a"] for x in tara("24a", lambda n: n % 4 == 0)) == [0, 4, 8], "A3")
ok(3125764 % 8 == 4, "A4")
ok([x["a"] for x in tara("6a3", lambda n: n % 11 == 0)] == [9] and 693 == 11 * 63, "A5")
r = tara("2a5b", lambda n: n % 5 == 0 and n % 9 == 0)
ok(max(x["a"] for x in r) == 6, "A6")
r = tara("a4b", lambda n: n % 6 == 0)
ok(max(sayi("a4b", **x) for x in r) == 948, "A7")
r = tara("3a4b", lambda n: n % 36 == 0)
ok(sorted(sayi("3a4b", **x) for x in r) == [3240, 3348, 3744], "A8")
r = tara("a1b", lambda n: n % 45 == 0)
ok(sorted(sayi("a1b", **x) for x in r) == [315, 810] and 315 + 810 == 1125, "A9")
ok(ebob(72, 108) == 36 and ekok(72, 108) == 216, "A10")
A, B = 2**3 * 3**2 * 5, 2 * 3**3 * 5**2
ok(ebob(A, B) == 90 and ekok(A, B) == 5400, "A11")
ok(9 * 270 // 54 == 45 and ebob(54, 45) == 9 and ekok(54, 45) == 270, "A12")
r = [(a, 90 // a) for a in range(1, 91) if 90 % a == 0 and ebob(a, 90 // a) == 1]
ok(min(a + b for a, b in r) == 19, "A13")
k = ebob(150, 210)
ok(k == 30 and (150 // k) * (210 // k) == 35, "A14")
k = ebob(96, 120)
ok(k == 24 and 2 * (96 + 120) == 432 and 432 // k == 18, "A15")
s = ekok(15, 20)
ok(s == 60 and (s // 15) * (s // 20) == 12, "A16")
ok(ekok(20, 30, 45) == 180, "A17")  # 07:15 + 3 saat = 10:15
ok(next(x for x in range(100, 1000) if x % 4 == 2 and x % 6 == 4 and x % 9 == 7) == 106, "A18")

# Kural kutusu kontrolleri: 11 kuralı ve kalan kuralları (1..20000 tarama)
for n in range(1, 20001):
    ok(n % 11 == kural11(n) % 11, "K11")
    ok(n % 9 == sum(map(int, str(n))) % 9 and n % 3 == sum(map(int, str(n))) % 3, "K39")
    ok(n % 4 == (n % 100) % 4 and n % 8 == (n % 1000) % 8, "K48")
    ok(n % 5 == (n % 10) % 5 and n % 2 == (n % 10) % 2, "K25")
# Bileşik bölünebilme ayrıştırmaları: n, a ve b ile bölünür <=> n, a*b ile bölünür
for a, b in [(2, 3), (3, 4), (3, 5), (2, 9), (3, 8), (4, 9), (5, 9), (8, 9)]:
    ok(ebob(a, b) == 1, "aralarinda asal")
    for n in range(1, 5000):
        ok((n % a == 0 and n % b == 0) == (n % (a * b) == 0), "bilesik")
# EBOB*EKOK = a*b (iki sayı)
for a in range(1, 200):
    for b in range(1, 200):
        ok(ebob(a, b) * ekok(a, b) == a * b, "EBOBEKOK")

# ================= SÜRÜM 2 EKLERİ =================
# ---- Sunum: yıldızlı Sınıfta Siz Çözün çözüm adımları ----
# D1-1: 11+a in {12,15,18}
ok([s for s in range(11, 21) if s % 3 == 0] == [12, 15, 18] and 714 % 3 == 0 and 744 % 3 == 0 and 774 % 3 == 0, "D1-1 adim")
# D1-4: a-6 in [-6,3], tek 11 katı 0; 3652 = 11*332
ok([v for v in range(-6, 4) if v % 11 == 0] == [0] and kural11(3652) == 0 and 3652 == 11 * 332, "D1-4 adim")
# D1-5: sağdan toplam -7, -7+11=4; 4173 = 11*379+4
ok(kural11(4173) == -7 and -7 + 11 == 4 and 4173 == 11 * 379 + 4, "D1-5 adim")
# D2-2: a+b+2 in {9,18}; a+b=16 ve b çift -> (8,8)
ok([s for s in range(1, 21) if s % 9 == 0] == [9, 18], "D2-2 adim")
ok([(a, 16 - a) for a in range(1, 10) if 0 <= 16 - a <= 9 and (16 - a) % 2 == 0] == [(8, 8)] and 828 == 18 * 46, "D2-2 adim2")
# D2-4: ortak bölme tablosu
ok((48 // 8, 72 // 8, 120 // 8) == (6, 9, 15) and (6 // 3, 9 // 3, 15 // 3) == (2, 3, 5) and ebob(2, 3, 5) == 1 and 2 * 2 * 2 * 3 == 24, "D2-4 adim")
# D2-5: 2^2*3
ok(2**min(4, 2) * 3**min(1, 3) == 12, "D2-5 adim")
# D3-2
ok(24 * 20 == 4 * 120 == 480 and ebob(24, 20) == 4 and ekok(24, 20) == 120 and 2**3 * 3 * 5 == 120, "D3-2 adim")
# D3-3
ok(60 == 2**2 * 3 * 5 and 84 == 2**2 * 3 * 7 and 60 // 12 == 5 and 84 // 12 == 7, "D3-3 adim")
# D3-5: 60k+2
ok(ekok(3, 4, 5) == 60 and [60 * k + 2 for k in range(1, 3)] == [62, 122], "D3-5 adim")

# ---- Ders notu: Çözümlü alıştırmalar (adımlar) ----
# Ç1 (eski A5): 9-a in [0,9]
ok([a for a in range(10) if (9 - a) % 11 == 0] == [9] and kural11(693) == 0, "C1")
# Ç2 (eski A6): 2250, 2655
r = tara("2a5b", lambda n: n % 5 == 0 and n % 9 == 0)
ok(sorted(sayi("2a5b", **x) for x in r) == [2250, 2655] and 2655 == 5 * 531 == 9 * 295, "C2")
# Ç3 (eski A8)
ok(3240 == 36 * 90 and 3348 == 36 * 93 and 3744 == 36 * 104, "C3")
ok(sorted(x["b"] for x in tara("4b", lambda n: n % 4 == 0)) == [0, 4, 8], "C3 b")
# Ç4 (eski A11)
A, B = 2**3 * 3**2 * 5, 2 * 3**3 * 5**2
ok(A == 360 and B == 1350 and ebob(A, B) == 90 and ekok(A, B) == 5400 and 90 * 5400 == 486000 == A * B and 8 * 27 * 25 == 5400, "C4")
# Ç5 (eski A13): tüm aralarında asal ikililer ve toplamlar
r = sorted({tuple(sorted((a, 90 // a))) for a in range(1, 91) if 90 % a == 0 and ebob(a, 90 // a) == 1})
ok(r == [(1, 90), (2, 45), (5, 18), (9, 10)] and [a + b for a, b in r] == [91, 47, 23, 19], "C5")
ok(6 * 15 == 90 and ebob(6, 15) == 3, "C5 tuzak")
# Ç6 (eski A15)
ok(96 == 2**5 * 3 and 120 == 2**3 * 3 * 5 and ebob(96, 120) == 24 and 2 * (96 // 24 + 120 // 24) == 18, "C6")
# Ç7 (eski A17): 07:15 + 180 dk = 10:15
t = 7 * 60 + 15 + ekok(20, 30, 45)
ok(ekok(20, 30, 45) == 2**2 * 3**2 * 5 == 180 and (t // 60, t % 60) == (10, 15), "C7")
# Ç8 (eski A18)
ok([36 * k - 2 for k in range(1, 4)] == [34, 70, 106] and 106 == 4 * 26 + 2 == 6 * 17 + 4 == 9 * 11 + 7, "C8")

# ---- Kendiniz çözün: yeni sorular ----
# K11: a<b, EBOB 4, EKOK 60 -> 2 ikili (brute force)
r = [(a, b) for a in range(1, 61) for b in range(a + 1, 61) if ebob(a, b) == 4 and ekok(a, b) == 60]
ok(r == [(4, 60), (12, 20)], "K11 yeni")
# K12: 8,12,15 ile hep 3 artan, 200'den az, en çok
r = [x for x in range(0, 200) if x % 8 == 3 and x % 12 == 3 and x % 15 == 3]
ok(r == [3, 123] and max(r) == 123 and ekok(8, 12, 15) == 120, "K12 yeni")
# Ders 3 SSÇ-4: 08:00 + 60 dk
ok(8 * 60 + ekok(15, 20) == 9 * 60, "D3-4 saat")

print(f"Tüm kontroller geçti: {sayac} assert.")
