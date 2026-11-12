:title: II. Teil, Kap. I: Cantors Beweis von der Existenz transzendenter Zahlen (1895 Deutsch)
:layout: book

.. _fp-part2-ch1-cantor-de:

II. Teil, I. Kapitel — Der Cantor'sche Beweis von der Existenz transzendenter Zahlen
====================================================================================

.. rubric:: Zweiter Abschnitt: Die transzendenten Zahlen und die Quadratur des Kreises — I. Kapitel (§§ 1–3; :cite:`B. G. Teubner, 1895, S. 38–43 <klein:1895>`)

§ 1. Rationale, algebraische und transzendente Zahlen
-----------------------------------------------------

**1.** Trägt man die Zahlen als Punkte auf der Abszissenachse auf und beschränkt sich auf die **rationalen Zahlen**, so wird die Achse durch diese Punktreihe *„überall dicht“* erfüllt: in jedem noch so kleinen Zwischenraume liegen unendlich viele rationale Punkte. Gleichwohl wird, wie schon die Alten erkannten, das Kontinuum dadurch nicht erschöpft; zwischen die rationalen schieben sich die irrationalen Zahlen ein, und es fragt sich, ob innerhalb der Irrationalzahlen weitere prinzipielle Unterscheidungen bestehen.

Wir nennen jede reelle Wurzel $\omega$ einer ganzzahligen algebraischen Gleichung

.. math::

   a_0 \omega^n + a_1 \omega^{n-1} + \dots + a_{n-1}\omega + a_n = 0

eine **algebraische Zahl** (wozu für $n = 1$ die rationalen Zahlen gehören). Bildet nun die Gesamtheit aller reellen algebraischen Zahlen bereits das volle Kontinuum, oder bleibt sie eine durchbrochene Punktreihe, in deren Lücken sich **nicht-algebraische**—sogenannte :term:`transzendente Zahlen <transcendental-number>`—einreihen lassen?

Zuerst hat :person:`Liouville <liouville>` (*Comptes rendus*, 1844; *Liouville's Journal*, Bd. 16, 1851) mittels ziemlich komplizierter Kettenbruchbetrachtungen die Existenz transzendenter Zahlen nachgewiesen. Wesentlich einfacher und begrifflich durchsichtiger gestaltet sich der Beweis durch :person:`Georg Cantors <cantor>` fundamentale Abhandlung :cite:`*Über eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen* (*Crelle's Journal*, Bd. 77, 1874 [1873]) <cantor:1874>`, verbunden mit dem Diagonalgedanken, den Cantor 1891 auf der Naturforscherversammlung in Halle vortrug.

§ 2. Abzählbarkeit, Mächtigkeit und die Höhe einer algebraischen Gleichung
--------------------------------------------------------------------------

**2.** Der Beweis beruht darauf, dass **die reellen algebraischen Zahlen eine abzählbare Menge bilden, das Kontinuum hingegen nicht**: die Mannigfaltigkeit der reellen algebraischen Zahlen und die Mannigfaltigkeit der positiven ganzen Zahlen $1, 2, 3, \dots$ lassen sich *ein-eindeutig* aufeinander beziehen. Der scheinbare Widerspruch, dass die positiven ganzen Zahlen nur ein echter Teil der algebraischen Zahlen sind, beruht auf einem falschen Analogieschluss aus dem Endlichen: für unendliche Mengen verliert der Satz, dass der Teil kleiner als das Ganze sei, seine Gültigkeit (wie schon $n \leftrightarrow 2n$ zeigt). An Stelle von „gross“ und „klein“ setzt :person:`Cantor <cantor>` den Begriff der **Mächtigkeit**: *zwei unendliche Mengen haben dieselbe Mächtigkeit, wenn sie sich ein-eindeutig aufeinander beziehen lassen*.

Jede reelle algebraische Zahl genügt genau einer **irreduziblen** Gleichung mit teilerfremden ganzen Koeffizienten und $a_0 > 0$. Wir ordnen diese Gleichungen nach ihrer :term:`Höhe <algebraic-height>`

.. math::

   N = n - 1 + |a_0| + |a_1| + \dots + |a_n|.

Zu jedem gegebenen $N$ gehört wegen $n \le N$ und $|a_0| + \dots + |a_n| = N - (n - 1)$ **nur eine endliche Anzahl irreduzibler Gleichungen** und folglich nur eine endliche Anzahl $\varphi(N)$ reeller algebraischer Zahlen:

.. list-table:: Berechnung von $\varphi(1), \varphi(2), \varphi(3), \varphi(4)$ nach der Höhe $N$
   :header-rows: 1
   :widths: 8 8 24 28 8 24

   * - $N$
     - $n$
     - $(|a_0|, |a_1|, \dots)$
     - Irreduzible Gleichungen (reell)
     - $\varphi(N)$
     - Zugehörige algebraische Zahlen $\omega$
   * - **$1$**
     - $1$
     - $(1, 0)$
     - $\omega = 0$
     - **$1$**
     - $0$
   * - **$2$**
     - $1$
     - $(1, 1)$
     - $\omega \pm 1 = 0$
     - **$2$**
     - $-1,\; +1$
   * - **$3$**
     - $1$
     - $(1, 2),\; (2, 1)$
     - $\omega \pm 2 = 0,\; 2\omega \pm 1 = 0$
     - **$4$**
     - $-2,\; -\frac{1}{2},\; +\frac{1}{2},\; +2$
   * - **$4$**
     - $1, 2$
     - $(1, 3), (3, 1)$; $(1, 1, 1), (1, 0, 2), (2, 0, 1)$
     - $\omega \pm 3 = 0$, $3\omega \pm 1 = 0$, $\omega^2 \pm \omega - 1 = 0$, $\omega^2 - 2 = 0$, $2\omega^2 - 1 = 0$
     - **$12$**
     - $\pm 3,\; \pm\frac{1}{3},\; \frac{\pm 1 \pm \sqrt{5}}{2},\; \pm\sqrt{2},\; \pm\frac{1}{\sqrt{2}}$

Damit lassen sich sämtliche reellen algebraischen Zahlen in eine einzige durchnummerierte Folge $\omega_1, \omega_2, \omega_3, \dots$ bringen.

§ 3. Cantors Diagonalverfahren zur Bildung transzendenter Zahlen
----------------------------------------------------------------

**3.** Schreiben wir sämtliche algebraischen Zahlen $\omega_1, \omega_2, \omega_3, \dots$ unserer Tabelle als unendliche Dezimalbrüche untereinander. Sollen nun in einem noch so kleinen Intervalle—etwa bei vorgeschriebenen ersten fünf Dezimalstellen—:term:`transzendente Zahlen <transcendental-number>` angegeben werden, so wählen wir nach :person:`Cantor <cantor>`:

* als **6. Dezimalstelle** eine Ziffer verschieden von $9$ und verschieden von der 6. Dezimalstelle von $\omega_1$,
* als **7. Dezimalstelle** eine Ziffer verschieden von $9$ und verschieden von der 7. Dezimalstelle von $\omega_2$,
* allgemein als **$(5 + k)$-te Dezimalstelle** eine Ziffer verschieden von $9$ und verschieden von der $(5 + k)$-ten Dezimalstelle von $\omega_k$.

Der so gebildete Dezimalbruch endigt niemals auf lauter Neunen (wodurch jede Mehrdeutigkeit der Dezimaldarstellung ausgeschlossen ist) und weicht von jeder algebraischen Zahl $\omega_k$ der vollständigen Tabelle mindestens an der $(5 + k)$-ten Stelle ab—er ist also gewiss **transzendent**! Da uns überdies auf jeder Stufe acht Ziffern zur freien Verfügung bleiben, lassen sich in jedem noch so kleinen Intervalle gewissermassen $8^\infty$ transzendente Zahlen bilden: *es gibt unendlich viel mehr transzendente als algebraische Zahlen*.
