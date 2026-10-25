# MMAT105 Hafta 2 -- sunum ve ders notundaki tüm sayısal cevapların doğrulanması
from math import gcd, isqrt

def asal(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

def bolenler(n):
    kucuk = [k for k in range(1, isqrt(n) + 1) if n % k == 0]
    return sorted(set(kucuk + [n // k for k in kucuk]))

def d(n):
    return len(bolenler(n))

def carpanlar(n):
    f, p = {}, 2
    while n > 1:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    return f

def fakt_us(n, p):  # n! içindeki p'nin üssü (brute force)
    s = 0
    for k in range(1, n + 1):
        while k % p == 0:
            s += 1
            k //= p
    return s

def tam_kare(n):
    return isqrt(n) ** 2 == n

def tam_kup(n):
    r = round(n ** (1 / 3))
    return any((r + e) ** 3 == n for e in (-1, 0, 1))

def en_kucuk(n, kosul):
    k = 1
    while not kosul(n * k):
        k += 1
    return k

gunler = ['pazartesi', 'salı', 'çarşamba', 'perşembe', 'cuma', 'cumartesi', 'pazar']
def gun_sonra(bugun, n):
    return gunler[(gunler.index(bugun) + n) % 7]

sayac = 0
def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1

# ---------------- Hatırlatma ----------------
ok([a + b for a in range(1, 10) for b in range(1, 10) if (10*a+b)+(10*b+a) == 132] and
   all(a + b == 12 for a in range(1, 10) for b in range(1, 10) if (10*a+b)+(10*b+a) == 132), 'H1')
ok(20 // 4 * 5 - 3**2 == 16, 'H2')
ok(720 // 24 == 30, 'H3')

# ---------------- SUNUM Ders 1 ----------------
P100 = [p for p in range(1, 101) if asal(p)]
ok(len(P100) == 25 and P100[-1] == 97, 'asal listesi')
ok(P100 == [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97], 'liste')
p30 = [p for p in range(1, 31) if asal(p)]
ok(len(p30) == 10 and sum(p30) == 129, 'Ö1')
p2050 = [p for p in range(21, 50) if asal(p)]
ok(len(p2050) == 7 and sum(p2050) == 251, 'Ö2')
iki = [p for p in range(10, 100) if asal(p)]
ok(max(iki) - min(iki) == 86, 'Ö3')
ok(not asal(91) and 91 == 7*13 and asal(97), 'Ö4')
ok(not asal(221) and 221 == 13*17 and asal(211) and isqrt(211) == 14 and isqrt(221) == 14, 'Ö5')
c = {a*b for a in range(2, 16) for b in range(2, 16) if asal(a) and asal(b) and a+b == 15}
ok(c == {26}, 'Ö6')
ok([p for p in range(2, 10000) if asal(p) and asal(p+5)] == [2], 'Ö7')
t = [(a, b, c_) for a in range(2, 30) for b in range(2, 30) for c_ in range(2, 30)
     if a < b < c_ and asal(a) and asal(b) and asal(c_) and a+b+c_ == 30]
ok({x[0] for x in t} == {2} and len(t) == 2 and {(x[1], x[2]) for x in t} == {(5,23),(11,17)}, 'Ö8')
t = [(a, b) for a in range(2, 40) for b in range(2, 40) if asal(a) and asal(b) and a*b+a == 39]
ok(t == [(13, 2)] and sum(t[0]) == 15, 'Ö9')
ok([gcd(*x) == 1 for x in [(8,15),(12,21),(14,25),(9,27)]] == [True, False, True, False], 'Ö10')
ok(sum(1 for x in range(1, 21) if gcd(x, 12) == 1) == 7, 'Ö11')
# Ders 1 sınıfta
ok([p for p in range(51, 70) if asal(p)] == [53,59,61,67], 'S1-1')
ok(not asal(143) and 143 == 11*13, 'S1-2')
ok({a*b for a in range(2, 21) for b in range(2, 21) if asal(a) and asal(b) and a+b == 21} == {38}, 'S1-3')
ok(sum(1 for x in range(1, 16) if gcd(x, 10) == 1) == 6, 'S1-4')
ok([p for p in range(10, 100) if asal(p) and p//10 + p % 10 == 10] == [19,37,73], 'S1-5')

# ---------------- SUNUM Ders 2 ----------------
ok(carpanlar(360) == {2:3, 3:2, 5:1}, 'Ö12')
ok(carpanlar(84) == {2:2, 3:1, 7:1} and sum(carpanlar(84)) == 12, 'Ö13a')
ok(carpanlar(150) == {2:1, 3:1, 5:2} and sum(carpanlar(150)) == 10, 'Ö13b')
ok(d(72) == 12 and bolenler(72) == [1,2,3,4,6,8,9,12,18,24,36,72], 'Ö14')
B = bolenler(360)
ok(len(B) == 24 and 2*len(B) == 48 and sum(1 for x in B if asal(x)) == 3
   and sum(1 for x in B if not asal(x)) == 21, 'Ö15')
ok(sum(1 for x in B if x % 2) == 6 and sum(1 for x in B if x % 2 == 0) == 18, 'Ö16')
ok([a for a in range(0, 20) if d(2**a * 9) == 18] == [5] and d(288) == 18, 'Ö17')
ok(d(12**3) == 28 and d(12) == 6, 'Ö18')
ok(sum(bolenler(12)) == 28 and sum(bolenler(72)) == 195, 'Ö19')
ok(en_kucuk(180, tam_kare) == 5 and 180*5 == 30**2, 'Ö20')
ok(en_kucuk(72, tam_kup) == 3 and 72*3 == 6**3, 'Ö21')
ok(fakt_us(20, 2) == 18 and fakt_us(20, 3) == 8, 'Ö22')
# Ders 2 sınıfta
ok(d(150) == 12, 'S2-1')
ok(2*d(200) == 24, 'S2-2')
ok([n for n in range(0, 20) if d(2**n * 5) == 10] == [4], 'S2-3')
ok(en_kucuk(48, tam_kare) == 3, 'S2-4')
ok(fakt_us(15, 3) == 6, 'S2-5')

# ---------------- SUNUM Ders 3 ----------------
ok(divmod(247, 9) == (27, 4), 'Ö23')
A = [a for a in range(0, 200) if a // 7 == 12]
ok(min(A) == 84 and max(A) == 90, 'Ö24')
Bmin = min(b for b in range(1, 100) if 11 < b)  # kalan 11 < bölen
ok(Bmin == 12 and divmod(12*6+11, 12) == (6, 11) and 12*6+11 == 83, 'Ö25')
A = [a for a in range(1, 1000) if a // 9 == a % 9]
ok(len(A) == 8 and max(A) == 80, 'Ö26')
t = [a for a in range(0, 1000) if a % 5 == 3 and (a//5) // 4 == 2 and (a//5) % 4 == 1]
ok(t == [48], 'Ö27')
ok({a % 15 for a in range(0, 5000) if a % 3 == 2 and (a//3) % 5 == 4} == {14}, 'Ö28')
ok({a % 3 for a in range(0, 1000) if a % 6 == 4} == {1}, 'Ö29')
R = [(a, b) for a in range(0, 200) for b in range(0, 200) if a % 7 == 3 and b % 7 == 5]
ok({(a+b) % 7 for a, b in R} == {1} and {(a*b) % 7 for a, b in R} == {1}
   and {(2*a+3*b) % 7 for a, b in R} == {0}, 'Ö30')
ok(gun_sonra('salı', 100) == 'perşembe', 'Ö31')
ok((437*128+59) == 55995 and (437*128+59) % 10 == 5, 'Ö32')
ok(2**26 % 10 == 4 and pow(3, 2026, 10) == 9, 'Ö33')
# Python köşesi
ok(divmod(247, 9) == (27, 4) and (3*5) % 7 == 1 and 2**26 % 10 == 4 and not asal(221), 'Python')
# Ders 3 sınıfta
ok(divmod(500, 13) == (38, 6), 'S3-1')
ok(max(a for a in range(0, 1000) if a // 11 == 8) == 98, 'S3-2')
R = [(a, b) for a in range(0, 200) for b in range(0, 200) if a % 9 == 5 and b % 9 == 7]
ok({(a+b) % 9 for a, b in R} == {3} and {(a*b) % 9 for a, b in R} == {8}, 'S3-3')
ok(2026*2027 % 10 == 2, 'S3-4')
ok(gun_sonra('pazartesi', 45) == 'perşembe', 'S3-5')

# ---------------- DERS NOTU örnekleri ----------------
t = [p for p in range(61, 80) if asal(p)]
ok(t == [61,67,71,73,79] and sum(t) == 351, 'N1')
ok(asal(307) and not asal(323) and 323 == 17*19 and isqrt(307) == 17 and isqrt(323) == 17, 'N2')
t = [(a, b) for a in range(2, 20) for b in range(2, 20) if a < b and asal(a) and asal(b) and asal(a+b) and a+b < 20]
ok(len(t) == 4, 'N3')
t = [(a, b) for a in range(2, 30) for b in range(2, 30) if asal(a) and asal(b) and 2*a+3*b == 23]
ok(t == [(7, 3)], 'N4')
ok(sum(1 for x in range(1, 31) if gcd(x, 15) == 1) == 16, 'N5')
ok(carpanlar(1260) == {2:2, 3:2, 5:1, 7:1} and sum(carpanlar(1260)) == 17 and d(1260) == 36, 'N6')
ok([a for a in range(0, 20) if d(8 * 3**a * 5) == 24] == [2], 'N7')
ok([n for n in range(0, 10) if d(10**n) == 49] == [6], 'N8')
ok(2*d(540) == 48 and sum(1 for x in bolenler(540) if not asal(x)) == 21, 'N9')
ok(sum(1 for x in bolenler(360) if x % 6 == 0) == 12, 'N10')
ok(sum(bolenler(36)) == 91, 'N11')
ok(en_kucuk(150, tam_kare) == 6 and 150*6 == 30**2 and en_kucuk(150, tam_kup) == 180 and 150*180 == 30**3, 'N12')
k = 0
while (1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20*21*22*23*24*25) % 6**(k+1) == 0:
    k += 1
ok(fakt_us(25, 3) == 10 and fakt_us(25, 2) == 22 and k == 10, 'N13')
A = [a for a in range(10, 100) if a // 9 + a % 9 == 12]
ok(min(A) == 44 and max(A) == 92, 'N14')
ok({a % 4 for a in range(0, 1000) if a % 12 == 7} == {3} and {a % 3 for a in range(0, 1000) if a % 12 == 7} == {1}, 'N15')
ok({a % 24 for a in range(0, 5000) if a % 4 == 3 and (a//4) % 6 == 5} == {23}, 'N16')
t = [(a, b) for b in range(1, 100) for a in range(0, 200) if a // b == 5 and a % b == 7 and a + b == 91]
ok(t == [(77, 14)], 'N17')
ok(max(a for a in range(0, 1000) if a // 8 == 13) == 111, 'N18')
ok({(x*x+3*x) % 8 for x in range(0, 1000) if x % 8 == 5} == {0}, 'N19')
ok(13*17*19*23 == 96577 and 96577 % 10 == 7 and pow(7, 2026, 10) == 9, 'N20')
ok(gun_sonra('cuma', 250) == 'çarşamba' and pow(8, 15, 10) == 2, 'N21')
ok({a**3 % 5 for a in range(0, 1000) if a % 5 == 3} == {2} and 512 % 5 == 2, 'N22')
ok([p for p in range(2, 5000) if asal(p) and asal(p*p+2)] == [3], 'N23')

# ---------------- DERS NOTU alıştırmaları ----------------
ok(len([p for p in range(31, 60) if asal(p)]) == 7, 'A1')
ok(not asal(187) and 187 == 11*17 and asal(191), 'A2')
ok({a*b for a in range(2, 31) for b in range(2, 31) if asal(a) and asal(b) and a+b == 31} == {58}, 'A3')
ok([p + p + 9 for p in range(2, 10000) if asal(p) and asal(p+9)] == [13], 'A4')
ok(sum(1 for x in range(1, 25) if gcd(x, 10) == 1) == 10, 'A5')
ok(carpanlar(252) == {2:2, 3:2, 7:1} and d(252) == 18, 'A6')
ok(2*d(400) == 30, 'A7')
ok([a for a in range(0, 20) if d(2**a * 125) == 20] == [4], 'A8')
ok(sum(1 for x in bolenler(120) if not asal(x)) == 13, 'A9')
ok(sum(1 for x in bolenler(90) if x % 2 == 0) == 6, 'A10')
ok(sum(bolenler(18)) == 39, 'A11')
ok(en_kucuk(108, tam_kup) == 2, 'A12')
ok(fakt_us(30, 5) == 7, 'A13')
A = [a for a in range(0, 1000) if a // 15 == 7]
ok(min(A) == 105 and max(A) == 119, 'A14')
ok({a % 21 for a in range(0, 5000) if a % 7 == 4 and (a//7) % 3 == 2} == {18}, 'A15')
R = [(a, b) for a in range(0, 300) for b in range(0, 300) if a % 11 == 6 and b % 11 == 9]
ok({(a+b) % 11 for a, b in R} == {4} and {(a*b) % 11 for a, b in R} == {10}, 'A16')
ok(pow(3, 50, 10) == 9, 'A17')
ok(max(a for a in range(1, 10000) if a // 9 == 2 * (a % 9)) == 152, 'A18')

print(f'Tüm kontroller geçti: {sayac} assert')

# --- 07.10.2026 ekleri: yeni alıştırmalar ---
assert sum(1 for d in range(1,361) if 360%d==0 and d%2==1)==6
assert all((5*A)%6==2 for A in range(4,1000,6))
assert [x for x in range(1,25) if x%2 and x%5]==[1,3,7,9,11,13,17,19,21,23]
assert sum(1 for d in range(1,121) if 120%d==0 and not (d>1 and all(d%k for k in range(2,d))))==13
assert max(A for A in range(1,1000) if A//9==2*(A%9))==152
print("Ekler geçti")
