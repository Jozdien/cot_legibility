# Original Question

Consider the extension of the Standard Model given by the following Lagrangian

\mathcal{L}\subset i\bar{N}_{R}\gamma^{\mu}\partial_{\mu}N_{R}+\frac{1}{2}\left(\partial^{\mu}\phi\right)^{2}+\left|D^{\mu}S\right|^{2}-\frac{y_{i}}{2}\phi\bar{N}_{iR}^{c}N_{iR}^{c}-g_{i\alpha}\bar{N}_{iR}L_{\alpha}S-V\left(\phi,S,H\right)
with singlet fermions,$N{iR}\sim\left(1,1,0\right)$, scalar-doublet $S\sim\left(1,2,1\right)$, and singlet scalar $\phi\sim\left(1,1,0\right)$. We give $\left\langle \phi\right\rangle ^{2}=\left(x^{2}+\upsilon^{2}\right)$, where $\left\langle \phi\right\rangle =x$ and $\left\langle h\right\rangle =v$.

What is the approximation of the mass of the pseudo-Goldostone boson $H_{2}$ through radiative corrections? 

---

# DeepSeek response (via openrouter)



---

# DeepSeek reasoning (via openrouter)

To solve for the mass of the pseudo-Goldstone boson $H_2$, let us first recall the given Lagrangian:

$$
\mathcal{L} \subset i\bar{N}_{R}\gamma^{\mu}\partial_{\mu}N_{R}+\frac{1}{2}\left(\partial^{\mu}\phi\right)^{2}+\left|D^{\mu}S\right|^{2}-\frac{y_{i}}{2}\phi\bar{N}_{iR}^{c}N_{iR}-g_{i\alpha}\bar{N}_{iR}L_{\alpha}S-V\left(\phi,S,H\right).
$$

Based on the question, $N_{iR}$ are right-handed singlet fermions with quantum numbers $N_{iR} \sim (1,1,0)$ under the standard $SU(3)_c \times SU(2)_L \times U(1)_Y$ gauge group. Similarly, the scalar doublet $S\sim (1,2,1)$ has a hypercharge of $1$. The singlet scalar field $\phi \sim (1,1,0)$ has a vacuum expectation value (VEV) given such that $\langle \phi \rangle^2 = x^2 + v^2$. Another part of the question statement specifies that $ \langle \phi \rangle = x$ and $ \langle h \rangle = v$, where $h$ presumably denotes the Higgs doublet $H$.

The question states that $H_2$ is a pseudo-Goldstone boson. To find the mass of this pseudo-Goldstone boson $H_2$, let us first analyze symmetries and potential $V(\phi, S, H)$ in our given setup.

However, the true form of the potential $V(\phi, S, H)$ isn't explicitly given here. Based on the question, $H_2$ being a “pseudo-Goldstone boson” implies that there might be some approximate symmetry that is explicitly broken only by terms such as the Yukawa couplings $y_i\phi\bar{N}_{iR}^{c}N_{iR}$.

The part of the Lagrangian that induces a Majorana mass term explicitly breaks a possible global $U(1)$ symmetry under which $\phi$ could carry a charge (such that $\phi\to e^{i\alpha}\phi$, which should be matched by an opposite phase transformation of $N_{iR}$, i.e., $N_{iR}\to e^{-i\alpha/2}N_{iR}$). Such a $U(1)$ symmetry is usually referred to as a Peccei-Quinn (PQ) symmetry. However, the Majorana mass term $y_i\phi\bar{N}_{iR}^{c}N_{iR}$ explicitly breaks this $U(1)$ symmetry because:
$$
\phi\bar{N}_{iR}^{c}N_{iR} \text{ requires that the sum of the charges of } \phi, N_{R}^{c}, \text{ and } N_{R} \text{ should be zero.}
$$
However, a Majorana mass term is only possible if there is a charge mismatch such that $2Q_{N_{iR}} + Q_{\phi} \neq 0$ where $Q_{\phi}$ is the charge of $\phi$ and $Q_{N_{iR}}$ is the charge of $N_{iR}$.

Apart from the Yukawa part $y_{i}\phi\bar{N}_{iR}^c N_{iR}$, there should be some part of the potential $V(\phi, S, H)$ which makes $H_2$ a pseudo-Goldstone boson. However, here it looks like a global symmetry might be spontaneously broken by the VEV $\langle \phi\rangle=x$, which generates a Goldstone boson (which we need to identify as $H_2$). However, the term $y_{i}\phi\bar{N}_{iR}^{c}N_{iR}$ explicitly breaks the global $U(1)$ symmetry:

Since $\langle \phi\rangle = x$, all occurring symmetries should be checked explicitly. When a global continuous symmetry is spontaneously broken, a Goldstone boson is typically generated. However, if the symmetry is explicitly broken as well, the generated Goldstone boson becomes a "pseudo-Goldstone boson," which gains a small mass due to the explicit symmetry-breaking term.

To find the mass of such a pseudo-Goldstone boson from radiative corrections, we need to identify corrections arising from the explicit symmetry-breaking terms such as $y_i \phi \bar{N}_{iR}^{c} N_{iR}$. 

Suppose that initially there exists a global $U(1)$ symmetry where $\phi \rightarrow e^{i\theta}\phi$, such rotations should keep the $i\bar{N}_{R}\gamma^{\mu}\partial_{\mu}N_{R}$ and $\frac{1}{2}(\partial^{\mu}\phi)^2$ terms invariant. However, the Yukawa term $-\frac{y_{i}}{2}\phi\bar{N}_{iR}^{c}N_{iR}$ isn't invariant unless $\bar{N}_{iR}^{c}N_{iR}$ transforms as $e^{-i\theta}\bar{N}_{iR}^{c}N_{iR}$. However, $\bar{N}_{Ri}^{c}N_{Ri}$ alone should transform as $e^{-2i\alpha\theta} \bar{N}_{Ri}^{c}N_{Ri}$ where $N_{iR}$ transforms as $e^{i\alpha\theta} N_{iR}$. To make the Yukawa term invariant, $\alpha = -\frac{1}{2}$ seems appropriate such that $N_{iR}$ transforms as $e^{-i\frac{\theta}{2}}N_{iR}$. 

Thus, $U(1)$ symmetry here seems to be explicitly broken by the interaction term $y_{i}\phi\bar{N}_{iR}^{c}N_{iR}$ (which makes some Goldstone boson into a pseudo-Goldstone boson). Another part of the potential $V(\phi, S, H)$ should allow for a part which preserves such a $U(1)$ symmetry except for the $y_{i}\phi\bar{N}_{iR}^{c}N_{iR}$ term; such a part might generate a mass for the pseudo-Goldstone boson $H_2$.

To find the mass explicitly, we need to analyze the Yukawa term $-\frac{y_{i}}{2}\phi\bar{N}_{iR}^{c}N_{iR}$ carefully. 

This term appears to induce a Majorana mass term for the right-handed neutrinos once $\phi$ gets a VEV $x$ such that:
$$
-\frac{y_{i}}{2} x\bar{N}_{iR}^{c} N_{iR} + \text{h.c.} = -\frac{y_{i} x}{2}\left(\bar{N}_{iR}^{c} N_{iR} + \bar{N}_{iR} N_{iR}^{c}\right).
$$
The Majorana mass $M_{i}$ for $N_{iR}$ thus would be something like $M_{i} = y_{i}x$. 

However, this same Yukawa term could generate radiative corrections to the potential for $\phi$. To find the mass of the pseudo-Goldstone boson, let us first recall what a pseudo-Goldstone boson is: a pseudo-Goldstone boson arises when a global symmetry is both spontaneously broken (which makes a Goldstone boson) and also explicitly broken (which gives a mass to what would otherwise be a massless Goldstone boson).

The Coleman Weinberg potential can be used to find radiative corrections to the scalar potential due to the fermion loop corrections from the $y_i\phi\bar{N}_{iR}^c N_{iR}$ term. The one-loop effective potential for $\phi$ generated by the $N_{iR}$ Majorana fields can be computed as follows:
$$
V_{\text{eff}}(\phi) \approx \frac{M_{N}^4(\phi)}{64\pi^2}\left(\ln\frac{M_{N}^2(\phi)}{\mu^2} - \frac{3}{2}\right).
$$

Here $M_N(\phi)$ denotes the mass of $N_{iR}$ given by $M_{N_i}(\phi) = y_{i}\phi$, such that the full one-loop effective potential generated due to $N_{iR}$ should be summed over all $y_i$ terms for $i$ flavors of $N_{iR}$. To make the reasoning simpler, let us only consider one flavor $i$, such that:
$$
M_{N}(\phi) = y\phi.
$$
The effective potential can be expanded about $\phi = x + \varphi$ where $x$ is the VEV of $\phi$. For small fluctuations $\varphi$, expanding $M_{N}(x + \varphi) = y(x + \varphi)$:
$$
V_{\text{eff}}(\phi) = V_{\text{eff}}(x + \varphi) = \frac{[y(x + \varphi)]^4}{64\pi^2}\left(\ln\left[\frac{y^2(x + \varphi)^2}{\mu^2}\right] - \frac{3}{2}\right).
$$
Note that here it is useful to make a further substitution $y(x + \varphi) = yx\left(1 + \frac{\varphi}{x}\right)$, so that $y(x + \varphi)^2 = y^2x^2\left(1 + \frac{\varphi}{x}\right)^2$. Using $y^2x^2 = M_N^2$ where $M_N = yx$ is the Majorana mass:
$$
V_{\text{eff}}(\varphi) = \frac{y^4(x + \varphi)^4}{64\pi^2} \left[\ln\left(\frac{[y(x + \varphi)]^2}{\mu^2}\right) - \frac{3}{2\right]}.
$$
$$
=\frac{y^4(x + \varphi)^4}{64\pi^2} \left[ \ln\frac{y^2 x^2\left(1 + \frac{\varphi}{x}\right)^2}{\mu^2} - \frac{3}{2}\right].
$$
$$
= \frac{y^4(x + \varphi)^4}{64\pi^2}\left[\ln\left(\frac{y^2 x^2}{\mu^2}\right) + \ln\left(1 + \frac{\varphi}{x}\right)^2 - \frac{3}{2}\right].
$$
If $\varphi$ is small in comparison to $x$, we expand further $\left(1 + \frac{\varphi}{x}\right)^4 \approx 1 + 4\frac{\varphi}{x} + 6\frac{\varphi^2}{x^2} + \mathcal{O}\left(\left(\frac{\varphi}{x}\right)^3\right)$ and $\ln\left(1 + \frac{\varphi}{x}\right)^2 \approx 2\ln\left(1 + \frac{\varphi}{x}\right) \approx 2\left(\frac{\varphi}{x} - \frac{\varphi^2}{2x^2} + \mathcal{O}\left(\left(\frac{\varphi}{x}\right)^3\right)\right)$:
$$
y^4(x + \varphi)^4 \approx y^4 x^4 \left(1 + 4\frac{\varphi}{x} + 6\frac{\varphi^2}{x^2} + \mathcal{O}\left(\left(\frac{\varphi}{x}\right)^3\right)\right)\\
\ln\left(1 + \frac{\varphi}{x}\right)^2 \approx 2\left(\frac{\varphi}{x} - \frac{\varphi^2}{2x^2} + \mathcal{O}\left(\frac{\varphi^3}{x^3}\right)\right)
$$
Thus, rewriting the effective potential explicitly about the small fluctuations $ \varphi$:
$$
V_{\text{eff}}(x + \varphi) \approx \frac{y^4 x^4\left(1 + 4\frac{\varphi}{x} + 6\frac{\varphi^2}{x^2}\right)}{64\pi^i2}\left( \ln\left(\frac{y^2 x^2}{\mu^2}\right) + 2\left(\frac{\varphi}{x} - \frac{\varphi^2}{2x^2}\right) - \frac{3}{2} + \mathcal{O}\left(\left(\frac{\varphi}{x}\right)^3\right)\right).
$$
To isolate the mass term for the fluctuation $\varphi$, we extract the $\varphi^2$ term from the potential $V_{\text{eff}}(x + \varphi)$:

Focusing on the part involving $\varphi$ explicitly:
$$
V_{\text{eff}}(x + \varphi) \approx \frac{y^4x^4}{64\pi^2}\left\{\left(1 + 4\frac{\varphi}{x} + 6\frac{\varphi^2}{x^2} + \ldots\right) \times \left[\ln\frac{y^2x^2}{\mu^2} - \frac{3}{2} + 2\left(\frac{\varphi}{x} - \frac{\varphi^2}{2x^2} + \ldots\right)\right]\right\}.
$$
To extract the part proportional to $\varphi^2$, multiply the terms separately:
$$
\approx \frac{y^4x^4}{64\pi^2}\left\{\left(1 + 4\frac{\varphi}{x} + 6\frac{\varphi^2}{x^2} + \ldots\right)\left(\ln\frac{y^2x^finding2}{\mu^2} - \frac{3}{2}\right)+\left(1 + 4\frac{\varphi}{x} + 6\frac{\varphi^2}{x^2}\right)2\left(\frac{\varphi}{x} - \frac{\varphi_mean}{2x^2} + \ldots\right)\right\}.
$$
$$
\implies \frac{y^4x^4}{64\pi^2}\bigg[\left(\ln\frac{y^2x^2}{\mu^2} - \frac{3}{2}\right) + \left(\ln\frac{y^2x^2}{\mu^2} - \frac{3}{2}\right)4\frac{\varphi}{x} + \left(\ln\frac{y^2x^2}{\mu^2} - \frac{3}{2}\right)6\frac{\varphi^2}{x^2} +\\
2\left(\frac{\varphi}{x} - \frac{\varphi^2}{2x^2} + 4\left(\frac{\varphi^2}{x^2} - \frac{\varphi^3}{2x^3}\right) + 6\frac{\varphi^3}{x^3} + \ldots\right)\bigg].
$$
Let us collect quadratic ($\varphi^2$) terms的花:
$$
\text{Constants and terms proportional to $\varphi$}\\
\cdots + \frac{y^4x^4}{64\pi^2}\left[6\left(\ln\frac{y^2x^2}{\mu^2} - \frac{3}{2}\right)\frac{\varphi^2}{x^2} - 2\left(\frac{\varphi^2}{x^2}\right) \ldots\\
= \frac{y^4x^4}{64\pi^2}\left[6\left(\ln\frac{y^2x^4}{\mu^2} - \frac{3}{2}\right)\frac{\varphi^2}{x^2} - \frac{\varphi^clin used corresponds to the "mass term" for $\varphi$. Hence, the quadratice^2}{x^2}\right]\\
= \frac{y^4x^4}{64\pi^2}\left[\left(6\ln\frac{y^2x^2}{\mu^2} - 9 - 1\right)\frac{\varphi^2}{x^2}\right] = \frac{y^4x^2}{64\pi^2}\left(6\ln\frac{y^2x^2}{\mu^2} - 10\right)\varphi^2}.
$$
The mass term for the field $\varphi$ comes from terms such that:
$$
\frac{1}{2}m_{\varphi}^{2}\varphi^2 \equiv \frac{y^4x^2}{64\pi^2} (6\ln\frac{y^2x^2}{\mu^2} - 10)\varphi^2,
$$
$$
\text{So } \frac{1}{2}m_{\varphi}^2 = \frac{y^4x^2}{64\pi^2}(6\ln\frac{y^2x^2}{\mu^2} - 10).
$$
Therefore:
$$
m_{\varphi}^2 = \frac{y^4x^2}{32\pi^2}(6\ln\frac{y^2x^2}{\mu^2} - 10).
$$
You could also make a more symmetric choice for $\mu$, such as $\mu = y x$, which makes $\ln\frac{y^ THERE corr ser:
$$
\log\frac{y^alt point x^Uns פסಗಿ}{\mu^2} = \ln 1 = 0.
$$

Thus:
$$
m_{\varphi}^2 = \frac{y^4x^2}{32\piLimited Word scheduledifies planned^2}( - 10) = -\frac{overrightarrow10y^4x^2}{32\pi^2} = -\frac{5y^4x^2}{16\pi^2}.
$$
This seems unphysical because mass squared cannot be negative; nevertheless, it suggests that we might need to have explicit expressions for $V(\phi,S,H)$ to fully understand the symmetry-breaking structure.

Rewriting the effective potential along another approach (commonly used in Coleman Weinberg):
$$
V_{\text{1 loop}} = +\frac{M^4(\phi)}{64\pi^2}\sthinks \ln\frac{M^এবং På^卸载(\phi)}{\mu^2}.
$$
This leads bsolutely gives a $\phi^4\ln\phi$ term which gives inpamiltonian topping:
$$
V_\text{effective}(\phi) = A\phi^4 + B\phi^4 diningln\frac{\phi}{\mu'},
$$
where $A\phi^4$ is comes from tree level and $B\phi^4\ln\frac{\phi}{\scriptsize\mu}$ is from loop correction.

Hence, typically,夫 resulting in a Coleman-Weinberg potential is:
$$
V(\emesCrit주국) = \lambda\phi^4 + Beta\phi^4 \ln\frac{\phi^2呛 {\mu^2}},
$$
which upon minimizing交 setting $\rhoidden =\langle\phi\rangle$:
$$
\lambda + B + 2B\ln\frac{\rhocap思维}{\mu^2} = 0.
$$
Also ensure $\left.\frac{d^2V}{d\phi^织物}\right|_{\phi=\rho}>0$.

An alternative并 used без很0 published sources treat х somewhat distinctively by实验ह桂枝of Goldstone boson scenario typics of具体Born in:
$$
m_{\text{pGBstem}}^2 \sim \frac{\Lambda

---

