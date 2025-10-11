# Original Question

The universe is filled with the Cosmic Microwave Background. Consider the annihilation of high energy \gamma-rays with a photon from the CMB Radiation into electron-positron, i.e. $\gamma\gamma\rightarrow e^{+}e^{-}$. From what energy \gamma-rays would have their lifetimes in the universe limited by this process? Knowing that the average photon energy of the CMB is $10^{-3}eV$.

---

# DeepSeek response (via openrouter)

\boxed{2.6 \times 10^{14} \text{ eV}}

---

# DeepSeek reasoning (via openrouter)

To solve for the energy threshold where high-energy $\gamma$-rays would interact with photons from the Cosmic Microwave Background (CMB) and produce an electron-positron pair ($\gamma + \gamma_{\text{CMB}} \rightarrow e^+ + e^-$), we need to analyze the energy required for this annihilation process.

This reaction can only take place if the center-of-momentum (CM) frame energy is sufficient to create an electron-positron pair. The total invariant mass squared for two photons with momenta $p_1$ and $p_2$ can be written as:

$$
s = (E_1 + E_2)^2 - (\vec{p}_1 + \vec{p}_2)^2 c^2,
$$
where $E_1$ and $E_2$ are the energies of the two photons (with $E_1$ being the energy of the high-energy gamma-ray and $E_2$ the energy of the CMB photon), and $\vec{p}_1$ and $\vec{p}_2$ are the momenta of the two photons. Since photons have momenta such that $|\vec{p}| = \frac{E}{c}$, the total momentum is $\vec{p}_1 + \vec{p}_2$, so the invariant mass squared becomes:

$$
s = (E_1 + E_2)^2 - |\vec{p}_1 c + \vec{p}_2 c|^2.
$$

Recall that $|\vec{p}_{i}| = \frac{E_i}{c}$ where $i$ is either $1$ or $2$. Thus:
$$
s = (E_1 + E_2)^2 - \left|\left(\vec{p}_1 + \vec{p}_2\right) c\right|^2 = (E_1 + E_2)^2 - (c|\vec{p}_1| + c|\vec{p}_2|\cos\theta)^2 - c^2\vec{p}_1^2\sin^2\theta,
$$
where $\theta$ is the angle between the two photon momenta $\vec{p}_1$ and $\vec{p}_2$. However, a more typical way to write the invariant mass is just using:
$$
s = (E_1 + E_2)^2 - \left|\vec{p}_1 c + \vec{p}_2 c\right|^2,
$$
and since $|\vec{p}_1| = \frac{E_1}{c}$ and $|\vec{p}_2| = \frac{E_2}{c}$, where $|\vec{p}|^2 = \frac{E^2}{c^2} \Rightarrow \vec{p} = \frac{E}{c} \hat{n}$ where $\hat{n}$ is the unit vector along the photon's momentum. Thus:
$$
s = (E_1 + E_2)^2 - (p_1c)^2 - (p_2c)^2 - 2(p_1c \cdot p_2c) = (E_1 + E_2)^2 - (E_1^2 + E_2^2 + 2 \vec{p}_1 \cdot \vec{p}_2 c^2).
$$
However, $\vec{p}_1 \cdot \vec{p_2} = |\vec{p_1}||\vec{p_2}| \cos \theta = \frac{E_1 E_2}{c^2} \cos \theta$, so:
$$
s = (E_1 + E_2)^2 - \left(E_1^2 + E_2^2 + 2E_1 E_2 \cos \theta \right).
$$
Expanding $(E_1 + E_2)^2$ yields:
$$
s = E_1^2 + E_2^2 + 2E_1 E_2 - E_1^2 - E_2^2 - 2 E_1 E_2 \cos \theta,
$$
$$
s = 2E_1 E_2(1 - \cos\theta).
$$
Notice that the formula above represents the squared center-of-momentum energy.

For the pair production $\gamma \gamma \rightarrow e^+ + e^-$, the threshold energy $s$ should be such that the total center-of-momentum energy should at least be equal to the total rest mass energy of the electron-positron pair. Since the rest mass energy of an electron (or positron) is about $m_e c^2 = 0.511$ MeV (which is $511$ keV or $0.511 \times 10^6$ eV), the total rest mass energy for an electron-positron pair is:
$$
s_{min} \geq (m_e c^2 + m_e c^2)^2 = (2m_e c^2)^2 = 4m_e^2 c^4.
$$
We need to solve for the threshold condition where $s \geq 4m_e^2 c^4$:
$$
2E_1 E_2(1 - \cos\theta) \geq 4m_e^2 c^4.
$$
Since we want to find the energy $E_1$ such that high-energy $\gamma$-rays interact preferentially head-on (i.e., most likely an angle of $\theta = \pi$, such that $\cos\theta = -1$ and $1 - \cos\theta = 2$), which makes the reaction most "efficient" for producing $e^+e^-$ pairs (since $1 - \cos\theta$ is maximized at such an incoming angle where photons are in opposite directions). However, for a more "average" case, we need to make an assumption about the "average" angle of collision $\theta$. However, an assumption often made here is that the high-energy photon collides with a CMB photon which could be traveling in any direction. Thus, if we aim for a "worst-case" scenario or a "threshold" condition for a "typical" collision angle, a reasonable initial assumption could be that photons collide "head-on," where $\cos\theta = -1$, such that:
$$
2E_1 E_2 \cdot 2 \geq 4m_e^2 c^4.
$$
$$
4E_1 E_2 \geq 4m_e^2 c^4.
$$
$$
E_\gamma E_{\text{CMB}} \geq m_e^2 c^4.
$$
However, this calculation makes an assumption about the angle of collision which might need some justification. Another way to interpret the "threshold" energy requirement typically recognizes that the reaction requires:
\begin{equation}
s \geq 4m_e^2~c^4.
\end{equation}
Thus, the minimum threshold condition could be expressed through the calculation upholding $2E_1 E_2(1 - \cos\theta) \geq 4m_e^2 c^4$, where $\cos\theta = -1$ makes this most probable as $1 - (-1) = 2$ gives us:
$$
4E_1 E_2 \geq (2m_ec^2)^2.
$$
$$
4E_1 E_2 \geq 4m_e^2 c^4.
$$
$$
E_1 \geq \frac{m_e^2 c^4}{E_2}.
$$
However, it seems $E_1$ is the high energy gamma-ray energy while $E_2$ is the CMB photon energy (which is given as $10^{-3}$ eV). Using $E_{\text{CMB}} = 10^{-3}$ eV and $mc^2 = 0.511\, \text{MeV} = 0.511 \times 10^6 \, \text{eV}$ for $m_e c^2$:

$$
E_{\gamma} \geq \frac{\left(0.511 \times 10^6\right)^2}{10^{-3}}.
$$
$$
E_{\gamma} \geq \frac{(0.511)^2 \times 10^{12}}{10^{-3}}.
$$
$$
E_{\gamma} \geq (0.511)^2 \times 10^{15} \approx (0.2611) \times 10^{15} \text{ (eV)}.
$$
$$
E_{\gamma} \geq 2.611 \times 10^{14} \text{ eV}.
$$

However, we need to verify the calculation a bit more explicitly. For $m_e \approx 0.511 \text{ MeV}/\text{c}^2$, $m_e c^2 \approx 0.511 \text{ MeV}$:
$$
s_{\text{min}} = (2m_e c^2)^2 = 4(m_e c^2)^2.
$$
In terms of what energy $E_1$ for the high-energy photon we need, and given $E_1 \gg E_2$ (where $E_2 \approx 10^{-3}$ eV):
$$
s = (E_1 + E_2)^2 - (p_1 c + p_2 c)^2.
$$
Approximately, $p_1 \approx E_1 / c$, $p_2 \approx E_2 / c$, thus once again:
$$
s = (E_1 + E_2)^2 - (E_1 - E_2)^2 = 4E_1 E_2,
$$
which holds only if the two photons are traveling in opposite directions such that $\vec{p_1}$ and $\vec{p_2}$ cancel out. Another way one usually proceeds makes use of the given $s \geq 4(m_e c^2)^2$, therefore:
$$
2E_1 E_2 (1 - \cos\theta) \geq 4(m_e c^2)^2.
$$
To find an "average value" for $1 - \cos\theta$, one might need to make an averaging argument here. However, if we assume a "head-on" collision as the "worst-case" favorable situation for pair production:
$$
2E_1 E_2 \cdot 2 \geq 4(m_e c^2)^2.
$$
$$
E_1 E_2 \geq (m_e c^2)^2.
$$
The question statement provides an "average photon energy" of the CMB photons $E_{\text{CMB}} = 10^{-3}eV$. So substituting $E_2 = 10^{-3}eV$ and $m_e c^2 = 0.511 \times 10^6$ eV:
$$
E_1 \geq \frac{(m_e c^2)^2}{10^{-3} \text{ eV}}.
$$
$$
E_1 \geq \frac{(0.511 \times 10^6 \text{ eV})^2}{10^{-3} \text{ eV}}.
$$
$$
E_1 \geq \frac{(0.511 \times 10^6)^2}{10^{-3}} \text{ eV}.
$$
$$
E_1 \geq \frac{(511000)^2}{10^{-3}}.
$$
$$
E_1 \geq \frac{2.61121 \times 10^{11}}{10^{-3}} \text{ eV}.
$$
$$
E_1 \geq 2.61121 \times 10^{14} \text{ eV}.
$$

This is the same as what we found previously where $E_1$ is the energy of the high-energy gamma-ray such that the process $\gamma \gamma_{\text{CMB}} \rightarrow e^+ + e^-$ could occur. Thus, the answer here seems roughly $2.6 \times 10^{14}$ eV.

Another round of double-checking shows that if the CMB photon energy is cited explicitly as "$10^{-3}$ eV," the "mean" energy of a CMB photon should technically be approximated from the relation:
$$
\langle\varepsilon_{\text{CMB}}\rangle \approx 2.7 k_B T,
$$
where $T = 2.73$ K for today's CMB background temperature. Thus:
$$
\langle\varepsilon_{\text{CMB}}\rangle \approx 2.7 \times (8.617\times 10^{-5} \text{ eV/K}) \times 2.73 \text{ K} \approx 6.35 \times 10^{-4} \text{ eV}.
$$

However, what matters here is the order of magnitude $10^{-3}$ eV seems about right. However, if one needs an accurate value, one should note that the "average" photon energy of the CMB is closer to $6.35 \times 10^{-4} \text{ eV}$ rather than $1 \times 10^{-3} \text{ eV}$.

However, if we keep the given $10^{-3} \text{ eV}$ as the given $E_{\text{CMB}}$:
$$
E_{\text{threshold}} \geq \frac{(0.511 \text{ MeV})^2}{10^{-3} \text{ eV}} = \frac{(0.511 \times 10^6 \text{ eV})^2}{10^{-3} \text{ eV}} \approx 2.61121 \times 10^{14} \text{ eV}.
$$

This translates roughly to:
$$
2.61121 \times 10^{14} \text{ eV} = 2.61121 \times 10^{11} \text{ keV} = 2.61121 \times 10^8 \text{ MeV} = 2.61121 \times 10^5 \text{ GeV} \approx 2.6 \times 10^{5} \text{ GeV}.
$$
which is $2.6 \times 10^{5}$ GeV or $260$ TeV. Such high-energy gamma rays are called ultra-high-energy photons.

Hence, the energy threshold for high-energy $\gamma$-rays such that their mean free path in the universe could be limited by pair production interaction with CMB photons (which have an approximate energy of $10^{-3} \text{ eV}$) is:
$$\boxed{2.6 \times 10^{14} \text{ eV}}$$

Another way to interpret the question might involve the cross-section for this process which depends on the available center-of-momentum frame energy $s$, but what seems most important here is deciding when the reaction $\gamma\gamma \rightarrow e^+ + e^-$ becomes feasible such that the "lifetime" of high-energy gamma-rays is significantly shortened due to the interaction probability with the CMB radiation. Thus, once gamma rays have energy exceeding this calculated threshold, they would be more liable to annihilate with CMB photons and thus have limited "lifetimes" in the universe.

Verifying such reasoning points out another physical effect called the "threshold for pair production." This is a well-known phenomenon called the "Greisen–Zatsepin–Kuzmin (GZK) limit" for ultra-high-energy cosmic rays (which applies primarily to protons interacting with the CMB, but we need a similar threshold calculation for gamma rays here called the "pair production threshold" or "gamma-gamma absorption" on the CMB photons).


---

