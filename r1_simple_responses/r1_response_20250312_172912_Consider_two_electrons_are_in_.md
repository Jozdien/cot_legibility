# Original Question

Consider two electrons are in p orbital angular momentum state. Ignoring there spin angular momentum, the coupled angular momentum state of the 2-electron system is represented by $|l_1, l_2, l, m> = |1,1, 2, -1>. Here, $l_1, l_2$ are the orbital angular momentum quantum numbers of particles 1 and 2 respectively. And, $l, m$ are the total angular momentum quantum number and the corresponding Z component of the 2-electron system respectively. If measurement is made of the orbital angular momentum components $L_{1z}$ and $L_{2z}$, what is the joint probability of getting the eigenvalues of both $L_{1z}$ and $L_{2z}$ as $-\hbar$?


---

# R1 response

The given coupled state is \( |1, 1, 2, -1\rangle \), which means the total angular momentum quantum numbers are \( l = 2 \) and \( m = -1 \). To find the joint probability of measuring both \( L_{1z} \) and \( L_{2z} \) as \( -\hbar \) (i.e., \( m_1 = -1 \) and \( m_2 = -1 \)), we analyze the expansion of the coupled state in terms of the uncoupled basis states \( |m_1, m_2\rangle \).

The possible combinations of \( m_1 \) and \( m_2 \) must satisfy \( m_1 + m_2 = -1 \) (since \( m = -1 \)). Considering \( l_1 = 1 \) and \( l_2 = 1 \), the valid \( m_1 \) and \( m_2 \) pairs are \( (-1, 0) \) and \( (0, -1) \). The Clebsch-Gordan coefficients for \( |2, -1\rangle \) show that:

\[
|2, -1\rangle = \frac{1}{\sqrt{2}} \left( |-1, 0\rangle + |0, -1\rangle \right).
\]

There is no term \( |-1, -1\rangle \) in this expansion because \( m_1 + m_2 = -2 \) does not match \( m = -1 \). Therefore, the amplitude for \( m_1 = -1 \) and \( m_2 = -1 \) is zero, leading to a joint probability of zero.

**Answer:** The joint probability is \(\boxed{0}\).

---

# R1 reasoning

Okay, so I have this problem here about two electrons in a p orbital angular momentum state. The coupled state is given as |1,1,2,-1>, which I think means that each electron has orbital angular momentum quantum number l1 = l2 = 1 (since they're in p orbitals), and the total orbital angular momentum is l=2 with m=-1. The question is asking for the joint probability of measuring both L1z and L2z as -ħ. Hmm, alright. 

First, I need to recall how angular momentum coupling works. Since the two electrons are in p orbitals, their individual angular momentum quantum numbers are l1 = 1 and l2 = 1. The total angular momentum can range from |l1 - l2| to l1 + l2, which in this case would be from 0 to 2. But the given coupled state is |2, -1>, meaning the total angular momentum l=2 and m=-1. But wait, if this is the state, then I need to express this coupled state in terms of the uncoupled basis states |l1, m1> |l2, m2> to find the probability amplitudes for each combination of m1 and m2. Then, the coefficient for the term where m1 = -1 and m2 = 0 (since m1 + m2 = m_total -1 + 0 = -1?), or wait, m1 + m2 should be equal to m. In this case, m = -1, so m1 + m2 = -1.

But if we want the eigenvalues of L1z and L2z to both be -ħ, that corresponds to m1 = -1 and m2 = -1. Then, m1 + m2 would be -2, which doesn't match the total m of -1 in the coupled state. So is that even possible?

Wait, the coupled state has m = -1. In the uncoupled basis, any combination of m1 and m2 such that m1 + m2 = -1. So possible m1 and m2 pairs would be (-1, 0), (0, -1), (1, -2). But since each individual l is 1, m can only be -1, 0, +1. So actually, possible pairs are (-1,0) and (0,-1). The third possibility would be m1 = 1 and m2 = -2, but m2 can't be -2 because each individual electron has l=1. So only m1=-1 and m2=0 or m1=0 and m2=-1.

Therefore, if the coupled state is expressed in terms of the uncoupled states, only those two combinations contribute. Hence, there is no term with m1=-1 and m2=-1 because their sum would be -2, which doesn't match the total m=-1. Therefore, the probability of measuring both L1z and L2z as -ħ would be zero?

Wait, but that seems too straightforward. Let me make sure.

The coupled state |l, m> = |2, -1> is a combination of the uncoupled states |m1, m2> such that m1 + m2 = -1. To find the expansion coefficients, we would need the Clebsch-Gordan coefficients for combining two l=1 states to get L=2, M=-1.

So to get |2, -1>, it's a linear combination of |m1, m2> where m1 + m2 = -1. The possible m1 and m2 are:

m1 = -1, m2 = 0

m1 = 0, m2 = -1

There's no m1 =1, m2=-2 since m2 can't be -2. Therefore, these are the only terms.

Therefore, the state |2, -1> is a combination of | -1, 0 > and | 0, -1 >. The coefficients can be found using Clebsch-Gordan coefficients.

For two particles with l1=1 and l2=1 coupling to L=2, M=-1.

Recall that the Clebsch-Gordan coefficients can be looked up or calculated. The formula for the coefficient for |l1, l2, m1, m2> in |L, M> is given by some square roots.

Alternatively, maybe I recall the expansion for |2, -1>.

I remember that for the highest weight state |2, 2> is |1,1>|1,1>, right? Then, you apply the lowering operator to get the other states. Let's see.

For L=2, M=2: |1,1>|1,1>.

Apply L- = L1- + L2-

So to get |2,1>, we apply L- to |2,2>:

L- |2,2> = sqrt{(2)(2 + 1) - (2)(2 - 1)} |2,1> = sqrt{6 - 2} |2,1> = sqrt{4} |2,1> = 2|2,1>

But also, applying L1- + L2- to |1,1>|1,1>, we get:

(L1-)|1,1>|1,1> + |1,1>(L2-|1,1>) = sqrt{1(1+1) - 1(1-1)} |1,0>|1,1> + sqrt{1(1+1) -1(1 -1)} |1,1>|1,0>

Which is sqrt{2} |1,0>|1,1> + sqrt{2} |1,1>|1,0>

Therefore, 2|2,1> = sqrt{2}( |1,0>|1,1> + |1,1>|1,0> )

Thus, |2,1> = (1/sqrt{2}) (|1,0>|1,1> + |1,1>|1,0> )

Similarly, lowering again to get |2,0>, let's apply L- again. But maybe it's not necessary. Alternatively, maybe there's a symmetry here.

But perhaps we can use symmetry to figure out the coefficients for |2, -1>.

Since the states with L=2 are symmetric under exchange? Since each p orbital is l=1, and when coupling two symmetric l's, the L=2 and L=0 states are symmetric, and L=1 is antisymmetric? Or wait, actually, under particle exchange, exchanging the two electrons, the angular momentum states will transform based on their total spin. But wait, here we are dealing with orbital angular momentum, not spin. But in any case, perhaps the symmetry of the orbital state.

But this might complicate things. Alternatively, let's try constructing the state |2, -1> by applying the lowering operator twice on |2,1> and then seeing what the coefficients are.

Alternatively, since from |2,1> we have the combination (|0,1> + |1,0>)/sqrt{2}, then applying the lowering operator once more would give |2,0> and can also continue lowering again to get |2, -1>.

Alternatively, perhaps use the fact that the Clebsch-Gordan coefficients for L=2, M=-1 would be the same as for M=1 except with all m's reversed.

That is, similarly, |2, -1> would be ( | -1,0 > + |0, -1> ) / sqrt{2}

Is that correct? Because in the same way that |2, 1> is (|0,1> + |1,0>)/sqrt{2}, perhaps |2, -1> is ( |-1, 0> + |0,-1> ) / sqrt{2}.

If that's the case, then in the state |2,-1>, the possible m1 and m2 are (-1,0) and (0,-1), each with amplitude 1/sqrt{2}, so magnitude squared 1/2 each.

Therefore, if we measure L1z and L2z, the possible outcomes would be either (-1,0) or (0,-1), each with probability 1/2.

But the problem asks for the joint probability of both L1z and L2z being -ħ, i.e., m1 = -1 and m2 = -1. But in the expansion of |2,-1>, that term is not present. Therefore, the coefficient for m1=-1 and m2=-1 is zero. Therefore, the probability is 0.

Therefore, is the answer 0? But I need to confirm that.

Alternatively, perhaps the state |2,-1> is not symmetric? Wait, for two particles with l1=1 and l2=1, the total L=2 states should be symmetric under exchange. Because 1 ⊗1 = 2 ⊕1 ⊕0, where L=2 and L=0 are symmetric and L=1 is antisymmetric. But since we are combining spatial wavefunctions, exchange symmetry would relate to swapping the two particles. However, the original question says "ignoring their spin angular momentum," so we don't need to consider the Pauli exclusion here. The state is purely orbital angular momentum state.

But maybe the Clebsch-Gordan coefficients for certain states account for symmetry. Wait, perhaps not necessarily. Because the Clebsch-Gordan coefficients just give the combination of m1 and m2 that combine to give a certain |L, M>, irrespective of symmetry. So even though L=2 states might be symmetric under exchange, the specific combination of m1 and m2 might not. Wait, no. If m1 and m2 are for different particles, then exchanging particles would swap m1 and m2. Let's see, if you swap particles 1 and 2, then m1 ↔ m2. For |2, M> states, the combination would need to be symmetric. For example, in |2, 1>, which is (|0,1> + |1,0>)/sqrt{2}, swapping m1 and m2 would leave the state invariant. Similarly, |2, -1> would be (| -1,0> + |0,-1>)/sqrt{2}, which is also symmetric under exchange. However, the antisymmetric combinations (for L=1) would be stuff like (|0,1> - |1,0>)/sqrt{2}, etc. But that's aside.

But regardless, in the |2,-1> state, any combination of m1 and m2 that sums to -1 must be considered. Since m can only go from -1 to +1 for each individual l=1. So possible pairs contributing are (-1, 0), (0, -1). Each contributes with equal amplitude 1/sqrt{2}.

Therefore, in the expansion, there is no component where both m1 and m2 are -1. Because that would require m1 + m2 = -2, which isn't the case here which requires m=-1. Therefore, the amplitude for m1 = -1, m2=-1 is zero, hence the probability is 0. So the answer is zero.

But maybe I'm missing something. Maybe there's a more complicated expansion. Wait, the total angular momentum state |2, -1> is a linear combination of the tensor product states |m1, m2> with coefficients given by the Clebsch-Gordan coefficients. So perhaps if I explicitly write that out, I can check.

For two l=1 states coupling to L=2, M=-1.

The Clebsch-Gordan coefficients for l1=1, l2=1, m1, m2, giving L=2, M=m1 + m2= -1. Let's check the table of Clebsch-Gordan coefficients.

Looking up the Clebsch-Gordan coefficients for 1 ⊗ 1 → 2.

The general formula for Clebsch-Gordan coefficients for coupling l1 and l2 to L is non-trivial, but for small l1 and l2, there are tables. 

Alternatively, in the case of coupling two l=1 states, the combinations for L=2 will have the following states:

For M=2: |1,1>
For M=1: (|1,0> + |0,1>)/√2
For M=0: (|1,-1> + |0,0> + |-1,1>)/√3 ??? Wait, no. Actually, wait, the states for L=2 are: for M=2: (1,1), M=1: (1,0)+(0,1) normalized, M=0: sqrt(6)|0,0> plus other terms?

Wait, maybe a better approach: using the formula. Clebsch-Gordan coefficients can be computed via:

⟨ l1 l2 m1 m2 | L M ⟩

But this can be found, for example, by using orthonormality and recursion. 

Alternatively, maybe use the Wigner 3-j symbols, which are related to Clebsch-Gordan coefficients.

The Clebsch-Gordan coefficient ⟨ l1 l2 m1 m2 | L M ⟩ is equal to (-1)^{l1 - l2 + M} sqrt(2L + 1) times the 3-j symbol:

( l1  l2  L

  m1  m2  -M )

So if I look up the 3-j symbol for (1 1 2; -1 0 1) and similar.

Wait, considering the problem where m1 + m2 = M = -1. The coefficients for |2,-1> are the combinations (m1, m2) with m1 + m2 = -1. The possible (m1, m2) are (-1, 0) and (0, -1). Let me compute their Clebsch-Gordan coefficients.

The Clebsch-Gordan coefficient C(l1=1, l2=1, m1=-1, m2=0; L=2, M=-1):

This is analogous to the coefficient for (m1, m2) = (-1,0). Using symmetry relations, perhaps.

Alternatively, from table. For example, let's refer to standard Clebsch-Gordan coefficient tables for 1 ⊗ 1 →2.

Wait, some online resources say:

The CG coefficients for combining l1 = 1, l2 = 1 to L=2 are:

For M = 2:
⟨1 1 1 1 | 2 2⟩ = 1

For M = 1:
⟨1 1 1 0 | 2 1⟩ = sqrt(1/2)
⟨1 1 0 1 | 2 1⟩ = sqrt(1/2)

For M = 0:
⟨1 1 1 -1 | 2 0⟩ = sqrt(1/6)
⟨1 1 0 0 | 2 0⟩ = sqrt(2/3)
⟨1 1 -1 1 | 2 0⟩ = sqrt(1/6)

For M =-1:
⟨1 1 0 -1 | 2 -1⟩ = sqrt(1/2)
⟨1 1 -1 0 | 2 -1⟩ = sqrt(1/2)

For M =-2:
⟨1 1 -1 -1 | 2 -2⟩ =1

So for M = -1, the state |2 -1> is:

sqrt(1/2) |0, -1> + sqrt(1/2)|-1,0>

Therefore, this matches my previous conclusion.

Therefore, the state |2,-1> is indeed ( |-1,0> + |0,-1> ) / sqrt(2)

Therefore, the probability of both L1z and L2z being -1 * ħ (i.e., m1 = -1 and m2 = -1) is zero because that term isn't present in the expansion.

Hence, the joint probability is 0.

But just to ensure that there are no other terms. Are there any other combinations of m1 and m2 where m1 and m2 are both -1? As per the allowable m values for l=1: m can be -1, 0, +1. So m1=-1 and m2=-1 would add up to m=-2, which would be part of the L=2, M=-2 state. Therefore, the state |2,-2> is | -1, -1 >, so only that.

But the given state is |2,-1>, which does not contain the | -1, -1 > component. Therefore, indeed, there is no component where m1 and m2 are both -1. Hence, the probability is zero.

Therefore, the answer should be 0. The joint probability is zero.


---

