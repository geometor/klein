:title: Notes I–VII: Cayley–Klein Metrics & Resolvent Symmetries — Symbolic Notes
:layout: book

.. _ep-notes-i-vii-notes:

Notes I–VII: Non-Euclidean Metrics & Resolvent Symmetries — Critical & Symbolic Notes
=====================================================================================

.. rubric:: Exact Symbolic Cayley–Klein Additivity (``geometor.klein.erlangen``) and Sister-Corpus Concordance

Cayley–Klein Projective Metric Additivity (Note V & Note VI)
------------------------------------------------------------

.. figure:: /_static/figures/fig_cayley_klein_metric.svg
   :alt: Cayley-Klein Projective Metric Inside the Absolute Conic
   :align: center

   **Klein's Projective Model of Non-Euclidean Metric Geometry (Note V, 1871–1872).** Inside a real non-degenerate Absolute conic $\Omega = 0$ (hyperbolic geometry of :person:`Lobachevsky <lobatchewsky>` and :person:`Bolyai <bolyai>`), straight chords act as geodesics and every chord cuts $\Omega$ in two ideal boundary points $I_1, I_2$. Projective distance is proportional to the logarithm of the $4$-point cross-ratio $d(A, B) = c \log(A, B; I_1, I_2)$.

In :func:`geometor.klein.erlangen.verify_cayley_klein_additivity`, we verify exact projective metric additivity in SymPy over $\mathbb{Q}$ on the diameter $(-1, 0)$ to $(1, 0)$ of the real unit-circle Absolute $x^2 + y^2 - 1 = 0$:

* Taking collinear interior points $A\!\left(-\frac{1}{2}, 0\right)$, $B\!\left(\frac{1}{5}, 0\right)$, $C\!\left(\frac{2}{3}, 0\right)$ between ideal points $I_1(-1, 0)$ and $I_2(1, 0)$ inside ``geometor.model.Model``:

  .. math::

     (A, B; I_1, I_2) \;=\; \frac{9}{2}, \qquad
     (B, C; I_1, I_2) \;=\; \frac{7}{2}, \qquad
     (A, C; I_1, I_2) \;=\; \frac{63}{4} \;=\; \frac{9}{2} \cdot \frac{7}{2}.

* Because the cross-ratio telescopes multiplicatively along every chord ($(A, B; I_1, I_2) \cdot (B, C; I_1, I_2) - (A, C; I_1, I_2) = 0$ identically), Klein's logarithmic metric satisfies exact additivity:

  .. math::

     d(A, B) + d(B, C) \;=\; c \ln\!\left(\tfrac{9}{2}\right) + c \ln\!\left(\tfrac{7}{2}\right) \;=\; c \ln\!\left(\tfrac{63}{4}\right) \;=\; d(A, C).

Note V's Direct Prophecy of Hilbert's *Grundlagen* (1899)
---------------------------------------------------------

Look closely at paragraph 3 of **Note V**:

   *“Similar investigations could and should be performed with regard to every axiom (and not alone in geometry); an insight would thus be obtained into the mutual relation of the axioms.”*

Twenty-seven years later, Klein's Göttingen colleague :person:`David Hilbert <hilbert>` carried out this exact program in :cite:`*Grundlagen der Geometrie* (1899) <hilbert:1899>` (`geometor/hilbert`), constructing algebraic coordinate fields to prove the mutual independence of Incidence, Order, Congruence, Continuity/Archimedes, and Parallels! Meanwhile, Klein's 1893 Footnote 41 directly sets the stage for :person:`Bertrand Russell's <russell>` :cite:`1897 *Essay on the Foundations of Geometry* <russell:1897>` (`geometor/bertrand-russell`) and :person:`P. H. J. Hoenen's <hoenen>` :cite:`1954 *De Noetica Geometriae* <hoenen:1954>` (`geometor/hoenen`).

Note VII & Quartic Resolvent Constructibility
---------------------------------------------

Klein's tetrahedral configuration $(x,y,z), (x,-y,-z), (-x,y,-z), (-x,-y,z)$ on the Riemann sphere in **Note VII** gives the geometric heart of ``geometor.klein.constructibility.cubic_resolvent``: the Klein four-group $V_4 = \{1, R_x, R_y, R_z\} \triangleleft S_4$ of $180^\circ$ rotations around the three coordinate axes $OX, OY, OZ$ preserves the four vertices of every tetrahedron in the syzygetic pencil $i H + \lambda j f$, while the quotient group $S_4 / V_4 \cong S_3$ permutes the three coordinate axes (the six octahedral vertices of $T$). Consequently, solving a quartic equation reduces to solving the degree-$3$ resolvent for the three pairs of opposite edge midpoints—which is constructible by straightedge and compasses **if and only if** that cubic resolvent splits over $\mathbb{Q}$ (as verified in :mod:`geometor.klein.constructibility` for $x^4 - 2$ vs. $x^4 - x - 1$)!
