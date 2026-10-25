# MMAT105 Hafta 14 -- sunum, ders notu, alıştırmalar ve karma tekrardaki TÜM sayısal cevapların doğrulanması
# Kesin aritmetik için Fraction kullanılır; mümkün olan yerde brute force (tarama) ile tekliği de kontrol edilir.
from fractions import Fraction as Fr
from math import gcd, isqrt, factorial
import sympy as sp

sayac = 0
def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1

def P(a):                      # %a  -> kesir
    return Fr(a) / 100

def yuzde(x, a):               # x'in %a'sı
    return Fr(x) * P(a)

def tara(kosul, bas=0, son=2000, adim=Fr(1, 2)):
    """bas..son aralığını adim ile tarar, koşulu sağlayan TÜM değerleri döndürür (teklik kontrolü için)."""
    out, x = [], Fr(bas)
    while x <= son:
        if kosul(x):
            out.append(x)
        x += adim
    return out

def basit(A, n, t, birim='yil'):
    return Fr(A) * n * t / {'yil': 100, 'ay': 1200, 'gun': 36000}[birim]

def bilesik(A, n, t):
    return Fr(A) * (1 + P(n)) ** t

def bolenler(n):
    return [d for d in range(1, n + 1) if n % d == 0]

# ================= Geçen hafta hatırlatma (Hafta 13) =================
ok(tara(lambda x: 3*x + 5 == 26, -100, 100, 1) == [7], 'H1')
s = tara(lambda x: Fr(2, 5)*x == 24, 0, 500, 1)
ok(s == [60] and Fr(3, 4)*60 == 45, 'H2')
ok(tara(lambda x: 40 + x == 3*(10 + x), 0, 100, 1) == [5], 'H3')

# ================= SUNUM Ders 1 =================
ok(yuzde(240, 35) == 84 and yuzde(240, Fr(25, 2)) == 30 and Fr(60, 240)*100 == 25, 'Ö1')
s = tara(lambda x: yuzde(x, 30) == 72, 0, 2000, 1)
ok(s == [240] and yuzde(240, 45) == 108 and yuzde(240, 15) == 36, 'Ö2')
ok(800*(1 + P(15)) == 920 and 800*(1 - P(15)) == 680, 'Ö3')
ok(tara(lambda x: x*(1 + P(30)) == 260, 0, 1000, 1) == [200] and 260 - yuzde(260, 30) == 182, 'Ö4')
ok(100*(1 + P(20))*(1 - P(20)) == 96 and Fr(12, 10)*Fr(8, 10) == Fr(96, 100), 'Ö5')
ok(yuzde(40, 25) + yuzde(60, 50) == 40, 'Ö6')
ok(tara(lambda M: M*(1 + P(25)) == 250, 0, 1000, 1) == [200], 'Ö7')
M = tara(lambda M: M*(1 - P(20)) == 240, 0, 1000, 1)
ok(M == [300] and 300*(1 + P(25)) == 375, 'Ö8')
# kalem: 3 tanesi 10 TL'ye alınıp 5 tanesi 20 TL'ye satılıyor; birim maliyet 10/3, birim satış 4
ok((Fr(20, 5) - Fr(10, 3)) / Fr(10, 3) * 100 == 20 and 15 // 3 * 10 == 50 and 15 // 5 * 20 == 60, 'Ö9')
ok(600*(1 - P(20)) == 480 and Fr(480 - 400, 400)*100 == 20, 'Ö10')
E = tara(lambda E: E*(1 - P(20)) == 120, 0, 1000, 1)
ok(E == [150] and (E[0] - 100) == 50, 'Ö11')
# Ders 1 sınıfta
ok(yuzde(360, 15) == 54, 'S1-1')
ok(tara(lambda x: x*(1 - P(20))*(1 + P(40)) == 112, 0, 1000, 1) == [100], 'S1-2')
ok(100*(1 + P(50))*(1 - P(20)) == 120, 'S1-3')
M = tara(lambda M: M*(1 + P(20)) == 240, 0, 1000, 1)
ok(M == [200] and 200*(1 - P(20)) == 160, 'S1-4')
sat = 500*(1 - P(30))
ok(sat == 350 and Fr(sat - 280, 280)*100 == 25, 'S1-5')

# ================= SUNUM Ders 2 =================
ok(yuzde(80, 15) == 12 and 80 - 12 == 68, 'Ö12')
ok(tara(lambda x: Fr(12)/(40 + x) == P(20), 0, 500) == [20] and yuzde(40, 30) == 12, 'Ö13')
ok(tara(lambda x: x < 50 and Fr(10)/(50 - x) == P(50), 0, 49) == [30], 'Ö14')
ok(yuzde(40, 20) == 8 and yuzde(10, 40) == 4 and Fr(12, 50) == P(24), 'Ö15')
t = [(x, 60 - x) for x in range(0, 61) if yuzde(x, 30) + yuzde(60 - x, 50) == yuzde(60, 35)]
ok(t == [(45, 15)], 'Ö16')
ok(tara(lambda x: (8 + x)/(40 + x) == P(36), 0, 500) == [10] and Fr(18, 50) == P(36), 'Ö17')
K = 100; tuz = yuzde(K, 20)
tuz = tuz/2 + yuzde(K/2, 40)
ok(tuz / K == P(30), 'Ö18')
ok(Fr(60*22, 24) == 55 and 60 - 55 == 5, 'Ö19')
saf = Fr(40*18, 24) + 20
ok(saf == 50 and saf/60*24 == 20, 'Ö20')
# Ders 2 sınıfta
ok(tara(lambda x: yuzde(60, 30)/(60 + x) == P(20), 0, 500) == [30], 'S2-1')
ok(tara(lambda x: x < 50 and yuzde(50, 40)/(50 - x) == P(50), 0, 49) == [10], 'S2-2')
ok((yuzde(30, 10) + yuzde(20, 30)) / 50 == P(18), 'S2-3')
ok(tara(lambda x: (yuzde(60, 25) + x)/(60 + x) == P(40), 0, 500) == [15] and Fr(30, 75) == P(40), 'S2-4')
ok(Fr(48*18, 24) == 36, 'S2-5')

# ================= SUNUM Ders 3: faiz =================
ok(basit(5000, 30, 2) == 3000 and 5000 + 3000 == 8000, 'Ö21')
ok(basit(6000, 24, 6, 'ay') == 720 and basit(9000, 40, 90, 'gun') == 900, 'Ö22')
ok(tara(lambda n: basit(3000, n, 8, 'ay') == 400, 0, 200) == [20], 'Ö23')
ok(tara(lambda t: basit(100, 30, t, 'ay') == 25, 0, 500) == [10], 'Ö24')
ok(bilesik(10000, 20, 2) == 14400 and 10000 + basit(10000, 20, 2) == 14000
   and 14400 - 14000 == 400 and basit(10000, 20, 1) == 2000, 'Ö25')
# Python köşesi (float çıktısı gerçekten 14400.0 ve 900.0 mı?)
A_, n_ = 10000, 20
ok(A_*n_*2/100 == 4000.0 and A_*(1 + n_/100)**2 == 14400.0 and 9000*40*90/36000 == 900.0, 'Python')

# ================= SUNUM Ders 3: genel tekrar =================
t = [x for x in range(-100, 100, 2) if x + (x+2) + (x+4) + (x+6) == 76]
ok(t == [16] and t[0] + 6 == 22, 'T1')
ok(gcd(72, 120) == 24 and 72*120 // gcd(72, 120) == 360 and 24*360 == 8640 == 72*120, 'T2')
ok((Fr(3, 10) + Fr(12, 100)) / Fr(7, 100) == 6, 'T3')
t = [(x, y) for x in range(-50, 50) for y in range(-50, 50) if x + y == 17 and 2*x - y == 4]
ok(t == [(7, 10)], 'T4')
t = [x for x in range(-100, 100) if abs(2*x - 3) <= 5]
ok(t == [-1, 0, 1, 2, 3, 4] and len(t) == 6 and sum(t) == 9, 'T5')
ok([x for x in range(-20, 20) if x >= 0 and 2**(x+1) + 2**x == 48] == [4]
   and sp.solve(sp.Eq(2**(sp.Symbol('x')+1) + 2**sp.Symbol('x'), 48)) == [4], 'T6')
ok(sp.simplify(sp.sqrt(50) + sp.sqrt(18) - sp.sqrt(32) - 4*sp.sqrt(2)) == 0, 'T7')
t = [(x, y) for x in range(-50, 50) for y in range(-50, 50) if x*x - y*y == 24 and x + y == 6]
ok(t == [(5, 1)], 'T8')
t = [(3*k, 4*k, 5*k) for k in range(-50, 50) if 12*k == 48]
ok(t == [(12, 16, 20)], 'T9')
# Ders 3 sınıfta
ok(basit(4000, 30, 2) == 2400, 'S3-1')
ok(tara(lambda t: basit(100, 40, t, 'ay') == 50, 0, 500) == [15], 'S3-2')
ok(tara(lambda A: basit(A, 25, 1) - basit(A, 20, 1) == 100, 0, 10000, 1) == [2000], 'S3-3')
ok(gcd(84, 126) == 42 and 84*126 // 42 == 252, 'S3-4')
ok(sp.sqrt(12)*sp.sqrt(27) == 18, 'S3-5')

# ================= DERS NOTU örnekleri =================
ok(yuzde(450, 18) == 81 and tara(lambda x: yuzde(x, 15) == 81, 0, 2000, 1) == [540], 'N1')
a, b = 3, 5
ok(Fr(a, b)*100 == 60 and Fr(a, a+b)*100 == Fr(75, 2), 'N2')
ok(100*(1 + P(40))*(1 - P(25)) == 105, 'N3')
ok((1 - P(20))*(1 - P(25)) == Fr(60, 100), 'N4')
ok(tara(lambda x: x*(1 + P(15)) - x*(1 - P(20)) == 56, 0, 2000, 1) == [160] and Fr(184) - 128 == 56, 'N5')
ok(Fr(120, 160) == Fr(3, 4) and 1 - Fr(3, 4) == P(25), 'N6')
ok((1 + P(20))*(1 - P(20)) == 1 - P(4), 'N7')
ok(tara(lambda M: M*(1 + P(10)) == 330, 0, 1000, 1) == [300], 'N8')
ok((100*(1 + P(20)) + 100*(1 - P(10)) - 200) / 200 == P(5), 'N9')
ok(tara(lambda M: M*(1 + P(20)) - M*(1 - P(10)) == 120, 0, 2000, 1) == [400] and 480 - 360 == 120, 'N10')
ok(100*(1 + P(60))*(1 - P(25)) == 120, 'N11')
ok(Fr(100*10, 100*(1 - P(20))) == Fr(25, 2), 'N12')   # 12,5 TL/kg
ok(yuzde(80, 25) / (80 + 20) == P(20), 'N13')
ok(yuzde(40, 15) / (40 - 10) == P(20), 'N14')
t = [(x, 90 - x) for x in range(0, 91) if yuzde(x, 20) + yuzde(90 - x, 50) == yuzde(90, 30)]
ok(t == [(60, 30)] and yuzde(90, 30) == 27, 'N15')
seker = yuzde(50, 10) * Fr(40, 50)    # 10 kg alınınca kalan şeker
ok(seker == 4 and (seker + 10) / (40 + 10) == P(28), 'N16')
saf = Fr(30*14, 24) + Fr(18*22, 24)
ok(Fr(30*14, 24) == Fr(35, 2) and Fr(18*22, 24) == Fr(33, 2) and saf == 34 and saf/48*24 == 17, 'N17')
ok(basit(15000, 32, 9, 'ay') == 3600 and 15000 + 3600 == 18600, 'N18')
ok(basit(7200, 30, 75, 'gun') == 450, 'N19')
ok(tara(lambda t: basit(100, 25, t) == 100, 0, 100) == [4], 'N20')
t = [(A, n) for A in range(100, 20001, 100) for n in range(1, 101)
     if A + basit(A, n, 2) == 13000 and A + basit(A, n, 5) == 17500]
ok(t == [(10000, 15)], 'N21')
ok(bilesik(20000, 10, 1) == 22000 and bilesik(20000, 10, 2) == 24200 and bilesik(20000, 10, 3) == 26620
   and 20000 + basit(20000, 10, 3) == 26000 and 26620 - 26000 == 620, 'N22')

# ================= Çözümlü alıştırmalar =================
ok(tara(lambda x: yuzde(yuzde(x, 25), 40) == 18, 0, 2000, 1) == [180] and yuzde(180, 25) == 45, 'A1')
ok(100*(1 + P(25))*(1 + P(20)) == 150, 'A2')
ok(yuzde(60, 30) + yuzde(40, 45) == 36 and yuzde(60, 30) == 18 and yuzde(40, 45) == 18, 'A3')
M = tara(lambda M: M*(1 + P(25)) == 400, 0, 1000, Fr(1, 10))
ok(M == [320] and 320*(1 - P(10)) == 288, 'A4')
E = tara(lambda E: E*(1 - P(30)) == 100*(1 + P(12)), 0, 1000, 1)
ok(E == [160], 'A5')
ok(tara(lambda x: yuzde(30, 40)/(30 + x) == P(25), 0, 500) == [18], 'A6')
tuz = yuzde(40, 20) + yuzde(60, 30)
ok(tuz == 26 and tuz/(100 - 35) == P(40), 'A7')
ok(tara(lambda x: basit(x, 30, 1) + basit(8000 - x, 20, 1) == 2000, 0, 8000, 1) == [4000], 'A8')

# ================= Kendiniz çözün =================
ok(yuzde(640, 15) == 96, 'K1')
ok(Fr(36, 240)*100 == 15, 'K2')
ok(tara(lambda x: yuzde(x, 35) == 84, 0, 2000, 1) == [240], 'K3')
ok(1200*(1 + P(15))*(1 - P(10)) == 1242, 'K4')
ok(tara(lambda x: x*(1 - P(30)) == 560, 0, 5000, 1) == [800], 'K5')
ok(tara(lambda k: (1 + P(25))*(1 - P(k)) == 1, 0, 100, 1) == [20], 'K6')
ok(Fr(310 - 250, 250)*100 == 24, 'K7')
ok((Fr(20, 4) - Fr(20, 5)) / Fr(20, 5) * 100 == 25 and 20//5*20 == 80 and 20//4*20 == 100, 'K8')
ok(tara(lambda M: M*(1 + P(20)) == 900*(1 - P(20)), 0, 2000, 1) == [600], 'K9')
ok(tara(lambda x: yuzde(25, 40)/(25 + x) == P(25), 0, 500) == [15], 'K10')
ok(tara(lambda x: x < 60 and yuzde(60, 20)/(60 - x) == P(30), 0, 59) == [20], 'K11')
ok((yuzde(20, 15) + yuzde(30, 35)) / 50 == P(27), 'K12')
ok(tara(lambda x: (Fr(36*22, 24) + x)/(36 + x)*24 == 23, 0, 500) == [36], 'K13')
ok(basit(4500, 40, 8, 'ay') == 1200, 'K14')
ok(tara(lambda n: 6000 + basit(6000, n, 3) == 9600, 0, 200) == [20], 'K15')
ok(bilesik(5000, 10, 2) == 6050, 'K16')

# ================= Finale Hazırlık: Karma Tekrar =================
ok(Fr(factorial(8) - factorial(7), factorial(6)) == 49, 'M1')
t = [(a, b) for a in range(10) for b in range(10) if int(f'4{a}7{b}') % 45 == 0]
ok(t == [(2, 5), (7, 0)] and sum(a for a, _ in t) == 9 and 4770 == 45*106 and 4275 == 45*95, 'M2')
t = [x for x in range(-100, 100) if abs(x - 2) < 5]
ok(len(t) == 9 and sum(t) == 18 and t == list(range(-2, 7)), 'M3')
x = sp.Symbol('x')
ok(sp.simplify((x**2 - 9)/(x**2 + x - 6) - (x - 3)/(x - 2)) == 0
   and sp.factor(x**2 + x - 6) == (x - 2)*(x + 3), 'M4')
E = tara(lambda E: E*(1 - P(20)) == 360, 0, 2000, 1)
M = tara(lambda M: M*(1 + P(50)) == 450, 0, 2000, 1)
ok(E == [450] and M == [300] and Fr(360 - 300, 300)*100 == 20, 'M5')
t = [s for s in range(0, 100) if 3*s + 6 == 2*(s + 12)]
ok(t == [18] and 3*18 == 54 and 54 + 6 == 2*(18 + 12), 'M6')
ok(len(bolenler(180)) == 18, 'M7')
g = gcd(48, 72)
ok(g == 24 and (48//g)*(72//g) == 6, 'M8')
ok(Fr(1, 2) + Fr(2, 3)*Fr(3, 4) == 1, 'M9')
ok(tara(lambda x: 3*(x - 2) + 4 == 2*x + 5, -100, 100, 1) == [7], 'M10')
t = [(o, m) for o in range(0, 31) for m in range(0, 31) if o + m == 30 and 4*o + 2*m == 100]
ok(t == [(20, 10)], 'M11')
ok([k for k in range(-20, 20) if k >= 1 and 9**k == 27**(k-1)] == [3], 'M12')
ok(sp.simplify(6/sp.sqrt(3) + sp.sqrt(27) - 5*sp.sqrt(3)) == 0, 'M13')
ok(5*18 - 4*16 == 26, 'M14')
ok((yuzde(30, 20) + 10)/(30 + 10) == P(40), 'M15')
ok(basit(7200, 25, 120, 'gun') == 600, 'M16')

print(f'Tüm kontroller geçti: {sayac} assert')

# 13.10.2026: karma soru 11 sayıları değişti (40 araç, 130 tekerlek)
_s=[(a,m) for a in range(41) for m in range(41) if a+m==40 and 4*a+2*m==130]
assert _s==[(25,15)]; print("karma 11 güncel: geçti")
