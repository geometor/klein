:title: I. Teil, Kap. I: Durch Quadratwurzeln lösbare Gleichungen (1895 Deutsch)
:layout: book
:canonical_id: Ch. I
:order: 1
:tracks: English: ch_01-en | German: ch_01-de | Summary: ch_01-summary | Notes: ch_01-notes

.. _fp-part_1-ch_01-de:
.. _fp-part1-ch_01-de:
.. _fp-ch_01-de:
.. _fp-part1-ch1-square-roots-de:

Erster Abschnitt, I. Kapitel — Über diejenigen algebraischen Gleichungen, welche sich durch Quadratwurzeln lösen lassen
=======================================================================================================================

.. rubric:: Erster Abschnitt: Die Möglichkeit der Konstruktion algebraischer Ausdrücke — I. Kapitel (§§ 1–15; :cite:`B. G. Teubner, 1895, S. 4–10 <klein:1895>`)

§§ 1–4. Aufbau der zu konstruierenden Größe :math:`x`
-----------------------------------------------------

**1.** Es sei :math:`x` eine algebraische Größe, welche sich aus gegebenen Strecken mit Zirkel und Lineal konstruieren lässt. Nach unserem Hauptsatze (:ref:`Einleitung <fp-intro-de>`) entsteht :math:`x` aus den gegebenen Größen—die wir nach Wahl einer Längeneinheit als rationale Zahlen bzw. als Elemente eines vorgegebenen :term:`Rationalitätsbereiches <domain-of-rationality>` ansehen—durch endlich viele rationale Rechnungsoperationen und Quadratwurzelausziehungen.

**2.** Um derartige Quadratwurzelausdrücke übersichtlich zu gliedern, teilen wir ihnen je nach der Anzahl übereinander geschachtelter Wurzelzeichen eine bestimmte :term:`Ordnung <radical-order>` :math:`\mu` zu:

* Ein rein rationaler Ausdruck :math:`R` (ohne jede Quadratwurzel) heiße von der **Ordnung** :math:`0`.
* Ein Ausdruck, der rational aus rationalen Größen und einfachen Quadratwurzeln :math:`\sqrt{R_1}, \sqrt{R_2}, \dots` (mit rationalen Radikanden :math:`R_i`) zusammengesetzt ist, heiße von der **Ordnung** :math:`1`, wie etwa

  .. math::

     \frac{\alpha + \beta \sqrt{R_1} + \gamma \sqrt{R_2}}{\delta + \varepsilon \sqrt{R_3}}.

* Werden aus Ausdrücken erster Ordnung abermals Quadratwurzeln gezogen, wie in :math:`\sqrt{p + q\sqrt{R_1}}`, und rational verknüpft, so entsteht ein Ausdruck der **Ordnung** :math:`2`.
* Allgemein heißt ein Ausdruck :math:`x` von der **Ordnung** :math:`\mu`, wenn höchstens :math:`\mu` Quadratwurzelzeichen übereinander geschachtelt auftreten, sodass jede Quadratwurzel :math:`\mu`-ter Ordnung aus einem Ausdrucke :math:`(\mu - 1)`-ter Ordnung gezogen wird.

**3.** Es mögen nun im gesamten Aufbau von :math:`x` überhaupt :math:`m` verschiedene einzelne Quadratwurzeln :math:`Q_1, Q_2, \dots, Q_m` vorkommen, geordnet nach aufsteigender Ordnung (:math:`1 \le \text{Ord}(Q_j) \le \mu`).

**4.** Wir treffen von vornherein die wesentliche Festsetzung, dass **keine der** :math:`m` **Quadratwurzeln** :math:`Q_1, \dots, Q_m` **sich rational durch die übrigen (bzw. vorangehenden) Quadratwurzeln und bekannte rationale Größen ausdrücken lässt**. Wäre nämlich irgendein :math:`Q_k` rational durch die übrigen Quadratwurzeln darstellbar, so würden wir :math:`Q_k` einfach überall durch diesen rationalen Ausdruck ersetzen und dadurch die Gesamtzahl :math:`m` der selbständigen Quadratwurzeln um eine Einheit vermindern. Durch schrittweise Ausführung solcher Reduktionen erreichen wir stets, dass sämtliche :math:`m` beibehaltenen Quadratwurzeln voneinander unabhängig sind.

§§ 5–6. Normalform von :math:`x`
--------------------------------

**5.** Greifen wir unter den Quadratwurzeln höchster Ordnung :math:`\mu` irgendeine bestimmte, :math:`Q_\mu`, heraus! Als Funktion von :math:`Q_\mu` allein betrachtet ist :math:`x` ein rationaler Quotient zweier Polynome in :math:`Q_\mu`, deren Koeffizienten nur noch von den übrigen :math:`m - 1` Quadratwurzeln abhängen. Da :math:`Q_\mu^2` bereits von höchstens :math:`(\mu - 1)`-ter Ordnung ist, lässt sich jede gerade Potenz von :math:`Q_\mu` durch niedrigere Wurzeln und jede ungerade Potenz als Produkt von :math:`Q_\mu` mit niedrigeren Wurzeln schreiben:

.. math::

   x = \frac{a + b Q_\mu}{c + d Q_\mu},

worin :math:`a, b, c, d` die Wurzel :math:`Q_\mu` nicht mehr enthalten.

**6.** Erweitern wir diesen Bruch mit dem konjugierten Faktor :math:`c - d Q_\mu` (wobei :math:`c + d Q_\mu \neq 0` sein muss, da sonst :math:`Q_\mu = -c/d` entgegen § 4 rational durch die übrigen Wurzeln ausdrückbar wäre), so verschwindet :math:`Q_\mu` aus dem Nenner:

.. math::

   x = \frac{(a + b Q_\mu)(c - d Q_\mu)}{c^2 - d^2 Q_\mu^2} = \alpha + \beta Q_\mu,

wo :math:`\alpha` und :math:`\beta` höchstens die übrigen :math:`m - 1` Quadratwurzeln enthalten. Indem wir genau dasselbe Fortschaffen der Wurzeln aus den Nennern der Reihe nach auf :math:`Q_{m-1}, Q_{m-2}, \dots, Q_1` anwenden, bringen wir :math:`x` auf seine **Normalform**: eine ganze lineare Verbindung von Produkten der :math:`m` unabhängigen Quadratwurzeln :math:`Q_1, \dots, Q_m` mit rationalen Koeffizienten:

.. math::

   x = A_0 + \sum_{i} A_i Q_i + \sum_{i < j} A_{ij} Q_i Q_j + \dots + A_{12\dots m} Q_1 Q_2 \cdots Q_m.

§§ 7–8. Die konjugierten Größen
-------------------------------

**7.** Jede Quadratwurzel :math:`Q_k = \sqrt{E_k}` ist ihrem Wesen nach zweideutig (:math:`\pm Q_k`). Erteilen wir in der Normalform von :math:`x` jeder der :math:`m` unabhängigen Quadratwurzeln :math:`Q_1, Q_2, \dots, Q_m` unabhängig voneinander sowohl das positive als auch das negative Vorzeichen (wobei sich bei Vorzeichenwechsel einer inneren Wurzel die äußeren Radikanden entsprechend mitändern), so entspringen im ganzen :math:`2^m` Werte

.. math::

   x_1, \; x_2, \; \dots, \; x_{2^m},

welche wir die :math:`2^m` :term:`konjugierten Werte <conjugate-values>` (*konjugierten Größen*) von :math:`x` nennen.

**8.** So gehören beispielsweise zu :math:`\sqrt{p + q\sqrt{R}}` die vier konjugierten Größen

.. math::

   +\sqrt{p + q\sqrt{R}}, \quad -\sqrt{p + q\sqrt{R}}, \quad +\sqrt{p - q\sqrt{R}}, \quad -\sqrt{p - q\sqrt{R}}.

Dabei brauchen die :math:`2^m` formal gebildeten Ausdrücke :math:`x_1, \dots, x_{2^m}` ihren Zahlenwerten nach nicht sämtlich voneinander verschieden zu sein (in :math:`\sqrt{p + q\sqrt{R}} + \sqrt{p - q\sqrt{R}}` vertauscht der Zeichenwechsel von :math:`\sqrt{R}` nur beide Summanden, sodass derselbe Wert doppelt auftritt).

§ 9. Die zugehörige Gleichung :math:`F(x) = 0`
----------------------------------------------

**9.** Wir bilden nunmehr das Produkt vom Grade :math:`2^m` über sämtliche :math:`2^m` konjugierten Größen:

.. math::

   F(x) = (x - x_1)(x - x_2)\cdots(x - x_{2^m}) = 0.

Kehrt man das Vorzeichen einer Wurzel höchster Ordnung :math:`Q_m` um, so vertauschen sich die Linearfaktoren :math:`(x - x_i)` lediglich paarweise untereinander; das Produkt :math:`F(x)` bleibt ungeändert, enthält also nur gerade Potenzen :math:`Q_m^{2k}` und ist somit von :math:`Q_m` frei. Wiederholt man diesen Schluss schrittweise für sämtliche Wurzeln :math:`\mu`-ter, sodann :math:`(\mu - 1)`-ter Ordnung usf. bis herab zur ersten Ordnung, so fallen alle Quadratwurzeln heraus:

* :math:`F(x) = 0` **ist eine algebraische Gleichung vom Grade** :math:`2^m` **mit rein rationalen Koeffizienten**, welcher :math:`x = x_1` samt allen seinen konjugierten Werten genügt.

§ 10. Andere rationale Gleichungen :math:`f(x) = 0`
---------------------------------------------------

**10.** Genügt unsere Größe :math:`x_1` irgendeiner *anderen* Gleichung mit rationalen Koeffizienten,

.. math::

   f(x) = x^n + a_1 x^{n-1} + \dots + a_{n-1} x + a_n = 0,

so gilt der wichtige Satz: **Jede rationale Gleichung** :math:`f(x) = 0`, **welche durch einen der Werte** :math:`x_1` **befriedigt wird, wird notwendig auch durch sämtliche konjugierten Werte** :math:`x_1, x_2, \dots, x_{2^m}` **befriedigt**.

*Beweis.* Setzen wir :math:`x_1 = \alpha + \beta Q_\mu` in :math:`f(x)` ein und ersetzen :math:`Q_\mu^2` durch seinen Radikanden niedrigerer Ordnung, so nimmt :math:`f(x_1) = 0` die Gestalt an:

.. math::

   f(x_1) = A + B Q_\mu = 0,

worin :math:`A` und :math:`B` die Wurzel :math:`Q_\mu` nicht enthalten. Hier muss notwendig :math:`B = 0` sein; denn wäre :math:`B \neq 0`, so folgte :math:`Q_\mu = -A/B`, d. h. :math:`Q_\mu` ließe sich rational durch die übrigen :math:`m - 1` Quadratwurzeln ausdrücken, entgegen der Voraussetzung in § 4! Aus :math:`B = 0` folgt sogleich auch :math:`A = 0`, mithin

.. math::

   f(\alpha - \beta Q_\mu) = A - B Q_\mu = 0.

Der Zeichenwechsel von :math:`Q_\mu` liefert also wieder eine Wurzel von :math:`f(x) = 0`; und indem man dieselbe Schlussweise auf die Gleichungen :math:`A = 0, B = 0` bezüglich :math:`Q_{m-1}, \dots, Q_1` anwendet, folgt :math:`f(x_k) = 0` für sämtliche :math:`2^m` konjugierten Größen.

§§ 11–12. Die irreduzible Gleichung :math:`\varphi(x) = 0`
----------------------------------------------------------

**11.** Unter allen rationalen Gleichungen, denen :math:`x_1` genügt, greifen wir die normierte Gleichung **niedrigsten positiven Grades** :math:`M` heraus:

.. math::

   \varphi(x) = x^M + c_1 x^{M-1} + \dots + c_M = 0.

Diese Gleichung ist im zugrunde gelegten Rationalitätsbereiche notwendig **irreduzibel** (d. h. nicht in rationale Faktoren niedrigeren Grades zerlegbar), da sonst :math:`x_1` bereits einem der Faktoren genügen müsste.

**12.** Ferner **ist jedes rationale Polynom** :math:`\psi(x)`, **welches für** :math:`x = x_1` **verschwindet, ohne Rest durch** :math:`\varphi(x)` **teilbar**, wodurch :math:`\varphi(x)` zugleich eindeutig bestimmt ist. Denn die euklidische Division liefert :math:`\psi(x) = q(x)\varphi(x) + r(x)` mit rationalen Polynomen :math:`q, r` und :math:`\deg r < M` (falls :math:`r \not\equiv 0`); Einsetzen von :math:`x = x_1` erzwingt :math:`r(x_1) = 0`, was wegen der Minimalität von :math:`M` nur für :math:`r(x) \equiv 0` möglich ist. Insbesondere besitzt :math:`\varphi(x) = 0` lauter einfache Wurzeln, und diese fallen nach § 10 genau mit den voneinander verschiedenen Werten unter :math:`x_1, \dots, x_{2^m}` zusammen.

§§ 13–15. Der Grad der Gleichung :math:`\varphi(x) = 0` eine Potenz von :math:`2`
---------------------------------------------------------------------------------

**13.** Wenden wir § 12 auf das Polynom :math:`F(x)` vom Grade :math:`2^m` aus § 9 an, so ist :math:`F(x)` durch :math:`\varphi(x)` teilbar: :math:`F(x) = \varphi(x) \cdot F_1(x)`. Hat der rationale Quotient :math:`F_1(x)` noch positiven Grad, so verschwindet er für irgendeine der konjugierten Größen :math:`x_k`, folglich nach §§ 10–12 abermals für alle konjugierten Größen und ist wiederum durch :math:`\varphi(x)` teilbar: :math:`F_1(x) = \varphi(x) \cdot F_2(x)` usf. So ergibt sich endlich

.. math::

   F(x) = [\varphi(x)]^\nu \qquad (\nu \ge 1).

**14.** Der Vergleich der Grade beider Seiten liefert unmittelbar

.. math::

   2^m = M \cdot \nu.

Da jeder Teiler einer Potenz von :math:`2` selbst eine Potenz von :math:`2` sein muss, ist der Grad :math:`M` der irreduziblen Gleichung :math:`\varphi(x) = 0` notwendig eine Potenz von :math:`2`:

.. math::

   M = 2^h \qquad (h \ge 0).

.. admonition:: Satz über den Grad konstruierbarer Größen

   **Jede durch Quadratwurzeln darstellbare (mit Zirkel und Lineal konstruierbare) Größe** :math:`x` **genügt einer irreduziblen Gleichung** :math:`\varphi(x) = 0`, **deren Grad** :math:`M = 2^h` **eine Potenz von** :math:`2` **ist**.

**15.** Durch Umkehrung (Kontraposition) fließt hieraus sofort unser allgemeines **Unmöglichkeitskriterium**:

   *Besitzt eine irreduzible Gleichung* :math:`\varphi(x) = 0` *einen Grad, welcher KEINE Potenz von* :math:`2` *ist, so ist sie durch endlich viele Quadratwurzeln unlösbar und ihre Wurzeln sind mit Zirkel und Lineal NICHT konstruierbar*.

Man hüte sich indessen vor dem Fehlschlusse, den Satz aus § 14 einfach umzukehren: **Nicht jede irreduzible Gleichung vom Grade** :math:`2^h` **ist durch Quadratwurzeln allein lösbar**! Schon eine allgemeine irreduzible biquadratische Gleichung (:math:`M = 4 = 2^2`) erfordert zu ihrer Auflösung eine kubische Resolvente (also Kubikwurzeln) und lässt sich nur dann durch bloße Quadratwurzeln lösen, wenn ihre Galois'sche Gruppe sich auf eine Untergruppe von Zweierpotenzordnung reduziert. Bei den Kreisteilungsgleichungen (:ref:`III. und IV. Kapitel <fp-part1-ch3-cyclotomy-de>`) wird sich allerdings zeigen, dass die Bedingung :math:`M = 2^h` infolge des Abel'schen Charakters der Gleichungen zugleich hinreichend ist.
