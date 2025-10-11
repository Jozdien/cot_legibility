# Original Question

Consider a bound system of two nucleons (NN) in a 1S0 state which emit a particle X of intrinsic parity -1. Pauli statistics require that the isospin, angular momentum, and spin quantum numbers of the final NN state satisfy T(NN) = S(NN) + L(NN) + 1 (mod 2).

Suppose the final NN state has T(NN) = 0. Which of the following partial waves is not permitted, where the lowercase letter denotes the angular momentum state of X? Make use of the conservation of both angular momentum and parity.

Note that the term symbol (e.g. 1S0) is in general defined (2S+1)L(J), where S is the total spin, L the total orbital angular momentum written in spectroscopic notation, and J the total angular momentum.

---

# DeepSeek response (via openrouter)



---

# DeepSeek reasoning (via openrouter)

To solve for which partial wave is not permitted for the emission of a particle $X$ from a bound system of two nucleons in a $^{1}S_{0}$ state where $X$ has an intrinsic parity of $-1$, let us first recall the given condition:

For the final $NN$ state, we need:
$$T(NN) = S(NN) + L(NN) + 1 \pmod{2}.$$
This equation uses Pauli statistics which require that the total wavefunction for identical fermions must be antisymmetric. However, here we need to interpret what this means specifically for two nucleons (which can be either two neutrons, two protons, or one neutron and one proton). 

The total wavefunction for two fermions (which the nucleons are) needs to be antisymmetric:
$$
\Psi_{\text{total}} = \psi_{\text{spin}} \psi_{\text{isospin}} \psi_{\text{space}}.
$$
For two nucleons (which are fermions with spin $1/2$), the total wavefunction should be antisymmetric with respect to the exchange of the two nucleons. 

#### Given:

1. The initial bound state is $^{1}S_{0}$ which translates to:
   - $S = 0$ (since $2S + 1 = 1$, so $2S = 0 \Rightarrow S = 0$).
   - $L = 0$ (since $S$ denotes the $L = 0$ state).
   - $J = 0$ (which is the value indicated in the subscript of $^{1}S_{0}$).

2. The initial state has total angular momentum $J = 0$, total orbital angular momentum $L = $ "S" $= 0$, and total spin $S = 0$.

3. The intrinsic parity of particle $X$ is given to be $-1$.

#### Question Objectives:

1. Conservation of angular momentum: Total angular momentum must be conserved in the reaction. The total angular momentum $J$ for the initial $NN$ $^{1}S_{0}$ state is $J_{i} = 0$. 

2. Conservation of parity: The total parity must be conserveed in the reaction. 

Let us denote the initial nucleon-nucleon bound state as $|^{1}S_{0}\rangle$, which has known values $S_i = 0$, $L_i = 0$, and $J_i = 0$. 

### Step-by-Step Reasoning

Let us first check the angular momentum conservation. Suppose the emitted particle $X$ has angular momentum $l_X$. The angular momentum conservation requires:
$$
\mathbf{J}_{\text{initial}} = \mathbf{J}_{\text{final}} = \mathbf{J}_{NN} \oplus \mathbf{l}_{X},
$$
where $\mathbf{J}_{\text{initial}}$ is the total angular momentum of the initial $NN$ system ($^{1}S_{0}$ state), which is $J_i = 0$, $\mathbf{J}_{NN}$ is the angular momentum quantum number of the final $NN$ system, and $l_{X}$ is the orbital angular momentum quantum number of the emitted particle $X$.

We need to find what values $l_{X}$ can take such that the angular momentum addition rules are satisfied:
$$
\mathbf{J}_{\text{final}} = \mathbf{J}_{NN} \otimes \mathbf{l}_{X} \implies |J_{NN} - l_{X}| \leq J_{\text{final}} \leq |J_{NN} + l_{X}|.
$$
However, $J_{\text{final}}$ should equal $J_{\text{initial}}$, which is $0$, hence:
$$
\mathbf{0} = \mathbf{J}_{NN} \otimes \mathbf{l}_{X}.
$$

Since $J_{\text{final}} = 0$, $J_{NN}$ must equal $l_{X}$ (since $0$ could result from adding $J_{NN}$ with $l_{X}$ such that $|J_{NN} - l_{X}| = 0$, which means $\mathbf{J}_{NN} = l_{X}$). 

#### Now, let us analyze the parity conservation.
The intrinsic parity of two nucleons (proton or neutron) is $+1$ each (both protons and neutrons have an intrinsic parity of $+1$), so the total intrinsic parity of the two nucleons is:
$$
P_{\text{intrinsic}}(NN) = (+1) \times (+1) = +1.
$$
The initial state $^{1}S_{0}$ has $L_i = 0$, so:
$$
P_{\text{initial}} = (P_{\text{intrinsic}}(NN)) \times (-1)^{L_i} = (+1) \times (-1)^0 = +1.
$$
Therefore, the total parity of the initial $^{1}S_{0}$ bound system is $+1$.

#### For the final state, there are three components: the final $NN$ state, the emitted particle $X$, and the relative orbital angular momentum $l_{X}$ between the $NN$ system and $X$. The total parity should be preserved such that:
$$
P_{\text{final}} = P(NN)_{\text{w.r.t. itself}} \times P_{X} \times (-1)^{l_{X}},
$$
where:
$$
P(NN)_{\text{w.r.t. itself}} = (P_{\text{intrinsic}}(NN)) \times (-1)^{L_{NN}}.
$$
Here $L_{NN}$ is the angular momentum state of the $NN$ system after emitting $X$, i.e., the orbital angular momentum in the $NN$ part alone. 

Since $P_{\text{intrinsic}}(NN) = +1$ (as derived earlier), $P(NN)_{\text{w.r.t. itself}}$ becomes:
$$
P(NN)_{\text{w.r.t. itself}} = (+1) \times (-1)^{L_{NN}} = (-1)^{L_{NN}}.
$$
Moreover, the intrinsic parity of particle $X$ is given as $P_{X} = -1$. Thus:
$$
P_{\text{final}} = (-1)^{L_{NN}} \times (-1) \times (-1)^{l_{X}} = (-1)^{L_{NN} + l_{X} + 1}.
$$
Since parity should be conserved, $P_{\text{initial}} = P_{\text{final}}$:
$$
+1 = (-1)^{L_{NN} + l_{X} + 1}.
$$
This implies that $(-1)^{L_{NN} + l_{X} + 1} = +1$, so:
$$
L_{NN} + l_{X} + 1 \text{ must be even.}
$$
This simplifies to:
$$
L_{NN} + l_{X} \text{ should be odd.}
$$
#### Given Pauli statistics for the $NN$ system requires:
$$
T(NN) = S(NN) + L(NN) + 1 \pmod{2}.
$$
The question specifies that the final $NN$ state has $T(NN) = 0$. Plugging $T(NN) = 0$ into the Pauli statistics requirement:
$$
0 = S(NN) + L(NN) + 1 \pmod{2}.
$$
This means that:
$$
S(NN) + L(NN) \equiv 1 \pmod{2}.
$$
Thus $S(NN)$ and $L(NN)$ must have opposite parities such that $S(NN) + L(NN)$ is odd (since one should be odd and the other even).

However, what matters here is that $T(NN) = $ $0$ means that the state is antisymmetric with respect to the isospin part (since symmetric $T(NN) = 1$ states are for $nn$ or $pp$, while antisymmetric $T(NN) = 0$ states are for $np$ mixtures such that the wave function part associated with isospin for $T = 0$ is antisymmetric under particle exchange.

As we need the total wave function to be antisymmetric (since nucleons are fermions), the part of the wave function formed by spin and orbital angular momentum should be symmetric:
$$
0 = \text{[symmetry of isospin part]} + \text{[symmetry of spin part]} + \text{[symmetry of space part]} \pmod{2}.
$$
The total wave function can be decomposed into:
$$
\Psi_{\text{total}} = \psi_{\text{isospin}} \otimes \psi_{\text{spin}} \otimes \psi_{\text{space}}.
$$
For fermions, the total wave function should be antisymmetric:
$$
\text{Antisymmetric} = \text{[symmetry of spin part]} + \text{[symmetry of space part]} + \text{[symmetry of isospin part]},
$$
where symmetric parts are represented by $0$ and antisymmetric by $1$. Thus:
$$
1 = ((1\text{ if antisymmetric, } 0\text{ if symmetric})_{\text{spin}} + (1\text{ if antisymmetric, } 0\text{ if symmetric})_{\text{space}} + (1\text{ if antisymmetric, } 0\text{ if symmetric})_{\text{isospin}}) \pmod{2}.
$$
Another way to phrase what is symmetric or antisymmetric:
1) If $T(NN) = 1$, the isospin part is symmetric.
2) If $T(NN) = 0$, the isospin part is antisymmetric.

So when $T(NN) = 0$, the wave function for isospin part is antisymmetric. Hence, the product $\psi_{\text{spin}} \otimes \psi_{\text{space}}$ must be symmetric to make the total wave function antisymmetric (antisymmetric $\times$ symmetric = antisymmetric).

Conversely:
1) $S(NN) = 0$, spin singlet state $\rightarrow$ spin part is antisymmetric (since two spins are paired oppositely such that the total spin is $0$, which corresponds to an antisymmetric spin state).
2) $S(NN) = 1$, spin triplet state $\rightarrow$ spin part is symmetric.

#### Since $\psi_{\text{spin}} \otimes \psi_{\text{space}}$ must be symmetric:
1) If $S(NN) = 0$ (antisymmetric spin part), the spatial part must also be antisymmetric such that the product $\psi_{\text{spin}} \otimes \psi_{\text{space}}$ is symmetric (since antisymmetric $\times$ antisymmetric $=$ symmetric).
2) If $S(NN) = 1$ (symmetric spin part), the spatial part should also be symmetric such that the product $\psi_{\text{spin}} \otimes \psi_{\text{space}}$ is symmetric (since symmetric $\times$ symmetric $=$ symmetric).

Since symmetric states (which correspond to symmetric parity $(-1)^L$) have $(-1)^L = +1 \implies L$ should be even. Antisymmetric states have $(-1)^L = -1 \implies L$ should be odd. Based on the arguments stated:
- If $S(NN) = 0$, the spin part is antisymmetric. Hence $\psi_{\text{space}}$ should also be antisymmetric. Thus $L(NN)$ should be odd.
- If $S(NN) = 1$, the spin part is symmetric. Hence $\psi_{\text{space}}$ should also be symmetric. Thus $L(NN)$ should be even.

However, we need another part derived previously:
$$
S(NN) + L(NN) \text{ should be odd.}
$$
Thus $S(NN)$ and $L(NN)$ must be such that one is odd and the other is even. 

Now, let us analyze the given options for partial waves where the angular momentum $l_X$ for particle $X$ is represented by lowercase letters ("s," "p," "d," "f," etc., corresponding to $l_X = 0, 1, 2, 3$, etc., respectively).

Based on the angular momentum conservation $J_{\text{initial}} = J_{\text{final}}$, $J_{\text{initial}} = 0$. Therefore:
$$
0 = \mathbf{J}_{NN} \oplus l_{X}.
$$
This implies that $J_{NN} = l_{X}$ such that $\mathbf{J}_{NN} + l_{X}$ must combine to give total angular momentum $0$. Another part of angular momentum conservation which ties $l_{X}$ to $J_{NN}$:
$$
\mathbf{J}_{\text{initial}} = 0 \Rightarrow J_{\text{final}} = 0,
$$
so:
$$
\vec{J}_{\text{final}} = \vec{J}_{NN} + \vec{l_{X}}. 

\text{(This implies $\vec{J}_{NN} = -\vec{l_{X}}$ such that the total angular momentum is zero; hence $l_{X} = J_{NN}$)}
$$
Since $l_{X} = J_{NN}$ and $J_{NN}$ itself is derived from:
$$
\vec{J}_{NN} = \vec{L}_{NN} + \vec{S}_{NN}.
$$
such that:
$$
J_{NN} = |L_{NN} - S_{NN}|, |L_{NN} - S_{NN}| + 1, \dots , L_{NN} + S_{NN}.
$$
But we need $l_{X} = J_{NN}$. 

#### Matching everything step by step again:

1) For $T(NN) = 0$, the isospin part of the two-nucleon state is antisymmetric.
2) The total wave function needs to be antisymmetric, so the spin-space part should be symmetric.
$\Rightarrow$
If $S(NN) = 0$, the spin part is antisymmetric. Hence $L_{NN}$ should be odd to make the overall spin-space part symmetric (antisymmetric spin part and antisymmetric space part).
If $S(NN) = 1$, the spin part is symmetric. Hence $L_{NN}$ should be even (since symmetric spin part requires symmetric space part).

Additionally, $l_{X}$ should satisfy:
#### Parity conservation:
$$
L_{NN} + l_{X} \text{ should be odd}.
$$

Let us define $T(NN) = $ $0$, so $T(NN) $ denotes the isospin state of the final $NN$ system.

For $T(NN) = 0$, the possible values for $S(NN)$ and $L(NN)$ such that $S(NN)}$ and $L(NN)}$ have opposite parities. 

#### Process to verify the given partial waves one by one until finding which one is not allowed.

### For $s$-wave ($l_{X} = 0$):
1. $l_{X} = 0$, thus $J_{NN} = l_{X} = 0$.
2. $J_{NN} = |L_{NN} - S_{NN}|, |L_{NN} - S_{NN}| + 1, \ldots, L_{NN} + S_{NN}$ should include $0$. This means:
    $0 = |L_{NN} - S_{NN}|, |L_{NN} - S_{NN}| + 1, \ldots, L_{NN} + S_{NN}$.
3. For $l_{X} = 0$, $L_{NN}$ needs to be odd to make $L_{NN} + l_{X} = L_{NN} + 0$, which should be odd (hence $L_{NN}$ must be odd).
    
Thus, $l_{X} = 0 \implies L_{NN} + 0\text{ (must be odd)} \implies L_{NN} \text{ is odd}$. Only $L_{NN} = 1, 3, 5, \ldots$ are allowed such that $J_{NN} = 0$. However, $j_{NN} = 0$ implies:
$$
\vec{L}_{NN} + \vec{S}_{NN} = 0,
$$
which means:
$$
L_{NN} = S_{NN}.
$$
However, $S_{NN}$ is either $0$ or $1$ (since $S_{NN}$ is the total spin which can be $0$ for a singlet state or $1$ for a triplet state). Therefore, $L_{NN}$ should be $0$ or $1$. However, here $L_{NN}$ must be odd such that $L_{NN} = 1$. Thus $L_{NN} = S_{NN} = 1$ might seem valid here where $J_{NN} = \vec{L}_{NN} + \vec{S}_{NN}$ forms a $1 \oplus 1$ system whose possible total angular momenta values ($J_{NN}$) are given by:
$$
|L_{NN} - S_{NN}| \text{ to } L_{NN} + S_{NN}.
$$
Since $L_{NN} = 1$ and $S_{NN} = 1$, $J_{NN}$ could be $0, 1,$ or $2$. 

However, another scenario where $l_{X} = 0$ yields $J_{NN} = 0$. Another possibility is $S_{NN} = 0, \, L_{NN} = 0$ such that $\vec{J}_{NN} = 0 + 0 = 0$, so $J_{NN} = 0$. However, $L_{NN}$ should be odd here, thus $L_{NN} = 0$ does not make $ L_{NN}$ odd which is required here. Therefore only $L_{NN} = 1$ makes sense here such that $S_{NN}$ should ideally be $1$ such that $1 \oplus 1$ could produce a $J_{NN} = 0$. 

Thus, let us verify:
$$
\begin{cases}
\text{if } L_{NN} = 1, S_{NN} = 0, \text{ thus } J_{NN} = L_{NN} + S_{NN} = 1,\\
\text{if } L_{NN} = 1, S_{NN} = 1, \text{ we need } J_{NN} = 0:\\
    \text{For } L_{NN} = 1, S_{NN} = 1, J_{NN} \text{ could be } 0, 1, \text{ or } 2. \\
\text{Thus $^3P_{0}$ fits well here such that $L_{NN}=1$, $S_{NN}=1$, $J_{NN}=0$.}
\end{cases}
$$
However, $^3P_{0}$ state satisfies:
1) $P(NN)_{\text{w.r.t. itself}} = (-1)^{L_{NN}} = (-1)^1 = -1.$
2) $P_{\text{final}} = (-1)^{1} \times (-1) \times (-1)^0 = (-1)^{1 + 0 + 

---

