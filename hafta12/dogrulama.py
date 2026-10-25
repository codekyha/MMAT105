# MMAT105 Hafta 12 -- sunum, ders notu ve alıştırmalardaki tüm sayısal cevapların doğrulanması
from fractions import Fraction as F
from math import isqrt, sqrt
from statistics import mean, harmonic_mean

sayac = 0
def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1

def coz_lineer(f, aralik=range(-1000, 1001)):
    """f(x)==0 olan tam sayı x'leri tarar (paydası sıfır olanları atlar)."""
    sonuc = []
    for x in aralik:
        try:
            if f(F(x)) == 0:
                sonuc.append(x)
        except ZeroDivisionError:
            pass
    return sonuc

def oran_ifade(a, b, f, ks=range(1, 30)):
    """a:b oranındaki tüm (a,b)=(ak,bk) çiftleri için f'nin değeri tek mi?"""
    vals = set()
    for k in ks:
        for s in (1, -1):
            try:
                vals.add(f(F(a * k * s), F(b * k * s)))
            except ZeroDivisionError:
                pass
    assert len(vals) == 1, vals
    return vals.pop()

def AO(*x): return F(sum(x), len(x))
def GO(a, b):
    r = isqrt(a * b); assert r * r == a * b; return r
def HO(a, b): return F(2 * a * b, a + b)
def ort_hiz(v1, v2, yol=F(1)):
    return 2 * yol / (yol / v1 + yol / v2)

# ---------------- Hatırlatma (Hafta 11) ----------------
ok(all(x*x - 9*x + 20 == (x-4)*(x-5) for x in range(-50, 51)), 'H1')
ok({a*a + b*b for a in [F(n, 2) for n in range(-40, 41)] for b in [7 - a] if a*b == 10} == {29}, 'H2')
ok(F(51**2 - 49**2, 20) == 10, 'H3')

# ---------------- SUNUM Ders 1 ----------------
ok(F(200, 50) == 4 and F(45, 120) == F(3, 8), 'Ö1')
ok(coz_lineer(lambda x: (x-1)/(x+3) - F(3, 5)) == [7], 'Ö2')
ok(oran_ifade(3, 4, lambda a, b: (2*a+b)/(b-a)) == 10, 'Ö3')
# Ö4: (a+b)/(a-b)=5/2 sağlayan tüm (a,b) için a/b=7/3
r = {F(a, b) for a in range(-60, 61) for b in range(-60, 61) if b and a != b and F(a+b, a-b) == F(5, 2)}
ok(r == {F(7, 3)}, 'Ö4')
t = [(2*k, 3*k, 5*k) for k in range(-50, 51) if 10*k == 40]
ok(t == [(8, 12, 20)], 'Ö5')
t = [2*k for k in range(-50, 51) if 2*(2*k) + 3*k - 5*k == 10]
ok(t == [10], 'Ö6')
ok(all(F(3, 4)*(b+d+f) == 15 for b in range(1, 20) for d in range(1, 20) for f in [20-b-d] if f > 0), 'Ö7a')
ok(all(F(2*F(3,4)*b + 5*F(3,4)*d, 2*b+5*d) == F(3, 4) for b in range(1, 15) for d in range(1, 15)), 'Ö7b')
t = [(a, b, c) for a in range(1, 40) for b in range(1, 40) for c in range(1, 40) if 3*a == 4*b == 6*c and a+b+c == 36]
ok(t == [(16, 12, 8)], 'Ö8')
t = [(a, b, c) for a in range(1, 71) for b in range(1, 71) for c in range(1, 71)
     if 3*a == 2*b and 5*b == 4*c and a+b+c == 70]
ok(t == [(16, 24, 30)], 'Ö9')
k = F(600, 10); ok((5*k, 2*k) == (300, 120), 'Ö10')
ok(6 * 500000 == 3_000_000 and 3_000_000 / 100_000 == 30, 'Ö11')
ok(45 * 100_000 == 4_500_000 and F(3, 4_500_000) == F(1, 1_500_000), 'Ö12')
# Ders 1 sınıfta
ok(coz_lineer(lambda x: (2*x+1)/(x+4) - F(5, 3)) == [17] and F(35, 21) == F(5, 3), 'S1-1')
ok([4*k for k in range(1, 30) if 13*k == 52] == [16], 'S1-2')
ok([4*k for k in range(1, 100) if 9*k == 180] == [80] and [2*20, 3*20] == [40, 60], 'S1-3')
ok(oran_ifade(2, 5, lambda a, b: (3*a+b)/(b-a)) == F(11, 3), 'S1-4')
ok(F(15, 2) * 200000 == 1_500_000 and F(1_500_000, 100_000) == 15, 'S1-5')

# ---------------- SUNUM Ders 2 ----------------
ok(F(10, 4) * 10 == 25, 'Ö13')
k = F(4-1, 4+2); ok([y for y in range(-100, 100) if F(y-1, 10+2) == k] == [7], 'Ö14')
ok(F(6*8, 4) == 12, 'Ö15')
ok(F(4*15, 10) == 6, 'Ö16')
ok(F(20*6, 30) == 4, 'Ö17')
ok(60*5 == 300 and F(300, 75) == 4, 'Ö18')
ok(F(6*20, 8) == 15, 'Ö19')
p = [F(1, 2), F(1, 3), F(1, 6)]; k = 300 / sum(p); paylar = [x*k for x in p]
ok(paylar == [150, 100, 50] and [x*6 for x in p] == [3, 2, 1], 'Ö20')
k = F(4*6, 2); ok([z for z in range(1, 100) if k*F(6, z) == 8] == [9], 'Ö21')
k = F(6*2, 3); ok(k == 4 and k*F(10, 4) == 10, 'Ö22')
ok([x for x in range(1, 50) if F(24, 6*8*5) == F(36, 10*12*x)] == [3], 'Ö23')
ok(F(40, 4*6*10) * (6*8*5) == 40, 'Ö24')
# Ders 2 sınıfta
ok(F(45, 3) * 7 == 105, 'S2-1')
ok([n for n in range(1, 100) if 8*12 == n*6] == [16], 'S2-2')
ok(F(5*12, 3) == 20, 'S2-3')
k = F(6*2, 4); ok(k == 3 and k*F(10, 5) == 6, 'S2-4')
ok(F(200, 5*8*10) * (4*10*12) == 240, 'S2-5')

# ---------------- SUNUM Ders 3 ----------------
ok(AO(7, 12, 15, 26) == 15, 'Ö25')
ok([x for x in range(0, 101) if AO(60, 70, x) == 75] == [95], 'Ö26')
ok(F(10*15 - 30, 6) == 20, 'Ö27')
ok(F(5*24 + 30, 6) == 25, 'Ö28')
ok(F(20*60 + 30*70, 50) == 66 and AO(60, 70) == 65, 'Ö29')
ok(F(2*50 + 3*80, 5) == 68, 'Ö30')
t = {F(kz, e) for kz in range(1, 40) for e in range(1, 40) if F(70*kz + 60*e, kz+e) == 64}
ok(t == {F(2, 3)}, 'Ö31')
ok(AO(4, 9) == F(13, 2) and GO(4, 9) == 6 and HO(4, 9) == F(72, 13)
   and round(float(HO(4, 9)), 2) == 5.54 and AO(4, 9) > 6 > HO(4, 9), 'Ö32')
t = [(a, b) for a in range(1, 20) for b in range(1, 20) if a*b == 16 and a + b == 10]
ok(t and all(a*a + b*b == 68 for a, b in t) and (2, 8) in t, 'Ö33')
ok(HO(60, 40) == 48 and ort_hiz(60, 40, 120) == 48 and F(240, 5) == 48, 'Ö34')
t = [n for n in range(-99, 100, 2) if sum(range(n, n+10, 2)) == 85]
ok(t == [13] and t[0] + 8 == 21, 'Ö35a')
tek = list(range(13, 48, 2)); ok(len(tek) == 18 and AO(*tek) == 30 and sum(tek) == 540, 'Ö35b')
# Python ile ortalama (sunumda yok, kontrol amaçlı)
ok(mean([7, 12, 15, 26]) == 15 and abs(harmonic_mean([60, 40]) - 48) < 1e-9, 'stat')
# Ders 3 sınıfta
ok(F(8*12 + 21, 9) == 13, 'S3-1')
ok(GO(3, 27) == 9, 'S3-2')
ok(HO(30, 60) == 40 and ort_hiz(30, 60, 60) == 40, 'S3-3')
ok(F(15*40 + 10*50, 25) == 44, 'S3-4')
t = [n for n in range(-100, 100, 2) if sum(range(n, n+14, 2)) == 98]
ok(t == [8], 'S3-5')

# ---------------- DERS NOTU örnekleri ----------------
ok(coz_lineer(lambda x: (3*x-2)/(x+1) - F(4, 3)) == [2], 'N1')
ok(oran_ifade(5, 2, lambda a, b: (a+2*b)/(a-b)) == 3, 'N2')
r = {F(a, b) for a in range(-60, 61) for b in range(-60, 61) if b and a+b and F(2*a-b, a+b) == F(1, 4)}
ok(r == {F(5, 7)}, 'N3')
t = [(3*k, 5*k, 7*k) for k in range(-50, 51) if 6*k + 5*k - 7*k == 16]
ok(t == [(12, 20, 28)] and sum(t[0]) == 60, 'N4')
t = [(a, b, c) for a in range(1, 62) for b in range(1, 62) for c in range(1, 62)
     if 4*a == 3*b and 5*b == 6*c and a+b+c == 62]
ok(t == [(18, 24, 20)], 'N5')
k = F(360, 12); ok([3*k, 4*k, 5*k] == [90, 120, 150], 'N6a')
p = [F(1, 2), F(1, 3), F(1, 4)]; k = 390 / sum(p)
ok([x*k for x in p] == [180, 120, 90] and [x*12 for x in p] == [6, 4, 3], 'N6b')
ok(F(48, 10) * 2_500_000 == 12_000_000 and 12_000_000 // 100_000 == 120
   and 5*200 == 1000 and F(7, 2)*200 == 700, 'N7')
ok(F(3*20, 12) == 5, 'N8')
ok(F(40*(30-10), 40-20) == 40, 'N9')
ok([n for n in range(1, 200) if n*15 == (n+10)*10] == [20], 'N10')
k = F(9*4, 6); ok(k == 6 and k*F(10, 6) == 10, 'N11')
ok([x for x in range(1, 100) if 12*8*15 == 9*10*x] == [16], 'N12')
ok(6*20 - 5*18 == 30, 'N13')
ok([f for f in range(0, 101) if F(48 + 2*f, 3) == 60] == [66], 'N14')
ok(F(30*62 - 12*68, 18) == 58 and 30*62 == 1860 and 12*68 == 816, 'N15')
ok(AO(2, 8) == 5 and GO(2, 8) == 4 and HO(2, 8) == F(16, 5) and AO(2, 8)*HO(2, 8) == 16, 'N16')
ok(HO(45, 90) == 60 and ort_hiz(45, 90, 90) == 60 and AO(45, 90) == F(135, 2), 'N17')
t = [n for n in range(-100, 100) if AO(*range(n, n+9)) == 23]
cift = list(range(20, 61, 2))
ok(t == [19] and t[0] + 8 == 27 and len(cift) == 21 and AO(*cift) == 40 and sum(cift) == 840, 'N18')

# ---------------- ÇÖZÜMLÜ ALIŞTIRMALAR ----------------
t = [(a, b) for a in range(1, 45) for b in range(1, 45) if 7*a == 4*b and a + b == 44]
ok(t == [(16, 28)] and 28 - 16 == 12, 'A1')
t = [(x, y, z) for x in range(1, 46) for y in range(1, 46) for z in range(1, 46)
     if 5*x == 4*y and 6*y == 5*z and x+y+z == 45]
ok(t == [(12, 15, 18)] and 12*18 == 216, 'A2')
t = [(a, b) for a in range(-100, 101) for b in range(-100, 101) if 2*a == 5*b and a - b == 18]
ok(t == [(30, 12)], 'A3')
p = [F(1, 2), F(1, 3), F(1, 4)]; k = 2600 / sum(p)
ok([x*k for x in p] == [1200, 800, 600], 'A4')
ok(F(9*(20-5), 9+6) == 9, 'A5')
ok([x for x in range(1, 100) if F(1800, 3*8*6) == F(2400, 4*6*x)] == [8] and F(1800, 144) == F(25, 2), 'A6')
ok(F(25*64 - 32 + 82, 25) == 66, 'A7')
t = sorted((a, b) for a in range(1, 30) for b in range(1, 30) if a + b == 20 and a*b == 64)
ok(t == [(4, 16), (16, 4)] and HO(4, 16) == F(32, 5), 'A8')

# ---------------- KENDİNİZ ÇÖZÜN ----------------
ok(coz_lineer(lambda x: (x+5)/(x-1) - F(7, 4)) == [9], 'K1')
ok(oran_ifade(3, 5, lambda a, b: (a+b)/(b-a)) == 4, 'K2')
ok([9*k for k in range(1, 30) if 20*k == 60] == [27], 'K3')
ok(F(720, 12) * 3 == 180, 'K4')
ok(8 * 300_000 == 2_400_000 and 2_400_000 // 100_000 == 24, 'K5')
ok(F(40*12, 60) == 8, 'K6')
ok(F(6*20, 12) == 10, 'K7')
k = F(6*4, 3); ok(k == 8 and k*F(5, 10) == 4, 'K8')
ok([x for x in range(1, 100) if F(120, 5*8*6) == F(160, 4*10*x)] == [8], 'K9')
ok(F(20*55 + 30*65, 50) == 61, 'K10')
ok(GO(5, 20) == 10 and HO(5, 20) == 8, 'K11')
ok(HO(30, 70) == 42 and ort_hiz(30, 70, 210) == 42, 'K12')
t = [n for n in range(-99, 100, 2) if sum(range(n, n+22, 2)) == 231]
ok(t == [11] and t[0] + 20 == 31, 'K13')
t = [(a, b) for a in range(1, 30) for b in range(1, 30) if a + b == 26 and a*b == 144]
ok(t and all(a*a + b*b == 388 for a, b in t), 'K14')

print(f'Tüm kontroller geçti: {sayac} assert')
