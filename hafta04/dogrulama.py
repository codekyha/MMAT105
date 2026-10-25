#!/usr/bin/env python3
"""MMAT105 Hafta 4 -- sunum ve ders notundaki tüm sayısal cevapların doğrulaması."""
from fractions import Fraction as F
from decimal import Decimal as D
from math import gcd, prod

sayac = 0


def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1


def devirli(tam, devretmeyen, devreden):
    """Geometrik seri ile: tam, devretmeyen (virgülden sonra, str), devreden (str)."""
    m, k = len(devretmeyen), len(devreden)
    v = F(tam) + (F(int(devretmeyen), 10**m) if m else 0)
    v += F(int(devreden), 10**m * (10**k - 1))
    return v


def kural(tam, devretmeyen, devreden):
    """Derste verilen kural: (tüm sayı - devretmeyen kısım)/(9..90..0)."""
    tum = int(str(tam) + devretmeyen + devreden)
    dk = int(str(tam) + devretmeyen)
    payda = int("9" * len(devreden) + "0" * len(devretmeyen))
    return F(tum - dk, payda)


def dv(tam, a, b):
    x, y = devirli(tam, a, b), kural(tam, a, b)
    ok(x == y, f"devirli kural {tam},{a},({b})")
    # sayısal yaklaşık kontrol
    s = float(f"{tam}." + a + b * 12)
    ok(abs(float(x) - s) < 1e-9, f"devirli yaklaşık {tam},{a},({b})")
    return x


def sirali(lst):
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))


def sade(f):
    return (f.numerator, f.denominator)


# ===================== SUNUM =====================
# Geçen hafta hatırlatma
a_list = [a for a in range(10) if int(f"37{a}") % 3 == 0 and int(f"37{a}") % 4 == 0]
ok(a_list == [2], "H1")
ok([a for a in range(10) if int(f"7{a}") % 4 == 0] == [2, 6], "H1 4 kuralı")
ok([a for a in range(10) if (3 + 7 + a) % 3 == 0] == [2, 5, 8], "H1 3 kuralı")
ok(gcd(24, 36) == 12 and 24 * 36 // gcd(24, 36) == 72, "H2")
ok([n for n in range(0, 100) if n % 12 == 5 and n % 18 == 5] == [5, 41, 77], "H3 liste")
ok(next(n for n in range(10, 100) if n % 12 == 5 and n % 18 == 5) == 41, "H3")

# Örnek 1
ok(F(0, 7) == 0 and F(5, 1) == 5 and F(D("2.5")) == F(5, 2) and F(12, -4) == -3, "Ö1")
# Örnek 2
basit = [f for f in [(3, 7), (9, 4), (6, 6), (11, 12), (13, 5)] if f[0] < f[1]]
ok(basit == [(3, 7), (11, 12)], "Ö2")
# Örnek 3
ok(3 + F(2, 5) == F(17, 5), "Ö3a")
ok(divmod(23, 4) == (5, 3) and 5 + F(3, 4) == F(23, 4), "Ö3b")
# Örnek 4
ok(gcd(84, 126) == 42 and F(84, 126) == F(2, 3), "Ö4a")
ok(F(3 * 7, 8 * 7) == F(3, 8) and 8 * 7 == 56, "Ö4b")
# Örnek 5
ok(-3 < F(-7, 3) < -2 and 2 < F(11, 4) < 3 and abs(F(-7, 3)) < abs(F(11, 4)), "Ö5")
ok(F(7, 3) == F(28, 12) and F(11, 4) == F(33, 12), "Ö5 payda")
# Örnek 6-8
ok(F(2, 3) + F(3, 4) - F(5, 6) == F(7, 12), "Ö6")
ok(F(5, 12) + F(7, 18) == F(29, 36) and 12 * 18 // gcd(12, 18) == 36, "Ö7")
ok(F(13, 4) - F(5, 3) == F(19, 12) and 1 + F(7, 12) == F(19, 12), "Ö8")
# Hata kutuları
ok(F(1, 2) + F(1, 3) == F(5, 6) and F(2 + 3, 2 + 5) != F(3, 5), "hata kutusu 1")
ok(3 / F(4, 5) == F(15, 4) and F(3, 4) / 5 == F(3, 20), "ana kesir çizgisi")
# Örnek 9-12
ok(F(14, 15) * F(25, 21) == F(10, 9), "Ö9")
ok(F(4, 9) / F(8, 15) == F(5, 6) and F(-3, 5) / 6 == F(-1, 10), "Ö10")
ok((F(2, 3) - F(1, 2)) / (F(1, 4) + F(1, 6)) == F(2, 5), "Ö11")
ok(2 - 1 / (2 - 1 / (2 - F(1, 2))) == F(5, 4), "Ö12")
# Ders 1 siz çözün
ok(4 + F(2, 7) == F(30, 7), "D1-1")
ok(F(90, 150) == F(3, 5), "D1-2")
ok(F(5, 6) - F(3, 8) == F(11, 24), "D1-3")
ok(F(9, 10) / F(3, 5) == F(3, 2), "D1-4")
ok(1 - 1 / (1 - F(1, 3)) == F(-1, 2), "D1-5")

# Ders 2 kural örnekleri
ok(F(D("0.25")) == F(1, 4) and F(D("4.375")) == F(35, 8) and F(3, 4) == F(D("0.75")), "ondalık kural")
ok(F(3, 40) == F(D("0.075")), "3/40")
# Sonlu ondalık kuralı: 1..200 paydalı kesirler için brute force


def sonlu_mu(fr):
    q = fr.denominator
    for p in (2, 5):
        while q % p == 0:
            q //= p
    return q == 1


def sonlu_gercek(fr):
    # 10^k * fr tam sayı olacak bir k (k<=20) var mı?
    return any((fr * 10**k).denominator == 1 for k in range(21))


ok(all(sonlu_mu(F(a, b)) == sonlu_gercek(F(a, b)) for b in range(1, 201) for a in range(1, 50)), "sonlu ondalık kuralı")
ok(not sonlu_mu(F(1, 3)) and not sonlu_mu(F(5, 12)), "1/3, 5/12 devirli")
# Örnek 13-14
ok(F(D("0.25")) == F(1, 4) and F(D("1.6")) == F(8, 5) and F(D("0.045")) == F(9, 200), "Ö13")
ok(D(7) / D(8) == D("0.875") and D(3) / D(20) == D("0.15"), "Ö14")
# Örnek 15-17
ok(D("3.75") + D("12.4") - D("0.08") == D("16.07"), "Ö15")
ok(D("2.4") * D("0.35") == D("0.84") and D("0.06") * D("0.5") == D("0.03"), "Ö16a")
ok(D("3.47") * 100 == D("347") and D("52.1") / 1000 == D("0.0521"), "Ö16b")
ok(24 * 35 == 840 and 6 * 5 == 30, "Ö16 ara")
ok(D("0.36") / D("0.012") == 30 and D("0.24") / D("0.6") + D("1.5") / D("0.05") == D("30.4"), "Ö17")
ok(D("0.3") * D("0.2") == D("0.06") and D("0.2") ** 2 == D("0.04"), "ondalık hata kutusu")
# Devirli (Örnek 18-22)
ok(dv(0, "", "3") == F(1, 3), "0,(3)")
ok(dv(1, "2", "3") == F(37, 30) and F(111, 90) == F(37, 30), "1,2(3)")
ok(dv(0, "", "9") == 1, "0,(9)=1")
ok(dv(0, "", "27") == F(3, 11), "Ö18")
ok(dv(0, "1", "6") == F(1, 6) and dv(2, "", "45") == F(27, 11), "Ö20")
ok(dv(2, "4", "9") == F(5, 2), "Ö21")
ok(dv(0, "", "8") / dv(0, "", "4") + dv(0, "", "6") * F(3, 2) == 3, "Ö22")
# Bilimsel gösterim
ok(D("3.4") * 10**6 == 3400000 and D("5.2") * D("1e-4") == D("0.00052"), "Ö23")
ok(D(34) * 10**5 == D("3.4") * 10**6, "34·10^5")
# Ders 2 siz çözün
ok(F(D("0.125")) == F(1, 8), "D2-1")
ok(D("4.2") * D("0.05") == D("0.21"), "D2-2")
ok(D("0.72") / D("0.018") == 40, "D2-3")
ok(dv(0, "2", "7") == F(5, 18), "D2-4")
ok(D("0.0045") * 10**5 == 450 and D("4.5") * 10**2 == 450, "D2-5")

# Ders 3
ok(sirali([F(5, 12), F(5, 9), F(5, 7)]), "Ö24 c<a<b")
ok(sirali([F(5, 8), F(2, 3), F(3, 4)]) and (F(2, 3) * 24, F(3, 4) * 24, F(5, 8) * 24) == (16, 18, 15), "Ö25")
ok(sirali([F(65, 100), dv(0, "6", "5"), F(2, 3)]), "Ö26 a<c<b")
ok(sirali([F(13, 14), F(15, 16), F(17, 18)]), "Ö27")
ok(17 * 18 == 306 and 13 * 23 == 299 and F(17, 23) > F(13, 18), "Ö28")
ok(sirali([F(-3, 4), F(-2, 3), F(-5, 8)]), "Ö29")
ok((F(1, 3) + F(1, 2)) / 2 == F(5, 12) and F(1, 3) < F(5, 12) < F(1, 2), "Ö30a")
ok([k for k in range(-100, 100) if F(3, 7) < F(k, 14) < F(4, 7)] == [7], "Ö30b")
ok(prod(1 - F(1, n) for n in range(2, 11)) == F(1, 10), "Ö31")
ok(360 * F(2, 3) == 240 and 360 * F(5, 8) == 225 and 360 * (F(2, 3) - F(5, 8)) == 15, "Ö32")
ok(F(3, 4) - F(1, 3) == F(5, 12) and F(3, 4) * (1 - F(1, 3)) == F(1, 2), "Ö33")
g1 = 120 * F(1, 4); k1 = 120 - g1; g2 = k1 * F(2, 5)
ok(g1 == 30 and k1 == 90 and g2 == 36 and k1 - g2 == 54 and 120 * F(3, 4) * F(3, 5) == 54, "Ö34")
ok(60 * F(3, 4) == 45, "kural 60'ın 3/4'ü")
# Ders 3 siz çözün
ok(sirali([F(4, 5), F(5, 6), F(6, 7)]), "D3-1")
ok(sirali([F(-1, 2), F(-3, 7), F(-2, 5)]), "D3-2")
ok((F(2, 9) + F(1, 3)) / 2 == F(5, 18), "D3-3")
ok(240 - 240 * F(3, 8) == 150, "D3-4")
ok(prod(1 + F(1, n) for n in range(2, 10)) == 5, "D3-5")

# ===================== DERS NOTU =====================
ok(F(36, 48) == F(3, 4) and F(-15, 25) == F(-3, 5) and 5 + F(3, 8) == F(43, 8), "N1")
denk = [(3 * k, 4 * k) for k in range(1, 100) if 30 < 4 * k < 50]
ok(len(denk) == 5 and denk == [(24, 32), (27, 36), (30, 40), (33, 44), (36, 48)], "N2")
# N2 brute force: paydası 31..49 olan tüm kesirler arasında 3/4'e eşit olanlar
ok(sum(1 for q in range(31, 50) for p in range(0, q + 1) if F(p, q) == F(3, 4)) == 5, "N2 brute")
ok(F(7, 10) - F(4, 15) + F(1, 6) == F(3, 5), "N3")
ok(F(9, 4) - F(5, 6) == F(17, 12) and (F(9, 4) - F(5, 6)) * F(6, 17) == F(1, 2), "N4")
ok(F(3, 4) / F(9, 8) * F(3, 2) == 1 and F(3, 4) / (F(9, 8) * F(3, 2)) == F(4, 9), "N5")
ok(1 / (1 + 1 / (1 + F(1, 3))) == F(4, 7), "N6")
ok((F(1, 2) + F(1, 3)) / (F(1, 2) - F(1, 3)) == 5, "N7")
ok(F(D("0.0375")) == F(3, 80) and gcd(375, 10000) == 125, "N8")
ok(D("1.2") * D("0.15") / D("0.009") == 20, "N9")
ok(D("0.3") / D("0.03") + D("0.03") / D("0.3") - D(3) / D("0.3") == D("0.1"), "N10")
ok(dv(0, "", "12") == F(4, 33) and dv(3, "1", "6") == F(19, 6), "N11")
ok(dv(0, "", "3") + dv(0, "", "6") == 1 and dv(0, "1", "9") == F(1, 5), "N12")
ok(3 * 10**5 == 300000 and 2 * D("1e-6") == D("0.000002"), "N13a")
ok(D("4.07") * 10**3 == 4070 and D("6.1") * D("1e-2") == D("0.061"), "N13b")
ok(sirali([F(19, 18), F(17, 16), F(15, 14)]), "N14")
ok(sirali([F(28, 100), dv(0, "", "28"), F(2, 7)]), "N15 c<b<a")
ok(101 * 104 == 10504 and 102 * 103 == 10506 and F(101, 103) < F(102, 104), "N16")
ok([k for k in range(-100, 100) if F(2, 5) < F(k, 20) < F(3, 5)] == [9, 10, 11], "N17")
ok((F(1, 2) - F(1, 3)) / F(1, 6) + F(D("0.5")) * F(4, 5) == F(7, 5) and F(7, 5) == F(D("1.4")), "N18")
ok(sum(F(1, n * (n + 1)) for n in range(1, 10)) == F(9, 10), "N19")
y = 600 * F(1, 3); kal = 600 - y; kit = kal * F(1, 4)
ok(y == 200 and kal == 400 and kit == 100 and kal - kit == 300 and F(y + kit, 600) == F(1, 2), "N20")
ok(all(F(1, n * (n + 1)) == F(1, n) - F(1, n + 1) for n in range(1, 200)), "teleskopik özdeşlik")

# Alıştırmalar
ok(6 + F(2, 3) == F(20, 3) and divmod(47, 6) == (7, 5), "A1")
ok(F(126, 168) == F(3, 4) and gcd(126, 168) == 42, "A2")
ok(F(3, 8) + F(5, 12) - F(1, 6) == F(5, 8), "A3")
ok((F(3, 2) + F(3, 4)) / (1 + F(1, 8)) == 2, "A4")
ok(F(2, 3) * F(9, 10) / F(3, 5) == 1, "A5")
ok(3 - 2 / (1 + F(1, 2)) == F(5, 3), "A6")
ok(F(D("0.64")) == F(16, 25) and F(D("2.05")) == F(41, 20), "A7")
ok(D("1.25") * D("0.08") + D("0.9") / D("0.03") == D("30.1"), "A8")
ok(D("0.056") / D("0.0014") == 40, "A9")
ok(dv(0, "", "36") == F(4, 11) and dv(0, "4", "5") == F(41, 90), "A10")
ok(dv(1, "", "6") + dv(0, "8", "3") == F(5, 2) and dv(1, "", "6") == F(5, 3) and dv(0, "8", "3") == F(5, 6), "A11")
ok(D("7.2") * D("1e-4") == D("0.00072") and D("5.8") * 10**7 == 58000000, "A12")
ok(sirali([F(5, 7), F(7, 9), F(9, 11)]), "A13 c<a<b")
ok(sirali([-dv(0, "", "6"), F(-3, 5), F(-7, 12)]), "A14 b<a<c")
ok(-F(7, 12) == -dv(0, "58", "3"), "A14 -0,58(3)")
ok([k for k in range(-100, 100) if F(3, 8) < F(k, 24) < F(1, 2)] == [10, 11], "A15")
ok((F(5, 6) + F(7, 8)) / 2 == F(41, 48), "A16")
h = 720 * F(5, 12); k = 720 - h; b = k * F(3, 7)
ok(h == 300 and k == 420 and b == 180 and k - b == 240, "A17")
ok(sum(F(1, n * (n + 1)) for n in range(2, 12)) == F(5, 12), "A18")

# ===================== SÜRÜM 2 EKLERİ =====================
# ---- Sunum: yıldızlı Sınıfta Siz Çözün çözüm adımları ----
ok(90 == 2 * 3**2 * 5 and 150 == 2 * 3 * 5**2 and gcd(90, 150) == 30 and (90 // 30, 150 // 30) == (3, 5), "D1-2 adim")
ok(6 * 8 // gcd(6, 8) == 24 and F(5, 6) == F(20, 24) and F(3, 8) == F(9, 24) and gcd(11, 24) == 1, "D1-3 adim")
ok(1 - F(1, 3) == F(2, 3) and 1 / F(2, 3) == F(3, 2) and 1 - F(3, 2) == F(-1, 2), "D1-5 adim")
ok(D("0.72") * 1000 == 720 and D("0.018") * 1000 == 18 and F(720, 18) == 40 and D("0.018") * 40 == D("0.72"), "D2-3 adim")
ok(F(27 - 2, 90) == F(25, 90) == F(5, 18), "D2-4 adim")
ok(D("0.0045") * 10**5 == 450 and D("4.5") * 10**2 == 450, "D2-5 adim")
ok(F(1, 2) == F(35, 70) and F(2, 5) == F(28, 70) and F(3, 7) == F(30, 70) and sirali([F(2, 5), F(3, 7), F(1, 2)]), "D3-2 adim")
ok(F(2, 9) + F(3, 9) == F(5, 9) and F(5, 9) * F(1, 2) == F(5, 18) and F(4, 18) < F(5, 18) < F(6, 18), "D3-3 adim")
ok(prod(F(n + 1, n) for n in range(2, 10)) == F(10, 2) == 5, "D3-5 adim")

# ---- Ders notu: Çözümlü alıştırmalar (adımlar) ----
ok(F(3, 2) + F(3, 4) == F(9, 4) and F(9, 4) / F(9, 8) == 2 and 1 + F(1, 8) == F(9, 8), "C1")
ok(1 + F(1, 2) == F(3, 2) and 2 / F(3, 2) == F(4, 3) and 3 - F(4, 3) == F(5, 3), "C2")
ok(D("1.25") * D("0.08") == D("0.1") and 125 * 8 == 1000 and D("0.9") / D("0.03") == 30 and D("0.1") + 30 == D("30.1"), "C3")
ok(F(16 - 1, 9) == F(5, 3) and F(83 - 8, 90) == F(5, 6) and F(5, 3) + F(5, 6) == F(5, 2) == F(D("2.5")), "C4")
ok(dv(0, "", "6") == F(2, 3) and F(3, 5) == F(36, 60) and F(2, 3) == F(40, 60) and F(7, 12) == F(35, 60), "C5")
ok(sirali([F(-2, 3), F(-3, 5), F(-7, 12)]), "C5 sira")
ok(F(3, 8) == F(9, 24) and F(1, 2) == F(12, 24) and F(10, 24) == F(5, 12), "C6")
ok(720 * F(7, 12) * F(4, 7) == 240, "C7 kisa yol")
ok(F(1, 2) - F(1, 12) == F(5, 12), "C8")

# ---- Kendiniz çözün: yeni sorular ----
ok(dv(0, "", "3") + dv(0, "", "6") * F(D("0.75")) == F(5, 6), "K9 yeni")
ok(dv(0, "", "6") * F(3, 4) == F(1, 2), "K9 ara")
dolu = 840 * F(3, 7); ekle = 840 * F(1, 4); kalan = (dolu + ekle) * (1 - F(1, 3))
ok(dolu == 360 and ekle == 210 and dolu + ekle == 570 and kalan == 380 and F(kalan, 840) == F(19, 42), "K12 yeni")
ok(dolu + ekle <= 840, "K12 depo taşmaz")
ok(F(5, 6) == F(20, 24) and F(7, 8) == F(21, 24), "K11 ara")
ok(1 - F(7, 9) == F(2, 9) and 1 - F(9, 11) == F(2, 11) and 1 - F(5, 7) == F(2, 7), "K10 ara")

print(f"Tüm kontroller geçti: {sayac} assert.")
