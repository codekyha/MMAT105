# -*- coding: utf-8 -*-
"""MMAT105 Hafta 5 -- sunum ve ders notundaki tüm sayısal cevapların doğrulaması.
Çalıştırma: python3 dogrulama.py
"""
from fractions import Fraction as F
from sympy import symbols, Rational as R, S, solveset, Eq, Interval, FiniteSet, \
    Complement, Union, simplify, expand, Poly, solve

x, t, m, n, a, b, k = symbols('x t m n a b k')
RE = S.Reals
sayac = 0


def kok(ifade_sol, ifade_sag, beklenen):
    """Denklemin gerçek sayılardaki çözüm kümesini beklenenle karşılaştırır."""
    global sayac
    cs = solveset(Eq(ifade_sol, ifade_sag), x, RE)
    if not isinstance(beklenen, (set, type(S.EmptySet))) and beklenen not in (RE,) \
            and not hasattr(beklenen, 'is_Set'):
        beklenen = FiniteSet(beklenen)
    assert cs == beklenen, (ifade_sol, ifade_sag, cs, beklenen)
    sayac += 1


def esit(deger, beklenen, etiket=''):
    global sayac
    assert simplify(S(deger) - S(beklenen)) == 0, (etiket, deger, beklenen)
    sayac += 1


def katsayi_kosulu(sol, sag):
    """sol=sag lineer denkleminin (A x + B = 0) A ve B katsayılarını döndürür."""
    p = Poly(expand(sol - sag), x)
    A = p.coeff_monomial(x)
    B = p.coeff_monomial(1)
    return A, B


# ================= SUNUM =================
# Geçen hafta hatırlatma
esit(R(2, 3) + R(5, 6) - R(1, 4), R(5, 4), 'H1')
esit(R(1, 3) + R(15, 90), R(1, 2), 'H2')          # 0,(3)=1/3 ; 0,1(6)=(16-1)/90=15/90=1/6
esit(R(16 - 1, 90), R(1, 6), 'H2b')
vals = {'a': R(2, 3), 'b': R(3, 5), 'c': R(5, 8)}
assert sorted(vals, key=lambda s: vals[s]) == ['b', 'c', 'a']; sayac += 1

# ---- Ders 1 ----
# S1: 2x+3=11 tek kök 4 ; 2(x+3)=2x+6 özdeşlik
kok(2*x + 3, 11, 4)
kok(2*(x + 3), 2*x + 6, RE)
# S2 terazi: 3x+2 = x+10
kok(3*x + 2, x + 10, 4)
# S3
kok(5*x - 7, 18, 5)
# S4
kok(3*x + 5, x + 9, 2)
# S5
kok(7 - 3*x, 2*x - 8, 3)
# S6
kok(3*(x - 2) - 2*(x + 1), 4, 12)
# S7
kok(5 - 2*(3 - x), 4*(x - 1) + 1, 1)
# S8
kok(2*(x - 3*(x - 1)), x + 1, 1)
# S9 sağlama: x=-1 kök değil, doğru kök -5
assert 4*(-1 + 1) != 2*(-1) - 6; sayac += 1
kok(4*(x + 1), 2*x - 6, -5)
esit(4*(-5 + 1), -16); esit(2*(-5) - 6, -16)
# S10: 3x=5x -> x=0
kok(3*x, 5*x, 0)
# S11
kok(-(x - 4) + 3, 2*(5 - x), 3)
# Ders 1 sınıfta siz çözün
kok(4*x - 9, 11, 5)
kok(2*(x + 3), x + 10, 4)
kok(7 - (x - 2), 3*x - 3, 3)
kok(3*(2*x - 1) - 2*(x + 4), 5, 4)
kok(5*x, -2*x, 0)

# ---- Ders 2 ----
kok(x/2 + x/3, 10, 12)                                      # S12
kok((x - 1)/3 - (x + 2)/4, 1, 22)                           # S13
kok((2*x + 1)/5 - (x - 3)/2, 1, 7)                          # S14
kok(R(2, 10)*x + R(15, 10), R(5, 10)*x - R(3, 10), 6)       # S15
kok(R(12, 100)*x + R(3, 10), R(6, 100)*x + R(9, 10), 10)    # S16
kok(2*(x + 3) - x, x + 6, RE)                               # S17a
kok(3*x - 2, 3*(x + 1), S.EmptySet)                         # S17b
# S18: (m-2)x+4 = 3x-n, Ç=R
A, B = katsayi_kosulu((m - 2)*x + 4, 3*x - n)
sol = solve([A, B], [m, n], dict=True)[0]
esit(sol[m], 5); esit(sol[n], -4); esit(sol[m] + sol[n], 1, 'S18')
# S19: (a+1)x-3 = 2x+b, Ç=∅ -> a=1, b != -3
A, B = katsayi_kosulu((a + 1)*x - 3, 2*x + b)
esit(solve(A, a)[0], 1)
esit(solve(B.subs(a, 1), b)[0], -3)   # B=0 olursa Ç=R olur; o yüzden b != -3
# S20: ax-4 = 2x+a, kök 3 -> a=5
esit(solve((a*x - 4 - 2*x - a).subs(x, 3), a)[0], 5)
kok(5*x - 4, 2*x + 5, 3)
# S21-S24 paydada bilinmeyen
kok(6/(x - 1), 3, 3)
kok((x + 3)/(x - 2), 2, 7)
kok((x + 1)/(x - 3), 4/(x - 3), S.EmptySet)
kok(2/x + 1/(2*x), R(5, 4), 2)
# Ders 2 sınıfta siz çözün
kok(x/3 + x/4, 7, 12)
kok((x + 2)/3 - (x - 1)/2, 1, 1)
kok(R(3, 10)*x - R(4, 10), R(1, 10)*x + R(6, 10), 5)
A, B = katsayi_kosulu((a - 3)*x + 2, 5*x + b)
s = solve([A, B], [a, b], dict=True)[0]
esit(s[a] + s[b], 10, 'D2-SSC4')
kok((2*x + 5)/(x + 1), 3, 2)

# ---- Ders 3 ----
kok(3*x + 5, 29, 8)                                         # S26
kok(3*(x + 4), 5*x - 2, 7)                                  # S27
kok(x/2 + x/3, 25, 30)                                      # S28
kok(x + x + x/2 + x/4 + 1, 100, 36)                         # S29 kaz
esit(36 + 36 + 18 + 9 + 1, 100)
# S30 ardışık üç tam sayı toplamı 96, en büyük 33 (brute force)
c = [i for i in range(-200, 200) if i + (i + 1) + (i + 2) == 96]
assert c == [31]; esit(c[0] + 2, 33)
# S31 ardışık üç çift: 3*en küçük = 2*en büyük + 14 ; toplam 72
c = [i for i in range(-200, 200, 2) if 3*i == 2*(i + 4) + 14]
assert c == [22]; esit(3*22 + 6, 72)
# S32 para: Ali=3*Ayşe, Ali Ayşe'ye 40 verince eşit
c = [y for y in range(0, 1000) if 3*y - 40 == y + 40]
assert c == [40]; sayac += 1
# S33 yaş: anne=4*kız, 6 yıl sonra anne=3*kız
c = [y for y in range(0, 100) if 4*y + 6 == 3*(y + 6)]
assert c == [12]; esit(4*12, 48)
# S34 yol: 60t+90t=450
kok(60*x + 90*x, 450, 3)
# S35 PIN: sol=2*sag+1, sol+sag=46 ; brute force dört basamaklı
c = [p for p in range(1000, 10000) if p // 100 == 2*(p % 100) + 1 and p // 100 + p % 100 == 46]
assert c == [3115]; esit(sum(map(int, str(c[0]))), 10)
# Ders 3 sınıfta siz çözün
kok(2*x - 7, 25, 16)
c = [i for i in range(-201, 201, 2) if 4*i + 12 == 64]
assert c == [13]; esit(13 + 6, 19)
kok((x + 3)/2, x - 3, 9)
kok(40 + x, 2*(12 + x), 16)
kok(x + x + 14, 50, 18)

# ================= DERS NOTU =================
kok(4*x + 3, x + 15, 4)                                     # N1 terazi
kok(7*x - 3, 4*x + 12, 5)                                   # N2
kok(4*(2*x - 3) - 3*(x + 1), 2*(x + 3), 7)                  # N3
kok(3 - (2*x - (x - 5)), 4 - 2*x, 6)                        # N4
kok(-6*x + 9, 0, R(3, 2))                                   # N5
kok((x + 1)/2 + (x - 2)/3, 4, 5)                            # N6
kok(x - (x - 1)/4, (x + 5)/2, 9)                            # N7
kok(R(25, 100)*x + R(5, 10), R(2, 10)*x + R(75, 100), 5)    # N8
kok(4*(x - 1) + 2, 2*(2*x - 1), RE)                         # N9a
kok(5*x - 3*(x + 2), 2*x + 1, S.EmptySet)                   # N9b
A, B = katsayi_kosulu((2*a - 1)*x + 3, 5*x + b - 1)         # N10
s = solve([A, B], [a, b], dict=True)[0]
esit(s[a], 3); esit(s[b], 4); esit(s[a]*s[b], 12, 'N10')
A, B = katsayi_kosulu((k + 2)*x - 5, 4*x + 1)               # N11
esit(solve(A, k)[0], 2); assert B != 0; sayac += 1
esit(solve((((k + 2)*x - 5) - (4*x + 1)).subs(x, 3), k)[0], 4)
kok(6*x - 5, 4*x + 1, 3)
esit(solve((((x + m)/3 - (x - m)/2) - 1).subs(x, 4), m)[0], 2)   # N12
kok((x + 2)/3 - (x - 2)/2, 1, 4)
kok((3*x - 1)/(x + 2), 2, 5)                                # N13
# N14: sympy solveset burada hatalı EmptySet döndürüyor; elle doğrula:
esit(simplify(3/(x - 2) + 1 - (x + 1)/(x - 2)), 0, 'N14 özdeşlik')   # x != 2 için her x sağlar
for v in [-7, -1, 0, 1, R(5, 2), 3, 10]:
    assert (3/(x - 2) + 1 - (x + 1)/(x - 2)).subs(x, v) == 0
assert (x - 2).subs(x, 2) == 0; sayac += 1                # x=2 tanımsız -> Ç = R - {2}
kok(5/x - 2/(3*x), R(13, 6), 2)                             # N15
kok(2*x + 3, 4*x - 9, 6)                                    # N16
c = [i for i in range(-300, 300) if sum(range(i, i + 5)) == 115]
assert c == [21]; sayac += 1                                # N17
c = [e for e in range(0, 41) if e + (e + 6) == 40]
assert c == [17]; esit(17 + 6, 23)                          # N18
c = [tt for tt in range(0, 11) if 38 - tt == 5*(10 - tt)]
assert c == [3]; esit(35, 5*7)                              # N19
kok(x/60 + x/90, 5, 180)                                    # N20
c = [o for o in range(0, 21) if 10*o + 5*(20 - o) == 145]
assert c == [9]; esit(20 - 9, 11)                           # N21

# Alıştırmalar
kok(6*x - 5, 2*x + 19, 6)                                   # 1
kok(3*(x - 4) + 2, 5 - (x - 1), 4)                          # 2
kok(2*(3 - (x - 1)), x + 2, 2)                              # 3
kok(x/4 - x/6, 2, 24)                                       # 4
kok((x + 2)/3 - (x - 2)/5, 2, 7)                            # 5
kok(R(4, 10)*x - R(12, 10), R(1, 10)*x + R(3, 10), 5)       # 6
kok(R(15, 100)*x + R(4, 10), R(5, 100)*x + R(14, 10), 10)   # 7
kok(3*(x + 2) - x, 2*(x + 3), RE)                           # 8a
kok(4*x - 2*(2*x - 1), 5, S.EmptySet)                       # 8b
A, B = katsayi_kosulu((2*m + 1)*x - 7, 5*x + n - 2)         # 9
s = solve([A, B], [m, n], dict=True)[0]
esit(s[m], 2); esit(s[n], -5); esit(s[m]*s[n], -10, 'A9')
A, B = katsayi_kosulu((a - 4)*x + 6, 2*x + 3)               # 10
esit(solve(A, a)[0], 6); assert B != 0; sayac += 1
esit(solve((3*x + 2*k - k*x - 11).subs(x, 3), k)[0], -2)    # 11
kok(3*x - 4, -2*x + 11, 3)
kok((x + 7)/(x - 1), 3, 5)                                  # 12
kok(2*x/(x - 4), 8/(x - 4), S.EmptySet)                     # 13
kok(4/x + R(1, 2), 7/(2*x), -1)                             # 14
c = [i for i in range(-301, 301, 2) if 3*i + 6 == 57]
assert c == [17]; esit(17 + 4, 21)                          # 15
kok(2*(x + 5), 3*x - 4, 14)                                 # 16
kok(45 + x, 2*(15 + x), 15)                                 # 17
kok(3*x + 3*(x + 10), 390, 60)                              # 18

# ================= SÜRÜM 2 EKLERİ =================
# ---- Sunum: yıldızlı Sınıfta Siz Çözün çözüm adımları ----
kok(7 - (x - 2), 3*x - 3, 3)                                # D1-3
esit(expand(7 - (x - 2)), 9 - x); kok(9 - x, 3*x - 3, 3); esit(7 - (3 - 2), 6); esit(3*3 - 3, 6)
kok(3*(2*x - 1) - 2*(x + 4), 5, 4)                          # D1-4
esit(expand(3*(2*x - 1) - 2*(x + 4)), 4*x - 11); esit(3*7 - 2*8, 5)
kok(5*x, -2*x, 0)                                           # D1-5
esit(expand(2*(x + 2) - 3*(x - 1)), -x + 7); esit(R(3, 3) - R(0, 2), 1)   # D2-2
A, B = katsayi_kosulu((a - 3)*x + 2, 5*x + b)               # D2-4
s2 = solve([A, B], [a, b], dict=True)[0]
esit(s2[a], 8); esit(s2[b], 2)
kok(2*x + 5, 3*(x + 1), 2); esit(R(2*2 + 5, 2 + 1), 3)      # D2-5
esit(13 + 15 + 17 + 19, 64)                                 # D3-2
esit(R(9 + 3, 2), 9 - 3)                                    # D3-3
esit(40 + 16, 2*(12 + 16)); esit(40 + 16, 56); esit(12 + 16, 28)   # D3-4

# ---- Ders notu: Çözümlü alıştırmalar (adımlar) ----
esit(expand(3 - (x - 1)), 4 - x); kok(8 - 2*x, x + 2, 2); esit(2*(3 - 1), 4)       # Ç1
esit(expand(5*(x + 2) - 3*(x - 2)), 2*x + 16); esit(R(9, 3) - R(5, 5), 2)          # Ç2
kok(15*x + 40, 5*x + 140, 10); esit(R(15, 100)*10 + R(4, 10), R(19, 10)); esit(R(5, 100)*10 + R(14, 10), R(19, 10))  # Ç3
esit(expand(((2*m + 1)*x - 7).subs(m, 2) - (5*x + n - 2).subs(n, -5)), 0)          # Ç4 özdeşlik
kok(2*x, 8, 4)                                              # Ç5: paylar eşitliği x=4 verir, koşul x!=4
kok(8 + x, 7, -1); esit(R(4, -1) + R(1, 2), R(-7, 2)); esit(R(7, -2), R(-7, 2))    # Ç6
esit(2*(14 + 5), 38); esit(3*14 - 4, 38)                    # Ç7
esit(3*60 + 3*70, 390)                                      # Ç8

# ---- Kendiniz çözün: yeni sorular ----
kok((x - 1)/2 + (x + 1)/3, x - 2, 11)                       # K11
esit(expand(3*(x - 1) + 2*(x + 1)), 5*x - 1); esit(R(10, 2) + R(12, 3), 11 - 2)
c = [t5 for t5 in range(1, 1000) if t5 % 5 == 0 and 3*t5//5 == 2*t5//5 + 4]        # K12 brute force
assert c == [20]; sayac += 1
kok(R(3, 5)*x, R(2, 5)*x + 4, 20)

print(f"Tüm doğrulamalar geçti: {sayac} assert.")
