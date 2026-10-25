# MMAT105 -- Hafta 15 Final Sınavı Denemesi: soru bankası (tek kaynak)
# Her soru: h (hafta), z (K/O/Z), konu, soru (LaTeX), sec (5 şık: (LaTeX, değer)),
# dogru (harf), duzen ('5' tek satır, '2' iki sütun, '1' alt alta), cozum (LaTeX).
# tex_uret.py bu dosyadan iki .tex üretir; dogrulama.py değerleri bağımsız hesaplayıp karşılaştırır.
from fractions import Fraction as F
import sympy as sp

x_ = sp.Symbol('x')
r2, r3, r5, r6, r7, r10, r15 = (sp.sqrt(k) for k in (2, 3, 5, 6, 7, 10, 15))

META = dict(
    hafta=15,
    baslik='Final Sınavı Deneme',
    altbaslik='Hafta 1--14 konuları',
    sure=75,
    soruara='2.3cm',  # sorular arası çalışma boşluğu
    dosya='hafta15',
)


def n(v):
    """Sayısal şık: LaTeX otomatik üretilir."""
    if isinstance(v, F) and v.denominator != 1:
        s = '-' if v < 0 else ''
        return (r'\(%s\dfrac{%d}{%d}\)' % (s, abs(v.numerator), v.denominator), v)
    v = int(v)
    if abs(v) >= 10000:
        t = '{:,}'.format(abs(v)).replace(',', r'\,')
        return (r'\(%s%s\)' % ('-' if v < 0 else '', t), v)
    return (r'\(%d\)' % v, v)


S = [
# ================================================================ Hafta 1-7
dict(h=1, z='K', konu='İşlem önceliği, işaret',
     soru=r'\((-2)^3-(-3)^2+4\cdot 5-12\div 3\) işleminin sonucu kaçtır?',
     sec=[n(-17), n(-9), n(-1), n(1), n(17)], dogru='C',
     cozum=r'''Üsler: \((-2)^3=-8\), \((-3)^2=9\). Çarpma ve bölme: \(4\cdot 5=20\), \(12\div 3=4\).
\[-8-9+20-4=-1.\]
\textit{Tipik hata:} \(-(-3)^2\) ifadesini \(+9\) almak \(\Rightarrow 17\).'''),

dict(h=2, z='K', konu='Asal çarpanlar',
     soru=r'\(84\) sayısının farklı asal bölenlerinin toplamı kaçtır?',
     sec=[n(7), n(12), n(14), n(16), n(21)], dogru='B',
     cozum=r'''\(84=2^2\cdot 3\cdot 7\). Farklı asal bölenler \(2,\ 3,\ 7\): \ \(2+3+7=12\).
\textit{Tipik hata:} \(2\)'yi iki kez saymak (\(2+2+3+7=14\)).'''),

dict(h=3, z='O', konu='EKOK problemi',
     soru=r'''Bir duraktan üç otobüs hattının otobüsleri sırasıyla \(15\), \(20\) ve \(25\) dakikada bir kalkmaktadır. Üç hattın otobüsleri saat 08.00'de birlikte kalktığına göre, üçü yeniden ilk kez birlikte saat kaçta kalkar?''',
     sec=[('09.00', 60), ('09.15', 75), ('09.40', 100), ('12.00', 240), ('13.00', 300)], dogru='E',
     cozum=r'''Birlikte kalkış aralığı EKOK\((15,20,25)\)'tir:
\(15=3\cdot 5,\ 20=2^2\cdot 5,\ 25=5^2\Rightarrow\) EKOK \(=2^2\cdot 3\cdot 5^2=300\) dakika \(=5\) saat.
\(08.00+5\) saat \(=\) \textbf{13.00}.
\textit{Tipik hatalar:} yalnızca iki hattın EKOK'unu almak: EKOK\((15,20)=60\) dk \(\Rightarrow\) 09.00; EKOK\((20,25)=100\) dk \(\Rightarrow\) 09.40; EKOK\((15,25)=75\) dk \(\Rightarrow\) 09.15.'''),

dict(h=4, z='O', konu='Merdiven kesir',
     soru=r'\(2-\cfrac{1}{1-\cfrac{1}{3}}\) işleminin sonucu kaçtır?',
     sec=[n(F(1, 2)), n(F(2, 3)), n(F(4, 3)), n(F(3, 2)), n(F(5, 2))], dogru='A',
     cozum=r'''En alttan başlayalım: \(1-\dfrac{1}{3}=\dfrac{2}{3}\). \quad \(\dfrac{1}{2/3}=\dfrac{3}{2}\).
\[2-\frac{3}{2}=\frac{1}{2}.\]
\textit{Tipik hata:} \(\dfrac{1}{2/3}\)'ü \(\dfrac{2}{3}\) almak \(\Rightarrow 2-\dfrac{2}{3}=\dfrac{4}{3}\).'''),

dict(h=5, z='O', konu='Denklem kurma',
     soru=r'''Ali'nin parası Ayşe'nin parasının \(3\) katıdır. Ali, Ayşe'ye \(40\) TL verirse paraları eşit oluyor. Ali'nin başlangıçtaki parası kaç TL'dir?''',
     sec=[n(40), n(80), n(100), n(120), n(160)], dogru='D',
     cozum=r'''Ayşe'nin parası \(x\) ise Ali'ninki \(3x\). Ali \(40\) TL verince Ali'de \(3x-40\), Ayşe'de \(x+40\) olur:
\[3x-40=x+40\Rightarrow 2x=80\Rightarrow x=40.\]
Ali'nin başlangıçtaki parası \(3\cdot 40=120\) TL. (Kontrol: \(80=80\) \checkmark)
\textit{Tipik hatalar:} \(x=40\)'ı (Ayşe'nin parası) cevap sanmak; toplamı (\(160\)) vermek.'''),

dict(h=6, z='O', konu='İki bilinmeyenli problem',
     soru=r'''\(30\) soruluk bir sınavda her doğru cevap \(4\) puan kazandırmakta, her yanlış cevap \(1\) puan kaybettirmektedir. Tüm soruları cevaplayan bir öğrenci \(70\) puan aldığına göre kaç soruya doğru cevap vermiştir?''',
     sec=[n(14), n(18), n(20), n(22), n(25)], dogru='C',
     cozum=r'''Doğru sayısı \(d\), yanlış sayısı \(y\): \ \(d+y=30\) ve \(4d-y=70\).
Taraf tarafa toplayalım: \(5d=100\Rightarrow d=20\), \(y=10\). (Kontrol: \(80-10=70\) \checkmark)'''),

dict(h=7, z='Z', konu='Mutlak değerli eşitsizlik',
     soru=r'\(2<|x-1|\le 5\) eşitsizliğini sağlayan kaç tane \(x\) tam sayısı vardır?',
     sec=[n(4), n(6), n(7), n(8), n(10)], dogru='B',
     cozum=r'''\(|x-1|\le 5\iff -4\le x\le 6\). \quad \(|x-1|>2\iff x-1>2\) veya \(x-1<-2\iff x>3\) veya \(x<-1\).
Ortak çözüm: \(-4\le x<-1\) veya \(3<x\le 6\).
Tam sayılar: \(-4,-3,-2\) ve \(4,5,6\) \(\Rightarrow\) \(6\) tane.
\textit{Tipik hata:} \(2\)'yi dahil etmek (\(|x-1|\ge 2\)) \(\Rightarrow\) \(-1\) ve \(3\) de eklenir: \(8\).'''),

# ================================================================ Hafta 9: Üslü
dict(h=9, z='K', konu='Üslü sayılarda işlem',
     soru=r'\(\dfrac{2^5\cdot 4^3}{8^4}\) işleminin sonucu kaçtır?',
     sec=[n(F(1, 2)), n(2), n(4), n(8), n(16)], dogru='A',
     cozum=r'''Hepsini \(2\) tabanına çevirelim: \(4^3=(2^2)^3=2^6\), \(8^4=(2^3)^4=2^{12}\).
\[\frac{2^5\cdot 2^6}{2^{12}}=2^{5+6-12}=2^{-1}=\frac{1}{2}.\]
\textit{Tipik hata:} \((2^3)^4\) için üsleri toplamak (\(2^7\)) \(\Rightarrow 2^4=16\).'''),

dict(h=9, z='O', konu='Ortak çarpan (üslü)',
     soru=r'\(x\) bir gerçek sayı olmak üzere \(\dfrac{2^{x+4}-2^{x}}{2^{x+1}+2^{x}}\) ifadesinin değeri kaçtır?',
     sec=[n(3), n(4), n(5), n(F(16, 3)), n(8)], dogru='C',
     cozum=r'''Pay ve paydada \(2^x\) ortak çarpan parantezine alınır:
\[\frac{2^x(2^4-1)}{2^x(2+1)}=\frac{16-1}{2+1}=\frac{15}{3}=5.\]
\textit{Tipik hatalar:} \(2^{x+4}-2^x=2^4\) gibi üsleri çıkarmak \(\Rightarrow\) \(\dfrac{16}{3}\); paydada \(2^{x+1}+2^x=2^{2x+1}\) sanıp \(2^x\)'leri yanlış sadeleştirmek.'''),

dict(h=9, z='Z', konu='Üslü sayılarda sıralama',
     soru=r'\(a=2^{48},\quad b=3^{36},\quad c=5^{24}\) sayılarının doğru sıralanışı aşağıdakilerden hangisidir?',
     duzen='2',
     sec=[(r'\(a<b<c\)', 'abc'), (r'\(b<c<a\)', 'bca'), (r'\(c<a<b\)', 'cab'),
          (r'\(a<c<b\)', 'acb'), (r'\(c<b<a\)', 'cba')], dogru='D',
     cozum=r'''Üslerin EBOB'u \(12\): hepsini \(12\). kuvvet olarak yazalım.
\[a=(2^4)^{12}=16^{12},\qquad b=(3^3)^{12}=27^{12},\qquad c=(5^2)^{12}=25^{12}.\]
Üsler eşit ve tabanlar pozitif: \(16<25<27\Rightarrow a<c<b\).
\textit{Tipik hata:} yalnızca tabanlara (\(2<3<5\)) ya da yalnızca üslere bakmak.'''),

# ================================================================ Hafta 10: Köklü
dict(h=10, z='K', konu='Kök dışına çıkarma',
     soru=r'\(\sqrt{98}+\sqrt{8}-\sqrt{32}\) işleminin sonucu kaçtır?',
     duzen='2',
     sec=[(r'\(\sqrt{74}\)', sp.sqrt(74)), (r'\(5\sqrt{2}\)', 5 * r2), (r'\(9\sqrt{2}\)', 9 * r2),
          (r'\(13\sqrt{2}\)', 13 * r2), (r'\(3\sqrt{2}\)', 3 * r2)], dogru='B',
     cozum=r'''\(\sqrt{98}=\sqrt{49\cdot 2}=7\sqrt2\), \ \(\sqrt{8}=2\sqrt2\), \ \(\sqrt{32}=\sqrt{16\cdot 2}=4\sqrt2\).
\[7\sqrt2+2\sqrt2-4\sqrt2=5\sqrt2.\]
\textit{Tipik hatalar:} kök içlerini toplamak: \(\sqrt{98+8-32}=\sqrt{74}\) (yanlış!); \(-\sqrt{32}\)'nin işaretini kaçırmak \(\Rightarrow 13\sqrt2\).'''),

dict(h=10, z='O', konu='Paydayı rasyonel yapma',
     soru=r'\(\dfrac{6}{\sqrt{7}-1}-\sqrt{7}\) işleminin sonucu kaçtır?',
     sec=[(r'\(1\)', sp.Integer(1)), (r'\(\sqrt{7}-1\)', r7 - 1), (r'\(2\)', sp.Integer(2)),
          (r'\(\sqrt{7}+1\)', r7 + 1), (r'\(6\)', sp.Integer(6))], dogru='A',
     cozum=r'''Eşlenikle genişletelim:
\[\frac{6}{\sqrt7-1}\cdot\frac{\sqrt7+1}{\sqrt7+1}=\frac{6(\sqrt7+1)}{7-1}=\sqrt7+1.\]
\((\sqrt7+1)-\sqrt7=1\).
\textit{Tipik hata:} \(\sqrt7\)'yi çıkarmayı unutmak \(\Rightarrow \sqrt7+1\).'''),

dict(h=10, z='Z', konu='İç içe kök',
     soru=r'\(\sqrt{11+\sqrt{72}}\) ifadesinin eşiti aşağıdakilerden hangisidir?',
     duzen='2',
     sec=[(r'\(\sqrt{6}+\sqrt{5}\)', r6 + r5), (r'\(2\sqrt{2}+\sqrt{3}\)', 2 * r2 + r3),
          (r'\(2+\sqrt{7}\)', 2 + r7), (r'\(3+2\sqrt{2}\)', 3 + 2 * r2), (r'\(3+\sqrt{2}\)', 3 + r2)],
     dogru='E',
     cozum=r'''Kural: \(\sqrt{a+b+2\sqrt{ab}}=\sqrt a+\sqrt b\) \ (\(a,b>0\)). Önce iç kökü \(2\sqrt{\ \ }\) biçimine getirelim:
\(\sqrt{72}=\sqrt{4\cdot 18}=2\sqrt{18}\). Toplamı \(11\), çarpımı \(18\) olan sayılar: \(9\) ve \(2\).
\[\sqrt{11+2\sqrt{18}}=\sqrt9+\sqrt2=3+\sqrt2.\]
Kontrol: \((3+\sqrt2)^2=9+6\sqrt2+2=11+\sqrt{72}\) \checkmark \
\textit{Tipik hata:} \(2\) çarpanını ayırmadan toplamı \(11\) olan sayılar aramak (\(6\) ve \(5\)).'''),

# ================================================================ Hafta 11: Çarpanlara ayırma
dict(h=11, z='K', konu='İki kare farkı',
     soru=r'\(x^2-y^2=48\) ve \(x+y=12\) olduğuna göre \(x\cdot y\) kaçtır?',
     sec=[n(4), n(16), n(20), n(24), n(32)], dogru='E',
     cozum=r'''\(x^2-y^2=(x-y)(x+y)\Rightarrow 48=(x-y)\cdot 12\Rightarrow x-y=4\).
\(x+y=12\) ile toplarsak \(2x=16\Rightarrow x=8\), \(y=4\). \quad \(x\cdot y=32\).
\textit{Tipik hata:} \(x-y=4\)'ü cevap sanmak.'''),

dict(h=11, z='O', konu='Tam kare özdeşliği',
     soru=r'\(a+b=10\) ve \(a\cdot b=21\) olduğuna göre \(a^2+b^2\) kaçtır?',
     sec=[n(16), n(58), n(79), n(100), n(142)], dogru='B',
     cozum=r'''\((a+b)^2=a^2+2ab+b^2\Rightarrow a^2+b^2=(a+b)^2-2ab=100-42=58\).
\textit{Tipik hatalar:} \(2ab\) yerine \(ab\) çıkarmak \(\Rightarrow 79\); \((a+b)^2=a^2+b^2\) sanmak \(\Rightarrow 100\); \(2ab\)'yi eklemek \(\Rightarrow 142\).'''),

dict(h=11, z='O', konu='Rasyonel ifade sadeleştirme',
     soru=r'''\(x\notin\{-3,\,-2,\,0,\,3\}\) olmak üzere \(\dfrac{x^2-x-6}{x^2-9}\div\dfrac{x+2}{x}\) ifadesinin en sade biçimi aşağıdakilerden hangisidir?''',
     duzen='2',
     sec=[(r'\(\dfrac{x+2}{x+3}\)', (x_ + 2) / (x_ + 3)), (r'\(\dfrac{x}{x-3}\)', x_ / (x_ - 3)),
          (r'\(\dfrac{x-3}{x}\)', (x_ - 3) / x_), (r'\(\dfrac{x}{x+3}\)', x_ / (x_ + 3)),
          (r'\(\dfrac{(x+2)^2}{x(x+3)}\)', (x_ + 2) ** 2 / (x_ * (x_ + 3)))],
     dogru='D',
     cozum=r'''\(x^2-x-6=(x-3)(x+2)\) (çarpımı \(-6\), toplamı \(-1\) olan sayılar: \(-3\) ve \(2\)); \ \(x^2-9=(x-3)(x+3)\).
Bölme, ikinci kesrin ters çevrilip çarpılmasıdır:
\[\frac{(x-3)(x+2)}{(x-3)(x+3)}\cdot\frac{x}{x+2}=\frac{x}{x+3}.\]
\textit{Tipik hata:} ters çevirmeden çarpmak \(\Rightarrow \dfrac{(x+2)^2}{x(x+3)}\).'''),

# ================================================================ Hafta 12: Oran-orantı
dict(h=12, z='K', konu='Oran',
     soru=r'\(\dfrac{a}{b}=\dfrac{5}{8}\) ve \(a+b=91\) olduğuna göre \(b\) kaçtır?',
     sec=[n(21), n(35), n(49), n(56), n(63)], dogru='D',
     cozum=r'''\(a=5k,\ b=8k\Rightarrow 13k=91\Rightarrow k=7\). \quad \(b=8\cdot 7=56\) \ (\(a=35\)).
\textit{Tipik hatalar:} \(a\)'yı (\(35\)) ya da \(b-a\)'yı (\(21\)) vermek.'''),

dict(h=12, z='O', konu='Bileşik orantı',
     soru=r'''\(8\) bahçıvan günde \(6\) saat çalışarak bir parkın bakımını \(5\) günde bitirmektedir. Aynı hızda çalışan \(6\) bahçıvan günde \(4\) saat çalışarak aynı işi kaç günde bitirir?''',
     sec=[n(10), n(12), n(15), n(16), n(20)], dogru='A',
     cozum=r'''İş miktarı \(=\) kişi \(\times\) günlük saat \(\times\) gün sabittir:
\[8\cdot 6\cdot 5=6\cdot 4\cdot g\Rightarrow 240=24g\Rightarrow g=10.\]
\textit{Not:} Bahçıvan sayısı ve günlük çalışma süresi azaldığından gün sayısı artar (ters orantı); oranları ters kurmak en sık hatadır.'''),

dict(h=12, z='Z', konu='Aritmetik ortalama',
     soru=r'''Bir sınıftaki \(24\) öğrencinin not ortalaması \(65\)'tir. Sınıfa, not ortalaması \(80\) olan \(k\) öğrenci katıldığında sınıfın not ortalaması \(70\) oluyor. Buna göre \(k\) kaçtır?''',
     sec=[n(4), n(6), n(8), n(10), n(12)], dogru='E',
     cozum=r'''Toplamlar üzerinden: \(24\cdot 65+80k=70(24+k)\).
\[1560+80k=1680+70k\Rightarrow 10k=120\Rightarrow k=12.\]
(Kısa yol: ilk grup ortalamanın \(5\) altında, yeni grup \(10\) üstünde: \(24\cdot 5=k\cdot 10\Rightarrow k=12\).)'''),

# ================================================================ Hafta 13: Sayı-kesir-yaş
dict(h=13, z='K', konu='Sayı problemi',
     soru=r'''Hangi sayının \(\dfrac{2}{5}\)'inin \(3\) fazlası \(15\)'tir?''',
     sec=[n(18), n(24), n(30), n(36), n(45)], dogru='C',
     cozum=r'''\(\dfrac{2}{5}x+3=15\Rightarrow\dfrac{2}{5}x=12\Rightarrow x=12\cdot\dfrac{5}{2}=30\).
\textit{Tipik hata:} \(3\)'ü çıkarmak yerine eklemek: \(\dfrac25x=18\Rightarrow x=45\).'''),

dict(h=13, z='O', konu='Yaş problemi',
     soru=r'''Bir annenin yaşı ile kızının yaşının toplamı bugün \(50\)'dir. \(4\) yıl önce annenin yaşı, kızının yaşının \(5\) katıydı. Annenin bugünkü yaşı kaçtır?''',
     sec=[n(35), n(39), n(41), n(45), n(46)], dogru='B',
     cozum=r'''Annenin bugünkü yaşı \(a\) ise kızınki \(50-a\). \(4\) yıl önce: \(a-4=5\,(50-a-4)\).
\[a-4=230-5a\Rightarrow 6a=234\Rightarrow a=39.\]
Kontrol: kız \(11\) yaşında; \(4\) yıl önce \(35=5\cdot 7\) \checkmark
\textit{Tipik hata:} annenin \(4\) yıl önceki yaşını (\(35\)) vermek.'''),

dict(h=13, z='O', konu='Kesir problemi',
     soru=r'''Bir öğrenci harçlığının \(\dfrac{1}{3}\)'ü ile kitap, kalan paranın \(\dfrac{1}{4}\)'ü ile defter almıştır. Geriye \(300\) TL kaldığına göre öğrencinin harçlığı kaç TL'dir?''',
     sec=[n(300), n(360), n(400), n(450), n(600)], dogru='E',
     cozum=r'''Kitaptan sonra kalan: \(\dfrac{2}{3}x\). Defter: \(\dfrac14\cdot\dfrac23x=\dfrac{x}{6}\). Geriye kalan:
\[\frac{2}{3}x-\frac{x}{6}=\frac{x}{2}=300\Rightarrow x=600.\]
\textit{Tipik hata:} defter harcamasını unutup \(\frac{2}{3}x=300\) yazmak \(\Rightarrow x=450\).'''),

# ================================================================ Hafta 14: Yüzde, kâr-zarar, karışım, faiz
dict(h=14, z='K', konu='Basit faiz',
     soru=r'''\(40\,000\) TL, yıllık \(\%24\) basit faiz oranıyla \(9\) ay süreyle bankaya yatırılıyor. Bu süre sonunda elde edilen faiz kaç TL'dir?''',
     sec=[n(800), n(4800), n(7200), n(9600), n(47200)], dogru='C',
     cozum=r'''Süre ay cinsinden: \(F=\dfrac{A\cdot n\cdot t}{1200}=\dfrac{40\,000\cdot 24\cdot 9}{1200}=7200\) TL.
\textit{Tipik hatalar:} bir yıllık faizi (\(9600\)) vermek; faiz yerine dönem sonundaki toplam parayı (\(47\,200\)) vermek.'''),

dict(h=14, z='O', konu='İndirim ve kâr',
     soru=r'''Bir satıcı, maliyeti \(1250\) TL olan bir ürünün etiket fiyatını maliyetin \(\%40\) fazlası olarak belirliyor. Ürünü etiket fiyatı üzerinden \(\%20\) indirimle satan satıcının kârı kaç TL'dir?''',
     sec=[n(150), n(250), n(280), n(350), n(500)], dogru='A',
     cozum=r'''Etiket fiyatı: \(1250\cdot\dfrac{140}{100}=1750\) TL. İndirimli satış fiyatı: \(1750\cdot\dfrac{80}{100}=1400\) TL.
\[\text{Kâr}=1400-1250=150\text{ TL}.\]
\textit{Tipik hatalar:} yüzdeleri doğrudan çıkarıp \(\%40-\%20=\%20\) kâr sanmak \(\Rightarrow 250\); indirim tutarını (\(350\)) ya da indirimsiz kârı (\(500\)) vermek.'''),

dict(h=14, z='Z', konu='Karışım',
     soru=r'''Tuz oranı \(\%20\) olan \(300\) gram tuzlu su ile tuz oranı \(\%35\) olan kaç gram tuzlu su karıştırılırsa tuz oranı \(\%30\) olan bir karışım elde edilir?''',
     sec=[n(150), n(300), n(450), n(600), n(900)], dogru='D',
     cozum=r'''Tuz miktarları korunur: \(300\cdot\dfrac{20}{100}+m\cdot\dfrac{35}{100}=(300+m)\cdot\dfrac{30}{100}\).
\(100\) ile çarpalım: \(6000+35m=9000+30m\Rightarrow 5m=3000\Rightarrow m=600\) gram.
(Kısa yol: \(\%20\), hedefin \(10\) puan altında; \(\%35\), \(5\) puan üstünde: \(300\cdot 10=m\cdot 5\Rightarrow m=600\).)'''),
]
