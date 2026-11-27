:title: Note VII: Spherical Binary Forms & Quartic Resolvents — Notes
:layout: book
:canonical_id: Note VII
:order: 7
:tracks: English: note_07-en | German: note_07-de | Summary: note_07-summary | Notes: note_07-notes

.. _ep-note_07-notes:
.. _ep-note-07-notes:
.. _ep-notes-note_07-notes:

Note VII: Spherical Binary Forms & Resolvent Symmetries — Critical Notes
========================================================================

.. rubric:: Binary Forms on the Riemann Sphere and Quartic Resolvent Constructibility

Note VII & Quartic Resolvent Constructibility
---------------------------------------------

Klein's tetrahedral configuration :math:`(x,y,z), (x,-y,-z), (-x,y,-z), (-x,-y,z)` on the Riemann sphere in **Note VII** gives the geometric heart of ``geometor.klein.constructibility.cubic_resolvent``: the Klein four-group :math:`V_4 = \{1, R_x, R_y, R_z\} \triangleleft S_4` of :math:`180^\circ` rotations around the three coordinate axes :math:`OX, OY, OZ` preserves the four vertices of every tetrahedron in the syzygetic pencil :math:`i H + \lambda j f`, while the quotient group :math:`S_4 / V_4 \cong S_3` permutes the three coordinate axes (the six octahedral vertices of :math:`T`). Consequently, solving a quartic equation reduces to solving the degree-:math:`3` resolvent for the three pairs of opposite edge midpoints—which is constructible by straightedge and compasses **if and only if** that cubic resolvent splits over :math:`\mathbb{Q}` (as verified in :mod:`geometor.klein.constructibility` for :math:`x^4 - 2` vs. :math:`x^4 - x - 1`)!
