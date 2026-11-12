:title: §§ 6–7: Reciprocal Radii & Lie's Sphere Geometry — Critical Notes
:layout: book

.. _ep-sec-06-07-inversion-lie-spheres-notes:

§§ 6–7: Reciprocal Radii & Lie's Sphere Geometry — Critical & Symbolic Notes
============================================================================

.. rubric:: Liouville's Rigidity Theorem, Tetracyclic Coordinates, and Exact Inversion Verification

Exact Symbolic Verification of Möbius Inversion (§ 6)
-----------------------------------------------------

In :func:`geometor.klein.erlangen.verify_erlangen_invariants`, we verify Klein's Footnote 24/22 theorem on $4$-point circular cross-ratios directly inside ``geometor.model.Model`` over $\mathbb{Q}$:

* Four rational collinear points $A(1, 1), B(2, 1), C(4, 1), D(7, 1)$ lie on the horizontal line $y = 1$ (which passes through $\infty$ and does *not* pass through the center of inversion $O(0, 0)$).
* Under exact inversion across $x^2 + y^2 = 4$, $(x, y) \mapsto \left(\frac{4x}{x^2 + y^2}, \frac{4y}{x^2 + y^2}\right)$, those four collinear points map to four non-collinear rational points on the circle $x^2 + (y - 2)^2 = 4$ passing through $O(0, 0)$:

  .. math::

     A'(2, 2), \quad B'\!\left(\tfrac{8}{5}, \tfrac{4}{5}\right), \quad C'\!\left(\tfrac{16}{17}, \tfrac{4}{17}\right), \quad D'\!\left(\tfrac{14}{25}, \tfrac{2}{25}\right).

* Whereas collinearity and division ratios break, the $4$-point **quadrance cross-ratio**

  .. math::

     \operatorname{QCR}(A, B; C, D) \;=\; \frac{Q(A, C)\, Q(B, D)}{Q(A, D)\, Q(B, C)} \;=\; \frac{9 \cdot 25}{36 \cdot 4} \;=\; \frac{25}{16} \quad \text{(or } \frac{Q_{AC}Q_{BD}}{Q_{BC}Q_{AD}} = \frac{16}{9}\text{)}

  evaluates on $(A', B', C', D')$ to the **exact same rational fraction** (residual $0$)!

Philological & Mathematical Notes on 1893 Additions
---------------------------------------------------

1. **Footnote 26 (Holomorphic vs. Anti-Holomorphic Möbius Maps):**
   Klein's 1893 self-correction notes that a genuine reflection or circle inversion reverses angle orientation, swapping the circular points $I, J$ and corresponding to $z' = \frac{\alpha \bar{z} + \beta}{\gamma \bar{z} + \delta}$, whereas orientation-preserving products of an *even* number of inversions correspond to $z' = \frac{\alpha z + \beta}{\gamma z + \delta} \in \operatorname{PSL}_2(\mathbb{C})$.
2. **Footnote 30 (Liouville's Conformal Theorem, 1850):**
   Klein derives :person:`Liouville's <liouville>` celebrated rigidity theorem from quadric geometry! On a $2$-dimensional quadric surface $Q^2 \subset \mathbb{P}^3 \cong \mathbb{P}^1 \times \mathbb{P}^1$, the two rulings of lines can be transformed by *arbitrary* holomorphic functions $(f(z), g(w))$, yielding an infinite-dimensional conformal group in dimension $2$. For $n \ge 3$, a smooth quadric $Q^n \subset \mathbb{P}^{n+1}$ contains isotropic cones at every point whose global preservation forces linearity ($\operatorname{PO}(n+1, 1)$), proving that every conformal map in dimension $n \ge 3$ belongs to the finite-dimensional Möbius inversion group!
3. **Footnote 31 & Translation Corrections in § 7:**
   In Haskell's 1893 printing of § 7, two minor typographical slips occur which are silently clarified against the 1872 German original:

   * On p. 228 (`erlangen_1893_en.md` § 6), Haskell printed *"by means of [projective] geometry with a manifoldness of five dimensions"* for Klein's *„wie vermöge der Liniengeometrie mit einer Mannigfaltigkeit von fünf Ausdehnungen“* (**line geometry**).
   * In § 7 (`erlangen_1893_en.md`), Klein's *„Ebenenbündel, dessen Scheitel auf der Kugel liegt“* ("sheaf of planes whose vertex lies on the sphere") was altered in 1893 to `[pencil] ... [axis touches]` (the dual plane-tangent formulation), and in Footnote 31 the fifth pentacyclic coordinate was misprinted once as `iu_3` and omitted in `u_1, u_2, u_3, u_4` immediately before `u_1^2 + u_2^2 + u_3^2 + u_4^2 + u_5^2`; we restore $i u_5$ and $u_1, u_2, u_3, u_4, u_5$ for mathematical clarity.
