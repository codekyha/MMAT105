# sorular.py'den soru kitapçığı ve çözüm kitapçığı .tex dosyalarını üretir.
# Kullanım: python3 tex_uret.py   (aynı klasörde sorular.py bulunmalı)
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sorular import META, S  # noqa: E402

HARF = 'ABCDE'
ZOR = {'K': 'Kolay', 'O': 'Orta', 'Z': 'Zor'}
N = len(S)
PUAN = 100 / N
PUAN_S = ('%d' % PUAN) if PUAN == int(PUAN) else ('%s' % PUAN).replace('.', '{,}')

PREAMBLE = r'''%% !TEX program = xelatex
%% Bu dosya tex_uret.py tarafından sorular.py'den üretilmiştir; düzenleme için sorular.py'yi değiştirip yeniden üretin.
\documentclass[11pt,a4paper]{article}
\usepackage[margin=1.8cm,top=1.9cm,bottom=1.9cm]{geometry}
\usepackage{fontspec}
\usepackage{polyglossia}
\setdefaultlanguage{turkish}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{enumitem}
\usepackage{multicol}
\usepackage[most]{tcolorbox}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{xcolor}
\usepackage{needspace}
\usepackage[hidelinks]{hyperref}

\definecolor{anamavi}{RGB}{0,45,98}
\definecolor{cozumyesil}{RGB}{0,110,50}
\definecolor{uyarikirmizi}{RGB}{180,20,20}

\titleformat{\section}{\large\bfseries\color{anamavi}}{\thesection.}{0.5em}{}
\titleformat{\subsection}{\normalsize\bfseries\color{anamavi}}{\thesubsection}{0.5em}{}

\pagestyle{fancy}\fancyhf{}
\lhead{\small MMAT105 Genel Matematik}
\rhead{\small Hafta %(hafta)d -- %(sagbaslik)s}
\cfoot{\small\thepage}
\renewcommand{\headrulewidth}{0.4pt}

\newtcolorbox{kural}[1][Kural]{colback=anamavi!5,colframe=anamavi,title=#1,fonttitle=\bfseries,breakable,left=4pt,right=4pt,top=2pt,bottom=2pt}
\newtcolorbox{dikkat}[1][Dikkat]{colback=uyarikirmizi!5,colframe=uyarikirmizi,title=#1,fonttitle=\bfseries,breakable,left=4pt,right=4pt,top=2pt,bottom=2pt}
\newenvironment{cozum}{\begin{tcolorbox}[colback=cozumyesil!6,colframe=cozumyesil,boxrule=0.5pt,left=4pt,right=4pt,top=2pt,bottom=2pt]\textbf{\color{cozumyesil}Çözüm.}\ }{\end{tcolorbox}}
\newcommand{\sk}[1]{\textbf{\color{anamavi}#1)}~}
\setlength{\parindent}{0pt}
\setlength{\parskip}{3pt}
\setlength{\lineskiplimit}{2pt}\setlength{\lineskip}{4pt}
\setlength{\columnsep}{0.9cm}
\setlength{\columnseprule}{0.4pt}
\newlength{\soruara}\setlength{\soruara}{%(soruara)s}

\begin{document}

\begin{minipage}[c]{\textwidth}
{\LARGE\bfseries\color{anamavi} MMAT105 Genel Matematik}\\[4pt]
{\large\bfseries %(baslik)s}\\[2pt]
{\normalsize %(altbaslik)s}\\[6pt]
{\small 2026--2027 Güz}
\end{minipage}

\vspace{4pt}\noindent\textcolor{anamavi}{\rule{\textwidth}{1pt}}
'''


def secenekler(q):
    s = q['sec']
    d = q.get('duzen', '5')
    if d == '5':
        hucre = [r'\sk{%s}%s' % (HARF[i], s[i][0]) for i in range(5)]
        return (r'\par\smallskip\noindent{\setlength{\tabcolsep}{1pt}\begin{tabular*}{\linewidth}{@{}l@{\extracolsep{\fill}}llll@{}}'
                + ' & '.join(hucre) + r'\end{tabular*}}')
    if d == '2':
        h = [r'\sk{%s}%s' % (HARF[i], s[i][0]) for i in range(5)]
        return (r'\par\smallskip\noindent\begin{tabular}{@{}p{0.47\linewidth}p{0.47\linewidth}@{}}'
                + r'%s & %s\\[7pt] %s & %s\\[7pt] %s & \end{tabular}' % tuple(h))
    # '1': alt alta
    return r'\par\smallskip' + ''.join(r'\noindent\sk{%s}%s\par' % (HARF[i], s[i][0]) for i in range(5))


def kitapcik():
    m = dict(META)
    m['sagbaslik'] = META['baslik']
    m.setdefault('soruara', '1.7cm')
    out = [PREAMBLE % m]
    out.append(r'''
\begin{minipage}[t]{0.55\textwidth}
\vspace{2pt}
\textbf{Ad Soyad:} \rule{0.68\linewidth}{0.4pt}\\[12pt]
\textbf{Öğrenci No:} \rule{0.6\linewidth}{0.4pt}
\end{minipage}\hfill
\begin{minipage}[t]{0.42\textwidth}
\begin{kural}[Yönerge]
\small\raggedright
\begin{itemize}[leftmargin=*,itemsep=0pt,topsep=0pt]
\item Soru sayısı: \(%(n)d\); \ önerilen süre: \textbf{\(%(sure)d\) dakika}.
\item Her soru eşit puanlıdır (\(%(puan)s\) puan).
\item Her sorunun yalnızca \textbf{bir} doğru cevabı vardır.
\item Yanlış cevaplar doğru cevapları götürmez.
\end{itemize}
\end{kural}
\end{minipage}

\vspace{6pt}
\begin{multicols}{2}
''' % dict(n=N, sure=META['sure'], puan=PUAN_S))
    for i, q in enumerate(S, 1):
        out.append(r'''\noindent\begin{minipage}{\linewidth}\raggedright
\textbf{\color{anamavi}%d.}\ %s
%s
\end{minipage}
\par\vspace{\soruara}
''' % (i, q['soru'], secenekler(q)))
    out.append(r'\end{multicols}' + '\n')
    # öğrenci cevap tablosu
    out.append(r'''
\vspace{6pt}
\needspace{8\baselineskip}
\noindent\textbf{\color{anamavi}Cevap tablosu} {\small (işaretlediğiniz şıkları buraya da yazabilirsiniz)}\par\smallskip
\noindent''')
    cols = 10
    rows = [list(range(r, min(r + cols, N + 1))) for r in range(1, N + 1, cols)]
    tab = r'\renewcommand{\arraystretch}{1.6}\begin{tabular}{|' + '>{\\centering\\arraybackslash}p{1.25cm}|' * cols + '}\\hline\n'
    for r in rows:
        r2 = r + [None] * (cols - len(r))
        tab += ' & '.join(r'\textbf{%d}' % k if k else '' for k in r2) + r'\\\hline' + '\n'
        tab += ' & '.join('' for _ in r2) + r'\\\hline' + '\n'
    tab += r'\end{tabular}'
    out.append(tab + '\n\n\\vfill\\centering{\\small Başarılar!}\n\\end{document}\n')
    return ''.join(out)


def cozumler():
    m = dict(META)
    m['baslik'] = META['baslik'] + r' -- Cevap Anahtarı ve Çözümler'
    m['sagbaslik'] = META['baslik'] + ' -- Çözümler'
    m.setdefault('soruara', '1.7cm')
    out = [PREAMBLE % m]
    # cevap anahtarı
    cols = 10
    out.append(r'''
\section*{Cevap Anahtarı}
\begin{center}
\renewcommand{\arraystretch}{1.5}
''')
    tab = r'\begin{tabular}{|' + '>{\\centering\\arraybackslash}p{1.1cm}|' * cols + '}\\hline\n'
    for r0 in range(1, N + 1, cols):
        r = list(range(r0, min(r0 + cols, N + 1)))
        r2 = r + [None] * (cols - len(r))
        tab += ' & '.join(r'\textbf{%d}' % k if k else '' for k in r2) + r'\\' + '\n'
        tab += ' & '.join(r'\textbf{\color{cozumyesil}%s}' % S[k - 1]['dogru'] if k else '' for k in r2) + r'\\\hline' + '\n'
    tab += r'\end{tabular}'
    out.append(tab + '\n\\end{center}\n')
    # kısa liste 1-A, 2-C ...
    out.append(r'{\small\textbf{Satır hâlinde:} ' + ', \ '.join('%d-%s' % (i, q['dogru']) for i, q in enumerate(S, 1)) + '}\n\n')
    # konu-zorluk tablosu
    out.append(r'''
\section*{Soruların Konu ve Zorluk Dağılımı}
\begin{center}\small\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}r l l c@{\hspace{1.2em}}|@{\hspace{1.2em}}r l l c@{}}
\toprule
No & Hafta -- Konu & Düzey & Cevap & No & Hafta -- Konu & Düzey & Cevap\\
\midrule
''')
    half = (N + 1) // 2
    for r in range(half):
        cells = []
        for i in (r, r + half):
            if i < N:
                q = S[i]
                cells.append(r'%d & H%d -- %s & %s & %s' % (i + 1, q['h'], q['konu'], ZOR[q['z']], q['dogru']))
            else:
                cells.append(' & & & ')
        out.append(' & '.join(cells) + r'\\' + '\n')
    out.append(r'\bottomrule\end{tabular}' + '\n' + r'\end{center}' + '\n')
    harf = {h: sum(q['dogru'] == h for q in S) for h in HARF}
    zor = {z: sum(q['z'] == z for q in S) for z in 'KOZ'}
    out.append(r'{\small Düzey dağılımı: Kolay %d, Orta %d, Zor (TYT orta üstü) %d. \quad Doğru şık dağılımı: %s.}' % (
        zor['K'], zor['O'], zor['Z'], ', '.join('%s: %d' % (h, harf[h]) for h in HARF)) + '\n')
    out.append('\n\\needspace{8\\baselineskip}\n\\section*{Çözümler}\n')
    for i, q in enumerate(S, 1):
        sec_line = secenekler(q)
        out.append(r'''
\par\medskip\noindent\begin{minipage}{\linewidth}
\noindent\textbf{\color{anamavi}Soru %d.} {\small\color{gray}(Hafta %d -- %s; %s)}\par
%s
%s
\begin{cozum}
%s
\par\smallskip\noindent\textbf{\color{cozumyesil}Cevap: %s}
\end{cozum}
\end{minipage}
''' % (i, q['h'], q['konu'], ZOR[q['z']], q['soru'], sec_line, q['cozum'], q['dogru']))
    out.append('\n\\end{document}\n')
    return ''.join(out)


if __name__ == '__main__':
    d = os.path.dirname(os.path.abspath(__file__))
    ad = META['dosya']
    with open(os.path.join(d, ad + '_deneme_sinavi.tex'), 'w', encoding='utf-8') as f:
        f.write(kitapcik())
    with open(os.path.join(d, ad + '_deneme_cozumler.tex'), 'w', encoding='utf-8') as f:
        f.write(cozumler())
    print('Yazıldı:', ad + '_deneme_sinavi.tex,', ad + '_deneme_cozumler.tex')
