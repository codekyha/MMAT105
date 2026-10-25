# MMAT105 Hafta 9 -- sunum, ders notu ve alıştırmalardaki tüm sayısal cevapların doğrulanması
# Üslü sayılar: tüm hesaplar Fraction (tam kesir) ile yapılır, ondalık yuvarlama yok.
from fractions import Fraction as F
from math import gcd

def us(a, n):
    """a^n (a kesir/tam sayı, n tam sayı); 0^0 ve 0^(negatif) tanımsız -> None"""
    a = F(a)
    if a == 0 and n <= 0:
        return None
    return a ** n

def coz(f, aralik=range(-50, 51)):
    """f(x) True olan tam sayı x değerleri (tanımsızlar elenir)"""
    out = []
    for x in aralik:
        try:
            if f(x):
                out.append(x)
        except (ZeroDivisionError, TypeError):
            pass
    return out

def esit(a, b):
    return a is not None and b is not None and a == b

def bilimsel(x):
    """x = a*10^n, 1<=|a|<10 -> (a, n) tam kesir olarak"""
    x = F(x); n = 0
    while abs(x) >= 10: x /= 10; n += 1
    while abs(x) < 1: x *= 10; n -= 1
    return x, n

def sirala(d):
    return sorted(d, key=lambda k: d[k])

sayac = 0
def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1

# ---------------- Hatırlatma (Hafta 7) ----------------
X = [F(k, 4) for k in range(-200, 201)]
ok([x for x in X if 3*x - 5 >= 7] == [x for x in X if x >= 4], 'H1')
ok(coz(lambda x: abs(x - 3) == 5) == [-2, 8], 'H2')
ok(coz(lambda x: abs(2*x + 1) < 5) == [-2, -1, 0, 1], 'H3')

# ---------------- SUNUM Ders 1 ----------------
ok(us(2,5) == 32 and us(3,4) == 81 and us(F(2,3),3) == F(8,27) and us(10,6) == 10**6, 'Ö1')
ok(us(-2,4) == 16 and -us(2,4) == -16 and us(-2,3) == -8 and -us(-2,3) == 8, 'Ö2')
ok(us(-1,2026) + us(-1,2027) - us(1,100) + us(0,5) == -1, 'Ö3')
ok(us(7,0) == 1 and us(-5,0) == 1 and -us(5,0) == -1 and us(3-3,0) is None, 'Ö4')
ok(us(2,-3) == F(1,8) and us(5,-1) == F(1,5) and us(-3,-2) == F(1,9) and us(10,-4) == F(1,10000), 'Ö5')
ok(us(F(2,3),-2) == F(9,4) and us(F(1,4),-2) == 16 and us(F(-1,2),-3) == -8, 'Ö6')
ok(us(F('0.2'),-2) == 25 and us(F('0.5'),-3) == 8 and us(F('0.1'),-3) == 1000 and us(F('1.5'),-2) == F(4,9), 'Ö7')
ok(us(F(1,2),-3) + us(-2,2) + us(-3,0) - us(1,2026) == 12, 'Ö8')
ok(-us(3,2) + us(-3,2) - us(-2,3) - us(2,-1)*4 == 6, 'Ö9')
for a in [F(-1), F(-3), F(-1,2), F(-7,3)]:
    ok(a**3 < 0 and a**4 > 0 and -a**2 < 0 and (-a)**5 > 0, 'Ö10')
x = -1
ok(-x**2 - x**3 + (-x)**4 == 1, 'Ö11')
# Ders 1 sınıfta
ok(us(-3,3) + us(-2,4) - us(4,0) == -12, 'S1-1')
ok(-us(2,2) + us(-2,2) == 0, 'S1-2')
ok(us(F(3,2),-2) + us(F('0.5'),-1) == F(22,9), 'S1-3')
ok(us(-1,15) - us(-1,20) + us(0,9) == -2, 'S1-4')
ok(us(-2,-1) + us(-2,-2) == F(-1,4), 'S1-5')

# ---------------- SUNUM Ders 2 ----------------
ok(us(2,3)*us(2,4)*us(2,-5) == 4 and us(5,9)/us(5,7) == 25, 'Ö12')
ok(us(us(2,3),2) == 64 and us(2,3**2) == 512 and us(us(3,-2),-1) == 9, 'Ö13')
ok(us(2,12)*us(5,12)/us(10,10)*us(us(10,2),3) == us(10,8), 'Ö14')
ok(us(12,4)/us(4,4) == 81 and us(6,5)/(us(2,5)*us(3,4)) == 3, 'Ö15')
ok(us(16,3)*us(4,2)/us(8,5) == 2, 'Ö16')
ok(us(F('0.25'),-2)*us(8,-1) == 2 and us(27,2)*us(9,-3)*3 == 3, 'Ö17')
ok(all(us(4,x+1)*us(8,x) == us(2,5*x+2) for x in range(-10, 11)), 'Ö18')
ok(all(us(9,x+1) == 9*us(3,x)**2 and us(3,x-1) == us(3,x)/3 for x in range(-10, 11)), 'Ö19')
ok(3*us(2,5) + 4*us(2,5) - us(2,5) == 192 and us(2,10) - us(2,9) == 512, 'Ö20')
ok(all(us(2,x+3) - us(2,x+1) + us(2,x) == 7*us(2,x) for x in range(-10, 11)), 'Ö21')
ok((us(2,10)+us(2,9))/(us(2,9)-us(2,8)) == 6, 'Ö22')
ok((us(3,20)+us(3,19)+us(3,18))/(13*us(3,17)) == 3, 'Ö23')
ok(bilimsel(F(3*10**5) * F(4, 10**8)) == (F(12,10), -2), 'Ö24a')
ok(bilimsel(F('8.4')*10**6 / (F('2.1')*F(1,100))) == (4, 8), 'Ö24b')
# kural çerçevesi örnekleri
ok(all(us(2,x+2) + us(2,x) == 5*us(2,x) for x in range(-10, 11)), 'kural 2^(x+2)+2^x')
ok(us(2,3) + us(2,4) == 24 and us(2,7) == 128 and us(2,5) + us(2,5) == us(2,6), 'kural toplama')
ok(12*F(1,1000) == F('1.2')*F(1,100), 'kural 12*10^-3')
ok(all(us(4,x) == us(2,2*x) and us(8,x+1) == us(2,3*x+3) for x in range(-5, 6)), 'kural tabanlar')
ok(us(F('0.5'),1) == us(2,-1) and F('0.25') == us(2,-2) and F('0.125') == us(2,-3)
   and F('0.2') == us(5,-1) and F('0.04') == us(5,-2) and F(1,9) == us(3,-2), 'tablo')
# Ders 2 sınıfta
ok(us(2,7)*us(2,-3)/us(2,2) == 4, 'S2-1')
ok(us(6,4)/(us(2,4)*us(3,3)) == 3, 'S2-2')
ok((us(2,8)+us(2,7))/us(2,6) == 6, 'S2-3')
ok(all(us(4,x) + us(2,x+3) == us(2,x)**2 + 8*us(2,x) for x in range(-10, 11)), 'S2-4')
ok(bilimsel(F(4,1000) * 5*10**7) == (2, 5), 'S2-5')

# ---------------- SUNUM Ders 3 ----------------
ok(sirala({'a': 2**30, 'b': 3**20, 'c': 5**10}) == ['c', 'a', 'b'], 'Ö25')
ok(sirala({'a': 4**15, 'b': 8**11, 'c': 16**8}) == ['a', 'c', 'b'], 'Ö26')
ok(us(F('0.5'),3) < us(F('0.5'),2) < us(F('0.5'),-1) and us(F('0.5'),3) == F(1,8), 'Ö27')
ok(coz(lambda x: us(2,x) == 32) == [5] and coz(lambda x: us(3,2*x-1) == 27) == [2], 'Ö28')
ok(coz(lambda x: us(5,x+4) == us(125,x-2)) == [5], 'Ö29')
ok(coz(lambda x: us(F(4,9),x) == us(F(3,2),x-6)) == [2], 'Ö30')
ok(coz(lambda x: us(3,x-2) == us(5,x-2)) == [2] and coz(lambda x: us(7,2*x-6) == 1) == [3], 'Ö31')
ok(coz(lambda x: us(3,x+1) + us(3,x) == 36) == [2], 'Ö32')
ok(coz(lambda x: us(5,x+1) + us(5,x) + us(5,x-1) == 155) == [2], 'Ö33')
ok(coz(lambda x: esit(us(x-2,x+3), us(x-2,2*x-1))) == [2, 3, 4], 'Ö34')
ok(pow(7, 2027, 10) == 3 and [pow(7,k,10) for k in range(1,5)] == [7,9,3,1], 'Ö35')
# kural çerçevesi: (-1)^2 = (-1)^4, 1^x = 1^y
ok(us(-1,2) == us(-1,4) and us(1,3) == us(1,8), 'kural istisna')
# Python köşesi
ok((2**30, 3**20, 5**10) == (1073741824, 3486784401, 9765625) and 2**-3 == 0.125
   and pow(7, 2027, 10) == 3 and F(2,3)**-2 == F(9,4) and (2**10+2**9) // (2**9-2**8) == 6
   and -3**2 == -9 and (-3)**2 == 9, 'Python')
# Ders 3 sınıfta
ok(coz(lambda x: us(9,x+1) == us(27,x)) == [2], 'S3-1')
ok(coz(lambda x: us(2,x+1) + us(2,x) == 24) == [3], 'S3-2')
ok(sirala({'a': 3**40, 'b': 4**30, 'c': 5**20}) == ['c', 'b', 'a'], 'S3-3')
ok(coz(lambda x: us(6,x-4) == 1) == [4], 'S3-4')
ok(coz(lambda x: us(F(1,2),x) == 8) == [-3], 'S3-5')

# ---------------- DERS NOTU örnekleri ----------------
ok(-us(2,4) + us(-2,4) - us(-1,99) - us(0,8) == 1, 'N1')
ok(us(F(-1,3),-2) + us(F('0.25'),-1) - us(F(2,5),-1) == F(21,2), 'N2')
ok(us(2,-1) + us(3,-1) == F(5,6) and us(2+3,-1) == F(1,5), 'N3')
a = -3
ok(a**2 - a**3 - (-a)**2 + a**0 == 28, 'N4')
ok(all(us(us(a,3),4)*us(a,-5)/us(us(a,2),3) == a for a in [F(2), F(-3), F(1,2)]), 'N5')
ok(us(25,3)*us(125,-2)/us(5,-4) == 625, 'N6')
ok(us(F('0.04'),-1)*us(F('0.2'),3) == F('0.2') and 25*F('0.008') == F('0.2'), 'N7')
ok(us(18,5)/(us(2,4)*us(9,5)) == 2, 'N8')
ok(all(F('0.01')*us(10,2*x+1) == us(10,x)**2/10 for x in range(-6, 7)), 'N9')
ok(all((us(3,x+2)-us(3,x))/(us(3,x+1)+us(3,x)) == 2 for x in range(-10, 11)), 'N10')
ok(4*us(4,5) == us(2,12) and 2*us(2,20) == us(2,21), 'N11')
ok((us(5,12)-us(5,11))/(us(5,11)+us(5,10)) == F(10,3), 'N12')
ok(F('0.00048')*25000000/F('0.0006') == 2*10**7 and bilimsel(F('0.00048')*25000000/F('0.0006')) == (2, 7), 'N13')
ok(bilimsel(3*10**8 * F('3.15')*10**7) == (F('9.45'), 15), 'N14')
ok(sirala({'a': us(F('0.5'),-10), 'b': us(4,6), 'c': us(8,3)}) == ['c', 'a', 'b'], 'N15')
ok(sirala({'a': 2**45, 'b': 3**30, 'c': 7**15}) == ['c', 'a', 'b'], 'N16')
ok(coz(lambda x: us(27,x-1) == us(9,x+1)) == [5], 'N17')
ok(coz(lambda x: us(F('0.2'),x+1) == us(125,x-3)) == [2] and F('0.2')**3 == F(1,125), 'N18')
ok(coz(lambda x: us(2,x+3) + us(2,x+1) - us(2,x) == 72) == [3], 'N19')
xs = coz(lambda x: us(2,x-3) == us(3,x-3)); ys = coz(lambda y: us(5,y+1) == 1)
ok(xs == [3] and ys == [-1] and xs[0] + ys[0] == 2, 'N20')
ok(coz(lambda x: esit(us(x+1,2*x), us(x+1,x+3))) == [0, 3], 'N21')
ok(pow(8, 43, 10) == 2 and [pow(8,k,10) for k in range(1,5)] == [8,4,2,6], 'N22')
ok(all(us(2,x+3) + us(2,x) == 9*us(2,x) for x in range(-10, 11)), 'not dikkat')
ok(3*us(3,5) == us(3,6) and us(3,6) != us(3,15) and us(3,6) != us(9,5), 'not dikkat 2')

# ---------------- ÇÖZÜMLÜ ALIŞTIRMALAR ----------------
ok(us(-2,3) + us(-1,2023) - us(-4,2) + us(3,0) == -24, 'A1')
ok(us(F(2,3),-2) + us(F(1,2),-3) == F(41,4), 'A2')
ok(us(F('0.2'),-1) + us(F('0.5'),-2) == 9, 'A3')
ok(us(us(2,3),4)*us(us(2,-2),5)*us(8,2) == 256, 'A4')
ok((us(3,11)+us(3,10))/(us(3,10)-us(3,9)) == 6, 'A5')
ok(coz(lambda x: us(8,x+1) == us(16,x-1)) == [7] and 8**8 == 2**24 == 16**6, 'A6')
ok(coz(lambda x: us(2,x+1) + us(2,x) + us(2,x-1) == 56) == [4], 'A7')
ok(sirala({'a': 2**60, 'b': 3**40, 'c': 5**20}) == ['c', 'a', 'b'], 'A8')

# ---------------- KENDİNİZ ÇÖZÜN (1-14) ----------------
ok(-us(5,2) + us(-5,2) - us(-2,4) == -16, 'K1')
ok(us(2,-3) + us(3,-1) - us(4,-1) == F(5,24), 'K2')
ok(us(F('0.1'),-2) + us(F('0.5'),-1) == 102, 'K3')
ok(all(us(2,x)*us(2,5)*us(2,-3) == us(2,x+2) for x in range(-10, 11)), 'K4')
ok(us(3,12)*us(3,-4)/us(3,5) == 27, 'K5')
ok(us(9,3)*us(27,-2)*81 == 81, 'K6')
ok(bilimsel(14500000) == (F('1.45'), 7) and bilimsel(F('0.000025')) == (F('2.5'), -5), 'K7')
ok(bilimsel(F(6,1000) * 5*10**8) == (3, 6), 'K8')
ok(all(us(8,x+1) == 8*us(2,x)**3 for x in range(-10, 11)), 'K9')
ok(coz(lambda x: us(3,2*x-1) == 243) == [3], 'K10')
ok(coz(lambda x: us(F(1,3),x-1) == us(9,x+2)) == [-1], 'K11')
ok(coz(lambda x: us(3,x+2) - us(3,x) == 72) == [2], 'K12')
ok(sirala({'a': 4**12, 'b': 3**18, 'c': 2**30}) == ['a', 'b', 'c'], 'K13')
ok(coz(lambda x: esit(us(x-1,2*x), us(x-1,x+4))) == [0, 1, 2, 4], 'K14')

print(f'Tüm kontroller geçti: {sayac} assert')
