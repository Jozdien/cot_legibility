# Original Question

Calculate the eigenvector of a quantum mechanical operator $\vec{P}$ for a muon along an arbitrary direction $\vec{n}$ lying in the x-z plane corresponding to the eigenvalue $+\hbar/2$. Given the $X-$component, $P_x$ of the operator $P$ as $\hbar/2$ times a 2 by 2 square matrix having elements in the first row as $(0 1)$, and that in the second row as $(1, 0)$. The $Y-$component, $P_y$ of the operator is given by the product of $\hbar/2$ and a 2 by 2 square matrix having elements in the first row as $(0, -i)$, and that in the second row as $(i, 0)$. Finally, the $Z-$component, $P_z$ of the operator is given by the product of $\hbar/2$  and another 2 by 2 square matrix having elements in the first row as $(1, 0)$, and that in the second row as $(0, -1)$.  What are the elements of the normalized eigenvector? 


---

# R1 response

To find the normalized eigenvector of the quantum mechanical operator \(\vec{P}\) along an arbitrary direction \(\vec{n}\) in the x-z plane corresponding to the eigenvalue \(+\hbar/2\), we start by noting that the direction \(\vec{n}\) can be parameterized as \((\sin\theta, 0, \cos\theta)\), where \(\theta\) is the angle from the z-axis to \(\vec{n}\).

The operator \(\vec{P}\) along \(\vec{n}\) is given by:
\[
\vec{P} \cdot \vec{n} = \sin\theta P_x + \cos\theta P_z
\]
Given the Pauli matrices for \(P_x\), \(P_y\), and \(P_z\) multiplied by \(\hbar/2\), we focus on the matrix part (since \(\hbar/2\) factors out, and we need the eigenvalue +1 for the corresponding Pauli matrix combination):
\[
\sigma \cdot \vec{n} = \sin\theta \sigma_x + \cos\theta \sigma_z
\]
The matrix \(\sigma \cdot \vec{n}\) becomes:
\[
\sigma \cdot \vec{n} = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}
\]

We solve the eigenvalue equation \((\sigma \cdot \vec{n}) |\psi\rangle = |\psi\rangle\) by setting up the equations:
\[
\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} a \\ b \end{pmatrix}
\]

This leads to the system of equations:
1. \((\cos\theta - 1)a + \sin\theta b = 0\)
2. \(\sin\theta a - (\cos\theta + 1)b = 0\)

From the first equation, we find:
\[
b = \frac{1 - \cos\theta}{\sin\theta} a
\]

Using trigonometric identities, this simplifies to:
\[
b = \tan\left(\frac{\theta}{2}\right) a
\]

Normalizing the eigenvector \(|\psi\rangle = \begin{pmatrix} a \\ b \end{pmatrix}\):
\[
|a|^2 + |b|^2 = 1 \implies |a|^2 \left(1 + \tan^2\left(\frac{\theta}{2}\right)\right) = 1
\]
\[
|a|^2 \sec^2\left(\frac{\theta}{2}\right) = 1 \implies |a| = \cos\left(\frac{\theta}{2}\right)
\]

Choosing \(a = \cos\left(\frac{\theta}{2}\right)\) and \(b = \sin\left(\frac{\theta}{2}\right)\), the normalized eigenvector is:
\[
\boxed{\begin{pmatrix} \cos\left(\frac{\theta}{2}\right) \\ \sin\left(\frac{\theta}{2}\right) \end{pmatrix}}
\]

---

# R1 reasoning

Okay, so I need to find the normalized eigenvector of the operator P along an arbitrary direction n in the x-z plane, corresponding to the eigenvalue +ħ/2. Let me see... The components P_x, P_y, and P_z are given as Pauli matrices multiplied by ħ/2. But wait, the direction is in the x-z plane, so the y-component should be zero? Because if the direction is in the x-z plane, then the vector n would have components (sinθ, 0, cosθ), right? So maybe the operator P along n is P·n = sinθ P_x + 0*P_y + cosθ P_z.

Let me confirm. The problem states that P is along an arbitrary direction n lying in the x-z plane. That means n has no y component. So we can parameterize n as (sinθ, 0, cosθ), where θ is the angle from the z-axis to the direction n.

Given that the eigenvalue is +ħ/2, we need to find the eigenvector of the operator P·n = sinθ P_x + cosθ P_z. Since P_x, P_y, P_z are the Pauli matrices multiplied by ħ/2, this operator would be ħ/2 times (sinθ σ_x + cosθ σ_z). So then, P·n = (ħ/2)(sinθ σ_x + cosθ σ_z). 

Therefore, to find the eigenvector with eigenvalue +ħ/2, we need to solve the equation (sinθ σ_x + cosθ σ_z)|ψ> = |ψ>.

Because the eigenvalue equation is (σ·n)|ψ> = |ψ>, since (ħ/2)(σ·n)|ψ> = (ħ/2)|ψ>. So after factoring out ħ/2, the eigenvalue becomes 1 for the matrix (σ·n).

So the matrix we need to consider is:

σ·n = sinθ σ_x + cosθ σ_z = [ [ cosθ, sinθ ], [ sinθ, -cosθ ] ]

Wait, let me compute that explicitly.

The Pauli matrices are:
σ_x = [[0, 1], [1, 0]]
σ_z = [[1, 0], [0, -1]]

Therefore:

sinθ σ_x = [[0, sinθ], [sinθ, 0]]
cosθ σ_z = [[cosθ, 0], [0, -cosθ]]

Adding the two matrices together:

σ·n = [[cosθ, sinθ], [sinθ, -cosθ]]

Wait, hold on:

First component (1,1) is cosθ (from σ_z)
(1,2) is sinθ (from σ_x)
(2,1) is sinθ (from σ_x)
(2,2) is -cosθ (from σ_z)
Yes, that's right.

So the matrix we're dealing with is:
[ cosθ       sinθ     ]
[ sinθ      -cosθ    ]

And we need to find the eigenvector corresponding to eigenvalue +1.

Wait, the eigenvalues of σ·n are ±1, so if the original operator P·n has eigenvalues ±ħ/2. Since we want the eigenvalue +ħ/2, then for the matrix σ·n, we want the eigenvalue +1.

So we need to solve (σ·n)|ψ> = |ψ>.

Let |ψ> = [a, b]^T. Then:

[ cosθ       sinθ     ] [a]   [a]
[ sinθ      -cosθ    ] [b] = [b]

So that leads to two equations:

cosθ * a + sinθ * b = a
sinθ * a - cosθ * b = b

Rearranging the first equation:

cosθ * a + sinθ * b = a
=> (cosθ - 1) * a + sinθ * b = 0

Second equation:

sinθ * a - cosθ * b = b
=> sinθ * a + (-cosθ -1)* b = 0

So we have two equations:

1. (cosθ -1) a + sinθ b = 0
2. sinθ a + (-cosθ -1) b = 0

Let me try to solve these equations. Let's try to express b in terms of a or vice versa.

From equation 1:

(cosθ -1) a + sinθ b = 0 => sinθ b = (1 - cosθ) a => b = [(1 - cosθ)/sinθ] a

Similarly, from equation 2:

sinθ a = (cosθ + 1) b => a = [(cosθ + 1)/sinθ] b

Now, if we take the ratio from both equations.

From equation 1: b/a = (1 - cosθ)/sinθ

From equation 2: a/b = (cosθ +1)/sinθ

Thus, b/a * a/b = [(1 - cosθ)/sinθ] * [ (cosθ +1)/sinθ ] = (1 - cos²θ)/sin²θ) = [sin²θ]/[sin²θ] = 1

Which holds, so the two equations are consistent.

Therefore, just pick one equation to express b in terms of a. Let's use the first equation: b = [(1 - cosθ)/sinθ] a

But we can also recall that 1 - cosθ = 2 sin²(θ/2) and sinθ = 2 sin(θ/2) cos(θ/2), so:

b = [2 sin²(θ/2)] / [2 sin(θ/2) cos(θ/2)] = [sin(θ/2)/cos(θ/2)] a = tan(θ/2) a

Alternatively, using the double-angle formulas:

Alternatively, we can parametrize in terms of θ. Let me think if there's a general expression.

So, since the components are expressed in terms of θ, let's set a, b in terms of θ. Let's also remember that the eigenvector must be normalized. Let me first write the eigenvector in terms of a.

Assuming a is the parameter, then the vector is [a, tan(θ/2) a]^T = a*[1, tan(θ/2)]^T.

To normalize:

|a|^2 (1 + tan²(θ/2)) = 1

Since 1 + tan²x = sec²x, so:

|a|^2 * sec²(θ/2) = 1 => |a| = cos(θ/2)

So taking a = cos(θ/2), then b = tan(θ/2) * cos(θ/2) = sin(θ/2)

Hence, the eigenvector becomes:

[ cos(θ/2), sin(θ/2) ]

But wait, but does this work for all θ?

Wait, but let's check with θ=0. If θ is 0, direction is along +z. Then the eigenvector should be [1, 0], since σ_z has eigenvector [1,0] for +1. Let's see, θ=0, so cosθ=1, sinθ=0, n=(0,0,1).

But in this case, our expression would be [cos(0), sin(0)] = [1,0], which is correct. For θ=π/2, direction along x-axis. Then θ/2= π/4, so the eigenvector would be [cos(π/4), sin(π/4)] = [√2/2, √2/2], which is the eigenvector of σ_x with eigenvalue +1. Indeed, σ_x [1,1]^T = [1,1], no... wait. Let me compute σ_x [a;b] = [b, a]. So [√2/2, √2/2], σ_x acting on it gives [√2/2, √2/2] which is the same vector. So eigenvalue 1. Therefore correct.

Hence, in general, the eigenvector is [cos(θ/2), sin(θ/2)]^T. Let's check for θ=π, direction along -z. Then θ=π, so eigenvector would be [cos(π/2), sin(π/2)] = [0,1], but the eigenvector for σ_z along -z (θ=π) would have eigenvalue -1. Wait, but in our case, we're looking for the eigenvector along n, which at θ=π is -z. Wait, but when θ=π, the matrix σ·n becomes sinπ σ_x + cosπ σ_z = 0 - σ_z, which is -σ_z. The eigenvalue equation would be -σ_z |ψ> = |ψ>, which is σ_z |ψ> = -|ψ>, so eigenvector [0,1]^T, which matches with ours.

Wait, hold on, because θ=π would correspond to the direction along -z. The eigenvalue is +1 for the matrix -σ_z. So we need eigenvector of -σ_z with eigenvalue +1, which is [0,1]^T, which is exactly [cos(π/2), sin(π/2)]^T.

Hence, this seems to be correct. Therefore, the normalized eigenvector is:

[cos(θ/2), sin(θ/2)]^T.

So the elements are cos(θ/2) and sin(θ/2). But since the problem states "along an arbitrary direction n", we might need to express it in terms of the components, but perhaps in the problem's context, they need it in terms of θ, but written as the components. The problem asks for the elements of the normalized eigenvector. But the problem statement might expect the answer written in spherical coordinates terms or something.

Wait, but the problem didn't specify the direction, it's arbitrary in the x-z plane. However, since it's x-z plane, θ is the polar angle from z-axis.

Alternatively, since we are free to parametrize direction n in x-z plane, so maybe the answer is expressed in terms of θ or as cos and sin of θ over 2.

But since the answer is expected in boxed notation, maybe in terms of θ. Alternatively, maybe there's a standard expression. Wait, perhaps the problem expects it written in terms of the components. Let me check the calculation again.

Alternatively, perhaps the answer is something like [e^{-iφ/2} cos(θ/2), e^{iφ/2} sin(θ/2)], but wait, no. Because in x-z plane, but φ is the azimuthal angle, which in x-z plane, φ=0 or π, which would make φ=0 since it's lying in x-z plane (assuming that standard coordinates, where x-z plane is φ=0 and φ=π, but φ=0 is along x-axis). Wait, maybe but the direction is given as n in the x-z plane, so if it's in x-z plane, phi is 0 or pi, but if theta is the polar angle, then the coordinates can be parametrized with phi=0.

But actually, the spin eigenstate for a general direction would normally have a phase factor involving phi, but since here it's in the x-z plane, phi is 0, so perhaps the standard eigenvector is [cos(theta/2), sin(theta/2)] without any phase factors, because phi=0.

So perhaps this is the case.

Alternatively, recall that when you rotate a spin-1/2 state, the eigenvectors are given by this. The general eigenstate for direction n with polar angles theta and phi is:

|n, +> = e^{-i phi/2} cos(theta/2) |+> + e^{i phi/2} sin(theta/2) |->

But if phi=0, since it's in the x-z plane, then phi=0, so the state becomes:

cos(theta/2) |+> + sin(theta/2) |->

Wait, but in terms of components, if |+> is [1,0]^T and |-> is [0,1]^T,

then |n, +> would be [cos(theta/2), sin(theta/2)]^T, which seems to be the same as I got earlier.

Therefore, this must be the answer.

Hence, the normalized eigenvector is [cos(theta/2), sin(theta/2)]^T. 

However, the problem might want the answer expressed in terms of theta. But since the problem didn't specify to leave it in terms of theta but says "along an arbitrary direction n lying in the x-z plane", perhaps they accept this expression. Alternatively, maybe since theta isn't given, I need to check if I need to parametrize it in another way, but given the problem's phrasing, they probably just want the answer in terms of theta. But sticking to their notation, I have θ.

Wait, but maybe they don't require it in terms of θ but as entries in the vector with some expressions. Let's think again. Suppose we write it as:

First component: cos(theta/2)

Second component: sin(theta/2)

But theta is the angle between n and the z-axis. Therefore, perhaps this is acceptable.

Alternatively, maybe we can write this in terms of n's components? Since in x-z plane, n = (nx, 0, nz), with nx^2 + nz^2 =1.

Let me see: expressing in terms of nx and nz.

Since nx = sinθ, nz = cosθ.

Therefore, cos(theta/2) = sqrt[(1 + cosθ)/2] = sqrt[(1 + nz)/2]

Similarly, sin(theta/2) = sqrt[(1 - cosθ)/2] = sqrt[(1 - nz)/2].

But then the numerator can be written as:

But in terms of nx and nz, since sinθ = nx, so sqrt[(1 - cosθ)/2] = sqrt[(1 - nz)/2] = sin(theta/2). Similarly, sqrt[(1 + cosθ)/2] = cos(theta/2). Alternatively, in terms of sqrt expressions.

Alternatively, we can write the eigenvector components in terms of nx and nz.

But given that theta is the polar angle from z-axis, then nx = sinθ and nz = cosθ, therefore, the components of the eigenvector can be written as:

cos(theta/2) = sqrt( (1 + nz)/2 )

sin(theta/2) = sqrt( (1 - nz)/2 )

But if mixed with nx:

But sin(theta/2) = sqrt( (1 - cosθ)/2 ) = sqrt( (1 - nz)/2 )

But since nx = sinθ, then is there a way to write sin(theta/2) in terms of nx?

Hmm:

sin(theta/2) = sqrt( (1 - cosθ)/2 )

But we also know that cosθ = sqrt(1 - nx^2 ), but nz = cosθ. Maybe that's complicating. Alternatively, given that n_x = sinθ, so theta = arcsin(n_x). But anyway, perhaps writing it as cos(theta/2) and sin(theta/2) is sufficient.

Therefore, the elements are cos(theta/2) and sin(theta/2).

But the question just asks for the elements. So probably we need to present the eigenvector as a column vector with entries cos(theta/2) and sin(theta/2), and specify that theta is the angle between n and the z-axis.

Alternatively, maybe the problem expects the answer in terms of components. Wait, in the problem statement, maybe to get a numerical answer, but theta is arbitrary. Therefore, the answer must be in terms of theta. Given that the direction n is along x-z plane, so it should be:

[ cos(theta/2), sin(theta/2) ]

Hence, normalized.

Therefore, the normalized eigenvector is:

[ cos(theta/2) ]

[ sin(theta/2) ]

So, boxed:

\boxed{\begin{pmatrix} \cos(\theta/2) \\ \sin(\theta/2) \end{pmatrix}}

But let me confirm once again. Since the problem said "What are the elements of the normalized eigenvector?" So writing the components in terms of theta over the angle from the z-axis. This seems correct. So θ is the angle between n and the z-axis. Therefore, this is the standard result. I think this is the right answer. I don't see any miscalculations here. 

Alternatively, let me check if in the linear algebra step. Suppose I look back when solving the equations.

We had:

(cosθ - 1) a + sinθ b = 0

sinθ a + (-cosθ -1) b = 0

Taking the first equation:

(cosθ -1) a + sinθ b = 0 => sinθ b = (1 - cosθ) a => b = (1 - cosθ)/sinθ a

Multiply numerator and denominator by (1 + cosθ):

(1 - cosθ)(1 + cosθ)/ sinθ(1 + cosθ) ) a

= [ (1 - cos²θ)/ (sinθ (1 + cosθ)) ] a

= [ sin²θ / (sinθ (1 + cosθ)) ] a

= [ sinθ / (1 + cosθ) ] a

So b = [ sinθ / (1 + cosθ) ] a

But sinθ/(1 + cosθ) = tan(theta/2)

As 1 + cosθ = 2 cos²(theta/2)

sinθ = 2 sin(theta/2) cos(theta/2)

Thus,

sinθ / (1 + cosθ) = [2 sin(theta/2) cos(theta/2)] / [2 cos²(theta/2)] = tan(theta/2)

So same as before. Hence, yes, that leads to b = tan(theta/2) a

Then, normalized. Therefore, writing the normalized components as [cos(theta/2), sin(theta/2)]^T.

So, yes, after normalization, this gives the correct eigenvector. Therefore, the answer is correct.

**Final Answer**
The normalized eigenvector is \boxed{\begin{pmatrix} \cos(\theta/2) \\ \sin(\theta/2) \end{pmatrix}}.


---

