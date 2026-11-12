:title: I. Teil, Kap. IV: Die Konstruktion des regulären Siebzehnecks (1895 Deutsch)
:layout: book

.. _fp-part1-ch4-heptadecagon-de:

I. Teil, IV. Kapitel — Die Konstruktion des regulären 17-Ecks
=============================================================

.. rubric:: I. Abschnitt, IV. Kapitel (§§ 1–9; :cite:`B. G. Teubner, 1895, S. 19–32 <klein:1895>`)

§§ 1–3. Primitivwurzel modulo 17 und Gauss'sche Periodenbildung
---------------------------------------------------------------

**1.** Nachdem wir im III. Kapitel eingesehen haben, dass nur für die :person:`Gauss'schen <gauss>` :term:`Fermat-Primzahlen <fermat-prime>` die Kreisteilung in eine ungerade Primzahl gleicher Teile durch Zirkel und Lineal möglich sein kann, soll es Aufgabe dieses Kapitels sein, in elementarer Weise auseinanderzulegen, wie sich speziell das **reguläre Siebzehneck** wirklich in den Kreis einzeichnen lässt.

Da wohl bislang aus rein geometrischen Erwägungen noch keine Konstruktionsmethode gefunden ist, untersuchen wir zunächst algebraisch die Wurzeln der Gleichung $16$-ten Grades

.. math::

   x^{16} + x^{15} + \dots + x^2 + x + 1 = 0,

deren transzendente Form lautet:

.. math::

   \varepsilon_\kappa = \cos\frac{2\kappa\pi}{17} + i\sin\frac{2\kappa\pi}{17} = \varepsilon_1^\kappa \qquad (\kappa = 1, 2, \dots, 16),

und übersetzen sodann den daraus resultierenden Quadratwurzelausdruck Schritt für Schritt ins Geometrische.

.. picture:: /_static/figures/fig_gauss_17gon_circle.svg
   :alt: Die 16 Einheitswurzeln des regulären 17-Ecks auf dem Einheitskreis und die Sehnen S_k
   :caption: Einheitswurzeln des regulären 17-Ecks und Sehnenkunstgriff (Klein Fig. 3–4): Konjugierte Paare C_r = eps_r + eps_(17-r) = 2 cos(2r pi/17) und Halbkreissehnen S_k = 2 sin(k pi/34).

**2.** Der Grundgedanke der :person:`Gauss'schen <gauss>` Lösung (:cite:`*Disquisitiones Arithmeticae*, 1801 <gauss:1801>`; vgl. :person:`Bachmann <bachmann>`, :cite:`*Die Lehre von der Kreisteilung*, Leipzig, 1872 <bachmann:1872>`) besteht darin, die $16$ Wurzeln vermittelst einer **Primitivwurzel zum Zahlenmodul $17$** in einen einzigen Zyklus zu ordnen. Die Zahl $a = 3$ hat für $\bmod\,17$ als kleinste positive Lösung von $3^s \equiv +1 \pmod{17}$ den Exponenten $s = 16$:

.. math::

   \begin{alignedat}{4}
   3^1 &\equiv 3,  &\quad 3^5 &\equiv 5,  &\quad 3^9  &\equiv 14, &\quad 3^{13} &\equiv 12, \\
   3^2 &\equiv 9,  &\quad 3^6 &\equiv 15, &\quad 3^{10} &\equiv 8, &\quad 3^{14} &\equiv 2,  \\
   3^3 &\equiv 10, &\quad 3^7 &\equiv 11, &\quad 3^{11} &\equiv 7, &\quad 3^{15} &\equiv 6,  \\
   3^4 &\equiv 13, &\quad 3^8 &\equiv 16, &\quad 3^{12} &\equiv 4, &\quad 3^{16} &\equiv 1   \pmod{17}.
   \end{alignedat}

Ordnen wir die Wurzeln $\varepsilon_\kappa$ nach diesen Resten:

.. math::

   \varepsilon_3,\; \varepsilon_9,\; \varepsilon_{10},\; \varepsilon_{13},\; \varepsilon_5,\; \varepsilon_{15},\; \varepsilon_{11},\; \varepsilon_{16},\; \varepsilon_{14},\; \varepsilon_8,\; \varepsilon_7,\; \varepsilon_4,\; \varepsilon_{12},\; \varepsilon_2,\; \varepsilon_6,\; \varepsilon_1,

so ist jede Wurzel die **dritte Potenz** der ihr vorangehenden ($\varepsilon_{16} = (\varepsilon_{11})^3 = \varepsilon_{33} = \varepsilon_{16}$). Die Gauss'sche Methode zerlegt diesen Zyklus entsprechend den Teilern von $16$ in $8$-, $4$-, $2$- und eingliedrige :term:`Perioden <gaussian-periods>`, die sich der Reihe nach durch quadratische Gleichungen berechnen lassen.

**3.** Lassen wir der Einfachheit halber die Basis $\varepsilon$ weg und schreiten im Zyklus jeweils um zwei Schritte vorwärts, so erhalten wir:

* **Zwei $8$-gliedrige Perioden $\eta_0, \eta_1$:**

  .. math::

     \begin{aligned}
     \eta_0 &= 9 + 13 + 15 + 16 + 8 + 4 + 2 + 1, \\
     \eta_1 &= 3 + 10 + 5 + 11 + 14 + 7 + 12 + 6.
     \end{aligned}

* **Vier $4$-gliedrige Perioden $\eta'_0, \eta'_1$ (aus $\eta_0$) und $(\eta'_0), (\eta'_1)$ (aus $\eta_1$):**

  .. math::

     \begin{alignedat}{2}
     \eta'_0 &= 13 + 16 + 4 + 1,   &\qquad \eta'_1 &= 9 + 15 + 8 + 2, \\
     (\eta'_0) &= 3 + 5 + 14 + 12, &\qquad (\eta'_1) &= 10 + 11 + 7 + 6.
     \end{alignedat}

* **Acht $2$-gliedrige Perioden:** $\eta''_0 = 16 + 1 = C_1$, $\eta''_1 = 13 + 4 = C_4$, usw.

§§ 4–5. Realität und Grössenverhältnisse der Perioden
-----------------------------------------------------

**4.** Da die Wurzeln $r$ und $17 - r$ konjugiert imaginär sind, setzen wir

.. math::

   C_r = \varepsilon_r + \varepsilon_{17-r} = 2\cos\frac{2r\pi}{17} \qquad (r = 1, 2, \dots, 8),

sodass sämtliche Perioden **reelle Zahlen** sind:

.. math::

   \eta_0 = C_1 + C_2 + C_4 + C_8, \quad \eta_1 = C_3 + C_5 + C_6 + C_7, \quad \eta'_0 = C_1 + C_4, \quad \eta'_1 = C_2 + C_8, \quad (\eta'_0) = C_3 + C_5, \quad (\eta'_1) = C_6 + C_7.

**5.** Um die Vorzeichen der Quadratwurzeln eindeutig festzulegen, teilen wir die Hälfte des Einheitskreises in $17$ gleiche Bögen und bezeichnen die Sehnen vom Anfangspunkt $0$ mit $S_1 < S_2 < \dots < S_{17} = 2$, wobei $S_k = 2\sin\frac{k\pi}{34}$. Dann gelten die Relationen:

.. math::

   C_1 = S_{13}, \quad C_2 = S_9, \quad C_3 = S_5, \quad C_4 = S_1, \quad C_5 = -S_3, \quad C_6 = -S_7, \quad C_7 = -S_{11}, \quad C_8 = -S_{15}.

Daraus lesen wir unmittelbar ab, dass alle massgeblichen Periodendifferenzen **positiv** sind:

.. math::

   \begin{aligned}
   \eta_0 - \eta_1 &= S_{13} + S_9 + S_{11} + S_7 + S_3 + S_1 - S_{15} - S_5 > 0 \implies \eta_0 > \eta_1, \\
   (\eta'_0) - (\eta'_1) &= S_{11} + S_7 + S_5 - S_3 > 0 \implies (\eta'_0) > (\eta'_1), \\
   \eta'_0 - \eta'_1 &= S_{15} + S_{13} - S_9 + S_1 > 0 \implies \eta'_0 > \eta'_1, \\
   \eta''_0 - \eta''_1 &= C_1 - C_4 = S_{13} - S_1 > 0 \implies \eta''_0 > \eta''_1.
   \end{aligned}

Überdies liefert das $64$-gliedrige Multiplikationsschema die bemerkenswerte Relation:

.. math::

   (\eta'_0 - \eta'_1)\bigl((\eta'_0) - (\eta'_1)\bigr) = 2(\eta_0 - \eta_1).

§ 6. Die Kette der vier quadratischen Gleichungen und die Normalform
--------------------------------------------------------------------

**6.** Durch Berechnung der elementarsymmetrischen Funktionen erhalten wir der Reihe nach die vier quadratischen Gleichungen:

1. **Erste Gleichung:** $\eta_0 + \eta_1 = -1$ und $\eta_0 \cdot \eta_1 = -4$ (jede der $16$ Wurzeln tritt viermal auf), also wegen $\eta_0 > \eta_1$:

   .. math::

      \eta^2 + \eta - 4 = 0 \implies \eta_0 = \frac{-1 + \sqrt{17}}{2}, \quad \eta_1 = \frac{-1 - \sqrt{17}}{2}.

2. **Zweite Gleichung:** $\eta'_0 + \eta'_1 = \eta_0$ und $\eta'_0 \cdot \eta'_1 = -1$, also wegen $\eta'_0 > \eta'_1$:

   .. math::

      {\eta'}^2 - \eta_0 \eta' - 1 = 0 \implies \eta'_0 = \frac{\eta_0 + \sqrt{\eta_0^2 + 4}}{2}, \quad \eta'_1 = \frac{\eta_0 - \sqrt{\eta_0^2 + 4}}{2}.

3. **Dritte Gleichung:** $(\eta'_0) + (\eta'_1) = \eta_1$ und $(\eta'_0)\cdot(\eta'_1) = -1$, also wegen $(\eta'_0) > (\eta'_1)$:

   .. math::

      (\eta')^2 - \eta_1(\eta') - 1 = 0 \implies (\eta'_0) = \frac{\eta_1 + \sqrt{\eta_1^2 + 4}}{2}, \quad (\eta'_1) = \frac{\eta_1 - \sqrt{\eta_1^2 + 4}}{2}.

4. **Vierte Gleichung:** $\eta''_0 + \eta''_1 = \eta'_0$ und $\eta''_0 \cdot \eta''_1 = (16 + 1)(13 + 4) = 12 + 3 + 14 + 5 = (\eta'_0)$, also wegen $\eta''_0 > \eta''_1$:

   .. math::

      {\eta''}^2 - \eta'_0 \eta'' + (\eta'_0) = 0 \implies \eta''_0 = \frac{\eta'_0 + \sqrt{{\eta'_0}^2 - 4(\eta'_0)}}{2}, \quad \eta''_1 = \frac{\eta'_0 - \sqrt{{\eta'_0}^2 - 4(\eta'_0)}}{2}.

Vermöge $(\eta'_0 - \eta'_1)((\eta'_0) - (\eta'_1)) = 2(\eta_0 - \eta_1)$ gilt für die Radikale die rationale Abhängigkeit

.. math::

   \sqrt{\eta_0^2 + 4}\cdot\sqrt{\eta_1^2 + 4} = 2\sqrt{17},

sodass sich $\sqrt{\eta_1^2 + 4}$ rational durch $\sqrt{17}$ und $\sqrt{\eta_0^2 + 4}$ ausdrückt. Einsetzen der Werte ergibt die explizite Normalform:

.. math::

   \begin{aligned}
   \eta'_0 &= \frac{-1 + \sqrt{17} + \sqrt{34 - 2\sqrt{17}}}{4}, \qquad
   (\eta'_0) = \frac{-1 - \sqrt{17} + \sqrt{34 + 2\sqrt{17}}}{4}, \\[6pt]
   \eta''_0 &= 2\cos\frac{2\pi}{17} = \frac{-1 + \sqrt{17} + \sqrt{34 - 2\sqrt{17}}}{8} \\
   &\quad + \frac{1}{8}\sqrt{68 + 12\sqrt{17} - 16\sqrt{34 + 2\sqrt{17}} - 2(1 - \sqrt{17})\sqrt{34 - 2\sqrt{17}}}.
   \end{aligned}

§ 7. Geschichtlicher Exkurs über Konstruktionen mit beschränkten Hilfsmitteln
-----------------------------------------------------------------------------

**7.** Wir schalten hier einen geschichtlichen Exkurs über Konstruktionen mit Zirkel und Lineal ein:

* *In der Geometrie der Alten wird Zirkel und Lineal immer nebeneinander gebraucht*, ohne zu unterscheiden, ob der einzelne Schritt mit dem Zirkel oder mit dem Lineal ausgeführt wird.
* Demgegenüber hat im Jahre **1797** der Italiener :person:`Mascheroni <mascheroni>` in seiner :cite:`*Geometria del compasso* <mascheroni:1797>` alle Konstruktionen **nur mit dem Zirkel allein** ausgeführt, wobei er für den Mechaniker betont, dass Zirkelkonstruktionen praktisch genauer seien als Linealkonstruktionen (deutscher Auszug von Hutt, *Die Mascheroni'schen Constructionen*, Halle, 1880). *(Fussnote 1895, S. 27: „Eine Construction des 17-Ecks nach Mascheroni nur mit dem Zirkel ist noch nicht versucht, obgleich sie jedenfalls möglich ist.“)*
* Umgekehrt haben die Franzosen—besonders die Schüler Carnots (*Géométrie de position*; vgl. auch :person:`Lambert <lambert>`, *Freie Perspective*, 1774, sowie :person:`Brianchon <brianchon>`, *Les applications de la théorie des transversales*, 1818, für Vermessungsarbeiten im Felde)—möglichst viel mit geraden Linien allein konstruiert. Algebraisch beantwortet sich die Reichweite sofort: **Mit dem Lineal allein können wir alle und nur diejenigen algebraischen Ausdrücke konstruieren, deren algebraische Form rational ist.**
* :person:`Poncelet <poncelet>` sprach zuerst in seinem :cite:`*Traité des propriétés projectives* (Bd. I, Nr. 351–357) <poncelet:1822>` den Gedanken aus—den :person:`Steiner <steiner>` 1833 in seiner berühmten Schrift :cite:`*Die geometrischen Constructionen, ausgeführt mittels der geraden Linie und eines festen Kreises* <steiner:1833>` durchführte—, dass **ein einziger fester Kreis mit gegebenem Mittelpunkt nebst dem Lineal allein ausreicht, um sämtliche Quadratwurzelausdrücke zu konstruieren** (:term:`Satz von Poncelet–Steiner <poncelet-steiner-theorem>`).

§§ 8–9. Geometrische Konstruktion nach von Staudt und Schröter mit einem festen Kreise
--------------------------------------------------------------------------------------

**8.** Im Anschluss an :person:`von Staudt <staudt>` (:cite:`*Crelle's Journal*, Bd. 24, 1842 <staudt:1842>`) und :person:`Schröter <schroeter>` (:cite:`*Crelle's Journal*, Bd. 75, 1872 <schroeter:1872>`) zeigen wir zunächst, **wie man mit Hilfe eines festen Einheitskreises $x^2 + y(y - 2) = 0$ und des Lineals jede quadratische Gleichung $x^2 - px + q = 0$ mit reellen Wurzeln $x_1, x_2$ löst**:

Man trägt auf der oberen Tangente $y = 2$ vom oberen Scheitel $A(0, 2)$ aus das Stück $\frac{4}{p}$ und auf der unteren Tangente $y = 0$ (der $x$-Achse) vom unteren Scheitel $O(0, 0)$ aus das Stück $\frac{q}{p}$ ab, verbindet beide Punkte durch die **Transversale 3** und projiziert deren Schnittpunkte mit dem Kreise von $A(0, 2)$ aus durch die **Strahlen 1 und 2** auf die $x$-Achse: diese schneiden genau $x_1$ und $x_2$ ab! Denn aus dem Linienpaar $[2x + x_1(y - 2)][2x + x_2(y - 2)] = 0$ folgt nach Abzug von $x^2 + y(y - 2) = 0$ und Abspaltung von $y - 2 = 0$ als Gleichung der Geraden 3 sofort $\frac{p}{2}x + \frac{q}{4}(y - 2) - y = 0$.

.. picture:: /_static/figures/fig_von_staudt_quadratic.svg
   :alt: Projektive Lösung der quadratischen Gleichung x^2 - px + q = 0 am festen Einheitskreis
   :caption: Lösung von x^2 - px + q = 0 nach von Staudt und Schröter (Klein § 8, Fig. I): Die Verbindungsgerade 3 von (q/p, 0) und (4/p, 2) liefert durch Projektion aus A(0, 2) die Wurzeln x_1, x_2 auf y = 0.

**9.** Zur Ausführung am Siebzehneck lösen wir am selben festen Kreise nacheinander die vier quadratischen Gleichungen für $\eta_0, \eta_1$, $\eta'_0$, $(\eta'_0)$ und $\eta''_0 = 2\cos\frac{2\pi}{17}$, wozu oben ($y = 2$) die Abschnitte $-4,\; +\frac{4}{\eta_0},\; +\frac{4}{\eta_1},\; +\frac{4}{\eta'_0}$ und unten ($y = 0$) die Abschnitte $+4,\; -\frac{1}{\eta_0},\; -\frac{1}{\eta_1},\; +\frac{(\eta'_0)}{\eta'_0}$ abzutragen sind:

1. **Erste Gleichung ($\eta^2 + \eta - 4 = 0$):** Verbinde $(+4, 0)$ unten mit $(-4, 2)$ oben; die Projektion der beiden Kreisschnittpunkte aus $A(0, 2)$ liefert $\eta_0 > 0$ und $\eta_1 < 0$ auf der $x$-Achse.
2. **Projektive Zuordnung $x' = \frac{4}{x}$ (Fig. 5):** Projiziert man den zu $x$ gehörigen Kreisschnittpunkt des Strahls $Ax$ vom unteren Scheitel $O(0, 0)$ auf die obere Tangente $y = 2$, so entsteht eine projektive Punktreihenbeziehung mit $x = \infty \leftrightarrow x' = 0$ und Fixpunkt $x = x' = 2$, also $x' = \frac{4}{x}$. So erhält man unmittelbar $+\frac{4}{\eta_0}$ und $+\frac{4}{\eta_1}$ auf $y = 2$.
3. **Zweite und dritte Gleichung ($\eta'_0$ und $(\eta'_0)$, Fig. 6–7):** Die Gerade von $(-4, 2)$ oben nach $(+1, 0)$ unten schneidet den vertikalen Durchmesser im festen Punkte $\left(0, \frac{2}{5}\right)$. Verbindet man diesen Punkt mit $\left(\frac{4}{\eta_0}, 2\right)$ bzw. $\left(\frac{4}{\eta_1}, 2\right)$, so schneiden die Geraden $5y - 2\eta_0 x = 2$ bzw. $5y - 2\eta_1 x = 2$ auf der $x$-Achse genau $-\frac{1}{\eta_0}$ bzw. $-\frac{1}{\eta_1}$ ab! Die zugehörigen Staudt-Transversalen liefern durch Projektion aus $A(0, 2)$ die positiven Wurzeln $\eta'_0$ und $(\eta'_0)$.
4. **Vierte Gleichung ($\eta''_0 = 2\cos\frac{2\pi}{17}$, Fig. 8 & Tafel Fig. II):** Projektion des Kreisschnittpunktes von $A\eta'_0$ aus $O(0, 0)$ nach oben gibt $\frac{4}{\eta'_0}$. Die Gerade von $(+4, 2)$ oben nach $((\eta'_0), 0)$ unten trifft die $y$-Achse in $\left(0, \frac{2(\eta'_0)}{(\eta'_0) - 4}\right)$; deren Verbindung mit $\left(\frac{4}{\eta'_0}, 2\right)$ ($2\eta'_0 x + ((\eta'_0) - 4)y = 2(\eta'_0)$) schneidet unten genau $\frac{(\eta'_0)}{\eta'_0}$ ab. Die Staudt-Transversale von $\left(\frac{(\eta'_0)}{\eta'_0}, 0\right)$ nach $\left(\frac{4}{\eta'_0}, 2\right)$ liefert bei Projektion ihres oberen Kreisschnittpunktes aus $A(0, 2)$ auf der $x$-Achse $\eta''_0 = 2\cos\frac{2\pi}{17}$ und **auf dem horizontalen Durchmesser $y = 1$ direkt $\cos\frac{2\pi}{17}$**—woraus das Lot sofort die **erste und sechzehnte Ecke** des regulären $17$-Ecks auf dem festen Kreise ausschneidet!

.. picture:: /_static/figures/fig_von_staudt_17gon.svg
   :alt: Ausgeführte Konstruktion des regulären 17-Ecks mit einem einzigen festen Kreis und Lineal
   :caption: Vollständige Konstruktion des regulären 17-Ecks mit einem festen Kreis C_0 und dem Lineal (Klein § 9, Tafel Fig. II; exakt konstruiert in geometor.klein.heptadecagon).
