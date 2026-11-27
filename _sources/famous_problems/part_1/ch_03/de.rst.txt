:type: de
:title: I. Teil, Kap. III: Die Kreisteilung (1895 Deutsch)
:layout: book
:canonical_id: Ch. III
:order: 3

.. _fp-part_1-ch_03-de:
.. _fp-part1-ch_03-de:
.. _fp-ch_03-de:
.. _fp-part1-ch3-cyclotomy-de:

Erster Abschnitt, III. Kapitel — Die Kreisteilung
=================================================

.. rubric:: Erster Abschnitt, III. Kapitel (§§ 1–8; :cite:`B. G. Teubner, 1895, S. 13–19 <klein:1895>`)

§ 1. Historischer Exkurs
------------------------

**1.** Die Aufgabe, einen gegebenen Kreis in :math:`n` gleiche Teile zu teilen, stammt bereits aus dem klassischen Altertum; lange Zeit hindurch kannte man ihre Ausführbarkeit mit Zirkel und Lineal nur für die Zahlen :math:`n = 2^h`, :math:`3`, :math:`5` sowie deren Produkte (:person:`Euklid <euclid>`, :cite:`*Elemente*, Buch IV <euclid:elements>`).

Erst :person:`Gauß <gauss>` hat in seinen *Disquisitiones Arithmeticae* (:cite:`1801 <gauss:1801>`) diese Reihe wesentlich erweitert, indem er bewies, dass die Kreisteilung **für jede Primzahl von der Gestalt**

.. math::

   p = 2^{2^\mu} + 1

**mit Zirkel und Lineal möglich, für alle übrigen ungeraden Primzahlen sowie deren Potenzen hingegen unmöglich ist**.

* Setzt man :math:`\mu = 0` und :math:`\mu = 1`, so erhält man :math:`p = 3` und :math:`p = 5`, also die schon den Alten bekannten Fälle.
* Für :math:`\mu = 2` folgt :math:`p = 2^{2^2} + 1 = 17`, das berühmte reguläre Siebzehneck, welches :person:`Gauß <gauss>` am 30. März 1796 entdeckte und vollständig durchführte.
* Für :math:`\mu = 3` ergibt sich :math:`p = 2^{2^3} + 1 = 257`, ebenfalls eine :term:`Gauß'sche (Fermat'sche) Primzahl <fermat-prime>`; über das reguläre :math:`257`-Eck veröffentlichte :person:`Richelot <richelot>` eine eingehende Abhandlung in *Crelles Journal*, Bd. 9 (:cite:`1832, S. 1–26, 146–161, 209–230, 337–357 <richelot:1832>`): *De resolutione algebraica aequationis* :math:`X^{257} = 1\dots`
* Auch :math:`\mu = 4` liefert eine Primzahl, nämlich :math:`2^{2^4} + 1 = 65537`. Dem regulären :math:`65537`-Eck hat :person:`Professor Hermes <hermes>` in Lingen zehn Jahre angestrengter Arbeit gewidmet; der Koffer mit seinen umfangreichen Manuskripten wird in der Modellsammlung des mathematischen Lesezimmers zu Göttingen aufbewahrt (vgl. die Mitteilung in den :cite:`*Göttinger Nachrichten* 1894, Nr. 3 <hermes:1894>`).
* Hingegen liefern :math:`\mu = 5`, :math:`\mu = 6` und :math:`\mu = 7` *keine* Primzahlen (schon :person:`Euler <euler>` zerlegte :math:`2^{32} + 1 = 641 \cdot 6700417`). Für :math:`\mu = 8` weiß man bis heute nicht, ob eine Primzahl vorliegt oder nicht; es wäre daher sehr wohl denkbar, dass :math:`\mu = 4` überhaupt die letzte Zahl dieser Reihe bildet, für welche die Kreisteilung gelingt.

.. picture:: /_static/figures/fig_constructibility_polygons.svg
   :alt: Gauss-Wantzel Kreisteilung (n = 3..18): Konstruierbare reguläre Vielecke im Vergleich zu unlösbaren Fällen
   :caption: Gauß–Wantzel-Übersicht der regulären n-Ecke (n = 3..18): Konstruierbare Vielecke mit Eulerscher Funktion phi(n) = 2^k (grün) gegenüber den unlösbaren Fällen n = 7, 9, 11, 13, 14, 18 (rot gestrichelt).

§§ 2–4. Zurückführung auf Primzahlpotenzen und die Gauß'schen Primzahlen
------------------------------------------------------------------------

**2.** Wir dürfen die Untersuchung der :math:`n`-Teilung von vornherein auf die Fälle beschränken, in denen :math:`n` eine Primzahl :math:`p` oder eine Primzahlpotenz :math:`p^\alpha` ist. Ist nämlich :math:`n = \mu\nu` zusammengesetzt aus zwei teilerfremden Faktoren :math:`\mu` und :math:`\nu` (:math:`\gcd(\mu, \nu) = 1`), so lassen sich stets ganze (positive oder negative) Zahlen :math:`a, b` bestimmen derart, dass

.. math::

   1 = a\mu + b\nu, \qquad \text{also} \qquad \frac{1}{\mu\nu} = \frac{a}{\nu} + \frac{b}{\mu}.

Kennt man demnach die :math:`\mu`-Teilung und die :math:`\nu`-Teilung, so gewinnt man durch Abtragen der entsprechenden Bögen sofort die :math:`\mu\nu`-Teilung; so beruht für :math:`n = 15 = 3 \cdot 5` Euklids Konstruktion des Fünfzehnecks (:cite:`*Elemente* IV.16 <euclid:elements>`) auf der Zerlegung :math:`\frac{1}{15} = \frac{2}{3} - \frac{3}{5}`.

**3.** Wie sich in § 5 zeigen wird, kann die Teilung in :math:`p` gleiche Teile (:math:`p` Primzahl) nur gelingen, wenn :math:`p = 2^h + 1` ist. Wir beweisen vorab, dass eine Primzahl die Form :math:`p = 2^h + 1` **nur dann haben kann, wenn auch der Exponent** :math:`h = 2^\mu` **eine Potenz von** :math:`2` **ist**.

Erster Beweis (mittels des Fermat'schen Satzes): Ist :math:`p` eine Primzahl und :math:`a` durch :math:`p` nicht teilbar, so gilt :math:`a^{p-1} \equiv +1 \pmod p`; der kleinste positive Exponent :math:`s`, für welchen :math:`a^s \equiv +1 \pmod p` ausfällt, ist stets ein Teiler von :math:`p - 1` (für :math:`s = p - 1` heißt :math:`a` eine *Primitivwurzel* modulo :math:`p`). Ist nun :math:`p = 2^h + 1` prim und :math:`s` der kleinste positive Exponent mit :math:`2^s \equiv +1 \pmod p`, so liegt :math:`p` zwischen :math:`2^h < p < 2^s`, also ist :math:`s > h`. Aus :math:`2^h \equiv -1 \pmod p` und :math:`2^s \equiv +1 \pmod p` folgt durch Division :math:`2^{s-h} \equiv -1 \pmod p`, mithin :math:`s - h \ge h` oder :math:`s \ge 2h`; andererseits gibt Quadrieren von :math:`2^h \equiv -1 \pmod p` sogleich :math:`2^{2h} \equiv +1 \pmod p`, also :math:`s \le 2h` und somit genau :math:`s = 2h`. Da nun :math:`s = 2h` ein Teiler von :math:`p - 1 = 2^h` sein muss, ist auch :math:`h` ein Teiler von :math:`2^{h-1}`, also selbst eine Potenz von :math:`2`: :math:`h = 2^\mu`.

**4.** Zweiter Beweis: Wäre :math:`h` durch eine ungerade Zahl :math:`2n + 1 > 1` teilbar, etwa :math:`h = h'(2n + 1)`, so wäre nach der algebraischen Identität

.. math::

   x^{2n+1} + 1 = (x + 1)\!\left(x^{2n} - x^{2n-1} + \dots - x + 1\right)

für :math:`x = 2^{h'}` die Zahl :math:`p = 2^{h'(2n+1)} + 1` durch :math:`2^{h'} + 1` teilbar, mithin keine Primzahl!

§ 5. Die Kreisteilungsgleichung
-------------------------------

**5.** Zeichnen wir in der komplexen :math:`z`-Ebene (:math:`z = x + iy`) den Einheitskreis und teilen ihn von :math:`z = 1` ausgehend in :math:`n` gleiche Teile, so verlangt dies die Auflösung von :math:`z^n - 1 = 0`. Spalten wir durch Division mit :math:`z - 1` die dem Ausgangspunkte entsprechende Wurzel :math:`z = 1` ab, so erhalten wir die **Kreisteilungsgleichung**:

.. math::

   \frac{z^n - 1}{z - 1} = z^{n-1} + z^{n-2} + \dots + z + 1 = 0.

Für eine Primzahl :math:`n = p` kommt alles darauf an zu beweisen, dass diese Gleichung :math:`(p - 1)`-ten Grades **irreduzibel** ist; denn alsdann kann sie nach Kapitel I, § 15 nur gelöst werden, wenn :math:`p - 1 = 2^h`, also :math:`p = 2^{2^\mu} + 1` eine Gauß'sche Primzahl ist.

§ 6. Das Gauß'sche Lemma
------------------------

**6.** Hierzu schalten wir das **Gauß'sche Lemma** ein: *Lässt sich ein ganzzahliges normiertes Polynom*

.. math::

   F(z) = z^m + A z^{m-1} + B z^{m-2} + \dots + L z + M

*in zwei rationale normierte Faktoren* :math:`f(z)` *und* :math:`\varphi(z)` *zerlegen, so ist diese Zerlegung notwendig schon ganzzahlig*.

*Beweis.* Bringen wir etwaige gebrochene Koeffizienten in :math:`f(z)` bzw. :math:`\varphi(z)` je auf ihren kleinsten gemeinsamen Hauptnenner :math:`a_0` bzw. :math:`b_0`, so entsteht durch Multiplikation mit :math:`a_0 b_0`:

.. math::

   a_0 b_0 F(z) = f_1(z)\,\varphi_1(z) = \left(a_0 z^{m'} + a_1 z^{m'-1} + \dots\right)\!\left(b_0 z^{m''} + b_1 z^{m''-1} + \dots\right),

worin die ganzen Zahlen :math:`a_0, a_1, \dots` unter sich teilerfremd sind und ebenso :math:`b_0, b_1, \dots` unter sich teilerfremd sind. Wäre :math:`a_0 b_0 > 1` und :math:`q` irgendeine in :math:`a_0 b_0` aufgehende Primzahl, so sei :math:`a_i` der erste durch :math:`q` *nicht* teilbare Koeffizient in :math:`f_1(z)` und :math:`b_k` der erste durch :math:`q` *nicht* teilbare Koeffizient in :math:`\varphi_1(z)`. Im ausmultiplizierten Produkte rechts lautet dann der Koeffizient von :math:`z^{m' + m'' - i - k}`:

.. math::

   a_i b_k + a_{i-1} b_{k+1} + a_{i-2} b_{k+2} + \dots + a_{i+1} b_{k-1} + a_{i+2} b_{k-2} + \dots.

Alle Glieder nach dem ersten sind nach Annahme durch :math:`q` teilbar, :math:`a_i b_k` dagegen nicht; andererseits müssen links in :math:`a_0 b_0 F(z)` sämtliche Koeffizienten durch :math:`a_0 b_0`, also auch durch :math:`q` teilbar sein! Dieser Widerspruch beweist :math:`a_0 b_0 = 1`, d. h. die Ganzzahligkeit der Faktoren.

§§ 7–8. Die Irreduzibilität der Kreisteilungsgleichung
------------------------------------------------------

**7.** Nach dem Gauß'schen Lemma genügt der Nachweis, dass :math:`f(z) = \frac{z^p - 1}{z - 1}` für primes :math:`p` nicht ganzzahlig zerfällt. Wir bedienen uns hierzu der überaus einfachen Methode von :person:`Eisenstein <eisenstein>` (:cite:`*Crelles Journal*, Bd. 39, 1850, S. 167 <eisenstein:1850>`), indem wir :math:`z = x + 1` substituieren:

.. math::

   f(x + 1) = \frac{(x + 1)^p - 1}{x} = x^{p-1} + p\,x^{p-2} + \frac{p(p-1)}{1\cdot 2} x^{p-3} + \dots + p = 0.

Alle Koeffizienten nach dem höchsten Gliede :math:`x^{p-1}` enthalten den Primfaktor :math:`p`, während das Absolutglied gleich :math:`p` selbst (nicht durch :math:`p^2` teilbar) ist. **Ein solcher Ausdruck ist stets irreduzibel.** Denn setzte man

.. math::

   f(x + 1) = \left(x^m + a_1 x^{m-1} + \dots + a_m\right)\!\left(x^{m'} + b_1 x^{m'-1} + \dots + b_{m'}\right),

so folgte aus :math:`a_m b_{m'} = p` etwa :math:`a_m = \pm p, b_{m'} = \pm 1`; aus der Teilbarkeit des linearen Gliedes :math:`a_{m-1} b_{m'} + a_m b_{m'-1}`, des quadratischen Gliedes usf. durch :math:`p` ergäbe sich schrittweise, dass :math:`a_{m-1}, a_{m-2}, \dots, a_1` und schließlich auch der höchste Koeffizient :math:`1` von :math:`x^m` durch :math:`p` teilbar sein müsste—was unmöglich ist! Damit ist die Kreisteilungsgleichung für jede Primzahl :math:`p` als irreduzibel erwiesen; insbesondere sind das **reguläre Siebeneck** (:math:`p = 7`), **Elfeck** (:math:`p = 11`) **und Dreizehneck** (:math:`p = 13`) **mit Zirkel und Lineal unkonstruierbar**.

**8.** Es bleibt noch der Fall einer Primzahlpotenz :math:`n = p^\alpha` (:math:`\alpha \ge 2`) für ungerades :math:`p > 2`. Da jede :math:`p^\alpha`-Teilung die :math:`p^2`-Teilung in sich schließt, genügt der Beweis für :math:`n = p^2`. Beseitigen wir aus :math:`z^{p^2} - 1 = 0` durch Division mit :math:`z^p - 1` sämtliche schon zur :math:`p`-Teilung gehörigen Wurzeln (so wie bei der Neunteilung die Drittelpunkte auftreten), so lautet die eigentliche Gleichung der :math:`p^2`-Teilung:

.. math::

   \frac{z^{p^2} - 1}{z^p - 1} = z^{p(p-1)} + z^{p(p-2)} + \dots + z^p + 1 = 0.

Die Substitution :math:`z = x + 1` verwandelt diese Summe von :math:`p` Gliedern in

.. math::

   (x + 1)^{p(p-1)} + (x + 1)^{p(p-2)} + \dots + (x + 1)^p + 1 = x^{p(p-1)} + p\cdot \chi(x) = 0,

wo :math:`\chi(x)` ganzzahlig mit Absolutglied :math:`\chi(0) = 1` ist. Nach § 7 ist auch diese Gleichung **irreduzibel**, und ihr Grad beträgt :math:`p(p - 1)`. Da für jede ungerade Primzahl :math:`p > 2` das Produkt :math:`p(p - 1)` den ungeraden Faktor :math:`p` enthält, also niemals eine Potenz von :math:`2` sein kann, **beschränkt sich die Teilbarkeit in Primzahlquadratteile ausschließlich auf** :math:`p = 2` (:math:`p^2 = 4`); schon das reguläre Neuneck (:math:`p^2 = 9`, Grad :math:`6`) und Fünfundzwanzigeck (:math:`p^2 = 25`, Grad :math:`20`) sind mit Zirkel und Lineal unmöglich.
