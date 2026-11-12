:title: II. Teil, Kap. IV & Anhang: Die Transzendenz von π und der Integraph (1895 Deutsch)
:layout: book

.. _fp-part2-ch4-lindemann-pi-de:

II. Teil, IV. Kapitel & Anhang — Die Transzendenz der Zahl π und der Integraph
==============================================================================

.. rubric:: II. Abschnitt, IV. Kapitel (§§ 1–7, S. 53–64) & Anhang (§§ 1–3, S. 64–66; :cite:`B. G. Teubner, 1895 <klein:1895>`)

IV. Kapitel, § 1. Der allgemeine Lindemann'sche Satz
----------------------------------------------------

**1.** Der Beweis, den :person:`Lindemann <lindemann>` (:cite:`1882 <lindemann:1882>`) für die Transzendenz von $\pi$ gegeben hat, erweitert unmittelbar den :person:`Hermite'schen <hermite>` Gedankengang (:cite:`1873 <hermite:1873>`), indem an Stelle einzelner Potenzen $e^\kappa$ symmetrische Summen über :term:`zusammengehörige algebraische Zahlen <conjugate-values>` treten:

**Allgemeiner Lindemann'scher Satz:** *Es ist unmöglich, dass die Zahl $e$ einer Gleichung mit reellen ganzen Koeffizienten ($C_0 \neq 0$) von der Form*

.. math::

   C_0 + C_1\bigl(e^{\kappa_1} + e^{\kappa_2} + \dots + e^{\kappa_N}\bigr) + C_2\bigl(e^{l_1} + e^{l_2} + \dots + e^{l_{N'}}\bigr) + \dots = 0

*genüge, worin $\kappa_1, \dots, \kappa_N$ (für sich) die von Null verschiedenen Wurzeln einer ganzzahligen Gleichung $a\kappa^N + a_1\kappa^{N-1} + \dots + a_N = 0$ ($a > 0,\; a_N \neq 0$), $l_1, \dots, l_{N'}$ (für sich) die Wurzeln von $b l^{N'} + b_1 l^{N'-1} + \dots + b_{N'} = 0$ ($b > 0,\; b_{N'} \neq 0$) usw. bedeuten (unter Einschluss komplexer Grössen).* In :person:`Leibniz' <leibniz>` Ausdrucksweise—der $x^\lambda$ für irrationales algebraisches $\lambda$ *interszendent* nannte—ist $e$ nicht einmal eine interszendente, sondern eine transzendente Zahl höherer Ordnung.

Damit die rationalen symmetrischen Funktionen der Wurzeln gewöhnliche **ganze Zahlen** werden, ziehen wir die **ganzen algebraischen Zahlen** $a\kappa_1, \dots, a\kappa_N$ heran, welche der normierten Gleichung

.. math::

   (a\kappa)^N + a_1(a\kappa)^{N-1} + a_2 a(a\kappa)^{N-2} + \dots + a_N a^{N-1} = 0

genügen (und entsprechend $b l_1, \dots, b l_{N'}$).

IV. Kapitel, §§ 2–3. Das verallgemeinerte Hilfspolynom und der Beweis
---------------------------------------------------------------------

**2.** Mit dem :person:`Gordan'schen <gordan>` Symbol $h^r = r!$ (:cite:`1893 <gordan:1893>`) wählen wir als Multiplikator $M = \varphi(h)$, gebildet aus

.. math::

   \varphi(x) = \frac{x^{p-1}\bigl[(\kappa_1 - x)\cdots(\kappa_N - x)\bigr]^p\,\bigl[(l_1 - x)\cdots(l_{N'} - x)\bigr]^p \cdots a^{Np + N'p + \dots}\,b^{Np + N'p + \dots}\cdots}{(p - 1)!},

wobei die Primzahl $p$ grösser als $|C_0|, a, b, \dots, |a_N|, |b_{N'}|, \dots$ gewählt wird und später unbegrenzt wächst. Es ergeben sich wieder drei Eigenschaften:

a) **$\varphi(h)$ ist eine ganze, durch $p$ nicht teilbare Zahl ($\neq 0$):** In $\varphi(h) = \sum_{r=p-1}^{Np+N'p+\dots+p-1} c_r h^r$ hebt sich für $h^r = r!$ der Nenner $(p - 1)!$ überall fort; alle Glieder ab $r = p$ sind durch $p$ teilbar, während das Anfangsglied ($r = p - 1$) den durch $p$ nicht teilbaren ganzzahligen Wert $(-1)^{p(N+N'+\dots)} a_N^p b_{N'}^p \cdots a^{(N-1)p + N'p + \dots} b^{Np + (N'-1)p + \dots}$ besitzt.
b) **Beliebige Kleinheit für $p \to \infty$:** Bei festem endlichem $x$ werden sowohl $\varphi(x) = \sum c_r x^r$ als auch $\sum |c_r|\,|x|^r$ mit unbegrenzt wachsendem $p$ beliebig klein.
c) **Jede Summe $\sum_{\nu=1}^N \varphi(\kappa_\nu + h)$ ist eine ganze, durch $p$ teilbare Zahl:** In $\varphi(\kappa_\nu + h)$ wird der $\nu$-te Faktor gleich $(-h)$, sodass die niedrigste Potenz $h^p$ ist; die Summation über $\nu = 1, \dots, N$ liefert ganzzahlige symmetrische Funktionen in $a\kappa_\nu, b l_\mu, \dots$ multipliziert mit $\frac{r!}{(p - 1)!}$ ($r \ge p$), also durchweg ganze durch $p$ teilbare Zahlen!

**3.** Für komplexe Exponenten $\kappa_\nu = \kappa' + i\kappa''$ mit $|\kappa_\nu| = \sqrt{{\kappa'}^2 + {\kappa''}^2}$ lautet die Reihengliedspaltung

.. math::

   e^{\kappa_\nu}\cdot h^r = (\kappa_\nu + h)^r + q_{r, \kappa_\nu}\,\kappa_\nu^r\,e^{|\kappa_\nu|} \qquad \bigl(|q_{r, \kappa_\nu}| < 1\bigr).

Multiplikation der angenommenen Gleichung mit $\varphi(h)$ liefert daher

.. math::

   \Biggl[C_0\varphi(h) + C_1\sum_{\nu=1}^N \varphi(\kappa_\nu + h) + C_2\sum_{\mu=1}^{N'} \varphi(l_\mu + h) + \dots\Biggr]
   + \Biggl[C_1\sum_{\nu=1}^N e^{|\kappa_\nu|}\sum_r c_r \kappa_\nu^r q_{r, \kappa_\nu} + \dots\Biggr] = 0,

worin die erste Zeile eine durch $p$ nicht teilbare ganze Zahl ($\neq 0$) ist, die zweite Zeile aber für hinreichend grosses $p$ dem Betrage nach $< 1$ wird—ein Widerspruch!

IV. Kapitel, § 4. Das Lindemann'sche Korollar
---------------------------------------------

**4.** Hieraus folgt unmittelbar das weit allgemeinere **Lindemann'sche Korollar**:

1. **Unverknüpfte algebraische Exponenten bei ganzen Koeffizienten:** Wäre $C'_0 + C'_1 e^{\kappa_1} + C'_2 e^{l_1} + \dots = 0$ ($C'_i \in \mathbb{Z}$) für paarweise verschiedene algebraische Exponenten, so liefert das Produkt $\prod_{\alpha, \beta, \dots} (C'_0 + C'_1 e^{\kappa_\alpha} + C'_2 e^{l_\beta} + \dots)$ über sämtliche konjugierten Wurzeln einen Ausdruck mit symmetrisch zusammengesetzten Exponentenfamilien, der nach dem Lindemann'schen Satze nicht verschwinden kann; also kann auch kein Faktor verschwinden.
2. **Algebraische Koeffizienten und algebraische Exponenten:** Dürfen überdies auch die Koeffizienten $C_0, C_1, C_2, \dots$ beliebige (nicht sämtlich verschwindende) algebraische Zahlen sein, so führt die Produktbildung über alle konjugierten Werte $C_0^{(\alpha)}, C_1^{(\beta)}, C_2^{(\gamma)}, \dots$ auf rationale (und nach Multiplikation mit dem Hauptnenner ganzzahlige) Koeffizienten zurück: **In einer nicht-trivialen Gleichung $C_0 + C_1 e^\kappa + C_2 e^l + \dots = 0$ mit verschiedenen Exponenten können Koeffizienten und Exponenten niemals gleichzeitig sämtlich algebraische Zahlen sein!**

IV. Kapitel, §§ 5–7. Folgerungen für $\pi$, $y = e^x$ und $y = \arcsin x$
-------------------------------------------------------------------------

* **5. Transzendenz von $\pi$:** In :person:`Eulers <euler>` Gleichung $1 + e^{i\pi} = 0$ sind die Koeffizienten $1, 1$ (und der Exponent $0$ in $1 = e^0$) algebraisch; folglich muss der Exponent $i\pi$—und damit **die Zahl $\pi$ selbst**—:term:`transzendent <transcendental-number>` sein!
* **6. Die Exponentialkurve $y = e^x$ ($x = \ln y$):** Abgesehen vom einzigen Punkte $(x = 0,\; y = 1)$ können $x$ und $y$ in $y = e^x$ niemals gleichzeitig algebraisch sein: **die Kurve $y = e^x$ windet sich durch das überall dichte Netz sämtlicher algebraischen Punkte $(x, y)$ der Ebene hindurch, ohne einen einzigen ausser $(0, 1)$ zu treffen!**
* **7. Die Sinusoide $y = \arcsin x$:** Wegen $2ix = e^{iy} - e^{-iy}$ geht ebenso **die Kurve $y = \arcsin x$ ausser durch den Ursprung $(0, 0)$ durch keinen einzigen algebraischen Punkt der Ebene**.

Anhang (§§ 1–3). Der Integraph und die geometrische Konstruktion von $\pi$
--------------------------------------------------------------------------

**1.** Durch den Lindemann'schen Satz ist die Unmöglichkeit der Kreisquadratur in weit allgemeinerem Sinne als im Altertum dargetan: $\pi$ lässt sich nicht nur nicht mit Zirkel und Lineal konstruieren, sondern **auch durch keine einzige höhere algebraische Kurve** als Ordinate zu einer rationalen oder algebraischen Abszisse ausschneiden! Eine wirkliche Konstruktion von $\pi$ erfordert daher einen stetig arbeitenden *transzendenten Apparat*.

**2.** Ein solcher Apparat ist der von dem Ingenieur :person:`Bruno Abdank-Abakanowicz <abakanowicz>` erfundene (:cite:`*Die Integraphen*, Teubner, 1889; *Les intégraphes*, Gauthier-Villars, 1889 <abakanowicz:1889>`) und von G. Coradi in Zürich ausgeführte :term:`Integraph <integraph>`. Ist eine Differentialkurve $y = f(x)$ vorgelegt, so bildet das Gestänge zum Fahrstiftpunkte $(x, y)$ das rechtwinklige Hilfsdreieck $(x, y), (x, 0), (x - 1, 0)$, dessen Hypotenuse gegen die $x$-Achse die Steigung $\tan\vartheta = y$ besitzt; ein scharfkantiges, durch ein Gewicht angedrücktes vertikales Rädchen wird stets parallel zu dieser Hypotenuse geführt und zwingt den Zeichenstift $(X, Y)$ in die Richtung $\frac{dY}{dX} = y$, sodass er in stetigem Zuge die **Integralkurve** $Y = F(x) = \int f(x)\,dx$ aufzeichnet.

.. picture:: /_static/figures/fig_integraph_quadrature.svg
   :alt: Mechanische Quadratur des Kreises x^2 + y^2 = r^2 mittels des Integraphen von Abdank-Abakanowicz
   :caption: Konstruktive Quadratur des Kreises durch den Integraphen von Abdank-Abakanowicz (Klein Anhang, §§ 2–3): Der Fahrstift auf x^2 + y^2 = r^2 steuert die Rädchenneigung tan(vartheta) = y und zeichnet Y = (r^2/2) arcsin(x/r) + (x/2) sqrt(r^2 - x^2) mit den Achsenabschnitten +-pi*r^2/4 und +-pi*r^2/2.

**3.** Wählt man als Differentialkurve den **Kreis** $x^2 + y^2 = r^2$, so verzeichnet der Integraph die aus kongruenten Zweigen bestehende Integralkurve

.. math::

   Y = \int \sqrt{r^2 - x^2}\,dx = \frac{r^2}{2}\arcsin\frac{x}{r} + \frac{x}{2}\sqrt{r^2 - x^2},

welche auf der $Y$-Achse ($X = 0$) die Ordinaten $0,\; \pm\frac{\pi r^2}{2},\; \dots$ und auf den Geraden $X = \pm r$ die Ordinaten $\pm\frac{\pi r^2}{4},\; \pm\frac{3\pi r^2}{4},\; \dots$ ausschneidet—für $r = 1$ also eine scharfe, mühelose mechanische Konstruktion von $\frac{\pi}{4}$, $\frac{\pi}{2}$ und $\pi$ im unmittelbaren Geiste der antiken :term:`Quadratrix <quadratrix>`!
