:title: Part I, Ch. IV: Regular 17-Gon — Critical & Symbolic Notes
:layout: book

.. _fp-part1-ch4-heptadecagon-notes:

Part I, Chapter IV — Critical & Symbolic Notes
==============================================

.. rubric:: Textual Collation (1895 vs. 1897), Exact Single-Circle Model in ``geometor.klein.heptadecagon``, and Sister Corpora

Textual Variants & Errata Between the 1895 Teubner and 1897 Ginn Witnesses
--------------------------------------------------------------------------

Collating the 1895 German *Editio Princeps* (:cite:`S. 19–32 <klein:1895>`) against :person:`Beman <beman>` and :person:`Smith's <smith>` 1897 English translation (:cite:`pp. 24–41 <klein:1897>`) reveals three noteworthy editorial refinements:

1. **Notation Renaming ($x, y, z$ vs. $\eta, \eta', \eta''$):** In 1895 DE (S. 21–26), Klein and :person:`Tägert <taegert>` use Gauss's primed period notation $\eta_0, \eta_1$ ($8$-periods), $\eta'_0, \eta'_1, (\eta'_0), (\eta'_1)$ ($4$-periods), and $\eta''_0, \eta''_1$ / $C_1, \dots, C_8$ ($2$-periods). In 1897 EN (pp. 26–32), Beman and Smith introduce the cleaner unprimed alphabet $x_1, x_2$, $y_1, y_2, y_3, y_4$ (with $y_4 = (\eta'_0) > 0 > y_3 = (\eta'_1)$), and $z_1, \dots, z_8$, naming the four quadratics $(\xi), (\eta), (\eta'), (\zeta)$. Both systems are preserved side-by-side in our synchronized tracks and in :mod:`geometor.klein.heptadecagon`.
2. **Correction of the S. 29 Sign Misprint in 1895 DE:** On S. 24 of the 1895 Teubner edition, the first quadratic equation is derived correctly as $\eta^2 + \eta - 4 = 0$ (since $\eta_0 + \eta_1 = -1$ and $\eta_0 \eta_1 = -4$), and S. 29 rightly connects $+4$ below with $-4$ above ($q/p = -4/(-1) = +4$, $4/p = -4$); however, the summary display at the top of S. 29 printed ``\eta^2 - \eta + 4 = 0`` by typographical slip. The 1897 English edition (p. 36) silently restores the exact equation $(\xi): x^2 + x - 4 = 0$, which we likewise restore in the German track with this apparatus note.
3. **L. Gérard's 1896 Mascheroni Construction (§ 8 Footnote):** In October 1895 (DE S. 27 fn.), Klein remarked: *„Eine Construction des 17-Ecks nach Mascheroni nur mit dem Zirkel ist noch nicht versucht, obgleich sie jedenfalls möglich ist.“* Prompted directly by Klein's Göttingen Festschrift, Louis Gérard published the first pure-compass construction of the regular $17$-gon within months (*Mathematische Annalen*, Vol. XLVIII, 1896, pp. 390–392), and Beman & Smith updated the 1897 English footnote (p. 34 fn.) accordingly!

Exact Symbolic Realization in ``geometor.klein.heptadecagon``
-------------------------------------------------------------

The function :func:`geometor.klein.heptadecagon.construct_gauss_17gon_periods` executes Klein's §§ 8–9 inside :class:`geometor.model.Model` (``auto_intersect=False``) backed by a dedicated exact polynomial-quotient arithmetic engine ``_K16Engine`` over $\mathbb{Q}[t]/(M_8(t))$ ($M_8(t) = t^8 - 68t^6 + 1088t^4 - 5440t^2 + 4352$, minimal polynomial of $R_1 = \sqrt{17 + 3\sqrt{17} - \sqrt{34 - 2\sqrt{17}} - 2\sqrt{34 + 2\sqrt{17}}}$):

* **Strict Poncelet–Steiner Purity (`len(model.circles) == 1`):** Only the single fixed circle $C_0: x^2 + y(y - 2) = 0$ is ever constructed in `model`. Even the final vertical chords through $K_m = (\cos\frac{2m\pi}{17}, 1)$ (which Klein § 9 describes simply as "erecting a perpendicular") are constructed **by pure straightedge alone** using Steiner's parallel-tangent harmonic bundle on $C_0$, inscribing all **17 exact vertices** ``V0``..``V16`` with **zero** ``float`` or ``sp.Float`` coordinates!
* **Sister-Corpus Links (`geometor/pappus`, `geometor/petersen`, `geometor/lemoine`):** Klein's projective inversion $x' = \frac{4}{x}$ and harmonic center $\left(0, \frac{2}{5}\right)$ directly exemplify the cross-ratio and involution machinery of `geometor/pappus` (:cite:`Pappus, Book VII <pappus:collection>`), while the structural comparison of straightedge-only, compass-only (:cite:`Mascheroni, 1797 <mascheroni:1797>`), single-circle (:cite:`Steiner, 1833 <steiner:1833>`), and standard Euclidean constructions bridges directly to :person:`Julius Petersen's <petersen>` *Methods and Theories* (:cite:`1879 <petersen:1879>`) and :person:`Émile Lemoine's <lemoine>` *Géométrographie* (:cite:`1902 <lemoine:1902>`).
