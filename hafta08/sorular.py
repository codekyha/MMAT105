# MMAT105 -- Hafta 8 Ara Sınav Denemesi: soru bankası (tek kaynak)
# Her soru: h (hafta), z (K/O/Z), konu, soru (LaTeX), sec (5 şık: (LaTeX, değer)),
# dogru (harf), duzen ('5' tek satır, '2' iki sütun, '1' alt alta), cozum (LaTeX).
# tex_uret.py bu dosyadan iki .tex üretir; dogrulama.py değerleri bağımsız hesaplayıp karşılaştırır.
from fractions import Fraction as F

META = dict(
    hafta=8,
    baslik='Ara Sınav Deneme',
    altbaslik='Hafta 1--7 konuları',
    sure=60,
    dosya='hafta8',
)


def n(v):
    """Sayısal şık: LaTeX otomatik üretilir."""
    if isinstance(v, F) and v.denominator != 1:
        s = '-' if v < 0 else ''
        return (r'\(%s\dfrac{%d}{%d}\)' % (s, abs(v.numerator), v.denominator), v)
    return (r'\(%d\)' % int(v), int(v))


S = [
# ------------------------------------------------------------------ Hafta 1
dict(h=1, z='K', konu='İşlem önceliği',
     soru=r'\(18-4\cdot(7-10)\div 2+(-3)^2\) işleminin sonucu kaçtır?',
     sec=[n(-12), n(15), n(21), n(33), n(39)], dogru='D',
     cozum=r'''Önce parantez: \(7-10=-3\). Üs: \((-3)^2=9\). Çarpma ve bölme soldan sağa:
\(4\cdot(-3)=-12\), \ \(-12\div 2=-6\). Son olarak toplama-çıkarma:
\[18-(-6)+9=18+6+9=33.\]
\textit{Tipik hatalar:} \((-3)^2\) yerine \(-9\) almak \(\Rightarrow 15\); işlemi soldan sağa öncelik gözetmeden yapmak (\(18-4=14\), \(14\cdot(-3)\ldots\)) \(\Rightarrow -12\).'''),

dict(h=1, z='O', konu='Ardışık sayılar',
     soru=r'''Ardışık altı çift sayının toplamı \(150\)'dir. Bu sayıların en büyüğü kaçtır?''',
     sec=[n(20), n(25), n(26), n(28), n(30)], dogru='E',
     cozum=r'''Ardışık sayılarda ortalama \(=\) (ilk terim \(+\) son terim)\(\,/\,2\) \(=\) toplam \(\div\) terim sayısı \(=150\div 6=25\).
Terim sayısı çift olduğundan \(25\) ortadaki iki terimin (\(24\) ve \(26\)) ortalamasıdır.
Sayılar: \(20,\ 22,\ 24,\ 26,\ 28,\ 30\). En büyüğü \(30\). (Kontrol: \(20+30=50\), \(3\cdot 50=150\) \checkmark)
\textit{Tipik hatalar:} ortalamayı (\(25\)) ya da en küçük sayıyı (\(20\)) cevap sanmak.'''),

dict(h=1, z='O', konu='Faktöriyel',
     soru=r'\(n\) pozitif bir tam sayı olmak üzere \(\dfrac{(n+1)!-n!}{(n-1)!}=49\) olduğuna göre \(n\) kaçtır?',
     sec=[n(6), n(7), n(8), n(9), n(49)], dogru='B',
     cozum=r'''Pay kısmında \(n!\) ortak çarpan parantezine alınır: \((n+1)!-n!=n!\,(n+1-1)=n\cdot n!\).
\(n!=n\cdot(n-1)!\) olduğundan
\[\frac{n\cdot n!}{(n-1)!}=n\cdot n=n^2=49\ \Rightarrow\ n=7\quad(n>0).\]
\textit{Tipik hata:} \((n+1)!-n!=1\cdot n!\) sanıp \(\dfrac{n!}{(n-1)!}=n=49\) bulmak.'''),

# ------------------------------------------------------------------ Hafta 2
dict(h=2, z='K', konu='Bölen sayısı',
     soru=r'\(600\) sayısının kaç tane pozitif böleni vardır?',
     sec=[n(12), n(24), n(30), n(36), n(48)], dogru='B',
     cozum=r'''\(600=2^3\cdot 3^1\cdot 5^2\). Pozitif bölen sayısı:
\[(3+1)(1+1)(2+1)=4\cdot 2\cdot 3=24.\]
\textit{Tipik hata:} tam bölen sayısını (\(2\cdot 24=48\)) vermek; soru \emph{pozitif} bölenleri soruyor.'''),

dict(h=2, z='O', konu='Bölme',
     soru=r'''\(A\) ve \(B\) doğal sayılardır. \(A\) sayısı \(9\)'a bölündüğünde bölüm \(B\), kalan \(5\)'tir. \(B\) sayısı \(4\)'e bölündüğünde kalan \(3\)'tür. Buna göre \(A\) sayısının \(36\)'ya bölümünden kalan kaçtır?''',
     sec=[n(5), n(8), n(23), n(27), n(32)], dogru='E',
     cozum=r'''\(A=9B+5\) ve \(B=4k+3\) (\(k\) doğal sayı). Yerine koyalım:
\[A=9(4k+3)+5=36k+27+5=36k+32.\]
\(0\le 32<36\) olduğundan kalan \(32\)'dir. (Kontrol: \(k=0\Rightarrow B=3,\ A=32\); \(k=1\Rightarrow B=7,\ A=68=36+32\).)'''),

dict(h=2, z='Z', konu='Asal olmayan bölen sayısı',
     soru=r'''\(x\) pozitif tam sayı olmak üzere \(A=2^x\cdot 5^3\) sayısının asal olmayan pozitif bölenlerinin sayısı \(22\)'dir. Buna göre \(x\) kaçtır?''',
     sec=[n(4), n(5), n(6), n(7), n(8)], dogru='B',
     cozum=r'''Pozitif bölen sayısı \(d(A)=(x+1)(3+1)=4(x+1)\). Asal bölenler yalnızca \(2\) ve \(5\) (iki tane); \(1\) asal olmayan bir bölendir. O hâlde
\[4(x+1)-2=22\ \Rightarrow\ 4(x+1)=24\ \Rightarrow\ x+1=6\ \Rightarrow\ x=5.\]
\textit{Tipik hatalar:} \(4x=24\) yazıp \(x=6\) bulmak; asal bölenleri çıkarmayı unutmak.'''),

# ------------------------------------------------------------------ Hafta 3
dict(h=3, z='K', konu='9 ile bölünebilme',
     soru=r'Üç basamaklı \(\overline{5a6}\) sayısı \(9\) ile tam bölünebildiğine göre \(a\) rakamı kaçtır?',
     sec=[n(1), n(3), n(4), n(7), n(8)], dogru='D',
     cozum=r'''\(9\) ile bölünebilme için rakamlar toplamı \(9\)'un katı olmalı: \(5+a+6=11+a\).
\(a\) bir rakam olduğundan \(11\le 11+a\le 20\); bu aralıktaki tek \(9\) katı \(18\)'dir: \(a=7\). (Kontrol: \(576=9\cdot 64\).)'''),

dict(h=3, z='O', konu='EBOB--EKOK',
     soru=r'''İki pozitif tam sayının EBOB'u \(6\), EKOK'u \(180\)'dir. Sayılardan biri \(36\) olduğuna göre diğeri kaçtır?''',
     sec=[n(15), n(24), n(30), n(45), n(60)], dogru='C',
     cozum=r'''İki sayının çarpımı \(=\) EBOB \(\cdot\) EKOK:
\[36\cdot y=6\cdot 180=1080\ \Rightarrow\ y=30.\]
Kontrol: \(36=2^2\cdot 3^2,\ 30=2\cdot 3\cdot 5\Rightarrow\) EBOB \(=6\), EKOK \(=2^2\cdot 3^2\cdot 5=180\) \checkmark'''),

dict(h=3, z='Z', konu='EBOB problemi',
     soru=r'''Kenar uzunlukları \(84\) m ve \(126\) m olan dikdörtgen biçimindeki bir bahçenin kenarları boyunca, her köşeye birer fidan gelecek şekilde fidan dikilecektir. Ardışık iki fidan arasındaki uzaklık her yerde aynı, metre cinsinden bir tam sayı ve \(10\) m'den kısa olacaktır. Buna göre en az kaç fidan gerekir?''',
     sec=[n(10), n(30), n(60), n(70), n(140)], dogru='C',
     cozum=r'''Köşelere fidan geleceği için aralık \(d\), hem \(84\)'ü hem \(126\)'yı bölmelidir; yani \(d\), EBOB\((84,126)=42\)'nin bir bölenidir:
\(d\in\{1,2,3,6,7,14,21,42\}\). En az fidan için \(d\) en büyük olmalı, ama \(d<10\) koşulu var: \(d=7\).
Kapalı bir çevre üzerinde fidan sayısı \(=\) çevre \(\div\) aralık:
\[\frac{2(84+126)}{7}=\frac{420}{7}=60.\]
\textit{Tipik hatalar:} koşulu unutup \(d=42\) almak \(\Rightarrow 10\); \(d=6\) almak \(\Rightarrow 70\).'''),

# ------------------------------------------------------------------ Hafta 4
dict(h=4, z='K', konu='Kesirlerde işlem sırası',
     soru=r'\(\dfrac{5}{6}-\dfrac{1}{3}\div\dfrac{2}{3}\) işleminin sonucu kaçtır?',
     sec=[n(F(1, 3)), n(F(1, 2)), n(F(11, 18)), n(F(3, 4)), n(F(7, 6))], dogru='A',
     cozum=r'''Önce bölme: \(\dfrac{1}{3}\div\dfrac{2}{3}=\dfrac{1}{3}\cdot\dfrac{3}{2}=\dfrac{1}{2}\). Sonra çıkarma:
\[\frac{5}{6}-\frac{1}{2}=\frac{5}{6}-\frac{3}{6}=\frac{2}{6}=\frac{1}{3}.\]
\textit{Tipik hata:} önce çıkarma yapmak: \(\left(\frac{5}{6}-\frac{1}{3}\right)\div\frac{2}{3}=\frac{1}{2}\cdot\frac{3}{2}=\frac{3}{4}\).'''),

dict(h=4, z='O', konu='Ondalık sayılar',
     soru=r'\(\dfrac{0{,}12}{0{,}04}+\dfrac{1{,}5}{0{,}03}-0{,}2\cdot 15\) işleminin sonucu kaçtır?',
     sec=[n(5), n(23), n(50), n(53), n(56)], dogru='C',
     cozum=r'''Pay ve paydayı \(100\) ile genişletelim:
\(\dfrac{0{,}12}{0{,}04}=\dfrac{12}{4}=3\), \quad \(\dfrac{1{,}5}{0{,}03}=\dfrac{150}{3}=50\), \quad \(0{,}2\cdot 15=3\).
\[3+50-3=50.\]
\textit{Tipik hatalar:} \(\dfrac{1{,}5}{0{,}03}\)'te virgülleri eşitlemeden \(\dfrac{15}{3}=5\) almak \(\Rightarrow 3+5-3=5\); \(0{,}2\cdot 15=30\) sanmak \(\Rightarrow 23\); çıkarmayı unutmak \(\Rightarrow 53\).'''),

dict(h=4, z='O', konu='Rasyonellerde sıralama',
     soru=r'\(a=\dfrac{7}{9},\quad b=\dfrac{5}{6},\quad c=\dfrac{11}{14}\) sayılarının doğru sıralanışı aşağıdakilerden hangisidir?',
     duzen='2', sec=[(r'\(a<c<b\)', 'acb'), (r'\(a<b<c\)', 'abc'), (r'\(c<a<b\)', 'cab'),
          (r'\(b<c<a\)', 'bca'), (r'\(b<a<c\)', 'bac')], dogru='A',
     cozum=r'''Üçü de \(1\)'den küçük ve paydası paydan biraz büyük: \(1\)'e uzaklıklarına bakalım.
\[1-a=\frac{2}{9},\qquad 1-b=\frac{1}{6},\qquad 1-c=\frac{3}{14}.\]
Paydaları eşitlemek yerine ondalık yaklaşımla: \(\frac{2}{9}\approx 0{,}222\), \(\frac{3}{14}\approx 0{,}214\), \(\frac{1}{6}\approx 0{,}167\).
\(1\)'e en uzak olan en küçüktür: \(a<c<b\).
(Doğrudan kontrol: \(a\approx 0{,}778\), \(c\approx 0{,}786\), \(b\approx 0{,}833\).)'''),

# ------------------------------------------------------------------ Hafta 5
dict(h=5, z='K', konu='Parantezli denklem',
     soru=r'\(4(x-3)-3(x+2)=4-x\) denkleminin çözümü kaçtır?',
     sec=[n(1), n(5), n(7), n(11), n(22)], dogru='D',
     cozum=r'''Parantezleri açalım (\(-3\) her iki terimle çarpılır):
\[4x-12-3x-6=4-x\ \Rightarrow\ x-18=4-x\ \Rightarrow\ 2x=22\ \Rightarrow\ x=11.\]
\textit{Tipik hatalar:} \(-3(x+2)=-3x+6\) yazmak \(\Rightarrow x-6=4-x\Rightarrow x=5\); \(2x=22\)'de bölmeyi unutmak \(\Rightarrow 22\).'''),

dict(h=5, z='O', konu='Kesirli katsayılı denklem',
     soru=r'\(\dfrac{x+1}{3}-\dfrac{x-2}{4}=\dfrac{x}{6}\) denkleminin çözümü kaçtır?',
     sec=[n(-2), n(2), n(6), n(10), n(14)], dogru='D',
     cozum=r'''Paydaların EKOK'u \(12\); her terimi \(12\) ile çarpalım:
\[4(x+1)-3(x-2)=2x\ \Rightarrow\ 4x+4-3x+6=2x\ \Rightarrow\ x+10=2x\ \Rightarrow\ x=10.\]
\textit{Tipik hata:} \(-3(x-2)=-3x-6\) yazmak \(\Rightarrow x-2=2x\Rightarrow x=-2\).'''),

dict(h=5, z='Z', konu='Parametreli denklem',
     soru=r'''\(x\)'e bağlı \(\dfrac{ax-2}{3}=x+\dfrac{b}{6}\) denkleminin çözüm kümesi gerçek sayılar kümesi \((\mathbb{R})\) olduğuna göre \(a\cdot b\) kaçtır?''',
     sec=[n(-12), n(-6), n(-4), n(6), n(12)], dogru='A',
     cozum=r'''Her terimi \(6\) ile çarpalım: \(2(ax-2)=6x+b\Rightarrow 2ax-4=6x+b\).
Çözüm kümesi \(\mathbb{R}\) ise her \(x\) için eşitlik sağlanmalı: \(x\)'li terimlerin katsayıları ve sabit terimler eşit olmalı.
\[2a=6\Rightarrow a=3,\qquad b=-4\qquad\Rightarrow\qquad a\cdot b=-12.\]
\textit{Tipik hata:} sol tarafı \(6\) ile çarparken \(-2\)'yi \(2\) ile çarpmayı unutmak \(\Rightarrow b=-2,\ ab=-6\).'''),

# ------------------------------------------------------------------ Hafta 6
dict(h=6, z='O', konu='Denklem sistemi',
     soru=r'\(2x+3y=17\) ve \(3x-y=9\) olduğuna göre \(x\cdot y\) kaçtır?',
     sec=[n(1), n(3), n(4), n(7), n(12)], dogru='E',
     cozum=r'''İkinci denklemden \(y=3x-9\). Birincide yerine koyalım:
\[2x+3(3x-9)=17\Rightarrow 11x-27=17\Rightarrow 11x=44\Rightarrow x=4,\quad y=3\cdot 4-9=3.\]
Kontrol: \(8+9=17\) \checkmark, \(12-3=9\) \checkmark. \quad \(x\cdot y=4\cdot 3=12\).
\textit{Not:} \(4\) ve \(3\) tek tek \(x\) ve \(y\); \(7=x+y\), \(1=x-y\).'''),

dict(h=6, z='Z', konu='Simetrik sistem',
     soru=r'\(\dfrac{x}{3}+\dfrac{y}{4}=5\) ve \(\dfrac{x}{4}+\dfrac{y}{3}=\dfrac{11}{2}\) olduğuna göre \(x+y\) kaçtır?',
     sec=[n(6), n(F(49, 8)), n(F(21, 2)), n(12), n(18)], dogru='E',
     cozum=r'''Katsayılar simetrik: iki denklemi taraf tarafa toplayalım.
\[\left(\frac{1}{3}+\frac{1}{4}\right)x+\left(\frac{1}{4}+\frac{1}{3}\right)y=5+\frac{11}{2}
\ \Rightarrow\ \frac{7}{12}(x+y)=\frac{21}{2}\ \Rightarrow\ x+y=\frac{21}{2}\cdot\frac{12}{7}=18.\]
(Çıkarırsak \(\frac{1}{12}(x-y)=-\frac{1}{2}\Rightarrow x-y=-6\); buradan \(x=6,\ y=12\). Kontrol: \(2+3=5\), \(\frac{3}{2}+4=\frac{11}{2}\) \checkmark)
\textit{Tipik hatalar:} \(\frac{21}{2}\)'yi cevap sanmak; \(\frac{12}{7}\) yerine \(\frac{7}{12}\) ile çarpmak \(\Rightarrow\frac{49}{8}\).'''),

# ------------------------------------------------------------------ Hafta 7
dict(h=7, z='K', konu='Eşitsizlik (tam sayılar)',
     soru=r'\(-2\le 4-x<3\) eşitsizliğini sağlayan kaç tane \(x\) tam sayısı vardır?',
     sec=[n(4), n(5), n(6), n(7), n(8)], dogru='B',
     cozum=r'''Her taraftan \(4\) çıkaralım: \(-6\le -x<-1\). \(-1\) ile çarpınca eşitsizlik yön değiştirir:
\[6\ge x>1\quad\text{yani}\quad 1<x\le 6.\]
Tam sayılar: \(2,3,4,5,6\) \(\Rightarrow\) \(5\) tane. (\(1\) dahil değil, \(6\) dahil.)
\textit{Tipik hata:} uçları karıştırıp \(1\le x\le 6\) almak \(\Rightarrow 6\).'''),

dict(h=7, z='O', konu='Mutlak değerli denklem',
     soru=r'\(|2x-5|=7\) denklemini sağlayan \(x\) değerlerinin çarpımı kaçtır?',
     sec=[n(-6), n(-1), n(5), n(6), n(7)], dogru='A',
     cozum=r'''\(|u|=7\iff u=7\) veya \(u=-7\).
\[2x-5=7\Rightarrow x=6,\qquad 2x-5=-7\Rightarrow x=-1.\]
Çarpım: \(6\cdot(-1)=-6\). \textit{Tipik hata:} kökleri toplamak \(\Rightarrow 5\).'''),

dict(h=7, z='O', konu='Mutlak değerli eşitsizlik',
     soru=r'\(|3-x|\le 4\) eşitsizliğini sağlayan \(x\) tam sayılarının toplamı kaçtır?',
     sec=[n(20), n(21), n(27), n(28), n(35)], dogru='C',
     cozum=r'''\(|3-x|=|x-3|\). \ \(|x-3|\le 4\iff -4\le x-3\le 4\iff -1\le x\le 7\).
Tam sayılar: \(-1,0,1,\dots,7\). Toplam: \(-1+(0+1+\dots+7)=-1+28=27\).
\textit{Tipik hatalar:} \(-1\)'i unutmak \(\Rightarrow 28\); uç noktaları dışlamak (\(0,\dots,6\)) \(\Rightarrow 21\).'''),
]
