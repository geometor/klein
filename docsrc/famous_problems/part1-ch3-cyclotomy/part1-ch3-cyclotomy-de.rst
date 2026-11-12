:title: I. Teil, Kap. III: Die Kreisteilung (1895 Deutsch)
:layout: book

.. _fp-part1-ch3-cyclotomy-de:

Erster Abschnitt, III. Kapitel — Die Kreisteilung
=================================================

.. rubric:: Erster Abschnitt, III. Kapitel (§§ 1–8; :cite:`B. G. Teubner, 1895, S. 13–19 <klein:1895>`)

§ 1. Historischer Exkurs
------------------------

**1.** Die Aufgabe, einen gegebenen Kreis in $n$ gleiche Teile zu teilen, stammt bereits aus dem klassischen Altertum; lange Zeit hindurch kannte man ihre Ausführbarkeit mit Zirkel und Lineal nur für die Zahlen $n = 2^h$, $3$, $5$ sowie deren Produkte (:person:`Euklid <euclid>`, :cite:`*Elemente*, Buch IV <euclid:elements>`).

Erst :person:`Gauß <gauss>` hat in seinen *Disquisitiones Arithmeticae* (:cite:`1801 <gauss:1801>`) diese Reihe wesentlich erweitert, indem er bewies, dass die Kreisteilung **für jede Primzahl von der Gestalt**

.. math::

   p = 2^{2^\mu} + 1

**mit Zirkel und Lineal möglich, für alle übrigen ungeraden Primzahlen sowie deren Potenzen hingegen unmöglich ist**.

* Setzt man $\mu = 0$ und $\mu = 1$, so erhält man $p = 3$ und $p = 5$, also die schon den Alten bekannten Fälle.
* Für $\mu = 2$ folgt $p = 2^{2^2} + 1 = 17$, das berühmte reguläre Siebzehneck, welches :person:`Gauß <gauss>` am 30. März 1796 entdeckte und vollständig durchführte.
* Für $\mu = 3$ ergibt sich $p = 2^{2^3} + 1 = 257$, ebenfalls eine :term:`Gauß'sche (Fermat'sche) Primzahl <fermat-prime>`; über das reguläre $257$-Eck veröffentlichte :person:`Richelot <richelot>` eine eingehende Abhandlung in *Crelles Journal*, Bd. 9 (:cite:`1832, S. 1–26, 146–161, 209–230, 337–357 <richelot:1832>`): *De resolutione algebraica aequationis $X^{257} = 1\dots$*
* Auch $\mu = 4$ liefert eine Primzahl, nämlich $2^{2^4} + 1 = 65537$. Dem regulären $65537$-Eck hat :person:`Professor Hermes <hermes>` in Lingen zehn Jahre angestrengter Arbeit gewidmet; der Koffer mit seinen umfangreichen Manuskripten wird in der Modellsammlung des mathematischen Lesezimmers zu Göttingen aufbewahrt (vgl. die Mitteilung in den :cite:`*Göttinger Nachrichten* 1894, Nr. 3 <hermes:1894>`).
* Hingegen liefern $\mu = 5$, $\mu = 6$ und $\mu = 7$ *keine* Primzahlen (schon :person:`Euler <euler>` zerlegte $2^{32} + 1 = 641 \cdot 6700417$). Für $\mu = 8$ weiß man bis heute nicht, ob eine Primzahl vorliegt oder nicht; es wäre daher sehr wohl denkbar, dass $\mu = 4$ überhaupt die letzte Zahl dieser Reihe bildet, für welche die Kreisteilung gelingt.

.. picture:: /_static/figures/fig_constructibility_polygons.svg
   :alt: Gauss-Wantzel Kreisteilung (n = 3..18): Konstruierbare reguläre Vielecke im Vergleich zu unlösbaren Fällen
   :caption: Gauß–Wantzel-Übersicht der regulären n-Ecke (n = 3..18): Konstruierbare Vielecke mit Eulerscher Funktion phi(n) = 2^k (grün) gegenüber den unlösbaren Fällen n = 7, 9, 11, 13, 14, 18 (rot gestrichelt).

§§ 2–4. Zurückführung auf Primzahlpotenzen und die Gauß'schen Primzahlen
------------------------------------------------------------------------

**2.** Wir dürfen die Untersuchung der $n$-Teilung von vornherein auf die Fälle beschränken, in denen $n$ eine Primzahl $p$ oder eine Primzahlpotenz $p^\alpha$ ist. Ist nämlich $n = \mu\nu$ zusammengesetzt aus zwei teilerfremden Faktoren $\mu$ und $\nu$ ($\gcd(\mu, \nu) = 1$), so lassen sich stets ganze (positive oder negative) Zahlen $a, b$ bestimmen derart, dass

.. math::

   1 = a\mu + b\nu, \qquad \text{also} \qquad \frac{1}{\mu\nu} = \frac{a}{\nu} + \frac{b}{\mu}.

Kennt man demnach die $\mu$-Teilung und die $\nu$-Teilung, so gewinnt man durch Abtragen der entsprechenden Bögen sofort die $\mu\nu$-Teilung; so beruht für $n = 15 = 3 \cdot 5$ Euklids Konstruktion des Fünfzehnecks (:cite:`*Elemente* IV.16 <euclid:elements>`) auf der Zerlegung $\frac{1}{15} = \frac{2}{3} - \frac{3}{5}$.

**3.** Wie sich in § 5 zeigen wird, kann die Teilung in $p$ gleiche Teile ($p$ Primzahl) nur gelingen, wenn $p = 2^h + 1$ ist. Wir beweisen vorab, dass eine Primzahl die Form $p = 2^h + 1$ **nur dann haben kann, wenn auch der Exponent $h = 2^\mu$ eine Potenz von $2$ ist**.

Erster Beweis (mittels des Fermat'schen Satzes): Ist $p$ eine Primzahl und $a$ durch $p$ nicht teilbar, so gilt $a^{p-1} \equiv +1 \pmod p$; der kleinste positive Exponent $s$, für welchen $a^s \equiv +1 \pmod p$ ausfällt, ist stets ein Teiler von $p - 1$ (für $s = p - 1$ heißt $a$ eine *Primitivwurzel* modulo $p$). Ist nun $p = 2^h + 1$ prim und $s$ der kleinste positive Exponent mit $2^s \equiv +1 \pmod p$, so liegt $p$ zwischen $2^h < p < 2^s$, also ist $s > h$. Aus $2^h \equiv -1 \pmod p$ und $2^s \equiv +1 \pmod p$ folgt durch Division $2^{s-h} \equiv -1 \pmod p$, mithin $s - h \ge h$ oder $s \ge 2h$; andererseits gibt Quadrieren von $2^h \equiv -1 \pmod p$ sogleich $2^{2h} \equiv +1 \pmod p$, also $s \le 2h$ und somit genau $s = 2h$. Da nun $s = 2h$ ein Teiler von $p - 1 = 2^h$ sein muss, ist auch $h$ ein Teiler von $2^{h-1}$, also selbst eine Potenz von $2$: $h = 2^\mu$.

**4.** Zweiter Beweis: Wäre $h$ durch eine ungerade Zahl $2n + 1 > 1$ teilbar, etwa $h = h'(2n + 1)$, so wäre nach der algebraischen Identität

.. math::

   x^{2n+1} + 1 = (x + 1)\!\left(x^{2n} - x^{2n-1} + \dots - x + 1\right)

für $x = 2^{h'}$ die Zahl $p = 2^{h'(2n+1)} + 1$ durch $2^{h'} + 1$ teilbar, mithin keine Primzahl!

§ 5. Die Kreisteilungsgleichung
-------------------------------

**5.** Zeichnen wir in der komplexen $z$-Ebene ($z = x + iy$) den Einheitskreis und teilen ihn von $z = 1$ ausgehend in $n$ gleiche Teile, so verlangt dies die Auflösung von $z^n - 1 = 0$. Spalten wir durch Division mit $z - 1$ die dem Ausgangspunkte entsprechende Wurzel $z = 1$ ab, so erhalten wir die **Kreisteilungsgleichung**:

.. math::

   \frac{z^n - 1}{z - 1} = z^{n-1} + z^{n-2} + \dots + z + 1 = 0.

Für eine Primzahl $n = p$ kommt alles darauf an zu beweisen, dass diese Gleichung $(p - 1)$-ten Grades **irreduzibel** ist; denn alsdann kann sie nach Kapitel I, § 15 nur gelöst werden, wenn $p - 1 = 2^h$, also $p = 2^{2^\mu} + 1$ eine Gauß'sche Primzahl ist.

§ 6. Das Gauß'sche Lemma
------------------------

**6.** Hierzu schalten wir das **Gauß'sche Lemma** ein: *Lässt sich ein ganzzahliges normiertes Polynom*

.. math::

   F(z) = z^m + A z^{m-1} + B z^{m-2} + \dots + L z + M

*in zwei rationale normierte Faktoren $f(z)$ und $\varphi(z)$ zerlegen, so ist diese Zerlegung notwendig schon ganzzahlig.*

*Beweis.* Bringen wir etwaige gebrochene Koeffizienten in $f(z)$ bzw. $\varphi(z)$ je auf ihren kleinsten gemeinsamen Hauptnenner $a_0$ bzw. $b_0$, so entsteht durch Multiplikation mit $a_0 b_0$:

.. math::

   a_0 b_0 F(z) = f_1(z)\,\varphi_1(z) = \left(a_0 z^{m'} + a_1 z^{m'-1} + \dots\right)\!\left(b_0 z^{m''} + b_1 z^{m''-1} + \dots\right),

worin die ganzen Zahlen $a_0, a_1, \dots$ unter sich teilerfremd sind und ebenso $b_0, b_1, \dots$ unter sich teilerfremd sind. Wäre $a_0 b_0 > 1$ und $q$ irgendeine in $a_0 b_0$ aufgehende Primzahl, so sei $a_i$ der erste durch $q$ *nicht* teilbare Koeffizient in $f_1(z)$ und $b_k$ der erste durch $q$ *nicht* teilbare Koeffizient in $\varphi_1(z)$. Im ausmultiplizierten Produkte rechts lautet dann der Koeffizient von $z^{m' + m'' - i - k}$:

.. math::

   a_i b_k + a_{i-1} b_{k+1} + a_{i-2} b_{k+2} + \dots + a_{i+1} b_{k-1} + a_{i+2} b_{k-2} + \dots.

Alle Glieder nach dem ersten sind nach Annahme durch $q$ teilbar, $a_i b_k$ dagegen nicht; andererseits müssen links in $a_0 b_0 F(z)$ sämtliche Koeffizienten durch $a_0 b_0$, also auch durch $q$ teilbar sein! Dieser Widerspruch beweist $a_0 b_0 = 1$, d. h. die Ganzzahligkeit der Faktoren.

§§ 7–8. Die Irreduzibilität der Kreisteilungsgleichung
------------------------------------------------------

**7.** Nach dem Gauß'schen Lemma genügt der Nachweis, dass $f(z) = \frac{z^p - 1}{z - 1}$ für primes $p$ nicht ganzzahlig zerfällt. Wir bedienen uns hierzu der überaus einfachen Methode von :person:`Eisenstein <eisenstein>` (:cite:`*Crelles Journal*, Bd. 39, 1850, S. 167 <eisenstein:1850>`), indem wir $z = x + 1$ substituieren:

.. math::

   f(x + 1) = \frac{(x + 1)^p - 1}{x} = x^{p-1} + p\,x^{p-2} + \frac{p(p-1)}{1\cdot 2} x^{p-3} + \dots + p = 0.

Alle Koeffizienten nach dem höchsten Gliede $x^{p-1}$ enthalten den Primfaktor $p$, während das Absolutglied gleich $p$ selbst (nicht durch $p^2$ teilbar) ist. **Ein solcher Ausdruck ist stets irreduzibel.** Denn setzte man

.. math::

   f(x + 1) = \left(x^m + a_1 x^{m-1} + \dots + a_m\right)\!\left(x^{m'} + b_1 x^{m'-1} + \dots + b_{m'}\right),

so folgte aus $a_m b_{m'} = p$ etwa $a_m = \pm p, b_{m'} = \pm 1$; aus der Teilbarkeit des linearen Gliedes $a_{m-1} b_{m'} + a_m b_{m'-1}$, des quadratischen Gliedes usf. durch $p$ ergäbe sich schrittweise, dass $a_{m-1}, a_{m-2}, \dots, a_1$ und schließlich auch der höchste Koeffizient $1$ von $x^m$ durch $p$ teilbar sein müsste—was unmöglich ist! Damit ist die Kreisteilungsgleichung für jede Primzahl $p$ als irreduzibel erwiesen; insbesondere sind das **reguläre Siebeneck ($p = 7$), Elfeck ($p = 11$) und Dreizehneck ($p = 13$) mit Zirkel und Lineal unkonstruierbar**.

**8.** Es bleibt noch der Fall einer Primzahlpotenz $n = p^\alpha$ ($\alpha \ge 2$) für ungerades $p > 2$. Da jede $p^\alpha$-Teilung die $p^2$-Teilung in sich schließt, genügt der Beweis für $n = p^2$. Beseitigen wir aus $z^{p^2} - 1 = 0$ durch Division mit $z^p - 1$ sämtliche schon zur $p$-Teilung gehörigen Wurzeln (so wie bei der Neunteilung die Drittelpunkte auftreten), so lautet die eigentliche Gleichung der $p^2$-Teilung:

.. math::

   \frac{z^{p^2} - 1}{z^p - 1} = z^{p(p-1)} + z^{p(p-2)} + \dots + z^p + 1 = 0.

Die Substitution $z = x + 1$ verwandelt diese Summe von $p$ Gliedern in

.. math::

   (x + 1)^{p(p-1)} + (x + 1)^{p(p-2)} + \dots + (x + 1)^p + 1 = x^{p(p-1)} + p\cdot \chi(x) = 0,

wo $\chi(x)$ ganzzahlig mit Absolutglied $\chi(0) = 1$ ist. Nach § 7 ist auch diese Gleichung **irreduzibel**, und ihr Grad beträgt $p(p - 1)$. Da für jede ungerade Primzahl $p > 2$ das Produkt $p(p - 1)$ den ungeraden Faktor $p$ enthält, also niemals eine Potenz von $2$ sein kann, **beschränkt sich die Teilbarkeit in Primzahlquadratteile ausschließlich auf $p = 2$ ($p^2 = 4$)**; schon das reguläre Neuneck ($p^2 = 9$, Grad $6$) und Fünfundzwanzigeck ($p^2 = 25$, Grad $20$) sind mit Zirkel und Lineal unmöglich.
