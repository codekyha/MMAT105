# MMAT105 Hafta 1 -- sunum, ders notu ve alıştırmalardaki tüm sayısal cevapların doğrulanması
from fractions import Fraction as F
from math import factorial as fa
from itertools import product

sayac = 0
def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1

def rakamlar(n):
    return [int(c) for c in str(n)]

def farkli(n):
    r = rakamlar(n)
    return len(set(r)) == len(r)

def sifir(n):  # n! sonundaki sıfır sayısı (brute force)
    s, x = 0, fa(n)
    while x % 10 == 0:
        x //= 10
        s += 1
    return s

def birler(n):
    return n % 10

R = range(-12, 13)          # işaret / tek-çift taramaları için
NZ = [x for x in R if x != 0]

def isaret(x):
    return 'pozitif' if x > 0 else ('negatif' if x < 0 else 'sıfır')

def tur(x):
    return 'çift' if x % 2 == 0 else 'tek'

# ================= SUNUM: Isınma =================
ok(7 + (-5) == 2, 'I1'); ok(5 - (-8) == 13, 'I2'); ok(3 + 4*2 == 11, 'I3')
ok((-2)*(-6) == 12, 'I4'); ok(F(20, 4)*5 == 25, 'I5')

# ================= SUNUM: Ders 1 =================
vals = [F(-3), F(0), F(7), F(5, 2), F(12, 4), F(-8, 2)]
ok([v for v in vals if v.denominator == 1 and v >= 0] == [0, 7, 3], 'O1-dogal')
ok([v for v in vals if v.denominator == 1] == [-3, 0, 7, 3, -4], 'O1-tam')
ok(0 + 1 + (-1) == 0, 'O2')
ok(len([x for x in range(-10, 10) if -4 < x < 3]) == 6 and len([x for x in range(-10, 10) if -4 <= x <= 3]) == 8, 'O3')
ok([int(c) * 10**(3 - i) for i, c in enumerate('2403')] == [2000, 400, 0, 3], 'O4')
ok(3050 - sum(rakamlar(3050)) == 3042, 'O5')
ok(max(range(10, 100)) + min(range(10, 100)) == 109, 'O6')
U = [n for n in range(100, 1000) if farkli(n)]
ok(max(U) - min(U) == 885 and max(U) == 987 and min(U) == 102, 'O7')
ok(min(n for n in range(-99, 100) if 10 <= abs(n) <= 99 and farkli(abs(n))) == -98, 'O8')
ok(len(range(10, 100)) == 90 and sum(1 for n in range(10, 100) if farkli(n)) == 81, 'O9')
S10 = {a + b for a in range(1, 10) for b in range(1, 10) if (10*a+b) + (10*b+a) == 121}
ok(S10 == {11}, 'O10')
S11 = [(a, b) for a in range(1, 10) for b in range(1, 10) if (10*a+b) - (10*b+a) == 54]
ok({a - b for a, b in S11} == {6} and max(10*a+b for a, b in S11) == 93, 'O11')
S12 = {a - c for a in range(1, 10) for b in range(10) for c in range(1, 10) if (100*a+10*b+c) - (100*c+10*b+a) == 396}
ok(S12 == {4}, 'O12')
ok([n for n in range(10, 100) if n == 4*sum(rakamlar(n))] == [12, 24, 36, 48], 'O13')
ok(all((100*(a+2) + 10*b + (c-3)) - (100*a+10*b+c) == 197 for a in range(1, 8) for b in range(10) for c in range(3, 10)), 'O14')
# Sınıfta Siz Çözün -- Ders 1
ok(min(n for n in range(1000, 10000) if farkli(n)) == 1023, 'D1S1')
ok({a + b for a in range(1, 10) for b in range(1, 10) if (10*a+b) + (10*b+a) == 88} == {8}, 'D1S2')
ok({a - b for a in range(1, 10) for b in range(1, 10) if (10*a+b) - (10*b+a) == 45} == {5}, 'D1S3')
ok(all((400 + 10*(a+3) + 7) - (400 + 10*a + 7) == 30 for a in range(0, 7)), 'D1S4')
ok(len([x for x in range(-20, 20) if -6 < x < 5]) == 10, 'D1S5')

# ================= SUNUM: Ders 2 =================
ok(18 - F(12, 3)*2 + 5 == 15, 'O15')
ok(F(48, 4)/2 == 6 and 48/F(4, 2) == 24, 'O16')
ok(5 - 3*(2-6) + 2**3 == 25, 'O17')
ok(3 + 2*(10 - (4-1)**2) == 5, 'O18')
ok((8 - (6 - (4-2)))*3 == 12, 'O19')
ok(F(12 - 3*2, 2*3 - 3) + 2**3*3 - F(4**2, 8) == 24, 'O20')
ok(-7 + (-5) - (-12) == 0 and (-2)*(-3)*(-1)*4 == -24, 'O21')
ok((-3)**2 - 2**3 == 1 and (-2)**4 - (-3)**3 == 43, 'O22')
ok(-2**2 + (-2)**2 == 0 and (-1)**2026 + (-1)**2027 - 1**2028 == -1, 'O23')
P = [(a, b) for a in R for b in R if a < 0 < b]
ok({isaret(a*b) for a, b in P} == {'negatif'} and {isaret(b-a) for a, b in P} == {'pozitif'}
   and {isaret(a-b) for a, b in P} == {'negatif'} and {isaret(a*a*b) for a, b in P} == {'pozitif'}, 'O24')
P = [(a, b, c) for a in R for b in R for c in R if a*b < 0 and b*c > 0 and c < 0]
ok({isaret(a) for a, b, c in P} == {'pozitif'} and {isaret(b) for a, b, c in P} == {'negatif'}, 'O25')
ok({isaret(b) for a in R for b in R if a < 0 and a**3*b > 0} == {'negatif'}, 'O26')
P = [(x, y) for x in R for y in R if x % 2 == 1 and y % 2 == 0]
ok({tur(x+y) for x, y in P} == {'tek'} and {tur(x*y) for x, y in P} == {'çift'}
   and {tur(x*x+y) for x, y in P} == {'tek'} and {tur(3*x+2*y) for x, y in P} == {'tek'}, 'O27')
P = [(x, y) for x in R for y in R if (3*x+2*y) % 2 == 1]
ok({tur(x) for x, y in P} == {'tek'} and {tur(y) for x, y in P} == {'tek', 'çift'}, 'O28')
ok({tur(a+c) for a in R for b in R for c in R if (a+b) % 2 == 1 and (b+c) % 2 == 0} == {'tek'}, 'O29')
ok({tur(b) for a in R for b in R if (a*b) % 2 == 0 and a % 2 == 1} == {'çift'}
   and {(tur(a), tur(b)) for a in R for b in R if (a*b) % 2 == 1} == {('tek', 'tek')}, 'O30')
# Bilgisayar köşesi
ok(20/4*5 == 25.0 and -3**2 == -9 and (-3)**2 == 9 and 2**3**2 == 512, 'BK1')
ok(2403 % 10 == 3 and 2403 // 10 % 10 == 0 and 7 % 2 == 1, 'BK2')
# Sınıfta Siz Çözün -- Ders 2
ok(F(24, 4)*3 - 2**3 == 10, 'D2S1')
ok(-3**2 - (-3)**2 + (-1)**101 == -19, 'D2S2')
P = [(a, b) for a in R for b in R if a > 0 > b]
ok({isaret(a*b*b) for a, b in P} == {'pozitif'} and {isaret(b-a) for a, b in P} == {'negatif'}, 'D2S3')
ok({tur(5*x+7) for x in R if x % 2 == 0} == {'tek'}, 'D2S4')
ok({isaret(b) for a in R for b in R for c in R if a*b*c < 0 and a < 0 and c > 0} == {'pozitif'}, 'D2S5')

# ================= SUNUM: Ders 3 =================
T = list(range(5, 63, 3)); ok(T[-1] == 62 and len(T) == 20 and sum(T) == 670, 'O31')
ok(sum(range(1, 31)) == 465 and sum(range(11, 31)) == 410, 'O32')
ok(sum(range(2, 51, 2)) == 650 and sum(range(1, 50, 2)) == 625, 'O33')
ok([x + 4 for x in range(-200, 200) if sum(range(x, x+5)) == 85] == [19], 'O34')
ok([x + 4 for x in range(-200, 200, 2) if x + (x+2) + (x+4) == 78] == [28], 'O35')
T = [x for x in range(41, 120) if x % 2 == 1]; ok(len(T) == 40 and sum(T) == 3200, 'O36')
ok(sum(len(str(k)) for k in range(1, 121)) == 252, 'O37')
ok(fa(8)//fa(6) == 56 and fa(7)//(fa(4)*fa(3)) == 35, 'O38')
ok(F(fa(8) - fa(7), fa(6)) == 49, 'O39')
ok([n for n in range(1, 50) if fa(n+1) == 20*fa(n-1)] == [4], 'O40')
ok(sifir(100) == 24, 'O41')
ok(min(n for n in range(1, 200) if sifir(n) == 6) == 25 and 5 not in {sifir(n) for n in range(1, 200)}
   and sifir(24) == 4 and sifir(20) == 4, 'O42')
s43 = sum(fa(k) for k in range(1, 22, 2)); ok(birler(s43) == 7 and s43 % 2 == 1, 'O43')
# Sınıfta Siz Çözün -- Ders 3
T = list(range(4, 100, 5)); ok(T[-1] == 99 and len(T) == 20 and sum(T) == 1030, 'D3S1')
ok([x for x in range(-200, 200, 2) if 4*x + 12 == 92] == [20], 'D3S2')
ok(sum(range(1, 21)) == 210, 'D3S3')
ok(fa(12)//(fa(10)*fa(2)) == 66, 'D3S4')
ok(sifir(75) == 18, 'D3S5')

# ================= DERS NOTU örnekleri =================
A = [x for x in range(-20, 20) if -3 < x <= 4]
ok(len(A) == 7 and [x for x in A if x >= 0] == [0, 1, 2, 3, 4], 'N1')
ok(max((10*a+b) + (10*b+a) for a in range(1, 10) for b in range(1, 10) if a != b) == 187, 'N2')
ok([a for a in range(1, 10) if (30+a) + (10*a+3) == 77] == [4], 'N3')
ok([x for x in range(10, 100) if (10*x+5) - x == 419] == [46], 'N4')
ok(F(3**2 - 2*(5-8), (-1)**3 + 2**2) == 5, 'N5')
ok(-(-2)**3 - 3*(-4 + 2*(1-3)) == 32, 'N6')
P = [(a, b, c) for a in R for b in R for c in R if a < b < 0 < c]
ok({isaret(F(a*c, b)) for a, b, c in P} == {'pozitif'} and {isaret((a-b)*c) for a, b, c in P} == {'negatif'}, 'N7')
ok({(-1)**n + (-1)**(n+1) + (-1)**(2*n) for n in range(1, 200)} == {1}, 'N8')
P = [(a, b) for a in R for b in R if a % 2 == 0 and (a*a + 3*b) % 2 == 1]
ok({tur(b) for a, b in P} == {'tek'} and {tur(a*b+b) for a, b in P} == {'tek'}, 'N9')
T = list(range(7, 153, 5)); ok(T[-1] == 152 and len(T) == 30 and sum(T) == 2385, 'N10')
ok(sum(range(2, 41, 2)) - sum(range(1, 40, 2)) == 20, 'N11')
ok([x for x in range(-201, 200) if x % 2 != 0 and x+(x+2)+(x+4)+(x+6) == 72] == [15], 'N12')
ok(sum(1 for n in range(100, 1000) if n % 7 == 0) == 128, 'N13')
ok(fa(9)//(fa(7)*fa(3)) == 12 and (fa(6)+fa(7)+fa(8))//fa(6) == 64, 'N14')
ok([n for n in range(1, 50) if fa(n) + fa(n-1) == 7*fa(n-1)] == [6], 'N15')
ok(sifir(50) == 12, 'N16')
ok(birler(sum(fa(k) for k in range(1, 11))) == 3, 'N17')

# ================= ÇÖZÜMLÜ ALIŞTIRMALAR =================
ok(max(n for n in range(100, 1000) if farkli(n) and n % 2 == 0) - min(n for n in range(100, 1000) if farkli(n) and n % 2 == 1) == 883, 'C1')
ok({a*c for a in range(1, 10) for b in range(10) for c in range(1, 10)
    if (100*a+10*b+c) - (100*c+10*b+a) == 594 and a + c == 12} == {27}, 'C2')
ok(F((-2)**3 + F(4**2, 2), -3**2 + 10) == 0, 'C3')
P = [(x, y, z) for x in R for y in R for z in R if (x*y) % 2 == 1 and (x+z) % 2 == 0]
ok({tur(z) for x, y, z in P} == {'tek'} and {tur(x+y+z) for x, y, z in P} == {'tek'}, 'C4')
T = list(range(13, 98, 4)); ok(T[-1] == 97 and len(T) == 22 and sum(T) == 1210, 'C5')
ok([x + 4 for x in range(-200, 200) if sum(range(x, x+5)) == -15] == [-1], 'C6')
ok([n for n in range(0, 50) if fa(n+2) // fa(n) == 56] == [6], 'C7')
s = sum(fa(k) for k in range(2, 21, 2)); ok(birler(s) == 6 and s % 2 == 0, 'C8')

# ================= KENDİNİZ ÇÖZÜN =================
ok(len([x for x in range(0, 50) if x < 5]) == 5 and len([x for x in range(-50, 50) if -2 <= x < 3]) == 5, 'K1')
ok(len([x for x in range(-50, 50) if -7 < x < 6]) == 12, 'K2')
ok([10*a+b for a in range(1, 10) for b in range(1, 10) if (10*a+b) + (10*b+a) == 143 and a - b == 5] == [94], 'K3')
ok([n for n in range(10, 100) if n == 7*sum(rakamlar(n))] == [21, 42, 63, 84], 'K4')
ok(F(36, 6)*2 - 3*(2-5)**2 == -15, 'K5')
ok(-2**4 + (-2)**3 - (-1)**99 == -23, 'K6')
P = [(a, b, c) for a in R for b in R for c in R if a*b > 0 and b*c < 0 and a < 0]
ok({(isaret(b), isaret(c), isaret(a*c)) for a, b, c in P} == {('negatif', 'pozitif', 'negatif')}, 'K7')
ok({tur(b) for a in R for b in R if a % 2 == 1 and (a*a*b + a) % 2 == 0} == {'tek'}, 'K8')
ok(sum(range(1, 60, 2)) == 900 and sum(range(2, 61, 2)) == 930, 'K9')
ok([x + 4 for x in range(-201, 200) if x % 2 == 1 and x + (x+2) + (x+4) == 117] == [41], 'K10')
ok(sum(1 for n in range(10, 100) if n % 6 == 0) == 15, 'K11')
ok(sum(range(11, 41)) == 765, 'K12')
ok(fa(10)//fa(8) - fa(7)//fa(5) == 48, 'K13')
ok(F(fa(7) + fa(8), 9*fa(6)) == 7, 'K14')
ok(sifir(40) == 9, 'K15')

print(f'Tüm kontroller geçti: {sayac} assert')
