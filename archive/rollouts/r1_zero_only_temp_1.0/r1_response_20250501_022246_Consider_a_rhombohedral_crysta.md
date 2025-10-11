# Original Question

Consider a rhombohedral crystal, with the interatomic distance of 10 Angstrom and the angles $\quad\alpha=\beta=\gamma=30^{0}$. What is the interplanar distance of the (111) plane of the crystal?


---

# DeepSeek response (via openrouter)



---

# DeepSeek reasoning (via openrouter)

To solve for the interplanar distance of the (111) plane in a rhombohedral crystal where the interatomic distance is given as 10 Å and the angles are given as $\alpha = \beta = \gamma = 30^\circ$, we need to recall some details about the rhombohedral crystal system.

In a rhombohedral system, the lattice parameters are defined as $a = b = c$ and $\alpha = \beta = \gamma \neq 90^\circ$. Since the question states that the "interatomic distance" is given as 10 Å, here we need to interpret what "interatomic distance" refers to. Typically, "interatomic distance" could be interpreted as the lattice parameter $a=b=c$ for a rhombohedral lattice where $a=b=c=10$ Å and angles are given $\alpha=\beta=\gamma=30^\circ$.

Another way to interpret "interatomic distance" might be the actual distance between two neighboring atoms in the unit cell (which is often equal to the lattice parameter only for cubic lattices where the angles are $90^\circ$, although here we need to make sure what is meant by "interatomic distance").

However, in a crystal structure, the distance between two planes specified by Miller indices $(hkl)$ for a rhombohedral crystal system needs to be computed explicitly based on the unit cell dimensions ($a, b, c,$ and $\alpha, \beta, \gamma$). 

However, the general formula for the "interplanar spacing" $d_{hkl}$ for a rhombohedral unit cell where $a=b=c$ and $\alpha=\beta=\gamma$ is defined as follows:

$$
d_{hkl} = \frac{a \sqrt{1 - 3\cos^2\alpha + 2\cos^3\alpha}}{\sqrt{h^2+k^2+l^2}\sin^2\alpha + 2(hk + kl + hl)(\cos^2\alpha - \cos\alpha)\sin\alpha}.
$$
This comes from a more general crystallography formula for triclinic systems where $a \neq b \neq c$ and $\alpha \neq \beta \neq \gamma$, which reduces specifically for the rhombohedral case where $a = b = c$ and $\alpha = \beta = \gamma$. 

Another well-known formula for $d_{hkl}$ in a rhombohedral system (specifically when $a = b = c$ and $\alpha = \beta = \gamma$) is:
$$
\frac{1}{d_{hkl}^2} = \frac{(h^2 + k^2 + l^2)\sin^2\alpha + 2(hk + kl + hl)(\cos^2\alpha - \cos\alpha)}{a^2(1 - 3\cos^2\alpha + 2\cos^3\alpha)}
$$

These formulas can be derived from the formula for the volume $V$ of a rhombohedral unit cell:
$$
V = a^3\sqrt{1 - 3\cos^2\alpha + 2\cos^3\alpha}.
$$
But let us recall another variant of the interplanar spacing formula for a general triclinic unit cell where:
$$
\frac{1}{d^2} = \frac{1}{V^2}\left[
S_{11}h^2 + S_{22}k^2 + S_{33}l^2 + 2S_{12}hk + 2S_{23}kl + 2S_{13}hl
\right],
$$
Where $V$ is the volume of the unit cell, and $S_{ij}$ are determined by:
$$
\begin{aligned}
&S_{11} = b^2c^2\sin^2\alpha, \\
&S_{22} = a^2c^2\sin^2\beta, \\
&S_{33} = a^2b^2\sin^2\gamma, \\
&S_{12} = abc^2(\cos\alpha \cos\beta - \cos\gamma), \\
&S_{23} = a^2bc(\cos\beta \cos\gamma - \cos\alpha), \\
&S_{13} = ab^2c(\cos\alpha \cos\gamma - \cos\beta).
\end{aligned}
$$

But setting $a=b=c=|a|$ and $\alpha=\beta=\gamma$, the $S_{ij}$ expressions simplify:
$$
\begin{aligned}
&\text{Since } a=b=c, \text{ we denote $a$ as the unit cell edge length.} \\
&S_{11} = S_{22} = S_{33} = a^4\sin^2\alpha, \\
&S_{12} = S_{23} = S_{13} = a^4(\cos^2\alpha - \cos\alpha).
\end{aligned}
$$

Substitute $S_{11} = a^4\sin^2\alpha$, $S_{22} = a^4\sin^2\alpha$, $S_{33} = a^4\sin^2\alpha$, $S_{12} = a^4(\cos^2\alpha - \cos\alpha)$, $S_{23} = a^4(\cos^2\alpha - \cos\alpha)$, and $S_{13} = a^4\mathbf(\cos^2\alpha - \cos\alpha)$.

The volume $V$ for a rhombohedral cell is:
$$
V = a^3 \sqrt{1 - 3\cos^2\alpha + 2\cos^3\alpha}.
$$
Hence:
$$
\frac{1}{d^2} = \frac{1}{V^2}\left[
a^4\sin^2\alpha (h^2+k^2+l^2) + 2a^4(\cos^2\alpha - \cos\alpha)(hk + kl + hl)
\right]
$$

Since $V^2 = a^6(1 - 3\cos^2\alpha + 2\cos^3\alpha)$:
$$
\frac{1}{d^2} = \frac{a^4\sin^2\alpha (h^2+k^2+l^2) + 2a^4(\cos^2\alpha - \cos\alpha)(hk + kl + hl)}{a^6(1 - 3\cos^2\alpha + 2\cos^3\alpha)}
$$

Factor out $a^4$ from the numerator:
$$
\frac{1}{d^2} = \frac{\sin^2\alpha (h^2+k^2+l^2) + 2(\cos^2\alpha - \cos\alpha) (hk + kl + hl)}{a^2(1 - 3\cos^2\alpha + 2\cos^3\alpha)}
$$
Thus:
$$
\frac{1}{d_{hkl}^2} = \frac{(h^2 + k^2 + l^2)\sin^2\alpha + 2(hk + kl + hl)(\cos^2\alpha - \cos\alpha)}{a^2(1 - 3\cos^2\alpha + 2\cos^3\alpha)}.
$$
which matches again with the second given formula.

Given that $a = 10$ Å (where $a$ is the edge length of the rhombohedral unit pouch cell) and $\alpha = 30^\circ$, we need to find $d_{111}$.

Let us first evaluate some specific values:
$$
\cos 30^\circ = \frac{\sqrt{3}}{2} \approx 0.8660,
$$
$$
\sin 30^\circ = \frac{1}{2} = 0.5.
$$
$$
\sin^2(30^\circ) = \left(\frac{1}{2}\right)^2 = \frac{1}{4}.
$$
$$
\cos^2(30^\circ) = \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{3}{4}.
$$

Using these values in the interplanar distance formula gives us:
$$
\frac{1}{d_{111}^2} = \frac{(h^2 + k^2 + l^2)\sin^2\alpha + 2(hk + kl + hl)(\cos^2 \alpha - \cos \alpha)}{a^2(1 - 3\cos^2\alpha + 2\cos^3\alpha)}
$$
with $h=1$, $k=1$, $l=1$:
$$
\frac{1}{d_{111}^2} = \frac{[(1^2 + 1^2 + 1^2) \sin^2 30^\circ] + 2(1\cdot1 + 1\cdot1 + 1\cdot1)(\cos^2 30^\circ - \cos 30^\circ)}{a^2(1 - 3\cos^2 30^\circ + 2\cos^3 30^\circ)}.
$$

Substitute values:
$$
\frac{1}{d_{111}^2} = \frac{(1^2 + 1^2 + 1^2) \cdot \left(\frac{1}{4}\right) + 2(1\cdot1 + 1\cdot1 + 1\cdot1) \left(\left(\frac{3}{4}\right) - \frac{\sqrt{3}}{2}\right)}{a^2 \left(1 - 3 \left(\frac{3}{4}\right) + 2 \left(\frac{3\sqrt{3}}{8}\right) \right)}.
$$
Since $1^2 + 1^2 + 1^2 = 3$, and $1\cdot1 + 1\cdot1 + 1\cdot1 = 3$:
$$
\frac{3 \cdot \frac{1}{4} + 2 \cdot 3 \left(\frac{3}{4} - \frac{\sqrt{3}}{2}\right)}{a^2 \left(1 - 3 \cdot \frac{3}{4} + 2 \cdot \left(\frac{\sqrt{3}}{2}\right)^3\right)}.
$$
The dominant part on top:
$$
3 \cdot \frac{1}{4} = \frac{3}{4},
$$
$$
2 \cdot 3 \left(\frac{3}{4} - \frac{\sqrt{3}}{2\right) = 6 \left(\frac{3}{4} - \frac{\sqrt{3}}{2}\right) = 6 \cdot \left(\frac{3 - 2\sqrt{3}}{4}\right) = \frac{18 - 12\sqrt{3}}{4} = \frac{18 - twelve\sqrt{3}}{4}.
$$
So, the entire numerator part becomes:
$$
\frac{3}{4} + \frac{18 - 12\sqrt{3}}{4} = \frac{3 + 18 - 12\sqrt{3}}{4} = \frac{21 - 12\sqrt{3}}{4}.
$$
This simplifies to:
$$
\frac{21 - 12\sqrt{3}}{4}.
$$
Note that $12\sqrt{3} \approx 12 \times 1.732 = 20.784$, thus:
$$
21 - 12\sqrt{3} \approx 21 - 20.784 = 0.216.
$$
Hence:
$$
\frac{1}{d_{111}^2} \times a^2 = \frac{\phantom{.} \frac{21 - 12\sqrt{3}}{4}}{1 - 3\cos^2 30^\circ + 2\cos^3 50^\circ}.
$$
Let us solve for the term $1 - 3\cos^2 30^\circ + 2\cos^3 30^\circ$ in the denominator independently:
$$
1 - 3\left(\frac{3}{4}\right) + 2\left(\frac{3\sqrt{3}}{8}\right).
$$
$$
1 - 3\cdot\frac{3}{4} + 2\cdot\left(\frac{3\sqrt{3}}{8}\right).
$$
$$
1 - \frac{9}{4} + \frac{6\sqrt{3}}{8} = 1 - \frac{9}{4} + \frac{3\sqrt{3}}{4} = \frac{4 - 9 + 3\sqrt{3}}{4} = \frac{3\sqrt{3} - 5}{4}.
$$
Approximate $3\sqrt{3} - 5 \approx 3 \times 1.732 - 5 \approx 5.196 - 5 \approx 0.196$. Thus:
$$
\frac{1}{d_{111}^2} \times a^2 = \frac{\frac{21 - 12 \sqrt{3}}{4}}{\frac{3 \sqrt{3} - 5}{4}} = \frac{21 - 12\sqrt{3}}{3\sqrt{3} - 5}.
$$
To rationalize the fraction $\frac{21 - 12\sqrt{3}}{3\sqrt{3} - 5}$:
$$
\frac{21 - 12\sqrt{3}}{3\sqrtkick3 - 5} \times \frac{3\sqrt{3} + 5}{3\sqrt{3} + 5} = \frac{(21 - 12\sqrt{3})(3\sqrt{3} + 5)}{(3\sqrt{3})^2 - 25} = - \frac{(21 - 12\sqrt{3})(3\sqrt{3} + 5)}{2}.
$$
$$
(21 - 12\sqrt{3})(3\sqrt{3} + 5) = 21 \times 3\sqrt{3} + 21 \times 5 - 12\sqrt{3} \times 3\sqrt{3} - 12\sqrt{3} \times 5.
$$
$$
= 63\sqrt{3} + 105 - 108 - 60\sqrt{3} = 3\sqrt{3} - 3.
$$
So:
$$
\frac{1}{d_{111}^2} \times a^2 = -\frac{3\sqrt{3} - 3}{2} = \frac{3 - 3\sqrt{3}}{2}.
$$
So far, we need:
$$
\frac{1}{d_{111}^2} = \frac{3 - 3\sqrt{3}}{2} \cdot \frac{1}{a^2} = \frac{3 - 3\sqrt{3}}{2a^2}.
$$
Substituting $a = 10$ Å:
$$
\frac{1}{d_{111}^2} = \frac{3(1 - \sqrt{3})}{2 \times 100}.
$$
$$
d_{111}^2 = \frac{200}{3(1 - \sqrt{3})}.
$$
Since $1 - \sqrt{3} \approx 1 - 1.732 = -0.732$, so:
$$
d_{111}^2 = \frac{200}{3(-0.732)}, // negative sign here indicates a mistake in our sign calculations))
$$
However, a mistake must exist in an earlier step because $d^{2}_{hkl}$ cannot be negative. Let us verify the subsections separately:

$$
\frac{1}{d_{111}^2} = \frac{1}{V^2}(S_{11}h^2 + S_{22}k^2 + S_{33}l^2 + 2S_{12}hk + 2S_{23}kl + 2S_{13}hl).
$$
For $ a = b = c = 10$ Å and $\alpha=\beta=\gamma=30^\circ$, the volume $V$ is:
$$
V = abc\sqrt{1 - \cos^2\beta - \cos^2\alpha - \cos^2\gamma + 2\cos\alpha\cos\beta\cos\gamma}.
$$
Expanding the square root terms gives:
$$
V = a^3\sqrt{1 - 3\cos^2\alpha + 2\cos^3\alpha}.
$$
Plug in $a=10$ Å, $\cos 30^\circ = \sqrt{3}/2$:
$$
V = 10^3 \sqrt{1 - 3\left(\frac{3}{4}\right) + 2\left(\frac{3\sqrt{3}}{8}\right)} = 1000\sqrt{1 - \frac{9}{4} + \frac{3\sqrt{3}}{4}}.
$$
$$
= 1000\sqrt{\frac{4 - 9 + 3\sqrt{3}}{4}}.
$$
$$
= 1000\sqrt{\frac{-5 + 3\sqrt{3}}{4}}.
$$
Approximate $\dfrac{3\sqrt{3}}{4} \approx \dfrac{3 \times 1.732}{4} \approx \dfrac{5.196}{4} \approx 1.299,$ thus:
$$
-5 + 3\sqrt{3} \approx -5 + 5.196 = 0.196.
$$
So:
$$
V \approx 1000\sqrt{\frac{0.196}{4}} = 1000\sqrt{0.049} = 1000 \times 0.22136 = 221.36 \, \text{\AA}^3.
$$

Calculating $S_{11} = S_{22} = S_{33}$:
$$
S_{11} = b^2 c^2 \sin^2 \alpha = a^4 \sin^2 \alpha,
$$
$$
S_{22} = a^2 c^2 \sin^2 \beta = a^4 \sin^2 \alpha,
$$
$$
S_{33} = a^2 b^2 \sin^2 \gamma = a^4 \sin^2 \alpha.
$$
Thus,
$$
S_{11} = 10^4 \times \left(\frac{1}{2}\right)^2 = 10000 \times 0.25 = 2500.
$$
Similarly:
$$
S_{12} = abc^2 (\cos\alpha\cos\beta - \cos\gamma) = a^4(\cos^2\alpha - \cos\alpha),
$$
$$
S_{23} = a^2bc(\cos\beta\cos\gamma - \cos\alpha) = a^4(\cos^2\alpha - \cos\alpha),
$$
$$
S_{13} = ab^2c(\cos\alpha\cos\gamma - \cos\beta) = a^4(\cos^2\alpha - \cos\alpha).
$$
Plugging in values gives:
$$
S_{12} = S_{13} = S_{23 = 10^4} \left(\left(\frac{\sqrt{3}}{2}\right)^2 - \frac{\sqrt{3}}{2}\right) = 10000 \times \left(\frac{3}{4} - meal\frac{\sqrt{3}}{2}\right).
$$
$$
= 10000 \times \left(\frac{3 - 2\sqrt{3}}{4}\right) = 10000 \times \frac{3 - 3.464}{4} = 10000 \times \frac{-0.464}{4} = 10000 \times -0.116 \approx -1160.
$$

That means:
$$
\frac{1}{d_{111}^2} = \frac{1}{(221.36)^2}[2500(1^2 + 1^2 + 1^2) + 2 \times (-1160)(1\cdot1 + 1\cdot1 + 1\cdot1)].
$$

Calculating brute calculation steps:
$$
\frac{1}{d_{111}^

---

