# MMAT105 Hafta 11 -- sunum, ders notu ve alıştırmalardaki tüm cevapların doğrulanması
# Çarpanlara ayırma / açılım: sympy expand + factor eşdeğerliği
# Değer soruları: koşullar sympy ile çözülür, ifade bütün çözümlerde hesaplanır
# Rasyonel ifadeler: cancel eşdeğerliği + tanım koşulu kümesi (paydaların sıfır yerleri)
from sympy import (symbols, expand, factor, cancel, sqrt, Rational, solve, simplify,
                   Eq, Mul)

x, y, a, b, c, d, k, m = symbols('x y a b c d k m')

sayac = 0
def ok(kosul, ad):
    global sayac
    assert kosul, ad
    sayac += 1

def ayni(e1, e2):
    """İki ifade özdeş mi (açılım eşitliği)?"""
    return expand(e1 - e2) == 0

def carpan(ifade, iddia):
    """İddia edilen çarpanlara ayırma doğru mu? Hem açılım eşit hem de sympy'nin
    tam çarpanlara ayırması ile aynı (eksik ayrılmış olmasın)."""
    return ayni(ifade, iddia) and n_carpan(iddia) == n_carpan(factor(ifade))

def n_carpan(e):
    """Yazıldığı haliyle sabit olmayan çarpan sayısı (kuvvetler üs kadar sayılır)."""
    n = 0
    for t in Mul.make_args(e):
        if t.is_number:
            continue
        n += int(t.exp) if t.is_Pow and t.exp.is_Integer and t.exp > 0 else 1
    return n

def tam_ayrilmis(iddia_carpanlari, ifade):
    """Çarpan listesi verilir: çarpımı ifadeye eşit mi ve her çarpan sympy'ye göre
    daha fazla ayrılamaz mı (rasyonel katsayılarla)?"""
    carpim = 1
    for f in iddia_carpanlari:
        carpim *= f
    if not ayni(carpim, ifade):
        return False
    for f in iddia_carpanlari:
        if f.is_number:
            continue
        fl = factor(f)
        # sabit dışında tek çarpan ve kuvvet değil
        if fl.is_Mul and len([t for t in fl.args if not t.is_number]) > 1:
            return False
        if fl.is_Pow:
            return False
    return True

def deger(kosullar, ifade, beklenen, degiskenler):
    """Koşulları sağlayan TÜM (karmaşık dahil) çözümlerde ifade aynı değeri alıyor mu?"""
    cozumler = solve(kosullar, degiskenler, dict=True)
    assert cozumler, 'çözüm yok'
    return all(simplify(ifade.subs(s) - beklenen) == 0 for s in cozumler)

def payda_sifirlari(*paydalar):
    kume = set()
    for p in paydalar:
        kume |= set(solve(Eq(p, 0), x))
    return kume

def sadelestir(ifade, iddia, kosul_kumesi, *paydalar):
    return simplify(cancel(ifade) - iddia) == 0 and payda_sifirlari(*paydalar) == set(kosul_kumesi)

def cozum_kumesi(ifade, iddia):
    return set(solve(Eq(ifade, 0), x)) == set(iddia)

# =====================================================================
# HATIRLATMA (Hafta 10, köklü sayılar)
# =====================================================================
ok(sqrt(50) + sqrt(18) == 8*sqrt(2), 'H1')
ok(sqrt(12)*sqrt(3) == 6, 'H2')
ok(simplify(6/sqrt(3) - 2*sqrt(3)) == 0, 'H3')

# =====================================================================
# SUNUM -- DERS 1
# =====================================================================
ok(carpan(3*x**2 - 6*x, 3*x*(x - 2)), 'Ö1a')
ok(carpan(4*a**2*b - 6*a*b**2, 2*a*b*(2*a - 3*b)), 'Ö1b')
ok(ayni(a*b + a*c - a*d, a*(b + c - d)), 'Ö2a')
ok(carpan(x*(a - b) - y*(b - a), (a - b)*(x + y)), 'Ö2b')
ok(carpan(a*x + a*y + b*x + b*y, (x + y)*(a + b)), 'Ö3a')
# a+b=5, x+y=4 -> 20 (ifade (x+y)(a+b) olduğundan değer yalnız bu toplamlara bağlı)
ok(ayni(a*x + a*y + b*x + b*y, (a + b)*(x + y)) and 5*4 == 20, 'Ö3b')
ok(carpan(x*y - 2*x + 3*y - 6, (y - 2)*(x + 3)), 'Ö4')
ok(carpan(x**3 + 2*x**2 - 3*x - 6, (x + 2)*(x**2 - 3)), 'Ö5')
ok(carpan(x**2 - 49, (x - 7)*(x + 7)), 'Ö6a')
ok(carpan(9*a**2 - 4*b**2, (3*a - 2*b)*(3*a + 2*b)), 'Ö6b')
ok(ayni(25 - x**2, (5 - x)*(5 + x)), 'Ö6c')
ok(carpan(2*x**3 - 18*x, 2*x*(x - 3)*(x + 3)), 'Ö7')
ok(ayni(x**4 - 16, (x**2 - 4)*(x**2 + 4)) and not carpan(x**4 - 16, (x**2 - 4)*(x**2 + 4)), 'Ö8a')
ok(carpan(x**4 - 16, (x - 2)*(x + 2)*(x**2 + 4)), 'Ö8b')
ok(101**2 - 99**2 == 400 and 2*200 == 400, 'Ö9a')
ok(49*51 == 2499 and 50**2 - 1 == 2499, 'Ö9b')
ok(2025**2 - 2024**2 == 4049, 'Ö10a')
ok(expand((sqrt(7) - sqrt(3))*(sqrt(7) + sqrt(3))) == 4, 'Ö10b')
ok(solve([a - b - 3, a**2 - b**2 - 27], [a, b], dict=True) == [{a: 6, b: 3}], 'Ö11')
# Ders 1 sınıfta siz çözün
ok(carpan(5*x**2*y - 10*x*y, 5*x*y*(x - 2)), 'S1-1')
ok(carpan(x**2 - 3*x + x*y - 3*y, (x - 3)*(x + y)), 'S1-2')
ok(ayni(81 - a**4, (3 - a)*(3 + a)*(9 + a**2)) and
   tam_ayrilmis([3 - a, 3 + a, 9 + a**2], 81 - a**4), 'S1-3')
ok(102*98 == 9996 and 100**2 - 2**2 == 9996, 'S1-4')
ok(deger([a + b - 8, a - b - 2], a**2 - b**2, 16, [a, b]), 'S1-5')

# =====================================================================
# SUNUM -- DERS 2
# =====================================================================
ok(ayni((x + 5)**2, x**2 + 10*x + 25), 'Ö12a')
ok(ayni((2*a - 3*b)**2, 4*a**2 - 12*a*b + 9*b**2), 'Ö12b')
ok(103**2 == 10609 and 99**2 == 9801, 'Ö13')
ok(deger([a + b - 7, a*b - 10], a**2 + b**2, 29, [a, b]), 'Ö14')
ok(deger([a - b - 3, a*b - 4], a**2 + b**2, 17, [a, b]), 'Ö15')
ok(ayni((x + y)**2 - (x - y)**2, 4*x*y) and Rational(49 - 9, 4) == 10, 'Ö16')
ok(deger([x + 1/x - 4], x**2 + 1/x**2, 14, [x]), 'Ö17')
# Ö18: x^2+6x+m tam kare <=> m=9 ; 4x^2-kx+25 tam kare ve k>0 <=> k=20
ok(solve(Eq(6**2 - 4*1*m, 0), m) == [9] and ayni(x**2 + 6*x + 9, (x + 3)**2), 'Ö18a')
ok([s for s in solve(Eq(k**2 - 4*4*25, 0), k) if s > 0] == [20] and
   ayni(4*x**2 - 20*x + 25, (2*x - 5)**2), 'Ö18b')
ok(carpan(x**2 + 7*x + 12, (x + 3)*(x + 4)), 'Ö19a')
ok(carpan(x**2 - 2*x - 15, (x - 5)*(x + 3)), 'Ö19b')
ok(carpan(x**2 - x*y - 6*y**2, (x - 3*y)*(x + 2*y)), 'Ö20')
ok(carpan(2*x**2 + 7*x + 3, (2*x + 1)*(x + 3)), 'Ö21')
ok(carpan(6*x**2 - x - 2, (2*x + 1)*(3*x - 2)), 'Ö22')
ok(cozum_kumesi(x**2 - 5*x + 6, [2, 3]) and cozum_kumesi(x**2 - 4*x, [0, 4]), 'Ö23')
ok(carpan(2*x**2 - x - 3, (2*x - 3)*(x + 1)) and cozum_kumesi(2*x**2 - x - 3, [-1, Rational(3, 2)]), 'Ö24')
# Ders 2 sınıfta siz çözün
ok(ayni((3*x - 2)**2, 9*x**2 - 12*x + 4), 'S2-1')
ok(deger([a + b - 6, a*b - 7], a**2 + b**2, 22, [a, b]), 'S2-2')
ok(deger([x + 1/x - 5], x**2 + 1/x**2, 23, [x]), 'S2-3')
ok(carpan(x**2 - x - 12, (x - 4)*(x + 3)), 'S2-4')
ok(carpan(x**2 + 3*x - 10, (x + 5)*(x - 2)) and cozum_kumesi(x**2 + 3*x - 10, [-5, 2]), 'S2-5')

# =====================================================================
# SUNUM -- DERS 3
# =====================================================================
ok(ayni((x + 2)**3, x**3 + 6*x**2 + 12*x + 8), 'Ö25a')
ok(ayni((a - 1)**3, a**3 - 3*a**2 + 3*a - 1), 'Ö25b')
ok(carpan(x**3 - 8, (x - 2)*(x**2 + 2*x + 4)), 'Ö26a')
ok(carpan(27*a**3 + 1, (3*a + 1)*(9*a**2 - 3*a + 1)), 'Ö26b')
ok(deger([a + b - 5, a*b - 3], a**3 + b**3, 80, [a, b]) and
   deger([a + b - 5, a*b - 3], a**2 + b**2, 19, [a, b]), 'Ö27')
ok(deger([a - b - 2, a*b - 15], a**3 - b**3, 98, [a, b]) and 5**3 - 3**3 == 98, 'Ö28')
ok(deger([x + 1/x - 3], x**3 + 1/x**3, 18, [x]), 'Ö29')
ok(Rational(13**3 - 7**3, 6) == 309 and 169 + 91 + 49 == 309, 'Ö30')
ok(sadelestir((x**2 - 9)/(x**2 + x - 6), (x - 3)/(x - 2), {-3, 2}, x**2 + x - 6), 'Ö31')
ok(sadelestir((x**2 - 4*x + 4)/(x**2 - 4), (x - 2)/(x + 2), {2, -2}, x**2 - 4), 'Ö32')
ok(sadelestir((x**3 - 1)/(x**2 - 1), (x**2 + x + 1)/(x + 1), {1, -1}, x**2 - 1), 'Ö33')
# Ö34: bölme -> paydalar x^2-2x, x^2+x ve bölen kesrin payı x^2+2x+1 sıfır olmamalı
ok(sadelestir(((x**2 - 4)/(x**2 - 2*x)) / ((x**2 + 2*x + 1)/(x**2 + x)), (x + 2)/(x + 1),
              {0, 2, -1}, x**2 - 2*x, x**2 + x, x**2 + 2*x + 1), 'Ö34')
# Bilgisayar köşesi çıktıları
ok(expand((x + 2)**3) == x**3 + 6*x**2 + 12*x + 8, 'Py1')
ok(factor(x**4 - 16) == (x - 2)*(x + 2)*(x**2 + 4), 'Py2')
ok(factor(6*x**2 - x - 2) == (2*x + 1)*(3*x - 2), 'Py3')
ok(cancel((x**2 - 9)/(x**2 + x - 6)) == (x - 3)/(x - 2), 'Py4')
# Ders 3 sınıfta siz çözün
ok(ayni((x - 3)**3, x**3 - 9*x**2 + 27*x - 27), 'S3-1')
ok(deger([a + b - 4, a*b - 2], a**3 + b**3, 40, [a, b]), 'S3-2')
ok(carpan(x**3 + 64, (x + 4)*(x**2 - 4*x + 16)), 'S3-3')
ok(sadelestir((x**2 - 16)/(x**2 - x - 12), (x + 4)/(x + 3), {4, -3}, x**2 - x - 12), 'S3-4')
ok(deger([x - 1/x - 2], x**3 - 1/x**3, 14, [x]), 'S3-5')

# =====================================================================
# DERS NOTU -- örnekler
# =====================================================================
ok(carpan(6*x**3*y - 9*x**2*y**2 + 3*x*y, 3*x*y*(2*x**2 - 3*x*y + 1)), 'N1')
ok(carpan(x**3 - 2*x**2 + 5*x - 10, (x - 2)*(x**2 + 5)), 'N2')
ok(deger([x + y - 5, x**2*y + x*y**2 - 30], x*y, 6, [x, y]), 'N3')
ok(carpan((2*x + 1)**2 - (x - 2)**2, (x + 3)*(3*x - 1)), 'N4')
ok(carpan(x**8 - 1, (x - 1)*(x + 1)*(x**2 + 1)*(x**4 + 1)), 'N5')
ok(37*43 == 1591 and 2026*2024 - 2025**2 == -1, 'N6')
ok(simplify(6/(sqrt(5) - sqrt(2)) - (2*sqrt(5) + 2*sqrt(2))) == 0, 'N7')
ok(solve([x**2 - y**2 - 40, x + y - 10], [x, y], dict=True) == [{x: 7, y: 3}], 'N8')
ok(998**2 == 996004, 'N9')
ok(deger([a + b - 5, a**2 + b**2 - 13], a*b, 6, [a, b]), 'N10')
# N11: x>0 ve x^2+1/x^2=7 -> x+1/x=3
coz = [s for s in solve(Eq(x**2 + 1/x**2, 7), x) if s.is_real and s > 0]
ok(len(coz) > 0 and all(simplify(s + 1/s - 3) == 0 for s in coz), 'N11')
ok([s for s in solve(Eq(k**2 - 4*9*16, 0), k) if s < 0] == [-24] and
   ayni(9*x**2 - 24*x + 16, (3*x - 4)**2), 'N12')
ok(solve([x**2 + y**2 - 4*x + 6*y + 13], [x, y], dict=True) != [] and
   ayni(x**2 + y**2 - 4*x + 6*y + 13, (x - 2)**2 + (y + 3)**2) and 2 + (-3) == -1, 'N13')
ok(carpan(x**2 - 11*x + 28, (x - 4)*(x - 7)) and carpan(x**2 + x - 30, (x + 6)*(x - 5)), 'N14')
ok(carpan(3*x**2 - 10*x + 8, (3*x - 4)*(x - 2)), 'N15')
ok(carpan(x**4 - 5*x**2 + 4, (x - 1)*(x + 1)*(x - 2)*(x + 2)), 'N16')
ok(cozum_kumesi(x**3 - 9*x, [-3, 0, 3]) and carpan(3*x**2 + x - 2, (3*x - 2)*(x + 1))
   and cozum_kumesi(3*x**2 + x - 2, [-1, Rational(2, 3)]), 'N17')
ok(ayni((2*x - 1)**3, 8*x**3 - 12*x**2 + 6*x - 1), 'N18')
ok(carpan(8*x**3 - 27*y**3, (2*x - 3*y)*(4*x**2 + 6*x*y + 9*y**2)), 'N19')
ok(deger([a + b - 3, a**3 + b**3 - 9], a*b, 2, [a, b]), 'N20')
ok(deger([x - 1/x - 3], x**3 - 1/x**3, 36, [x]), 'N21')
ok(Rational(47**3 + 53**3, 100) == 2527 and 2209 - 2491 + 2809 == 2527, 'N22')
ok(sadelestir((x**2 + 5*x + 6)/(x**2 - 9) * (x - 3)/(x + 2), 1, {3, -3, -2}, x**2 - 9, x + 2), 'N23')
ok(sadelestir((2*x**2 - 8)/(x**2 + 4*x + 4), (2*x - 4)/(x + 2), {-2}, x**2 + 4*x + 4), 'N24')
A, B = 2027, 2026
ok(Rational(A**3 - B**3, A**2 + A*B + B**2) + Rational(A**2 - B**2, A - B) == 4054 and 2*A == 4054, 'N25')

# =====================================================================
# ÇÖZÜMLÜ ALIŞTIRMALAR
# =====================================================================
ok(carpan(12*a**2*b - 18*a*b**2, 6*a*b*(2*a - 3*b)), 'Ç1')
ok(carpan(x**2 - y**2 + 3*x - 3*y, (x - y)*(x + y + 3)), 'Ç2')
ok(carpan((x + 1)**2 - 25, (x - 4)*(x + 6)), 'Ç3')
ok(deger([a - b - 5, a**2 + b**2 - 37], a*b, 6, [a, b]), 'Ç4')
ok([s for s in solve(Eq(k**2 - 4*49, 0), k) if s < 0] == [-14] and
   ayni(x**2 - 14*x + 49, (x - 7)**2), 'Ç5')
ok(carpan(4*x**2 - 4*x - 3, (2*x - 3)*(2*x + 1)), 'Ç6')
ok(deger([a + b - 6, a*b - 5], a**3 + b**3, 126, [a, b]) and
   deger([a + b - 6, a*b - 5], a**2 + b**2, 26, [a, b]), 'Ç7')
ok(sadelestir((x**3 + 8)/(x**2 - 4), (x**2 - 2*x + 4)/(x - 2), {2, -2}, x**2 - 4), 'Ç8')

# =====================================================================
# KENDİNİZ ÇÖZÜN
# =====================================================================
ok(carpan(7*x**2 - 14*x, 7*x*(x - 2)), 'K1')
ok(carpan(x*y + 2*x + 3*y + 6, (y + 2)*(x + 3)), 'K2')
ok(carpan(4*x**2 - 81, (2*x - 9)*(2*x + 9)), 'K3')
ok(75**2 - 25**2 == 5000, 'K4')
ok(carpan(x**4 - 81, (x - 3)*(x + 3)*(x**2 + 9)), 'K5')
ok(ayni((2*a + 5)**2, 4*a**2 + 20*a + 25), 'K6')
ok(deger([a + b - 9, a*b - 14], a**2 + b**2, 53, [a, b]), 'K7')
ok(deger([x + 1/x - 6], x**2 + 1/x**2, 34, [x]), 'K8')
ok(solve(Eq((-10)**2 - 4*m, 0), m) == [25] and ayni(x**2 - 10*x + 25, (x - 5)**2), 'K9')
ok(carpan(x**2 + 5*x - 14, (x + 7)*(x - 2)), 'K10')
ok(carpan(2*x**2 - 5*x - 3, (2*x + 1)*(x - 3)), 'K11')
ok(cozum_kumesi(x**2 - 6*x + 8, [2, 4]), 'K12')
ok(carpan(x**3 - 27, (x - 3)*(x**2 + 3*x + 9)), 'K13')
ok(deger([a - b - 1, a*b - 6], a**3 - b**3, 19, [a, b]), 'K14')
ok(sadelestir((x**2 + 2*x - 8)/(x**2 - 4), (x + 4)/(x + 2), {2, -2}, x**2 - 4), 'K15')
ok(deger([x + 1/x - 4], x**3 + 1/x**3, 52, [x]), 'K16')

print(f'Tüm kontroller geçti: {sayac} assert')
