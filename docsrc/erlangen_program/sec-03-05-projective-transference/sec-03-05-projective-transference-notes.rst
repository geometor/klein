:title: §§ 3–5: Projective Geometry, Representation & Space-Elements — Notes
:layout: book

.. _ep-sec-03-05-projective-transference-notes:

§§ 3–5: Projective Geometry & Space-Elements — Critical & Symbolic Notes
========================================================================

.. rubric:: Algebraic Group Isomorphisms, the Klein Quadric in $\mathbb{P}^5$, and 1893 Revisions

Classical Lie-Group Isomorphisms Discovered in §§ 4–5
-----------------------------------------------------

Klein's geometric transference arguments in §§ 4–5 establish several of the celebrated low-dimensional exceptional isomorphisms of classical Lie algebras and algebraic groups without a single matrix computation:

1. **$\operatorname{PGL}_2(\mathbb{C}) \;\cong\; \operatorname{PO}_3(\mathbb{C})$ (§§ 4–5):**
   Via the Veronese conic embedding $[u : v] \mapsto [u^2 : uv : v^2]$, binary projective transformations act as projective orthogonal transformations preserving the conic $x z - y^2 = 0$, identifying binary invariant theory with planar non-Euclidean Cayley–Klein geometry.
2. **$\operatorname{PGL}_4(\mathbb{C}) \rtimes \mathbb{Z}_2 \;\cong\; \operatorname{PO}_6(\mathbb{C})$ (§ 5 — The Plücker–Klein Quadric):**
   Representing a line joining $X = (x_0 : x_1 : x_2 : x_3)$ and $Y = (y_0 : y_1 : y_2 : y_3)$ in $\mathbb{P}^3$ by its six $2 \times 2$ Plücker determinants $p_{ij} = x_i y_j - x_j y_i$ embeds the Grassmannian $\operatorname{Gr}(2, 4)$ as the smooth $4$-dimensional quadric

   .. math::

      \Omega_{\text{Plücker}}(p) \;=\; p_{01} p_{23} + p_{02} p_{31} + p_{03} p_{12} \;=\; 0 \quad \subset \mathbb{P}^5,

   where spatial collineations and dualities correspond to the two connected components of orthogonal transformations preserving $\Omega_{\text{Plücker}} = 0$.

Two Important 1893 Revisions by Klein
-------------------------------------

* **Footnote 14 (1872 *Chasles* $\to$ 1893 *[the French school]*):**
  In the 1872 Erlangen pamphlet (fn. 13), Klein attributed the interpretation of metric properties via the imaginary spherical circle at infinity solely to :person:`Michel Chasles <chasles>`. Recognizing the earlier foundational priority of :person:`Jean-Victor Poncelet <poncelet>` (:cite:`1822 <poncelet:1822>`) and Edmond Laguerre (1853, angle via logarithm of cross-ratio with $I, J$), Klein broadened the 1893 wording to ``[the French school]``.
* **Footnote 23 (1893 Addition on Normal Subgroups and Faithful Orbits):**
  In § 5, Klein defines a *Körper* ("body," modern *homogeneous space* $G / H$) as the orbit of a geometric element under $G$. In 1893, Klein added Footnote 23 pointing out that if the stabilizer $H = \operatorname{Stab}_G(x_0)$ contains a nontrivial *self-conjugate* (normal) subgroup $N \triangleleft G$, then $N$ acts trivially on *every* element $g \cdot x_0$ of the orbit ($N \subset g H g^{-1}$), so the orbit represents only the quotient group $G / N$ rather than $G$ faithfully. For instance, points at infinity fail to represent translations inside the affine or Euclidean group because translations act trivially on the plane at infinity!

Cross-Corpus Links in GEOMETOR
------------------------------

* **Pappus & Projective Cross-Ratio (`geometor/pappus`):** See :cite:`Pappus, *Collection* Book VII <pappus:collection>` for the ancient root of projective invariance and :person:`von Staudt's <staudt>` *Geometrie der Lage* discussed in § 3.
* **Bertrand Russell on Dimension & Space-Elements (`geometor/bertrand-russell`):** In :cite:`*An Essay on the Foundations of Geometry* (1897) <russell:1897>`, :person:`Russell <russell>` directly engages Klein's § 5 thesis that dimensionality is relative to the chosen space-element (*Raumelement*).
