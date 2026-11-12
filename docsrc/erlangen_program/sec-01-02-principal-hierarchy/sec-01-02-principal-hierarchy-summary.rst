:title: §§ 1–2: Principal Group & Transformation Hierarchy — Summary
:layout: book

.. _ep-sec-01-02-principal-hierarchy-summary:

§§ 1–2: The Principal Group and Transformation Hierarchy — Summary
==================================================================

.. rubric:: Analytical Structure of Klein's Axiomatic Definition of a Geometry

§ 1. Groups of Transformations, the Principal Group, and the Erlangen Problem
-----------------------------------------------------------------------------

1. **Axiomatic Group Closure (and Inverses):**
   Klein defines a :term:`transformation group <transformation-group>` $G$ on space (or on an $n$-dimensional :term:`manifold <manifold>` $M$) as a family of transformations closed under composition—adding in his famous 1893 bracketed footnote that for infinite families one must explicitly stipulate closure under inverses ($g \in G \implies g^{-1} \in G$). While dualities (correlations) alone do not form a group because the product of two dualities is a collineation, the union of collineations and dualities forms an index-$2$ group extension.
2. **The Principal Group (*Hauptgruppe*):**
   Elementary Euclidean properties depend neither on absolute spatial position (translations and rotations), nor on absolute scale (homotheties), nor on chiral orientation (mirror reflections). Their composite group is the $7$-parameter spatial (or $4$-parameter planar) :term:`Principal Group <principal-group>` of similarities. Elementary geometry is *defined* by invariance under the Principal Group.
3. **The Erlangen Problem:**
   Abstracting from physical space to any manifold $M$ equipped with an arbitrarily chosen transformation group $G$, Klein states the universal program of modern geometry:

   .. math::

      \text{Geometry}(M, G) \;\equiv\; \text{Invariant Theory of } G \text{ acting on } M.

§ 2. Stabilizer Subgroups and Distinguished Fundamental Loci
------------------------------------------------------------

Klein establishes the Galois-style duality between **restricting the group** and **adjoining a fixed geometric locus**:

* **Stabilizer Principle (Descending to a Subgroup $H \subset G$):**
  Studying configurations on $M$ relative to a fixed figure $\Omega$ under a larger group $G$ is mathematically identical to studying configurations *by themselves* under the stabilizer subgroup

  .. math::

     \operatorname{Stab}_G(\Omega) \;=\; \{\, g \in G \mid g(\Omega) = \Omega \,\}.

  For example, spherical trigonometry is the invariant theory of the $3$-parameter rotation subgroup fixing a center $O$ inside the Principal Group.
* **Ascent to Supergroups ($G_{\text{sim}} \subset G$):**
  Replacing the Principal Group $G_{\text{sim}}$ by a larger group $G$ (such as affine, projective, or inversion transformations) retains only a subset of elementary invariants as *intrinsic* properties; all remaining elementary metric properties reappear as *joint invariants* of the figure together with a distinguished locus $\Omega$ whose stabilizer in $G$ is $G_{\text{sim}}$.
