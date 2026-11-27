:title: Part I, Ch. III: Cyclotomy & Fermat Primes — Critical & Symbolic Notes
:layout: book
:canonical_id: Ch. III
:order: 3
:tracks: English: ch_03-en | German: ch_03-de | Summary: ch_03-summary | Notes: ch_03-notes

.. _fp-part_1-ch_03-notes:
.. _fp-part1-ch_03-notes:
.. _fp-ch_03-notes:
.. _fp-part1-ch3-cyclotomy-notes:

Part I, Chapter III — Critical & Symbolic Notes
===============================================

.. rubric:: Real Cyclotomic Minimal Polynomials, Kepler's Heptagon, and Fermat Number Status

Exact Polygon Classifier in ``geometor.klein.constructibility``
---------------------------------------------------------------

Combining §§ 2, 7, and 8 yields the complete **Gauss–Wantzel Theorem**: a regular :math:`n`-gon (:math:`n \ge 3`) is constructible with straightedge and compasses if and only if Euler's totient :math:`\varphi(n) = \deg \Phi_n(z)` is a power of :math:`2`:

.. math::

   \varphi(n) = 2^k \iff n = 2^a p_1 p_2 \cdots p_r,

where :math:`a \ge 0` and :math:`p_1 < p_2 < \dots < p_r` are **distinct** :term:`Fermat primes <fermat-prime>` (:math:`3, 5, 17, 257, 65537, \dots`).

In :func:`geometor.klein.constructibility.cyclotomic_real_minimal_poly`, we also compute the exact minimal polynomial :math:`\psi_n(u) \in \mathbb{Q}[u]` of the real chord coordinate :math:`u = z + z^{-1} = 2\cos\!\left(\frac{2\pi}{n}\right)` of degree :math:`\frac{1}{2}\varphi(n)`:

.. list-table:: First Non-Constructible Regular Polygons Verified by ``geometor.klein``
   :header-rows: 1
   :widths: 12 16 36 36

   * - :math:`n`
     - :math:`\varphi(n)`
     - Cyclotomic :math:`\Phi_n(z)`
     - Real Minimal Polynomial :math:`\psi_n(u)` (:math:`u = 2\cos\frac{2\pi}{n}`)
   * - :math:`7`
     - :math:`6`
     - :math:`z^6 + z^5 + z^4 + z^3 + z^2 + z + 1`
     - :math:`u^3 + u^2 - 2u - 1` (deg :math:`3`)
   * - :math:`9`
     - :math:`6`
     - :math:`z^6 + z^3 + 1`
     - :math:`u^3 - 3u + 1` (deg :math:`3`)
   * - :math:`11`
     - :math:`10`
     - :math:`z^{10} + \dots + z + 1`
     - :math:`u^5 + u^4 - 4u^3 - 3u^2 + 3u + 1` (deg :math:`5`)
   * - :math:`13`
     - :math:`12`
     - :math:`z^{12} + \dots + z + 1`
     - :math:`u^6 + u^5 - 5u^4 - 4u^3 + 6u^2 + 3u - 1` (deg :math:`6`)

Historical & Sister-Corpus Notes
--------------------------------

* **Kepler's *Inscibilis* Heptagon (`geometor/kepler`):** Nearly two centuries before :person:`Gauss <gauss>` and :person:`Wantzel <wantzel>`, :person:`Johannes Kepler <kepler>` argued in :cite:`*Harmonices Mundi*, Liber I, Props. XLV–XLVII (1619) <kepler:1619>` that the regular heptagon (:math:`n = 7`) is *inscibilis* ("unknowable" by plane geometry) because its chord determination leads to an irreducible solid/cubic problem (:math:`u^3 + u^2 - 2u - 1 = 0`) possessing no prior ground in planar bisections.
* **Status of** :math:`F_\mu = 2^{2^\mu} + 1` **After 1895**: In § 1, Klein notes that in 1895 :math:`F_5, F_6, F_7` were known to be composite while :math:`F_8` remained open (:math:`F_7` and :math:`F_8` were proved composite by Morehead and Western in 1905 and 1909; today :math:`F_5` through :math:`F_{32}` are all known to be composite, leaving Klein's prophetic remark that :math:`\mu = 4` *may be the last prime case* completely unrefuted!).
