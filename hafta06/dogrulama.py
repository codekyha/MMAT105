#!/usr/bin/env python3
"""MMAT105 Hafta 6 -- sunum ve ders notundaki tüm sayısal cevapların doğrulaması."""
from fractions import Fraction as F
from sympy import symbols, Eq, solve, Rational, linsolve

x, y, z, k, m, a, b = symbols('x y z k m a b')
N = 0


def ok(cond, msg):
    global N
    assert cond, msg
    N += 1


def coz(e1, e2, beklenen, msg):
    """İki denklemli sistemin tek çözümünü sympy ile bul, beklenenle karşılaştır."""
    s = solve([e1, e2], [x, y], dict=True)
    ok(len(s) == 1, msg + ': tek çözüm yok')
    ok((s[0][x], s[0][y]) == tuple(Rational(v) for v in beklenen), f"{msg}: {s}")
    return s[0][x], s[0][y]


def durum(a1, b1, c1, a2, b2, c2):
    """a1x+b1y=c1, a2x+b2y=c2 sisteminin çözüm sayısı: 'tek', 'yok', 'sonsuz'."""
    s = linsolve([a1*x + b1*y - c1, a2*x + b2*y - c2], [x, y])
    if s == set() or len(s) == 0:
        return 'yok'
    sol = list(s)[0]
    return 'tek' if not any(e.free_symbols for e in sol) else 'sonsuz'


def dogal_sayac(f, lim=200):
    return sum(1 for X in range(lim) for Y in range(lim) if f(X, Y))


def sayi_bul(kosul):
    return [10*A + B for A in range(1, 10) for B in range(10) if kosul(A, B)]

# ---------------- SUNUM: Geçen hafta ----------------
ok(solve(Eq(3*(x-2)+5, 2*x+7), x) == [8], "H1")
ok(solve(Eq(x/2 + x/3, 10), x) == [12], "H2")
ok(solve(Eq(3*x+4, 5*x-6), x) == [5], "H3")

# ---------------- SUNUM: Ders 1 ----------------
for X, Y in [(0, 7), (1, 5), (2, 3)]:
    ok(2*X + Y == 7, "S1")
ok(2*3 + 2 != 7 and 2*3 + 2 == 8, "S1 (3,2)")
sag = [p for p in [(3, -1), (-2, 4), (1, 2)] if 3*p[0] + 2*p[1] - 7 == 0]
ok(sag == [(3, -1), (1, 2)], "S2")
ok(3*(-2) + 2*4 - 7 == -5, "S2 deger")
ok(solve(Eq(5*2 - 3*k, 1), k) == [3], "S3")
ok(solve(Eq(4*a - (a+1), 8), a) == [3], "S4")
ok(dogal_sayac(lambda X, Y: 2*X + 3*Y == 24) == 5, "S5")
ok(sorted([(X, Y) for X in range(30) for Y in range(30) if 2*X+3*Y == 24]) == [(0, 8), (3, 6), (6, 4), (9, 2), (12, 0)], "S5 liste")
coz(Eq(x+y, 12), Eq(x-y, 4), (8, 4), "S6")
coz(Eq(2*x+3*y, 13), Eq(2*x-y, 1), (2, 3), "S7")
coz(Eq(3*x+2*y, 16), Eq(x-2*y, 0), (4, 2), "S8")
coz(Eq(3*x+4*y, 10), Eq(2*x-3*y, 1), (2, 1), "S9")
coz(Eq(5*x+2*y, 4), Eq(3*x-4*y, 18), (2, -3), "S10")
coz(Eq(2*(x+1)-y, 5), Eq(x+3*(y-2), -1), (2, 1), "S11")
X, Y = coz(Eq(4*x-3*y, -1), Eq(6*x+5*y, 27), (2, 3), "S12")
ok(X*Y == 6, "S12 xy")
# Ders 1 sınıfta
ok(solve(Eq(3*(-1) + 2*m, 5), m) == [4], "D1-1")
coz(Eq(x+y, 9), Eq(x-y, 3), (6, 3), "D1-2")
coz(Eq(3*x-y, 7), Eq(x+y, 5), (3, 2), "D1-3")
coz(Eq(2*x+5*y, 1), Eq(3*x-2*y, 11), (3, -1), "D1-4")
ok(dogal_sayac(lambda X, Y: X + 2*Y == 10) == 6, "D1-5")

# ---------------- SUNUM: Ders 2 ----------------
coz(Eq(y, 2*x-1), Eq(3*x+2*y, 12), (2, 3), "S13")
coz(Eq(x-3*y, 1), Eq(2*x-5*y, 4), (7, 2), "S14")
X, Y = coz(Eq(x, 2*y), Eq(3*x+y, 21), (6, 3), "S15")
ok(X + Y == 9, "S15 x+y")
coz(Eq(x/2 + y/3, 4), Eq(x/4 - y/6, 0), (4, 6), "S16")
coz(Eq(Rational('0.2')*x + Rational('0.5')*y, Rational('1.9')),
    Eq(Rational('0.3')*x - Rational('0.1')*y, Rational('0.3')), (2, 3), "S17")
X, Y = coz(Eq(3*x+2*y, 12), Eq(2*x+3*y, 13), (2, 3), "S18")
ok(X + Y == 5 and X - Y == -1, "S18 x+y, x-y")
X, Y = coz(Eq(7*x+4*y, 37), Eq(4*x+7*y, 40), (3, 4), "S19")
ok(X + Y == 7 and X - Y == -1 and X*Y == 12, "S19")
X, Y = coz(Eq(2*x+y, 11), Eq(x+2*y, 7), (5, 1), "S20")
ok(X + Y == 6 and X - Y == 4, "S20")
X, Y = coz(Eq(x+y, 8), Eq(x-y, 2), (5, 3), "S21")
ok(X*Y == 15 and F(int(X), int(Y)) == F(5, 3), "S21")
ok(durum(2, -3, 5, 4, -6, 10) == 'sonsuz', "S22a")
ok(durum(2, -3, 5, 4, -6, 7) == 'yok', "S22b")
ok(durum(2, -3, 5, 1, 1, 5) == 'tek', "S22c")
coz(Eq(2*x-3*y, 5), Eq(x+y, 5), (4, 1), "S22c çözüm")
# Grafik çerçevesi
coz(Eq(x+y, 4), Eq(x-y, 2), (3, 1), "Grafik kesisen")
ok(durum(1, 1, 4, 1, 1, 1) == 'yok' and durum(1, 1, 4, 2, 2, 8) == 'sonsuz', "Grafik")
# S23: çözüm yoksa m
ok([M for M in range(-50, 51) if durum(3, M, 5, 6, 4, 7) == 'yok'] == [2], "S23")
# S24: sonsuz çözüm -> a=-6, b=-9
ok([(A, B) for A in range(-30, 31) for B in range(-30, 31) if durum(2, -1, 3, A, 3, B) == 'sonsuz'] == [(-6, -9)], "S24")
ok(-6 + -9 == -15, "S24 a+b")
# S25: tek çözüm değilse m=7; m=7 için çözüm yok
ok([M for M in range(-50, 51) if durum(M-1, 2, 4, 3, 1, 5) != 'tek'] == [7], "S25")
ok(durum(6, 2, 4, 3, 1, 5) == 'yok', "S25 m=7")
# S26
ok([K for K in range(-50, 51) if durum(1, 2, 5, 3, K, 15) == 'sonsuz'] == [6], "S26")
ok(1 + 2*2 == 5 and 3*1 + 6*2 == 15, "S26 (1,2)")
# Ders 2 sınıfta
coz(Eq(y, x+2), Eq(2*x+y, 11), (3, 5), "D2-1")
X, Y = coz(Eq(5*x+3*y, 21), Eq(3*x+5*y, 19), (3, 2), "D2-2")
ok(X + Y == 5 and X - Y == 1, "D2-2")
coz(Eq(x/3 + y/2, 3), Eq(x-y, -1), (3, 4), "D2-3")
ok([K for K in range(-50, 51) if durum(4, K, 3, 2, 3, 5) == 'yok'] == [6], "D2-4")
ok(durum(1, -2, 1, 3, -6, 3) == 'sonsuz', "D2-5")

# ---------------- SUNUM: Ders 3 ----------------
coz(Eq(x+y, 50), Eq(x-y, 14), (32, 18), "S27")
coz(Eq(x, 3*y+4), Eq(x+y, 44), (34, 10), "S28")
coz(Eq(x+y, 17), Eq(5*x+10*y, 120), (10, 7), "S29")
coz(Eq(x+y, 30), Eq(40*x+70*y, 1560), (18, 12), "S30")
X, Y = coz(Eq(2*x+3*y, 85), Eq(3*x+2*y, 65), (5, 25), "S31 (kalem, defter)")
ok(X + Y == 30 and Y - X == 20, "S31")
coz(Eq(x+y, 20), Eq(2*x+4*y, 56), (12, 8), "S32 (tavuk, tavsan)")
ok((56 - 2*20) // 2 == 8, "S32 pratik")
coz(Eq(x+y, 20), Eq(5*x-2*y, 72), (16, 4), "S33")
ok(sayi_bul(lambda A, B: A+B == 11 and (10*B+A) - (10*A+B) == 27) == [47], "S34")
ok(sayi_bul(lambda A, B: 10*A+B == 7*(A+B) and A - B == 3) == [63], "S35")
X, Y = coz(Eq(x+y, 50), Eq(y-x, 26), (12, 38), "S36 (Ali, baba)")
ok((X+5) + (Y+5) == 60, "S36 5 yil sonra")
# Ders 3 sınıfta
coz(Eq(x+y, 40), Eq(x, 4*y), (32, 8), "D3-1")
coz(Eq(x+y, 12), Eq(20*x+50*y, 390), (7, 5), "D3-2")
coz(Eq(x+y, 30), Eq(2*x+4*y, 84), (18, 12), "D3-3")
ok(sayi_bul(lambda A, B: A+B == 9 and (10*A+B)-(10*B+A) == 45) == [72], "D3-4")
coz(Eq(3*x+2*y, 55), Eq(x+2*y, 25), (15, 5), "D3-5 (simit, cay)")

# ---------------- DERS NOTU: Örnekler ----------------
ok(solve(Eq(3*4 - 2*y, 6), y) == [3] and solve(Eq(3*x, 6), x) == [2], "N1")
ok(solve(Eq((m+1) + 2*(2*m), 11), m) == [2], "N2")
ok(sorted([(X, Y) for X in range(40) for Y in range(40) if 3*X+5*Y == 30]) == [(0, 6), (5, 3), (10, 0)], "N3")
coz(Eq(2*x+y, 10), Eq(x-y, 2), (4, 2), "N4")
coz(Eq(3*x-5*y, -1), Eq(2*x+3*y, 12), (3, 2), "N5")
X, Y = coz(Eq(4*x+3*y, 2), Eq(5*x-2*y, 14), (2, -2), "N6")
ok(X - Y == 4, "N6 x-y")
coz(Eq(2*x+y, 7), Eq(3*x-2*y, 0), (2, 3), "N7")
coz(Eq((x+1)/3, (y-1)/2), Eq(x+y, 15), (8, 7), "N8")
coz(Eq(Rational('0.5')*x + Rational('0.2')*y, Rational('2.6')),
    Eq(x - Rational('0.4')*y, Rational('2.8')), (4, 3), "N9")
X, Y = coz(Eq(6*x+5*y, 39), Eq(5*x+6*y, 38), (4, 3), "N10")
ok(X*Y == 12 and X+Y == 7 and X-Y == 1, "N10")
s = solve([Eq(x+y, 7), Eq(y+z, 9), Eq(x+z, 10)], [x, y, z])
ok((s[x], s[y], s[z]) == (4, 3, 6), "N11 (ileri)")
ok([A for A in range(-30, 31) if A != 0 and durum(3, -1, 2, 9, A, 6) == 'sonsuz'] == [-3], "N12")
ok([A for A in range(-30, 31) if durum(A, 2, 5, 3, -1, 4) == 'yok'] == [-6], "N13")
ok([K for K in range(-50, 51) if durum(2, 3, 5, 4, 6, K) == 'sonsuz'] == [10], "N14 sonsuz")
ok(all(durum(2, 3, 5, 4, 6, K) == 'yok' for K in range(-50, 51) if K != 10), "N14 yok")
coz(Eq(x-y, 12), Eq(x/2, y+1), (22, 10), "N15")
coz(Eq(x+y, 40), Eq(x + Rational(1, 2)*y, 29), (18, 22), "N16")
coz(Eq(x+y, 14), Eq(120*x+80*y, 1440), (8, 6), "N17")
ok(sayi_bul(lambda A, B: (10*A+B)+(10*B+A) == 110 and A - B == 4) == [73], "N18")
coz(Eq(x+y, 35), Eq(2*x+4*y, 94), (23, 12), "N19 (ordek, inek)")
X, Y = coz(Eq(x+y, 48), Eq(x, 3*y), (36, 12), "N20 (anne, kiz)")
ok(X - Y == 24, "N20 fark")

# ---------------- DERS NOTU: Alıştırmalar ----------------
ok(solve(Eq(2*3 - k, 4), k) == [2], "A1")
ok([p for p in [(-2, 1), (2, 1), (1, 0), (4, -1)] if p[0] + 3*p[1] == 1] == [(-2, 1), (1, 0), (4, -1)], "A2")
ok(sorted([(X, Y) for X in range(40) for Y in range(40) if 4*X+Y == 12]) == [(0, 12), (1, 8), (2, 4), (3, 0)], "A3")
coz(Eq(x+y, 15), Eq(x-y, 7), (11, 4), "A4")
coz(Eq(2*x+3*y, 8), Eq(4*x-3*y, -2), (1, 2), "A5")
coz(Eq(3*x+2*y, 7), Eq(5*x-3*y, -1), (1, 2), "A6")
X, Y = coz(Eq(y, 3*x-5), Eq(2*x+y, 10), (3, 4), "A7")
ok(X*Y == 12, "A7")
coz(Eq(x/3 - y/2, 0), Eq(x/2 + y/4, 4), (6, 4), "A8")
coz(Eq(Rational('0.3')*x + Rational('0.2')*y, Rational('1.3')),
    Eq(Rational('0.1')*x - Rational('0.4')*y, Rational('-0.5')), (3, 2), "A9")
X, Y = coz(Eq(4*x+3*y, 18), Eq(3*x+4*y, 17), (3, 2), "A10")
ok(X+Y == 5 and X*Y == 6, "A10")
X, Y = coz(Eq(x+y, 10), Eq(x-y, 4), (7, 3), "A11")
ok(X*Y == 21, "A11")
ok([(A, B) for A in range(-30, 31) for B in range(-30, 31) if durum(2, A, 3, 6, 9, B) == 'sonsuz'] == [(3, 9)], "A12")
ok(3 + 9 == 12, "A12 a+b")
ok([K for K in range(-50, 51) if durum(K+1, 2, 5, 6, 4, 7) == 'yok'] == [2], "A13")
ok(durum(Rational(-2, 3), -1, 4, 2, 3, 5) == 'yok', "A14 m=-2/3 -> cozum yok")
ok(solve(Eq(m*3, -1*2), m) == [Rational(-2, 3)], "A14 m")  # m/2 = -1/3
# A14: tek çözüm olmayan tek m değeri -2/3 (det = 3m + 2)
ok(solve(Eq(m*3 - 2*(-1), 0), m) == [Rational(-2, 3)], "A14 det")
coz(Eq(x+y, 63), Eq(x, 2*y), (42, 21), "A15")
ok(42 - 21 == 21, "A15 fark")
coz(Eq(x+y, 15), Eq(10*x+20*y, 210), (9, 6), "A16")
coz(Eq(x+y, 40), Eq(150*x+250*y, 7400), (26, 14), "A17")
coz(Eq(x+y, 26), Eq(2*x+4*y, 76), (14, 12), "A18 (tavuk, tavsan)")
ok(sayi_bul(lambda A, B: A+B == 12 and (10*A+B)-(10*B+A) == 36) == [84], "A19")
coz(Eq(x+y, 30), Eq(4*x-y, 80), (22, 8), "A20")
ok(4*22 - 8 == 80, "A20 kontrol")

# Brute-force: sözel problemlerde doğal sayı çözümünün tekliği
for toplam, fiyat, n, pa, pb in [(120, None, 17, 5, 10), (1560, None, 30, 40, 70), (390, None, 12, 20, 50),
                                 (210, None, 15, 10, 20), (7400, None, 40, 150, 250), (1440, None, 14, 120, 80)]:
    cozumler = [(X, n-X) for X in range(n+1) if pa*X + pb*(n-X) == toplam]
    ok(len(cozumler) == 1, f"tekillik {toplam}")

# ======================================================================
# SÜRÜM 2 EKLERİ
# ---------------- SUNUM: yıldızlı alıştırma çözüm çerçeveleri ----------------
# Ders 1 Soru 3: 3x-y=7, x+y=5 -> topla 4x=12
ok((3*x - y) + (x + y) == 4*x and 7 + 5 == 12 and F(12, 4) == 3 and 5 - 3 == 2, "S2-D1-3 adımlar")
ok(3*3 - 2 == 7 and 3 + 2 == 5, "S2-D1-3 kontrol")
# Ders 1 Soru 4: x2, x5 -> 4x+10y=2, 15x-10y=55 -> 19x=57
ok(2*(2*x + 5*y) == 4*x + 10*y and 5*(3*x - 2*y) == 15*x - 10*y and 2*1 == 2 and 5*11 == 55, "S2-D1-4 çarpma")
ok((4*x + 10*y) + (15*x - 10*y) == 19*x and 2 + 55 == 57 and 57 // 19 == 3, "S2-D1-4 topla")
ok(6 + 5*(-1) == 1 and 9 - 2*(-1) == 11, "S2-D1-4 y ve kontrol")
# Ders 1 Soru 5: x=10-2y>=0, y=0..5
ok(sorted([(X, Y) for X in range(40) for Y in range(40) if X + 2*Y == 10]) ==
   [(0, 5), (2, 4), (4, 3), (6, 2), (8, 1), (10, 0)], "S2-D1-5 liste")
# Ders 2 Soru 2: 8x+8y=40, 2x-2y=2
ok((5*x + 3*y) + (3*x + 5*y) == 8*x + 8*y and 21 + 19 == 40 and (5*x + 3*y) - (3*x + 5*y) == 2*x - 2*y and 21 - 19 == 2, "S2-D2-2")
ok(5*3 + 3*2 == 21, "S2-D2-2 kontrol")
# Ders 2 Soru 3: x6 -> 2x+3y=18 ; x=y-1 ; 5y=20
ok(6*(x/3 + y/2) - (2*x + 3*y) == 0 and 6*3 == 18, "S2-D2-3 payda")
ok(solve(Eq(2*(y-1) + 3*y, 18), y) == [4] and F(3, 3) + F(4, 2) == 3, "S2-D2-3 adımlar")
# Ders 2 Soru 4: 4/2 = k/3 != 3/5 -> k=6 ; 2. denklem x2: 4x+6y=10
ok(F(4, 2) == F(6, 3) and F(4, 2) != F(3, 5) and durum(4, 6, 3, 4, 6, 10) == 'yok', "S2-D2-4")
# Ders 3 Soru 2: 2x+5y=39 ; 3y=15
ok(20*x + 50*y == 10*(2*x + 5*y) and 390 == 10*39, "S2-D3-2 sadeleştirme")
ok(solve(Eq(2*(12-y) + 5*y, 39), y) == [5] and 20*7 + 50*5 == 390, "S2-D3-2")
# Ders 3 Soru 3: t+2k=42 ; k=12, t=18
ok(84 // 2 == 42 and 42 - 30 == 12 and 2*18 + 4*12 == 84, "S2-D3-3")
# Ders 3 Soru 4: 9(a-b)=45 -> a-b=5 ; a=7,b=2
ok(45 // 9 == 5 and (9 + 5) // 2 == 7 and 72 - 27 == 45, "S2-D3-4")

# ---------------- ALIŞTIRMA GÖVDESİ (sürüm 2 numaralandırması) ----------------
# Çözümlü Alıştırmalar (eski no -> yeni no): 3->Ç1, 6->Ç2, 8->Ç3, 10->Ç4, 12->Ç5, 14->Ç6, 17->Ç7, 19->Ç8
ok([X for X in range(0, 50) if 12 - 4*X >= 0] == [0, 1, 2, 3] and [12 - 4*X for X in range(4)] == [12, 8, 4, 0], "Ç1")
ok(len([(X, Y) for X in range(50) for Y in range(50) if 4*X + Y == 12]) == 4, "Ç1 sayma")
ok(3*(3*x + 2*y) == 9*x + 6*y and 2*(5*x - 3*y) == 10*x - 6*y and 3*7 == 21 and 2*(-1) == -2, "Ç2 çarpma")
ok(21 + (-2) == 19 and 3 + 2*2 == 7 and 5*1 - 3*2 == -1, "Ç2 adımlar")
coz(Eq(3*x+2*y, 7), Eq(5*x-3*y, -1), (1, 2), "Ç2")
ok(6*(x/3 - y/2) == 2*x - 3*y and 4*(x/2 + y/4) == 2*x + y, "Ç3 payda temizleme")
ok((2*x + y) - (2*x - 3*y) == 4*y and F(16, 4) == 4 and F(16 - 4, 2) == 6, "Ç3 adımlar")
ok(F(6, 3) - F(4, 2) == 0 and F(6, 2) + F(4, 4) == 4, "Ç3 kontrol")
coz(Eq(x/3 - y/2, 0), Eq(x/2 + y/4, 4), (6, 4), "Ç3")
X, Y = coz(Eq(4*x+3*y, 18), Eq(3*x+4*y, 17), (3, 2), "Ç4")
ok(X + Y == 5 and X - Y == 1 and X*Y == 6 and 18 + 17 == 35 and 35 // 7 == 5, "Ç4 adımlar")
ok([(A, B) for A in range(-30, 31) for B in range(-30, 31) if durum(2, A, 3, 6, 9, B) == 'sonsuz'] == [(3, 9)], "Ç5")
ok(F(2, 6) == F(3, 9) == F(3, 9) == F(1, 3) and 3*2 == 6 and 3*3 == 9, "Ç5 kontrol")
M = Rational(-2, 3)
ok(durum(M, -1, 4, 2, 3, 5) == 'yok' and M / 2 == Rational(-1, 3) and F(4, 5) != F(-1, 3), "Ç6")
ok([MM for MM in [Rational(n, 3) for n in range(-60, 61)] if durum(MM, -1, 4, 2, 3, 5) != 'tek'] == [M], "Ç6 teklik")
ok((-3)*M == 2 and (-3)*(-1) == 3 and (-3)*4 == -12, "Ç6 (-3) ile çarpma")
coz(Eq(x+y, 40), Eq(150*x+250*y, 7400), (26, 14), "Ç7")
ok(7400 // 50 == 148 and 120 + 2*14 == 148 and 150*26 == 3900 and 250*14 == 3500, "Ç7 adımlar")
ok(sayi_bul(lambda A, B: A+B == 12 and (10*A+B)-(10*B+A) == 36) == [84] and 84 - 48 == 36, "Ç8")
# Kendiniz Çözün (yeni no: eski no): 1:1, 2:2, 3:4, 4:5, 5:7, 6:9, 7:11, 8:13, 9:15, 10:16, 11:18, 12:20
ok(solve(Eq(2*3 - k, 4), k) == [2], "KÇ1")
ok([p for p in [(-2, 1), (2, 1), (1, 0), (4, -1)] if p[0] + 3*p[1] == 1] == [(-2, 1), (1, 0), (4, -1)] and 2 + 3*1 == 5, "KÇ2")
coz(Eq(x+y, 15), Eq(x-y, 7), (11, 4), "KÇ3")
coz(Eq(2*x+3*y, 8), Eq(4*x-3*y, -2), (1, 2), "KÇ4")
X, Y = coz(Eq(y, 3*x-5), Eq(2*x+y, 10), (3, 4), "KÇ5"); ok(X*Y == 12, "KÇ5 xy")
coz(Eq(Rational('0.3')*x + Rational('0.2')*y, Rational('1.3')),
    Eq(Rational('0.1')*x - Rational('0.4')*y, Rational('-0.5')), (3, 2), "KÇ6")
ok(solve(Eq(3*(4*y - 5) + 2*y, 13), y) == [2], "KÇ6 cevap anahtarı adımı 14y=28")
X, Y = coz(Eq(x+y, 10), Eq(x-y, 4), (7, 3), "KÇ7"); ok(X*Y == 21, "KÇ7 xy")
ok([K for K in range(-50, 51) if durum(K+1, 2, 5, 6, 4, 7) == 'yok'] == [2], "KÇ8")
X, Y = coz(Eq(x+y, 63), Eq(x, 2*y), (42, 21), "KÇ9"); ok(X - Y == 21, "KÇ9 fark")
coz(Eq(x+y, 15), Eq(10*x+20*y, 210), (9, 6), "KÇ10")
coz(Eq(x+y, 26), Eq(2*x+4*y, 76), (14, 12), "KÇ11")
coz(Eq(x+y, 30), Eq(4*x-y, 80), (22, 8), "KÇ12"); ok(5*22 == 110, "KÇ12 5d=110")

print(f"Tüm kontroller geçti: {N} assert.")
