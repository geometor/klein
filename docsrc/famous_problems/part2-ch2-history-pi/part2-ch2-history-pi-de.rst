:title: II. Teil, Kap. II: Geschichtlicher Überblick über Berechnung und Konstruktion von π (1895 Deutsch)
:layout: book

.. _fp-part2-ch2-history-pi-de:

II. Teil, II. Kapitel — Geschichtlicher Überblick über die Versuche zur Berechnung und Konstruktion von π
=========================================================================================================

.. rubric:: II. Abschnitt, II. Kapitel (§§ 1–5; :cite:`B. G. Teubner, 1895, S. 43–47 <klein:1895>`)

Einordnung des 4000-jährigen Quadraturproblems
----------------------------------------------

Im IV. Kapitel werden wir beweisen, dass die Zahl $\pi$ zu den :term:`transzendenten Zahlen <transcendental-number>` gehört. Diesen Beweis hat zuerst :person:`Lindemann <lindemann>` im Jahre 1882 (:cite:`*Mathematische Annalen*, Bd. 20 <lindemann:1882>`) erbracht und damit ein Problem endgültig erledigt, das die Mathematiker fast $4000$ Jahre lang beschäftigt hat: **die Quadratur des Kreises**. Denn ist $\pi$ nicht einmal algebraisch, so ist sie erst recht nicht mit Zirkel und Lineal konstruierbar.

Wie diese notwendig vergeblichen Bemühungen dennoch die vielseitigsten Fortschritte der gesamten Mathematik hervorriefen, zeigt unser kurzer geschichtlicher Überblick im Anschluss an die treffliche Schrift von :person:`Ferdinand Rudio <rudio>`, :cite:`*Archimedes, Huygens, Lambert, Legendre. Vier Abhandlungen über die Kreismessung* (Leipzig, 1892) <rudio:1892>`.

§ 1. Das empirische Stadium (Papyrus Rhind und Altertum)
--------------------------------------------------------

**1.** Auf der ältesten, **empirischen Stufe** suchte man das Verhältnis von Kreisumfang und Durchmesser durch Messung oder unmittelbare Schätzung zu gewinnen:

* Das älteste bekannte mathematische Schriftdenkmal, der **Papyrus Rhind** (um 2000 v. Chr., verfasst von **Ahmes**), gibt die Vorschrift: *Man schneide $\frac{1}{9}$ vom Durchmesser ab und errichte über dem Rest ein Quadrat*. Dies liefert den recht guten Näherungswert

  .. math::

     \pi \approx \left(\frac{16}{9}\right)^2 = \frac{256}{81} = 3{,}16049\dots.

* Ungenauer ist der in der Bibel (1. Könige 7, 23; 2. Chronik 4, 2) benutzte Wert $\pi = 3$.

§ 2. Die Griechen: Archimedes, Huygens und die Quadratrix
---------------------------------------------------------

**2.** Über diesen empirischen Standpunkt erhoben sich die Griechen, vor allen :person:`Archimedes <archimedes>`, der in seiner *Kreismessung* (*Κύκλου μέτρησις*) den Kreisinhalt durch ein- und umbeschriebene reguläre Polygone ($96$-Eck: $3\frac{10}{71} < \pi < 3\frac{1}{7}$) einschloss—eine Methode, die bis zur Erfindung der Differentialrechnung herrschte und besonders durch :person:`Christiaan Huygens <huygens>` (*De circuli magnitudine inventa*, 1654) praktisch vervollkommnet wurde.

Daneben suchten die Griechen die Quadratur des Kreises auch mittels **höherer Kurven** zu erzwingen. In moderner Sprache erscheint $\pi$ etwa als spezielle Ordinate der **Integralkurve**

.. math::

   y = \arcsin x = \int_0^x \frac{dx}{\sqrt{1 - x^2}};

jeder mechanische Apparat, der eine solche transzendente Kurve stetig aufzeichnet (*„transzendenter Apparat“*), liefert eine geometrische Konstruktion von $\pi$.

Im Altertum nannte man eine solche Kurve :term:`Quadratrix <quadratrix>` (*τετραγωνίζουσα*). Die bekannteste ist die **Quadratrix des Dinostratus** (um 350 v. Chr.; Tafel Fig. X), welche bereits :person:`Hippias <hippias>` von Elis (um 420 v. Chr.) zur Winkeldreiteilung ersonnen hatte: Auf zwei senkrechten Radien $OA, OB$ des Einheitskreises bewegen sich gleichzeitig und gleichförmig ein Punkt $M$ auf dem Radius $OB$ von $O$ nach $B$ und ein Punkt $L$ auf dem Viertelkreisbogen $AB$ von $A$ nach $B$. Der Schnittpunkt $P(x, y)$ des Strahls $OL$ (Winkel $\vartheta$) mit der Parallelen zu $OA$ durch $M$ beschreibt die Quadratrix. Wegen $\vartheta = \frac{\pi}{2}y$ und $\vartheta = \arctan\frac{y}{x}$ lautet ihre Gleichung

.. math::

   x = \frac{y}{\tan\!\left(\frac{\pi}{2}y\right)}, \qquad \text{und für } y \to 0: \qquad x_0 = \frac{2}{\pi}.

Der Kreisradius $1$ ist demnach die **mittlere Proportionale** zwischen dem Kreisquadranten $\frac{\pi}{2}$ und dem Achsenabschnitt $x_0 = \frac{2}{\pi}$! Solange freilich kein Apparat vorliegt, der die Kurve in kontinuierlichem Zuge beschreibt, bleibt die Quadratrix nur eine geometrische Umformulierung des Rektifikationsproblems.

§§ 3–4. Entstehung der modernen Analysis (Euler) und Irrationalitätsbeweise (Lambert, Legendre)
-----------------------------------------------------------------------------------------------

**3.** In das Jahrhundert **1670–1770** (:person:`Leibniz <leibniz>`, Newton, :person:`Euler <euler>`) fällt die Entstehung der modernen Analysis und Reihenlehre (z. B. die sogenannte Leibniz'sche Reihe $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots$) sowie die Entdeckung des **Zusammenhanges zwischen $e$ und $\pi$**. Die Zahl $e$ und die natürlichen Logarithmen treten im Prinzip bei Napier (1614) auf; ihre Brücke zu den Kreisfunktionen schlug erst :person:`Euler <euler>`, indem er imaginäre Exponenten einführte:

.. math::

   e^{ix} = \cos x + i\sin x, \qquad \text{also für } x = \pi: \qquad e^{i\pi} = -1.

An diese wunderbare Formel knüpfen sämtliche modernen Transzendenzbeweise für $\pi$ an, indem sie zuerst die Eigenschaften der Exponentialfunktion und die Transzendenz von $e$ darlegen.

**4.** Seit **1770** trat die strenge Kritik wieder in ihr Recht: 1770 veröffentlichte :person:`Lambert <lambert>` seine *Vorläufigen Kenntnisse für die, so die Quadratur des Cirkuls suchen* (Irrationalität von $\pi$), und 1794 bewies :person:`Legendre <legendre>` in seinen *Éléments de géométrie* endgültig, dass $\pi$ und $\pi^2$ irrational sind.

§ 5. Die Transzendenzbeweise von Hermite (1873) und Lindemann (1882) bis Gordan (1893)
--------------------------------------------------------------------------------------

**5.** Ein volles Jahrhundert später setzten die modernen Transzendenzbeweise ein:

* **1873:** :person:`Hermite <hermite>`, :cite:`*Sur la fonction exponentielle* (*Comptes rendus*, 1873; als Schrift 1874) <hermite:1873>` — erster Beweis der **Transzendenz von $e$**.
* **1882:** :person:`Lindemann <lindemann>`, :cite:`*Über die Zahl $\pi$* (*Mathematische Annalen*, Bd. 20, 1882) <lindemann:1882>` — Beweis der **Transzendenz von $\pi$** im engen Anschluss an Hermite.
* **1885 / 1892:** Vereinfachung durch :person:`Weierstrass <weierstrass>` (*Berliner Berichte*, 1885) und Lehrbuchdarstellung durch :person:`Bachmann <bachmann>` (*Vorlesungen über die Natur der Irrationalzahlen*, 1892).
* **Frühjahr 1893:** Entscheidende elementare Vereinfachung zuerst durch :person:`Hilbert <hilbert>` (*Göttinger Nachrichten*, noch unter Benutzung des Integrals $\int_0^\infty z^\rho e^{-z}\,dz = \rho!$) und unmittelbar darauf durch :person:`Hurwitz <hurwitz>` und :person:`Gordan <gordan>` (:cite:`*Mathematische Annalen*, Bd. 43, 1893 <gordan:1893>`), welche auch diesen letzten transzendenten Integralbestandteil abstreiften. Wir schliessen uns im folgenden hauptsächlich der Darstellung von **Gordan** an.
