:title: I. Teil, Kap. I: Durch Quadratwurzeln lösbare Gleichungen (1895 Deutsch)
:layout: book

.. _fp-part1-ch1-square-roots-de:

Erster Abschnitt, I. Kapitel — Über diejenigen algebraischen Gleichungen, welche sich durch Quadratwurzeln lösen lassen
=======================================================================================================================

.. rubric:: Erster Abschnitt: Die Möglichkeit der Konstruktion algebraischer Ausdrücke — I. Kapitel (§§ 1–15; :cite:`B. G. Teubner, 1895, S. 4–10 <klein:1895>`)

§§ 1–4. Aufbau der zu konstruierenden Größe $x$
-----------------------------------------------

**1.** Es sei $x$ eine algebraische Größe, welche sich aus gegebenen Strecken mit Zirkel und Lineal konstruieren lässt. Nach unserem Hauptsatze (:ref:`Einleitung <fp-intro-de>`) entsteht $x$ aus den gegebenen Größen—die wir nach Wahl einer Längeneinheit als rationale Zahlen bzw. als Elemente eines vorgegebenen :term:`Rationalitätsbereiches <domain-of-rationality>` ansehen—durch endlich viele rationale Rechnungsoperationen und Quadratwurzelausziehungen.

**2.** Um derartige Quadratwurzelausdrücke übersichtlich zu gliedern, teilen wir ihnen je nach der Anzahl übereinander geschachtelter Wurzelzeichen eine bestimmte :term:`Ordnung <radical-order>` $\mu$ zu:

* Ein rein rationaler Ausdruck $R$ (ohne jede Quadratwurzel) heiße von der **Ordnung $0$**.
* Ein Ausdruck, der rational aus rationalen Größen und einfachen Quadratwurzeln $\sqrt{R_1}, \sqrt{R_2}, \dots$ (mit rationalen Radikanden $R_i$) zusammengesetzt ist, heiße von der **Ordnung $1$**, wie etwa

  .. math::

     \frac{\alpha + \beta \sqrt{R_1} + \gamma \sqrt{R_2}}{\delta + \varepsilon \sqrt{R_3}}.

* Werden aus Ausdrücken erster Ordnung abermals Quadratwurzeln gezogen, wie in $\sqrt{p + q\sqrt{R_1}}$, und rational verknüpft, so entsteht ein Ausdruck der **Ordnung $2$**.
* Allgemein heißt ein Ausdruck $x$ von der **Ordnung $\mu$**, wenn höchstens $\mu$ Quadratwurzelzeichen übereinander geschachtelt auftreten, sodass jede Quadratwurzel $\mu$-ter Ordnung aus einem Ausdrucke $(\mu - 1)$-ter Ordnung gezogen wird.

**3.** Es mögen nun im gesamten Aufbau von $x$ überhaupt $m$ verschiedene einzelne Quadratwurzeln $Q_1, Q_2, \dots, Q_m$ vorkommen, geordnet nach aufsteigender Ordnung ($1 \le \text{Ord}(Q_j) \le \mu$).

**4.** Wir treffen von vornherein die wesentliche Festsetzung, dass **keine der $m$ Quadratwurzeln $Q_1, \dots, Q_m$ sich rational durch die übrigen (bzw. vorangehenden) Quadratwurzeln und bekannte rationale Größen ausdrücken lässt**. Wäre nämlich irgendein $Q_k$ rational durch die übrigen Quadratwurzeln darstellbar, so würden wir $Q_k$ einfach überall durch diesen rationalen Ausdruck ersetzen und dadurch die Gesamtzahl $m$ der selbständigen Quadratwurzeln um eine Einheit vermindern. Durch schrittweise Ausführung solcher Reduktionen erreichen wir stets, dass sämtliche $m$ beibehaltenen Quadratwurzeln voneinander unabhängig sind.

§§ 5–6. Normalform von $x$
--------------------------

**5.** Greifen wir unter den Quadratwurzeln höchster Ordnung $\mu$ irgendeine bestimmte, $Q_\mu$, heraus! Als Funktion von $Q_\mu$ allein betrachtet ist $x$ ein rationaler Quotient zweier Polynome in $Q_\mu$, deren Koeffizienten nur noch von den übrigen $m - 1$ Quadratwurzeln abhängen. Da $Q_\mu^2$ bereits von höchstens $(\mu - 1)$-ter Ordnung ist, lässt sich jede gerade Potenz von $Q_\mu$ durch niedrigere Wurzeln und jede ungerade Potenz als Produkt von $Q_\mu$ mit niedrigeren Wurzeln schreiben:

.. math::

   x = \frac{a + b Q_\mu}{c + d Q_\mu},

worin $a, b, c, d$ die Wurzel $Q_\mu$ nicht mehr enthalten.

**6.** Erweitern wir diesen Bruch mit dem konjugierten Faktor $c - d Q_\mu$ (wobei $c + d Q_\mu \neq 0$ sein muss, da sonst $Q_\mu = -c/d$ entgegen § 4 rational durch die übrigen Wurzeln ausdrückbar wäre), so verschwindet $Q_\mu$ aus dem Nenner:

.. math::

   x = \frac{(a + b Q_\mu)(c - d Q_\mu)}{c^2 - d^2 Q_\mu^2} = \alpha + \beta Q_\mu,

wo $\alpha$ und $\beta$ höchstens die übrigen $m - 1$ Quadratwurzeln enthalten. Indem wir genau dasselbe Fortschaffen der Wurzeln aus den Nennern der Reihe nach auf $Q_{m-1}, Q_{m-2}, \dots, Q_1$ anwenden, bringen wir $x$ auf seine **Normalform**: eine ganze lineare Verbindung von Produkten der $m$ unabhängigen Quadratwurzeln $Q_1, \dots, Q_m$ mit rationalen Koeffizienten:

.. math::

   x = A_0 + \sum_{i} A_i Q_i + \sum_{i < j} A_{ij} Q_i Q_j + \dots + A_{12\dots m} Q_1 Q_2 \cdots Q_m.

§§ 7–8. Die konjugierten Größen
-------------------------------

**7.** Jede Quadratwurzel $Q_k = \sqrt{E_k}$ ist ihrem Wesen nach zweideutig ($\pm Q_k$). Erteilen wir in der Normalform von $x$ jeder der $m$ unabhängigen Quadratwurzeln $Q_1, Q_2, \dots, Q_m$ unabhängig voneinander sowohl das positive als auch das negative Vorzeichen (wobei sich bei Vorzeichenwechsel einer inneren Wurzel die äußeren Radikanden entsprechend mitändern), so entspringen im ganzen $2^m$ Werte

.. math::

   x_1, \; x_2, \; \dots, \; x_{2^m},

welche wir die **$2^m$** :term:`konjugierten Werte <conjugate-values>` (*konjugierten Größen*) von $x$ nennen.

**8.** So gehören beispielsweise zu $\sqrt{p + q\sqrt{R}}$ die vier konjugierten Größen

.. math::

   +\sqrt{p + q\sqrt{R}}, \quad -\sqrt{p + q\sqrt{R}}, \quad +\sqrt{p - q\sqrt{R}}, \quad -\sqrt{p - q\sqrt{R}}.

Dabei brauchen die $2^m$ formal gebildeten Ausdrücke $x_1, \dots, x_{2^m}$ ihren Zahlenwerten nach nicht sämtlich voneinander verschieden zu sein (in $\sqrt{p + q\sqrt{R}} + \sqrt{p - q\sqrt{R}}$ vertauscht der Zeichenwechsel von $\sqrt{R}$ nur beide Summanden, sodass derselbe Wert doppelt auftritt).

§ 9. Die zugehörige Gleichung $F(x) = 0$
----------------------------------------

**9.** Wir bilden nunmehr das Produkt vom Grade $2^m$ über sämtliche $2^m$ konjugierten Größen:

.. math::

   F(x) = (x - x_1)(x - x_2)\cdots(x - x_{2^m}) = 0.

Kehrt man das Vorzeichen einer Wurzel höchster Ordnung $Q_m$ um, so vertauschen sich die Linearfaktoren $(x - x_i)$ lediglich paarweise untereinander; das Produkt $F(x)$ bleibt ungeändert, enthält also nur gerade Potenzen $Q_m^{2k}$ und ist somit von $Q_m$ frei. Wiederholt man diesen Schluss schrittweise für sämtliche Wurzeln $\mu$-ter, sodann $(\mu - 1)$-ter Ordnung usf. bis herab zur ersten Ordnung, so fallen alle Quadratwurzeln heraus:

* **$F(x) = 0$ ist eine algebraische Gleichung vom Grade $2^m$ mit rein rationalen Koeffizienten**, welcher $x = x_1$ samt allen seinen konjugierten Werten genügt.

§ 10. Andere rationale Gleichungen $f(x) = 0$
---------------------------------------------

**10.** Genügt unsere Größe $x_1$ irgendeiner *anderen* Gleichung mit rationalen Koeffizienten,

.. math::

   f(x) = x^n + a_1 x^{n-1} + \dots + a_{n-1} x + a_n = 0,

so gilt der wichtige Satz: **Jede rationale Gleichung $f(x) = 0$, welche durch einen der Werte $x_1$ befriedigt wird, wird notwendig auch durch sämtliche konjugierten Werte $x_1, x_2, \dots, x_{2^m}$ befriedigt.**

*Beweis.* Setzen wir $x_1 = \alpha + \beta Q_\mu$ in $f(x)$ ein und ersetzen $Q_\mu^2$ durch seinen Radikanden niedrigerer Ordnung, so nimmt $f(x_1) = 0$ die Gestalt an:

.. math::

   f(x_1) = A + B Q_\mu = 0,

worin $A$ und $B$ die Wurzel $Q_\mu$ nicht enthalten. Hier muss notwendig $B = 0$ sein; denn wäre $B \neq 0$, so folgte $Q_\mu = -A/B$, d. h. $Q_\mu$ ließe sich rational durch die übrigen $m - 1$ Quadratwurzeln ausdrücken, entgegen der Voraussetzung in § 4! Aus $B = 0$ folgt sogleich auch $A = 0$, mithin

.. math::

   f(\alpha - \beta Q_\mu) = A - B Q_\mu = 0.

Der Zeichenwechsel von $Q_\mu$ liefert also wieder eine Wurzel von $f(x) = 0$; und indem man dieselbe Schlussweise auf die Gleichungen $A = 0, B = 0$ bezüglich $Q_{m-1}, \dots, Q_1$ anwendet, folgt $f(x_k) = 0$ für sämtliche $2^m$ konjugierten Größen.

§§ 11–12. Die irreduzible Gleichung $\varphi(x) = 0$
----------------------------------------------------

**11.** Unter allen rationalen Gleichungen, denen $x_1$ genügt, greifen wir die normierte Gleichung **niedrigsten positiven Grades $M$** heraus:

.. math::

   \varphi(x) = x^M + c_1 x^{M-1} + \dots + c_M = 0.

Diese Gleichung ist im zugrunde gelegten Rationalitätsbereiche notwendig **irreduzibel** (d. h. nicht in rationale Faktoren niedrigeren Grades zerlegbar), da sonst $x_1$ bereits einem der Faktoren genügen müsste.

**12.** Ferner **ist jedes rationale Polynom $\psi(x)$, welches für $x = x_1$ verschwindet, ohne Rest durch $\varphi(x)$ teilbar**, wodurch $\varphi(x)$ zugleich eindeutig bestimmt ist. Denn die euklidische Division liefert $\psi(x) = q(x)\varphi(x) + r(x)$ mit rationalen Polynomen $q, r$ und $\deg r < M$ (falls $r \not\equiv 0$); Einsetzen von $x = x_1$ erzwingt $r(x_1) = 0$, was wegen der Minimalität von $M$ nur für $r(x) \equiv 0$ möglich ist. Insbesondere besitzt $\varphi(x) = 0$ lauter einfache Wurzeln, und diese fallen nach § 10 genau mit den voneinander verschiedenen Werten unter $x_1, \dots, x_{2^m}$ zusammen.

§§ 13–15. Der Grad der Gleichung $\varphi(x) = 0$ eine Potenz von $2$
---------------------------------------------------------------------

**13.** Wenden wir § 12 auf das Polynom $F(x)$ vom Grade $2^m$ aus § 9 an, so ist $F(x)$ durch $\varphi(x)$ teilbar: $F(x) = \varphi(x) \cdot F_1(x)$. Hat der rationale Quotient $F_1(x)$ noch positiven Grad, so verschwindet er für irgendeine der konjugierten Größen $x_k$, folglich nach §§ 10–12 abermals für alle konjugierten Größen und ist wiederum durch $\varphi(x)$ teilbar: $F_1(x) = \varphi(x) \cdot F_2(x)$ usf. So ergibt sich endlich

.. math::

   F(x) = [\varphi(x)]^\nu \qquad (\nu \ge 1).

**14.** Der Vergleich der Grade beider Seiten liefert unmittelbar

.. math::

   2^m = M \cdot \nu.

Da jeder Teiler einer Potenz von $2$ selbst eine Potenz von $2$ sein muss, ist der Grad $M$ der irreduziblen Gleichung $\varphi(x) = 0$ notwendig eine Potenz von $2$:

.. math::

   M = 2^h \qquad (h \ge 0).

.. admonition:: Satz über den Grad konstruierbarer Größen

   **Jede durch Quadratwurzeln darstellbare (mit Zirkel und Lineal konstruierbare) Größe $x$ genügt einer irreduziblen Gleichung $\varphi(x) = 0$, deren Grad $M = 2^h$ eine Potenz von $2$ ist.**

**15.** Durch Umkehrung (Kontraposition) fließt hieraus sofort unser allgemeines **Unmöglichkeitskriterium**:

   *Besitzt eine irreduzible Gleichung $\varphi(x) = 0$ einen Grad, welcher KEINE Potenz von $2$ ist, so ist sie durch endlich viele Quadratwurzeln unlösbar und ihre Wurzeln sind mit Zirkel und Lineal NICHT konstruierbar.*

Man hüte sich indessen vor dem Fehlschlusse, den Satz aus § 14 einfach umzukehren: **Nicht jede irreduzible Gleichung vom Grade $2^h$ ist durch Quadratwurzeln allein lösbar!** Schon eine allgemeine irreduzible biquadratische Gleichung ($M = 4 = 2^2$) erfordert zu ihrer Auflösung eine kubische Resolvente (also Kubikwurzeln) und lässt sich nur dann durch bloße Quadratwurzeln lösen, wenn ihre Galois'sche Gruppe sich auf eine Untergruppe von Zweierpotenzordnung reduziert. Bei den Kreisteilungsgleichungen (:ref:`III. und IV. Kapitel <fp-part1-ch3-cyclotomy-de>`) wird sich allerdings zeigen, dass die Bedingung $M = 2^h$ infolge des Abel'schen Charakters der Gleichungen zugleich hinreichend ist.
