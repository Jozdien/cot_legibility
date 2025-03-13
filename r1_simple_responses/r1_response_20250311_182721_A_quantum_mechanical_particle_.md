# Original Question

A quantum mechanical particle of mass m moves in two dimensions in the following potential, as a function of (r,θ): V (r, θ) = 1/2 kr^2 + 3/2 kr^2 cos^2(θ)
Find the energy spectrum.

---

# R1 response

To find the energy spectrum of a quantum mechanical particle moving in two dimensions with the potential \( V(r, \theta) = \frac{1}{2} kr^2 + \frac{3}{2} kr^2 \cos^2(\theta) \), we start by converting the potential into Cartesian coordinates. 

First, we recognize that \(\cos^2(\theta) = \frac{x^2}{r^2}\). Substituting this into the potential gives:
\[
V(r, \theta) = \frac{1}{2} kr^2 + \frac{3}{2} kr^2 \frac{x^2}{r^2} = \frac{1}{2} k (x^2 + y^2) + \frac{3}{2} kx^2
\]
Simplifying this expression, we get:
\[
V(x, y) = 2kx^2 + \frac{1}{2}ky^2
\]
This potential represents a two-dimensional anisotropic harmonic oscillator with different spring constants in the \(x\) and \(y\) directions. The angular frequencies for the oscillators in each direction are:
\[
\omega_x = 2 \sqrt{\frac{k}{m}} \quad \text{and} \quad \omega_y = \sqrt{\frac{k}{m}}
\]

The energy levels for a quantum harmonic oscillator in each direction are given by:
\[
E_x = \hbar \omega_x \left(n_x + \frac{1}{2}\right) \quad \text{and} \quad E_y = \hbar \omega_y \left(n_y + \frac{1}{2}\right)
\]
Substituting the angular frequencies, we get:
\[
E_x = 2\hbar \sqrt{\frac{k}{m}} \left(n_x + \frac{1}{2}\right) \quad \text{and} \quad E_y = \hbar \sqrt{\frac{k}{m}} \left(n_y + \frac{1}{2}\right)
\]

The total energy is the sum of the energies from each direction:
\[
E = E_x + E_y = 2\hbar \sqrt{\frac{k}{m}} \left(n_x + \frac{1}{2}\right) + \hbar \sqrt{\frac{k}{m}} \left(n_y + \frac{1}{2}\right)
\]
Factoring out \(\hbar \sqrt{\frac{k}{m}}\), we get:
\[
E = \hbar \sqrt{\frac{k}{m}} \left[2\left(n_x + \frac{1}{2}\right) + \left(n_y + \frac{1}{2}\right)\right]
\]
Simplifying inside the brackets:
\[
E = \hbar \sqrt{\frac{k}{m}} \left(2n_x + n_y + \frac{3}{2}\right)
\]

Thus, the energy spectrum is given by:
\[
\boxed{E = \hbar \sqrt{\frac{k}{m}} \left(2n_x + n_y + \frac{3}{2}\right)}
\]
where \(n_x\) and \(n_y\) are non-negative integers.

---

# R1 reasoning

Okay, so I need to find the energy spectrum for a quantum mechanical particle moving in two dimensions with this potential: V(r, θ) = (1/2) kr² + (3/2) kr² cos²(θ). Hmm, let's break this down step by step.

First, I know that in two-dimensional quantum mechanics problems with polar coordinates, the Schrödinger equation is usually separated into radial and angular parts. The potential here is given in polar coordinates, which suggests that maybe I should work in polar coordinates too. But the potential isn't just a function of r; it also depends on θ. That complicates things because if the potential has angular dependence, the usual separation of variables might not be straightforward. 

Wait, the given potential is V(r, θ) = (1/2) kr² + (3/2) kr² cos²θ. Let me simplify this expression first. Combine the terms:

V(r, θ) = (1/2 kr²)(1 + 3 cos²θ). So, that's a combination of a radial part and an angular part. Maybe I can factor this potential in a way that allows separation of variables. But 1 + 3 cos²θ... Hmm.

Alternatively, maybe there's a coordinate system or some substitution that can turn this into a more familiar problem. Let me think. If we consider cos²θ, if I remember correctly, trigonometric identities, cos²θ = (1 + cos2θ)/2. Let me try substituting that:

V(r, θ) = (1/2 kr²)[1 + 3*(1 + cos2θ)/2] = (1/2 kr²)[ (2 + 3 + 3 cos2θ)/2 ] = (1/2 kr²)(5/2 + 3/2 cos2θ). 

That simplifies to V(r,θ) = (5/4) kr² + (3/4) kr² cos2θ. Wait, but does this help? Maybe not immediately. Let's see.

Alternatively, in 2D polar coordinates, the Schrödinger equation is:

[-ħ²/(2m) (1/r ∂/∂r (r ∂/∂r) + 1/r² ∂²/∂θ²) + V(r,θ)]ψ(r,θ) = Eψ(r,θ)

Since the potential still has angular dependence, the solution might not simply be the product of radial and angular functions. But maybe if we can express the angular part in terms of spherical harmonics or some other angular functions? Wait, but this is in 2D, so the angular part is just periodic in θ with period 2π. So, in 2D, the angular solutions are e^(ilθ) where l is an integer.

But if there's a potential that depends on θ, that complicates the angular equation. So, perhaps we can treat the angular part as a perturbation, but since this is a problem looking for an exact solution, maybe not. Alternatively, maybe the angular part can be rewritten such that it resembles a known equation.

Let me analyze the angular part. Let's try to separate variables. Let’s assume that the wavefunction can be written as ψ(r,θ) = R(r)Φ(θ). Substituting into the Schrödinger equation:

[-ħ²/(2m) (1/r d/dr (r dR/dr) Φ + R/r² d²Φ/dθ² ) + (1/2 kr² + 3/2 kr² cos²θ)RΦ ] = E R Φ

Divide both sides by RΦ:

-ħ²/(2m) [ (1/r R d/dr (r dR/dr) ) + (1/(r² Φ) d²Φ/dθ²) ] + (1/2 kr² + 3/2 kr² cos²θ) = E

Multiply both sides by -2m/ħ²:

[ (1/r R d/dr (r dR/dr) ) + (1/(r² Φ) d²Φ/dθ²) ] - (2m/ħ²)(1/2 kr² + 3/2 kr² cos²θ ) = -2m E / ħ²

Rearrange terms:

(1/r R d/dr (r dR/dr) ) - (2m/ħ²)(1/2 kr² + 3/2 kr² cos²θ ) + (1/(r² Φ) d²Φ/dθ²) = -2m E / ħ²

Wait, this seems messy. Let's see if separating variables is possible here. Let's group terms depending on r and θ. The term with the potential has both r² and cos²θ. When trying to separate, we need to have the equation split into parts depending only on r and only on θ. Let me bring the potential terms to the other side.

But actually, perhaps, if we move all terms to the right except the angular derivative term, so:

(1/r R d/dr (r dR/dr)) + (2m/ħ²)(E - V(r,θ)) = - (1/(r² Φ) d²Φ/dθ² )

Wait, but the left side has dependence on both r and θ (since V depends on both), and the right side is just dependent on θ. This suggests that unless V(r,θ) can be expressed as a sum of terms each depending only on r or θ, we can't separate variables. However, let me see: our potential V(r,θ) is (1/2 kr²)(1 + 3 cos²θ), so we can write V(r,θ) = (1/2 kr²) + (3/2 kr² cos²θ). Therefore, V(r,θ) = f(r) + g(r) h(θ), where f(r) = (1/2 k r²), g(r) = (3/2 k r²), and h(θ) = cos²θ.

But this complicates separation of variables because now the potential couples r and θ terms. So perhaps separation of variables isn't straightforward here.

Alternatively, maybe there is a coordinate transformation that can turn this potential into a separable form. For example, maybe elliptical coordinates? Because the angular dependence is cos²θ, which might suggest something like squashed or stretched coordinates.

Alternatively, let's consider polar coordinates and whether cos²θ can be expressed somehow. Cos²θ is a quadrupole term. So, perhaps this potential resembles something in a multipole expansion. But in two dimensions... Alternatively, maybe convert to cartesian coordinates.

Wait, cosθ = x/r. So, cos²θ = x²/r². Then, the potential becomes V(r,θ) = (1/2 kr²) + (3/2 kr²)(x²/r²) = (1/2 kr²) + (3/2 kx²). Therefore, V(r,θ) = (1/2 k)(x² + y²) + (3/2 k x²) = (1/2 k y²) + (1/2 k x² + 3/2 k x²) = (1/2 k y²) + (2 k x²). So, V(x, y) = 2k x² + (1/2) k y².

Oh! Wait, this seems interesting. So, converting to Cartesian coordinates, the potential is V(x,y) = 2k x² + (1/2)k y². That's just a two-dimensional anisotropic harmonic oscillator potential with different spring constants in the x and y directions! 

So, in this case, the problem reduces to a 2D anisotropic harmonic oscillator where the potential is V(x,y) = (1/2)m ω_x² x² + (1/2)m ω_y² y². But in our case, we've expressed V(x,y) as 2k x² + (1/2)k y². So identifying:

(1/2) m ω_x² x² = 2k x² => ω_x = sqrt(4k/m)
Similarly, (1/2)m ω_y² y² = (1/2)k y² => ω_y = sqrt(k/m)

Therefore, the frequencies in x and y directions are ω_x = 2 sqrt(k/m) and ω_y = sqrt(k/m).

Ah! So the problem is actually separable in Cartesian coordinates, giving an anisotropic harmonic oscillator, which has known energy levels. Then, the energy spectrum is just the sum of the energies from the x and y directions:

E = ħ ω_x (n_x + 1/2) + ħ ω_y (n_y + 1/2) where n_x and n_y are non-negative integers (0,1,2,...). Therefore, substituting ω_x and ω_y:

E = ħ * 2 sqrt(k/m) (n_x + 1/2) + ħ * sqrt(k/m) (n_y + 1/2)
= ħ sqrt(k/m) [ 2(n_x + 1/2) + (n_y + 1/2) ]
= ħ sqrt(k/m) [2n_x + n_y + 3/2 ]

But we can factor the sqrt(k/m): let's denote ω = sqrt(k/m), which is the natural frequency if it were a symmetric oscillator. Then:

E = ħ ω (2n_x + n_y + 3/2 )

Wait, but maybe expressed in terms of the quantum numbers? Or perhaps normal ordering.

Alternatively, in cartesian coordinates, since the oscillator is anisotropic, the energies are simply additive for each direction. So for the x-direction, frequency ω_x = 2 sqrt(k/m), so E_x = (n_x + 1/2) ħ ω_x = (n_x + 1/2) * 2 ħ sqrt(k/m) = ħ sqrt(k/m) (2n_x + 1)

Similarly, the y-direction has ω_y = sqrt(k/m), so E_y = (n_y + 1/2) ħ sqrt(k/m)

Total energy E = E_x + E_y = ħ sqrt(k/m) [ (2n_x + 1) + (n_y + 1/2) ] = ħ sqrt(k/m)( 2n_x + n_y + 3/2 )

So, this would give the energy levels depending on the quantum numbers n_x and n_y which are non-negative integers.

But the problem is initially presented in polar coordinates. However, given that conversion to Cartesian coordinates unveils the potential as that of an anisotropic harmonic oscillator, we can use that knowledge to write the energy spectrum directly.

Alternatively, had the potential not been separable in Cartesian coordinates, the problem would have been much more challenging. But here, since V(x,y) splits into x and y parts, it's separable, leading to a straightforward solution with energy levels as above.

Alternatively, let's check this result by considering another approach.

Suppose we start from polar coordinates. Even though the potential V(r, θ) isn't purely radial, in cartesian coordinates, it becomes a simple anisotropic oscillator, so we might need to confirm that it's separable in polar coordinates. Wait, but in polar coordinates, with an angular dependence, separating variables is tough unless we can write the potential in a special form.

But from Cartesian coordinates, where the problem is separable, the energy levels seem straightforward. So the answer must be that the energy spectrum is E = ħ sqrt(k/m)(2n_x + n_y + 3/2 ). 

Alternatively, since in 2D harmonic oscillators (anisotropic), each direction contributes its own quantum number. So indeed, the energy is sum of each harmonic oscillator energy in their respective directions.

However, let me check the conversion again. Original potential was V(r,θ) = 1/2 kr² + 3/2 kr² cos²θ. Then converting to Cartesian coordinates:

cosθ = x/r, so cos²θ = x²/r². Then, V = (1/2)k(x² + y²) + (3/2)k (x²) = (1/2 k x² + 1/2 k y²) + 3/2 k x² = (1/2 k + 3/2 k) x² + 1/2 k y² = 2k x² + (1/2 k) y². Which matches.

So, the potential is a harmonic oscillator with different spring constants in x and y directions: V(x, y) = (1/2)(4k) x² + (1/2)k y². Wait, but when we write a harmonic oscillator potential as (1/2)mω² x², so here, in x direction, m ω_x² /2 = 2k? No, original potential is 2k x², so (1/2)m ω_x² x² = 2k x², so (1/2)m ω_x² = 2k, which gives ω_x² = 4k/m, so ω_x = 2 sqrt(k/m). Similarly, the y-direction, (1/2)m ω_y² y² = (1/2) k y² => m ω_y² = k => ω_y² = k/m => ω_y = sqrt(k/m), which is consistent with earlier.

Therefore, if the problem is separable in Cartesian coordinates, the energy is indeed E = ħω_x (n_x + 1/2) + ħω_y (n_y + 1/2) = ħ*2sqt(k/m)(n_x + 1/2 ) + ħ*sqrt(k/m)(n_y + 1/2 ) = ħ sqrt(k/m)[2(n_x +1/2) + (n_y +1/2)] = ħ sqrt(k/m)(2n_x + n_y + 3/2 )

Alternatively, sometimes energy levels are written using different constants, but it's the same expression. Therefore, if we want to write the energy spectrum, we can write:

E_{n_x, n_y} = ħ sqrt(k/m) (2n_x + n_y + 3/2 )

where n_x and n_y are non-negative integers (0,1,2,...)

Alternatively, perhaps to express in terms of a single quantum number? Not sure. In anisotropic oscillators, energy depends on both n_x and n_y, but depending on ratios of frequencies. In this case, the x-frequency is twice the y-frequency. So maybe we can combine quantum numbers in some way, but typically they remain as two independent quantum numbers. 

Alternatively, think in terms of creating a basis for the energy levels. The energy levels would thus be characterized by pairs (n_x, n_y), and the energy is linear in these. However, if frequencies are commensurate, there could be degeneracy. For example, here ω_x = 2ω and ω_y = ω, so frequencies are in 2:1 ratio. So you could have different pairs of (n_x, n_y) giving the same energy. For instance, suppose taking n_x and n_y such that 2n_x + n_y = constant. Then E = ħω (constant + 3/2 ). The different combinations would correspond to degeneracies.

However, in the problem statement, they just ask for the energy spectrum. So, in this case, the answer would be the energies given by E = ħ sqrt(k/m)(2n_x + n_y + 3/2 ) with n_x, n_y ≥ 0 integers.

Alternatively, to check if this is correct, maybe plug in some values. For example, if n_x = 0 and n_y = 0:

E = ħ sqrt(k/m)(0 + 0 + 3/2 ) = (3/2) ħ sqrt(k/m)

If in x and y directions, the ground state energy of each.

For x-direction: (1/2) ħ ω_x = (1/2) * ħ * 2 sqrt(k/m ) = ħ sqrt(k/m )

For y-direction: (1/2) ħ ω_y = (1/2) ħ sqrt(k/m )

So total energy: ħ sqrt(k/m ) + (1/2) ħ sqrt(k/m ) = (3/2) ħ sqrt(k/m ). That's correct.

For n_x =1, n_y =0:

E = ħ sqrt(k/m)(2 +0 +3/2) = (7/2) ħ sqrt(k/m )

In x-direction: (1 +1/2) ω_x ħ= (3/2)*2 sqrt(k/m )* ħ = 3 sqrt(k/m ) ħ

Wait, no, sorry, earlier substitution: shouldn't V(x) be written as (1/2 m ω_x² x²). Here, they had (1/2 kr² + 3/2 kr² cos²θ) converted to cartesian gave 2k x² + (1/2 k)y².

But so x component: 2k x² = (1/2)m ω_x² x² => ω_x² = 4k/m, ω_x=2√(k/m )

Thus, energy levels for x are ħ ω_x(n_x +1/2) = 2ħ√(k/m)(n_x +1/2)

Similarly, for y: (1/2)k y² = (1/2 m ω_y² y² ) => ω_y = √(k/m )

Energy levels in y: ħ√(k/m)(n_y +1/2 )

Therefore, total energy E = 2ħ√(k/m)(n_x +1/2 ) + ħ√(k/m)(n_y +1/2 ) = ħ√(k/m)[2(n_x +1/2) + (n_y +1/2 ) ] = ħ√(k/m)(2n_x + 1 + n_y + 0.5 )=ĥ√(k/m)(2n_x + n_y + 1.5 )

Yes, that seems correct. So to check for n_x=0, n_y=0: E= 1.5 ħ√(k/m )

If n_x=1, n_y=0: 2*1 +0 +1.5=3.5, so E=3.5 ħ√(k/m )

While in x-direction: (1 +0.5)* 2ħ√(k/m) =3.0 ħ√(k/m ). Then 3 +0.5 (= y's 0.5 )=3.5. Ok correct.

Similarly, n_x=0, n_y=1: E=2*0 +1 +1.5=2.5 ħ√(k/m )

Which matches with x contributing 1.0 (0.5*2) and y contributing 1.5 (1+0.5 ), sum 2.5. Correct.

Therefore, this does hold up.

Thus, the answer is that the energy spectrum is given by E_{n_x,n_y} = ħ ω (2n_x + n_y + 3/2 ), where ω = sqrt(k/m ), and n_x,n_y are non-negative integers.

But we can write this more cleanly.

Let me factor ω as sqrt(k/m ). So, E = ħ sqrt(k/m ) (2n_x +n_y +3/2 )

Alternatively, write this as:

E = (2n_x +n_y + 3/2 )ħ √(k/m )

Therefore, the energy levels are quantized in terms of quantum numbers n_x and n_y, non-negative integers.

In some cases, people might write using separate frequencies:

E = (n_x +1/2 ) ħ ω_x + (n_y +1/2 ) ħ ω_y

But since ω_x =2 ω and ω_y= ω, this reduces to the same expression.

So yes, this is the answer.

**Final Answer**
The energy spectrum is given by \boxed{E = \hbar \sqrt{\frac{k}{m}} \left(2n_x + n_y + \frac{3}{2}\right)} where \(n_x\) and \(n_y\) are non-negative integers.


---

