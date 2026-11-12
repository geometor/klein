:title: Vorwort & Einleitung (1895 Deutsch)
:layout: book

.. _fp-intro-de:

Vorträge über ausgewählte Fragen der Elementargeometrie — Vorwort & Einleitung
==============================================================================

.. rubric:: Ausgearbeitet von :person:`F. Tägert <taegert>`, Oberlehrer am Realprogymnasium zu Ems — Eine Festschrift zu der Pfingsten 1895 in Göttingen stattfindenden dritten Versammlung des Vereins zur Förderung des mathematischen und naturwissenschaftlichen Unterrichts (:cite:`Leipzig: B. G. Teubner, 1895, S. iii–v, 1–3 <klein:1895>`)

Vorwort (Ostern 1895)
---------------------

Zu Ostern 1895 fand in Göttingen der übliche Ferienkursus für Lehrer der Mathematik und Physik an höheren Schulen statt. Ich habe in den Vorträgen, welche ich bei dieser Gelegenheit hielt, ausgewählte Fragen der Elementargeometrie behandelt, insbesondere in der Absicht, darzulegen, wie sich die moderne Mathematik zu der Frage nach der Möglichkeit geometrischer Konstruktionen mittels Zirkels und Lineals stellt.

:person:`Herr Oberlehrer Tägert <taegert>` aus Ems, welcher an dem Kursus teilnahm, hat seine Aufzeichnungen unmittelbar danach sorgfältig ausgearbeitet und so das vorliegende kleine Heft hergestellt, welches nunmehr als Festschrift für die zu Pfingsten 1895 in Göttingen zusammentretende dritte Hauptversammlung des *Vereins zur Förderung des mathematischen und naturwissenschaftlichen Unterrichts* veröffentlicht wird (:cite:`Teubner 1895 <klein:1895>`).

Möge die anspruchslose Schrift auch in weiteren Kreisen dazu beitragen, die mathematische Forschung der Universität mit dem Unterricht der höheren Schulen in lebendigere Fühlung zu setzen!

Göttingen, Ostern 1895. — :person:`F. KLEIN <klein>`.

Einleitung
----------

1. Praktische und theoretische Konstruktionen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wenn man über geometrische Konstruktionen handelt, so ist es vor allen Dingen notwendig, zwischen **praktischer** und **theoretischer** Ausführung scharf zu unterscheiden.

Handelt es sich lediglich um die *praktische* Zeichnung oder Messung—wie etwa in der Geodäsie, der darstellenden Geometrie oder der Mechanik—, so bedient man sich unbedenklich eines eingeteilten Maßstabes, eines Transporteurs, geeigneter Kurvenlineale oder numerischer Tafeln und erreicht damit jeden Genauigkeitsgrad, den die physische Beschaffenheit unserer Sinne und Zeicheninstrumente überhaupt zulässt. Von diesem empirischen Standpunkte aus bietet weder die Dreiteilung eines vorgelegten Winkels noch die angenäherte Aufzeichnung der Zahl $\pi = 3{,}14159\dots$ die geringste Schwierigkeit; denn jede wirkliche Zeichnung bleibt ohnehin mit einem kleinen Beobachtungs- und Ausführungsfehler behaftet.

Ganz anders steht es um die Frage der **theoretischen Konstruierbarkeit**. Hier fragen wir im Sinne strenger mathematischer Logik: *Lässt sich eine gesuchte Größe unter ausschließlicher, endlich oft wiederholter Anwendung ganz bestimmter, ideell vollkommen genau gedachter Elementaroperationen exakt herstellen?* In der klassischen Elementargeometrie seit :person:`Euklid <euclid>` (:cite:`*Elemente*, Buch I, Postulate 1–3 <euclid:elements>`) bestehen diese zugelassenen Elementaroperationen ausschließlich in dem Ziehen gerader Linien durch gegebene Punkte (**dem Lineal**) und dem Beschreiben von Kreisen aus gegebenem Mittelpunkt mit gegebenem Radius (**dem Zirkel**).

Nun gehören zu den berühmtesten Aufgaben, welche uns das Altertum überliefert hat, die **Würfelverdoppelung** (:term:`das Delische Problem <delian-problem>`), die **Dreiteilung des beliebigen Winkels**, die **Konstruktion des regulären Siebenecks** ($n = 7$) und die **Quadratur des Kreises** ($\pi$). Im Schulunterricht wird zwar regelmäßig mitgeteilt, dass diese Probleme mit Zirkel und Lineal *unmöglich* zu lösen seien; allein einen wirklichen Beweis dieser Unmöglichkeit sucht man in den gangbaren Lehrbüchern vergebens. Fast die einzige rühmliche Ausnahme bildet der dänische Mathematiker :person:`Julius Petersen <petersen>` in seinen trefflichen Lehrbüchern (:cite:`*Methoden und Theorien zur Auflösung geometrischer Konstruktionsaufgaben* und *Theorie der algebraischen Gleichungen*, 1878–1879 <petersen:1879>`).

Und doch hat die Wissenschaft des neunzehnten Jahrhunderts—durch :person:`Gauß <gauss>` (:cite:`1801 <gauss:1801>`), :person:`Wantzel <wantzel>` (:cite:`1837 <wantzel:1837>`), :person:`Abel <abel>` und :person:`Galois <galois>` auf algebraischem Gebiete, sowie durch :person:`Hermite <hermite>` (:cite:`1873 <hermite:1873>`), :person:`Lindemann <lindemann>` (:cite:`1882 <lindemann:1882>`), :person:`Weierstraß <weierstrass>` und neuerdings im Frühjahr 1893 durch :person:`Hilbert <hilbert>`, :person:`Hurwitz <hurwitz>` und :person:`Gordan <gordan>` (:cite:`1893 <gordan:1893>`) hinsichtlich der :term:`transzendenten Zahlen <transcendental-number>`—alle diese alten Fragen nicht nur endgültig entschieden, sondern ihre Beweise auf eine so durchsichtige und elementare Gestalt gebracht, dass sie jedem Mathematiker unmittelbar zugänglich sind.

2. Problemstellung in algebraischer Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wie ist es überhaupt möglich zu beweisen, dass eine vorgelegte geometrische Aufgabe durch *keinerlei* endliche Kombination von Geraden und Kreisen gelöst werden kann? Auf rein synthetisch-geometrischem Wege lässt sich die Gesamtheit aller erdenklichen Konstruktionsversuche kaum überblicken; wohl aber gelingt dies sofort durch Übersetzung in die Sprache der **analytischen Geometrie und Algebra**.

Seien irgendwelche Ausgangsstrecken $a, b, c, \dots$ gegeben. Legen wir eine Einheitsstrecke und ein rechtwinkliges Koordinatensystem zugrunde, so drücken sich die Koordinaten der gegebenen Punkte rational durch $a, b, c, \dots$ aus:

* Das Ziehen einer **Geraden** durch zwei bekannte Punkte liefert eine lineare Gleichung $Ax + By + C = 0$ mit rational bekannten Koeffizienten; der Schnittpunkt zweier Geraden erfordert die Auflösung zweier linearer Gleichungen, führt also niemals über die vier **rationalen Grundoperationen** (Addition, Subtraktion, Multiplikation, Division) hinaus.
* Das Schlagen eines **Kreises** um einen bekannten Punkt mit bekanntem Radius liefert eine quadratische Gleichung $(x - x_0)^2 + (y - y_0)^2 = r^2$; der Schnitt einer Geraden mit einem Kreise—ebenso der Schnitt zweier Kreise nach Abzug beider Gleichungen zur linearen Potenzlinie—erfordert die Auflösung einer quadratischen Gleichung, fügt also höchstens das **Ausziehen einer Quadratwurzel** hinzu.

Da umgekehrt jede rationale Verbindung ($a \pm b$, $\frac{ab}{c}$ mittels Parallelen) sowie jede Quadratwurzel ($\sqrt{ab}$ als mittlere Proportionale im Halbkreise) wirklich mit Zirkel und Lineal konstruiert werden kann, gewinnen wir bei endlicher Wiederholung den grundlegenden **Hauptsatz**:

.. admonition:: Hauptsatz der Konstruierbarkeit mit Zirkel und Lineal

   **Eine analytische Größe ist dann und nur dann mit Zirkel und Lineal konstruierbar, wenn sie aus den bekannten Größen durch eine endliche Anzahl rationaler Operationen und Quadratwurzelausziehungen abgeleitet werden kann.**

Um also die Unmöglichkeit einer Konstruktion mit Zirkel und Lineal streng nachzuweisen, haben wir das Problem algebraisch zu formulieren und zu zeigen, dass sich die gesuchte Größe $x$ *nicht* durch endlich viele Quadratwurzeln darstellen lässt—sei es, weil $x$ einer algebraischen Gleichung genügt, die nicht durch Quadratwurzeln lösbar ist (**Erster Abschnitt**: Würfelverdoppelung, Winkeldreiteilung, allgemeine Kreisteilung im Gegensatz zum regulären Siebzehneck), sei es, weil die betreffende Zahl ($e$ bzw. $\pi$) überhaupt *keiner* algebraischen Gleichung mit ganzzahligen Koeffizienten genügt (**Zweiter Abschnitt**: Transzendenzbeweise und mechanische Integration mittels des :term:`Integraphen <integraph>`).
