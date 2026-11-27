:title: I. Teil, Kap. II: Delisches Problem & Winkeldreiteilung (1895 Deutsch)
:layout: book
:canonical_id: Ch. II
:order: 2
:tracks: English: ch_02-en | German: ch_02-de | Summary: ch_02-summary | Notes: ch_02-notes

.. _fp-part_1-ch_02-de:
.. _fp-part1-ch_02-de:
.. _fp-ch_02-de:
.. _fp-part1-ch2-delian-trisection-de:

Erster Abschnitt, II. Kapitel — Das Delische Problem und die Dreiteilung des Winkels
====================================================================================

.. rubric:: Erster Abschnitt, II. Kapitel (§§ 1–3; :cite:`B. G. Teubner, 1895, S. 10–12 <klein:1895>`)

§ 1. Die Unmöglichkeit, das Delische Problem mit Zirkel und Lineal zu lösen
---------------------------------------------------------------------------

**1.** Wir machen von dem im ersten Kapitel bewiesenen allgemeinen Satze sogleich die Anwendung auf das altberühmte :term:`Delische Problem <delian-problem>`, d. h. die **Verdoppelung des Würfels**. Der Überlieferung zufolge verlangte das Orakel zu Delos zur Abwendung einer Pest, man solle den würfelförmigen Altar des Apollon unter Beibehaltung der Würfelgestalt auf das Doppelte seines Rauminhalts vergrößern.

Wählen wir die Kante des gegebenen Würfels zur Längeneinheit (:math:`1`), so hat die gesuchte Kante :math:`x` des verdoppelten Würfels der Gleichung dritten Grades zu genügen:

.. math::

   x^3 = 2 \qquad \text{oder} \qquad x^3 - 2 = 0.

Nach Kapitel I, § 15 ist diese Aufgabe mit Zirkel und Lineal unlösbar, sobald feststeht, dass die Gleichung :math:`x^3 - 2 = 0` im Bereiche der rationalen Zahlen **irreduzibel** ist. Ließe sich aber ein kubisches Polynom rational zerlegen, so müsste mindestens ein Faktor linear sein, die Gleichung :math:`x^3 = 2` also eine rationale Wurzel :math:`x = \frac{p}{q}` besitzen, worin :math:`p` und :math:`q` teilerfremde ganze Zahlen bedeuten (:math:`\gcd(p, q) = 1`). Einsetzen liefert

.. math::

   p^3 = 2 q^3.

Hiernach muss :math:`p^3`, also auch :math:`p` selbst, eine gerade Zahl sein: :math:`p = 2 p'`. Trägt man dies ein, so folgt :math:`8 p'^3 = 2 q^3` oder

.. math::

   4 p'^3 = q^3,

woraus ebenso folgt, dass auch :math:`q` gerade sein müsste—im Widerspruch zur vorausgesetzten Teilerfremdheit von :math:`p` und :math:`q`! Mithin ist die Gleichung :math:`x^3 - 2 = 0` irreduzibel; da ihr Grad :math:`3` keine Potenz von :math:`2` ist, **kann das Delische Problem unmöglich mit Zirkel und Lineal gelöst werden**.

§ 2. Die allgemeine Gleichung :math:`x^3 = \lambda`
---------------------------------------------------

**2.** Ehe wir zur Dreiteilung des Winkels übergehen, betrachten wir allgemeiner die Gleichung

.. math::

   x^3 = \lambda,

worin :math:`\lambda` einen **willkürlich veränderlichen Parameter** (reell oder komplex) bezeichnet. Als zugrunde gelegten :term:`Rationalitätsbereich <domain-of-rationality>` (nach Kroneckers Ausdrucksweise) fassen wir hier die Gesamtheit aller rationalen Funktionen :math:`\frac{f(\lambda)}{\psi(\lambda)}` auf, in denen Zähler :math:`f(\lambda)` und Nenner :math:`\psi(\lambda)` ganze rationale Funktionen (Polynome) von :math:`\lambda` sind. Alle Schlüsse des ersten Kapitels übertragen sich wörtlich auf diesen Rationalitätsbereich.

Wäre nun :math:`x^3 - \lambda = 0` in diesem Bereiche reduzibel, so müsste eine Wurzel :math:`x = \frac{f(\lambda)}{\psi(\lambda)}` mit teilerfremden Polynomen :math:`f(\lambda)` und :math:`\psi(\lambda)` unsere Gleichung identisch befriedigen:

.. math::

   [f(\lambda)]^3 = \lambda \, [\psi(\lambda)]^3.

Vergleicht man die Grade in :math:`\lambda` auf beiden Seiten (:math:`3 \deg f = 1 + 3 \deg \psi`), so springt der Widerspruch sofort in die Augen. Unter der Voraussetzung eines frei veränderlichen :math:`\lambda` ist die Gleichung :math:`x^3 - \lambda = 0` daher **irreduzibel**, und da ihr Grad :math:`3` nicht die Form :math:`2^h` besitzt, **lässt sie sich nicht durch Quadratwurzeln auflösen**.

§ 3. Die Unmöglichkeit, einen Winkel mit Zirkel und Lineal zu dritteln
----------------------------------------------------------------------

**3.** Beschränken wir jetzt die Veränderlichkeit von :math:`\lambda`, indem wir in Polarkoordinaten setzen:

.. math::

   \lambda = r(\cos\varphi + i\sin\varphi), \qquad \text{also} \qquad \sqrt[3]{\lambda} = \sqrt[3]{r}\,\sqrt[3]{\cos\varphi + i\sin\varphi}.

Unsere Aufgabe spaltet sich dadurch in zwei getrennte Probleme: die Ausziehung der Kubikwurzel aus einer beliebigen positiven reellen Zahl :math:`r` und die Ausziehung der Kubikwurzel aus einer komplexen Zahl vom Betrage :math:`1` der Gestalt :math:`\cos\varphi + i\sin\varphi`.

**I. Die Vervielfältigung des Würfels** (:math:`x^3 = r`).
Die drei Wurzeln der Gleichung :math:`x^3 = r` lauten

.. math::

   \sqrt[3]{r}, \qquad \varepsilon\sqrt[3]{r}, \qquad \varepsilon^2\sqrt[3]{r},

wenn :math:`\varepsilon` und :math:`\varepsilon^2` die imaginären dritten Einheitswurzeln bezeichnen:

.. math::

   \varepsilon = \frac{-1 + i\sqrt{3}}{2}, \qquad \varepsilon^2 = \frac{-1 - i\sqrt{3}}{2}.

Wählen wir als Rationalitätsbereich die Gesamtheit der rationalen Funktionen von :math:`r`, so ist :math:`x^3 = r` nach § 2 irreduzibel; *das allgemeine Problem der Würfelvervielfältigung lässt daher keine Konstruktion mit Zirkel und Lineal zu*.

**II. Die Dreiteilung des Winkels** (:math:`x^3 = \cos\varphi + i\sin\varphi`).
Die drei Wurzeln der Gleichung :math:`x^3 = \cos\varphi + i\sin\varphi` sind nach der Moivre'schen Formel:

.. math::

   x_1 = \cos\frac{\varphi}{3} + i\sin\frac{\varphi}{3}, \qquad
   x_2 = \cos\frac{\varphi + 2\pi}{3} + i\sin\frac{\varphi + 2\pi}{3}, \qquad
   x_3 = \cos\frac{\varphi + 4\pi}{3} + i\sin\frac{\varphi + 4\pi}{3}.

Geometrisch stellen sich diese drei Wurzeln in der komplexen Zahlenebene als die Ecken eines dem Einheitskreise einbeschriebenen gleichseitigen Dreiecks dar; zur Wurzel :math:`x_1` gehört das Argument :math:`\frac{\varphi}{3}`, sodass :math:`x^3 = \cos\varphi + i\sin\varphi` den genauen analytischen Ausdruck für das Problem der **Winkeldreiteilung** bildet.

Wäre diese Gleichung in dem durch :math:`\cos\varphi` und :math:`\sin\varphi` bestimmten Rationalitätsbereiche reduzibel, so ließe sich mindestens eine ihrer Wurzeln als rationale Funktion von :math:`\cos\varphi` und :math:`\sin\varphi` darstellen; ihr Wert müsste daher **ungeändert bleiben**, wenn man :math:`\varphi` durch :math:`\varphi + 2\pi` ersetzt. Führt man diesen Übergang jedoch durch **stetige Änderung des Winkels** :math:`\varphi` **um** :math:`2\pi` aus, so erkennt man unmittelbar, dass die drei Wurzeln :math:`x_1, x_2, x_3` eine **zyklische Vertauschung** (:math:`x_1 \to x_2 \to x_3 \to x_1`) erleiden! Mithin kann keine einzige Wurzel rational durch :math:`\cos\varphi` und :math:`\sin\varphi` ausgedrückt werden; die Gleichung ist irreduzibel vom Grade :math:`3 \neq 2^h` und durch endlich viele Quadratwurzeln unlösbar:

.. admonition:: Satz über die Dreiteilung des Winkels

   **Die Dreiteilung eines unbestimmten (allgemeinen) Winkels** :math:`\varphi` **ist mit Zirkel und Lineal unmöglich**.

Selbstverständlich gilt dieser Beweis für einen *allgemeinen* Winkel :math:`\varphi`; für einzelne **spezielle** Winkelwerte (wie z. B. :math:`\varphi = \frac{\pi}{2}`) wird die Gleichung reduzibel und die Konstruktion ausführbar, während sie für andere spezielle Winkel (wie :math:`\varphi = \frac{\pi}{3}`, entsprechend der Neunteilung des Kreises) auch numerisch über :math:`\mathbb{Q}` irreduzibel und unlösbar bleibt.
