# MMAT105 Hafta 13 -- Sayı, Kesir ve Yaş Problemleri
# Sunum, ders notu, çözümlü alıştırmalar, "Kendiniz Çözün", "Sınıfta Siz Çözün"
# ve hatırlatma sorularındaki TÜM sayısal cevapların doğrulanması.
# İlke: mümkün olan her yerde brute force (tam sayı taraması) + sağlama;
# yaş sorularında sorudaki her an için yaşların negatif olmadığı kontrol edilir.
from fractions import Fraction as F

sayac = 0
def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1

def tek(liste, beklenen, ad):
    """Taramada tam olarak bir çözüm bulunmalı ve beklenen olmalı."""
    ok(len(liste) == 1 and liste[0] == beklenen, f'{ad}: {liste}')

R = range(-500, 2001)            # sayı problemleri için tarama aralığı
YAS = range(0, 121)              # yaşlar için tarama aralığı
IKI = [(a, b) for a in range(1, 10) for b in range(0, 10)]   # ab, a != 0
def ab(a, b):
    return 10 * a + b

# ---------------- Geçen hafta hatırlatma (12. hafta) ----------------
tek([(a, b) for a in range(0, 49) for b in range(0, 49) if a + b == 48 and 5 * a == 3 * b], (18, 30), 'H1')
ok(F(4 + 7 + 10 + 15, 4) == 9, 'H2')
ok(F(10, 4) * 6 == 15, 'H3')

# =============== SUNUM -- Ders 1: Sayı problemleri ===============
tek([x for x in R if 3*x - 5 == 2*x + 7], 12, 'Ö1')
ok(3*12 - 5 == 31 == 2*12 + 7, 'Ö1 sağlama')
tek([x for x in R if F(x, 2) + F(x, 3) == 35], 42, 'Ö2')
ok(21 + 14 == 35, 'Ö2 sağlama')
tek([x for x in R if 3*(x + 4) == 5*x - 6], 9, 'Ö3')
ok(3*13 == 39 == 5*9 - 6, 'Ö3 sağlama')
tek([(x, y) for x in R for y in range(-100, 101) if x + y == 64 and x - y == 18], (41, 23), 'Ö4')
tek([(x, y) for x in range(0, 97) for y in range(0, 97) if x + y == 96 and 5*x == 3*y], (36, 60), 'Ö5')
tek([(b, k) for k in range(1, 71) for b in range(0, 71) if b + k == 70 and b // k == 4 and b % k == 5], (57, 13), 'Ö6')
t = [x for x in R if x + (x+1) + (x+2) == 87]
ok(t == [28] and t[0] + 2 == 30, 'Ö7')
t = [x for x in R if x % 2 == 0 and x + (x+2) + (x+4) + (x+6) == 100]
ok(t == [22], 'Ö8')
tek([ab(a, b) for a, b in IKI if b != 0 and a + b == 11 and ab(b, a) - ab(a, b) == 27], 47, 'Ö9')
t = [n for n in range(10, 100) if n == 4 * (n // 10 + n % 10)]
ok(t == [12, 24, 36, 48], 'Ö10')
t = [x for x in range(1, 200) if 2*x + 5 == 3*(x - 2)]
ok(t == [11] and 2*11 + 5 == 27, 'Ö11')
tek([(x, y) for x in range(0, 21) for y in range(0, 21) if x + y == 20 and x + 5*y == 68], (8, 12), 'Ö12')
# Ders 1 -- Sınıfta Siz Çözün
tek([x for x in R if 5*x - 8 == 3*x + 12], 10, 'S1-1')
t = [x for x in R if x % 2 == 1 and x + (x+2) + (x+4) == 75]
ok(t == [23] and t[0] + 4 == 27, 'S1-2')
tek([x for x in R if x + 4*x == 50], 10, 'S1-3')
tek([ab(a, b) for a, b in IKI if b != 0 and ab(a, b) + ab(b, a) == 121 and a - b == 5], 83, 'S1-4')
t = [x for x in range(1, 200) if 3*x + 4 == 4*(x - 3)]
ok(t == [16] and 3*16 + 4 == 52, 'S1-5')

# =============== SUNUM -- Ders 2: Kesir problemleri ===============
t = [x for x in range(1, 2000) if F(3, 4) * x == 36]
ok(t == [48] and F(5, 6) * 48 == 40, 'Ö13')
def ardisik_kesir(top, k1, k2):
    h1 = k1 * top; kalan1 = top - h1
    h2 = k2 * kalan1
    return kalan1 - h2
tek([p for p in range(1, 5000) if ardisik_kesir(p, F(2, 5), F(1, 3)) == 120], 300, 'Ö14')
ok(300 - 120 == 180 and 180 - 60 == 120, 'Ö14 sağlama')
tek([p for p in range(1, 10000) if p - F(1, 5)*p - F(1, 3)*p == 1400], 3000, 'Ö15')
ok(3000 - 600 - 1000 == 1400, 'Ö15 sağlama')
tek([p for p in range(1, 5000) if ardisik_kesir(p, F(1, 4), F(2, 5)) == 90], 200, 'Ö16')
ok(200 - 50 == 150 and 150 - 60 == 90, 'Ö16 sağlama')
tek([v for v in range(1, 5000) if F(3, 4)*v + 20 == F(5, 6)*v], 240, 'Ö17')
ok(180 + 20 == 200 == F(5, 6)*240, 'Ö17 sağlama')
tek([v for v in range(1, 5000) if F(2, 3)*v - 30 == F(1, 2)*v], 180, 'Ö18')
t = [n for n in range(1, 1000) if n % 7 == 0 and F(3*n//7 + 4, n + 4) == F(1, 2)]
ok(t == [28], 'Ö19')
t = [n for n in range(1, 1000) if n % 3 == 0 and F(n - n//3 + 6, n) == F(3, 4)]
ok(t == [72] and 72 - 24 + 6 == 54, 'Ö20')
tek([x for x in R if F(2, 3)*x + 4 == F(3, 4)*x - 1], 60, 'Ö21')
ok(40 + 4 == 44 == 45 - 1, 'Ö21 sağlama')
tek([(p, p+5) for p in range(1, 500) if F(p + 3, p + 8) == F(2, 3)], (7, 12), 'Ö22')
tek([h for h in range(1, 5000) if F(2, 5)**2 * h == 8], 50, 'Ö23')
ok(F(2, 5)*50 == 20 and F(2, 5)*20 == 8, 'Ö23 sağlama')
# Ders 2 -- Sınıfta Siz Çözün
t = [x for x in range(1, 2000) if F(2, 7)*x == 18]
ok(t == [63] and F(3, 7)*63 == 27, 'S2-1')
tek([p for p in range(1, 5000) if ardisik_kesir(p, F(1, 3), F(1, 4)) == 60], 120, 'S2-2')
tek([v for v in range(1, 5000) if F(2, 5)*v + 60 == F(2, 3)*v], 225, 'S2-3')
tek([p for p in range(1, 20000) if p - F(1, 4)*p - F(1, 6)*p == 2100], 3600, 'S2-4')
tek([x for x in R if F(3, 5)*x + 2 == F(1, 2)*x + 5], 30, 'S2-5')

# =============== SUNUM -- Ders 3: Yaş problemleri ===============
ok(40 + 3*5 == 55, 'Ö24a')
ok(all((a + 5) - (b + 5) == 10 for a in range(10, 80) for b in [a - 10]), 'Ö24b')
tek([t for t in range(0, 100) if 40 + t == 3*(12 + t)], 2, 'Ö25')
tek([(k, 4*k) for k in YAS if 4*k + 6 == 3*(k + 6)], (12, 48), 'Ö26')
t = [(o, 3*o) for o in YAS if o >= 5 and 3*o - 5 == 4*(o - 5)]
ok(t == [(15, 45)] and 40 == 4*10, 'Ö27')
tek([(a, k) for a in YAS for k in YAS if a + k == 48 and a + 4 == 3*(k + 4)], (38, 10), 'Ö28')
t = [v for v in YAS if v < 24 and (v - (24 - v)) == 12]
ok(t == [18], 'Ö29')
t = [(a, v) for a in YAS for v in YAS if a > v and v - (a - v) == 10 and a + (a - v) == 34]
ok(t == [(26, 18)], 'Ö30')
t = [(2*k, 3*k) for k in range(1, 40) if F(2*k + 4, 3*k + 4) == F(3, 4)]
ok(t == [(8, 12)], 'Ö31')
ok(22*4 + 4*3 == 100 and (22 + 3)*4 == 100, 'Ö32')
t = [k for k in YAS if (k + 4) + (k + 4 + 4) == 48]
ok(t == [18] and 18 + 4 == 22, 'Ö33')
ok(2026 - 1998 == 28 and 1998 - 27 + 60 == 2031, 'Ö34a')
t = [y for y in range(1998, 2100) if (y - 1971) == 2 * (y - 1998)]
ok(t == [2025], 'Ö34b')
# Ders 3 -- Sınıfta Siz Çözün
tek([t for t in range(0, 100) if 42 + t == 2*(12 + t)], 18, 'S3-1')
ok(96 + 5*4 == 116, 'S3-2')
tek([v for v in YAS if v < 30 and v - (30 - v) == 14], 22, 'S3-3')
t = [(3*k, 4*k) for k in range(1, 40) if 3*k >= 5 and F(3*k - 5, 4*k - 5) == F(2, 3)]
ok(t == [(15, 20)], 'S3-4')
ok(2009 + 40 == 2049, 'S3-5')

# =============== DERS NOTU örnekleri ===============
tek([x for x in R if 3*x - 5 == F(x, 2) + 10], 6, 'N1')
ok(all(3*(x + 2) - (3*x + 2) == 4 for x in R), 'N2')
t = [x for x in R if sum(x + i for i in range(5)) == 130]
ok(t == [24] and 24 * 28 == 672, 'N3')
tek([ab(a, b) for a, b in IKI if b != 0 and a + b == 12 and ab(a, b) - ab(b, a) == 36], 84, 'N4')
tek([n for n in range(10, 100) if (10*n + 3) - n == 444], 49, 'N5')
tek([(o, m) for o in range(0, 31) for m in range(0, 31) if o + m == 30 and 4*o + 2*m == 100], (20, 10), 'N6')
t = [x for x in range(1, 200) if 2*x + 6 == 3*(x - 2)]
ok(t == [12] and 2*12 + 6 == 30, 'N7')
t = [n for n in range(1, 1000) if n % 6 == 0 and n // 2 - n // 3 == 6]
ok(t == [36], 'N8')
tek([p for p in range(1, 10000) if ardisik_kesir(p, F(1, 4), F(1, 3)) == 100], 200, 'N9')
tek([h for h in range(1, 5000) if F(3, 4)**2 * h == 18], 32, 'N10')
ok(F(3, 4)*32 == 24 and F(3, 4)*24 == 18, 'N10 sağlama')
tek([v for v in range(1, 5000) if F(3, 8)*v + 45 == F(1, 2)*v], 360, 'N11')
tek([L for L in range(1, 5000) if F(L, 2) - F(L - F(L, 6), 2) == 5], 60, 'N12')
tek([(p, 36 - p) for p in range(1, 36) if F(p - 2, 36 - p + 2) == F(1, 3)], (11, 25), 'N13')
t = [s for s in range(0, 100) if 3*s + 2 == 2*(s + 3*2)]
ok(t == [10] and 3*10 == 30, 'N14')
ok((18 + 3 + 2)*4 == 92, 'N15')
t = [(d, 5*d) for d in range(1, 40) if 5*d + 8 == 6*d]
ok(t == [(8, 40)], 'N16')
tek([(d, t_) for d in YAS for t_ in YAS if d == 12*t_ and d + t_ == 65], (60, 5), 'N17')
t = [(c, e) for c in YAS for e in YAS if c > e and e - (c - e) == 6 and c + (c - e) == 30]
ok(t == [(22, 14)], 'N18')
t = [y for y in range(2004, 2100) if (y - 1978) == 3 * (y - 2004)]
ok(t == [2017], 'N19')
ok(5*24 == 120 and (25 + 3)*6 - 3*6 == 150 and 150 - 120 == 30, 'N20')

# =============== ÇÖZÜMLÜ ALIŞTIRMALAR ===============
tek([x for x in R if x % 2 == 0 and 3*x + 6 == 138], 44, 'A1')
tek([(b, k) for k in range(1, 86) for b in range(0, 86) if b + k == 85 and b // k == 3 and b % k == 9], (66, 19), 'A2')
tek([ab(a, b) for a, b in IKI if b != 0 and a + b == 9 and ab(a, b) - ab(b, a) == 45], 72, 'A3')
tek([p for p in range(1, 10000) if ardisik_kesir(p, F(3, 8), F(2, 5)) == 180], 480, 'A4')
tek([v for v in range(1, 5000) if F(1, 3)*v + 50 == F(3, 4)*v], 120, 'A5')
tek([(b, k) for b in YAS for k in YAS if b + k == 30 and k >= 5 and b - 5 == 3*(k - 5)], (20, 10), 'A6')
tek([t for t in range(0, 100) if 46 + t == (14 + 10 + 6) + 3*t], 8, 'A7')
t = [o for o in YAS if o < 32 and o - (32 - o) == 20]
ok(t == [26] and 32 + (32 - 26) == 38, 'A8')

# =============== KENDİNİZ ÇÖZÜN ===============
tek([x for x in R if 4*x + 7 == 43], 9, 'K1')
tek([x for x in R if 5*(x - 3) == 2*x + 6], 7, 'K2')
tek([(x, y) for x in R for y in range(-100, 200) if x + y == 75 and x - y == 21], (48, 27), 'K3')
t = [x for x in R if x % 2 == 1 and sum(x + 2*i for i in range(5)) == 115]
ok(t == [19] and 19 + 8 == 27, 'K4')
tek([ab(a, b) for a, b in IKI if b != 0 and ab(a, b) + ab(b, a) == 154 and a - b == 2], 86, 'K5')
t = [x for x in range(1, 200) if 4*(x - 2) == 3*x + 5]
ok(t == [13] and 3*13 + 5 == 44, 'K6')
t = [x for x in range(1, 2000) if F(3, 5)*x == 27]
ok(t == [45] and F(2, 9)*45 == 10, 'K7')
tek([p for p in range(1, 5000) if ardisik_kesir(p, F(1, 6), F(2, 5)) == 90], 180, 'K8')
tek([v for v in range(1, 5000) if F(5, 8)*v - 36 == F(1, 4)*v], 96, 'K9')
tek([x for x in R if F(3, 4)*x - 2 == F(2, 3)*x + 1], 36, 'K10')
tek([t for t in range(0, 100) if 34 + t == 4*(7 + t)], 2, 'K11')
ok(6*20 - 6*5 == 90 and 7 >= 5, 'K12')
t = [5*x for x in YAS if 5*x + 3 == 4*(x + 3)]
ok(t == [45], 'K13')
t = [e for e in YAS if (e + 6) + (e + 12) == 50]
ok(t == [16], 'K14')
t = [y for y in range(2019, 2100) if (y - 1992) == 4 * (y - 2019)]
ok(t == [2028], 'K15')

print(f'Tüm kontroller geçti: {sayac} assert')
