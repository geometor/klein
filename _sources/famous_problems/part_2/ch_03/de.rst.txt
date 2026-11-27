:type: de
:title: II. Teil, Kap. III: Die Transzendenz der Zahl e (1895 Deutsch)
:layout: book
:canonical_id: Ch. III
:order: 3

.. _fp-part_2-ch_03-de:
.. _fp-part2-ch_03-de:
.. _fp-ch_03-de:
.. _fp-part2-ch3-hermite-e-de:

II. Teil, III. Kapitel — Die Transzendenz der Zahl e
====================================================

.. rubric:: II. Abschnitt, III. Kapitel (§§ 1–3; :cite:`B. G. Teubner, 1895, S. 47–53 <klein:1895>`)

§ 1. Praktische und theoretische Konvergenz; Anlage des indirekten Beweises
---------------------------------------------------------------------------

**1.** An die Spitze unserer Untersuchung stellen wir die für alle endlichen Werte von :math:`x` konvergente Reihe

.. math::

   e^x = 1 + \frac{x}{1} + \frac{x^2}{2!} + \dots + \frac{x^s}{s!} + \dots,

wobei der Unterschied zwischen *praktischer* und *theoretischer* Konvergenz hervorzuheben ist: für :math:`x = 1000` wäre eine numerische Berechnung aus der Reihe praktisch unausführbar, und doch wächst vom :math:`1000`-sten Gliede an die Fakultät :math:`s!` im Nenner rascher als :math:`x^s` im Zähler, sodass für jedes endliche :math:`x` gilt:

.. math::

   \lim_{s \to \infty} \frac{x^s}{s!} = 0.

**Behauptung (:person:`Hermitescher <hermite>` Satz, :cite:`1873 <hermite:1873>`):** :math:`e` *ist keine algebraische Zahl; eine Gleichung mit teilerfremden ganzzahligen Koeffizienten* (:math:`C_0 \neq 0`)

.. math::

   F(e) = C_0 + C_1 e + C_2 e^2 + \dots + C_n e^n = 0

*ist unmöglich.*

Zum indirekten Beweise multiplizieren wir :math:`F(e) = 0` mit einer geeigneten ganzen Zahl :math:`M`, sodass sich jedes Produkt :math:`M e^\kappa = M_\kappa + \varepsilon_\kappa` in eine ganze Zahl :math:`M_\kappa` und einen kleinen Rest :math:`\varepsilon_\kappa` spaltet:

.. math::

   M F(e) = \bigl(M C_0 + M_1 C_1 + \dots + M_n C_n\bigr) + \bigl(C_1 \varepsilon_1 + \dots + C_n \varepsilon_n\bigr) = 0,

wobei der ganzzahlige Bestandteil :math:`G = M C_0 + \dots + M_n C_n` bei Division durch eine Primzahl :math:`p` einen **von Null verschiedenen Rest** lässt (also :math:`G \neq 0`), während :math:`\sum C_\kappa \varepsilon_\kappa` ein **beliebig kleiner echter Bruch** wird—ein offenbarer Widerspruch!

§ 2. Das Symbol :math:`h^r = r!` und Gordans Hilfspolynom :math:`\varphi(x)`
----------------------------------------------------------------------------

**2.** Nach :person:`Gordan <gordan>` (:cite:`1893 <gordan:1893>`) verstehen wir unter dem Symbol :math:`h^r` kurz die Fakultät :math:`r!`: für ein ausgerechnetes Polynom :math:`\varphi(x) = \sum c_r x^r` bedeutet :math:`\varphi(h) = \sum c_r h^r = \sum c_r\,r!`, während bei einem nicht entwickelten Ausdruck wie :math:`\varphi(\kappa + h)` **zuerst formal nach Potenzen von** :math:`h` **zu ordnen** und erst danach :math:`h^r = r!` einzutragen ist.

Wir wenden dies auf das merkwürdige Polynom an:

.. math::

   \varphi(x) = \frac{x^{p-1}\bigl[(1 - x)(2 - x)\cdots(n - x)\bigr]^p}{(p - 1)!},

worin :math:`n` den Grad von :math:`F(e) = 0` und :math:`p` eine Primzahl mit :math:`p > n` und :math:`p > |C_0|` bezeichnet, die wir später über alle Grenzen wachsen lassen. Geometrisch schmiegt sich die Kurve :math:`y = \varphi(x)` in :math:`x = 1, 2, \dots, n` die Achse durchsetzend eng an die :math:`x`-Achse an, in :math:`x = 0` dagegen ohne Durchsetzung. Wir stellen drei Haupteigenschaften von :math:`\varphi` fest:

a) **Verschwinden für** :math:`p \to \infty`: Bei festem endlichem :math:`x` und wachsendem :math:`p` verschwindet wegen der Fakultät :math:`(p - 1)!` im Nenner nicht nur :math:`\varphi(x) = \sum c_r x^r`, sondern—wenn man im unentwickelten Ausdruck überall :math:`(-x)` durch :math:`+|x|` ersetzt—auch die Summe der absoluten Beträge :math:`\sum_{r=p-1}^{np+p-1} |c_r|\,|x|^r \to 0`.
b) :math:`\varphi(h)` **ist eine ganze, nicht durch** :math:`p` **teilbare Zahl**: In :math:`\varphi(h) = \sum_{r=p-1}^{np+p-1} c_r h^r` hebt sich für :math:`h^r = r!` der Nenner :math:`(p - 1)!` überall fort; alle Glieder ab :math:`r = p` enthalten den Faktor :math:`p`, bis auf das erste Glied (:math:`r = p - 1`):

   .. math::

      \frac{(1\cdot 2 \cdots n)^p\,(p - 1)!}{(p - 1)!} = (n!)^p \not\equiv 0 \pmod p \qquad (\text{da } p > n).

   Also gilt :math:`\varphi(h) \equiv (n!)^p \not\equiv 0 \pmod p`, mithin :math:`\varphi(h) \neq 0`.
c) **Für** :math:`\kappa = 1, 2, \dots, n` **ist** :math:`\varphi(h + \kappa)` **eine ganze, durch** :math:`p` **teilbare Zahl**: In

   .. math::

      \varphi(h + \kappa) = \frac{(\kappa + h)^{p-1}\bigl[(1 - \kappa - h)\cdots(-h)\cdots(n - \kappa - h)\bigr]^p}{(p - 1)!} = \sum_{r=p}^{np+p-1} c'_r h^r

   wird der :math:`\kappa`-te Klammerfaktor gleich :math:`(-h)`, sodass die niedrigste Potenz :math:`h^p` lautet. Nach Einsetzen von :math:`h^r = r!` (:math:`r \ge p`) behalten **sämtliche Glieder** (beginnend mit :math:`(-1)^{\kappa p} \kappa^{p-1}[(\kappa-1)!(n-\kappa)!]^p \cdot p`) den Primfaktor :math:`p`!

§ 3. Spaltung von :math:`e^\kappa \varphi(h)` und Vollendung des Beweises
-------------------------------------------------------------------------

**3.** Wir wählen :math:`M = \varphi(h)` und spalten in :math:`e^\kappa \varphi(h) = \sum_r c_r (e^\kappa h^r)` jedes einzelne Glied :math:`e^\kappa h^r` vermöge :math:`h^r = r!`:

.. math::

   \begin{aligned}
   e^\kappa \cdot h^r &= h^r + \frac{r}{1} h^{r-1}\kappa + \frac{r(r-1)}{1\cdot 2} h^{r-2}\kappa^2 + \dots + \kappa^r + \kappa^r\left[\frac{\kappa}{r + 1} + \frac{\kappa^2}{(r + 1)(r + 2)} + \dots\right] \\
   &= (h + \kappa)^r + q_{r,\kappa}\,\kappa^r e^\kappa,
   \end{aligned}

worin :math:`0 < q_{r,\kappa} < 1` ein echter positiver Bruch ist (da jedes Reihenglied in der eckigen Klammer kleiner als das entsprechende Glied von :math:`1 + \frac{\kappa}{1!} + \frac{\kappa^2}{2!} + \dots = e^\kappa` ist). Summation über :math:`r` liefert die Spaltung

.. math::

   e^\kappa \varphi(h) = \varphi(h + \kappa) + \varepsilon_\kappa, \qquad \varepsilon_\kappa = e^\kappa \sum_r q_{r,\kappa} c_r \kappa^r.

Setzen wir dies in :math:`\varphi(h) F(e) = 0` ein, so erhalten wir

.. math::

   \underbrace{C_0 \varphi(h) + C_1 \varphi(h + 1) + \dots + C_n \varphi(h + n)}_{=\;G \;\equiv\; C_0 \varphi(h) \;\not\equiv\; 0 \pmod p} + \sum_{\kappa=1}^n C_\kappa \varepsilon_\kappa = 0.

Nach 2b und 2c sowie :math:`0 < |C_0| < p` ist :math:`G` eine **von Null verschiedene ganze Zahl**, während nach 2a für hinreichend grosses :math:`p` der Restbruch :math:`\left|\sum_{\kappa=1}^n C_\kappa \varepsilon_\kappa\right| < 1` wird. Damit ist die Unmöglichkeit von :math:`F(e) = 0`—der **Hermitesche Satz**—bewiesen.
