:type: notes
:title: § 5: Space-Element & Plücker Quadric — Symbolic Notes
:layout: book
:canonical_id: § 5
:order: 6

.. _ep-sec_05-notes:
.. _ep-sec-05-notes:

§ 5: Choice of Space-Element & Plücker Quadric — Critical & Symbolic Notes
==========================================================================

.. rubric:: Plücker's Line Geometry, the Klein Quadric in :math:`\mathbb{P}^5`, and Dedekind Bodies

The Plücker–Klein Quadric in :math:`\mathbb{P}^5`
-------------------------------------------------

* :math:`\operatorname{PGL}_4(\mathbb{C}) \rtimes \mathbb{Z}_2 \;\cong\; \operatorname{PO}_6(\mathbb{C})` (**The Plücker–Klein Quadric**):
  Representing a line joining :math:`X = (x_0 : x_1 : x_2 : x_3)` and :math:`Y = (y_0 : y_1 : y_2 : y_3)` in :math:`\mathbb{P}^3` by its six :math:`2 \times 2` Plücker determinants :math:`p_{ij} = x_i y_j - x_j y_i` embeds the Grassmannian :math:`\operatorname{Gr}(2, 4)` as the smooth :math:`4`-dimensional quadric

  .. math::

     \Omega_{\text{Plücker}}(p) \;=\; p_{01} p_{23} + p_{02} p_{31} + p_{03} p_{12} \;=\; 0 \quad \subset \mathbb{P}^5,

  where spatial collineations and dualities correspond to the two connected components of orthogonal transformations preserving :math:`\Omega_{\text{Plücker}} = 0`.

* **Footnote 23 (1893 Addition on Normal Subgroups and Faithful Orbits):**
  In § 5, Klein defines a *Körper* ("body," modern *homogeneous space* :math:`G / H`) as the orbit of a geometric element under :math:`G`. In 1893, Klein added Footnote 23 pointing out that if the stabilizer :math:`H = \operatorname{Stab}_G(x_0)` contains a nontrivial *self-conjugate* (normal) subgroup :math:`N \triangleleft G`, then :math:`N` acts trivially on *every* element :math:`g \cdot x_0` of the orbit (:math:`N \subset g H g^{-1}`), so the orbit represents only the quotient group :math:`G / N` rather than :math:`G` faithfully. For instance, points at infinity fail to represent translations inside the affine or Euclidean group because translations act trivially on the plane at infinity!

Cross-Corpus Links in GEOMETOR
------------------------------

* **Bertrand Russell on Dimension & Space-Elements (`geometor/bertrand-russell`):** In :cite:`*An Essay on the Foundations of Geometry* (1897) <russell:1897>`, :person:`Russell <russell>` directly engages Klein's § 5 thesis that dimensionality is relative to the chosen space-element (*Raumelement*).
