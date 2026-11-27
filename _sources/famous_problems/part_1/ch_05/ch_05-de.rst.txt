:title: I. Teil, Kap. V: Allgemeines über algebraische Konstruktionen (1895 Deutsch)
:layout: book
:canonical_id: Ch. V
:order: 5
:tracks: English: ch_05-en | German: ch_05-de | Summary: ch_05-summary | Notes: ch_05-notes

.. _fp-part_1-ch_05-de:
.. _fp-part1-ch_05-de:
.. _fp-ch_05-de:
.. _fp-part1-ch5-higher-constructions-de:

I. Teil, V. Kapitel — Allgemeines über algebraische Konstruktionen
==================================================================

.. rubric:: I. Abschnitt, V. Kapitel (§§ 1–5; :cite:`B. G. Teubner, 1895, S. 32–37 <klein:1895>`)

§ 1. Konstruktionen durch Papierfalten (Wiener und Sundara Row)
---------------------------------------------------------------

**1.** Indem wir die Konstruktionen mit Zirkel und Lineal nunmehr verlassen, erwähnen wir noch der Merkwürdigkeit halber eine neuerdings vorgeschlagene einfache Konstruktionsart: das **Falten von Papier**. :person:`Hermann Wiener <wiener>` hat angegeben (vgl. W. Dyck, *Katalog der Münchener mathematischen Ausstellung von 1893*, Nachtrag, S. 52), wie man sich durch Papierfalten die Netze der regulären Körper verschaffen kann. Eigentümlicherweise hat zu derselben Zeit ein indischer Mathematiker, :person:`T. Sundara Row <sundara-row>` in Madras, ein kleines Buch über Papierfalten (:cite:`1893 <sundara-row:1893>`) erscheinen lassen, worin gezeigt wird, wie man durch Falten beliebig viele Punkte krummer Linien (z. B. Ellipse, Cissoide) konstruieren kann.

§ 2. Lösung kubischer und biquadratischer Gleichungen mittels Kegelschnitten
----------------------------------------------------------------------------

**2.** Mit welchen Hilfsmitteln ist es möglich—und wie haben es insbesondere die Alten erreicht—, Probleme, die sich algebraisch als kubische Gleichungen oder Gleichungen höheren Grades darstellen, geometrisch zu lösen?

In erster Linie bieten sich hierzu die **Kegelschnitte** dar, mit deren Hilfe die Alten sowohl die :term:`Würfelverdoppelung <delian-problem>` als auch die Dreiteilung des Winkels lösten. In der Sprache der modernen analytischen Geometrie sei etwa die kubische oder biquadratische Gleichung

.. math::

   x^3 + a x^2 + b x + c = 0 \qquad \text{bzw.} \qquad x^4 + a x^3 + b x^2 + c x + d = 0

aufzulösen. Setzt man :math:`x^2 = y`, so hat man die feste **Parabel** :math:`x^2 = y` (mit vertikaler Achse) jeweils mit einer **Hyperbel** zum Schnitt zu bringen:

.. math::

   x y + a y + b x + c = 0 \qquad \text{bzw.} \qquad y^2 + a x y + b y + c x + d = 0.

* Im **kubischen Falle** (Tafel Fig. III) laufen die Asymptoten der Hyperbel den Koordinatenachsen parallel; von den vier Schnittpunkten liegt einer im unendlich fernen Punkte der :math:`y`-Achse, während die **drei im Endlichen liegenden Schnittpunkte** als Abszissen die drei Wurzeln liefern.
* Im **biquadratischen Falle** (Tafel Fig. IV) behält die Hyperbel nur die horizontale Asymptote bei, während die zweite geneigt ist; beide Kurven besitzen nun **vier Schnittpunkte im Endlichen**.

(Zu den Verfahrensweisen der Alten vgl. M. Cantor, *Geschichte der Mathematik*, Leipzig, 1894, 2. Aufl.; H. G. Zeuthen, *Die Kegelschnitte im Altertum*, Kopenhagen, 1886; sowie R. Baltzer, *Analytische Geometrie*, Leipzig, 1882.)

§ 3. Die Cissoide des Diokles und das Delische Problem
------------------------------------------------------

**3.** Ausser den Kegelschnitten benutzten die Alten eigens zu diesem Zwecke ersonnene höhere Kurven, darunter namentlich die :term:`Cissoide <cissoid>` und die :term:`Conchoide <conchoid>`.

Die **Cissoide des** :person:`Diokles <diocles>` (ca. 150 v. Chr., Tafel Fig. V) entsteht an einem Kreise vom Durchmesser :math:`1` mit vertikaler rechter Tangente :math:`x = 1` und gegenüberliegendem Scheitel :math:`O(0, 0)`, indem man auf jedem Strahl durch :math:`O` (Winkel :math:`\vartheta` zur :math:`x`-Achse) von :math:`O` aus das zwischen Kreis (:math:`\cos\vartheta`) und Tangente (:math:`\frac{1}{\cos\vartheta}`) gelegene Differenzstück :math:`r` abträgt:

.. math::

   r = \frac{1}{\cos\vartheta} - \cos\vartheta = \frac{\sin^2\vartheta}{\cos\vartheta}, \qquad \text{oder rechtwinklig:} \qquad (x^2 + y^2)x - y^2 = 0.

Die Kurve ist von **dritter Ordnung**, symmetrisch zur :math:`x`-Achse, besitzt im Ursprung :math:`O` eine **Spitze**, hat :math:`x = 1` zur Asymptote und schneidet die unendlich ferne Gerade in den beiden **imaginären Kreispunkten**.

.. picture:: /_static/figures/fig_conchoid_cissoid.svg
   :alt: Die Cissoide des Diokles zur Würfelverdoppelung und die Conchoide des Nikomedes zur Winkeldreiteilung
   :caption: Höhere algebraische Kurven des Altertums (Klein Kap. V, §§ 3–4, Tafel Fig. V–IX): Links — Cissoide des Diokles zur Konstruktion von 2^(1/3); Rechts — Conchoide des Nikomedes zur Dreiteilung des Winkels MOY.

Schreiben wir ihre Gleichung in der Gestalt

.. math::

   \left(\frac{y}{x}\right)^3 = \frac{y}{1 - x},

so schneidet die Ursprungsgerade :math:`\frac{y}{x} = \lambda` auf :math:`x = 1` das Stück :math:`\lambda` ab und trifft die Cissoide in einem Punkte, dessen Verbindungsgerade mit :math:`(1, 0)` auf der :math:`y`-Achse genau das Stück :math:`\lambda^3` abschneidet (Tafel Fig. VI). Umgekehrt tragen wir auf der :math:`y`-Achse das Stück :math:`2` ab, verbinden :math:`(0, 2)` mit :math:`(1, 0)` und ziehen vom Ursprung :math:`O` durch den Cissoidenschnittpunkt den Strahl bis zur Tangente :math:`x = 1`: dessen Ordinate auf :math:`x = 1` ist exakt :math:`\sqrt[3]{2}`!

§ 4. Die Conchoide des Nikomedes und die Dreiteilung des Winkels
----------------------------------------------------------------

**4.** Die **Conchoide des** :person:`Nikomedes <nicomedes>` (ca. 150 v. Chr., Tafel Fig. VII–IX) entsteht, indem man von einem festen Punkte :math:`O(0, 0)` im Abstand :math:`a` zur Geraden :math:`x = a` ein Strahlenbüschel legt und auf jedem Strahl vom Schnittpunkt mit :math:`x = a` aus nach beiden Seiten die konstante Strecke :math:`b` abträgt (für :math:`b < a` *gestreckte*, für :math:`b > a` *verschlungene* Conchoide, für :math:`b = a` Spitze in :math:`O`). Aus :math:`r : x = \pm b : (x - a)` folgt ihre Gleichung **vierter Ordnung**:

.. math::

   (x^2 + y^2)(x - a)^2 - b^2 x^2 = 0,

mit Doppelpunkt in :math:`O`, gemeinsamer Asymptote :math:`x = a` beider Zweige und Durchgang durch die **imaginären Kreispunkte** im Unendlichen.

Um den Winkel :math:`\varphi = \angle MOY` in drei gleiche Teile zu teilen, trägt man auf dem schrägen Schenkel :math:`OM = b` beliebig ab, schlägt um :math:`M` den Kreis vom Radius :math:`b` und legt durch :math:`M` die Vertikale als Asymptote der von :math:`O` aus mit der Strecke :math:`b` gezeichneten Conchoide: verbindet man deren Schnittpunkt :math:`A` mit dem Kreise mit :math:`O`, so ist :math:`\angle AOY = \frac{1}{3}\varphi`.

**Abzählung sämtlicher Schnittpunkte:** Da die Winkeldreiteilung ein irreduzibles kubisches Problem mit den drei Wurzeln :math:`\frac{\varphi}{3}, \frac{\varphi + 2\pi}{3}, \frac{\varphi + 4\pi}{3}` vorstellt, muss jede algebraische Konstruktion notwendig **alle drei Lösungen zugleich** liefern:

* Kreis (:math:`2`. Ordnung) und Conchoide (:math:`4`. Ordnung) haben :math:`8` Schnittpunkte gemeinsam.
* Davon fallen **zwei** in den Doppelpunkt :math:`O` und **zwei** in die imaginären Kreispunkte im Unendlichen, sodass **vier** reelle Schnittpunkte im Endlichen verbleiben.
* Von diesen vier scheidet der auf der Verlängerung von :math:`OM` gelegene Punkt :math:`B` (:math:`OMB = 2b`) aus, der von vornherein rational konstruierbar ist—es bleiben in der Tat **genau drei Schnittpunkte**, welche sämtliche drei kubischen Wurzeln liefern!

§ 5. Mechanische Kurvenzeichner in kontinuierlichem Zuge
--------------------------------------------------------

**5.** Zur praktischen Ausführung solcher Konstruktionen bedarf man mechanischer Apparate, **welche die Kurve in einem kontinuierlichen Zuge liefern**, da jede punktweise Konstruktion bloss eine Näherungsmethode darstellt. Schon :person:`Nikomedes <nicomedes>` erfand eine einfache Vorrichtung zum Zeichnen der Conchoide—die älteste derartige neben Lineal und Zirkel (M. Cantor, Bd. I, S. 302; :person:`Pappus <pappus>`, :cite:`*Collectio*, Buch IV <pappus:collection>`). Neuere Instrumente verzeichnet W. Dycks *Katalog* (S. 227–230, 340; Nachtrag S. 42–43).
