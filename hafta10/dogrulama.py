# MMAT105 Hafta 10 -- sunum, ders notu, çözümlü/kendiniz çözün alıştırmaları,
# Sınıfta Siz Çözün ve hatırlatma sorularındaki tüm sayısal cevapların doğrulanması.
# Her eşitlik hem cebirsel (sympy minimal polinom) hem de 60 basamaklı sayısal olarak kontrol edilir.
import math
import sympy as sp
from sympy import sqrt, Rational as R, real_root, Abs

X = sp.Symbol('X')
sayac = 0


def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1


def esit(a, b, ad):
    a, b = sp.sympify(a), sp.sympify(b)
    fark = a - b
    ok(abs(sp.N(fark, 60)) < sp.Float('1e-50'), ad + ' (sayısal)')
    ok(sp.minimal_polynomial(fark, X) == X, ad + ' (cebirsel)')
    ok(abs(float(a) - float(b)) < 1e-9, ad + ' (kayan nokta)')


def kok(a, n):  # reel n. dereceden kök (tek derecede negatif içerik serbest)
    return real_root(sp.sympify(a), n)


def reel_mi(a, n):  # n. dereceden kök reel mi?
    return n % 2 == 1 or a >= 0


def sirala(d):  # {'a':deger,...} -> küçükten büyüğe isim listesi
    return [k for k, _ in sorted(d.items(), key=lambda t: float(sp.N(t[1], 50)))]


# ---------------- Hatırlatma (Hafta 9) ----------------
ok(R(2**3 * 2**5, 2**6) == 4, 'H1')
ok(R(1, 5) + 5**0 == R(6, 5), 'H2')
ok([x for x in range(-20, 21) if 3**(x - 1) == 27] == [4], 'H3')

# ---------------- SUNUM Ders 1 ----------------
ok([n**2 for n in range(1, 21)] == [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400], 'kareler')
ok([n**3 for n in range(1, 11)] == [1,8,27,64,125,216,343,512,729,1000], 'küpler')
ok([2**4, 3**4, 4**4, 5**4, 2**5, 3**5] == [16, 81, 256, 625, 32, 243], '4. ve 5. kuvvetler')
esit(sqrt(49), 7, 'tanım √49'); esit(kok(16, 4), 2, 'tanım ⁴√16'); esit(kok(-8, 3), -2, 'tanım ∛-8')
esit(sqrt(9 + 16), 5, 'hata √25'); ok(sqrt(9) + sqrt(16) == 7, 'hata 7')
esit(sqrt(144) + kok(-27, 3) - kok(16, 4), 7, 'Ö1')
ok([reel_mi(a, n) for a, n in [(-9, 2), (-64, 3), (-16, 4), (-32, 5)]] == [False, True, False, True], 'Ö2 reel')
esit(kok(-64, 3), -4, 'Ö2 a'); esit(kok(-32, 5), -2, 'Ö2 b')
ok([x for x in range(-100, 101) if x - 3 >= 0 and 6 - x >= 0] == [3, 4, 5, 6], 'Ö3')
esit(R(8)**R(2, 3), 4, 'kural 8^(2/3)')
esit(R(8)**R(2, 3) + R(16)**R(3, 4), 12, 'Ö4')
ok([x for x in range(-20, 21) if sqrt(3**x) == 27] == [6], 'Ö5')
esit(sqrt((-5)**2), 5, 'kural a'); esit(kok((-5)**3, 3), -5, 'kural b'); esit(kok((-2)**4, 4), 2, 'kural c')
esit(sqrt((-7)**2), 7, 'Ö6a'); esit(kok((-7)**3, 3), -7, 'Ö6b'); esit(kok((-3)**4, 4), 3, 'Ö6c'); esit(kok((-1)**5, 5), -1, 'Ö6d')
esit(sqrt((2 - sqrt(5))**2) + sqrt((3 - sqrt(5))**2), 1, 'Ö7')
for x in [R(k, 7) for k in range(-13, 21)]:  # -2 < x < 3
    ok(sqrt((x + 2)**2) + sqrt((x - 3)**2) == 5, 'Ö8 x=%s' % x)
esit(sqrt(72), 6*sqrt(2), 'kural √72'); esit(3*sqrt(2), sqrt(18), 'kural 3√2'); esit(2*sqrt(18), sqrt(72), 'hata 2√18')
esit(sqrt(50), 5*sqrt(2), 'Ö9a'); esit(sqrt(300), 10*sqrt(3), 'Ö9b'); esit(sqrt(72), 6*sqrt(2), 'Ö9c'); esit(kok(54, 3), 3*kok(2, 3), 'Ö9d')
esit(3*sqrt(2), sqrt(18), 'Ö10a'); esit(2*sqrt(5), sqrt(20), 'Ö10b'); esit(2*kok(3, 3), kok(24, 3), 'Ö10c')
ok([a for a in range(1, 50) if a*a*3 == 75] == [5], 'Ö10d')
ok(math.isqrt(50) == 7 and math.isqrt(110) == 10 and math.isqrt(45) == 6, 'Ö11')
ok(7 < math.sqrt(50) < 8 and 10 < math.sqrt(110) < 11 and 6 < 3*math.sqrt(5) < 7, 'Ö11 float')
ok(len([n for n in range(0, 1000) if 4 < sqrt(n) < 6]) == 19, 'Ö12')
# Ders 1 sınıfta
esit(sqrt(81) - kok(-125, 3) + kok(81, 4), 17, 'S1-1')
esit(sqrt(98), 7*sqrt(2), 'S1-2')
esit(sqrt((3 - sqrt(10))**2), sqrt(10) - 3, 'S1-3')
esit(R(27)**R(2, 3), 9, 'S1-4')
ok(len([x for x in range(-100, 101) if x - 2 >= 0 and 8 - x >= 0]) == 7, 'S1-5')

# ---------------- SUNUM Ders 2 ----------------
esit(sqrt(12) + sqrt(27), 5*sqrt(3), 'kural toplama')
ok(abs((1.41 + 1.73) - 3.14) < 1e-12 and round(math.sqrt(5), 2) == 2.24, 'hata √2+√3')
ok(abs(float(sqrt(2) + sqrt(3) - sqrt(5))) > 0.5, 'hata √2+√3≠√5')
esit(2*sqrt(3) + 5*sqrt(3) - 4*sqrt(3), 3*sqrt(3), 'Ö13a'); esit(7*kok(2, 3) - 2*kok(2, 3), 5*kok(2, 3), 'Ö13b')
esit(sqrt(12) + sqrt(27) - sqrt(48), sqrt(3), 'Ö14')
esit(sqrt(50) - sqrt(18) + sqrt(8), 4*sqrt(2), 'Ö15')
esit(kok(16, 3) + kok(54, 3), 5*kok(2, 3), 'Ö16')
esit(2*sqrt(3)*5*sqrt(2), 10*sqrt(6), 'kural çarpma')
ok(abs(float(sqrt(2)*kok(3, 3) - kok(6, 6))) > 0.1, 'hata √2∛3≠⁶√6')
esit(sqrt(5)*sqrt(10)*sqrt(2), 10, 'Ö17a'); esit(2*sqrt(5)*3*sqrt(10), 30*sqrt(2), 'Ö17b')
esit(sqrt(72)/sqrt(2) + sqrt(75)/sqrt(3), 11, 'Ö18')
esit(sqrt(2), kok(8, 6), 'kural √2=⁶√8'); esit(sqrt(kok(64, 3)), 2, 'kural kökün kökü')
esit(sqrt(2*sqrt(2)), kok(8, 4), 'kural √(2√2)'); esit(kok(3, 3), kok(9, 6), 'hata ∛3=⁶√9')
ok(abs(float(kok(3, 3) - kok(6, 6))) > 0.05, 'hata ∛3≠⁶√6')
esit(sqrt(2)*kok(3, 3), kok(72, 6), 'Ö19')
esit(kok(4, 3)*kok(4, 6), 2, 'Ö20')
esit(sqrt(kok(64, 3)), 2, 'Ö21a'); esit(sqrt(2*sqrt(2)), kok(8, 4), 'Ö21b')
ok(2*sqrt(3) < 3*sqrt(2), 'sıralama kuralı')
ok(round(3*math.sqrt(2), 2) == 4.24 and round(2*math.sqrt(5), 2) == 4.47, 'sıralama hata')
ok(sirala({'a': 2*sqrt(3), 'b': 3*sqrt(2), 'c': sqrt(15)}) == ['a', 'c', 'b'], 'Ö22')
ok(sirala({'a': sqrt(3), 'b': kok(5, 3), 'c': kok(30, 6)}) == ['b', 'a', 'c'] and 3**3 == 27 and 5**2 == 25, 'Ö23')
a_, b_ = sqrt(2), sqrt(3)
esit(sqrt(24) + sqrt(54), 5*a_*b_, 'Ö24')
esit(sqrt(R(9, 100)) + sqrt(R(121, 100)) - sqrt(R(16, 100)), 1, 'Ö25')
# Ders 2 sınıfta
esit(sqrt(75) - sqrt(27) + sqrt(12), 4*sqrt(3), 'S2-1')
esit(sqrt(6)*sqrt(15)*sqrt(10), 30, 'S2-2')
esit(sqrt(2)*kok(2, 3), kok(32, 6), 'S2-3')
esit(kok(sqrt(256), 4), 2, 'S2-4')
ok(sirala({'a': 3*sqrt(3), 'b': 2*sqrt(7), 'c': 4*sqrt(2)}) == ['a', 'b', 'c'], 'S2-5')

# ---------------- SUNUM Ders 3 ----------------
esit(1/kok(2, 3), kok(4, 3)/2, 'kural 1/∛2')
esit((sqrt(5) - sqrt(2))*(sqrt(5) + sqrt(2)), 3, 'kural eşlenik')
esit(R(6)/sqrt(2), 3*sqrt(2), 'Ö26a'); esit(R(10)/sqrt(5), 2*sqrt(5), 'Ö26b')
esit(3/(2*sqrt(6)), sqrt(6)/4, 'Ö27a'); esit(1/kok(2, 3), kok(4, 3)/2, 'Ö27b')
esit(1/(sqrt(5) - sqrt(2)), (sqrt(5) + sqrt(2))/3, 'Ö28')
esit(2/(3 + sqrt(7)), 3 - sqrt(7), 'Ö29')
esit(8/sqrt(2) + 1/(sqrt(2) - 1), 5*sqrt(2) + 1, 'Ö30')
esit(1/(3 - sqrt(8)) + 1/(3 + sqrt(8)), 6, 'Ö31')
esit(sp.expand((sqrt(3) + 1)*(sqrt(3) + 1)), 4 + 2*sqrt(3), 'Ö32 pay')
esit((sqrt(3) + 1)/(sqrt(3) - 1), 2 + sqrt(3), 'Ö32')
esit(sp.expand((sqrt(3) + sqrt(2))**2), 5 + 2*sqrt(6), 'kural iç içe kontrol')
esit(sqrt(5 + 2*sqrt(6)), sqrt(3) + sqrt(2), 'Ö33')
esit(sqrt(7 - 2*sqrt(12)), 2 - sqrt(3), 'Ö34a'); esit(sqrt(96), 2*sqrt(24), 'Ö34 ara')
esit(sqrt(10 + sqrt(96)), sqrt(6) + 2, 'Ö34b')
esit(sqrt(8 + sqrt(60)), sqrt(5) + sqrt(3), 'kural √(8+√60)')
# Ö35: pozitif çözüm tek ve yineleme 3'e yakınsar
ok([s for s in sp.solve(sp.Eq(X, sp.sqrt(6 + X)), X) if s > 0] == [3], 'Ö35 denklem')
t = 0.0
for _ in range(100):
    t = math.sqrt(6 + t)
ok(abs(t - 3) < 1e-12, 'Ö35 yineleme')
x = sqrt(3) + 1
esit(sp.expand(x*x - 2*x), 2, 'Ö36')
# Python köşesi
ok(round(math.sqrt(72), 4) == 8.4853 and round(6*math.sqrt(2), 4) == 8.4853 and math.isqrt(50) == 7, 'Python math')
ok(str(sqrt(72)) == '6*sqrt(2)' and str(sqrt(12) + sqrt(27)) == '5*sqrt(3)'
   and str(sp.radsimp(2/(3 + sqrt(7)))) == '3 - sqrt(7)', 'Python sympy')
# Ders 3 sınıfta
esit(R(12)/sqrt(6), 2*sqrt(6), 'S3-1')
esit(6/(sqrt(5) + sqrt(2)), 2*sqrt(5) - 2*sqrt(2), 'S3-2')
esit(1/(sqrt(3) - sqrt(2)) + 1/(sqrt(3) + sqrt(2)), 2*sqrt(3), 'S3-3')
esit(sqrt(9 + 2*sqrt(14)), sqrt(7) + sqrt(2), 'S3-4')
esit(sqrt(4 - 2*sqrt(3)), sqrt(3) - 1, 'S3-5')

# ---------------- DERS NOTU örnekleri ----------------
esit(sqrt(R(9, 100)) + kok(R(-8, 1000), 3), R(1, 10), 'N1a'); esit(kok(R(1, 81), 4), R(1, 3), 'N1b')
xs = [x for x in range(-100, 101) if 10 - 2*x >= 0]
ok(max(xs) == 5 and len([x for x in xs if x > 0]) == 5, 'N2')
esit(R(32)**R(3, 5) + R(81)**R(-1, 4), R(25, 3), 'N3')
ok([x for x in range(-20, 21) if kok(R(4)**x, 3) == 16] == [6], 'N4')
esit(kok(4**6, 3), 16, 'N4 kontrol')
esit(sqrt((sqrt(3) - 2)**2) + sqrt((sqrt(3) - 1)**2), 1, 'N5')
for xv in [-5, -1, R(-1, 3)]:
    for yv in [R(1, 2), 2, 7]:
        ok(sqrt(sp.sympify(xv)**2) + kok(sp.sympify(yv)**3, 3) - sqrt((xv - yv)**2) == 0, 'N6')
esit(sqrt(2**5 * 3**3), 12*sqrt(6), 'N7a'); esit(kok(2**7 * 5**4, 3), 20*kok(10, 3), 'N7b')
ok([a for a in range(1, 100) if a*a*5 == 180] == [6] and [b for b in range(1, 1000) if b == 8*5] == [40], 'N8')
esit(2*kok(5, 3), kok(40, 3), 'N8 b'); ok(6 + 40 == 46, 'N8 toplam')
ok(math.isqrt(130) == 11 and 4**3 < 100 < 5**3 and math.isqrt(28) == 5, 'N9')
ok(4 < float(kok(100, 3)) < 5 and 5 < 2*math.sqrt(7) < 6, 'N9 float')
esit(3*sqrt(8) - sqrt(50) + sqrt(32), 5*sqrt(2), 'N10')
esit(2*kok(24, 3) - kok(81, 3), kok(3, 3), 'N11')
esit((sqrt(12) + sqrt(75))*sqrt(3), 21, 'N12')
esit(sqrt(2)*sqrt(18) + sqrt(63)/sqrt(7), 9, 'N13')
esit(kok(2, 3)*kok(2, 4), kok(128, 12), 'N14a')
esit(sqrt(3*kok(3, 3)), kok(9, 3), 'N14b'); esit(3*kok(3, 3), kok(81, 3), 'N14 ara'); esit(kok(81, 6), kok(9, 3), 'N14 ara2')
ok(sirala({'a': sqrt(2), 'b': kok(3, 3), 'c': kok(5, 4)}) == ['a', 'b', 'c'] and (2**6, 3**4, 5**3) == (64, 81, 125), 'N15')
esit(sqrt(20) + sqrt(45) - sqrt(80), sqrt(5), 'N16'); ok(round(math.sqrt(5), 3) == 2.236, 'N16 yaklaşık')
esit(R(15)/sqrt(5) + sqrt(20), 5*sqrt(5), 'N17')
esit(R(2)/kok(4, 3), kok(2, 3), 'N18')
esit(3/(sqrt(7) + 2), sqrt(7) - 2, 'N19')
esit(sp.expand((sqrt(5) + sqrt(3))**2), 8 + 2*sqrt(15), 'N20 pay')
esit((sqrt(5) + sqrt(3))/(sqrt(5) - sqrt(3)), 4 + sqrt(15), 'N20')
x = 1/(sqrt(2) - 1)
esit(x, sqrt(2) + 1, 'N21 x'); esit(x - 1/x, 2, 'N21')
esit(sqrt(11 + 2*sqrt(30)), sqrt(6) + sqrt(5), 'N22a')
esit(sqrt(56), 2*sqrt(14), 'N22 ara'); esit(sqrt(9 - sqrt(56)), sqrt(7) - sqrt(2), 'N22b')
ok([s for s in sp.solve(sp.Eq(X, sp.sqrt(20 + X)), X) if s > 0] == [5], 'N23')
esit(sqrt(60), 2*sqrt(15), 'kural √60')

# ---------------- ÇÖZÜMLÜ ALIŞTIRMALAR ----------------
esit(kok(-8, 3) + kok(16, 4) - kok(-32, 5), 2, 'A1')
esit(sqrt(50) + sqrt(8) - sqrt(32), 3*sqrt(2), 'A2')
esit(sqrt(48)/sqrt(3) + sqrt(45)/sqrt(5), 7, 'A3')
esit(4/(sqrt(5) - 1), sqrt(5) + 1, 'A4')
esit(2*kok(4, 3), kok(32, 3), 'A5 ara'); esit(sqrt(2*kok(4, 3)), kok(32, 6), 'A5')
ok(sirala({'a': kok(3, 3), 'b': sqrt(2), 'c': kok(10, 6)}) == ['b', 'a', 'c'], 'A6')
esit(sqrt(8 + 2*sqrt(15)) - sqrt(8 - 2*sqrt(15)), 2*sqrt(3), 'A7')
xs = [x for x in range(-50, 51) if 3*x + 4 >= 0 and sqrt(3*x + 4) == 5]
ys = [y for y in range(-50, 51) if kok(2**(y + 1) if y + 1 >= 0 else R(1, 2**(-(y + 1))), 3) == 4]
ok(xs == [7] and ys == [5] and xs[0] + ys[0] == 12, 'A8')

# ---------------- KENDİNİZ ÇÖZÜN ----------------
esit(sqrt(R(4, 100)) + sqrt(R(144, 100)) - sqrt(R(25, 100)), R(9, 10), 'K1')
esit(kok(81, 4) + kok(-64, 3), -1, 'K2')
esit(sqrt(18), 3*sqrt(2), 'K3a'); esit(sqrt(75), 5*sqrt(3), 'K3b'); esit(sqrt(128), 8*sqrt(2), 'K3c')
esit(3*sqrt(2) + 5*sqrt(2) - 7*sqrt(2), sqrt(2), 'K4')
esit(sqrt(3)*sqrt(6)*sqrt(2), 6, 'K5')
esit(R(9)**R(3, 2) - R(32)**R(2, 5), 23, 'K6')
esit(sqrt((2 - sqrt(7))**2), sqrt(7) - 2, 'K7')
ok(math.isqrt(60) == 7 and 7 < math.sqrt(60) < 8, 'K8')
esit(R(6)/sqrt(3), 2*sqrt(3), 'K9')
esit(kok(3, 3)*sqrt(3), kok(243, 6), 'K10')
ok(sirala({'a': 2*sqrt(5), 'b': 3*sqrt(2), 'c': sqrt(19)}) == ['b', 'c', 'a'], 'K11')
esit(1/(sqrt(6) - sqrt(5)), sqrt(6) + sqrt(5), 'K12')
esit(2/(sqrt(3) + 1) + 2/(sqrt(3) - 1), 2*sqrt(3), 'K13')
esit(sqrt(6 - 2*sqrt(5)), sqrt(5) - 1, 'K14')
x = sqrt(2) + 1
esit(sp.expand(x*x), 3 + 2*sqrt(2), 'K15 ara'); esit(sp.expand(x*x - 2*x), 1, 'K15')
ok([s for s in sp.solve(sp.Eq(X, sp.sqrt(30 + X)), X) if s > 0] == [6], 'K16')
t = 0.0
for _ in range(100):
    t = math.sqrt(30 + t)
ok(abs(t - 6) < 1e-12, 'K16 yineleme')

print(f'Tüm kontroller geçti: {sayac} assert')
