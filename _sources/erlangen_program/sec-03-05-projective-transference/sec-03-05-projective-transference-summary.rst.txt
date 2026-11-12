:title: §§ 3–5: Projective Geometry, Representation & Space-Elements — Summary
:layout: book

.. _ep-sec-03-05-projective-transference-summary:

§§ 3–5: Projective Geometry, Representation, and Choice of Space-Element — Summary
==================================================================================

.. rubric:: Analytical Synopsis of Projective Extensions, Group Equivalence, and Plücker Coordinates

§ 3. Projective Geometry, Duality, and Imaginary Elements
---------------------------------------------------------

* **Genesis of Projective Geometry:** Projective geometry emerged when projection ceased to be merely a heuristic trick for transferring properties between individual figures and became the defining equivalence relation under **the group of all projective collineations**.
* **Two Internal Group Extensions:**
  1. Adjoining **dualistic transformations** (correlations exchanging points and planes in $3$-space, or points and lines in the plane), rendering dual figures identical in the group sense.
  2. Adjoining **complex/imaginary elements and transformations** (:person:`von Staudt's <staudt>` *Beiträge*, 1856–1860), motivated not by projectivity *per se* (since real projectivities already form a group) but by closure under algebraic equations.
* **Recovery of Real Elementary Geometry:** Elementary real Euclidean geometry is recovered inside complex projective geometry by simultaneously fixing :term:`the imaginary spherical circle at infinity <the-absolute>` **and** the real subspace $\mathbb{RP}^3$.

§ 4. Transfer of Properties by Representation (*Abbildung*)
-----------------------------------------------------------

Whenever a bijection $f : A \to A'$ conjugates a group action $(A, B)$ into $(A', B' = f B f^{-1})$, the two geometries $(A, B)$ and $(A', B')$ are **isomorphic**. Klein illustrates this by two canonical isomorphisms:

1. **Binary Forms $\cong$ Conic Projectivities:** Stereographic projection from a point on a conic maps $\mathbb{P}^1$ under $\operatorname{PGL}_2$ isomorphically onto the conic under planar projectivities stabilizing it.
2. **Elementary Plane Geometry $\cong$ Punctured Quadric:** Stereographic projection of a quadric surface from a point $P_0$ maps the two generators through $P_0$ to the circular points $I, J$ at infinity, identifying planar similarity geometry with projective quadric geometry fixing $P_0$.

§ 5. Arbitrariness of the Space-Element and Transitive Group-Bodies (*Körper*)
------------------------------------------------------------------------------

* **Dimension Is Relative to the Space-Element:** Taking points ($\infty^3$), lines ($\infty^4$, :person:`Plücker <pluecker>`), planes ($\infty^3$), or general quadrics ($\infty^9$) as the primary :term:`space-element <space-element>` changes the dimension of space at will, while **preserving the mathematical substance of the geometry** so long as the underlying transformation group remains unchanged.
* **Hesse's Principle & Plücker's Line Quadric:** Pairing points on a conic identifies binary form theory with Cayley–Klein planar metric geometry; similarly, Plücker's $6$ homogeneous line coordinates satisfying $p_{01} p_{23} + p_{02} p_{31} + p_{03} p_{12} = 0$ identify $3$-dimensional projective geometry ($\operatorname{PGL}_4 \rtimes \mathbb{Z}_2$) with $5$-dimensional projective metric geometry relative to the Klein quadric in $\mathbb{P}^5$.
* **Group-Bodies (*Körper*):** Borrowing Dedekind's algebraic term *Körper*, Klein defines a geometric :term:`body <body-group>` as a single transitive orbit $G \cdot x_0$ (requiring in 1893 that the stabilizer contain no normal subgroup of $G$). Coherent coordinate representation demands that chosen space-elements form a single *Körper* (homogeneous space) or decompose cleanly into *Körper*.
