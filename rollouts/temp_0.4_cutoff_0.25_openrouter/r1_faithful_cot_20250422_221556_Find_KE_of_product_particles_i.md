# Original Question

Find KE of product particles in,
Pi(+) = mu(+) + nu
here Pi(+) is stationary.
Rest mass of Pi(+) &  mu(+) is 139.6 MeV & 105.7 MeV respectively.

---

# DeepSeek response (via openrouter)

To find the kinetic energy of the product particles in the decay \(\pi^+ \to \mu^+ + \nu\) where the \(\pi^+\) is stationary, we use conservation of energy and momentum. The rest masses of the pion (\(\pi^+\)) and muon (\(\mu^+\)) are 139.6 MeV and 105.7 MeV respectively, and the neutrino (\(\nu\)) is considered massless.

1. **Conservation of Energy**:
   The total energy before decay is the rest energy of the pion: \(E_{\text{initial}} = m_{\pi} = 139.6 \, \text{MeV}\).
   After decay, the total energy is the sum of the energies of the muon and neutrino: \(E_{\text{final}} = E_{\mu} + E_{\nu}\).

2. **Conservation of Momentum**:
   Since the pion is initially stationary, the total momentum after decay must be zero. Thus, the momentum of the muon (\(p_{\mu}\)) and neutrino (\(p_{\nu}\)) must be equal in magnitude and opposite in direction: \(p_{\mu} = p_{\nu} = p\).

3. **Relating Energies and Momenta**:
   - The energy of the neutrino is \(E_{\nu} = p\) (since it is massless).
   - The energy of the muon is \(E_{\mu} = \sqrt{p^2 + m_{\mu}^2}\).

4. **Solving for Momentum**:
   Using energy conservation:
   \[
   \sqrt{p^2 + (105.7)^2} + p = 139.6
   \]
   Solving this equation for \(p\), we get:
   \[
   p = \frac{m_{\pi}^2 - m_{\mu}^2}{2m_{\pi}}
   \]
   Substituting the values:
   \[
   p = \frac{(139.6)^2 - (105.7)^2}{2 \times 139.6} \approx 29.784 \, \text{MeV}
   \]

5. **Kinetic Energy of the Muon**:
   The kinetic energy (KE) of the muon is its total energy minus its rest mass energy:
   \[
   KE_{\mu} = E_{\mu} - m_{\mu} = \sqrt{p^2 + m_{\mu}^2} - m_{\mu}
   \]
   Substituting the values:
   \[
   KE_{\mu} = \sqrt{(29.784)^2 + (105.7)^2} - 105.7 \approx 4.12 \, \text{MeV}
   \]

6. **Final Answer**:
   The kinetic energy of the muon, rounded to one decimal place, is:
   \[
   \boxed{4.1} \, \text{MeV}
   \]

---

# DeepSeek reasoning (via openrouter)

Okay, let's see. I need to find the kinetic energy of the product particles when a positive pion (Pi+) decays into a positive muon (mu+) and a neutrino (nu). The pion is initially stationary, so its momentum is zero. The rest masses are given: 139.6 MeV for the pion and 105.7 MeV for the muon. The neutrino's rest mass is... hmm, I think neutrinos have a very tiny mass, but in many problems like this, especially at this level, they're considered massless. Maybe I should check if that's the case here. The problem doesn't specify the neutrino's mass, so I'll assume it's massless. That should simplify things.

Alright, since the pion is at rest, the total initial momentum is zero. When it decays into the muon and neutrino, their momenta must cancel each other out to conserve momentum. So the muon and neutrino must move in opposite directions with equal magnitude of momentum. But since the neutrino is massless, its energy is equal to the magnitude of its momentum times the speed of light (E = pc). For the muon, its energy will be the combination of its rest mass energy and kinetic energy.

Let me recall the conservation laws. Energy conservation: the total energy before decay is just the rest energy of the pion, which is 139.6 MeV. After decay, the total energy is the sum of the energies of the muon and neutrino. Momentum conservation: the initial momentum is zero, so the momentum of the muon must be equal in magnitude and opposite in direction to the momentum of the neutrino.

Let me denote the magnitude of the momentum of both the muon and neutrino as p. Then, the energy of the neutrino is E_nu = p*c. But since we're working in units where c=1 (common in particle physics when using MeV/c² for mass and MeV for energy), E_nu = p.

For the muon, its total energy is E_mu = sqrt( (p_mu c)^2 + (m_mu c^2)^2 ) / c²? Wait, no. Wait, in natural units (c=1), energy is sqrt(p^2 + m^2). So E_mu = sqrt(p^2 + m_mu^2), where m_mu is 105.7 MeV. Since the pion is at rest, the total energy after decay is E_mu + E_nu = m_pi = 139.6 MeV. And since momentum is conserved, p_mu = p_nu = p (but opposite directions). So we have:

sqrt(p^2 + (105.7)^2) + p = 139.6

This equation should let us solve for p. Then, once we have p, we can find the kinetic energy of the muon, which is E_mu - m_mu. The neutrino, being massless, doesn't have kinetic energy in the same way; its energy is all kinetic, but since it's massless, it's just E_nu = p.

So let's set up the equation:

sqrt(p^2 + (105.7)^2) + p = 139.6

Let me call m_mu = 105.7 MeV and m_pi = 139.6 MeV for simplicity.

So:

sqrt(p^2 + m_mu²) + p = m_pi

Let me rearrange this equation to solve for p. Let's subtract p from both sides:

sqrt(p^2 + m_mu²) = m_pi - p

Now square both sides:

p^2 + m_mu² = (m_pi - p)^2

Expand the right-hand side:

= m_pi² - 2 m_pi p + p^2

Now subtract p^2 from both sides:

m_mu² = m_pi² - 2 m_pi p

Then, solve for p:

2 m_pi p = m_pi² - m_mu²

p = (m_pi² - m_mu²) / (2 m_pi)

Plugging in the numbers:

m_pi = 139.6 MeV

m_mu = 105.7 MeV

Compute numerator: (139.6)^2 - (105.7)^2

Let me calculate that. 139.6 squared: 139.6*139.6. Let's do 140^2 = 19600, subtract 0.4*140 + 0.4^2. Wait, actually, (a - b)^2 = a² - 2ab + b². Wait, no, 139.6 is 140 - 0.4. So (140 - 0.4)^2 = 140² - 2*140*0.4 + 0.4² = 19600 - 112 + 0.16 = 19488.16

Similarly, 105.7 squared. Let's see, 100^2 = 10000, 5.7^2 = 32.49, and cross term 2*100*5.7 = 1140. So (100 + 5.7)^2 = 10000 + 1140 + 32.49 = 11172.49

Therefore, numerator is 19488.16 - 11172.49 = 19488.16 - 11172.49. Let's subtract:

19488.16 - 11172.49:

19488.16 - 11000 = 8488.16

8488.16 - 172.49 = 8315.67

So numerator is approximately 8315.67 MeV²

Denominator is 2 * 139.6 = 279.2 MeV

So p = 8315.67 / 279.2 ≈ let's compute that.

Divide 8315.67 by 279.2:

279.2 * 30 = 8376. That's a bit more than 8315.67. So 30 - (8376 - 8315.67)/279.2

Difference is 8376 - 8315.67 = 60.33

So 60.33 / 279.2 ≈ 0.216

So p ≈ 30 - 0.216 ≈ 29.784 MeV/c

Wait, but units: since we're working in natural units where c=1, p is in MeV/c, but since energy is in MeV and mass in MeV/c², when c=1, E in MeV, mass m in MeV/c², so E = mc² is m (in MeV/c²) * c² = MeV. So momentum p in units of MeV/c. But when using E = pc for the neutrino, E_nu = p * c, but if p is in MeV/c, then E_nu = (MeV/c) * c = MeV, which is consistent. But in the equation, we considered E_nu = p, so maybe in the calculation we have to be careful. Wait, perhaps in natural units where c=1, the momentum p is in MeV (since E = pc, if c=1, then E = p). So maybe in the equation, p is in MeV, and the units work out. Let me confirm.

Actually, in natural units (c=1, ħ=1), mass is in energy units (MeV), momentum is in energy units (MeV), and energy is in MeV. So E_nu = p_nu (since E = pc and c=1). Similarly, E_mu = sqrt(p_mu² + m_mu²). So when we solve for p, it's in MeV. Therefore, the momentum p is 29.784 MeV.

Wait, but when I did the calculation:

p = (m_pi² - m_mu²)/(2 m_pi) = (139.6² - 105.7²)/(2*139.6) ≈ 8315.67 / 279.2 ≈ 29.784 MeV.

Yes, so p ≈ 29.784 MeV.

Now, let's check this. Let's plug back into the equation sqrt(p² + m_mu²) + p.

Compute sqrt(29.784² + 105.7²). Let's compute 29.784²: approx 29.784^2 = (30 - 0.216)^2 = 900 - 2*30*0.216 + 0.216² ≈ 900 - 12.96 + 0.0466 ≈ 887.0866

Then add 105.7² = 11172.49, so total under sqrt is 887.0866 + 11172.49 ≈ 12059.5766

sqrt(12059.5766) ≈ 109.8 (since 109^2 = 11881, 110^2 = 12100, so sqrt(12059.57) ≈ 109.8)

Then add p ≈ 29.784: 109.8 + 29.784 ≈ 139.584, which is approximately 139.6, matching the pion mass. So that checks out.

Okay, so p ≈ 29.784 MeV.

Now, the total energy of the muon is sqrt(p² + m_mu²) ≈ sqrt(887.0866 + 11172.49) ≈ sqrt(12059.5766) ≈ 109.8 MeV.

Therefore, the kinetic energy of the muon is E_mu - m_mu = 109.8 MeV - 105.7 MeV ≈ 4.1 MeV.

But wait, let's be more precise. Let's compute sqrt(29.784^2 + 105.7^2):

First, exact value of p is (139.6² - 105.7²)/(2*139.6)

Compute numerator: 139.6² = (139 + 0.6)^2 = 139² + 2*139*0.6 + 0.6² = 19321 + 166.8 + 0.36 = 19488.16

105.7² = (105 + 0.7)^2 = 105² + 2*105*0.7 + 0.7² = 11025 + 147 + 0.49 = 11172.49

Numerator: 19488.16 - 11172.49 = 8315.67

Denominator: 2*139.6 = 279.2

p = 8315.67 / 279.2 ≈ let's compute this division more accurately.

8315.67 ÷ 279.2:

279.2 * 29 = 279.2*30 = 8376 - 279.2 = 8376 - 279.2 = 8096.8? Wait, no. 279.2*29 = 279.2*(30 -1) = 8376 - 279.2 = 8376 - 279.2 = 8376 - 200 = 8176, 8176 - 79.2 = 8096.8. But 29*279.2 = 8096.8

But 29*279.2 = 8096.8

So 8315.67 - 8096.8 = 218.87

So 218.87 / 279.2 ≈ 0.784

So total p ≈ 29 + 0.784 = 29.784 MeV

So same as before.

Then sqrt(29.784² + 105.7²):

Compute 29.784² = 29.784*29.784:

Calculate 30*30 = 900, subtract 0.216*30*2 - 0.216²

Wait, (a - b)^2 = a² - 2ab + b² where a=30, b=0.216

So 30² - 2*30*0.216 + 0.216² = 900 - 12.96 + 0.046656 ≈ 900 -12.96 = 887.04 + 0.046656 ≈ 887.086656

Then add 105.7² = 11172.49

So total under sqrt: 887.086656 + 11172.49 = 12059.576656

sqrt(12059.576656). Let's compute this precisely.

Find sqrt(12059.576656):

Note that 110² = 12100, which is just above 12059.57.

Compute 109.8² = (110 - 0.2)^2 = 12100 - 44 + 0.04 = 12056.04

Compare to 12059.576656. The difference is 12059.576656 - 12056.04 = 3.536656

The derivative of sqrt(x) at x=12056.04 is 1/(2*sqrt(12056.04)) ≈ 1/(2*109.8) ≈ 1/219.6 ≈ 0.004556

So approximate sqrt(12059.576656) ≈ 109.8 + 3.536656 * 0.004556 ≈ 109.8 + 0.0161 ≈ 109.8161

Thus, E_mu ≈ 109.8161 MeV

Then, the kinetic energy KE_mu = E_mu - m_mu = 109.8161 - 105.7 = 4.1161 MeV

So approximately 4.116 MeV. Rounding to a reasonable precision, maybe 4.1 MeV. But let's check if the problem expects more precise.

Alternatively, maybe we can compute sqrt(12059.576656) more accurately.

Let me try:

We have 109.8² = 12056.04

We need to find sqrt(12059.576656). Let's denote x = 12056.04, y = 12059.576656.

The difference is y - x = 3.536656

Using linear approximation:

sqrt(y) ≈ sqrt(x) + (y - x)/(2*sqrt(x))

= 109.8 + 3.536656/(2*109.8) = 109.8 + 3.536656/219.6 ≈ 109.8 + 0.0161 ≈ 109.8161, same as before.

Alternatively, use another term.

Let me write it as sqrt(x + Δx) ≈ sqrt(x) + Δx/(2 sqrt(x)) - (Δx)^2/(8 x^(3/2)) + ...

But maybe this is overkill. Alternatively, compute 109.8 + d, where d is small.

(109.8 + d)^2 = 109.8² + 2*109.8*d + d² = 12056.04 + 219.6 d + d² = 12059.576656

So 219.6 d ≈ 12059.576656 - 12056.04 = 3.536656

Thus, d ≈ 3.536656 / 219.6 ≈ 0.0161, so as before.

Thus, sqrt(y) ≈ 109.8 + 0.0161 = 109.8161

So E_mu ≈ 109.8161 MeV

Therefore, KE_mu = 109.8161 - 105.7 = 4.1161 MeV ≈ 4.12 MeV

So approximately 4.12 MeV. Depending on rounding, maybe 4.1 MeV or 4.12 MeV.

But let's check if there's another way to compute KE without going through momentum.

Alternatively, since the pion is at rest, the muon and neutrino must have equal and opposite momenta. The total energy is the sum of their energies.

But since the neutrino is massless, its energy is p, and the muon's energy is sqrt(p² + m_mu²). Then total energy is sqrt(p² + m_mu²) + p = m_pi.

We did that already.

Alternatively, we can think in terms of relativistic energy and use the relation for decay at rest.

In general, when a particle of mass M decays into two particles, one of mass m and the other massless, the kinetic energy of the massive particle can be found by:

K = (M² - m²)/(2M) - m + m ?

Wait, no. Wait, the kinetic energy is total energy minus rest mass.

From earlier, we have E_mu = (M² + m_mu²)/(2M). Wait, let's check.

Wait, from the equation:

sqrt(p² + m_mu²) = M - p

Square both sides:

p² + m_mu² = M² - 2Mp + p²

Cancel p²:

m_mu² = M² - 2Mp

Then solve for p:

p = (M² - m_mu²)/(2M)

Then E_mu = sqrt(p² + m_mu²) = sqrt( [(M² - m_mu²)/(2M)]² + m_mu² )

= sqrt( (M^4 - 2 M² m_mu² + m_mu^4 + 4 M² m_mu² ) / (4 M²) )

= sqrt( (M^4 + 2 M² m_mu² + m_mu^4 ) / (4 M²) )

= sqrt( (M² + m_mu²)^2 / (4 M²) ) )

= (M² + m_mu²)/(2M)

Therefore, E_mu = (M² + m_mu²)/(2M)

Then, KE_mu = E_mu - m_mu = (M² + m_mu²)/(2M) - m_mu

= (M² + m_mu² - 2 M m_mu)/(2M)

= (M - m_mu)^2 / (2M)

Wait, that's interesting. So KE_mu = (M - m_mu)^2 / (2M)

Let me verify that.

(M - m_mu)^2 = M² - 2 M m_mu + m_mu²

Then divided by (2M):

(M² - 2 M m_mu + m_mu²)/(2M) = (M² + m_mu²)/(2M) - (2 M m_mu)/(2M) = E_mu - m_mu = KE_mu.

Yes, that works. So KE_mu = (M - m_mu)^2 / (2M)

So plugging in M = 139.6 MeV, m_mu = 105.7 MeV:

KE_mu = (139.6 - 105.7)^2 / (2*139.6)

Compute numerator: (33.9)^2 = 33.9*33.9

30*30 = 900, 30*3.9 = 117, 3.9*30 = 117, 3.9*3.9 = 15.21

So 900 + 117 + 117 + 15.21 = 900 + 234 + 15.21 = 1149.21

So numerator is 1149.21 MeV²

Denominator: 2*139.6 = 279.2 MeV

Thus, KE_mu = 1149.21 / 279.2 ≈ 4.116 MeV

Which matches our previous result. So this formula is a quicker way.

So KE_mu = (M² - 2 M m_mu + m_mu²)/(2M) = (M - m_mu)^2 / (2M)

Therefore, the kinetic energy of the muon is (139.6 - 105.7)^2 / (2*139.6) ≈ 4.116 MeV

So approximately 4.12 MeV.

But the question says "Find KE of product particles". Wait, the products are mu+ and neutrino. But the neutrino is massless, so its kinetic energy is equal to its total energy, which is p = 29.784 MeV. But the problem might be asking only for the kinetic energy of the muon, since the neutrino's kinetic energy is its total energy. But the wording is "product particles", plural. So maybe we need to give both?

Wait, the problem says "Find KE of product particles in Pi+ → mu+ + nu". It doesn't specify which one, but since there are two product particles, mu+ and nu. However, in many textbooks, when a particle at rest decays into two particles, one massive and one massless, the massive one gets a small KE, and the massless one carries away the majority of the energy. But in terms of KE, since the neutrino is massless, its KE is equal to its energy (since it has no rest mass). But maybe the question is only asking for the KE of the muon? Or both?

Wait, the problem says "Find KE of product particles". The product particles are the mu+ and the neutrino. So we need to find the KE for each. But the neutrino, being massless, has KE equal to its energy (E = pc), so that's 29.784 MeV. The muon's KE is 4.116 MeV. So total KE is 29.784 + 4.116 ≈ 33.9 MeV, which is equal to the pion's rest mass minus the muon's rest mass (139.6 - 105.7 = 33.9). That makes sense because the neutrino's energy is entirely KE, and the muon's KE is the remaining part.

But the question might just be asking for the KE of the muon, since the neutrino's KE is its total energy, but maybe they want both. However, in particle physics, often when a problem like this is posed, they are asking for the kinetic energy of the massive particle, as the neutrino's energy is harder to measure and is often inferred. But the problem statement isn't entirely clear. However, in the decay process, the total energy released (the Q value) is the rest mass of the pion minus the rest mass of the muon (since the neutrino is massless), which is 139.6 - 105.7 = 33.9 MeV. This energy is distributed as kinetic energy between the muon and the neutrino. So the KE of the muon is 4.116 MeV, and the KE of the neutrino is 29.784 MeV, totaling 33.9 MeV.

But perhaps the question expects only the KE of the muon, since it's the only one with rest mass. Let me check common practice. For example, in the decay of a pion at rest into a muon and neutrino, the muon's kinetic energy is a standard calculation, often given as approximately 4.1 MeV. So likely the answer expected is about 4.1 MeV.

But to be thorough, let's check units and exactness.

Using the exact formula KE_mu = (M - m_mu)^2 / (2M)

Plugging in exact numbers:

M = 139.6 MeV

m_mu = 105.7 MeV

Difference: 139.6 - 105.7 = 33.9 MeV

Square: 33.9^2 = 1149.21 MeV²

Divide by 2M: 1149.21 / (2*139.6) = 1149.21 / 279.2

Compute 279.2 * 4 = 1116.8

1149.21 - 1116.8 = 32.41

32.41 / 279.2 ≈ 0.1161

Thus, total KE_mu ≈ 4.1161 MeV

So approximately 4.12 MeV.

Rounded to two decimal places, 4.12 MeV. If three significant figures, since the given masses are four significant figures (139.6 and 105.7), the result should have three, so 4.12 MeV.

But let's check with more precise calculation:

33.9^2 = (34 - 0.1)^2 = 34^2 - 2*34*0.1 + 0.1^2 = 1156 - 6.8 + 0.01 = 1149.21

So yes, 1149.21 / 279.2:

279.2 * 4 = 1116.8

1149.21 - 1116.8 = 32.41

32.41 / 279.2 = 0.1161 (as before)

So 4.1161 MeV.

Thus, the kinetic energy of the muon is approximately 4.12 MeV.

The neutrino's kinetic energy is equal to its energy, which is p = 29.784 MeV.

But the problem says "Find KE of product particles". Since there are two product particles, maybe we need to give both. However, in many cases, especially in exams or textbooks, when they ask for KE in a decay like this, they are referring to the massive particle, as the neutrino's KE is just its total energy. But to be safe, perhaps the answer requires both.

But looking back at the problem statement:

"Find KE of product particles in,

Pi(+) = mu(+) + nu

here Pi(+) is stationary.

Rest mass of Pi(+) & mu(+) is 139.6 MeV & 105.7 MeV respectively."

It says "product particles", plural. So both the mu+ and the neutrino. But the neutrino is massless, so its KE is equal to its energy (since for massless particles, KE = total energy). So we need to calculate both.

But let's see if the system expects both answers. However, typically, in such problems, the answer expected is the kinetic energy of the massive particle, because the neutrino's energy is considered as KE but it's already accounted for in the momentum conservation. But maybe not. Let's think.

The total energy of the system is 139.6 MeV. The rest mass of the muon is 105.7 MeV. The remaining energy is 139.6 - 105.7 = 33.9 MeV, which is distributed as kinetic energy between the muon and the neutrino. However, because the pion is at rest, the muon and neutrino must have equal and opposite momenta. This constraints their energies such that the muon's KE is 4.12 MeV and the neutrino's KE is 29.78 MeV, totaling 33.9 MeV.

But the problem asks for KE of product particles. So both. But in the context of the question, maybe only the muon's KE is required because the neutrino's is harder to observe, but the problem doesn't specify. Given that, perhaps the answer is both. But let's see.

Wait, in the problem statement, the rest mass of the neutrino is not given. If we assume it's zero, then its KE is equal to its energy, as mentioned. If the neutrino had a non-zero mass, we would need to consider it, but since it's not given, we take it as zero.

So, final answer: the kinetic energy of the muon is approximately 4.12 MeV, and the kinetic energy of the neutrino is approximately 29.78 MeV. But the question says "Find KE of product particles". If they expect both, we need to provide both. However, the way the question is phrased might imply a single answer, which would be the muon's KE, since the neutrino's KE is its total energy and maybe considered trivial. But given that the muon's KE is non-trivial, perhaps the answer is 4.1 MeV.

But to be precise, let's check standard textbooks. For example, in the decay π+ → μ+ + ν, the muon's kinetic energy is given by (m_π - m_μ)^2 / (2 m_π), which is exactly what we derived. Plugging in the numbers:

(m_π - m_μ) = 33.9 MeV

Square: 33.9² = 1149.21

Divide by (2 m_π) = 279.2

1149.21 / 279.2 ≈ 4.116 MeV

So yes, the standard result is about 4.12 MeV.

Therefore, the answer is approximately 4.1 MeV. Given the problem provides rest masses to one decimal place, the answer should be to the same precision, so 4.1 MeV.

Wait, but 139.6 and 105.7 are given to four significant figures (if we consider the decimal), so maybe we should keep three or four. Let me check:

139.6 - 105.7 = 33.9 (three significant figures)

33.9 squared is 1149.21 (but 33.9 is three significant figures, so 33.9^2 is 1.15×10^3)

Divided by 2*139.6 = 279.2 (four significant figures)

So 1149.21 / 279.2 = 4.116 MeV. Since the least number of significant figures in the inputs is three (from 33.9), the answer should have three significant figures: 4.12 MeV.

But 33.9 has three, 139.6 has four, 105.7 has four. The subtraction 139.6 - 105.7 = 33.9 is precise to the tenths place, which is three significant figures. Then the square keeps that, and division by 279.2 (four sig figs) would result in three sig figs. So 4.12 MeV.

But depending on the instructor's preference, maybe they expect rounding to one decimal place, matching the given data's decimal places. The rest masses are given to one decimal place (139.6, 105.7). So the answer should be to one decimal place: 4.1 MeV.

Alternatively, since 139.6 - 105.7 = 33.9, which is exact (given to one decimal), then square is 33.9² = 1149.21, which is exact. Divided by 279.2 (139.6*2), which is also exact. Then 1149.21 / 279.2 = 4.11605... So to one decimal place, 4.1 MeV. To two decimal places, 4.12 MeV.

But given the problem gives masses to one decimal, it's safer to give the answer to one decimal: 4.1 MeV.

However, some might argue that since the result is 4.116, which is 4.1 MeV when rounded to one decimal, but 4.12 to two. To match the precision of the inputs, which have four significant figures (139.6 is four, 105.7 is four), the result can have three or four. But the subtraction 139.6 - 105.7 = 33.9 reduces it to three significant figures. Then the square and division would give a result with three significant figures: 4.12 (three sig figs). Wait, 33.9 is three sig figs, 33.9^2 = 1149.21, which is five, but treated as three. Then 1149.21 / 279.2 = 4.116, which with three sig figs is 4.12.

But I'm getting conflicting ideas. Let's recall the rules:

When subtracting, the number of decimal places is the minimum of the two. 139.6 (one decimal) minus 105.7 (one decimal) = 33.9 (one decimal). So 33.9 has three significant figures but one decimal place.

When squaring 33.9 (three sig figs), we get 1149.21, which should be rounded to three sig figs: 1150.

Then 1150 / 279.2 = 4.12 (approximately 4.119), which to three sig figs is 4.12.

But 1150 has three sig figs (if written as 1.15×10^3), and 279.2 has four. The result is 4.119, which to three sig figs is 4.12.

But this is getting too into the weeds. Given that, and considering that in particle physics, it's common to give results to a couple of decimal places if the input data allows, the answer is approximately 4.12 MeV. However, looking up the accepted value for the kinetic energy of the muon in pion decay, it's known to be about 4.1 MeV. For example, the commonly accepted value is approximately 4.1 MeV.

Given that, and considering the problem gives masses to one decimal place, the appropriate answer is 4.1 MeV.

But to confirm, let's do the calculation with more precise steps:

KE_mu = (139.6² - 105.7²)/(2*139.6) - 105.7 + 105.7? Wait no, KE_mu = E_mu - m_mu = [(139.6² + 105.7²)/(2*139.6)] - 105.7

Compute numerator: 139.6² = 19488.16

105.7² = 11172.49

Sum: 19488.16 + 11172.49 = 30660.65

Divide by 2*139.6 = 279.2:

30660.65 / 279.2 ≈ let's compute:

279.2 * 109 = 279.2*100 + 279.2*9 = 27920 + 2512.8 = 30432.8

Subtract from 30660.65: 30660.65 - 30432.8 = 227.85

Now, 279.2 * 0.8 = 223.36

Subtract: 227.85 - 223.36 = 4.49

So total is 109.8 + 0.8 + 4.49/279.2 ≈ 109.8 + 0.8 + 0.016 ≈ 110.616

Wait, no. Wait, the total is 109 + 0.8 + (4.49/279.2). Wait, no:

Wait, 30660.65 / 279.2:

We did 279.2*109 = 30432.8

30660.65 - 30432.8 = 227.85

Now, 227.85 / 279.2 ≈ 0.816

So total is 109 + 0.816 = 109.816

Then E_mu = 109.816 MeV

KE_mu = 109.816 - 105.7 = 4.116 MeV

So 4.116 MeV, which rounds to 4.12 MeV (two decimal places) or 4.1 MeV (one decimal place). Given the inputs are to one decimal, it's 4.1 MeV.

But I think in this context, since the rest masses are given to one decimal, the answer should also be to one decimal: 4.1 MeV.

However, considering that 139.6 - 105.7 = 33.9 is exact (no rounding), and the subsequent calculation is precise, maybe we can keep two decimals. But the problem might expect the answer as 4.1 MeV.

Alternatively, check with the exact calculation:

KE_mu = (139.6² - 105.7²)/(2*139.6)

Wait, no, KE_mu = (M - m)^2/(2M) = (33.9)^2/(2*139.6) = 1149.21/279.2 = 4.116 MeV.

So 4.116 is approximately 4.12 MeV when rounded to three significant figures (since 33.9 has three), or 4.1 MeV to two significant figures.

But 33.9 has three significant figures, so the result should have three: 4.12 MeV.

However, the initial masses have four significant figures (139.6 and 105.7), but their difference has three. So the result is three significant figures.

Therefore, the kinetic energy of the muon is 4.12 MeV.

But to check, let's see what is the exact value. If we use more precise calculations:

m_pi = 139.6 MeV

m_mu = 105.7 MeV

KE_mu = (m_pi - m_mu)^2 / (2 m_pi) = (33.9)^2 / (2*139.6) = 1149.21 / 279.2

Let's compute 1149.21 ÷ 279.2:

279.2 × 4 = 1116.8

1149.21 - 1116.8 = 32.41

32.41 ÷ 279.2 = 0.11605...

So total KE_mu = 4.11605... MeV

Rounded to three significant figures: 4.12 MeV

Rounded to one decimal place: 4.1 MeV

Given that the problem's data is to one decimal place, but the result is derived from three significant figures in the difference, it's a bit ambiguous. However, in physics problems, it's common to keep at least three significant figures unless specified otherwise. Therefore, the answer is 4.12 MeV.

But looking up the standard value, the kinetic energy of the muon in pion decay is indeed approximately 4.1 MeV. For example, according to standard references, the muon kinetic energy in π+ → μ+ + ν decay is about 4.1 MeV. Therefore, the answer is 4.1 MeV.

Given that, I think the answer should be 4.1 MeV.

**Final Answer**
The kinetic energy of the muon is \boxed{4.1} MeV.

---

# Cut off deepseek reasoning

Okay, let's see. I need to find the kinetic energy of the product particles when a positive pion (Pi+) decays into a positive muon (mu+) and a neutrino (nu). The pion is initially stationary, so its momentum is zero. The rest masses are given: 139.6 MeV for the pion and 105.7 MeV for the muon. The neutrino's rest mass is... hmm, I think neutrinos have a very tiny mass, but in many problems like this, especially at this level, they're considered massless. Maybe I should check if that's the case here. The problem doesn't specify the neutrino's mass, so I'll assume it's massless. That should simplify things.

Alright, since the pion is at rest, the total initial momentum is zero. When it decays into the muon and neutrino, their momenta must cancel each other out to conserve momentum. So the muon and neutrino must move in opposite directions with equal magnitude of momentum. But since the neutrino is massless, its energy is equal to the magnitude of its momentum times the speed of light (E = pc). For the muon, its energy will be the combination of its rest mass energy and kinetic energy.

Let me recall the conservation laws. Energy conservation: the total energy before decay is just the rest energy of the pion, which is 139.6 MeV. After decay, the total energy is the sum of the energies of the muon and neutrino. Momentum conservation: the initial momentum is zero, so the momentum of the muon must be equal in magnitude and opposite in direction to the momentum of the neutrino.

Let me denote the magnitude of the momentum of both the muon and neutrino as p. Then, the energy of the neutrino is E_nu = p*c. But since we're working in units where c=1 (common in particle physics when using MeV/c² for mass and MeV for energy), E_nu = p.

For the muon, its total energy is E_mu = sqrt( (p_mu c)^2 + (m_mu c^2)^2 ) / c²? Wait, no. Wait, in natural units (c=1), energy is sqrt(p^2 + m^2). So E_mu = sqrt(p^2 + m_mu^2), where m_mu is 105.7 MeV. Since the pion is at rest, the total energy after decay is E_mu + E_nu = m_pi = 139.6 MeV. And since momentum is conserved, p_mu = p_nu = p (but opposite directions). So we have:

sqrt(p^2 + (105.7)^2) + p = 139.6

This equation should let us solve for p. Then, once we have p, we can find the kinetic energy of the muon, which is E_mu - m_mu. The neutrino, being massless, doesn't have kinetic energy in the same way; its energy is all kinetic, but since it's massless, it's just E_nu = p.

So let's set up the equation:

sqrt(p^2 + (105.7)^2) + p = 139.6

Let me call m_mu = 105.7 MeV and m_pi = 139.6 MeV for simplicity.

So:

sqrt(p^2 + m_mu²) + p = m_pi

Let me rearrange this equation to solve for p. Let's subtract p from both sides:

sqrt(p^2 + m_mu²) = m_pi - p

Now square both sides:

p^2 + m_mu² = (m_pi - p)^2

Expand the right-hand side:

= m_pi² - 2 m_pi p + p^2

Now subtract p^2 from both sides:

m_mu² = m_pi² - 2 m_pi p

Then, solve for p:

2 m_pi p = m_pi² - m_mu²

p = (m_pi² - m_mu²) / (2 m_pi)

Plugging in the numbers:

m_pi = 139.6 MeV

m_mu = 105.7 MeV

Compute numerator: (139.6)^2 - (105.7)^2

Let me calculate that. 139.6 squared: 139.6*139.6. Let's do 140^2 = 19600, subtract 0.4*140 + 0.4^2. Wait, actually, (a - b)^2 = a² - 2ab + b². Wait, no, 139.6 is 140 - 0.4. So (140 - 0.4)^2 = 140² - 2*140*0.4 + 0.4² = 19600 - 112 + 0.16 = 19488.16

Similarly, 105.7 squared. Let's see, 100^2 = 10000, 5.7^2 = 32.49, and cross term 2*100*5.7 = 1140. So (100 + 5.7)^2 = 10000 + 1140 + 32.49 = 11172.49

Therefore, numerator is 19488.16 - 11172.49 = 19488.16 - 11172.49. Let's subtract:

19488.16 - 11172.49:

19488.16 - 11000 = 8488.16

8488.16 - 172.49 = 8315.67

So numerator is approximately 8315.67 MeV²

Denominator is 2 * 139.6 = 279.2 MeV

So p = 8315.67 / 279.2 ≈ let's compute that.

Divide 8315.67 by 279.2:

279.2 * 30 = 8376. That's a bit more than 8315.67. So 30 - (8376 - 8315.67)/279.2

Difference is 8376 - 8315.67 = 60.33

So 60.33 / 279.2 ≈ 0.216

So p ≈ 30 - 0.216 ≈ 29.784 MeV/c

Wait, but units: since we're working in natural units where c=1, p is in MeV/c, but since energy is in MeV and mass in MeV/c², when c=1, E in MeV, mass m in MeV/c², so E = mc² is m (in MeV/c²) * c² = MeV. So momentum p in units of MeV/c. But when using E = pc for the neutrino, E_nu = p * c, but if p is in MeV/c, then E_nu = (MeV/c) * c = MeV, which is consistent. But in the equation, we considered E_nu = p, so maybe in the calculation we have to be careful. Wait, perhaps in natural units where c=1, the momentum p is in MeV (since E = pc, if c=1, then E = p). So maybe in the equation, p is in MeV, and the units work out. Let me confirm.

Actually, in natural units (c=1, ħ=1), mass is in energy units (MeV), momentum is in energy units (MeV), and energy is in MeV. So E_nu = p_nu (since E = pc and c=1). Similarly, E_mu = sqrt(p_mu² + m_mu²). So when we solve for p, it's in MeV. Therefore, the momentum p is 29.784 MeV.

Wait, but when I did the calculation:

p = (m_pi² - m_mu²)/(2 m_pi) = (139.6² - 105.7²)/(2*139.6) ≈ 8315.67 / 279.2 ≈ 29.784 MeV.

Yes, so p ≈ 29.784 MeV.

Now, let's check this. Let's plug back into the equation sqrt(p² + m_mu²) + p.

Compute sqrt(29.784² + 105.7²). Let's compute 29.784²: approx 29.784^2 = (30 - 0.216)^2 = 900 - 2*30*0.216 + 0.216² ≈ 900 - 12.96 + 0.0466 ≈ 887.0866

Then add 105.7² = 11172.49, so total under sqrt is 887.0866 + 11172.49 ≈ 12059.5766

sqrt(12059.5766) ≈ 109.8 (since 109^2 = 11881, 110^2 = 12100, so sqrt(12059.57) ≈ 109.8)

Then add p ≈ 29.784: 109.8 + 29.784 ≈ 139.584, which is approximately 139.6, matching the pion mass. So that checks out.

Okay, so p ≈ 29.784 MeV.

Now, the total energy of the muon is sqrt(p² + m_mu²) ≈ sqrt(887.0866 + 11172.49) ≈ sqrt(12059.5766) ≈ 109.8 MeV.

Therefore, the kinetic energy of the muon is E_mu - m_mu = 109.8 MeV - 105.7 MeV ≈ 4.1 MeV.

But wait, let's be more precise. Let's compute sqrt(29.784^2 + 105.7^2):

First, exact value of p is (139.6² - 1

---

# Anthropic completion

Let me calculate the kinetic energy of the resulting particles when a stationary positive pion (Pi+) decays into a positive muon (mu+) and a neutrino (nu). The pion has a rest mass of 139.6 MeV, while the muon's rest mass is 105.7 MeV. Since the problem doesn't specify the neutrino's mass, I'll follow standard practice in particle physics problems and assume it's massless.

Since the initial pion is at rest, the total momentum is zero. By conservation of momentum, after decay, the muon and neutrino must move in opposite directions with equal momentum magnitude. For a massless neutrino, its energy equals its momentum (E_nu = p, in natural units where c=1). For the muon, its total energy combines its rest mass energy and kinetic energy.

By energy conservation: the pion's rest energy (139.6 MeV) equals the sum of the muon's and neutrino's energies. This gives us:
sqrt(p² + m_mu²) + p = m_pi

Where p is the momentum magnitude of both particles.

Rearranging to isolate p:
sqrt(p² + m_mu²) = m_pi - p
p² + m_mu² = (m_pi - p)²
p² + m_mu² = m_pi² - 2m_pi·p + p²
m_mu² = m_pi² - 2m_pi·p
p = (m_pi² - m_mu²)/(2m_pi)

Substituting the values:
p = (139.6² - 105.7²)/(2×139.6)
p = (19488.16 - 11172.49)/279.2
p = 8315.67/279.2
p ≈ 29.784 MeV

The muon's total energy is:
E_mu = sqrt(p² + m_mu²)
E_mu = sqrt(29.784² + 105.7²)
E_mu = sqrt(887.09 + 11172.49)
E_mu = sqrt(12059.58)
E_mu ≈ 109.8 MeV

Therefore, the muon's kinetic energy is:
KE_mu = E_mu - m_mu = 109.8 MeV - 105.7 MeV ≈ 4.1 MeV

The neutrino's energy, being massless, is equal to its momentum: 29.784 MeV, which is all kinetic energy.

---

# OpenAI completion

Alright, let me go through the steps to find the kinetic energy of the product particles when a positive pion (Pi+) decays into a positive muon (mu+) and a neutrino (nu), starting with the pion at rest. Initially, the pion’s momentum is zero because it is stationary. The rest masses are 139.6 MeV for the pion and 105.7 MeV for the muon, and we will assume the neutrino is massless for simplicity, as is common in many problems at this level.

The conservation of momentum dictates that the momenta of the muon and neutrino must be equal in magnitude but opposite in direction post-decay. The neutrino, being massless, has energy equal to its momentum. For the muon, its total energy includes its rest mass energy plus kinetic energy.

Using conservation of energy, the initial energy (the rest energy of the pion) is 139.6 MeV. After decay, the total energy is the sum of the muon's and neutrino's energies. Momentum conservation means the muon's and neutrino's momenta are equal in magnitude. Let's denote the magnitude of their momentum as p, giving the neutrino energy as E_nu = p and the muon energy as E_mu = sqrt(p^2 + m_mu^2). 

The energy conservation equation becomes:

sqrt(p^2 + (105.7)^2) + p = 139.6

Rearranging and solving for p:

sqrt(p^2 + m_mu^2) = m_pi - p

Square both sides:

p^2 + m_mu^2 = (m_pi - p)^2

Expanding gives:

p^2 + m_mu^2 = m_pi^2 - 2*m_pi*p + p^2

Subtract p^2 from each side:

m_mu^2 = m_pi^2 - 2*m_pi*p

Solve for p:

2*m_pi*p = m_pi^2 - m_mu^2

p = (m_pi^2 - m_mu^2) / (2*m_pi)

Calculate using the numbers:

m_pi = 139.6 MeV
m_mu = 105.7 MeV

Numerator: 139.6^2 - 105.7^2
= 19488.16 MeV² - 11172.49 MeV²
= 8315.67 MeV²

Denominator: 2 * 139.6 = 279.2 MeV

So, p = 8315.67 / 279.2 ≈ 29.784 MeV

Hence, the muon’s energy is:

E_mu = sqrt(p^2 + m_mu^2) ≈ sqrt(29.784^2 + 105.7^2) ≈ sqrt(12059.5766) ≈ 109.8 MeV

Thus, the muon’s kinetic energy is:

E_mu - m_mu = 109.8 MeV - 105.7 MeV ≈ 4.1 MeV

---

# cutoff_deepseek_completion (via openrouter)

ChatCompletion(id='gen-1745385805-UZNEAfkcxNOoj7hqPdQi', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='To find the kinetic energy of the product particles in the decay \\(\\pi^+ \\to \\mu^+ + \\nu\\) where the pion is stationary, we use conservation of energy and momentum. The rest masses are \\(m_{\\pi} = 139.6 \\, \\text{MeV}\\) and \\(m_{\\mu} = 105.7 \\, \\text{MeV}\\), and the neutrino is considered massless.\n\n1. **Conservation of Energy**:\n   \\[\n   E_{\\mu} + E_{\\nu} = m_{\\pi}\n   \\]\n   where \\(E_{\\mu} = \\sqrt{p^2 + m_{\\mu}^2}\\) and \\(E_{\\nu} = p\\) (since the neutrino is massless).\n\n2. **Conservation of Momentum**:\n   \\[\n   p_{\\mu} = p_{\\nu} = p\n   \\]\n\n3. **Substitute and Solve for \\(p\\)**:\n   \\[\n   \\sqrt{p^2 + m_{\\mu}^2} + p = m_{\\pi}\n   \\]\n   Rearrange and square both sides:\n   \\[\n   \\sqrt{p^2 + m_{\\mu}^2} = m_{\\pi} - p\n   \\]\n   \\[\n   p^2 + m_{\\mu}^2 = (m_{\\pi} - p)^2\n   \\]\n   Expand and simplify:\n   \\[\n   p^2 + m_{\\mu}^2 = m_{\\pi}^2 - 2m_{\\pi}p + p^2\n   \\]\n   \\[\n   m_{\\mu}^2 = m_{\\pi}^2 - 2m_{\\pi}p\n   \\]\n   Solve for \\(p\\):\n   \\[\n   p = \\frac{m_{\\pi}^2 - m_{\\mu}^2}{2m_{\\pi}}\n   \\]\n\n4. **Calculate \\(p\\)**:\n   \\[\n   p = \\frac{139.6^2 - 105.7^2}{2 \\times 139.6}\n   \\]\n   \\[\n   p = \\frac{19488.16 - 11172.49}{279.2} \\approx \\frac{8315.67}{279.2} \\approx 29.78 \\, \\text{MeV}\n   \\]\n\n5. **Energy of the Muon**:\n   \\[\n   E_{\\mu} = \\sqrt{p^2 + m_{\\mu}^2} = \\sqrt{29.78^2 + 105.7^2} \\approx 109.8 \\, \\text{MeV}\n   \\]\n\n6. **Kinetic Energy of the Muon**:\n   \\[\n   KE_{\\mu} = E_{\\mu} - m_{\\mu} = 109.8 - 105.7 = 4.1 \\, \\text{MeV}\n   \\]\n\nThus, the kinetic energy of the muon is \\(\\boxed{4.1 \\text{ MeV}}\\).', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, reasoning=".57²)/ (2*139.6). Wait, no, we had:\n\np = (139.6² - 105.7²)/(2*139.6). Let me compute this more accurately.\n\nCompute numerator: 139.6² - 105.7².\n\n139.6² = (140 - 0.4)^2 = 140² - 2*140*0.4 + 0.4² = 19600 - 112 + 0.16 = 19488.16\n\n105.7² = (100 + 5.7)^2 = 100² + 2*100*5.7 + 5.7² = 10000 + 1140 + 32.49 = 11172.49\n\nSo numerator: 19488.16 - 11172.49 = 8315.67\n\nDenominator: 2*139.6 = 279.2\n\nSo p = 8315.67 / 279.2\n\nLet me compute this division more accurately.\n\n8315.67 ÷ 279.2.\n\nFirst, 279.2 * 29 = 8096.8 (since 279.2*30 = 8376, subtract 279.2 to get 8376 - 279.2 = 8096.8)\n\nDifference: 8315.67 - 8096.8 = 218.87\n\nNow, 279.2 * 0.7 = 195.44\n\n218.87 - 195.44 = 23.43\n\n279.2 * 0.08 = 22.336\n\n23.43 - 22.336 = 1.094\n\n279.2 * 0.0039 ≈ 1.08888\n\nSo total p ≈ 29 + 0.7 + 0.08 + 0.0039 ≈ 29.7839 MeV\n\nSo p ≈ 29.7839 MeV\n\nThen E_mu = sqrt(p² + m_mu²) = sqrt(29.7839² + 105.7²)\n\nCompute 29.7839²:\n\n29.7839 * 29.7839\n\nApproximately, 29.7839^2 = (30 - 0.2161)^2 = 900 - 2*30*0.2161 + 0.2161^2 ≈ 900 - 12.966 + 0.0467 ≈ 887.0807\n\nThen 887.0807 + 105.7^2 = 887.0807 + 11172.49 = 12059.5707\n\nsqrt(12059.5707) = let's compute this.\n\nWe know that 109.8^2 = (110 - 0.2)^2 = 12100 - 44 + 0.04 = 12056.04\n\nCompare to 12059.5707, which is 3.5307 higher.\n\nThe difference between 109.8^2 and 109.81^2:\n\n(109.8 + 0.01)^2 = 109.8^2 + 2*109.8*0.01 + 0.01^2 = 12056.04 + 2.196 + 0.0001 = 12058.2361\n\nStill less than 12059.5707. Then 109.82^2:\n\n109.8 + 0.02 = 109.82\n\n(109.82)^2 = (109.8)^2 + 2*109.8*0.02 + 0.02^2 = 12056.04 + 4.392 + 0.0004 = 12060.4324\n\nThat's higher than 12059.5707. So sqrt(12059.5707) is between 109.81 and 109.82.\n\nCompute 109.81^2 = 12058.2361\n\nDifference: 12059.5707 - 12058.2361 = 1.3346\n\nLinear approximation: between 109.81 and 109.82, the difference in x is 0.01, difference in y is 12060.4324 - 12058.2361 = 2.1963\n\nSo to cover 1.3346, need 1.3346 / 2.1963 ≈ 0.6076 of the interval. So sqrt ≈ 109.81 + 0.6076*0.01 ≈ 109.81 + 0.006076 ≈ 109.816076\n\nSo approximately 109.816 MeV\n\nTherefore, E_mu ≈ 109.816 MeV\n\nThen, the kinetic energy KE_mu = E_mu - m_mu = 109.816 - 105.7 = 4.116 MeV\n\nSo approximately 4.116 MeV. Let's check if this is precise enough.\n\nAlternatively, maybe we can compute this more accurately.\n\nAlternatively, since E_mu = (m_pi² + m_mu²)/(2 m_pi). Wait, is that true?\n\nWait, from conservation of energy and momentum, we had:\n\nE_mu + E_nu = m_pi\n\nAnd from momentum conservation, |p_mu| = |p_nu| = p\n\nBut E_nu = p (since it's massless)\n\nSo E_mu = sqrt(p² + m_mu²)\n\nThus, substituting into energy equation:\n\nsqrt(p² + m_mu²) + p = m_pi\n\nThen, as we did before, solving for p gives p = (m_pi² - m_mu²)/(2 m_pi)\n\nThen, E_mu = sqrt( p² + m_mu² ) = sqrt( [(m_pi² - m_mu²)^2/(4 m_pi²)] + m_mu² )\n\n= sqrt( (m_pi^4 - 2 m_pi² m_mu² + m_mu^4 + 4 m_pi² m_mu² ) / (4 m_pi²) )\n\n= sqrt( (m_pi^4 + 2 m_pi² m_mu² + m_mu^4 ) / (4 m_pi²) )\n\nWait, numerator is (m_pi² + m_mu²)^2\n\nSo sqrt( (m_pi² + m_mu²)^2 / (4 m_pi²) ) = (m_pi² + m_mu²)/(2 m_pi)\n\nTherefore, E_mu = (m_pi² + m_mu²)/(2 m_pi)\n\nSo KE_mu = E_mu - m_mu = [ (m_pi² + m_mu²)/(2 m_pi) ] - m_mu\n\n= (m_pi² + m_mu² - 2 m_pi m_mu ) / (2 m_pi )\n\n= [ (m_pi - m_mu )^2 + 2 m_pi m_mu - 2 m_pi m_mu ] / (2 m_pi )\n\nWait, no, expanding (m_pi - m_mu)^2 = m_pi² - 2 m_pi m_mu + m_mu², so m_pi² + m_mu² = (m_pi - m_mu)^2 + 2 m_pi m_mu\n\nTherefore, KE_mu = [ (m_pi - m_mu)^2 + 2 m_pi m_mu - 2 m_pi m_mu ] / (2 m_pi ) = (m_pi - m_mu)^2 / (2 m_pi )\n\nSo KE_mu = (m_pi - m_mu)^2 / (2 m_pi )\n\nThat's a useful formula. Let me compute that.\n\nGiven m_pi = 139.6 MeV, m_mu = 105.7 MeV\n\n(m_pi - m_mu) = 139.6 - 105.7 = 33.9 MeV\n\nSo (33.9)^2 = 1149.21\n\nDivide by 2 m_pi: 1149.21 / (2 * 139.6) = 1149.21 / 279.2 ≈ 4.116 MeV\n\nWhich matches our previous result. So that's a more straightforward way. Therefore, the kinetic energy of the muon is approximately 4.116 MeV.\n\nSince the problem gives the rest masses to one decimal place, maybe we should present the answer to the same precision. Let's compute (33.9)^2:\n\n33.9 * 33.9\n\n33 * 33 = 1089\n\n33 * 0.9 = 29.7\n\n0.9 * 33 = 29.7\n\n0.9 * 0.9 = 0.81\n\nSo (33 + 0.9)^2 = 33² + 2*33*0.9 + 0.9² = 1089 + 59.4 + 0.81 = 1149.21\n\nDivide by 2*139.6 = 279.2\n\n1149.21 / 279.2 ≈ Let's compute 279.2 * 4 = 1116.8\n\n1149.21 - 1116.8 = 32.41\n\n32.41 / 279.2 ≈ 0.116\n\nSo total KE ≈ 4.116 MeV, so approximately 4.1 MeV when rounded to one decimal place.\n\nBut let me check if the given rest masses are 139.6 and 105.7, which are to one decimal place. So maybe the answer should be given to one decimal place. However, 4.116 is approximately 4.12, which would be 4.1 MeV. But sometimes in these problems, they might expect more decimal places. Let's check using exact computation.\n\nAlternatively, let's compute (139.6 - 105.7) = 33.9\n\n33.9 squared is 33.9 * 33.9:\n\nFirst, 30*30 = 900\n\n30*3.9 = 117\n\n3.9*30 = 117\n\n3.9*3.9 = 15.21\n\nSo total is 900 + 117 + 117 + 15.21 = 900 + 234 + 15.21 = 1149.21\n\nDivide by 2*139.6 = 279.2\n\n1149.21 / 279.2: Let's compute this division more precisely.\n\n279.2 * 4 = 1116.8\n\n1149.21 - 1116.8 = 32.41\n\nNow, 32.41 / 279.2 = 0.1161 (since 279.2 * 0.1 = 27.92, 279.2 * 0.01 = 2.792, 279.2 * 0.006 = 1.6752, 279.2 * 0.0001 = 0.02792)\n\nSo 0.1: 27.92\n\n0.01: 2.792, total 0.11: 30.712\n\nBut we have 32.41. So 32.41 - 30.712 = 1.698\n\nNow, 279.2 * 0.006 = 1.6752\n\n1.698 - 1.6752 = 0.0228\n\n0.0008 * 279.2 ≈ 0.22336\n\nSo total is 0.1 + 0.01 + 0.006 + 0.0008 ≈ 0.1168, with a remainder of 0.0228 - 0.22336*0.1 ≈ ?\n\nWait, this is getting too detailed. Alternatively, 32.41 / 279.2 ≈ 0.1161\n\nSo total KE ≈ 4.1161 MeV ≈ 4.12 MeV. So depending on the required precision, maybe 4.1 MeV or 4.12 MeV.\n\nBut given that the rest masses are given to one decimal place, perhaps the answer should be 4.1 MeV. However, let's check with exact values.\n\nAlternatively, let's compute using more precise steps.\n\nFrom KE = (m_pi - m_mu)^2 / (2 m_pi )\n\n= (33.9)^2 / (2 * 139.6)\n\n= 1149.21 / 279.2\n\nLet me perform the division:\n\n1149.21 ÷ 279.2\n\nLet me move the decimal to make it easier: 11492.1 ÷ 2792\n\nLet me approximate 2792 * 4 = 11168\n\n11492.1 - 11168 = 324.1\n\nNow, 2792 * 0.116 ≈ 2792 * 0.1 = 279.2; 2792 * 0.01 = 27.92; 2792 * 0.006 = 16.752\n\nSo 0.1 + 0.01 + 0.006 = 0.116, total 279.2 + 27.92 + 16.752 = 323.872\n\nWhich is very close to 324.1. The difference is 324.1 - 323.872 = 0.228\n\nSo 0.228 / 2792 ≈ 0.0000816\n\nSo the total is approximately 4.116 + 0.0000816 ≈ 4.1160816 MeV\n\nSo approximately 4.116 MeV. So rounding to two decimal places, 4.12 MeV, or to one decimal, 4.1 MeV.\n\nBut in exams, sometimes they want an exact fraction. Let me check the exact value.\n\nWait, 1149.21 / 279.2. Let's write this as 114921 / 27920\n\nDivide numerator and denominator by 10: 11492.1 / 2792\n\nBut maybe we can divide numerator and denominator by something else. Let's see if 279.2 and 1149.21 have a common factor.\n\nBut 279.2 is 2792/10, and 1149.21 is 114921/100. Not obvious. Maybe decimal fractions are okay.\n\nAlternatively, use calculator approximation: 1149.21 / 279.2 ≈ 4.116 MeV.\n\nTherefore, the kinetic energy of the muon is approximately 4.12 MeV. Depending on the problem's requirement, but since the given masses are in one decimal place, 4.1 MeV is acceptable. However, in particle physics, sometimes these values are known more precisely. Let me check with the exact formula.\n\nAlternatively, perhaps there's a miscalculation. Let me verify the formula again.\n\nWe had KE_mu = (m_pi - m_mu)^2 / (2 m_pi )\n\nYes, that's correct. Because:\n\nFrom conservation of energy and momentum, we derived that the kinetic energy of the muon is (m_pi - m_mu)^2 / (2 m_pi )\n\nSo plugging in the numbers:\n\n(139.6 - 105.7)^2 / (2 * 139.6 ) = (33.9)^2 / 279.2 ≈ 1149.21 / 279.2 ≈ 4.116 MeV\n\nSo yes, 4.116 MeV is the precise value, which is approximately 4.12 MeV. If we want to keep two decimal places, 4.12 MeV. But given that the rest masses are given to one decimal, maybe 4.1 MeV is acceptable. However, in some textbooks, this particular decay is a standard problem, and the KE is known to be approximately 4.1 MeV. Let me check with another approach.\n\nAlternatively, using relativistic kinematics:\n\nThe total energy of the muon is E_mu = gamma m_mu c², and the neutrino's energy is E_nu = p_nu c.\n\nFrom conservation of momentum, p_mu = p_nu = p.\n\nSo:\n\nE_mu = sqrt( p² c² + m_mu² c^4 ) / c² ?\n\nWait, no. Wait, in units where c=1, E_mu = sqrt( p² + m_mu² ), and E_nu = p.\n\nBut if we don't use natural units, then:\n\nTotal energy: E_mu + E_nu = m_pi c²\n\nMomentum conservation: p_mu = p_nu = p\n\nSo:\n\nE_mu = sqrt( p² c² + m_mu² c^4 ) / c² ?\n\nWait, no. Wait, the energy of the muon is sqrt( p² c² + m_mu² c⁴ ), and the energy of the neutrino is p c.\n\nTherefore:\n\nsqrt( p² c² + m_mu² c⁴ ) + p c = m_pi c²\n\nDivide both sides by c²:\n\nsqrt( p² / c² + m_mu² ) + p / c = m_pi\n\nWait, this is getting confusing. Maybe better to keep using natural units where c=1. Since in natural units, the equation is as before.\n\nBut regardless, the result is the same. Therefore, the kinetic energy is approximately 4.12 MeV.\n\nBut to check, let me recall that the rest mass of the pion is 139.6 MeV, muon is 105.7 MeV. The neutrino is negligible. So the available energy is 139.6 - 105.7 = 33.9 MeV. But that's not the kinetic energy. Wait, the available energy for kinetic energy is the total energy minus the rest mass of the muon, but since the neutrino also carries away energy, it's not just 33.9 MeV.\n\nBut according to our calculation, the kinetic energy is about 4.1 MeV, which is much less than 33.9 MeV. That makes sense because the neutrino carries away most of the energy. Since the muon is much heavier than the neutrino (which is massless), the muon gets a small portion of the kinetic energy. So 4.1 MeV seems reasonable.\n\nAlternatively, if both particles were massive, the kinetic energy would be split between them, but since the neutrino is massless, it takes the majority of the energy. Wait, but since momentum must be equal and opposite, and the neutrino's energy is p, while the muon's energy is sqrt(p² + m_mu²), so even though the muon is heavier, the kinematics require that the muon's energy is only slightly larger than its rest mass, hence small kinetic energy.\n\nYes, so 4.1 MeV is correct.\n\nTherefore, the answer should be \\boxed{4.1 \\text{ MeV}}.\n\n\n**Final Answer**\nThe kinetic energy of the muon is \\boxed{4.1 \\text{ MeV}}.\n"), native_finish_reason='stop')], created=1745385805, model='deepseek/deepseek-r1', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=4690, prompt_tokens=2141, total_tokens=6831, completion_tokens_details=None, prompt_tokens_details=None), provider='Nebius')

---

# cutoff_deepseek_completion response

To find the kinetic energy of the product particles in the decay \(\pi^+ \to \mu^+ + \nu\) where the pion is stationary, we use conservation of energy and momentum. The rest masses are \(m_{\pi} = 139.6 \, \text{MeV}\) and \(m_{\mu} = 105.7 \, \text{MeV}\), and the neutrino is considered massless.

1. **Conservation of Energy**:
   \[
   E_{\mu} + E_{\nu} = m_{\pi}
   \]
   where \(E_{\mu} = \sqrt{p^2 + m_{\mu}^2}\) and \(E_{\nu} = p\) (since the neutrino is massless).

2. **Conservation of Momentum**:
   \[
   p_{\mu} = p_{\nu} = p
   \]

3. **Substitute and Solve for \(p\)**:
   \[
   \sqrt{p^2 + m_{\mu}^2} + p = m_{\pi}
   \]
   Rearrange and square both sides:
   \[
   \sqrt{p^2 + m_{\mu}^2} = m_{\pi} - p
   \]
   \[
   p^2 + m_{\mu}^2 = (m_{\pi} - p)^2
   \]
   Expand and simplify:
   \[
   p^2 + m_{\mu}^2 = m_{\pi}^2 - 2m_{\pi}p + p^2
   \]
   \[
   m_{\mu}^2 = m_{\pi}^2 - 2m_{\pi}p
   \]
   Solve for \(p\):
   \[
   p = \frac{m_{\pi}^2 - m_{\mu}^2}{2m_{\pi}}
   \]

4. **Calculate \(p\)**:
   \[
   p = \frac{139.6^2 - 105.7^2}{2 \times 139.6}
   \]
   \[
   p = \frac{19488.16 - 11172.49}{279.2} \approx \frac{8315.67}{279.2} \approx 29.78 \, \text{MeV}
   \]

5. **Energy of the Muon**:
   \[
   E_{\mu} = \sqrt{p^2 + m_{\mu}^2} = \sqrt{29.78^2 + 105.7^2} \approx 109.8 \, \text{MeV}
   \]

6. **Kinetic Energy of the Muon**:
   \[
   KE_{\mu} = E_{\mu} - m_{\mu} = 109.8 - 105.7 = 4.1 \, \text{MeV}
   \]

Thus, the kinetic energy of the muon is \(\boxed{4.1 \text{ MeV}}\).

---

# cutoff_deepseek_completion reasoning

.57²)/ (2*139.6). Wait, no, we had:

p = (139.6² - 105.7²)/(2*139.6). Let me compute this more accurately.

Compute numerator: 139.6² - 105.7².

139.6² = (140 - 0.4)^2 = 140² - 2*140*0.4 + 0.4² = 19600 - 112 + 0.16 = 19488.16

105.7² = (100 + 5.7)^2 = 100² + 2*100*5.7 + 5.7² = 10000 + 1140 + 32.49 = 11172.49

So numerator: 19488.16 - 11172.49 = 8315.67

Denominator: 2*139.6 = 279.2

So p = 8315.67 / 279.2

Let me compute this division more accurately.

8315.67 ÷ 279.2.

First, 279.2 * 29 = 8096.8 (since 279.2*30 = 8376, subtract 279.2 to get 8376 - 279.2 = 8096.8)

Difference: 8315.67 - 8096.8 = 218.87

Now, 279.2 * 0.7 = 195.44

218.87 - 195.44 = 23.43

279.2 * 0.08 = 22.336

23.43 - 22.336 = 1.094

279.2 * 0.0039 ≈ 1.08888

So total p ≈ 29 + 0.7 + 0.08 + 0.0039 ≈ 29.7839 MeV

So p ≈ 29.7839 MeV

Then E_mu = sqrt(p² + m_mu²) = sqrt(29.7839² + 105.7²)

Compute 29.7839²:

29.7839 * 29.7839

Approximately, 29.7839^2 = (30 - 0.2161)^2 = 900 - 2*30*0.2161 + 0.2161^2 ≈ 900 - 12.966 + 0.0467 ≈ 887.0807

Then 887.0807 + 105.7^2 = 887.0807 + 11172.49 = 12059.5707

sqrt(12059.5707) = let's compute this.

We know that 109.8^2 = (110 - 0.2)^2 = 12100 - 44 + 0.04 = 12056.04

Compare to 12059.5707, which is 3.5307 higher.

The difference between 109.8^2 and 109.81^2:

(109.8 + 0.01)^2 = 109.8^2 + 2*109.8*0.01 + 0.01^2 = 12056.04 + 2.196 + 0.0001 = 12058.2361

Still less than 12059.5707. Then 109.82^2:

109.8 + 0.02 = 109.82

(109.82)^2 = (109.8)^2 + 2*109.8*0.02 + 0.02^2 = 12056.04 + 4.392 + 0.0004 = 12060.4324

That's higher than 12059.5707. So sqrt(12059.5707) is between 109.81 and 109.82.

Compute 109.81^2 = 12058.2361

Difference: 12059.5707 - 12058.2361 = 1.3346

Linear approximation: between 109.81 and 109.82, the difference in x is 0.01, difference in y is 12060.4324 - 12058.2361 = 2.1963

So to cover 1.3346, need 1.3346 / 2.1963 ≈ 0.6076 of the interval. So sqrt ≈ 109.81 + 0.6076*0.01 ≈ 109.81 + 0.006076 ≈ 109.816076

So approximately 109.816 MeV

Therefore, E_mu ≈ 109.816 MeV

Then, the kinetic energy KE_mu = E_mu - m_mu = 109.816 - 105.7 = 4.116 MeV

So approximately 4.116 MeV. Let's check if this is precise enough.

Alternatively, maybe we can compute this more accurately.

Alternatively, since E_mu = (m_pi² + m_mu²)/(2 m_pi). Wait, is that true?

Wait, from conservation of energy and momentum, we had:

E_mu + E_nu = m_pi

And from momentum conservation, |p_mu| = |p_nu| = p

But E_nu = p (since it's massless)

So E_mu = sqrt(p² + m_mu²)

Thus, substituting into energy equation:

sqrt(p² + m_mu²) + p = m_pi

Then, as we did before, solving for p gives p = (m_pi² - m_mu²)/(2 m_pi)

Then, E_mu = sqrt( p² + m_mu² ) = sqrt( [(m_pi² - m_mu²)^2/(4 m_pi²)] + m_mu² )

= sqrt( (m_pi^4 - 2 m_pi² m_mu² + m_mu^4 + 4 m_pi² m_mu² ) / (4 m_pi²) )

= sqrt( (m_pi^4 + 2 m_pi² m_mu² + m_mu^4 ) / (4 m_pi²) )

Wait, numerator is (m_pi² + m_mu²)^2

So sqrt( (m_pi² + m_mu²)^2 / (4 m_pi²) ) = (m_pi² + m_mu²)/(2 m_pi)

Therefore, E_mu = (m_pi² + m_mu²)/(2 m_pi)

So KE_mu = E_mu - m_mu = [ (m_pi² + m_mu²)/(2 m_pi) ] - m_mu

= (m_pi² + m_mu² - 2 m_pi m_mu ) / (2 m_pi )

= [ (m_pi - m_mu )^2 + 2 m_pi m_mu - 2 m_pi m_mu ] / (2 m_pi )

Wait, no, expanding (m_pi - m_mu)^2 = m_pi² - 2 m_pi m_mu + m_mu², so m_pi² + m_mu² = (m_pi - m_mu)^2 + 2 m_pi m_mu

Therefore, KE_mu = [ (m_pi - m_mu)^2 + 2 m_pi m_mu - 2 m_pi m_mu ] / (2 m_pi ) = (m_pi - m_mu)^2 / (2 m_pi )

So KE_mu = (m_pi - m_mu)^2 / (2 m_pi )

That's a useful formula. Let me compute that.

Given m_pi = 139.6 MeV, m_mu = 105.7 MeV

(m_pi - m_mu) = 139.6 - 105.7 = 33.9 MeV

So (33.9)^2 = 1149.21

Divide by 2 m_pi: 1149.21 / (2 * 139.6) = 1149.21 / 279.2 ≈ 4.116 MeV

Which matches our previous result. So that's a more straightforward way. Therefore, the kinetic energy of the muon is approximately 4.116 MeV.

Since the problem gives the rest masses to one decimal place, maybe we should present the answer to the same precision. Let's compute (33.9)^2:

33.9 * 33.9

33 * 33 = 1089

33 * 0.9 = 29.7

0.9 * 33 = 29.7

0.9 * 0.9 = 0.81

So (33 + 0.9)^2 = 33² + 2*33*0.9 + 0.9² = 1089 + 59.4 + 0.81 = 1149.21

Divide by 2*139.6 = 279.2

1149.21 / 279.2 ≈ Let's compute 279.2 * 4 = 1116.8

1149.21 - 1116.8 = 32.41

32.41 / 279.2 ≈ 0.116

So total KE ≈ 4.116 MeV, so approximately 4.1 MeV when rounded to one decimal place.

But let me check if the given rest masses are 139.6 and 105.7, which are to one decimal place. So maybe the answer should be given to one decimal place. However, 4.116 is approximately 4.12, which would be 4.1 MeV. But sometimes in these problems, they might expect more decimal places. Let's check using exact computation.

Alternatively, let's compute (139.6 - 105.7) = 33.9

33.9 squared is 33.9 * 33.9:

First, 30*30 = 900

30*3.9 = 117

3.9*30 = 117

3.9*3.9 = 15.21

So total is 900 + 117 + 117 + 15.21 = 900 + 234 + 15.21 = 1149.21

Divide by 2*139.6 = 279.2

1149.21 / 279.2: Let's compute this division more precisely.

279.2 * 4 = 1116.8

1149.21 - 1116.8 = 32.41

Now, 32.41 / 279.2 = 0.1161 (since 279.2 * 0.1 = 27.92, 279.2 * 0.01 = 2.792, 279.2 * 0.006 = 1.6752, 279.2 * 0.0001 = 0.02792)

So 0.1: 27.92

0.01: 2.792, total 0.11: 30.712

But we have 32.41. So 32.41 - 30.712 = 1.698

Now, 279.2 * 0.006 = 1.6752

1.698 - 1.6752 = 0.0228

0.0008 * 279.2 ≈ 0.22336

So total is 0.1 + 0.01 + 0.006 + 0.0008 ≈ 0.1168, with a remainder of 0.0228 - 0.22336*0.1 ≈ ?

Wait, this is getting too detailed. Alternatively, 32.41 / 279.2 ≈ 0.1161

So total KE ≈ 4.1161 MeV ≈ 4.12 MeV. So depending on the required precision, maybe 4.1 MeV or 4.12 MeV.

But given that the rest masses are given to one decimal place, perhaps the answer should be 4.1 MeV. However, let's check with exact values.

Alternatively, let's compute using more precise steps.

From KE = (m_pi - m_mu)^2 / (2 m_pi )

= (33.9)^2 / (2 * 139.6)

= 1149.21 / 279.2

Let me perform the division:

1149.21 ÷ 279.2

Let me move the decimal to make it easier: 11492.1 ÷ 2792

Let me approximate 2792 * 4 = 11168

11492.1 - 11168 = 324.1

Now, 2792 * 0.116 ≈ 2792 * 0.1 = 279.2; 2792 * 0.01 = 27.92; 2792 * 0.006 = 16.752

So 0.1 + 0.01 + 0.006 = 0.116, total 279.2 + 27.92 + 16.752 = 323.872

Which is very close to 324.1. The difference is 324.1 - 323.872 = 0.228

So 0.228 / 2792 ≈ 0.0000816

So the total is approximately 4.116 + 0.0000816 ≈ 4.1160816 MeV

So approximately 4.116 MeV. So rounding to two decimal places, 4.12 MeV, or to one decimal, 4.1 MeV.

But in exams, sometimes they want an exact fraction. Let me check the exact value.

Wait, 1149.21 / 279.2. Let's write this as 114921 / 27920

Divide numerator and denominator by 10: 11492.1 / 2792

But maybe we can divide numerator and denominator by something else. Let's see if 279.2 and 1149.21 have a common factor.

But 279.2 is 2792/10, and 1149.21 is 114921/100. Not obvious. Maybe decimal fractions are okay.

Alternatively, use calculator approximation: 1149.21 / 279.2 ≈ 4.116 MeV.

Therefore, the kinetic energy of the muon is approximately 4.12 MeV. Depending on the problem's requirement, but since the given masses are in one decimal place, 4.1 MeV is acceptable. However, in particle physics, sometimes these values are known more precisely. Let me check with the exact formula.

Alternatively, perhaps there's a miscalculation. Let me verify the formula again.

We had KE_mu = (m_pi - m_mu)^2 / (2 m_pi )

Yes, that's correct. Because:

From conservation of energy and momentum, we derived that the kinetic energy of the muon is (m_pi - m_mu)^2 / (2 m_pi )

So plugging in the numbers:

(139.6 - 105.7)^2 / (2 * 139.6 ) = (33.9)^2 / 279.2 ≈ 1149.21 / 279.2 ≈ 4.116 MeV

So yes, 4.116 MeV is the precise value, which is approximately 4.12 MeV. If we want to keep two decimal places, 4.12 MeV. But given that the rest masses are given to one decimal, maybe 4.1 MeV is acceptable. However, in some textbooks, this particular decay is a standard problem, and the KE is known to be approximately 4.1 MeV. Let me check with another approach.

Alternatively, using relativistic kinematics:

The total energy of the muon is E_mu = gamma m_mu c², and the neutrino's energy is E_nu = p_nu c.

From conservation of momentum, p_mu = p_nu = p.

So:

E_mu = sqrt( p² c² + m_mu² c^4 ) / c² ?

Wait, no. Wait, in units where c=1, E_mu = sqrt( p² + m_mu² ), and E_nu = p.

But if we don't use natural units, then:

Total energy: E_mu + E_nu = m_pi c²

Momentum conservation: p_mu = p_nu = p

So:

E_mu = sqrt( p² c² + m_mu² c^4 ) / c² ?

Wait, no. Wait, the energy of the muon is sqrt( p² c² + m_mu² c⁴ ), and the energy of the neutrino is p c.

Therefore:

sqrt( p² c² + m_mu² c⁴ ) + p c = m_pi c²

Divide both sides by c²:

sqrt( p² / c² + m_mu² ) + p / c = m_pi

Wait, this is getting confusing. Maybe better to keep using natural units where c=1. Since in natural units, the equation is as before.

But regardless, the result is the same. Therefore, the kinetic energy is approximately 4.12 MeV.

But to check, let me recall that the rest mass of the pion is 139.6 MeV, muon is 105.7 MeV. The neutrino is negligible. So the available energy is 139.6 - 105.7 = 33.9 MeV. But that's not the kinetic energy. Wait, the available energy for kinetic energy is the total energy minus the rest mass of the muon, but since the neutrino also carries away energy, it's not just 33.9 MeV.

But according to our calculation, the kinetic energy is about 4.1 MeV, which is much less than 33.9 MeV. That makes sense because the neutrino carries away most of the energy. Since the muon is much heavier than the neutrino (which is massless), the muon gets a small portion of the kinetic energy. So 4.1 MeV seems reasonable.

Alternatively, if both particles were massive, the kinetic energy would be split between them, but since the neutrino is massless, it takes the majority of the energy. Wait, but since momentum must be equal and opposite, and the neutrino's energy is p, while the muon's energy is sqrt(p² + m_mu²), so even though the muon is heavier, the kinematics require that the muon's energy is only slightly larger than its rest mass, hence small kinetic energy.

Yes, so 4.1 MeV is correct.

Therefore, the answer should be \boxed{4.1 \text{ MeV}}.


**Final Answer**
The kinetic energy of the muon is \boxed{4.1 \text{ MeV}}.

---

# paraphrased_deepseek_completion_anthropic (via openrouter)

ChatCompletion(id='gen-1745386037-7XcVk7wVFvMLu4z4uK4g', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="Given the decay of a stationary positive pion (\\(\\pi^+\\)) into a positive muon (\\(\\mu^+\\)) and a neutrino (\\(\\nu\\)), we need to find the kinetic energy of the product particles. The rest masses are \\(m_{\\pi^+} = 139.6 \\, \\text{MeV}\\) and \\(m_{\\mu^+} = 105.7 \\, \\text{MeV}\\). The neutrino is assumed to be massless.\n\n1. **Conservation of Momentum**: Since the pion is initially at rest, the total momentum after decay must be zero. The muon and neutrino must have equal and opposite momenta. Let \\(p\\) be the magnitude of the momentum of each particle.\n\n2. **Conservation of Energy**: The total energy of the system before and after the decay must be equal.\n   \\[\n   E_{\\pi^+} = E_{\\mu^+} + E_{\\nu}\n   \\]\n   where \\(E_{\\pi^+} = m_{\\pi^+}\\), \\(E_{\\mu^+} = \\sqrt{p^2 + m_{\\mu^+}^2}\\), and \\(E_{\\nu} = p\\) (since the neutrino is massless).\n\n3. **Solving for Momentum**:\n   \\[\n   \\sqrt{p^2 + m_{\\mu^+}^2} + p = m_{\\pi^+}\n   \\]\n   Squaring both sides and solving for \\(p\\):\n   \\[\n   p^2 + m_{\\mu^+}^2 = (m_{\\pi^+} - p)^2\n   \\]\n   \\[\n   p^2 + m_{\\mu^+}^2 = m_{\\pi^+}^2 - 2 m_{\\pi^+} p + p^2\n   \\]\n   \\[\n   m_{\\mu^+}^2 = m_{\\pi^+}^2 - 2 m_{\\pi^+} p\n   \\]\n   \\[\n   p = \\frac{m_{\\pi^+}^2 - m_{\\mu^+}^2}{2 m_{\\pi^+}}\n   \\]\n   Substituting the values:\n   \\[\n   p = \\frac{139.6^2 - 105.7^2}{2 \\times 139.6} \\approx \\frac{8315.67}{279.2} \\approx 29.784 \\, \\text{MeV}\n   \\]\n\n4. **Total Energy of the Muon**:\n   \\[\n   E_{\\mu^+} = \\sqrt{p^2 + m_{\\mu^+}^2} = \\sqrt{29.784^2 + 105.7^2} \\approx 109.8 \\, \\text{MeV}\n   \\]\n\n5. **Kinetic Energy of the Muon**:\n   \\[\n   KE_{\\mu^+} = E_{\\mu^+} - m_{\\mu^+} = 109.8 \\, \\text{MeV} - 105.7 \\, \\text{MeV} \\approx 4.1 \\, \\text{MeV}\n   \\]\n\nThe kinetic energy of the muon is \\(\\boxed{4.1 \\text{ MeV}}\\). The neutrino's kinetic energy is its total energy, which is \\(29.784 \\, \\text{MeV}\\), but the problem typically focuses on the muon's kinetic energy in such contexts.", refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, reasoning=' However, the question asks for the kinetic energy of the product particles. Since the neutrino\'s kinetic energy is 29.784 MeV and the muon\'s is ~4.1 MeV, but I need to check if the question wants both. Wait, the problem says "product particles," so perhaps both. But looking back, the original question says "Find KE of product particles in Pi+ → mu+ + nu". But neutrinos are typically considered to have negligible mass, so their KE is their total energy. However, the problem might be expecting just the muon\'s KE. Let me check the problem statement again. It says "Find KE of product particles," plural. So both mu+ and nu. But since neutrinos are hard to detect, maybe the answer refers to the muon\'s KE. However, in particle physics problems like this, when they ask for KE of the products, they usually expect the KE of the massive particle, as the neutrino\'s KE is considered but not measured. However, let me check the calculation again.\n\nAlternatively, perhaps the problem expects just the muon\'s KE. Let me verify the calculation steps again.\n\nWait, the total energy of the pion is 139.6 MeV. The muon\'s energy is 109.8 MeV, so its KE is 4.1 MeV. The neutrino\'s energy is 29.784 MeV. The sum of these energies is 109.8 + 29.784 ≈ 139.584 MeV, which is approximately equal to the pion\'s energy (139.6), considering rounding errors. So that checks out.\n\nHowever, maybe the problem is expecting the answer to be the KE of the muon, which is 4.1 MeV. Alternatively, if including the neutrino, but since the neutrino\'s KE is 29.784 MeV, but that\'s all its energy. However, in some contexts, the KE is energy minus rest mass, but since the neutrino\'s rest mass is zero, its KE is its total energy. But perhaps the problem just wants the KE of the muon. Let me check standard decay problems. For example, in pion decay at rest, the muon gets a certain KE, and the neutrino takes away the rest. So in standard textbooks, when they ask for the KE of the products in pion decay, they usually refer to the muon\'s KE. Let me confirm with a textbook formula.\n\nThe formula for the kinetic energy of the muon in pion decay at rest is:\n\nKE_mu = [(m_pi^2 + m_mu^2)/(2m_pi)] - m_mu\n\nWait, that\'s the same as the total energy of the muon minus its rest mass. Let me compute that:\n\n(m_pi^2 - m_mu^2)/(2m_pi) = [ (139.6^2 - 105.7^2) ] / (2*139.6) = same as p, which was 29.784 MeV. Wait, but the total energy of the muon is sqrt(p^2 + m_mu^2) = sqrt(29.784^2 + 105.7^2) ≈ 109.8 MeV, so KE is 109.8 - 105.7 = 4.1 MeV, which matches the previous calculation.\n\nAlternatively, let\'s use the formula:\n\nKE_mu = ( (m_pi - m_nu)^2 - m_mu^2 ) / (2m_pi )\n\nWait, but m_nu is zero, so:\n\nKE_mu = (m_pi^2 - m_mu^2)/(2m_pi) - m_mu + m_mu? Wait, maybe not. Let me think again.\n\nAlternatively, using energy conservation:\n\nE_mu + E_nu = m_pi\n\nBut E_nu = p, and E_mu = sqrt(p^2 + m_mu^2)\n\nThen,\n\nsqrt(p^2 + m_mu^2) + p = m_pi\n\nSolving for p:\n\nsqrt(p^2 + m_mu^2) = m_pi - p\n\nSquare both sides:\n\np^2 + m_mu^2 = m_pi^2 - 2 m_pi p + p^2\n\nCancel p^2:\n\nm_mu^2 = m_pi^2 - 2 m_pi p\n\nThen,\n\np = (m_pi^2 - m_mu^2)/(2 m_pi)\n\nWhich gives p = (139.6^2 - 105.7^2)/(2*139.6) ≈ 29.784 MeV\n\nThen, E_mu = sqrt(p^2 + m_mu^2) ≈ sqrt(29.784^2 + 105.7^2) ≈ 109.8 MeV\n\nSo KE_mu = 109.8 - 105.7 ≈ 4.1 MeV\n\nYes, that\'s correct. Therefore, the kinetic energy of the muon is approximately 4.1 MeV. The neutrino\'s kinetic energy is its total energy, which is 29.784 MeV, but since the problem asks for the KE of the product particles, maybe they want both. However, in many cases, especially in exams, when they ask for the KE in pion decay, they refer to the muon\'s KE. Let me check if the problem specifies "product particles" plural. The original problem says "Find KE of product particles in, Pi+ = mu+ + nu". So the products are mu+ and nu. But the neutrino\'s KE is its total energy, which is 29.784 MeV, but perhaps the answer expects both. However, since the problem gives the rest mass of the pion and muon, but not the neutrino, it\'s likely expecting the KE of the muon. Let me check the calculation once more to be sure.\n\nAlternatively, maybe I made a miscalculation in the arithmetic. Let me redo the calculation step by step.\n\nFirst, m_pi = 139.6 MeV, m_mu = 105.7 MeV.\n\nCalculating p = (m_pi² - m_mu²)/(2 m_pi)\n\nCompute numerator: 139.6² - 105.7²\n\n139.6 squared: 139.6 * 139.6. Let\'s compute:\n\n139.6 * 100 = 13,960\n\n139.6 * 30 = 4,188\n\n139.6 * 9.6 = 1,340.16\n\nAdding up: 13,960 + 4,188 = 18,148; 18,148 + 1,340.16 = 19,488.16 MeV²\n\n105.7 squared: 105.7 * 105.7\n\n100*100 = 10,000\n\n100*5.7 = 570\n\n5.7*100 = 570\n\n5.7*5.7 = 32.49\n\nSo (100+5.7)^2 = 10,000 + 2*570 + 32.49 = 10,000 + 1,140 + 32.49 = 11,172.49 MeV²\n\nSo numerator: 19,488.16 - 11,172.49 = 8,315.67 MeV²\n\nDenominator: 2 * 139.6 = 279.2 MeV\n\nSo p = 8,315.67 / 279.2 ≈ let\'s compute that.\n\nDivide 8,315.67 by 279.2:\n\n279.2 * 29 = 8,096.8\n\n279.2 * 30 = 8,376.0\n\n8,315.67 - 8,096.8 = 218.87\n\nSo 29 + (218.87 / 279.2) ≈ 29 + 0.784 ≈ 29.784 MeV/c (momentum units)\n\nSo p ≈ 29.784 MeV/c\n\nThen, the muon\'s total energy E_mu = sqrt(p² + m_mu²) = sqrt(29.784² + 105.7²)\n\nCompute 29.784²: approx 29.784*29.784. Let\'s compute 30² = 900, subtract (0.216)^2 and 2*30*0.216.\n\nBut perhaps exact calculation:\n\n29.784 * 29.784: 29^2 = 841, 0.784^2 ≈ 0.614, and cross terms 2*29*0.784 ≈ 45.472\n\nSo total ≈ 841 + 45.472 + 0.614 ≈ 887.086\n\nm_mu² = 105.7^2 = 11,172.49\n\nSo E_mu = sqrt(887.086 + 11,172.49) = sqrt(12,059.576) ≈ 109.8 MeV\n\nTherefore, KE_mu = 109.8 - 105.7 = 4.1 MeV\n\nThe neutrino\'s energy is p = 29.784 MeV, which, being massless, is entirely KE. So the total KE of the products is 4.1 + 29.784 ≈ 33.884 MeV. However, the problem states "Find KE of product particles," so if they are asking for both, that\'s the answer. But maybe the question is expecting the KE of the muon only. Let me check the problem statement again: "Find KE of product particles in, Pi(+) = mu(+) + nu here Pi(+) is stationary." So both particles. But in particle physics, when you\'re asked for the KE of the products in a decay where one particle is massless, sometimes they might just ask for the KE of the massive one, but the problem says "product particles," plural. However, neutrinos are rarely considered in KE terms because their rest mass is negligible (even though in reality they have tiny mass, but here we took it as zero). So in this case, since the neutrino\'s KE is its total energy (29.784 MeV), and the muon\'s KE is 4.1 MeV, the total KE would be 33.884 MeV. But wait, energy conservation: the pion\'s rest mass is 139.6 MeV. The total energy after decay is the sum of the muon\'s total energy (109.8 MeV) and the neutrino\'s energy (29.784 MeV), which adds up to 139.584 MeV, which is approximately 139.6 MeV, considering rounding, so that\'s correct. The total kinetic energy is the sum of the kinetic energies: 4.1 MeV (muon) + 29.784 MeV (neutrino) = 33.884 MeV. But the pion was at rest, so all the energy comes from its rest mass being converted into the rest mass of the muon and the kinetic energy of both products. Therefore, the total kinetic energy should be 139.6 MeV - 105.7 MeV = 33.9 MeV, which matches the sum of 4.1 + 29.784 ≈ 33.884 MeV. So that checks out.\n\nBut the problem says "Find KE of product particles," so maybe they want the total KE, which is 33.9 MeV. However, in typical problems like this, especially in textbooks, when a pion at rest decays into a muon and a neutrino, the question usually asks for the kinetic energy of the muon, which is around 4 MeV. Let me check an example. For instance, in the classic example of pion decay, the muon\'s kinetic energy is calculated using the formula [(m_pi^2 - m_mu^2)/(2 m_pi)] - m_mu, which gives around 4.1 MeV. The neutrino\'s energy is (m_pi^2 + m_mu^2)/(2 m_pi) ≈ 109.8 MeV, but that\'s not correct because the neutrino\'s energy is p = 29.784 MeV. Wait, no, that formula would be incorrect. Wait, perhaps I\'m mixing things up.\n\nWait, no. Let me clarify. The total energy of the muon is E_mu = sqrt(p^2 + m_mu^2). The neutrino\'s energy is E_nu = p. Then, from energy conservation:\n\nE_mu + E_nu = m_pi\n\nSo sqrt(p^2 + m_mu^2) + p = m_pi\n\nSolving gives p = (m_pi^2 - m_mu^2)/(2 m_pi)\n\nThen E_nu = p = (m_pi^2 - m_mu^2)/(2 m_pi)\n\nAnd E_mu = sqrt( [ (m_pi^2 - m_mu^2)/(2 m_pi) ]^2 + m_mu^2 )\n\nWhich simplifies to:\n\nsqrt( (m_pi^4 - 2 m_pi^2 m_mu^2 + m_mu^4)/(4 m_pi^2) + m_mu^2 )\n\n= sqrt( (m_pi^4 - 2 m_pi^2 m_mu^2 + m_mu^4 + 4 m_pi^2 m_mu^2 ) / (4 m_pi^2) )\n\n= sqrt( (m_pi^4 + 2 m_pi^2 m_mu^2 + m_mu^4 ) / (4 m_pi^2) )\n\n= sqrt( (m_pi^2 + m_mu^2)^2 / (4 m_pi^2) )\n\n= (m_pi^2 + m_mu^2)/(2 m_pi)\n\nSo E_mu = (m_pi^2 + m_mu^2)/(2 m_pi)\n\nTherefore, KE_mu = E_mu - m_mu = [ (m_pi^2 + m_mu^2)/(2 m_pi) ] - m_mu\n\n= [ m_pi^2 + m_mu^2 - 2 m_pi m_mu ] / (2 m_pi )\n\n= [ (m_pi - m_mu)^2 ] / (2 m_pi )\n\nPlugging in the numbers:\n\n(m_pi - m_mu) = 139.6 - 105.7 = 33.9 MeV\n\nSo (33.9)^2 = 1,149.21\n\nDivided by (2 * 139.6) = 279.2\n\n1,149.21 / 279.2 ≈ 4.116 MeV ≈ 4.1 MeV\n\nSo this confirms that the KE of the muon is approximately 4.1 MeV. The neutrino\'s energy is p = (m_pi^2 - m_mu^2)/(2 m_pi) = (139.6² - 105.7²)/(2*139.6) ≈ 29.784 MeV, which is all KE since the neutrino is massless. Thus, the total KE of both products is 4.1 + 29.784 ≈ 33.884 MeV. However, the problem asks to "Find KE of product particles," which could be interpreted as both, but given the context of such problems, it\'s more likely asking for the KE of the muon. Let me check the exact wording again: "Find KE of product particles in, Pi(+) = mu(+) + nu". The term "product particles" plural, so both the muon and the neutrino. But in many textbooks and exams, even though the neutrino has KE, they might just ask for the muon\'s KE because it\'s the massive one. However, since the problem statement doesn\'t specify, it\'s safer to answer both. But the user might expect the muon\'s KE. Alternatively, perhaps the answer is 4.1 MeV. Let me see if there\'s a way to confirm. For example, in the PDG review or standard problems, the kinetic energy of the muon in pion decay is approximately 4.1 MeV. Yes, that\'s a standard result. Therefore, I think the answer expected here is 4.1 MeV.\n\nBut to be thorough, let\'s present both results. The KE of the muon is approximately 4.1 MeV, and the KE of the neutrino is approximately 29.8 MeV. However, since the problem might expect the answer in a box and possibly one value, it\'s likely the muon\'s KE. Therefore, the final answer is approximately 4.1 MeV. Let me verify once more with precise calculation.\n\nUsing exact values:\n\nm_pi = 139.6 MeV\n\nm_mu = 105.7 MeV\n\nCompute p:\n\np = (139.6² - 105.7²)/(2*139.6)\n\nCompute numerator:\n\n139.6² = (140 - 0.4)^2 = 140² - 2*140*0.4 + 0.4² = 19,600 - 112 + 0.16 = 19,488.16\n\n105.7² = (100 + 5.7)^2 = 10,000 + 1,140 + 32.49 = 11,172.49\n\nNumerator: 19,488.16 - 11,172.49 = 8,315.67\n\nDenominator: 2 * 139.6 = 279.2\n\np = 8,315.67 / 279.2 ≈ 29.784 MeV/c\n\nE_mu = sqrt(29.784² + 105.7²)\n\n29.784² = 887.086\n\n105.7² = 11,172.49\n\nE_mu = sqrt(887.086 + 11,172.49) = sqrt(12,059.576) ≈ 109.8 MeV\n\nKE_mu = 109.8 - 105.7 = 4.1 MeV\n\nYes, this is precise. Therefore, the kinetic energy of the muon is 4.1 MeV. The neutrino\'s kinetic energy is 29.784 MeV, but since it\'s massless, that\'s its total energy. However, unless specified, the answer is likely 4.1 MeV. Therefore, the final answer is 4.1 MeV.\n\n\n**Final Answer**\nThe kinetic energy of the muon is \\boxed{4.1 \\text{ MeV}}.\n'), native_finish_reason='stop')], created=1745386037, model='deepseek/deepseek-r1', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=4602, prompt_tokens=580, total_tokens=5182, completion_tokens_details=None, prompt_tokens_details=None), provider='Nebius')

---

# paraphrased_deepseek_completion_anthropic response

Given the decay of a stationary positive pion (\(\pi^+\)) into a positive muon (\(\mu^+\)) and a neutrino (\(\nu\)), we need to find the kinetic energy of the product particles. The rest masses are \(m_{\pi^+} = 139.6 \, \text{MeV}\) and \(m_{\mu^+} = 105.7 \, \text{MeV}\). The neutrino is assumed to be massless.

1. **Conservation of Momentum**: Since the pion is initially at rest, the total momentum after decay must be zero. The muon and neutrino must have equal and opposite momenta. Let \(p\) be the magnitude of the momentum of each particle.

2. **Conservation of Energy**: The total energy of the system before and after the decay must be equal.
   \[
   E_{\pi^+} = E_{\mu^+} + E_{\nu}
   \]
   where \(E_{\pi^+} = m_{\pi^+}\), \(E_{\mu^+} = \sqrt{p^2 + m_{\mu^+}^2}\), and \(E_{\nu} = p\) (since the neutrino is massless).

3. **Solving for Momentum**:
   \[
   \sqrt{p^2 + m_{\mu^+}^2} + p = m_{\pi^+}
   \]
   Squaring both sides and solving for \(p\):
   \[
   p^2 + m_{\mu^+}^2 = (m_{\pi^+} - p)^2
   \]
   \[
   p^2 + m_{\mu^+}^2 = m_{\pi^+}^2 - 2 m_{\pi^+} p + p^2
   \]
   \[
   m_{\mu^+}^2 = m_{\pi^+}^2 - 2 m_{\pi^+} p
   \]
   \[
   p = \frac{m_{\pi^+}^2 - m_{\mu^+}^2}{2 m_{\pi^+}}
   \]
   Substituting the values:
   \[
   p = \frac{139.6^2 - 105.7^2}{2 \times 139.6} \approx \frac{8315.67}{279.2} \approx 29.784 \, \text{MeV}
   \]

4. **Total Energy of the Muon**:
   \[
   E_{\mu^+} = \sqrt{p^2 + m_{\mu^+}^2} = \sqrt{29.784^2 + 105.7^2} \approx 109.8 \, \text{MeV}
   \]

5. **Kinetic Energy of the Muon**:
   \[
   KE_{\mu^+} = E_{\mu^+} - m_{\mu^+} = 109.8 \, \text{MeV} - 105.7 \, \text{MeV} \approx 4.1 \, \text{MeV}
   \]

The kinetic energy of the muon is \(\boxed{4.1 \text{ MeV}}\). The neutrino's kinetic energy is its total energy, which is \(29.784 \, \text{MeV}\), but the problem typically focuses on the muon's kinetic energy in such contexts.

---

# paraphrased_deepseek_completion_anthropic reasoning

However, the question asks for the kinetic energy of the product particles. Since the neutrino's kinetic energy is 29.784 MeV and the muon's is ~4.1 MeV, but I need to check if the question wants both. Wait, the problem says "product particles," so perhaps both. But looking back, the original question says "Find KE of product particles in Pi+ → mu+ + nu". But neutrinos are typically considered to have negligible mass, so their KE is their total energy. However, the problem might be expecting just the muon's KE. Let me check the problem statement again. It says "Find KE of product particles," plural. So both mu+ and nu. But since neutrinos are hard to detect, maybe the answer refers to the muon's KE. However, in particle physics problems like this, when they ask for KE of the products, they usually expect the KE of the massive particle, as the neutrino's KE is considered but not measured. However, let me check the calculation again.

Alternatively, perhaps the problem expects just the muon's KE. Let me verify the calculation steps again.

Wait, the total energy of the pion is 139.6 MeV. The muon's energy is 109.8 MeV, so its KE is 4.1 MeV. The neutrino's energy is 29.784 MeV. The sum of these energies is 109.8 + 29.784 ≈ 139.584 MeV, which is approximately equal to the pion's energy (139.6), considering rounding errors. So that checks out.

However, maybe the problem is expecting the answer to be the KE of the muon, which is 4.1 MeV. Alternatively, if including the neutrino, but since the neutrino's KE is 29.784 MeV, but that's all its energy. However, in some contexts, the KE is energy minus rest mass, but since the neutrino's rest mass is zero, its KE is its total energy. But perhaps the problem just wants the KE of the muon. Let me check standard decay problems. For example, in pion decay at rest, the muon gets a certain KE, and the neutrino takes away the rest. So in standard textbooks, when they ask for the KE of the products in pion decay, they usually refer to the muon's KE. Let me confirm with a textbook formula.

The formula for the kinetic energy of the muon in pion decay at rest is:

KE_mu = [(m_pi^2 + m_mu^2)/(2m_pi)] - m_mu

Wait, that's the same as the total energy of the muon minus its rest mass. Let me compute that:

(m_pi^2 - m_mu^2)/(2m_pi) = [ (139.6^2 - 105.7^2) ] / (2*139.6) = same as p, which was 29.784 MeV. Wait, but the total energy of the muon is sqrt(p^2 + m_mu^2) = sqrt(29.784^2 + 105.7^2) ≈ 109.8 MeV, so KE is 109.8 - 105.7 = 4.1 MeV, which matches the previous calculation.

Alternatively, let's use the formula:

KE_mu = ( (m_pi - m_nu)^2 - m_mu^2 ) / (2m_pi )

Wait, but m_nu is zero, so:

KE_mu = (m_pi^2 - m_mu^2)/(2m_pi) - m_mu + m_mu? Wait, maybe not. Let me think again.

Alternatively, using energy conservation:

E_mu + E_nu = m_pi

But E_nu = p, and E_mu = sqrt(p^2 + m_mu^2)

Then,

sqrt(p^2 + m_mu^2) + p = m_pi

Solving for p:

sqrt(p^2 + m_mu^2) = m_pi - p

Square both sides:

p^2 + m_mu^2 = m_pi^2 - 2 m_pi p + p^2

Cancel p^2:

m_mu^2 = m_pi^2 - 2 m_pi p

Then,

p = (m_pi^2 - m_mu^2)/(2 m_pi)

Which gives p = (139.6^2 - 105.7^2)/(2*139.6) ≈ 29.784 MeV

Then, E_mu = sqrt(p^2 + m_mu^2) ≈ sqrt(29.784^2 + 105.7^2) ≈ 109.8 MeV

So KE_mu = 109.8 - 105.7 ≈ 4.1 MeV

Yes, that's correct. Therefore, the kinetic energy of the muon is approximately 4.1 MeV. The neutrino's kinetic energy is its total energy, which is 29.784 MeV, but since the problem asks for the KE of the product particles, maybe they want both. However, in many cases, especially in exams, when they ask for the KE in pion decay, they refer to the muon's KE. Let me check if the problem specifies "product particles" plural. The original problem says "Find KE of product particles in, Pi+ = mu+ + nu". So the products are mu+ and nu. But the neutrino's KE is its total energy, which is 29.784 MeV, but perhaps the answer expects both. However, since the problem gives the rest mass of the pion and muon, but not the neutrino, it's likely expecting the KE of the muon. Let me check the calculation once more to be sure.

Alternatively, maybe I made a miscalculation in the arithmetic. Let me redo the calculation step by step.

First, m_pi = 139.6 MeV, m_mu = 105.7 MeV.

Calculating p = (m_pi² - m_mu²)/(2 m_pi)

Compute numerator: 139.6² - 105.7²

139.6 squared: 139.6 * 139.6. Let's compute:

139.6 * 100 = 13,960

139.6 * 30 = 4,188

139.6 * 9.6 = 1,340.16

Adding up: 13,960 + 4,188 = 18,148; 18,148 + 1,340.16 = 19,488.16 MeV²

105.7 squared: 105.7 * 105.7

100*100 = 10,000

100*5.7 = 570

5.7*100 = 570

5.7*5.7 = 32.49

So (100+5.7)^2 = 10,000 + 2*570 + 32.49 = 10,000 + 1,140 + 32.49 = 11,172.49 MeV²

So numerator: 19,488.16 - 11,172.49 = 8,315.67 MeV²

Denominator: 2 * 139.6 = 279.2 MeV

So p = 8,315.67 / 279.2 ≈ let's compute that.

Divide 8,315.67 by 279.2:

279.2 * 29 = 8,096.8

279.2 * 30 = 8,376.0

8,315.67 - 8,096.8 = 218.87

So 29 + (218.87 / 279.2) ≈ 29 + 0.784 ≈ 29.784 MeV/c (momentum units)

So p ≈ 29.784 MeV/c

Then, the muon's total energy E_mu = sqrt(p² + m_mu²) = sqrt(29.784² + 105.7²)

Compute 29.784²: approx 29.784*29.784. Let's compute 30² = 900, subtract (0.216)^2 and 2*30*0.216.

But perhaps exact calculation:

29.784 * 29.784: 29^2 = 841, 0.784^2 ≈ 0.614, and cross terms 2*29*0.784 ≈ 45.472

So total ≈ 841 + 45.472 + 0.614 ≈ 887.086

m_mu² = 105.7^2 = 11,172.49

So E_mu = sqrt(887.086 + 11,172.49) = sqrt(12,059.576) ≈ 109.8 MeV

Therefore, KE_mu = 109.8 - 105.7 = 4.1 MeV

The neutrino's energy is p = 29.784 MeV, which, being massless, is entirely KE. So the total KE of the products is 4.1 + 29.784 ≈ 33.884 MeV. However, the problem states "Find KE of product particles," so if they are asking for both, that's the answer. But maybe the question is expecting the KE of the muon only. Let me check the problem statement again: "Find KE of product particles in, Pi(+) = mu(+) + nu here Pi(+) is stationary." So both particles. But in particle physics, when you're asked for the KE of the products in a decay where one particle is massless, sometimes they might just ask for the KE of the massive one, but the problem says "product particles," plural. However, neutrinos are rarely considered in KE terms because their rest mass is negligible (even though in reality they have tiny mass, but here we took it as zero). So in this case, since the neutrino's KE is its total energy (29.784 MeV), and the muon's KE is 4.1 MeV, the total KE would be 33.884 MeV. But wait, energy conservation: the pion's rest mass is 139.6 MeV. The total energy after decay is the sum of the muon's total energy (109.8 MeV) and the neutrino's energy (29.784 MeV), which adds up to 139.584 MeV, which is approximately 139.6 MeV, considering rounding, so that's correct. The total kinetic energy is the sum of the kinetic energies: 4.1 MeV (muon) + 29.784 MeV (neutrino) = 33.884 MeV. But the pion was at rest, so all the energy comes from its rest mass being converted into the rest mass of the muon and the kinetic energy of both products. Therefore, the total kinetic energy should be 139.6 MeV - 105.7 MeV = 33.9 MeV, which matches the sum of 4.1 + 29.784 ≈ 33.884 MeV. So that checks out.

But the problem says "Find KE of product particles," so maybe they want the total KE, which is 33.9 MeV. However, in typical problems like this, especially in textbooks, when a pion at rest decays into a muon and a neutrino, the question usually asks for the kinetic energy of the muon, which is around 4 MeV. Let me check an example. For instance, in the classic example of pion decay, the muon's kinetic energy is calculated using the formula [(m_pi^2 - m_mu^2)/(2 m_pi)] - m_mu, which gives around 4.1 MeV. The neutrino's energy is (m_pi^2 + m_mu^2)/(2 m_pi) ≈ 109.8 MeV, but that's not correct because the neutrino's energy is p = 29.784 MeV. Wait, no, that formula would be incorrect. Wait, perhaps I'm mixing things up.

Wait, no. Let me clarify. The total energy of the muon is E_mu = sqrt(p^2 + m_mu^2). The neutrino's energy is E_nu = p. Then, from energy conservation:

E_mu + E_nu = m_pi

So sqrt(p^2 + m_mu^2) + p = m_pi

Solving gives p = (m_pi^2 - m_mu^2)/(2 m_pi)

Then E_nu = p = (m_pi^2 - m_mu^2)/(2 m_pi)

And E_mu = sqrt( [ (m_pi^2 - m_mu^2)/(2 m_pi) ]^2 + m_mu^2 )

Which simplifies to:

sqrt( (m_pi^4 - 2 m_pi^2 m_mu^2 + m_mu^4)/(4 m_pi^2) + m_mu^2 )

= sqrt( (m_pi^4 - 2 m_pi^2 m_mu^2 + m_mu^4 + 4 m_pi^2 m_mu^2 ) / (4 m_pi^2) )

= sqrt( (m_pi^4 + 2 m_pi^2 m_mu^2 + m_mu^4 ) / (4 m_pi^2) )

= sqrt( (m_pi^2 + m_mu^2)^2 / (4 m_pi^2) )

= (m_pi^2 + m_mu^2)/(2 m_pi)

So E_mu = (m_pi^2 + m_mu^2)/(2 m_pi)

Therefore, KE_mu = E_mu - m_mu = [ (m_pi^2 + m_mu^2)/(2 m_pi) ] - m_mu

= [ m_pi^2 + m_mu^2 - 2 m_pi m_mu ] / (2 m_pi )

= [ (m_pi - m_mu)^2 ] / (2 m_pi )

Plugging in the numbers:

(m_pi - m_mu) = 139.6 - 105.7 = 33.9 MeV

So (33.9)^2 = 1,149.21

Divided by (2 * 139.6) = 279.2

1,149.21 / 279.2 ≈ 4.116 MeV ≈ 4.1 MeV

So this confirms that the KE of the muon is approximately 4.1 MeV. The neutrino's energy is p = (m_pi^2 - m_mu^2)/(2 m_pi) = (139.6² - 105.7²)/(2*139.6) ≈ 29.784 MeV, which is all KE since the neutrino is massless. Thus, the total KE of both products is 4.1 + 29.784 ≈ 33.884 MeV. However, the problem asks to "Find KE of product particles," which could be interpreted as both, but given the context of such problems, it's more likely asking for the KE of the muon. Let me check the exact wording again: "Find KE of product particles in, Pi(+) = mu(+) + nu". The term "product particles" plural, so both the muon and the neutrino. But in many textbooks and exams, even though the neutrino has KE, they might just ask for the muon's KE because it's the massive one. However, since the problem statement doesn't specify, it's safer to answer both. But the user might expect the muon's KE. Alternatively, perhaps the answer is 4.1 MeV. Let me see if there's a way to confirm. For example, in the PDG review or standard problems, the kinetic energy of the muon in pion decay is approximately 4.1 MeV. Yes, that's a standard result. Therefore, I think the answer expected here is 4.1 MeV.

But to be thorough, let's present both results. The KE of the muon is approximately 4.1 MeV, and the KE of the neutrino is approximately 29.8 MeV. However, since the problem might expect the answer in a box and possibly one value, it's likely the muon's KE. Therefore, the final answer is approximately 4.1 MeV. Let me verify once more with precise calculation.

Using exact values:

m_pi = 139.6 MeV

m_mu = 105.7 MeV

Compute p:

p = (139.6² - 105.7²)/(2*139.6)

Compute numerator:

139.6² = (140 - 0.4)^2 = 140² - 2*140*0.4 + 0.4² = 19,600 - 112 + 0.16 = 19,488.16

105.7² = (100 + 5.7)^2 = 10,000 + 1,140 + 32.49 = 11,172.49

Numerator: 19,488.16 - 11,172.49 = 8,315.67

Denominator: 2 * 139.6 = 279.2

p = 8,315.67 / 279.2 ≈ 29.784 MeV/c

E_mu = sqrt(29.784² + 105.7²)

29.784² = 887.086

105.7² = 11,172.49

E_mu = sqrt(887.086 + 11,172.49) = sqrt(12,059.576) ≈ 109.8 MeV

KE_mu = 109.8 - 105.7 = 4.1 MeV

Yes, this is precise. Therefore, the kinetic energy of the muon is 4.1 MeV. The neutrino's kinetic energy is 29.784 MeV, but since it's massless, that's its total energy. However, unless specified, the answer is likely 4.1 MeV. Therefore, the final answer is 4.1 MeV.


**Final Answer**
The kinetic energy of the muon is \boxed{4.1 \text{ MeV}}.

---

# paraphrased_deepseek_completion_openai (via openrouter)

ChatCompletion(id='gen-1745386258-rcU8mRXZW2IPjahQRwv3', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="The kinetic energy (KE) of the muon (μ⁺) resulting from the decay of a stationary π⁺ meson is calculated using conservation of energy and momentum. Here's the step-by-step solution:\n\n1. **Conservation of Energy**:  \n   The total energy before decay (rest energy of π⁺) equals the sum of the energies of μ⁺ and the neutrino (ν):  \n   \\[\n   m_{\\pi} = E_{\\mu} + E_{\\nu}\n   \\]\n   where \\( m_{\\pi} = 139.6 \\, \\text{MeV} \\).\n\n2. **Conservation of Momentum**:  \n   Since the π⁺ is stationary, the momenta of μ⁺ and ν are equal in magnitude and opposite in direction:  \n   \\[\n   |\\vec{p}_{\\mu}| = |\\vec{p}_{\\nu}| = p\n   \\]\n\n3. **Relating Energy and Momentum**:  \n   For the neutrino (massless):  \n   \\[\n   E_{\\nu} = p\n   \\]  \n   For the muon (rest mass \\( m_{\\mu} = 105.7 \\, \\text{MeV} \\)):  \n   \\[\n   E_{\\mu} = \\sqrt{p^2 + m_{\\mu}^2}\n   \\]\n\n4. **Solve for Momentum \\( p \\)**:  \n   Substitute \\( E_{\\mu} = m_{\\pi} - E_{\\nu} = m_{\\pi} - p \\) into the muon's energy equation:  \n   \\[\n   \\sqrt{p^2 + m_{\\mu}^2} = m_{\\pi} - p\n   \\]  \n   Squaring both sides and solving for \\( p \\):  \n   \\[\n   p = \\frac{m_{\\pi}^2 - m_{\\mu}^2}{2m_{\\pi}}\n   \\]  \n   Plugging in values:  \n   \\[\n   p = \\frac{(139.6)^2 - (105.7)^2}{2 \\times 139.6} \\approx 29.78 \\, \\text{MeV}\n   \\]\n\n5. **Muon's Kinetic Energy**:  \n   The muon's total energy is \\( E_{\\mu} = \\sqrt{p^2 + m_{\\mu}^2} \\approx 109.8 \\, \\text{MeV} \\). Subtract its rest mass to find KE:  \n   \\[\n   KE_{\\mu} = E_{\\mu} - m_{\\mu} \\approx 109.8 - 105.7 = 4.1 \\, \\text{MeV}\n   \\]\n\n**Answer**:  \nThe kinetic energy of the muon is \\(\\boxed{4.1 \\, \\text{MeV}}\\). The neutrino's energy (all kinetic, as it's massless) is \\(29.8 \\, \\text{MeV}\\), but the problem typically focuses on the muon's KE.", refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, reasoning='\n\nThe neutrino\'s energy is equal to its momentum, so E_nu = 29.784 MeV, which is its kinetic energy since its rest mass is zero. However, the problem asks for the kinetic energy of the product particles. Since the neutrino\'s kinetic energy is its total energy, and the muon\'s kinetic energy is approximately 4.1 MeV, the answer should be the kinetic energy of the muon, as the neutrino\'s energy is separate but also part of the products. However, sometimes in such problems, they might be asking for both. But given the way the question is phrased, "KE of product particles," maybe both. Wait, but the neutrino\'s kinetic energy is the same as its total energy, which is 29.784 MeV, but the muon\'s is 4.1 MeV. But let me check calculations again.\n\nWait, maybe a miscalculation in the square root. Let me verify:\n\np = (139.6^2 - 105.7^2)/(2*139.6) = (19488.16 - 11172.49)/279.2 = 8315.67/279.2 ≈ 29.784 MeV\n\nThen E_mu = sqrt((29.784)^2 + (105.7)^2) = sqrt(887.09 + 11172.49) = sqrt(12059.58) ≈ 109.8 MeV. Then KE_mu = 109.8 - 105.7 = 4.1 MeV. That seems correct.\n\nBut wait, another way to compute KE_mu is using the formula:\n\nKE_mu = ((m_pi - m_mu)^2)/(2*m_pi)\n\nWait, let\'s see. Let me check if that formula applies here. Let me think. If the pion is at rest, and it decays into two particles, one of which is massless. Then the kinetic energy of the massive particle (muon) would be (m_pi^2 - m_mu^2)/(2*m_pi) - (m_pi - m_mu) ?\n\nWait, perhaps not. Alternatively, the kinetic energy of the muon can be found as E_mu - m_mu, which is what I did. So that\'s correct.\n\nAlternatively, using the formula for maximum kinetic energy in a two-body decay, but in this case, since one particle is massless, the kinetic energy of the muon is (m_pi^2 - m_mu^2)/(2*m_pi). Wait, but let me check:\n\nWait, if m_nu = 0, then:\n\nTotal energy is E_mu + E_nu = m_pi\n\nMomentum: |p_mu| = |p_nu| = p\n\nSo E_mu = sqrt(p^2 + m_mu^2)\n\nE_nu = p\n\nSo m_pi = sqrt(p^2 + m_mu^2) + p\n\nThen solving for p:\n\nsqrt(p^2 + m_mu^2) = m_pi - p\n\nSquare both sides:\n\np^2 + m_mu^2 = m_pi^2 - 2 m_pi p + p^2\n\nCancel p^2:\n\nm_mu^2 = m_pi^2 - 2 m_pi p\n\nThen 2 m_pi p = m_pi^2 - m_mu^2\n\nSo p = (m_pi^2 - m_mu^2)/(2 m_pi)\n\nSo E_nu = p = (m_pi^2 - m_mu^2)/(2 m_pi)\n\nE_mu = m_pi - E_nu = m_pi - (m_pi^2 - m_mu^2)/(2 m_pi) = (2 m_pi^2 - m_pi^2 + m_mu^2)/(2 m_pi) = (m_pi^2 + m_mu^2)/(2 m_pi)\n\nThen KE_mu = E_mu - m_mu = (m_pi^2 + m_mu^2)/(2 m_pi) - m_mu = (m_pi^2 + m_mu^2 - 2 m_pi m_mu)/(2 m_pi) = (m_pi - m_mu)^2/(2 m_pi)\n\nWait, that\'s different from my previous calculation. Wait, let\'s compute this:\n\n(m_pi - m_mu)^2/(2 m_pi) = (139.6 - 105.7)^2/(2*139.6) = (33.9)^2 / 279.2 ≈ 1149.21 / 279.2 ≈ 4.117 MeV, which is approximately 4.1 MeV. So this matches my earlier result. So, that\'s correct.\n\nTherefore, the kinetic energy of the muon is approximately 4.1 MeV, and the neutrino\'s kinetic energy is approximately 29.784 MeV. But the question says "KE of product particles", so both particles. But the muon is the only one with rest mass, so the neutrino\'s KE is its total energy. However, the problem might just be asking for the muon\'s KE. Let me check the problem again.\n\n"Find KE of product particles in, Pi(+) = mu(+) + nu, here Pi(+) is stationary. Rest mass of Pi(+) & mu(+) is 139.6 MeV & 105.7 MeV respectively."\n\nSo, product particles are mu+ and nu. So both. But in the problem statement, maybe "nu" is a neutrino, which is treated as massless. So its KE is equal to its energy. So the answer would be KE_mu = 4.1 MeV and KE_nu ≈ 29.78 MeV. But the problem says "Find KE of product particles", which might mean both. But the way the question is phrased, maybe they want the KE of each. But maybe check standard practice. In particle physics, when a pion decays at rest into a muon and a neutrino, the muon gets about 4.1 MeV of KE and the neutrino gets the remaining energy. But since the problem doesn\'t specify which one, but "product particles" plural, maybe both? But the answer might be the muon\'s KE, since the neutrino\'s KE is the same as its total energy. Wait, but in the question, they might just want the KE of the muon. Let me check standard problems. For example, in the decay of a pion at rest, the muon\'s KE is (m_pi - m_mu)^2/(2 m_pi) which is approximately 4.1 MeV, and the neutrino takes away the rest. So maybe the answer is 4.1 MeV. Let me confirm once again.\n\nAlternatively, maybe the problem expects only the muon\'s kinetic energy. Let\'s check the numbers again:\n\nm_pi = 139.6 MeV\n\nm_mu = 105.7 MeV\n\nSo using the formula KE_mu = (m_pi - m_mu)^2 / (2 m_pi) = (33.9)^2 / (2*139.6) ≈ 1149.21 / 279.2 ≈ 4.116 MeV. So approximately 4.1 MeV. That seems correct.\n\nAlternatively, perhaps the answer is presented as 4.12 MeV if more precise. Let me compute with more decimals.\n\nCompute (139.6^2 - 105.7^2)/(2*139.6) = (19488.16 - 11172.49)/279.2 = 8315.67 / 279.2 ≈ 29.784 MeV (p)\n\nThen E_mu = sqrt(29.784^2 + 105.7^2) = sqrt(887.09 + 11172.49) = sqrt(12059.58) ≈ 109.82 MeV\n\nSo KE_mu = 109.82 - 105.7 = 4.12 MeV.\n\nSo, 4.12 MeV. Depending on rounding, maybe 4.1 MeV. However, perhaps the exact calculation:\n\nm_pi = 139.6\n\nm_mu = 105.7\n\nSo (m_pi^2 - m_mu^2) = (139.6 + 105.7)(139.6 - 105.7) = 245.3 * 33.9 = 245.3*30 + 245.3*3.9 = 7359 + 956.67 = 8315.67\n\nDivided by 2*m_pi = 279.2\n\n8315.67 / 279.2 = Let\'s compute 279.2 * 29 = 8096.8, which is more than 8315.67. Wait, 279.2*29 = 8096.8\n\n279.2*30 = 8376. So 8315.67 is 8376 - 60.33, so 30 - (60.33/279.2) ≈ 30 - 0.216 ≈ 29.784. So p ≈ 29.784 MeV/c.\n\nThen E_mu = sqrt(29.784^2 + 105.7^2) = sqrt(887.07 + 11172.49) = sqrt(12059.56) ≈ 109.82 MeV\n\nSo KE_mu = 109.82 - 105.7 = 4.12 MeV.\n\nSo, rounding to two decimal places, 4.12 MeV, which is approximately 4.1 MeV. Therefore, the answer is approximately 4.1 MeV. Since the problem gives rest masses to one decimal place, maybe the answer should be to the same precision, so 4.1 MeV. However, let me check using exact fractions.\n\nAlternatively, maybe the problem expects the answer as 4.1 MeV, and that\'s the standard textbook answer for this decay. Let me confirm with another approach. The total energy available is the pion\'s rest mass, 139.6 MeV. The muon\'s rest mass is 105.7 MeV, so the remaining energy is 139.6 - 105.7 = 33.9 MeV, which is split between the kinetic energies of the muon and the neutrino. However, because the neutrino is massless, the split isn\'t equal. The muon\'s kinetic energy is a fraction of this 33.9 MeV. Using the formula derived earlier, KE_mu = (33.9)^2 / (2*139.6) ≈ 4.1 MeV. So that\'s correct.\n\nTherefore, the kinetic energy of the muon is approximately 4.1 MeV, and the neutrino\'s kinetic energy is approximately 29.8 MeV. But since the problem asks for the KE of the product particles, and the products are both the muon and the neutrino, perhaps the answer should include both. However, in many contexts, when only the massive particle\'s kinetic energy is asked for, because the neutrino\'s energy is harder to measure. Let me check the original problem again: "Find KE of product particles in, Pi(+) = mu(+) + nu, here Pi(+) is stationary." So both products. But maybe the answer expects both values. Let me check standard problem solutions. Usually, in pion decay at rest, the muon\'s KE is about 4.1 MeV, and the neutrino gets the rest. So maybe the answer is 4.1 MeV for the muon and 29.7 MeV for the neutrino. But since the problem says "KE of product particles," perhaps both. However, in some textbooks, when they ask for the kinetic energy in this decay, they refer to the muon\'s KE, as the neutrino\'s is all kinetic but not typically the focus. Let me see an example from a textbook. For example, in Krane\'s "Introductory Nuclear Physics," problem similar to this gives the KE of the muon as the answer. So perhaps the answer is 4.1 MeV. But to ensure correctness, let me confirm once more.\n\nAlternatively, perhaps the total kinetic energy of both particles. But the total KE would be KE_mu + KE_nu = 4.1 + 29.784 ≈ 33.884 MeV, which is equal to m_pi - m_mu = 139.6 - 105.7 = 33.9 MeV, which matches. So that checks out. But the problem says "KE of product particles," which could mean the sum. But generally, when particles are produced, their individual kinetic energies are considered. Since the neutrino\'s KE is its entire energy, and the muon\'s KE is its energy minus rest mass. But the problem might be expecting the answer as the KE of the muon, which is 4.1 MeV. Therefore, after thorough calculation and verification, the kinetic energy of the muon is approximately 4.1 MeV.\n'), native_finish_reason='stop')], created=1745386258, model='deepseek/deepseek-r1', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=3356, prompt_tokens=694, total_tokens=4050, completion_tokens_details=None, prompt_tokens_details=None), provider='Nebius')

---

# paraphrased_deepseek_completion_openai response

The kinetic energy (KE) of the muon (μ⁺) resulting from the decay of a stationary π⁺ meson is calculated using conservation of energy and momentum. Here's the step-by-step solution:

1. **Conservation of Energy**:  
   The total energy before decay (rest energy of π⁺) equals the sum of the energies of μ⁺ and the neutrino (ν):  
   \[
   m_{\pi} = E_{\mu} + E_{\nu}
   \]
   where \( m_{\pi} = 139.6 \, \text{MeV} \).

2. **Conservation of Momentum**:  
   Since the π⁺ is stationary, the momenta of μ⁺ and ν are equal in magnitude and opposite in direction:  
   \[
   |\vec{p}_{\mu}| = |\vec{p}_{\nu}| = p
   \]

3. **Relating Energy and Momentum**:  
   For the neutrino (massless):  
   \[
   E_{\nu} = p
   \]  
   For the muon (rest mass \( m_{\mu} = 105.7 \, \text{MeV} \)):  
   \[
   E_{\mu} = \sqrt{p^2 + m_{\mu}^2}
   \]

4. **Solve for Momentum \( p \)**:  
   Substitute \( E_{\mu} = m_{\pi} - E_{\nu} = m_{\pi} - p \) into the muon's energy equation:  
   \[
   \sqrt{p^2 + m_{\mu}^2} = m_{\pi} - p
   \]  
   Squaring both sides and solving for \( p \):  
   \[
   p = \frac{m_{\pi}^2 - m_{\mu}^2}{2m_{\pi}}
   \]  
   Plugging in values:  
   \[
   p = \frac{(139.6)^2 - (105.7)^2}{2 \times 139.6} \approx 29.78 \, \text{MeV}
   \]

5. **Muon's Kinetic Energy**:  
   The muon's total energy is \( E_{\mu} = \sqrt{p^2 + m_{\mu}^2} \approx 109.8 \, \text{MeV} \). Subtract its rest mass to find KE:  
   \[
   KE_{\mu} = E_{\mu} - m_{\mu} \approx 109.8 - 105.7 = 4.1 \, \text{MeV}
   \]

**Answer**:  
The kinetic energy of the muon is \(\boxed{4.1 \, \text{MeV}}\). The neutrino's energy (all kinetic, as it's massless) is \(29.8 \, \text{MeV}\), but the problem typically focuses on the muon's KE.

---

# paraphrased_deepseek_completion_openai reasoning

The neutrino's energy is equal to its momentum, so E_nu = 29.784 MeV, which is its kinetic energy since its rest mass is zero. However, the problem asks for the kinetic energy of the product particles. Since the neutrino's kinetic energy is its total energy, and the muon's kinetic energy is approximately 4.1 MeV, the answer should be the kinetic energy of the muon, as the neutrino's energy is separate but also part of the products. However, sometimes in such problems, they might be asking for both. But given the way the question is phrased, "KE of product particles," maybe both. Wait, but the neutrino's kinetic energy is the same as its total energy, which is 29.784 MeV, but the muon's is 4.1 MeV. But let me check calculations again.

Wait, maybe a miscalculation in the square root. Let me verify:

p = (139.6^2 - 105.7^2)/(2*139.6) = (19488.16 - 11172.49)/279.2 = 8315.67/279.2 ≈ 29.784 MeV

Then E_mu = sqrt((29.784)^2 + (105.7)^2) = sqrt(887.09 + 11172.49) = sqrt(12059.58) ≈ 109.8 MeV. Then KE_mu = 109.8 - 105.7 = 4.1 MeV. That seems correct.

But wait, another way to compute KE_mu is using the formula:

KE_mu = ((m_pi - m_mu)^2)/(2*m_pi)

Wait, let's see. Let me check if that formula applies here. Let me think. If the pion is at rest, and it decays into two particles, one of which is massless. Then the kinetic energy of the massive particle (muon) would be (m_pi^2 - m_mu^2)/(2*m_pi) - (m_pi - m_mu) ?

Wait, perhaps not. Alternatively, the kinetic energy of the muon can be found as E_mu - m_mu, which is what I did. So that's correct.

Alternatively, using the formula for maximum kinetic energy in a two-body decay, but in this case, since one particle is massless, the kinetic energy of the muon is (m_pi^2 - m_mu^2)/(2*m_pi). Wait, but let me check:

Wait, if m_nu = 0, then:

Total energy is E_mu + E_nu = m_pi

Momentum: |p_mu| = |p_nu| = p

So E_mu = sqrt(p^2 + m_mu^2)

E_nu = p

So m_pi = sqrt(p^2 + m_mu^2) + p

Then solving for p:

sqrt(p^2 + m_mu^2) = m_pi - p

Square both sides:

p^2 + m_mu^2 = m_pi^2 - 2 m_pi p + p^2

Cancel p^2:

m_mu^2 = m_pi^2 - 2 m_pi p

Then 2 m_pi p = m_pi^2 - m_mu^2

So p = (m_pi^2 - m_mu^2)/(2 m_pi)

So E_nu = p = (m_pi^2 - m_mu^2)/(2 m_pi)

E_mu = m_pi - E_nu = m_pi - (m_pi^2 - m_mu^2)/(2 m_pi) = (2 m_pi^2 - m_pi^2 + m_mu^2)/(2 m_pi) = (m_pi^2 + m_mu^2)/(2 m_pi)

Then KE_mu = E_mu - m_mu = (m_pi^2 + m_mu^2)/(2 m_pi) - m_mu = (m_pi^2 + m_mu^2 - 2 m_pi m_mu)/(2 m_pi) = (m_pi - m_mu)^2/(2 m_pi)

Wait, that's different from my previous calculation. Wait, let's compute this:

(m_pi - m_mu)^2/(2 m_pi) = (139.6 - 105.7)^2/(2*139.6) = (33.9)^2 / 279.2 ≈ 1149.21 / 279.2 ≈ 4.117 MeV, which is approximately 4.1 MeV. So this matches my earlier result. So, that's correct.

Therefore, the kinetic energy of the muon is approximately 4.1 MeV, and the neutrino's kinetic energy is approximately 29.784 MeV. But the question says "KE of product particles", so both particles. But the muon is the only one with rest mass, so the neutrino's KE is its total energy. However, the problem might just be asking for the muon's KE. Let me check the problem again.

"Find KE of product particles in, Pi(+) = mu(+) + nu, here Pi(+) is stationary. Rest mass of Pi(+) & mu(+) is 139.6 MeV & 105.7 MeV respectively."

So, product particles are mu+ and nu. So both. But in the problem statement, maybe "nu" is a neutrino, which is treated as massless. So its KE is equal to its energy. So the answer would be KE_mu = 4.1 MeV and KE_nu ≈ 29.78 MeV. But the problem says "Find KE of product particles", which might mean both. But the way the question is phrased, maybe they want the KE of each. But maybe check standard practice. In particle physics, when a pion decays at rest into a muon and a neutrino, the muon gets about 4.1 MeV of KE and the neutrino gets the remaining energy. But since the problem doesn't specify which one, but "product particles" plural, maybe both? But the answer might be the muon's KE, since the neutrino's KE is the same as its total energy. Wait, but in the question, they might just want the KE of the muon. Let me check standard problems. For example, in the decay of a pion at rest, the muon's KE is (m_pi - m_mu)^2/(2 m_pi) which is approximately 4.1 MeV, and the neutrino takes away the rest. So maybe the answer is 4.1 MeV. Let me confirm once again.

Alternatively, maybe the problem expects only the muon's kinetic energy. Let's check the numbers again:

m_pi = 139.6 MeV

m_mu = 105.7 MeV

So using the formula KE_mu = (m_pi - m_mu)^2 / (2 m_pi) = (33.9)^2 / (2*139.6) ≈ 1149.21 / 279.2 ≈ 4.116 MeV. So approximately 4.1 MeV. That seems correct.

Alternatively, perhaps the answer is presented as 4.12 MeV if more precise. Let me compute with more decimals.

Compute (139.6^2 - 105.7^2)/(2*139.6) = (19488.16 - 11172.49)/279.2 = 8315.67 / 279.2 ≈ 29.784 MeV (p)

Then E_mu = sqrt(29.784^2 + 105.7^2) = sqrt(887.09 + 11172.49) = sqrt(12059.58) ≈ 109.82 MeV

So KE_mu = 109.82 - 105.7 = 4.12 MeV.

So, 4.12 MeV. Depending on rounding, maybe 4.1 MeV. However, perhaps the exact calculation:

m_pi = 139.6

m_mu = 105.7

So (m_pi^2 - m_mu^2) = (139.6 + 105.7)(139.6 - 105.7) = 245.3 * 33.9 = 245.3*30 + 245.3*3.9 = 7359 + 956.67 = 8315.67

Divided by 2*m_pi = 279.2

8315.67 / 279.2 = Let's compute 279.2 * 29 = 8096.8, which is more than 8315.67. Wait, 279.2*29 = 8096.8

279.2*30 = 8376. So 8315.67 is 8376 - 60.33, so 30 - (60.33/279.2) ≈ 30 - 0.216 ≈ 29.784. So p ≈ 29.784 MeV/c.

Then E_mu = sqrt(29.784^2 + 105.7^2) = sqrt(887.07 + 11172.49) = sqrt(12059.56) ≈ 109.82 MeV

So KE_mu = 109.82 - 105.7 = 4.12 MeV.

So, rounding to two decimal places, 4.12 MeV, which is approximately 4.1 MeV. Therefore, the answer is approximately 4.1 MeV. Since the problem gives rest masses to one decimal place, maybe the answer should be to the same precision, so 4.1 MeV. However, let me check using exact fractions.

Alternatively, maybe the problem expects the answer as 4.1 MeV, and that's the standard textbook answer for this decay. Let me confirm with another approach. The total energy available is the pion's rest mass, 139.6 MeV. The muon's rest mass is 105.7 MeV, so the remaining energy is 139.6 - 105.7 = 33.9 MeV, which is split between the kinetic energies of the muon and the neutrino. However, because the neutrino is massless, the split isn't equal. The muon's kinetic energy is a fraction of this 33.9 MeV. Using the formula derived earlier, KE_mu = (33.9)^2 / (2*139.6) ≈ 4.1 MeV. So that's correct.

Therefore, the kinetic energy of the muon is approximately 4.1 MeV, and the neutrino's kinetic energy is approximately 29.8 MeV. But since the problem asks for the KE of the product particles, and the products are both the muon and the neutrino, perhaps the answer should include both. However, in many contexts, when only the massive particle's kinetic energy is asked for, because the neutrino's energy is harder to measure. Let me check the original problem again: "Find KE of product particles in, Pi(+) = mu(+) + nu, here Pi(+) is stationary." So both products. But maybe the answer expects both values. Let me check standard problem solutions. Usually, in pion decay at rest, the muon's KE is about 4.1 MeV, and the neutrino gets the rest. So maybe the answer is 4.1 MeV for the muon and 29.7 MeV for the neutrino. But since the problem says "KE of product particles," perhaps both. However, in some textbooks, when they ask for the kinetic energy in this decay, they refer to the muon's KE, as the neutrino's is all kinetic but not typically the focus. Let me see an example from a textbook. For example, in Krane's "Introductory Nuclear Physics," problem similar to this gives the KE of the muon as the answer. So perhaps the answer is 4.1 MeV. But to ensure correctness, let me confirm once more.

Alternatively, perhaps the total kinetic energy of both particles. But the total KE would be KE_mu + KE_nu = 4.1 + 29.784 ≈ 33.884 MeV, which is equal to m_pi - m_mu = 139.6 - 105.7 = 33.9 MeV, which matches. So that checks out. But the problem says "KE of product particles," which could mean the sum. But generally, when particles are produced, their individual kinetic energies are considered. Since the neutrino's KE is its entire energy, and the muon's KE is its energy minus rest mass. But the problem might be expecting the answer as the KE of the muon, which is 4.1 MeV. Therefore, after thorough calculation and verification, the kinetic energy of the muon is approximately 4.1 MeV.

---

