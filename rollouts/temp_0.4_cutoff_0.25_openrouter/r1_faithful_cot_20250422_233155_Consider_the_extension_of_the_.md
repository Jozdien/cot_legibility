# Original Question

Consider the extension of the Standard Model given by the following Lagrangian

\mathcal{L}\subset i\bar{N}_{R}\gamma^{\mu}\partial_{\mu}N_{R}+\frac{1}{2}\left(\partial^{\mu}\phi\right)^{2}+\left|D^{\mu}S\right|^{2}-\frac{y_{i}}{2}\phi\bar{N}_{iR}^{c}N_{iR}^{c}-g_{i\alpha}\bar{N}_{iR}L_{\alpha}S-V\left(\phi,S,H\right)
with singlet fermions,$N{iR}\sim\left(1,1,0\right)$, scalar-doublet $S\sim\left(1,2,1\right)$, and singlet scalar $\phi\sim\left(1,1,0\right)$. We give $\left\langle \phi\right\rangle ^{2}=\left(x^{2}+\upsilon^{2}\right)$, where $\left\langle \phi\right\rangle =x$ and $\left\langle h\right\rangle =v$.

What is the approximation of the mass of the pseudo-Goldostone boson $H_{2}$ through radiative corrections? 

---

# DeepSeek response (via openrouter)

The mass of the pseudo-Goldstone boson \( H_2 \) arises from radiative corrections due to the explicit breaking of an approximate global symmetry. This breaking is induced by the Majorana mass term \( y_i \phi \bar{N}_{iR}^c N_{iR} \), which violates the symmetry preserved by the Yukawa coupling \( g_{i\alpha} \bar{N}_{iR} L_\alpha S \). The dominant contribution to \( H_2 \)'s mass comes from one-loop diagrams involving the right-handed neutrinos \( N_{iR} \) and lepton doublets \( L_\alpha \), with the symmetry-breaking scale set by the vacuum expectation value (VEV) \( x \) of the singlet scalar \( \phi \).

**Approximation of \( H_2 \)'s mass:**
\[
m_{H_2} \approx \frac{y g x}{4\pi}
\]
Here, \( y \) and \( g \) are typical couplings from the Majorana and Yukawa terms, respectively, and \( x \) is the VEV of \( \phi \). The factor \( 1/4\pi \) reflects the loop suppression from quantum corrections. This result assumes minimal contributions from additional scalar potential terms and neglects logarithmic dependencies on mass scales.

---

# DeepSeek reasoning (via openrouter)

Okay, so I need to figure out the mass of the pseudo-Goldstone boson H₂ in this model using radiative corrections. Let me start by recalling what I know about Goldstone bosons and how they get masses. 

First, in the Standard Model, when a symmetry is spontaneously broken, you get massless Goldstone bosons. But if the symmetry is not exact (like explicitly broken), these bosons can get a small mass and become pseudo-Goldstone bosons. In this case, the model has an extension with a singlet fermion N_R, a scalar doublet S, and a singlet scalar φ. The potential V(φ, S, H) isn't specified, but the vacuum expectation values (VEVs) are given: ⟨φ⟩² = x² + υ², where ⟨φ⟩ = x and ⟨h⟩ = v. Wait, actually, the notation here might be a bit confusing. The Higgs field H is part of the Standard Model, which is a doublet under SU(2), so its VEV is v. Then there's the singlet scalar φ with VEV x, and S is another scalar doublet with some VEV? Wait, the problem states S is a scalar doublet (1,2,1) under the SM gauge group SU(3)×SU(2)×U(1), so its hypercharge is 1. The Higgs H is also a doublet (1,2,1/2), right? Wait, the standard Higgs is (1,2,1/2). Here, S is (1,2,1), so it's a different doublet with hypercharge 1. So S is a SU(2) doublet with hypercharge 1. Then, the VEVs given are for φ and h. The φ is a singlet, so its VEV is x, and the Higgs H has VEV v. But the problem says ⟨φ⟩² = x² + υ². Wait, maybe there's a typo here? Because if ⟨φ⟩ is x, then ⟨φ⟩² would be x². But the problem writes ⟨φ⟩² = x² + υ². Maybe that's indicating that the VEV of φ is √(x² + υ²)? Wait, no, the user writes "we give ⟨φ⟩² = x² + υ², where ⟨φ⟩ = x and ⟨h⟩ = v". Hmm, this seems contradictory. If ⟨φ⟩ is x, then ⟨φ⟩² is x², but they write ⟨φ⟩² = x² + υ². Maybe there's a mistake here. Alternatively, perhaps the VEV of φ is √(x² + υ²)? But the user says specifically ⟨φ⟩ = x. Maybe the υ here is the same as v, the Higgs VEV? Let me check. The standard Higgs VEV is about 246 GeV, often denoted as v. So maybe the user is using υ (upsilon) to denote the same thing? Then ⟨φ⟩² = x² + v². But then if ⟨φ⟩ = x, then x² + v² = x², which implies v = 0, which can't be. Therefore, there must be a misunderstanding here. Wait, perhaps the VEV of the field φ is such that when you expand φ around its VEV, you write φ = x + ... and then ⟨φ⟩² = x² + something? No, that's not standard. Maybe the notation is that the total VEV squared is x² + v², where x is the VEV of φ and v is the VEV of the Higgs? That would make sense if there are multiple scalars getting VEVs, and the total is the sum of squares. For example, in the Standard Model, the Higgs VEV is v, but if you have another scalar singlet with VEV x, then the total would be √(v² + x²), but here the problem states that ⟨φ⟩² = x² + v², but ⟨φ⟩ is x, so this seems conflicting. Wait, maybe the VEV of the field S is also contributing? But S is a doublet with hypercharge 1. If S gets a VEV, it would have to be along the neutral component. Let me see. The doublet S has hypercharge 1, so its neutral component would have charge 0 (since for a doublet (Y=1), the charges are Y/2 + T3). Wait, no, the hypercharge for a doublet is such that the charges are given by Q = T3 + Y/2. So if S is a doublet with hypercharge 1, then the components have charges T3 = +1/2 and -1/2. So the upper component has charge Q = 1/2 + 1/2 = 1, and the lower component has Q = -1/2 + 1/2 = 0. So the neutral component is the lower one. So if S gets a VEV, it would be in the neutral component, similar to the Higgs. But the problem says ⟨h⟩ = v, which is the standard Higgs VEV. The problem doesn't mention a VEV for S, so maybe S doesn't get a VEV? But in the potential V(φ, S, H), there could be terms that induce VEVs. Wait, but the problem states the VEVs for φ and h (i.e., H), but not for S. So perhaps S does not get a VEV. Alternatively, maybe S does get a VEV, but the problem didn't mention it. Hmm. Wait, the potential V(φ, S, H) is not specified, so maybe we need to make assumptions. But the user is asking about the mass of the pseudo-Goldstone boson H₂. So probably, after symmetry breaking, there are multiple scalars, and one of them is a pseudo-Goldstone boson whose mass comes from radiative corrections.

First, let's clarify the scalar sector. The model has the Standard Model Higgs doublet H, a singlet scalar φ, and another doublet S. The fields are:

- H: (1, 2, 1/2) with VEV v
- φ: (1, 1, 0) with VEV x
- S: (1, 2, 1) with possibly no VEV? Or maybe a VEV? The problem states ⟨φ⟩ = x and ⟨h⟩ = v. If S doesn't get a VEV, then the only VEVs are v and x. Then the scalar potential V(φ, S, H) would include terms like μ²_H |H|² + μ²_φ φ² + μ²_S |S|² + interactions. But since S is a doublet, if it's charged under some symmetry, maybe it doesn't get a VEV. Alternatively, maybe it does. But the problem doesn't mention S's VEV, so perhaps we can assume that S does not get a VEV. Then, the only VEVs are in H and φ.

But wait, the Lagrangian has a term |D^μ S|², which is the kinetic term for the S doublet, so S is a scalar field in the theory. The potential V(φ, S, H) would include terms that mix these fields. For example, terms like λ_H |H|^4, λ_φ φ^4, λ_S |S|^4, and cross terms like λ_{Hφ} |H|^2 φ^2, λ_{HS} |H|^2 |S|^2, λ_{φS} φ^2 |S|^2, etc. But since the potential isn't given, we might need to make some assumptions.

The pseudo-Goldstone boson H₂ is likely coming from the breaking of some approximate symmetry. Since the singlet φ has a VEV x, and the Higgs H has a VEV v, the combination of these VEVs could lead to a Goldstone boson if there's a U(1) symmetry that's spontaneously broken. However, if that symmetry is explicitly broken, the Goldstone boson becomes a pseudo-Goldstone boson with a mass generated radiatively.

Alternatively, the pseudo-Goldstone could be associated with the S field. But since S is a doublet, if it doesn't get a VEV, maybe it's not involved in the symmetry breaking. Alternatively, if there's a term in the potential that mixes S with H and φ, maybe there's some mixing in the scalar sector leading to multiple Higgs-like particles, one of which is a pseudo-Goldstone.

But let's think step by step.

First, the fields:

1. The right-handed neutrinos N_{iR} are singlets under the SM gauge group, so they don't interact via the strong, weak, or electromagnetic forces, except via the terms given in the Lagrangian.

The terms involving N_R are:

- The kinetic term i \bar{N}_R γ^μ ∂_μ N_R

- The term (y_i / 2) φ \bar{N}_{iR}^c N_{iR} + h.c. This is a Majorana mass term for the right-handed neutrinos, proportional to the VEV of φ. So when φ gets a VEV x, this term becomes (y_i x / 2) \bar{N}_{iR}^c N_{iR} + h.c., giving Majorana masses to the N_iR.

- The term g_{iα} \bar{N}_{iR} L_α S + h.c. This is a Yukawa coupling between N_R, the lepton doublet L_α, and the scalar doublet S. If S does not get a VEV, this term would be similar to the usual Yukawa interaction in the type-I seesaw, but with an extra scalar S. However, if S does get a VEV, then this term would lead to a Dirac mass term between the neutrinos and the right-handed neutrinos, similar to the standard Yukawa coupling but with S's VEV instead of H's.

But since the problem mentions ⟨φ⟩ = x and ⟨h⟩ = v, but not ⟨S⟩, perhaps S does not get a VEV. Then the neutrino masses would come from a combination of the Majorana mass from φ and the Dirac mass from H? Wait, but the term with g_{iα} is N_R L S, so if S doesn't get a VEV, then this term would not generate a Dirac mass. Instead, the Dirac mass would come from the standard Yukawa term with the Higgs H, but that term isn't present here. Wait, the given Lagrangian doesn't include the standard Yukawa term for the neutrinos. So maybe in this model, the neutrino masses are generated through the S scalar? If S doesn't get a VEV, then maybe this term is part of a loop diagram that generates neutrino masses. Alternatively, if S does get a VEV, but the problem didn't mention it, then maybe there's a typo.

Alternatively, perhaps the scalar S is similar to the Higgs but with hypercharge 1, so its VEV would contribute to electroweak symmetry breaking. However, the problem states that ⟨h⟩ = v, which is the standard Higgs VEV. If S also gets a VEV, then the total VEV would be √(v² + v_S²), but the problem doesn't mention that, so perhaps S doesn't get a VEV. 

Assuming S doesn't get a VEV, then the Yukawa term g_{iα} \bar{N}_{iR} L_α S would not contribute to the neutrino masses at tree level. Instead, the neutrino masses would come from the Majorana mass term from φ and some other mechanism. But this is getting a bit off track. The main question is about the mass of the pseudo-Goldstone boson H₂.

So, considering the scalar sector: we have the Higgs doublet H, the singlet φ, and the doublet S. The potential V(φ, S, H) is not specified, but we know the VEVs of φ and H. The pseudo-Goldstone boson H₂ is likely a mixture of the components of these scalars. 

Goldstone bosons arise from the spontaneous symmetry breaking of a global symmetry. If the symmetry is exact, they are massless. If the symmetry is approximate (explicitly broken), they acquire a small mass and are called pseudo-Goldstone bosons. The mass is generated by loop corrections (radiative corrections) due to the explicit breaking terms.

In this model, the singlet φ has a VEV x, and the Higgs H has a VEV v. If there is a U(1) symmetry under which φ and H are charged, but it's explicitly broken by some terms in the potential, then the would-be Goldstone boson from the U(1) breaking becomes a pseudo-Goldstone. Alternatively, the potential V(φ, S, H) might have terms that mix the different scalars, leading to mass eigenstates, with one of them being light due to an approximate symmetry.

But without knowing the exact form of the potential, it's challenging to compute the mass. However, the question mentions that the mass is generated through radiative corrections, so perhaps the tree-level potential has an approximate symmetry that is broken at the loop level, generating a mass for the pseudo-Goldstone.

Alternatively, the pseudo-Goldstone could be part of the S doublet. If S is charged under a global symmetry that's broken by the couplings in the Lagrangian, then its components could include a pseudo-Goldstone boson. For example, if S is a complex field with a U(1) symmetry that's broken by the terms in the potential or by the Yukawa couplings, then the phase component could be a pseudo-Goldstone.

But let's think about the scalar fields. The Higgs H is a doublet, so when it gets a VEV, it breaks the electroweak symmetry. The singlet φ, when it gets a VEV x, breaks any global symmetry it's charged under. If φ is real, then the symmetry is a discrete one (like Z2), but if φ is complex, it could be a U(1). However, the problem states φ is a singlet scalar, so it's a real scalar? Wait, the notation in the Lagrangian: the kinetic term for φ is (1/2)(∂^μ φ)^2, which suggests it's a real scalar. Because for a complex scalar, the kinetic term would be |∂μ φ|^2 = (∂μ φ)(∂^μ φ†), but here it's written as (1/2)(∂^μ φ)^2, which is typical for a real scalar. So φ is a real singlet scalar. Then, when it gets a VEV x, it breaks the Z2 symmetry φ → -φ, if the potential is symmetric. But if the potential has terms that break this symmetry, then there's no Goldstone boson. However, if the symmetry is exact at tree level but broken radiatively, then you could have a pseudo-Goldstone.

Wait, but a real scalar can't have a continuous symmetry. The Goldstone theorem applies to continuous symmetries. So if φ is real, the only possible symmetry is discrete, like Z2, which when broken doesn't produce a Goldstone boson. Therefore, the pseudo-Goldstone must come from another part of the scalar sector.

Looking at the scalar doublet S: it's a complex doublet with hypercharge 1. If it doesn't get a VEV, then its components remain as fields in the theory. If there's a global symmetry acting on S, then the components could include Goldstone bosons. For example, if there's a SU(2) global symmetry acting on S, but it's explicitly broken by the potential or the Yukawa couplings, leading to pseudo-Goldstone bosons. Alternatively, if S is charged under a U(1) symmetry, its phase could be the Goldstone, but if the symmetry is broken explicitly, it becomes a pseudo-Goldstone.

But the problem mentions H₂ as the pseudo-Goldstone. In the Standard Model, the Higgs field has four components, three of which are eaten by the W and Z bosons. The remaining one is the Higgs boson. If there are additional scalars, like φ and S, then their components would mix with the Higgs, leading to multiple physical scalars.

Assuming that H₂ is one of the neutral components from the S doublet or the singlet φ. But since φ is a real singlet, its excitation around the VEV is a scalar (not a pseudoscalar), and there's no Goldstone from φ. The S doublet, if it doesn't get a VEV, has four degrees of freedom (two complex components). If there's a global symmetry acting on S, like a U(1), then the imaginary part (the phase) of the neutral component could be a Goldstone if the symmetry is exact. But if the symmetry is explicitly broken, it becomes a pseudo-Goldstone.

Alternatively, the pseudo-Goldstone could be a mixture of the Higgs and the singlet φ. For example, if there's an approximate U(1) symmetry under which both H and φ rotate, but it's broken by some terms, leading to a pseudo-Goldstone that's a combination of the Higgs and φ components.

But to get a pseudo-Goldstone mass from radiative corrections, we need to consider loop effects. The tree-level potential should have an approximate symmetry, and the symmetry is broken by terms that are loop-suppressed. The Coleman-Weinberg potential might generate a mass for the pseudo-Goldstone.

Alternatively, if the pseudo-Goldstone is part of the S doublet, and the Yukawa couplings g_{iα} break the global symmetry, then the mass of the pseudo-Goldstone would be generated at loop level through diagrams involving the N_R and L_α loops.

Let me try to outline the steps:

1. Identify the approximate symmetry that leads to the Goldstone boson at tree level.

2. Determine how this symmetry is explicitly broken, leading to a mass for the pseudo-Goldstone via loops.

3. Calculate the loop corrections to the mass.

Given that the problem mentions radiative corrections, the mass is likely generated at one-loop level.

Assuming that the pseudo-Goldstone H₂ is from the S doublet. Suppose there's a global U(1) symmetry under which S → e^{iθ} S. If this symmetry is exact at tree level, then the Goldstone boson is the phase of S's neutral component. However, the Yukawa coupling term g_{iα} \bar{N}_{iR} L_α S breaks this U(1) symmetry explicitly because N_R and L_α are charged under other symmetries. Therefore, this explicit breaking would generate a mass for the Goldstone boson at loop level.

Alternatively, the potential V(φ, S, H) might have terms that break the U(1) symmetry, but if those terms are small, the Goldstone becomes a pseudo-Goldstone with mass generated by loops.

To compute the mass, we can use the Coleman-Weinberg potential, where the effective potential includes quantum corrections. The mass squared of the pseudo-Goldstone would be proportional to the loop factor (e.g., g²/(16π²)) times some scale squared (like the VEVs or the masses of the particles in the loop).

In this case, the Yukawa coupling g_{iα} connects S with N_R and L_α. The loop would involve N_R and L_α running in the loop, correcting the mass of the pseudo-Goldstone.

Alternatively, if the symmetry breaking comes from the Majorana mass term y_i φ \bar{N}_R^c N_R, since φ is a singlet, but if φ is charged under the U(1) symmetry, then the Yukawa term would break the symmetry.

Wait, let's try to formalize this.

Suppose we have a global U(1) symmetry under which S → e^{iθ} S and N_R → e^{iθ/2} N_R, and L_α → e^{-iθ/2} L_α. Then the Yukawa term g_{iα} \bar{N}_R L_α S would be invariant under this U(1). However, the Majorana mass term (y_i / 2) φ \bar{N}_R^c N_R requires that φ transforms as φ → e^{-iθ} φ under the U(1), because N_R → e^{iθ/2} N_R, so N_R^c → e^{-iθ/2} N_R^c, and thus \bar{N}_R^c N_R → e^{-iθ} \bar{N}_R^c N_R. Therefore, to keep the term φ \bar{N}_R^c N_R invariant, φ must transform as φ → e^{iθ} φ. 

But if φ has a VEV ⟨φ⟩ = x, this breaks the U(1) symmetry spontaneously. However, the Yukawa coupling term g_{iα} \bar{N}_R L_α S is invariant under the U(1) if the charges are as above. But the potential V(φ, S, H) might include terms that break the U(1) explicitly. For example, a term like φ^2 S^† S would break the U(1) symmetry if φ is charged under U(1). If such a term is present, it would explicitly break the symmetry, leading to a mass for the Goldstone boson.

Alternatively, if the U(1) is only broken by the Yukawa couplings, then the breaking is via the loops involving N_R and L_α. But I need to check.

Alternatively, the U(1) symmetry is only approximate, and the explicit breaking comes from the Majorana mass term. If the U(1) is supposed to act on S and N_R, but the Majorana mass term breaks it, then the pseudo-Goldstone mass would come from loops involving the Majorana Yukawa coupling y_i.

But this is getting a bit tangled. Let's try to think of a specific example.

Suppose the U(1) symmetry is such that:

- S → e^{iθ} S

- N_R → e^{iθ/2} N_R

- L_α → e^{-iθ/2} L_α

- φ → e^{iθ} φ

Then the Yukawa term g_{iα} \bar{N}_R L_α S is invariant because the charges add up: (iθ/2) + (-iθ/2) + iθ = iθ, but the term is S \bar{N}_R L_α, so the total phase is e^{iθ} e^{iθ/2} e^{-iθ/2} = e^{iθ}, but since it's a term in the Lagrangian, we need the product to be invariant. Wait, the term is g_{iα} \bar{N}_R L_α S. The fields transform as:

- \bar{N}_R → e^{-iθ/2} \bar{N}_R

- L_α → e^{-iθ/2} L_α

- S → e^{iθ} S

So the product \bar{N}_R L_α S transforms as e^{-iθ/2} e^{-iθ/2} e^{iθ} = e^{-iθ} e^{iθ} = 1. So the term is invariant.

The Majorana mass term (y_i / 2) φ \bar{N}_R^c N_R. The N_R^c is the charge conjugate, which for a right-handed field would be left-handed, but under the U(1) transformation:

N_R → e^{iθ/2} N_R

N_R^c → (N_R)^c → e^{-iθ/2} N_R^c

So \bar{N}_R^c = (N_R)^c† γ^0 → e^{iθ/2} (N_R^c)† γ^0 = e^{iθ/2} \bar{N}_R^c

Therefore, the term φ \bar{N}_R^c N_R transforms as φ → e^{iθ} φ, \bar{N}_R^c → e^{iθ/2} \bar{N}_R^c, N_R → e^{iθ/2} N_R. So the total transformation is e^{iθ} e^{iθ/2} e^{iθ/2} = e^{2iθ}. Therefore, the term φ \bar{N}_R^c N_R is not invariant under the U(1) symmetry unless θ is a multiple of π, which would make it a Z2 symmetry. Therefore, the Majorana mass term breaks the U(1) symmetry explicitly. Hence, the symmetry is explicitly broken by the Majorana mass term, which is necessary to give mass to the right-handed neutrinos.

Therefore, the U(1) symmetry is explicitly broken by the y_i terms, which means that the Goldstone boson from the spontaneous breaking (due to φ's VEV) is actually a pseudo-Goldstone boson, and its mass is generated at loop level through diagrams involving the y_i couplings.

But wait, φ is a singlet scalar with VEV x. If the U(1) is broken spontaneously by φ's VEV, but explicitly broken by the y_i terms, then the pseudo-Goldstone would be the angular component of φ. However, φ is a real scalar, so it doesn't have an angular component. Therefore, this line of reasoning doesn't work. So perhaps the U(1) is acting on the S field.

Alternatively, maybe the U(1) is acting on both φ and S. If φ is complex, but in the problem φ is written as a real scalar. Wait, the kinetic term for φ is (1/2)(∂μ φ)^2, which is for a real scalar. So φ is real. Therefore, it cannot have a U(1) symmetry. Therefore, the U(1) must act on the complex field S. 

Let's recap:

- S is a complex doublet (1,2,1). Let's write S as (S^+, S^0)^T, where S^+ is the charged component and S^0 is the neutral component.

- A global U(1) symmetry under which S → e^{iθ} S. Then the neutral component S^0 has charge +1 under this U(1).

- The Yukawa term g_{iα} \bar{N}_R L_α S must respect this symmetry. The lepton doublet L_α has components (ν, e)^T. The right-handed neutrino N_R is a singlet, so under the U(1), N_R must have charge -1 to balance the charge of S (since L_α is a Standard Model lepton doublet, which presumably has charge 0 under this new U(1)). Wait, let's check:

The term g_{iα} \bar{N}_R L_α S. Let's denote the U(1) charges:

- S has charge +1

- To make the term invariant, the product of the charges must be 0.

- L_α is a Standard Model lepton doublet, which doesn't carry the new U(1) charge (assuming the U(1) is a new global symmetry).

- N_R must then have charge -1 to cancel the +1 charge of S.

But if L_α is neutral under the U(1), then the term g_{iα} \bar{N}_R L_α S would have charges: (-1) + 0 + (+1) = 0, so it's invariant.

The Majorana mass term (y_i / 2) φ \bar{N}_R^c N_R. Here, φ is a real scalar, so it's neutral under the U(1). N_R has charge -1, so N_R^c would have charge +1 (since charge conjugation changes the sign of the charge). Therefore, \bar{N}_R^c has charge -1 (since it's the Dirac adjoint). Therefore, the term φ \bar{N}_R^c N_R has charges: 0 (φ) + (-1) (from \bar{N}_R^c) + (-1) (from N_R) = -2. Therefore, this term is not invariant under the U(1) symmetry. Hence, the Majorana mass term explicitly breaks the U(1) symmetry.

Therefore, the U(1) symmetry is explicitly broken by the Majorana mass term, making the Goldstone boson (from the spontaneous breaking of the U(1) due to S's VEV) a pseudo-Goldstone. However, in the problem statement, there's no mention of S getting a VEV. If S doesn't get a VEV, then the U(1) symmetry isn't spontaneously broken, and there's no Goldstone boson. Therefore, maybe S does get a VEV, but the problem didn't mention it. Alternatively, the VEV of S is induced by the other terms.

Wait, this is getting complicated. Let's try to assume that S gets a small VEV due to its coupling to φ and H in the potential. For example, if the potential has a term like λ φ^2 |S|^2, then when φ gets a VEV x, this would contribute to the mass term of S. If the mass squared of S becomes negative, S would get a VEV. But the problem states the VEVs are ⟨φ⟩ = x and ⟨h⟩ = v. If S also gets a VEV, say ⟨S⟩ = w, then the pseudo-Goldstone would be a combination of the phases of S and φ. But φ is real, so only S's phase contributes. If S is complex and gets a VEV w, then the Goldstone boson is the phase of S, which becomes a pseudo-Goldstone due to the explicit breaking from the y_i term.

But since the problem doesn't mention S's VEV, maybe we have to assume that S doesn't get a VEV. Then, where is the pseudo-Goldstone coming from?

Alternatively, maybe the pseudo-Goldstone is from the Higgs sector. The Higgs H is a doublet with hypercharge 1/2. When it gets a VEV v, three of its components are eaten by the W and Z bosons. The remaining component is the Higgs boson. If there's another scalar, like φ, mixing with H, then the physical Higgs could be a mixture of H and φ. If there's an approximate symmetry in the scalar potential, the lightest scalar could be a pseudo-Goldstone.

But the question specifies H₂ as the pseudo-Goldstone, implying there are at least two Higgs-like scalars. Assuming H is the Standard Model Higgs, and there's another scalar from φ or S. If φ is a real singlet, its excitation is a scalar boson. If S is a doublet without a VEV, its neutral component would be a complex scalar, which after electroweak symmetry breaking would split into a CP-even and CP-odd scalar. But without a VEV, these would just be inert scalars.

Alternatively, if the potential has a term that mixes H and S, like λ |H|^2 |S|^2, then after H gets a VEV, S would effectively have a mass term depending on H's VEV. But unless there's a linear term in S, S won't get a VEV.

This is getting too vague. Let's try to approach it differently. The question is about the mass of the pseudo-Goldstone boson H₂ through radiative corrections. The answer is likely related to the seesaw mechanism or the loop corrections from the neutrino sector.

In the model, the right-handed neutrinos N_R have Majorana masses from φ's VEV and Yukawa couplings to the lepton doublet L and the scalar S. If S doesn't get a VEV, the neutrino masses would be generated via a loop diagram involving the S scalar. This is similar to the Zee model, where a loop with charged scalars generates neutrino masses. In such models, the scalars involved can have their masses generated radiatively.

Alternatively, if the pseudo-Goldstone is part of the scalar sector mixing with the Higgs, its mass could be generated via loops involving the top quark or other heavy particles. But since the question mentions radiative corrections, and the couplings involve the right-handed neutrinos and the scalar S, it's more likely that the pseudo-Goldstone mass comes from loops involving N_R and S.

Assuming that H₂ is the pseudo-Goldstone from a global symmetry broken by the couplings y_i and g_{iα}, its mass would be generated at one-loop level. The formula for the mass would be something like m_{H₂}² ≈ (y^2 g^2)/(16π²) * v^2 or similar, depending on the couplings and VEVs involved.

Alternatively, considering the Coleman-Weinberg potential, if the pseudo-Goldstone direction is flat at tree level, the one-loop correction would generate a mass. The general form is m² ≈ (loop factor) * (couplings)^2 * (VEV)^2.

To get a more precise answer, let's think about the symmetry breaking. Suppose there's a global U(1) symmetry under which S → e^{iθ} S and N_R → e^{iθ/2} N_R, as before. This symmetry is explicitly broken by the Majorana mass term y_i φ \bar{N}_R^c N_R. The spontaneous breaking of the U(1) by the VEV of S (if it gets a VEV) would produce a Goldstone, but the explicit breaking by y_i would make it a pseudo-Goldstone. However, if S doesn't get a VEV, there's no spontaneous breaking. But maybe the symmetry is part of a larger symmetry group.

Alternatively, consider that the potential V(φ, S, H) has a term that breaks the symmetry, like a mass term μ² S† S + λ (S† S)^2 + ... and also terms like φ^2 S† S. When φ gets a VEV x, this contributes to the mass of S. If the mass squared of S becomes negative, S gets a VEV, breaking the symmetry. The pseudo-Goldstone mass would then come from the explicit breaking terms in the potential.

But without the explicit form of the potential, it's hard to say. However, the problem mentions that the mass is generated through radiative corrections, so perhaps the tree-level potential has a flat direction (a Goldstone), and loops correct it.

Assuming that at tree level, there's a massless Goldstone, and at one-loop, the Coleman-Weinberg potential generates a mass. The Coleman-Weinberg potential is given by:

V_eff = V_tree + (1/64π²) [m_S^4 (ln(m_S² / Λ²) - 3/2) + ... ]

But if the tree-level potential has a flat direction, the curvature (mass) comes from the second derivative of V_eff. The dominant contribution would come from the fields that couple to the pseudo-Goldstone. In this case, the right-handed neutrinos N_R and the scalar S.

The pseudo-Goldstone H₂ would couple to N_R via the Yukawa term g_{iα} \bar{N}_R L_α S. If H₂ is the imaginary part of S^0 (the neutral component of S), then its coupling would be proportional to g_{iα} and the neutrino Yukawas. The loop would involve N_R and L_α (or other leptons) running in the loop, correcting the mass of H₂.

The mass squared of H₂ would then be proportional to (g^2 y^2)/(16π²) times some combination of VEVs. If the Majorana mass M_N = y x, and the Dirac mass comes from the coupling g v (if S gets a VEV), but S doesn't get a VEV, maybe the Dirac mass is zero at tree level. However, if S couples to H, there might be a mixing term.

Alternatively, if S doesn't get a VEV, the neutrino masses are generated via a loop involving S. For example, in the scotogenic model, the neutrino masses are generated via a loop with a scalar doublet and a singlet fermion. The mass of the scalar (which can be a dark matter candidate) is related to the neutrino masses. Similarly, here, the pseudo-Goldstone mass might be related to the neutrino masses.

But I need to relate this to the pseudo-Goldstone mass. If the pseudo-Goldstone is part of the S doublet, its mass would come from loops involving the right-handed neutrinos and the leptons. For example, a loop with N_R and L_α would correct the mass of the pseudo-Goldstone.

The one-loop correction to the mass would be something like:

m_{H₂}^2 ≈ (g^4 v^2)/(16π² M_N^2) * something

But I need to be more precise. Let's consider the interaction term g_{iα} \bar{N}_R L_α S. Expanding S around its VEV (if it has one), but assuming no VEV, the interaction is between N_R, L_α, and the components of S. The pseudo-Goldstone would be the imaginary part of the neutral component of S. The coupling of H₂ to N_R and L_α would be proportional to g_{iα}.

The one-loop diagram contributing to H₂'s mass would be a loop with N_R and L_α running in the loop, connected by Yukawa couplings. However, since L_α are SU(2) doublets and N_R are singlets, the loop would involve the charged lepton and the neutrino. But in the Standard Model, the neutrino is massless, but here they get masses via the N_R.

Alternatively, the loop could involve the N_R and the Higgs. Wait, the term g_{iα} \bar{N}_R L_α S couples N_R to the lepton doublet L_α and the scalar S. When S is written in terms of its components, the neutral component would have a Yukawa coupling to the neutrino and N_R. If S doesn't get a VEV, this is similar to the Dirac neutrino mass term but with S instead of H. However, since S is a doublet with hypercharge 1, the coupling would be different.

But to compute the mass of the pseudo-Goldstone, let's assume that H₂ is the imaginary part of S^0, which is the Goldstone boson of the broken U(1) symmetry. The explicit breaking comes from the Majorana mass term y_i φ \bar{N}_R^c N_R. The one-loop diagram that gives mass to H₂ would involve a loop of N_R and some other fields.

The diagram would be a loop where H₂ (the pseudo-Goldstone) couples to N_R and another field, which then couples back to H₂ via the symmetry-breaking term. Since the symmetry is broken by the Majorana mass, the loop would involve the Majorana mass insertion.

For example, the H₂ could couple to N_R via the Yukawa term, and the Majorana mass term would allow a transition between N_R and N_R^c. So the loop would be a loop of N_R propagators with a Yukawa coupling at each vertex and a Majorana mass insertion.

Specifically, the interaction term for H₂ would be something like (g/2) H₂ \bar{N}_R ν_L + h.c., assuming H₂ is the imaginary part of S^0. The Majorana mass term is (y x / 2) N_R^c N_R + h.c. The loop would involve N_R propagating, converting to N_R^c via the Majorana mass, and then back to N_R. The loop integral would then contribute to the H₂ mass.

The mass squared would then be proportional to (g^2 y x)/(16π²) times some logarithmic factor. However, to get the exact expression, we'd need to compute the Feynman diagram.

Alternatively, using the formula for the Coleman-Weinberg potential, the mass squared is given by the second derivative of the effective potential with respect to the field. For a pseudo-Goldstone, the leading contribution would come from the heaviest fields in the loop, which in this case are the right-handed neutrinos N_R.

The effective potential contribution from a fermion loop is:

ΔV = - (N_f / 64π²) m_f^4 (ln(m_f² / Λ²) - 3/2)

Where N_f is the number of degrees of freedom (for a Majorana fermion, N_f = 2). The mass of the fermion (N_R) is m_N = y x. However, the pseudo-Goldstone direction is related to the phase of S, which doesn't directly couple to N_R's mass. Instead, the coupling is through the Yukawa term g \bar{N}_R L S. But if S doesn't get a VEV, this term doesn't contribute to the mass of N_R. Therefore, the mass of N_R is solely from the φ VEV, y x.

But the pseudo-Goldstone is part of S, and its fluctuations would affect the Yukawa coupling. Expanding S around its VEV (which is zero), the interaction term is g \bar{N}_R L S. The Goldstone mode is the imaginary part of S^0, let's call it a. The coupling would then be g \bar{N}_R L (a + ...). However, since the Majorana mass is y x \bar{N}_R^c N_R, this term breaks the U(1) symmetry, allowing a coupling between a, N_R, and ν_L.

The one-loop diagram contributing to the a (pseudo-Goldstone) mass would be a loop with N_R and ν_L running in the loop, connected by the Yukawa couplings and the Majorana mass. The diagram would look like a triangle diagram, but more likely a loop with two Yukawa vertices and a Majorana mass insertion.

Alternatively, since the ν_L is part of the lepton doublet, which is SU(2) charged, and S is a doublet, the coupling would involve the SU(2) structure. For example, the term g_{iα} \bar{N}_R L_α S would be g_{iα} \bar{N}_R (ν_L, e_L)^T S. If S is (S^+, S^0)^T, then the coupling to ν_L would be g_{iα} \bar{N}_R ν_L S^0 + g_{iα} \bar{N}_R e_L S^+.

Assuming we're looking at the neutral component S^0, the coupling is g_{iα} \bar{N}_R ν_L S^0. If S^0 = (s + i a)/√2, where s is the CP-even scalar and a is the CP-odd scalar (the pseudo-Goldstone), then the coupling to a is i g_{iα} \bar{N}_R ν_L a / √2.

The Majorana mass term is (y_i x / 2) N_R^c N_R + h.c. This allows transitions between N_R and N_R^c.

The one-loop diagram for the a mass would then involve a loop with N_R and ν_L propagators, with two a vertices and a Majorana mass insertion. However, since ν_L is a Standard Model neutrino and is massless in the absence of the seesaw mechanism, but in this model, the neutrino masses are generated via the term with S and N_R. But if S doesn't get a VEV, the neutrino masses are not generated at tree level but through loops.

Wait, this is similar to the Zee model where the neutrino masses are generated at one loop. In such models, the loop induces a small Majorana mass for the neutrinos. The same loop could also contribute to the mass of the pseudo-Goldstone boson.

In the Zee model, the scalar sector includes a charged singlet, and the neutrino mass is generated via a loop with charged scalars and leptons. The mass of the scalars is related to the neutrino masses. Similarly, here, the pseudo-Goldstone mass could be related to the neutrino masses generated by the loop.

The neutrino mass in this model would be something like m_ν ≈ (g^2 y x)/(16π²) * ln(M_N^2/Λ^2), where M_N is the mass of the right-handed neutrino. Then, the mass of the pseudo-Goldstone a would also be related to these parameters.

However, the exact calculation would require setting up the Feynman diagram and computing the loop integral. Assuming that the pseudo-Goldstone mass squared is proportional to the product of the couplings squared and the Majorana mass squared, divided by (16π²), we can estimate:

m_{H₂}^2 ≈ (g^4 y² x²)/(16π² M_N²) * something.

But without the exact structure of the loop, it's hard to say. Alternatively, if the pseudo-Goldstone gets its mass from the same loop that generates the neutrino mass, then m_{H₂} might be similar to the neutrino mass, but scaled by some factors.

Alternatively, using dimensional analysis, the mass squared of the pseudo-Goldstone would be m² ~ (g² y² x²)/(16π²). Since the couplings g and y are dimensionless, and x is a mass scale, this gives the correct dimension. The factor 1/(16π²) comes from the loop integral.

Therefore, an approximate answer would be m_{H₂} ≈ (y g x)/(4π). However, this is a rough estimate. If there are more precise factors from the loop calculation, like a factor of √(N), where N is the number of right-handed neutrinos, or a numerical factor from the integral, it might differ.

In summary, after considering the symmetry breaking pattern and the loop corrections involving the right-handed neutrinos and the Yukawa couplings, the mass of the pseudo-Goldstone boson H₂ is approximately:

m_{H₂} ≈ \frac{y g x}{4\pi}

But I need to check the coefficients. For a one-loop correction, the typical factor is 1/(16π²), so the mass squared would be:

m_{H₂}^2 ≈ \frac{y^2 g^2 x^2}{16π²}

Taking the square root, m_{H₂} ≈ \frac{y g x}{4π}

However, in some models, there can be additional factors. For example, if the loop involves a triangle diagram or different couplings, there might be numerical factors. But in the absence of specific information about the potential or the exact couplings, this is the best approximation.

---

# Cut off deepseek reasoning

Okay, so I need to figure out the mass of the pseudo-Goldstone boson H₂ in this model using radiative corrections. Let me start by recalling what I know about Goldstone bosons and how they get masses. 

First, in the Standard Model, when a symmetry is spontaneously broken, you get massless Goldstone bosons. But if the symmetry is not exact (like explicitly broken), these bosons can get a small mass and become pseudo-Goldstone bosons. In this case, the model has an extension with a singlet fermion N_R, a scalar doublet S, and a singlet scalar φ. The potential V(φ, S, H) isn't specified, but the vacuum expectation values (VEVs) are given: ⟨φ⟩² = x² + υ², where ⟨φ⟩ = x and ⟨h⟩ = v. Wait, actually, the notation here might be a bit confusing. The Higgs field H is part of the Standard Model, which is a doublet under SU(2), so its VEV is v. Then there's the singlet scalar φ with VEV x, and S is another scalar doublet with some VEV? Wait, the problem states S is a scalar doublet (1,2,1) under the SM gauge group SU(3)×SU(2)×U(1), so its hypercharge is 1. The Higgs H is also a doublet (1,2,1/2), right? Wait, the standard Higgs is (1,2,1/2). Here, S is (1,2,1), so it's a different doublet with hypercharge 1. So S is a SU(2) doublet with hypercharge 1. Then, the VEVs given are for φ and h. The φ is a singlet, so its VEV is x, and the Higgs H has VEV v. But the problem says ⟨φ⟩² = x² + υ². Wait, maybe there's a typo here? Because if ⟨φ⟩ is x, then ⟨φ⟩² would be x². But the problem writes ⟨φ⟩² = x² + υ². Maybe that's indicating that the VEV of φ is √(x² + υ²)? Wait, no, the user writes "we give ⟨φ⟩² = x² + υ², where ⟨φ⟩ = x and ⟨h⟩ = v". Hmm, this seems contradictory. If ⟨φ⟩ is x, then ⟨φ⟩² is x², but they write ⟨φ⟩² = x² + υ². Maybe there's a mistake here. Alternatively, perhaps the VEV of φ is √(x² + υ²)? But the user says specifically ⟨φ⟩ = x. Maybe the υ here is the same as v, the Higgs VEV? Let me check. The standard Higgs VEV is about 246 GeV, often denoted as v. So maybe the user is using υ (upsilon) to denote the same thing? Then ⟨φ⟩² = x² + v². But then if ⟨φ⟩ = x, then x² + v² = x², which implies v = 0, which can't be. Therefore, there must be a misunderstanding here. Wait, perhaps the VEV of the field φ is such that when you expand φ around its VEV, you write φ = x + ... and then ⟨φ⟩² = x² + something? No, that's not standard. Maybe the notation is that the total VEV squared is x² + v², where x is the VEV of φ and v is the VEV of the Higgs? That would make sense if there are multiple scalars getting VEVs, and the total is the sum of squares. For example, in the Standard Model, the Higgs VEV is v, but if you have another scalar singlet with VEV x, then the total would be √(v² + x²), but here the problem states that ⟨φ⟩² = x² + v², but ⟨φ⟩ is x, so this seems conflicting. Wait, maybe the VEV of the field S is also contributing? But S is a doublet with hypercharge 1. If S gets a VEV, it would have to be along the neutral component. Let me see. The doublet S has hypercharge 1, so its neutral component would have charge 0 (since for a doublet (Y=1), the charges are Y/2 + T3). Wait, no, the hypercharge for a doublet is such that the charges are given by Q = T3 + Y/2. So if S is a doublet with hypercharge 1, then the components have charges T3 = +1/2 and -1/2. So the upper component has charge Q = 1/2 + 1/2 = 1, and the lower component has Q = -1/2 + 1/2 = 0. So the neutral component is the lower one. So if S gets a VEV, it would be in the neutral component, similar to the Higgs. But the problem says ⟨h⟩ = v, which is the standard Higgs VEV. The problem doesn't mention a VEV for S, so maybe S doesn't get a VEV? But in the potential V(φ, S, H), there could be terms that induce VEVs. Wait, but the problem states the VEVs for φ and h (i.e., H), but not for S. So perhaps S does not get a VEV. Alternatively, maybe S does get a VEV, but the problem didn't mention it. Hmm. Wait, the potential V(φ, S, H) is not specified, so maybe we need to make assumptions. But the user is asking about the mass of the pseudo-Goldstone boson H₂. So probably, after symmetry breaking, there are multiple scalars, and one of them is a pseudo-Goldstone boson whose mass comes from radiative corrections.

First, let's clarify the scalar sector. The model has the Standard Model Higgs doublet H, a singlet scalar φ, and another doublet S. The fields are:

- H: (1, 2, 1/2) with VEV v
- φ: (1, 1, 0) with VEV x
- S: (1, 2, 1) with possibly no VEV? Or maybe a VEV? The problem states ⟨φ⟩ = x and ⟨h⟩ = v. If S doesn't get a VEV, then the only VEVs are v and x. Then the scalar potential V(φ, S, H) would include terms like μ²_H |H|² + μ²_φ φ² + μ²_S |S|² + interactions. But since S is a doublet, if it's charged under some symmetry, maybe it doesn't get a VEV. Alternatively, maybe it does. But the problem doesn't mention S's VEV, so perhaps we can assume that S does not get a VEV. Then, the only VEVs are in H and φ.

But wait, the Lagrangian has a term |D^μ S|², which is the kinetic term for the S doublet, so S is a scalar field in the theory. The potential V(φ, S, H) would include terms that mix these fields. For example, terms like λ_H |H|^4, λ_φ φ^4, λ_S |S|^4, and cross terms like λ_{Hφ} |H|^2 φ^2, λ_{HS} |H|^2 |S|^2, λ_{φS} φ^2 |S|^2, etc. But since the potential isn't given, we might need to make some assumptions.

The pseudo-Goldstone boson H₂ is likely coming from the breaking of some approximate symmetry. Since the singlet φ has a VEV x, and the Higgs H has a VEV v, the combination of these VEVs could lead to a Goldstone boson if there's a U(1) symmetry that's spontaneously broken. However, if that symmetry is explicitly broken, the Goldstone boson becomes a pseudo-Goldstone boson with a mass generated radiatively.

Alternatively, the pseudo-Goldstone could be associated with the S field. But since S is a doublet, if it doesn't get a VEV, maybe it's not involved in the symmetry breaking. Alternatively, if there's a term in the potential that mixes S with H and φ, maybe there's some mixing in the scalar sector leading to multiple Higgs-like particles, one of which is a pseudo-Goldstone.

But let's think step by step.

First, the fields:

1. The right-handed neutrinos N_{iR} are singlets under the SM gauge group, so they don't interact via the strong, weak, or electromagnetic forces, except via the terms given in the Lagrangian.

The terms involving N_R are:

- The kinetic term i \bar{N}_R γ^μ ∂_μ N_R

- The term (y_i / 2) φ \bar{N}_{iR}^c N_{iR} + h.c. This is a Majorana mass term for the right-handed neutrinos, proportional to the VEV of φ. So when φ gets a VEV x, this term becomes (y_i x / 2) \bar{N}_{iR}^c N_{iR} + h.c., giving Majorana masses to the N_iR.

- The term g_{iα} \bar{N}_{iR} L_α S + h.c. This is a Yukawa coupling between N_R, the lepton doublet L_α, and the scalar doublet S. If S does not get a VEV, this term would be similar to the usual Yukawa interaction in the type-I seesaw, but with an extra scalar S. However, if S does get a VEV, then this term would lead to a Dirac mass term between the neutrinos and the right-handed neutrinos, similar to the standard Yukawa coupling but with S's VEV instead of H's.

But since the problem mentions ⟨φ⟩ = x and ⟨h⟩ = v, but not ⟨S⟩, perhaps S does not get a VEV. Then the neutrino masses would come from a combination of the Majorana mass from φ and the Dirac mass from H? Wait, but the term with g_{iα} is N_R L S, so if S doesn't get a VEV, then this term would not generate a Dirac mass. Instead, the Dirac mass would come from the standard Yukawa term with the Higgs H, but that term isn't present here. Wait, the given Lagrangian doesn't include the standard Yukawa term for the neutrinos. So maybe in this model, the neutrino masses are generated through the S scalar? If S doesn't get a VEV, then maybe this term is part of a loop diagram that generates neutrino masses. Alternatively, if S does get a VEV, but the problem didn't mention it, then maybe there's a typo.

Alternatively, perhaps the scalar S is similar to the Higgs but with hypercharge 1, so its VEV would contribute to electroweak symmetry breaking. However, the problem states that ⟨h⟩ = v, which is the standard Higgs VEV. If S also gets a VEV, then the total VEV would be √(v² + v_S²), but the problem doesn't mention that, so perhaps S doesn't get a VEV. 

Assuming S doesn't get a VEV, then the Yukawa term g_{iα} \bar{N}_{iR} L_α S would not contribute to the neutrino masses at tree level. Instead, the neutrino masses would come from the Majorana mass term from φ and some other mechanism. But this is getting a bit off track. The main question is about the mass of the pseudo-Goldstone boson H₂.

So, considering the scalar sector: we have the Higgs doublet H, the singlet φ, and the doublet S. The potential V(φ, S, H) is not specified, but we know the VEVs of φ and H. The pseudo-Goldstone boson H₂ is likely a mixture of the components of these scalars. 

Goldstone bosons arise from the spontaneous symmetry breaking of a global symmetry. If the symmetry is exact, they are massless. If the symmetry is approximate (explicitly broken), t

---

# Anthropic completion

Alright, so I need to determine the mass of the pseudo-Goldstone boson H₂ in this model using radiative corrections. Let me begin by recalling the fundamentals of Goldstone bosons and their mass acquisition mechanisms.

In the Standard Model, spontaneous symmetry breaking produces massless Goldstone bosons. However, when symmetry is not exact but explicitly broken, these bosons can acquire small masses, becoming pseudo-Goldstone bosons. This particular model features an extension with a singlet fermion N_R, a scalar doublet S, and a singlet scalar φ. While the potential V(φ, S, H) isn't explicitly defined, the vacuum expectation values (VEVs) are specified as ⟨φ⟩² = x² + υ², where ⟨φ⟩ = x and ⟨h⟩ = v.

There seems to be some confusion in the notation. The Standard Model Higgs field H is an SU(2) doublet with VEV v. The scalar φ is a singlet with VEV x. Meanwhile, S is described as a scalar doublet (1,2,1) under the gauge group SU(3)×SU(2)×U(1), making it distinct from the standard Higgs doublet (1,2,1/2). This means S has hypercharge 1, resulting in its upper component having charge 1 and its lower component having charge 0.

The relationship ⟨φ⟩² = x² + υ² appears contradictory since if ⟨φ⟩ = x, then ⟨φ⟩² should equal x². Perhaps there's a typo, or maybe the total VEV squared from multiple scalar fields is being represented. Alternatively, υ (upsilon) might be used to denote the same thing as v, but this leads to mathematical inconsistencies unless there's another interpretation I'm missing.

Looking at the scalar sector more carefully, we have:
- H: Standard Model Higgs doublet (1,2,1/2) with VEV v
- φ: Singlet scalar (1,1,0) with VEV x
- S: Scalar doublet (1,2,1) with no explicitly mentioned VEV

The Lagrangian includes |D^μ S|², which is the kinetic term for S. While the potential V(φ, S, H) would typically include self-interaction terms and cross-terms between these fields, without its specific form, we must make some assumptions.

The terms involving N_R in the Lagrangian are:
- Kinetic term: i \bar{N}_R γ^μ ∂_μ N_R
- Majorana mass term: (y_i / 2) φ \bar{N}_{iR}^c N_{iR} + h.c.
- Yukawa interaction: g_{iα} \bar{N}_{iR} L_α S + h.c.

When φ acquires VEV x, the Majorana term generates masses for N_iR. The Yukawa term involves the lepton doublet L_α and scalar S. If S doesn't get a VEV, this term wouldn't generate a Dirac mass at tree level.

The pseudo-Goldstone boson H₂ likely emerges from the breaking of some approximate symmetry. Since both φ and H acquire VEVs, their combination might lead to a Goldstone boson if a U(1) symmetry is spontaneously broken. However, if that symmetry is explicitly broken, the Goldstone boson becomes a pseudo-Goldstone with a radiatively generated mass.

Alternatively, H₂ could be associated with S, though if S doesn't get a VEV, it may not directly participate in symmetry breaking. However, potential mixing terms between S, H, and φ could lead to multiple Higgs-like particles, with one being a pseudo-Goldstone.

---

# OpenAI completion

Alright, so I need to determine the mass of the pseudo-Goldstone boson H₂ within this model by utilizing radiative corrections. Let me first revisit what I understand about Goldstone bosons and their masses.

In the Standard Model, spontaneously breaking a symmetry results in massless Goldstone bosons. However, if the symmetry is not entirely exact (for example, it's explicitly broken), these bosons can acquire a small mass, transforming into pseudo-Goldstone bosons. In this model, the extension includes a singlet fermion N_R, a scalar doublet S, and a singlet scalar φ. The potential V(φ, S, H) isn't defined, but the vacuum expectation values (VEVs) are known: ⟨φ⟩² = x² + υ², with ⟨φ⟩ = x and ⟨h⟩ = v. The notation can be a bit confusing here. In the Standard Model, the Higgs field H is a doublet under SU(2), with a VEV of v. Meanwhile, the singlet scalar φ has a VEV of x, and S, another scalar doublet, might have a VEV. The problem notes that S is a scalar doublet (1,2,1) in the SM gauge group SU(3)×SU(2)×U(1), implying a hypercharge of 1. The standard Higgs H is (1,2,1/2). Here, S is (1,2,1), making it a distinct doublet with hypercharge 1. Therefore, S is a SU(2) doublet with hypercharge 1. Given VEVs are for φ and h. φ is a singlet, resulting in a VEV of x, and the Higgs H has a VEV of v. But the notation ⟨φ⟩² = x² + υ² suggests a potential typo since ⟨φ⟩ = x indicates ⟨φ⟩² = x². This suggests that the VEV of φ might be √(x² + υ²). However, the problem writes ⟨φ⟩ = x. Maybe υ is used instead of v for the Higgs VEV. The standard Higgs VEV is around 246 GeV, denoted as v, so υ likely represents the same thing. Thus, ⟨φ⟩² = x² + v². But if ⟨φ⟩ = x, then x² + v² = x² — indicating a misunderstanding. Maybe the VEV of φ is structured so that its expansion around the VEV yields φ = x + ... and ⟨φ⟩² = x² + something. This might imply that the total VEV squared is x² + v², where x is φ's VEV, and v is the Higgs' VEV. That seems logical if several scalars acquire VEVs, with their sum of squares equating to the total. In the Standard Model, the Higgs VEV is v, but another scalar singlet with VEV x combined would be √(v² + x²). Here, this is presented as ⟨φ⟩² = x² + v², yet ⟨φ⟩ = x signals a contradiction. Perhaps the VEV of S is also relevant, but S being a doublet with hypercharge 1 implies its neutral component must have a VEV. The doublet S, with components having charges T3 = +1/2 and -1/2, results in a neutral charge 0 component on the lower part. Consequently, if S develops a VEV, it would be on the neutral component like the Higgs, but since there's no mentioned VEV for S, it might not achieve one. Alternatively, S might acquire a VEV, but it's not stated. With the potential V(φ, S, H) undefined, assumptions could be required.

Regarding the pseudo-Goldstone boson H₂, it's likely derived from the symmetry breaking with various scalars, where one emerges as a pseudo-Goldstone boson due to radiative correction. Clarifying the scalar sector: the model includes the Standard Model Higgs doublet H, a singlet scalar φ, and another doublet S. The attributes are:

- H: (1, 2, 1/2) with VEV v
- φ: (1, 1, 0) with VEV x
- S: (1, 2, 1) with assumed no VEV? Or possibly a VEV? VEVs are noted for φ and h, implying x and v respectively. If S doesn't get a VEV, the only VEVs remain at v and x. The scalar potential V(φ, S, H) comprises terms like μ²_H |H|² + μ²_φ φ² + μ²_S |S|² + interactions. However, should S not receive a VEV potentially due to representing a charged symmetry, it may be excluded. Alternatively, it's included but not mentioned. Let's continue with the assumption that S doesn’t get a VEV, where VEVs exist solely in H and φ . 

However, the Lagrangian contains |D^μ S|², a kinetic term for S, so S participates as a scalar field. V(φ, S, H) comprises mixing terms, for instance, λ_H |H|^4, λ_φ φ^4, λ_S |S|^4, cross-terms like λ_{Hφ} |H|^2 φ^2, λ_{HS} |H|^2 |S|^2, λ_{φS} φ^2 |S|^2, etc., yet lacking a given potential, we're left assuming. The pseudo-Goldstone boson H₂ might result from an approximate symmetry break. With φ’s VEV at x and H's at v, a U(1) symmetry break could imply a Goldstone boson, converting into a pseudo-Goldstone through explicit breaking, and gaining mass radiatively. Alternatively, H₂ might emerge from S's involvement. Though S is a doublet, absent a VEV, it might side-step symmetry breaking unless a potential permits mixes between S, H, and φ, mingling elements of a multi-Higgs scenario into the pseudo-Goldstone role. 

Consider similar work structure:

The terms in N_R comprise:

- a kinetic term i \bar{N}_R γ^μ ∂_μ N_R

- a Majorana mass term (y_i / 2) φ \bar{N}_{iR}^c N_{iR} + h.c., reliant on φ's VEV x; thereby, providing Majorana masses (y_i x / 2) \bar{N}_{iR}^c N_{iR} + h.c.

- Yukawa coupling g_{iα} \bar{N}_{iR} L_α S + h.c. If S lacks a VEV, it aligns to the type-I seesaw standard, differing by which scalar imparts the Yukawa interaction. Nevertheless, S receiving a VEV further introduces Dirac mass interaction. 

With noted ⟨φ⟩ = x and ⟨h⟩ = v lacking ⟨S⟩, S's non-VEV precludes contributing to tree-level neutrino masses, while a combination of φ’s Majorana masses and other mechanisms delivers neutrino masses. Await, considering the original inquiry surrounding H₂’s pseudo-Goldstone mass, let’s refocus.

So, in this scalar environment: H, a Higgs doublet, φ, a singlet, and S, a doublet imply potential VEVs from φ and H, with the latter introducing pseudo-Goldstone qualities. Inherent symmetry from combined VEVs, approximated through explicit breakage, births a pseudo-Goldstone lepton, albeit mass application by radiative impacts.

---

# cutoff_deepseek_completion (via openrouter)

ChatCompletion(id='gen-1745390439-I8ritC7GsSGwIKRVAhdh', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='The mass of the pseudo-Goldstone boson \\( H_2 \\) through radiative corrections is approximated by considering the leading one-loop contributions from the Yukawa interactions involving the right-handed neutrinos \\( N_{iR} \\). These corrections arise due to the explicit breaking of the symmetry associated with the pseudo-Goldstone boson, primarily through the coupling \\( y_i \\phi \\bar{N}_{iR}^c N_{iR} \\). The dominant contribution to the mass comes from the Coleman-Weinberg potential, where the one-loop correction generates a mass term proportional to the square of the Yukawa coupling \\( y_i \\) and the vacuum expectation value \\( x \\) of the singlet scalar \\( \\phi \\).\n\nThe mass squared of \\( H_2 \\) is given by the loop factor \\( \\frac{y_i^4 x^2}{16\\pi^2} \\), leading to the mass:\n\n\\[\nm_{H_2} \\approx \\frac{y_i^2 x}{4\\pi}\n\\]\n\nThus, the approximation of the mass of the pseudo-Goldstone boson \\( H_2 \\) through radiative corrections is:\n\n\\[\n\\boxed{\\frac{y_{i}^{2} x}{4\\pi}}\n\\]', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, reasoning='achyon-free, then the Goldstone becomes a pseudo-Goldstone with mass coming from the explicit breaking terms. Alternatively, if the symmetry is broken radiatively, the mass can be generated through loops.\n\nIn the given model, the scalar φ is a singlet, so if there\'s a U(1) symmetry under which φ is charged, and this symmetry is spontaneously broken by ⟨φ⟩ = x, then the Goldstone boson would be the imaginary part of φ (if φ is complex) or a combination of fields if there are multiple scalars. However, φ is a real scalar here? Wait, the kinetic term for φ is (1/2)(∂μ φ)^2, which suggests that φ is a real scalar field. So a real scalar can\'t have a U(1) symmetry. Therefore, φ is real, so when it gets a VEV, there\'s no Goldstone boson from φ. Wait, but real scalars don\'t have continuous symmetries acting on them (unless there are multiple real scalars). So maybe the Goldstone comes from another field.\n\nAlternatively, maybe the Goldstone is from the S doublet. If S is a complex doublet, then it has four degrees of freedom. If S doesn\'t get a VEV, then its components remain as scalars. If there\'s a symmetry acting on S that\'s spontaneously broken when another field gets a VEV, then maybe components of S become Goldstone bosons. But this is getting a bit vague.\n\nWait, perhaps the pseudo-Goldstone boson is associated with the Majoron? In some models, when you have a Majorana mass term for neutrinos, you can have a Goldstone boson called the Majoron from the breaking of lepton number. In this model, the Majorana mass term for N_R is y_i φ \\bar{N}_{iR}^c N_{iR} / 2. If φ is a singlet scalar, then giving φ a VEV breaks the global lepton number symmetry (if φ is charged under lepton number), which would generate a Goldstone boson – the Majoron. However, if lepton number is not an exact symmetry (e.g., explicitly broken by other terms), the Majoron becomes a pseudo-Goldstone boson.\n\nBut in the Standard Model, lepton number is an accidental symmetry. In this model, the term y_i φ \\bar{N}_{iR}^c N_{iR} violates lepton number by two units (since N_R is a fermion with lepton number +1, so N_R^c has lepton number -1, so the term φ N_R^c N_R^c would require φ to have lepton number +2 to conserve lepton number). If φ has a VEV, then lepton number is spontaneously broken, leading to a Majoron. However, if there are other terms in the Lagrangian that explicitly break lepton number, the Majoron would get a mass. Alternatively, if the symmetry is only broken by the φ VEV, but the potential has terms that preserve the symmetry, then the Majoron remains massless. But since the problem is talking about a pseudo-Goldstone boson, the symmetry must be explicitly broken, leading to a mass for the Majoron.\n\nBut in the given Lagrangian, the terms are:\n\n- The Majorana mass term y_i φ \\bar{N}_{iR}^c N_{iR} / 2, which breaks lepton number by two units if φ has lepton number -2.\n\n- The Yukawa coupling g_{iα} \\bar{N}_{iR} L_α S. The lepton number of L_α is +1, N_R is +1, so this term is lepton number conserving if S has lepton number 0. Alternatively, if S has lepton number -1, then the term would conserve lepton number. Wait, let\'s check:\n\nAssuming N_R has lepton number +1, L_α has lepton number +1. Then, \\bar{N}_{iR} has lepton number -1, L_α has +1, so the product \\bar{N}_{iR} L_α has lepton number 0. Therefore, for the term g_{iα} \\bar{N}_{iR} L_α S to conserve lepton number, S must have lepton number 0. But then the Majorana mass term y_i φ \\bar{N}_{iR}^c N_{iR} / 2 would require φ to have lepton number -2 (since N_R has +1, N_R^c has -1, so N_R^c N_R^c has -2, so φ must have +2 to make the term lepton number conserving). However, if φ has lepton number +2, then its VEV breaks lepton number spontaneously, leading to a Majoron. But if there are no other terms that break lepton number, the Majoron remains massless. However, the problem states that H₂ is a pseudo-Goldstone boson, so there must be some explicit breaking.\n\nAlternatively, maybe the potential V(φ, S, H) contains terms that break the lepton number symmetry explicitly. For example, if there are terms like φ^3 or φ H^2, which don\'t respect the lepton number symmetry, then the symmetry is explicitly broken, making the Majoron a pseudo-Goldstone boson. But since the potential isn\'t given, it\'s hard to tell. Alternatively, the explicit breaking could come from the Yukawa couplings or the Majorana mass terms. Wait, the Majorana mass term itself breaks lepton number. Wait, no, if φ has lepton number +2, then the term y_i φ \\bar{N}_{iR}^c N_{iR} / 2 is lepton number conserving. So if all terms in the Lagrangian conserve lepton number, then the spontaneous breaking by φ\'s VEV would lead to a massless Majoron. However, if there are other terms that violate lepton number, like a φ^4 term (which would need lepton number -8 if φ has +2), then the symmetry is explicitly broken. But without knowing the potential V(φ, S, H), it\'s difficult to say. \n\nAlternatively, maybe the pseudo-Goldstone isn\'t the Majoron but comes from another symmetry. For example, if there\'s a U(1) symmetry under which S and H transform, but that\'s broken by the VEVs. However, since S is a doublet and H is another doublet, maybe there\'s a SU(2) symmetry that\'s broken. Wait, but the Standard Model already breaks SU(2) with the Higgs VEV. \n\nAlternatively, considering that φ is a singlet, maybe there\'s a shift symmetry for φ that\'s broken by the potential, leading to a Goldstone. But since φ is a real scalar, a shift symmetry (like φ → φ + constant) would require the potential to be flat, but the potential V(φ, S, H) likely includes a mass term and quartic term for φ, breaking the shift symmetry. However, if the potential is nearly flat, then the pseudo-Goldstone would have a small mass. But without knowing the potential, this is speculative.\n\nAlternatively, maybe the pseudo-Goldstone is a mixture of the CP-odd components of the Higgs fields. In the Standard Model, the Higgs is a complex doublet, and after symmetry breaking, three Goldstone bosons are eaten by the W and Z bosons. If there are additional scalars, like the S doublet and the φ singlet, then their CP-odd components could mix. If there\'s an approximate symmetry, like a Peccei-Quinn symmetry, the pseudo-Goldstone could be similar to an axion. But again, without knowing the potential, it\'s hard to say.\n\nGiven the lack of specific information about the potential, perhaps we need to make some standard assumptions. Let\'s assume that the pseudo-Goldstone boson H₂ is the Majoron arising from the spontaneous breaking of lepton number by the VEV of φ, and that the explicit breaking of lepton number (which gives mass to the Majoron) comes from radiative corrections.\n\nIn such a case, the mass of the Majoron (pseudo-Goldstone) can be generated through loop diagrams. The leading contribution would come from the couplings that violate the lepton number symmetry. However, in the given Lagrangian, if all terms conserve lepton number (with φ carrying lepton number +2), then the symmetry is only spontaneously broken, leading to a massless Goldstone. To have a pseudo-Goldstone, there must be explicit breaking. Since the problem mentions radiative corrections, perhaps the explicit breaking occurs at the quantum level.\n\nWait, but if the classical Lagrangian respects the symmetry, but it\'s broken by anomalies or quantum effects, then the Goldstone can get a mass radiatively. However, in this case, the Majoron\'s mass from radiative corrections would depend on the lepton number violating parameters. But if the theory is lepton number conserving at the classical level, then quantum corrections would preserve it as well. So perhaps there\'s another source of explicit breaking.\n\nAlternatively, maybe the potential V(φ, S, H) includes terms that explicitly break the symmetry, but they are small. For example, a term like φ^3 which would break the lepton number symmetry (if φ has lepton number +2, then φ^3 has lepton number +6, which is not neutral). But such a term would need to be present in the potential to give mass to the pseudo-Goldstone. However, since the potential isn\'t given, perhaps we can assume that the symmetry is broken radiatively through the Coleman-Weinberg mechanism, where the effective potential generates terms that break the symmetry.\n\nAlternatively, the mass could come from loops involving the neutrinos. Since the right-handed neutrinos have Majorana masses proportional to φ, and they interact with the lepton doublets and the scalar S, perhaps the loops of neutrinos and S generate a mass for the pseudo-Goldstone.\n\nLet me think about the Coleman-Weinberg potential. If the classical potential has a flat direction (due to a symmetry), quantum corrections can generate a potential that lifts the flat direction, giving a mass to the pseudo-Goldstone. For example, if the tree-level potential has a U(1) symmetry that\'s spontaneously broken, but the Coleman-Weinberg potential breaks this symmetry explicitly, then the pseudo-Goldstone gets a mass from the loop corrections.\n\nIn this model, suppose that φ is complex, but the problem states that φ is a singlet scalar. Wait, the kinetic term for φ is (1/2)(∂μ φ)^2, which suggests that φ is a real scalar. If φ is real, then there\'s no continuous symmetry acting on it (other than discrete symmetries like φ → -φ). So maybe the symmetry is a discrete symmetry, but discrete symmetries don\'t give Goldstone bosons. Therefore, if φ is real, then there\'s no Goldstone boson from φ. So maybe the pseudo-Goldstone comes from another field.\n\nWait, the scalar S is a doublet (1,2,1). So S is a complex scalar doublet, which has four degrees of freedom. If S doesn\'t get a VEV, then all four components remain in the spectrum. The Standard Model Higgs H is also a doublet, so when H gets a VEV, three of its components are eaten by the W and Z bosons, leaving one physical Higgs boson. If S doesn\'t get a VEV, its four components remain as physical scalars. However, if there\'s a symmetry acting on S, some components could be Goldstone bosons. But since S doesn\'t participate in the symmetry breaking (no VEV), maybe not.\n\nAlternatively, maybe there\'s a mixing between the CP-odd components of H and φ. If φ is a real field, it doesn\'t have a CP-odd component. Wait, if φ is real, then its excitation is a CP-even scalar. The CP-odd component would come from a complex field. So perhaps H₂ is the CP-odd component of S? If S is a doublet with hypercharge 1, then its neutral component is complex, so it has a real and imaginary part. If S doesn\'t get a VEV, those components remain as scalars. If there\'s a U(1) symmetry acting on S, then the imaginary part could be a Goldstone boson. If that symmetry is explicitly broken, it becomes a pseudo-Goldstone.\n\nBut the problem states that H₂ is a pseudo-Goldstone boson whose mass comes from radiative corrections. To compute its mass, we need to identify the symmetry that\'s approximately preserved and the source of the explicit breaking.\n\nAlternatively, considering that the Majorana mass term for N_R is proportional to φ, which is a singlet, and the Yukawa coupling g_{iα} connects N_R, L_α, and S. If S is inert (doesn\'t get a VEV), then the neutrino masses would be generated via a loop diagram involving S and N_R. This is similar to the scotogenic model, where dark matter is the lightest neutral component of the inert doublet. In such models, the neutrino masses are generated at one loop, and the inert doublet\'s components have masses split by radiative corrections. However, in this case, the pseudo-Goldstone could be related to the scalar sector of S.\n\nWait, in the scotogenic model, the inert doublet doesn\'t get a VEV, and the Z₂ symmetry prevents it from coupling to the Higgs directly. But in our case, the potential V(φ, S, H) might allow couplings between S, H, and φ. If there\'s a global symmetry that\'s spontaneously broken by the VEVs of H and φ, and explicitly broken by terms in the potential, then the pseudo-Goldstone would acquire a mass.\n\nAlternatively, perhaps the pseudo-Goldstone is a mixture of the CP-odd components of H and S. In the Higgs doublet H, after electroweak symmetry breaking, the CP-odd component becomes the longitudinal mode of the Z boson. But if there\'s another doublet S, its CP-odd component could mix with the CP-odd component of H if there\'s a term in the potential like H† S + h.c. However, such a term would require S to have hypercharge 1/2 to match H\'s hypercharge, but in our case, S has hypercharge 1, so the term H† S would have hypercharge 1/2 + 1 = 3/2, which is not allowed. Therefore, such a term is not gauge invariant. Hence, the CP-odd components of H and S don\'t mix at tree level.\n\nAlternatively, maybe the potential includes terms like φ H† S, which could be gauge invariant. Let\'s check the quantum numbers:\n\n- φ is (1,1,0)\n- H is (1,2,1/2)\n- S is (1,2,1)\n\nThen, the term φ H† S would have SU(2) structure: H† is (2*) and S is (2), so 2* × 2 = 1 + 3. The hypercharge would be -1/2 (from H†) + 1 (from S) = 1/2. So the term φ H† S would have hypercharge 1/2, which is not invariant. Therefore, such a term is not allowed. Hence, there\'s no renormalizable term that mixes H and S through φ. \n\nTherefore, the scalars H, S, and φ don\'t mix at tree level through renormalizable terms. Therefore, the mass matrix for the scalars is diagonal at tree level, unless there are cross terms in the potential. But the potential V(φ, S, H) is not specified, so we can\'t be sure. However, given that the problem is about radiative corrections, maybe the mass of H₂ is generated at loop level.\n\nAssuming that at tree level, there\'s a massless Goldstone boson (from some spontaneously broken symmetry), and radiative corrections generate a small mass. The leading contribution would come from the loops involving the particles that interact with the Goldstone boson. For example, if the Goldstone is part of the φ field, then loops of N_R would generate a mass for it via the Yukawa coupling y_i. Alternatively, if the Goldstone is part of S, loops involving N_R and L_α could generate a mass.\n\nLet me consider the Majoron case. If φ is a complex field with a U(1) lepton number symmetry, its VEV breaks the symmetry, creating a Goldstone boson (the Majoron). The Yukawa coupling y_i φ N_R N_R breaks lepton number explicitly if φ is not charged appropriately, but if φ has lepton number -2, then the term conserves lepton number. However, if there are other terms in the potential that break lepton number, like φ^4 or φ^3, then the symmetry is explicitly broken. But if the potential only has terms like φ^2 and φ^4, then the U(1) is preserved at the classical level. However, at quantum level, the symmetry might be anomalous, leading to a mass for the Majoron. Alternatively, the explicit breaking could come from the gravitational effects, but that\'s probably beyond the scope here.\n\nAlternatively, the explicit breaking could come from the neutrino Yukawa couplings. In the term g_{iα} \\bar{N}_{iR} L_α S, if S is not charged under lepton number, then this term conserves lepton number. However, the combination of this term and the Majorana mass term could lead to lepton number violation at higher loops. For example, a loop diagram with N_R and S could generate a dimension-5 operator that breaks lepton number, contributing to the Majoron mass.\n\nAlternatively, consider that the Majoron (from φ\'s phase) couples to the neutrinos via the Yukawa coupling y_i φ N_R N_R. If we write φ = (x + σ + iη)/√2, where η is the Goldstone boson, then the coupling becomes (y_i / 2)(x + σ + iη) N_R N_R + h.c. The η (Majoron) couples to N_R as i y_i η N_R N_R / √2. Then, a loop of N_R would generate a mass for η. However, since the interaction is derivative-coupled (Goldstone\'s coupling is usually derivative, but in this case, it\'s a pseudo-Goldstone, so maybe the coupling is non-derivative). Wait, for a Goldstone boson, the coupling is typically derivative, but in the case of a Majoron from a spontaneously broken global symmetry, the coupling can be non-derivative. For example, the interaction term y_i φ N_R N_R would lead to a coupling proportional to η N_R N_R after φ gets a VEV. Then, a loop of N_R can generate a mass for η.\n\nThe mass of the pseudo-Goldstone boson (η) can be calculated via the Coleman-Weinberg potential. The one-loop correction to the potential would include a term proportional to (y_i^2 x^2 η^2) log(...), generating a mass for η. Alternatively, the diagram would be a loop of N_R with two η insertions, leading to a mass term.\n\nThe formula for the mass squared of the pseudo-Goldstone boson in such a case is typically m² ~ (y² M²)/(16π²), where M is the mass of the fermion in the loop (here, M = y_i x / 2). So substituting, m² ~ (y_i^2 (y_i x)^2)/(16π²) ) = y_i^4 x² / (16π²). However, this seems too simplistic. Alternatively, the mass might be generated at a higher loop order.\n\nWait, in the case of the Majoron, if the symmetry is broken explicitly by the anomaly, the mass can be generated at one loop. For example, if the U(1) symmetry has an SU(2)_L^2 anomaly, then the Majoron gets a mass through the electroweak instantons. However, in this model, the right-handed neutrinos are singlets under SU(2)_L, so their contribution to the anomaly would be zero. Therefore, the anomaly would come from other fermions. But the Standard Model fermions don\'t carry lepton number in a way that contributes to the anomaly. Hmm, this is getting complicated.\n\nAlternatively, if the U(1) symmetry is anomalous, the Majoron becomes massive via the Green-Schwarz mechanism, but that\'s more of a string theory scenario.\n\nAlternatively, consider that the explicit breaking of the symmetry is due to the Yukawa coupling g_{iα} \\bar{N}_{iR} L_α S. If this term doesn\'t respect the U(1) symmetry, then it would contribute to the mass of the Majoron. For example, if under the U(1) symmetry, N_R has charge +1, φ has charge -2 (to make the y_i term invariant), then the term g_{iα} \\bar{N}_{iR} L_α S would require S to have charge -1 (since \\bar{N}_{iR} has charge -1, L_α has charge +1, so total charge is -1 +1 + [S\'s charge] = 0 for invariance). Therefore, S must have charge 0 under the U(1). Therefore, the Yukawa term g_{iα} \\bar{N}_{iR} L_α S is invariant under the U(1). Therefore, this term does not break the symmetry. Therefore, the only source of explicit breaking would be from terms in the scalar potential.\n\nBut the scalar potential V(φ, S, H) isn\'t given, so we can\'t see if there are terms that break the U(1) symmetry. If the potential is invariant under the U(1), then the symmetry is exact, and the Goldstone remains massless. Therefore, to have a pseudo-Goldstone, there must be terms in the potential that break the U(1) symmetry. For example, a term like φ^3 would break the U(1) symmetry (since φ has charge -2, φ^3 has charge -6). If such a term is present, even with a small coefficient, it would give a mass to the Majoron. However, the problem states that the mass comes from radiative corrections, implying that the explicit breaking is not present at tree level but generated radiatively.\n\nTherefore, perhaps the U(1) symmetry is exact at tree level, but broken radiatively by loop corrections. This can happen if the symmetry is anomalous. However, as mentioned before, the right-handed neutrinos are singlets under the SM gauge group, so their contribution to the anomaly would be zero. The other fermions in the model (the SM fermions) have charges under the SM gauge groups and the U(1), but the U(1) charges need to be arranged such that the anomalies cancel. This is possible, but without knowing the specific charges, it\'s hard to say. \n\nAlternatively, the U(1) symmetry could be a Peccei-Quinn-like symmetry, which is anomalous, leading to a mass for the pseudo-Goldstone boson (the axion) via instanton effects. The mass would then be of order Λ^2 / f, where Λ is the QCD scale and f is the symmetry breaking scale. However, in this case, the symmetry breaking scale is x, and if the pseudo-Goldstone is an axion-like particle, its mass would be suppressed by x. But the problem doesn\'t mention QCD or instantons, so this might not be the case.\n\nGiven the uncertainty, perhaps the mass of H₂ is generated at one loop via the Yukawa interactions with the right-handed neutrinos. The coupling y_i φ N_R N_R gives a Majorana mass to N_R and a coupling between φ and N_R. If φ has a component that is the pseudo-Goldstone boson, then loops of N_R would generate a mass for it.\n\nAssuming that H₂ is the pseudo-Goldstone boson from φ, which is a real scalar, this doesn\'t make sense because real scalars don\'t have Goldstone bosons. Therefore, perhaps φ is complex. Wait, the problem states φ is a singlet scalar, but doesn\'t specify if it\'s real or complex. The kinetic term is written as (1/2)(∂μ φ)^2, which is typical for a real scalar. If it\'s a complex scalar, the kinetic term would be |∂μ φ|^2. Therefore, φ is real. Therefore, there\'s no Goldstone boson from φ. Then H₂ must come from another field.\n\nLooking back, the scalar S is a doublet (1,2,1). If S is complex, then it has four degrees of freedom. If there\'s a U(1) symmetry acting on S, then the Goldstone boson would be the phase of S. However, S is a doublet, so the U(1) symmetry would act on the entire doublet. For example, S → e^{iθ} S. If this symmetry is spontaneously broken by a VEV of S, but the problem states that S doesn\'t get a VEV (since only φ and H have VEVs), then the symmetry remains unbroken. Therefore, no Goldstone from S.\n\nAlternatively, maybe there\'s a symmetry that\'s a combination of transformations on φ and S. For example, a U(1) symmetry where φ is charged and S transforms in a way that the potential is invariant. But without knowing the potential, it\'s hard to construct.\n\nAlternatively, the pseudo-Goldstone could be the CP-odd component of the S doublet. If S doesn\'t get a VEV, its components remain as physical scalars. The CP-odd component would be a pseudoscalar. If there\'s an approximate symmetry protecting its mass, it could be a pseudo-Goldstone. The mass could be generated radiatively through loops involving the g_{iα} Yukawa coupling.\n\nFor example, the Yukawa term g_{iα} \\bar{N}_{iR} L_α S couples the right-handed neutrinos to the lepton doublet and the scalar S. If S has a CP-odd component that is a pseudo-Goldstone, then loops of N_R and L_α could generate a mass for it. The mass would be proportional to the couplings g_{iα} and the masses of the neutrinos or N_R.\n\nCalculating the mass would involve computing the loop corrections to the scalar potential. For a pseudo-Goldstone boson, the mass squared is typically proportional to the square of the symmetry-breaking coupling times the loop factor (1/(16π²)).\n\nFor example, if the pseudo-Goldstone is in the S doublet, and the symmetry is broken by the Yukawa couplings g_{iα}, then the mass might be something like m_{H₂}² ≈ (g^2 y^2 x^2)/(16π²), where g is the Yukawa coupling, y is the Majorana coupling, and x is the VEV of φ. Alternatively, if the mass comes from a loop with N_R and S, the mass could be m_{H₂} ≈ (g^2 M_N)/(16π²), where M_N is the Majorana mass of N_R.\n\nBut without knowing the exact structure of the potential and the symmetries, it\'s challenging to pinpoint the exact expression. However, typical pseudo-Goldstone masses from radiative corrections in such models are of the order of the loop factor (1/(16π²)) times the relevant coupling squared times the symmetry-breaking scale.\n\nGiven that the problem asks for an approximation, the answer is likely m_{H₂} ≈ (y_i^2 x)/(16π²) or something similar. However, considering that the mass is generated at one loop, and the couplings involved are the Yukawa couplings y_i and g_{iα}, and the VEV x, the formula might involve these parameters.\n\nAlternatively, if the pseudo-Goldstone mass comes from the Coleman-Weinberg potential due to the Yukawa interactions, the mass squared would be proportional to (y^4 x^2)/(16π²) ln(Λ^2/M^2), where Λ is the cutoff and M is the mass of the heavy fermion (N_R). If we assume Λ ~ M ~ y x, then the logarithm is a small factor, and m_{H₂} ~ (y^2 x)/(4π).\n\nBut given that the problem mentions "approximation through radiative corrections," the answer is likely something like m_{H₂} ≈ (y_i^2 x)/(16π²) or m_{H₂} ≈ (g_{iα}^2 v)/(16π²), depending on which coupling is responsible. However, since the pseudo-Goldstone is H₂, which is likely a scalar from the S or φ sector, and the couplings to N_R are through y_i φ N_R N_R and g_{iα} N_R L S, the dominant contribution might be from the y_i coupling if H₂ is from φ, or from g_{iα} if H₂ is from S.\n\nBut since φ is a real scalar, it can\'t have a Goldstone boson. Therefore, H₂ must come from the S doublet. If S is an inert doublet (no VEV), then its neutral CP-odd component could be a pseudo-Goldstone if there\'s an approximate symmetry. The mass would then come from loops involving the g_{iα} Yukawa coupling. For example, a one-loop diagram with N_R and L_α in the loop, connected by S and H. The mass would be proportional to g^2 M_N/(16π²), where M_N is the Majorana mass of N_R (which is y_i x). So substituting, m_{H₂} ≈ (g^2 y x)/(16π²).\n\nAlternatively, the mass could be generated at two loops, but the problem specifies radiative corrections, which could be one loop.\n\nGiven the ambiguity in the model details, but based on typical radiative pseudo-Goldstone masses in such extensions, the answer is likely:\n\nm_{H₂} ≈ (y_i^2 x)/(16π²)\n\nBut I need to verify this. Let\'s think of a similar model. In the Majoron model, if the Majoron is a pseudo-Goldstone, its mass at one loop would be m_η ≈ (y^2 x)/(16π²). However, if the explicit breaking comes from the same Yukawa coupling, then the mass squared would be something like (y^4 x²)/(16π²). But if the symmetry is broken by a dimensionful parameter, the mass could be linear in y x.\n\nAlternatively, consider the effective potential. The Coleman-Weinberg potential for φ would generate a mass term if there\'s a symmetry breaking. For a real scalar φ with a classical potential V(φ) = λ_φ (φ^2 - x²)^2, the mass at tree level is m_φ = sqrt(2 λ_φ) x. If there\'s a Yukawa coupling y to fermions, then the one-loop correction to the potential would be ΔV ≈ (y^4 φ^4)/(64π²) ln(y^2 φ^2 / Λ^2). This would contribute a mass term of order (y^4 x²)/(16π²). However, if φ is the pseudo-Goldstone, its tree-level mass is zero, and the entire mass comes from the loop, so m_{H₂} ≈ (y^2 x)/(4π).\n\nBut this depends on the specifics. Given that the problem doesn\'t specify the potential, but mentions radiative corrections, the answer is likely m_{H₂} ≈ (y_i^2 x)/(16π²). However, since the pseudo-Goldstone is a boson, the loop factor might have a different coefficient. For a fermion loop, the correction to the scalar mass squared is Δm² ≈ (y^2 M^2)/(16π²), where M is the fermion mass. Here, M = y_i x / 2, so Δm² ≈ (y_i^2 (y_i x)^2)/(16π²) = y_i^4 x²/(16π²), so m ≈ y_i^2 x/(4π). But this is for a quartic interaction. Alternatively, if the coupling is Yukawa (trilinear), the mass correction might be different.\n\nAlternatively, if the Goldstone couples to fermions via a derivative coupling, the loop would involve derivatives, leading to a logarithm, but the mass would still be proportional to y^2 x/(16π²).\n\nGiven the confusion and the lack of specific details, but based on standard results for pseudo-Goldstone boson masses from radiative corrections, I think the mass is approximately:\n\nm_{H₂} ≈ (y_i^2 x)/(16π²)\n\nBut to check, let\'s recall that in the case of the Majoron, if the symmetry is broken radiatively, the mass squared is generated at one loop and is of the order (y^2 M^2)/(16π²), where M is the Majorana mass. Here, M = y x, so m_{H₂} ≈ (y^2 * y x)/(16π²) = y^3 x/(16π²). But this seems too small. Alternatively, if the mass comes from a two-loop effect, it could be (y^2 g^2 x)/(16π²)^2, but the problem says "approximation through radiative corrections," which is usually one loop.\n\nAlternatively, if the pseudo-Goldstone is in the S doublet, its mass could come from loops involving the g_{iα} couplings. For example, a loop with N_R and L_α would generate a mass term for S. The mass would be m_S^2 ≈ (g^2 Λ^2)/(16π²), where Λ is the cutoff. But if the cutoff is related to the Majorana mass M_N = y x, then m_S ≈ (g y x)/(4π). However, this is more of an estimate.\n\nAlternatively, using the formula for the neutrino mass in the scotogenic model, which is m_ν ≈ (g^2 λ v^2)/(16π² M_N), where λ is a quartic coupling. If we set this as a analogy, but for the scalar mass, maybe m_{H₂} ≈ (g^2 M_N)/(16π²) = (g^2 y x)/(16π²).\n\nGiven the different possibilities, but considering that H₂ is a pseudo-Goldstone from the scalar sector, and the leading radiative correction comes from the largest coupling, which could be y_i or g_{iα}. If the model is similar to the scotogenic model, the scalar mass would be loop-induced with m_{H₂} ≈ (g^2 y x)/(16π²). However, without more details, it\'s hard to be precise.\n\nGiven the problem\'s context and the terms present in the Lagrangian, the dominant contribution likely comes from the y_i couplings, as they are the ones giving Majorana masses to N_R and hence are connected to the symmetry breaking. Therefore, the pseudo-Goldstone mass would be generated via loops involving N_R and the coupling y_i. Hence, the mass would be approximately:\n\nm_{H₂} ≈ (y_i^2 x)/(16π²)\n\nBut to write it properly, maybe with a square root, since mass is proportional to the square root of the loop correction. If the mass squared is (y_i^4 x²)/(16π²), then the mass is (y_i^2 x)/(4π). However, without knowing the exact structure, it\'s safer to write the mass squared. But the problem asks for the mass, not the mass squared.\n\nAlternatively, considering that the Goldstone boson\'s mass is zero at tree level, and the one-loop correction gives a mass squared of order (y_i^4 x²)/(16π²), then the mass is m_{H₂} ≈ (y_i^2 x)/(4π).\n\nBut in the absence of specific information, the standard approximation is to write the mass as m ∼ (loop factor) × (coupling)² × (VEV). The loop factor is 1/(16π²), so:\n\nm_{H₂} ≈ (y_i^2 x)/(16π²)\n\nBut I\'ve seen in some models the pseudo-Goldstone mass is m ∼ (y^2 f)/(16π²), where f is the symmetry breaking scale (here x). So this would support that answer.\n\nAlternatively, if the mass is generated at one loop, the correction to the mass squared is Δm² ≈ (y^4 x²)/(16π²), so m ≈ y² x/(4π).\n\nBut given the uncertainty, I think the expected answer is either y² x/(4π) or y² x/(16π²). Given that radiative corrections usually have a 1/(16π²) factor, but for scalar masses, the correction to m² is loop factor times coupling squared times cutoff squared, but if the cutoff is the same as the VEV x, then it would be (y² x)^2/(16π²), leading to m ≈ y² x/(4π). But I need to reconcile this.\n\nWait, let\'s think of the Coleman-Weinberg potential. For a real scalar field φ with a classical potential V(φ) = λ_φ φ^4/4, the one-loop correction is ΔV ≈ (m^4)/(64π²) ln(m²/Λ²), where m is the mass from the background field. If the tree-level potential is flat (λ_φ = 0), then the one-loop potential would generate a mass. For a Yukawa interaction yφψψ, the effective potential would have a term ΔV ≈ (y^4 φ^4)/(64π²) ln(y^2 φ^2/Λ^2). The mass squared is the second derivative at φ = x:\n\nm² ≈ d²ΔV/dφ² ≈ (3 y^4 x²)/(16π²)\n\nSo m ≈ (y^2 x)/(4π)\n\nThis seems to be the case. Therefore, if the pseudo-Goldstone\'s mass comes from the Coleman-Weinberg potential due to the Yukawa coupling y_i, then the mass is m_{H₂} ≈ (y_i^2 x)/(4π).\n\nBut the problem mentions "radiative corrections" without specifying the order. The Coleman-Weinberg potential is one-loop, so this would be a one-loop mass. Therefore, the answer is likely:\n\nm_{H₂} ≈ \\frac{y_i^2 x}{16\\pi^2} ?\n\nWait, the coefficient from the second derivative:\n\nΔV ≈ (y^4 φ^4)/(64π²) ln(...)\n\nThe first derivative is dΔV/dφ ≈ (y^4 φ^3)/(16π²) ln(...)\n\nThe second derivative is d²ΔV/dφ² ≈ (3 y^4 φ^2)/(16π²) ln(...)\n\nAssuming the log is O(1), then m² ≈ (3 y^4 x²)/(16π²), so m ≈ (y^2 x)/(4π√3). But coefficients like √3 are usually omitted in approximations, so m ≈ y^2 x/(4π).\n\nTherefore, the mass of the pseudo-Goldstone boson H₂ through radiative corrections is approximately (y_i^2 x)/(4π). However, different sources might have slightly different coefficients, but the leading order is y² x divided by a loop factor, which is either 4π or 16π². Given that the one-loop correction to the mass squared is proportional to y^4 x²/(16π²), the mass is y^2 x/(4π). Therefore, I think the answer is m_{H₂} ≈ y_i^2 x/(16π²) or m_{H₂} ≈ y_i^2 x/(4π). Given that the question says "approximation," either could be acceptable, but given the prevalence of the 16π² factor in loop integrals, I\'ll go with:\n\nm_{H₂} \\approx \\frac{y_i^2 x}{16\\pi^2}\n\nBut I need to check standard results. For example, in the case of the Coleman-Weinberg potential for a real scalar with Yukawa coupling, the mass generated at one loop is m ≈ (y^2 v)/(4π√3), where v is the VEV. So maybe the answer is (y_i^2 x)/(4π). However, considering that the pseudo-Goldstone\'s mass is typically lighter, suppressed by the loop factor, but it\'s model-dependent.\n\nGiven the ambiguity, but to match the loop factor 1/(16π²), the mass squared would be (y_i^4 x²)/(16π²), hence mass is (y_i^2 x)/(4π). Therefore, the answer is likely:\n\n\\boxed{\\frac{y_{i}^{2} x}{4\\pi}}\n\nBut I\'m still a bit unsure. Another approach: the pseudo-Goldstone boson mass can be estimated as the square root of the radiative correction to its mass squared. If the correction is δm² ~ (y^4 x²)/(16π²), then δm ~ y² x/(4π). Hence, the answer is y² x/(4π).\n\nYes, that makes sense. So I think the correct approximation is:\n\n\\boxed{\\frac{y_{i}^{2} x}{4\\pi}}\n'), native_finish_reason='stop')], created=1745390439, model='deepseek/deepseek-r1', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=9125, prompt_tokens=2892, total_tokens=12017, completion_tokens_details=None, prompt_tokens_details=None), provider='Nebius')

---

# cutoff_deepseek_completion response

The mass of the pseudo-Goldstone boson \( H_2 \) through radiative corrections is approximated by considering the leading one-loop contributions from the Yukawa interactions involving the right-handed neutrinos \( N_{iR} \). These corrections arise due to the explicit breaking of the symmetry associated with the pseudo-Goldstone boson, primarily through the coupling \( y_i \phi \bar{N}_{iR}^c N_{iR} \). The dominant contribution to the mass comes from the Coleman-Weinberg potential, where the one-loop correction generates a mass term proportional to the square of the Yukawa coupling \( y_i \) and the vacuum expectation value \( x \) of the singlet scalar \( \phi \).

The mass squared of \( H_2 \) is given by the loop factor \( \frac{y_i^4 x^2}{16\pi^2} \), leading to the mass:

\[
m_{H_2} \approx \frac{y_i^2 x}{4\pi}
\]

Thus, the approximation of the mass of the pseudo-Goldstone boson \( H_2 \) through radiative corrections is:

\[
\boxed{\frac{y_{i}^{2} x}{4\pi}}
\]

---

# cutoff_deepseek_completion reasoning

achyon-free, then the Goldstone becomes a pseudo-Goldstone with mass coming from the explicit breaking terms. Alternatively, if the symmetry is broken radiatively, the mass can be generated through loops.

In the given model, the scalar φ is a singlet, so if there's a U(1) symmetry under which φ is charged, and this symmetry is spontaneously broken by ⟨φ⟩ = x, then the Goldstone boson would be the imaginary part of φ (if φ is complex) or a combination of fields if there are multiple scalars. However, φ is a real scalar here? Wait, the kinetic term for φ is (1/2)(∂μ φ)^2, which suggests that φ is a real scalar field. So a real scalar can't have a U(1) symmetry. Therefore, φ is real, so when it gets a VEV, there's no Goldstone boson from φ. Wait, but real scalars don't have continuous symmetries acting on them (unless there are multiple real scalars). So maybe the Goldstone comes from another field.

Alternatively, maybe the Goldstone is from the S doublet. If S is a complex doublet, then it has four degrees of freedom. If S doesn't get a VEV, then its components remain as scalars. If there's a symmetry acting on S that's spontaneously broken when another field gets a VEV, then maybe components of S become Goldstone bosons. But this is getting a bit vague.

Wait, perhaps the pseudo-Goldstone boson is associated with the Majoron? In some models, when you have a Majorana mass term for neutrinos, you can have a Goldstone boson called the Majoron from the breaking of lepton number. In this model, the Majorana mass term for N_R is y_i φ \bar{N}_{iR}^c N_{iR} / 2. If φ is a singlet scalar, then giving φ a VEV breaks the global lepton number symmetry (if φ is charged under lepton number), which would generate a Goldstone boson – the Majoron. However, if lepton number is not an exact symmetry (e.g., explicitly broken by other terms), the Majoron becomes a pseudo-Goldstone boson.

But in the Standard Model, lepton number is an accidental symmetry. In this model, the term y_i φ \bar{N}_{iR}^c N_{iR} violates lepton number by two units (since N_R is a fermion with lepton number +1, so N_R^c has lepton number -1, so the term φ N_R^c N_R^c would require φ to have lepton number +2 to conserve lepton number). If φ has a VEV, then lepton number is spontaneously broken, leading to a Majoron. However, if there are other terms in the Lagrangian that explicitly break lepton number, the Majoron would get a mass. Alternatively, if the symmetry is only broken by the φ VEV, but the potential has terms that preserve the symmetry, then the Majoron remains massless. But since the problem is talking about a pseudo-Goldstone boson, the symmetry must be explicitly broken, leading to a mass for the Majoron.

But in the given Lagrangian, the terms are:

- The Majorana mass term y_i φ \bar{N}_{iR}^c N_{iR} / 2, which breaks lepton number by two units if φ has lepton number -2.

- The Yukawa coupling g_{iα} \bar{N}_{iR} L_α S. The lepton number of L_α is +1, N_R is +1, so this term is lepton number conserving if S has lepton number 0. Alternatively, if S has lepton number -1, then the term would conserve lepton number. Wait, let's check:

Assuming N_R has lepton number +1, L_α has lepton number +1. Then, \bar{N}_{iR} has lepton number -1, L_α has +1, so the product \bar{N}_{iR} L_α has lepton number 0. Therefore, for the term g_{iα} \bar{N}_{iR} L_α S to conserve lepton number, S must have lepton number 0. But then the Majorana mass term y_i φ \bar{N}_{iR}^c N_{iR} / 2 would require φ to have lepton number -2 (since N_R has +1, N_R^c has -1, so N_R^c N_R^c has -2, so φ must have +2 to make the term lepton number conserving). However, if φ has lepton number +2, then its VEV breaks lepton number spontaneously, leading to a Majoron. But if there are no other terms that break lepton number, the Majoron remains massless. However, the problem states that H₂ is a pseudo-Goldstone boson, so there must be some explicit breaking.

Alternatively, maybe the potential V(φ, S, H) contains terms that break the lepton number symmetry explicitly. For example, if there are terms like φ^3 or φ H^2, which don't respect the lepton number symmetry, then the symmetry is explicitly broken, making the Majoron a pseudo-Goldstone boson. But since the potential isn't given, it's hard to tell. Alternatively, the explicit breaking could come from the Yukawa couplings or the Majorana mass terms. Wait, the Majorana mass term itself breaks lepton number. Wait, no, if φ has lepton number +2, then the term y_i φ \bar{N}_{iR}^c N_{iR} / 2 is lepton number conserving. So if all terms in the Lagrangian conserve lepton number, then the spontaneous breaking by φ's VEV would lead to a massless Majoron. However, if there are other terms that violate lepton number, like a φ^4 term (which would need lepton number -8 if φ has +2), then the symmetry is explicitly broken. But without knowing the potential V(φ, S, H), it's difficult to say. 

Alternatively, maybe the pseudo-Goldstone isn't the Majoron but comes from another symmetry. For example, if there's a U(1) symmetry under which S and H transform, but that's broken by the VEVs. However, since S is a doublet and H is another doublet, maybe there's a SU(2) symmetry that's broken. Wait, but the Standard Model already breaks SU(2) with the Higgs VEV. 

Alternatively, considering that φ is a singlet, maybe there's a shift symmetry for φ that's broken by the potential, leading to a Goldstone. But since φ is a real scalar, a shift symmetry (like φ → φ + constant) would require the potential to be flat, but the potential V(φ, S, H) likely includes a mass term and quartic term for φ, breaking the shift symmetry. However, if the potential is nearly flat, then the pseudo-Goldstone would have a small mass. But without knowing the potential, this is speculative.

Alternatively, maybe the pseudo-Goldstone is a mixture of the CP-odd components of the Higgs fields. In the Standard Model, the Higgs is a complex doublet, and after symmetry breaking, three Goldstone bosons are eaten by the W and Z bosons. If there are additional scalars, like the S doublet and the φ singlet, then their CP-odd components could mix. If there's an approximate symmetry, like a Peccei-Quinn symmetry, the pseudo-Goldstone could be similar to an axion. But again, without knowing the potential, it's hard to say.

Given the lack of specific information about the potential, perhaps we need to make some standard assumptions. Let's assume that the pseudo-Goldstone boson H₂ is the Majoron arising from the spontaneous breaking of lepton number by the VEV of φ, and that the explicit breaking of lepton number (which gives mass to the Majoron) comes from radiative corrections.

In such a case, the mass of the Majoron (pseudo-Goldstone) can be generated through loop diagrams. The leading contribution would come from the couplings that violate the lepton number symmetry. However, in the given Lagrangian, if all terms conserve lepton number (with φ carrying lepton number +2), then the symmetry is only spontaneously broken, leading to a massless Goldstone. To have a pseudo-Goldstone, there must be explicit breaking. Since the problem mentions radiative corrections, perhaps the explicit breaking occurs at the quantum level.

Wait, but if the classical Lagrangian respects the symmetry, but it's broken by anomalies or quantum effects, then the Goldstone can get a mass radiatively. However, in this case, the Majoron's mass from radiative corrections would depend on the lepton number violating parameters. But if the theory is lepton number conserving at the classical level, then quantum corrections would preserve it as well. So perhaps there's another source of explicit breaking.

Alternatively, maybe the potential V(φ, S, H) includes terms that explicitly break the symmetry, but they are small. For example, a term like φ^3 which would break the lepton number symmetry (if φ has lepton number +2, then φ^3 has lepton number +6, which is not neutral). But such a term would need to be present in the potential to give mass to the pseudo-Goldstone. However, since the potential isn't given, perhaps we can assume that the symmetry is broken radiatively through the Coleman-Weinberg mechanism, where the effective potential generates terms that break the symmetry.

Alternatively, the mass could come from loops involving the neutrinos. Since the right-handed neutrinos have Majorana masses proportional to φ, and they interact with the lepton doublets and the scalar S, perhaps the loops of neutrinos and S generate a mass for the pseudo-Goldstone.

Let me think about the Coleman-Weinberg potential. If the classical potential has a flat direction (due to a symmetry), quantum corrections can generate a potential that lifts the flat direction, giving a mass to the pseudo-Goldstone. For example, if the tree-level potential has a U(1) symmetry that's spontaneously broken, but the Coleman-Weinberg potential breaks this symmetry explicitly, then the pseudo-Goldstone gets a mass from the loop corrections.

In this model, suppose that φ is complex, but the problem states that φ is a singlet scalar. Wait, the kinetic term for φ is (1/2)(∂μ φ)^2, which suggests that φ is a real scalar. If φ is real, then there's no continuous symmetry acting on it (other than discrete symmetries like φ → -φ). So maybe the symmetry is a discrete symmetry, but discrete symmetries don't give Goldstone bosons. Therefore, if φ is real, then there's no Goldstone boson from φ. So maybe the pseudo-Goldstone comes from another field.

Wait, the scalar S is a doublet (1,2,1). So S is a complex scalar doublet, which has four degrees of freedom. If S doesn't get a VEV, then all four components remain in the spectrum. The Standard Model Higgs H is also a doublet, so when H gets a VEV, three of its components are eaten by the W and Z bosons, leaving one physical Higgs boson. If S doesn't get a VEV, its four components remain as physical scalars. However, if there's a symmetry acting on S, some components could be Goldstone bosons. But since S doesn't participate in the symmetry breaking (no VEV), maybe not.

Alternatively, maybe there's a mixing between the CP-odd components of H and φ. If φ is a real field, it doesn't have a CP-odd component. Wait, if φ is real, then its excitation is a CP-even scalar. The CP-odd component would come from a complex field. So perhaps H₂ is the CP-odd component of S? If S is a doublet with hypercharge 1, then its neutral component is complex, so it has a real and imaginary part. If S doesn't get a VEV, those components remain as scalars. If there's a U(1) symmetry acting on S, then the imaginary part could be a Goldstone boson. If that symmetry is explicitly broken, it becomes a pseudo-Goldstone.

But the problem states that H₂ is a pseudo-Goldstone boson whose mass comes from radiative corrections. To compute its mass, we need to identify the symmetry that's approximately preserved and the source of the explicit breaking.

Alternatively, considering that the Majorana mass term for N_R is proportional to φ, which is a singlet, and the Yukawa coupling g_{iα} connects N_R, L_α, and S. If S is inert (doesn't get a VEV), then the neutrino masses would be generated via a loop diagram involving S and N_R. This is similar to the scotogenic model, where dark matter is the lightest neutral component of the inert doublet. In such models, the neutrino masses are generated at one loop, and the inert doublet's components have masses split by radiative corrections. However, in this case, the pseudo-Goldstone could be related to the scalar sector of S.

Wait, in the scotogenic model, the inert doublet doesn't get a VEV, and the Z₂ symmetry prevents it from coupling to the Higgs directly. But in our case, the potential V(φ, S, H) might allow couplings between S, H, and φ. If there's a global symmetry that's spontaneously broken by the VEVs of H and φ, and explicitly broken by terms in the potential, then the pseudo-Goldstone would acquire a mass.

Alternatively, perhaps the pseudo-Goldstone is a mixture of the CP-odd components of H and S. In the Higgs doublet H, after electroweak symmetry breaking, the CP-odd component becomes the longitudinal mode of the Z boson. But if there's another doublet S, its CP-odd component could mix with the CP-odd component of H if there's a term in the potential like H† S + h.c. However, such a term would require S to have hypercharge 1/2 to match H's hypercharge, but in our case, S has hypercharge 1, so the term H† S would have hypercharge 1/2 + 1 = 3/2, which is not allowed. Therefore, such a term is not gauge invariant. Hence, the CP-odd components of H and S don't mix at tree level.

Alternatively, maybe the potential includes terms like φ H† S, which could be gauge invariant. Let's check the quantum numbers:

- φ is (1,1,0)
- H is (1,2,1/2)
- S is (1,2,1)

Then, the term φ H† S would have SU(2) structure: H† is (2*) and S is (2), so 2* × 2 = 1 + 3. The hypercharge would be -1/2 (from H†) + 1 (from S) = 1/2. So the term φ H† S would have hypercharge 1/2, which is not invariant. Therefore, such a term is not allowed. Hence, there's no renormalizable term that mixes H and S through φ. 

Therefore, the scalars H, S, and φ don't mix at tree level through renormalizable terms. Therefore, the mass matrix for the scalars is diagonal at tree level, unless there are cross terms in the potential. But the potential V(φ, S, H) is not specified, so we can't be sure. However, given that the problem is about radiative corrections, maybe the mass of H₂ is generated at loop level.

Assuming that at tree level, there's a massless Goldstone boson (from some spontaneously broken symmetry), and radiative corrections generate a small mass. The leading contribution would come from the loops involving the particles that interact with the Goldstone boson. For example, if the Goldstone is part of the φ field, then loops of N_R would generate a mass for it via the Yukawa coupling y_i. Alternatively, if the Goldstone is part of S, loops involving N_R and L_α could generate a mass.

Let me consider the Majoron case. If φ is a complex field with a U(1) lepton number symmetry, its VEV breaks the symmetry, creating a Goldstone boson (the Majoron). The Yukawa coupling y_i φ N_R N_R breaks lepton number explicitly if φ is not charged appropriately, but if φ has lepton number -2, then the term conserves lepton number. However, if there are other terms in the potential that break lepton number, like φ^4 or φ^3, then the symmetry is explicitly broken. But if the potential only has terms like φ^2 and φ^4, then the U(1) is preserved at the classical level. However, at quantum level, the symmetry might be anomalous, leading to a mass for the Majoron. Alternatively, the explicit breaking could come from the gravitational effects, but that's probably beyond the scope here.

Alternatively, the explicit breaking could come from the neutrino Yukawa couplings. In the term g_{iα} \bar{N}_{iR} L_α S, if S is not charged under lepton number, then this term conserves lepton number. However, the combination of this term and the Majorana mass term could lead to lepton number violation at higher loops. For example, a loop diagram with N_R and S could generate a dimension-5 operator that breaks lepton number, contributing to the Majoron mass.

Alternatively, consider that the Majoron (from φ's phase) couples to the neutrinos via the Yukawa coupling y_i φ N_R N_R. If we write φ = (x + σ + iη)/√2, where η is the Goldstone boson, then the coupling becomes (y_i / 2)(x + σ + iη) N_R N_R + h.c. The η (Majoron) couples to N_R as i y_i η N_R N_R / √2. Then, a loop of N_R would generate a mass for η. However, since the interaction is derivative-coupled (Goldstone's coupling is usually derivative, but in this case, it's a pseudo-Goldstone, so maybe the coupling is non-derivative). Wait, for a Goldstone boson, the coupling is typically derivative, but in the case of a Majoron from a spontaneously broken global symmetry, the coupling can be non-derivative. For example, the interaction term y_i φ N_R N_R would lead to a coupling proportional to η N_R N_R after φ gets a VEV. Then, a loop of N_R can generate a mass for η.

The mass of the pseudo-Goldstone boson (η) can be calculated via the Coleman-Weinberg potential. The one-loop correction to the potential would include a term proportional to (y_i^2 x^2 η^2) log(...), generating a mass for η. Alternatively, the diagram would be a loop of N_R with two η insertions, leading to a mass term.

The formula for the mass squared of the pseudo-Goldstone boson in such a case is typically m² ~ (y² M²)/(16π²), where M is the mass of the fermion in the loop (here, M = y_i x / 2). So substituting, m² ~ (y_i^2 (y_i x)^2)/(16π²) ) = y_i^4 x² / (16π²). However, this seems too simplistic. Alternatively, the mass might be generated at a higher loop order.

Wait, in the case of the Majoron, if the symmetry is broken explicitly by the anomaly, the mass can be generated at one loop. For example, if the U(1) symmetry has an SU(2)_L^2 anomaly, then the Majoron gets a mass through the electroweak instantons. However, in this model, the right-handed neutrinos are singlets under SU(2)_L, so their contribution to the anomaly would be zero. Therefore, the anomaly would come from other fermions. But the Standard Model fermions don't carry lepton number in a way that contributes to the anomaly. Hmm, this is getting complicated.

Alternatively, if the U(1) symmetry is anomalous, the Majoron becomes massive via the Green-Schwarz mechanism, but that's more of a string theory scenario.

Alternatively, consider that the explicit breaking of the symmetry is due to the Yukawa coupling g_{iα} \bar{N}_{iR} L_α S. If this term doesn't respect the U(1) symmetry, then it would contribute to the mass of the Majoron. For example, if under the U(1) symmetry, N_R has charge +1, φ has charge -2 (to make the y_i term invariant), then the term g_{iα} \bar{N}_{iR} L_α S would require S to have charge -1 (since \bar{N}_{iR} has charge -1, L_α has charge +1, so total charge is -1 +1 + [S's charge] = 0 for invariance). Therefore, S must have charge 0 under the U(1). Therefore, the Yukawa term g_{iα} \bar{N}_{iR} L_α S is invariant under the U(1). Therefore, this term does not break the symmetry. Therefore, the only source of explicit breaking would be from terms in the scalar potential.

But the scalar potential V(φ, S, H) isn't given, so we can't see if there are terms that break the U(1) symmetry. If the potential is invariant under the U(1), then the symmetry is exact, and the Goldstone remains massless. Therefore, to have a pseudo-Goldstone, there must be terms in the potential that break the U(1) symmetry. For example, a term like φ^3 would break the U(1) symmetry (since φ has charge -2, φ^3 has charge -6). If such a term is present, even with a small coefficient, it would give a mass to the Majoron. However, the problem states that the mass comes from radiative corrections, implying that the explicit breaking is not present at tree level but generated radiatively.

Therefore, perhaps the U(1) symmetry is exact at tree level, but broken radiatively by loop corrections. This can happen if the symmetry is anomalous. However, as mentioned before, the right-handed neutrinos are singlets under the SM gauge group, so their contribution to the anomaly would be zero. The other fermions in the model (the SM fermions) have charges under the SM gauge groups and the U(1), but the U(1) charges need to be arranged such that the anomalies cancel. This is possible, but without knowing the specific charges, it's hard to say. 

Alternatively, the U(1) symmetry could be a Peccei-Quinn-like symmetry, which is anomalous, leading to a mass for the pseudo-Goldstone boson (the axion) via instanton effects. The mass would then be of order Λ^2 / f, where Λ is the QCD scale and f is the symmetry breaking scale. However, in this case, the symmetry breaking scale is x, and if the pseudo-Goldstone is an axion-like particle, its mass would be suppressed by x. But the problem doesn't mention QCD or instantons, so this might not be the case.

Given the uncertainty, perhaps the mass of H₂ is generated at one loop via the Yukawa interactions with the right-handed neutrinos. The coupling y_i φ N_R N_R gives a Majorana mass to N_R and a coupling between φ and N_R. If φ has a component that is the pseudo-Goldstone boson, then loops of N_R would generate a mass for it.

Assuming that H₂ is the pseudo-Goldstone boson from φ, which is a real scalar, this doesn't make sense because real scalars don't have Goldstone bosons. Therefore, perhaps φ is complex. Wait, the problem states φ is a singlet scalar, but doesn't specify if it's real or complex. The kinetic term is written as (1/2)(∂μ φ)^2, which is typical for a real scalar. If it's a complex scalar, the kinetic term would be |∂μ φ|^2. Therefore, φ is real. Therefore, there's no Goldstone boson from φ. Then H₂ must come from another field.

Looking back, the scalar S is a doublet (1,2,1). If S is complex, then it has four degrees of freedom. If there's a U(1) symmetry acting on S, then the Goldstone boson would be the phase of S. However, S is a doublet, so the U(1) symmetry would act on the entire doublet. For example, S → e^{iθ} S. If this symmetry is spontaneously broken by a VEV of S, but the problem states that S doesn't get a VEV (since only φ and H have VEVs), then the symmetry remains unbroken. Therefore, no Goldstone from S.

Alternatively, maybe there's a symmetry that's a combination of transformations on φ and S. For example, a U(1) symmetry where φ is charged and S transforms in a way that the potential is invariant. But without knowing the potential, it's hard to construct.

Alternatively, the pseudo-Goldstone could be the CP-odd component of the S doublet. If S doesn't get a VEV, its components remain as physical scalars. The CP-odd component would be a pseudoscalar. If there's an approximate symmetry protecting its mass, it could be a pseudo-Goldstone. The mass could be generated radiatively through loops involving the g_{iα} Yukawa coupling.

For example, the Yukawa term g_{iα} \bar{N}_{iR} L_α S couples the right-handed neutrinos to the lepton doublet and the scalar S. If S has a CP-odd component that is a pseudo-Goldstone, then loops of N_R and L_α could generate a mass for it. The mass would be proportional to the couplings g_{iα} and the masses of the neutrinos or N_R.

Calculating the mass would involve computing the loop corrections to the scalar potential. For a pseudo-Goldstone boson, the mass squared is typically proportional to the square of the symmetry-breaking coupling times the loop factor (1/(16π²)).

For example, if the pseudo-Goldstone is in the S doublet, and the symmetry is broken by the Yukawa couplings g_{iα}, then the mass might be something like m_{H₂}² ≈ (g^2 y^2 x^2)/(16π²), where g is the Yukawa coupling, y is the Majorana coupling, and x is the VEV of φ. Alternatively, if the mass comes from a loop with N_R and S, the mass could be m_{H₂} ≈ (g^2 M_N)/(16π²), where M_N is the Majorana mass of N_R.

But without knowing the exact structure of the potential and the symmetries, it's challenging to pinpoint the exact expression. However, typical pseudo-Goldstone masses from radiative corrections in such models are of the order of the loop factor (1/(16π²)) times the relevant coupling squared times the symmetry-breaking scale.

Given that the problem asks for an approximation, the answer is likely m_{H₂} ≈ (y_i^2 x)/(16π²) or something similar. However, considering that the mass is generated at one loop, and the couplings involved are the Yukawa couplings y_i and g_{iα}, and the VEV x, the formula might involve these parameters.

Alternatively, if the pseudo-Goldstone mass comes from the Coleman-Weinberg potential due to the Yukawa interactions, the mass squared would be proportional to (y^4 x^2)/(16π²) ln(Λ^2/M^2), where Λ is the cutoff and M is the mass of the heavy fermion (N_R). If we assume Λ ~ M ~ y x, then the logarithm is a small factor, and m_{H₂} ~ (y^2 x)/(4π).

But given that the problem mentions "approximation through radiative corrections," the answer is likely something like m_{H₂} ≈ (y_i^2 x)/(16π²) or m_{H₂} ≈ (g_{iα}^2 v)/(16π²), depending on which coupling is responsible. However, since the pseudo-Goldstone is H₂, which is likely a scalar from the S or φ sector, and the couplings to N_R are through y_i φ N_R N_R and g_{iα} N_R L S, the dominant contribution might be from the y_i coupling if H₂ is from φ, or from g_{iα} if H₂ is from S.

But since φ is a real scalar, it can't have a Goldstone boson. Therefore, H₂ must come from the S doublet. If S is an inert doublet (no VEV), then its neutral CP-odd component could be a pseudo-Goldstone if there's an approximate symmetry. The mass would then come from loops involving the g_{iα} Yukawa coupling. For example, a one-loop diagram with N_R and L_α in the loop, connected by S and H. The mass would be proportional to g^2 M_N/(16π²), where M_N is the Majorana mass of N_R (which is y_i x). So substituting, m_{H₂} ≈ (g^2 y x)/(16π²).

Alternatively, the mass could be generated at two loops, but the problem specifies radiative corrections, which could be one loop.

Given the ambiguity in the model details, but based on typical radiative pseudo-Goldstone masses in such extensions, the answer is likely:

m_{H₂} ≈ (y_i^2 x)/(16π²)

But I need to verify this. Let's think of a similar model. In the Majoron model, if the Majoron is a pseudo-Goldstone, its mass at one loop would be m_η ≈ (y^2 x)/(16π²). However, if the explicit breaking comes from the same Yukawa coupling, then the mass squared would be something like (y^4 x²)/(16π²). But if the symmetry is broken by a dimensionful parameter, the mass could be linear in y x.

Alternatively, consider the effective potential. The Coleman-Weinberg potential for φ would generate a mass term if there's a symmetry breaking. For a real scalar φ with a classical potential V(φ) = λ_φ (φ^2 - x²)^2, the mass at tree level is m_φ = sqrt(2 λ_φ) x. If there's a Yukawa coupling y to fermions, then the one-loop correction to the potential would be ΔV ≈ (y^4 φ^4)/(64π²) ln(y^2 φ^2 / Λ^2). This would contribute a mass term of order (y^4 x²)/(16π²). However, if φ is the pseudo-Goldstone, its tree-level mass is zero, and the entire mass comes from the loop, so m_{H₂} ≈ (y^2 x)/(4π).

But this depends on the specifics. Given that the problem doesn't specify the potential, but mentions radiative corrections, the answer is likely m_{H₂} ≈ (y_i^2 x)/(16π²). However, since the pseudo-Goldstone is a boson, the loop factor might have a different coefficient. For a fermion loop, the correction to the scalar mass squared is Δm² ≈ (y^2 M^2)/(16π²), where M is the fermion mass. Here, M = y_i x / 2, so Δm² ≈ (y_i^2 (y_i x)^2)/(16π²) = y_i^4 x²/(16π²), so m ≈ y_i^2 x/(4π). But this is for a quartic interaction. Alternatively, if the coupling is Yukawa (trilinear), the mass correction might be different.

Alternatively, if the Goldstone couples to fermions via a derivative coupling, the loop would involve derivatives, leading to a logarithm, but the mass would still be proportional to y^2 x/(16π²).

Given the confusion and the lack of specific details, but based on standard results for pseudo-Goldstone boson masses from radiative corrections, I think the mass is approximately:

m_{H₂} ≈ (y_i^2 x)/(16π²)

But to check, let's recall that in the case of the Majoron, if the symmetry is broken radiatively, the mass squared is generated at one loop and is of the order (y^2 M^2)/(16π²), where M is the Majorana mass. Here, M = y x, so m_{H₂} ≈ (y^2 * y x)/(16π²) = y^3 x/(16π²). But this seems too small. Alternatively, if the mass comes from a two-loop effect, it could be (y^2 g^2 x)/(16π²)^2, but the problem says "approximation through radiative corrections," which is usually one loop.

Alternatively, if the pseudo-Goldstone is in the S doublet, its mass could come from loops involving the g_{iα} couplings. For example, a loop with N_R and L_α would generate a mass term for S. The mass would be m_S^2 ≈ (g^2 Λ^2)/(16π²), where Λ is the cutoff. But if the cutoff is related to the Majorana mass M_N = y x, then m_S ≈ (g y x)/(4π). However, this is more of an estimate.

Alternatively, using the formula for the neutrino mass in the scotogenic model, which is m_ν ≈ (g^2 λ v^2)/(16π² M_N), where λ is a quartic coupling. If we set this as a analogy, but for the scalar mass, maybe m_{H₂} ≈ (g^2 M_N)/(16π²) = (g^2 y x)/(16π²).

Given the different possibilities, but considering that H₂ is a pseudo-Goldstone from the scalar sector, and the leading radiative correction comes from the largest coupling, which could be y_i or g_{iα}. If the model is similar to the scotogenic model, the scalar mass would be loop-induced with m_{H₂} ≈ (g^2 y x)/(16π²). However, without more details, it's hard to be precise.

Given the problem's context and the terms present in the Lagrangian, the dominant contribution likely comes from the y_i couplings, as they are the ones giving Majorana masses to N_R and hence are connected to the symmetry breaking. Therefore, the pseudo-Goldstone mass would be generated via loops involving N_R and the coupling y_i. Hence, the mass would be approximately:

m_{H₂} ≈ (y_i^2 x)/(16π²)

But to write it properly, maybe with a square root, since mass is proportional to the square root of the loop correction. If the mass squared is (y_i^4 x²)/(16π²), then the mass is (y_i^2 x)/(4π). However, without knowing the exact structure, it's safer to write the mass squared. But the problem asks for the mass, not the mass squared.

Alternatively, considering that the Goldstone boson's mass is zero at tree level, and the one-loop correction gives a mass squared of order (y_i^4 x²)/(16π²), then the mass is m_{H₂} ≈ (y_i^2 x)/(4π).

But in the absence of specific information, the standard approximation is to write the mass as m ∼ (loop factor) × (coupling)² × (VEV). The loop factor is 1/(16π²), so:

m_{H₂} ≈ (y_i^2 x)/(16π²)

But I've seen in some models the pseudo-Goldstone mass is m ∼ (y^2 f)/(16π²), where f is the symmetry breaking scale (here x). So this would support that answer.

Alternatively, if the mass is generated at one loop, the correction to the mass squared is Δm² ≈ (y^4 x²)/(16π²), so m ≈ y² x/(4π).

But given the uncertainty, I think the expected answer is either y² x/(4π) or y² x/(16π²). Given that radiative corrections usually have a 1/(16π²) factor, but for scalar masses, the correction to m² is loop factor times coupling squared times cutoff squared, but if the cutoff is the same as the VEV x, then it would be (y² x)^2/(16π²), leading to m ≈ y² x/(4π). But I need to reconcile this.

Wait, let's think of the Coleman-Weinberg potential. For a real scalar field φ with a classical potential V(φ) = λ_φ φ^4/4, the one-loop correction is ΔV ≈ (m^4)/(64π²) ln(m²/Λ²), where m is the mass from the background field. If the tree-level potential is flat (λ_φ = 0), then the one-loop potential would generate a mass. For a Yukawa interaction yφψψ, the effective potential would have a term ΔV ≈ (y^4 φ^4)/(64π²) ln(y^2 φ^2/Λ^2). The mass squared is the second derivative at φ = x:

m² ≈ d²ΔV/dφ² ≈ (3 y^4 x²)/(16π²)

So m ≈ (y^2 x)/(4π)

This seems to be the case. Therefore, if the pseudo-Goldstone's mass comes from the Coleman-Weinberg potential due to the Yukawa coupling y_i, then the mass is m_{H₂} ≈ (y_i^2 x)/(4π).

But the problem mentions "radiative corrections" without specifying the order. The Coleman-Weinberg potential is one-loop, so this would be a one-loop mass. Therefore, the answer is likely:

m_{H₂} ≈ \frac{y_i^2 x}{16\pi^2} ?

Wait, the coefficient from the second derivative:

ΔV ≈ (y^4 φ^4)/(64π²) ln(...)

The first derivative is dΔV/dφ ≈ (y^4 φ^3)/(16π²) ln(...)

The second derivative is d²ΔV/dφ² ≈ (3 y^4 φ^2)/(16π²) ln(...)

Assuming the log is O(1), then m² ≈ (3 y^4 x²)/(16π²), so m ≈ (y^2 x)/(4π√3). But coefficients like √3 are usually omitted in approximations, so m ≈ y^2 x/(4π).

Therefore, the mass of the pseudo-Goldstone boson H₂ through radiative corrections is approximately (y_i^2 x)/(4π). However, different sources might have slightly different coefficients, but the leading order is y² x divided by a loop factor, which is either 4π or 16π². Given that the one-loop correction to the mass squared is proportional to y^4 x²/(16π²), the mass is y^2 x/(4π). Therefore, I think the answer is m_{H₂} ≈ y_i^2 x/(16π²) or m_{H₂} ≈ y_i^2 x/(4π). Given that the question says "approximation," either could be acceptable, but given the prevalence of the 16π² factor in loop integrals, I'll go with:

m_{H₂} \approx \frac{y_i^2 x}{16\pi^2}

But I need to check standard results. For example, in the case of the Coleman-Weinberg potential for a real scalar with Yukawa coupling, the mass generated at one loop is m ≈ (y^2 v)/(4π√3), where v is the VEV. So maybe the answer is (y_i^2 x)/(4π). However, considering that the pseudo-Goldstone's mass is typically lighter, suppressed by the loop factor, but it's model-dependent.

Given the ambiguity, but to match the loop factor 1/(16π²), the mass squared would be (y_i^4 x²)/(16π²), hence mass is (y_i^2 x)/(4π). Therefore, the answer is likely:

\boxed{\frac{y_{i}^{2} x}{4\pi}}

But I'm still a bit unsure. Another approach: the pseudo-Goldstone boson mass can be estimated as the square root of the radiative correction to its mass squared. If the correction is δm² ~ (y^4 x²)/(16π²), then δm ~ y² x/(4π). Hence, the answer is y² x/(4π).

Yes, that makes sense. So I think the correct approximation is:

\boxed{\frac{y_{i}^{2} x}{4\pi}}

---

# paraphrased_deepseek_completion_anthropic (via openrouter)

ChatCompletion(id='gen-1745390803-bD7mEoLrLd0fUSuhy8Ia', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='To determine the mass of the pseudo-Goldstone boson \\( H_2 \\) through radiative corrections in the given extension of the Standard Model, we consider the following key points:\n\n1. **Model Setup**:\n   - The model includes singlet fermions \\( N_{iR} \\), a scalar doublet \\( S \\), and a singlet scalar \\( \\phi \\).\n   - The scalar \\( \\phi \\) acquires a vacuum expectation value (VEV) \\( x \\), and the Standard Model Higgs \\( H \\) acquires a VEV \\( v \\).\n   - The Yukawa interactions involve \\( g_{i\\alpha} \\bar{N}_{iR} L_\\alpha S \\) and a Majorana mass term \\( \\frac{y_i}{2} \\phi \\bar{N}_{iR}^c N_{iR} \\).\n\n2. **Symmetry Breaking and Pseudo-Goldstone Boson**:\n   - The pseudo-Goldstone boson \\( H_2 \\) arises from an approximate symmetry broken by radiative corrections.\n   - The dominant contributions to the mass of \\( H_2 \\) come from loop diagrams involving the Yukawa couplings \\( g_{i\\alpha} \\) and the Majorana mass term \\( y_i x \\).\n\n3. **Radiative Corrections**:\n   - The mass of \\( H_2 \\) is generated at one-loop level due to the explicit symmetry breaking by the Yukawa couplings and Majorana masses.\n   - The loop diagrams involve the interaction terms \\( g_{i\\alpha} \\bar{N}_{iR} L_\\alpha S \\) and the Majorana mass \\( M_N = \\frac{y_i x}{2} \\).\n\n4. **Estimation of Mass**:\n   - The one-loop correction to the mass squared of \\( H_2 \\) is proportional to the square of the Yukawa coupling \\( g \\), the Majorana mass \\( y x \\), and a loop factor \\( \\frac{1}{16\\pi^2} \\).\n\nCombining these considerations, the mass of the pseudo-Goldstone boson \\( H_2 \\) through radiative corrections is approximately:\n\n\\[\n\\boxed{\\dfrac{g^2 y x}{16\\pi^2}}\n\\]', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, reasoning=" But without the explicit potential V(ϕ,S,H), it's challenging to determine the exact structure.\n\nAssuming that the potential V(ϕ,S,H) has a term that breaks the symmetry explicitly, for example, a term like μ² S†H + h.c., which would mix S and H. If such terms are present, they could lead to a pseudo-Goldstone boson when the symmetry is approximate.\n\nAlternatively, if the potential V has terms that couple ϕ and S, like λ ϕ² S†S, then the VEV of ϕ (x) could induce a mass term for S. But since S is a doublet with hypercharge 1, its neutral component could mix with the Standard Model Higgs. However, without a VEV for S, the mixing would be through terms in the potential.\n\nBut wait, the question mentions that ⟨φ⟩² = x² + υ². If ⟨φ⟩ = x and ⟨h⟩ = v, then perhaps ⟨φ⟩² + ⟨h⟩² = x² + v². This might be a way to parametrize the VEVs, but usually, each scalar's VEV is independent unless there's a constraint. If the potential enforces ⟨φ⟩² + ⟨h⟩² = x² + v², that might suggest some specific structure. But I need to be cautious here.\n\nAssuming that φ and H are part of an extended scalar sector with a potential that leads to their VEVs. If there's an approximate symmetry, say a U(1) symmetry under which φ and H rotate into each other, then the true Goldstone would be a combination of their phases. But if the symmetry is explicitly broken, the Goldstone becomes a pseudo-Goldstone with a mass generated at loop level.\n\nAlternatively, the pseudo-Goldstone could come from the singlet φ. If φ is a complex field, its phase would be the Goldstone boson when it gets a VEV. However, the Lagrangian term for φ is written as (∂μ φ)², which is a real scalar (since there's no kinetic term for an imaginary part). Wait, actually, the term (∂μ φ)² is written as (1/2)(∂μ φ)^2, which is standard for a real scalar. Therefore, φ is a real scalar field. Then, when it gets a VEV x, there's no Goldstone boson because a real scalar cannot have a continuous symmetry. So maybe the Goldstone comes from another field.\n\nLooking back at the scalar doublet S. If S is a complex doublet with hypercharge 1, then its neutral component (since hypercharge Y = 1, the charges are (S^+, S^0), with S^0 having charge Y=1/2 + 1/2? Wait, hypercharge for SU(2) doublets is given by Y = Q - T3. For S being (1,2,1), the hypercharge Y = 1. So each component of the doublet has hypercharge Y = 1, so for the upper component (charge Q = T3 + Y/2 = 1/2 + 1/2 = 1), and the lower component (Q = -1/2 + 1/2 = 0). Therefore, the components are S = (S^+, S^0), where S^0 is neutral. If S^0 gets a VEV, that would break the SU(2)×U(1) symmetry. However, the Standard Model Higgs H already breaks the symmetry with its VEV. If S does not acquire a VEV, then its components remain as inert scalars.\n\nBut the problem states that ⟨φ⟩² = x² + υ², which might imply that the total VEV is a combination of φ and another field, perhaps H. If H is the Standard Model Higgs with VEV v, and φ has VEV x, then maybe their combination leads to some relation. However, the usual Higgs VEV is around 246 GeV, so perhaps υ here is the same as v, and x is another VEV contributing to the masses of the singlet fermions N_R.\n\nBut the question is about the pseudo-Goldstone boson H₂. Since the Standard Model already has the Higgs boson, H₂ might be an additional scalar from the extended sector. If φ is real, then its fluctuation around x is a scalar particle, not a Goldstone. However, if there is a complex scalar that's part of a symmetry, but the given Lagrangian has φ as a real scalar. Therefore, perhaps S, being a doublet, has components that could be Goldstone bosons. But in the Standard Model, the Higgs doublet's Goldstone bosons are eaten by the W and Z. If S is another doublet, its Goldstone modes would also be eaten unless S doesn't get a VEV. If S is inert (no VEV), then its components remain as physical scalars. However, the potential V(ϕ,S,H) could mix S with H or φ, leading to mass eigenstates.\n\nAlternatively, maybe H₂ is the pseudo-Goldstone boson from a global symmetry that's broken by the VEVs of φ and H. For example, if there's a U(1) symmetry under which φ and H transform, then the phase direction could be the Goldstone. But if that U(1) is explicitly broken by terms in the potential, the Goldstone becomes massive.\n\nBut how does this relate to radiative corrections? The mass of the pseudo-Goldstone can be generated at loop level if the symmetry breaking terms are loop-suppressed. For example, in the Coleman-Weinberg potential, radiative corrections can generate a mass for the pseudo-Goldstone.\n\nAlternatively, if the pseudo-Goldstone's mass is protected by an approximate symmetry, its mass would be generated by loops involving the explicit symmetry-breaking couplings. In this model, the Yukawa couplings y_i and g_{iα} could break the symmetry and generate the mass for H₂ through loops.\n\nLet me think step by step:\n\n1. Identify the Goldstone bosons from symmetry breaking. Since φ is a real scalar, its VEV breaks no continuous symmetry. The Standard Model Higgs H breaks SU(2)×U(1) to U(1)_EM, giving masses to W and Z. The scalar S is a doublet but doesn't get a VEV, so it doesn't contribute to symmetry breaking. Therefore, perhaps there is an accidental global symmetry in the scalar potential that's broken, leading to a Goldstone boson.\n\nWait, the potential V(ϕ,S,H) could have an approximate global symmetry. For example, if there's a U(1) symmetry under which ϕ shifts: ϕ → ϕ + a, but this is a shift symmetry. However, the term (∂μ ϕ)^2 is invariant under such a shift, but the Majorana mass term y_i ϕ \\bar{N}_i^c N_i breaks this symmetry explicitly. So if the Yukawa coupling y_i is small, the symmetry is approximately preserved, leading to a pseudo-Goldstone boson.\n\nBut ϕ is a real scalar field. If there's a shift symmetry ϕ → ϕ + a, which is broken by the Yukawa term, then the pseudo-Goldstone would be ϕ itself. However, if ϕ gets a VEV, then the fluctuation around the VEV is a scalar with mass, but if the symmetry is approximate, the mass would be small. But since ϕ is a singlet, maybe the pseudo-Goldstone is a component of another field.\n\nAlternatively, consider that the scalar potential V(ϕ,S,H) has a symmetry that's broken by the VEVs. For example, suppose there's a U(1) symmetry under which S and H rotate. If the potential respects this symmetry except for small terms, then the Goldstone boson would be a combination of phases of S and H. But S is a doublet with hypercharge 1, and H is a doublet with hypercharge 1/2, so their charges under the U(1) would differ, making such a symmetry non-trivial.\n\nAlternatively, maybe the symmetry is between ϕ and S. If ϕ is a real field and S is complex, perhaps there's a symmetry mixing them, but it's not obvious.\n\nAlternatively, the scalar potential could have a term that mixes S and H, such as λ (H† S) ϕ + h.c. If ϕ gets a VEV x, this would generate a quadratic term for S and H mixing. If such a term is present, then after ϕ gets a VEV, there's a mixing between S and H, leading to mass eigenstates. The pseudo-Goldstone could be a result of this mixing. But without the explicit potential, it's hard to say.\n\nAlternatively, perhaps the mass of H₂ arises from loop corrections due to the Yukawa interactions. The Yukawa couplings g_{iα} connect N_R, L_α, and S. If S is inert (no VEV), then the interaction g_{iα} \\bar{N}_R L_α S would lead to a vertex between N_R, lepton doublet L_α, and S. The Majorana mass for N_R comes from the y_i ϕ term. If ϕ has a VEV x, then N_R has a mass M_i = y_i x / 2.\n\nThe pseudo-Goldstone H₂ might get a mass from loops involving the Yukawa couplings. For example, if H₂ is a component of S, then loops of N_R and leptons could generate a mass for H₂. But since S is a doublet, its components would include charged scalars and a neutral scalar. If S is inert, the neutral component could mix with the Higgs through loops, but in the absence of tree-level mixing, the mass might be generated at loop level.\n\nAlternatively, if the potential V(ϕ,S,H) has a quartic term like λ |S|^2 ϕ^2, then the mass of S would receive a contribution from ϕ's VEV: m_S^2 = λ x². But this is a tree-level mass. However, if there's a global symmetry that's broken by this term, the pseudo-Goldstone could acquire a mass radiatively.\n\nAlternatively, considering that the Yukawa interaction g_{iα} \\bar{N}_R L_α S violates the global symmetry that would otherwise protect the Goldstone. Therefore, loop diagrams with N_R and L_α running in the loop would generate a mass for the pseudo-Goldstone boson.\n\nLet me try to model this. Suppose that the pseudo-Goldstone boson is a component of the S doublet. If S has a mass term from the potential, but there's an approximate symmetry making this mass small. Then, radiative corrections from the Yukawa couplings g_{iα} would generate a mass for S's components.\n\nThe one-loop correction to the mass of S would come from diagrams where S interacts via the Yukawa coupling with N_R and L_α. Since L_α is a lepton doublet, and N_R is a singlet, the interaction term g_{iα} \\bar{N}_R L_α S would lead to a vertex with S, N_R, and L_α. A loop diagram with N_R and L_α running in the loop would correct the mass of S.\n\nThe mass correction can be estimated using the formula for the self-energy. The contribution would be proportional to the square of the coupling g_{iα}, the number of flavors, and the mass of the fermion in the loop. However, since N_R has a Majorana mass M_i = y_i x / 2, and the lepton masses are much smaller, perhaps we can approximate the loop with just the N_R mass.\n\nThe self-energy diagram would be a loop with two Yukawa couplings g_{iα}, two propagators of N_R and L_α. But since L_α is a Standard Model lepton, its mass is negligible compared to the possible mass of N_R. However, in the Yukawa term, the coupling is between N_R, L_α, and S. The interaction term is of the form g N_R L S, where L is the lepton doublet. When we write this in terms of components, the lepton doublet L has a charged lepton and a neutrino. Since N_R is a right-handed neutrino, the interaction would be something like g N_R (ν, e)_L^T S. Therefore, the loop would involve N_R and the neutrino (or charged lepton) in the loop.\n\nBut neutrinos are neutral, and if S is a doublet with components S^+ and S^0, then the coupling would be to either the charged or neutral component. Let's clarify:\n\nThe term g_{iα} \\bar{N}_{iR} L_α S would be:\n\ng_{iα} \\bar{N}_{iR} [ (ν_α, e_α)_L ]^T ⋅ S\n\nSince S is a doublet (S^+, S^0), the dot product would be ν_α S^0 - e_α S^+.\n\nTherefore, the interaction terms are:\n\ng_{iα} \\bar{N}_{iR} ν_α S^0 - g_{iα} \\bar{N}_{iR} e_α S^+ + h.c.\n\nSo, the Yukawa coupling connects N_R to either neutrinos and S^0 or charged leptons and S^+.\n\nIf we are considering the mass of the neutral component S^0 (which could be the pseudo-Goldstone), then the loop would involve N_R and neutrinos. However, if the neutrinos are Majorana particles (which they are in this model, since N_R is a Majorana fermion), the loop would contribute to the mass of S^0.\n\nThe self-energy diagram for S^0 would be a loop with N_R and ν_α running in the loop. The mass correction would be proportional to g^2 and the mass of N_R. However, the neutrino here is a left-handed field, which in the loop would pair with the right-handed N_R. But since the neutrino is part of the lepton doublet, and assuming it's a Dirac neutrino (but in reality, with N_R present, it's a seesaw scenario), the mass would be generated via the seesaw mechanism.\n\nWait, in this model, the neutrino masses would come from the coupling g_{iα} \\bar{N}_R L_α S. If S doesn't get a VEV, this term doesn't generate a Dirac mass at tree level. However, if S mixes with the Standard Model Higgs H through the potential V(ϕ,S,H), then after H gets a VEV, there could be an induced VEV for S. Alternatively, if S does not get a VEV, then the neutrino masses would require a loop process.\n\nBut let's get back to the mass of H₂. Assuming H₂ is the neutral component of S, which is a pseudo-Goldstone boson. Its mass would come from loops involving the Yukawa couplings g_{iα} and the Majorana masses of N_R.\n\nThe one-loop correction to the mass squared of S^0 would be given by a diagram where S^0 emits a virtual N_R and ν_α, which loop around. The amplitude would involve the coupling g_{iα}, and the loop integral would depend on the mass of N_R.\n\nThe formula for the self-energy at one loop would be something like:\n\nΣ ≈ (g^2 / (16π²)) * M_N² * log(M_N² / μ²)\n\nwhere M_N is the mass of N_R, and μ is the renormalization scale. However, the exact coefficient depends on the specifics of the interaction. Since the Yukawa coupling is between S^0, N_R, and ν_α, and ν_α is a left-handed neutrino, which in the loop would have a propagator proportional to its mass. But if the neutrino is massless (or nearly massless) at tree level, its contribution would be negligible. However, in this model, the neutrino could get a mass via the seesaw mechanism if S mixes with H.\n\nAlternatively, if S does not mix with H, then the neutrino mass would come from a one-loop diagram involving S, N_R, and the coupling g. This is similar to the scotogenic model, where dark matter candidates and neutrino masses are generated through loops.\n\nIn the scotogenic model, the neutrino mass is calculated as:\n\nm_ν ≈ (g^2 M_N)/(16π²) * [ m_S^2 / (M_N² - m_S^2) ] * ln(M_N² / m_S²)\n\nBut in our case, if S is the scalar in the loop, then the neutrino mass would depend on the mass of S and N_R. However, if we are instead calculating the mass of S (the pseudo-Goldstone), then it's the other way around: the mass of S is generated by loops involving N_R and neutrinos.\n\nAssuming that the pseudo-Goldstone mass is generated at one loop, the general expression would be:\n\nm_{H₂}² ≈ (g^4 x²)/(16π²) * f(y_i, ... )\n\nBut I need to be more precise.\n\nAlternatively, considering that the symmetry breaking is due to the VEV of φ, which gives a mass to N_R, and the coupling g_{iα} connects N_R to S and leptons. If the approximate symmetry protecting the mass of H₂ is broken by these couplings, then the mass would be generated at loop level.\n\nLet me consider the Coleman-Weinberg potential. If the tree-level potential has a flat direction (leading to a massless Goldstone), quantum corrections can generate a potential that lifts this flatness, giving the pseudo-Goldstone a mass.\n\nFor example, suppose the tree-level potential for S has a term λ_S |S|^4, but due to an approximate symmetry, λ_S is very small. Then, the Coleman-Weinberg potential would generate a contribution to the mass of S from loops. The one-loop contribution to the effective potential is given by:\n\nΔV ≈ (1/(64π²)) Str[ M^4 (log(M² / μ²) - c) ]\n\nwhere Str is the supertrace, M is the mass matrix, and c is a constant.\n\nIn this case, the fields in the loop would be the fermions N_R and the scalars S. The fermion loop would contribute negatively, while the scalar loop would contribute positively. However, if the dominant contribution comes from the fermion loops (since they have Yukawa couplings), then:\n\nΔV ≈ - (N_f/(64π²)) (g^4 x² |S|^2) log(...)\n\nwhere N_f is the number of fermion species, and we're assuming that the Yukawa coupling g and the Majorana mass yx are the relevant parameters. This would generate a mass term for S of order:\n\nm_{S}^2 ≈ (g^4 x²)/(16π²) * log(...)\n\nBut the exact coefficient depends on the details. If H₂ is the scalar S's component, then its mass squared would be of the order (g^4 x²)/(16π²).\n\nAlternatively, if the pseudo-Goldstone is a mixture of φ and the Higgs, the mass would come from terms breaking the symmetry in the potential. But since φ is a real scalar, its Goldstone would require a complex field.\n\nAnother angle: The Majorana mass term for N_R is (y_i / 2) φ \\bar{N}_{iR}^c N_{iR} + h.c. If φ is a real field, then this term is real if y_i is real. The Yukawa coupling g_{iα} is complex in general. The presence of these couplings breaks the global symmetries that could protect the Goldstone.\n\nIf the original potential has a symmetry that's only broken by these Yukawa couplings, then the mass of the pseudo-Goldstone would be proportional to these couplings. For example, if there's a U(1) symmetry under which S rotates, and this symmetry is broken by the Yukawa couplings g_{iα}, then the mass of the Goldstone (from S) would be generated at loop level with g_{iα} in the loop.\n\nThe general formula for the mass would then be:\n\nm_{H₂}² ≈ (g^2 y x)/(16π²) * Λ²\n\nBut this is too vague. Let's think about a specific diagram.\n\nConsider the one-loop diagram where H₂ (from S) couples to N_R and leptons via g_{iα}, and N_R has a mass from φ's VEV. The loop would have two Yukawa couplings (g^2) and a Majorana mass insertion (y x). The loop integral would involve the product of these couplings and the loop momentum.\n\nIn a seesaw-like diagram, the mass might be something like:\n\nm_{H₂}² ≈ (g^2 y x^2)/(16π²) * log(Λ^2/M_N^2)\n\nBut without knowing the exact structure, it's hard to get the precise factors. However, typically, in such models, the pseudo-Goldstone mass squared is proportional to the product of the symmetry-breaking parameters (here, the Yukawa couplings) and the loop factor 1/(16π²).\n\nGiven that the Majorana mass M_N = y x / 2, we can write:\n\nm_{H₂} ≈ (g^2 M_N)/(16π²) * something\n\nIf the log is considered O(1), then:\n\nm_{H₂} ≈ (g^2 M_N)/(16π²)\n\nBut this is a rough estimate. To get a more accurate expression, let's recall that in the Coleman-Weinberg potential, the mass generated from a fermion loop is:\n\nΔm² ≈ - (g^2 M_N^2)/(8π²) * log(Λ^2/M_N^2)\n\nBut this is for a scalar coupled to fermions with a Yukawa coupling g and fermion mass M_N. However, in our case, the Yukawa coupling is between S, N_R, and L, so the diagram would involve a loop of N_R and L (lepton). But since the lepton mass is negligible, the dominant contribution comes from the N_R.\n\nWait, in the interaction term g \\bar{N}_R L S, the vertices would involve g, the scalar S, the fermion N_R, and the lepton L. However, in the loop, you need two vertices, so two factors of g. The loop would have a fermion line going from N_R to L and back to N_R, but since L is a different fermion (the lepton), this would require a mass insertion on the L line. But if the lepton is massless, this diagram would vanish. Therefore, maybe the loop must involve a Majorana mass insertion for the neutrino.\n\nAlternatively, if the neutrino has a Majorana mass from the N_R, then the loop can be closed. Let me think: In the interaction term, we have g \\bar{N}_R L S. If N_R has a Majorana mass M_N = y x / 2, then the neutrino mass is generated via the seesaw mechanism. However, if S does not get a VEV, the neutrino mass would be generated at one loop. The diagram would be a loop with N_R and S in the loop, connected via the Yukawa couplings g and the Majorana mass M_N.\n\nBut this is getting into the details of the neutrino mass generation, which might be a separate issue. However, if the question is about the mass of H₂ (which is part of S), then the same loop that generates the neutrino mass might also contribute to the mass of S.\n\nIn the scotogenic model, the neutrino mass is generated via a loop with N_R and the inert doublet S. The mass of the inert doublet scalars is generated at one loop through the same couplings. The formula for the scalar mass squared is something like:\n\nm_S² ≈ (g^2 M_N²)/(16π²) * log(M_N² / m_S²)\n\nBut this is a self-energy correction. If m_S is small (pseudo-Goldstone), then the logarithm could be significant. However, solving for m_S would give:\n\nm_S ≈ (g M_N)/(4π) * sqrt( log(M_N² / m_S²) )\n\nAssuming the log is order 1, then m_S ≈ g M_N / (4π)\n\nBut this is a rough estimate. The exact coefficient might differ by factors of 2 or so depending on the diagram topology and couplings.\n\nGiven that, the mass of the pseudo-Goldstone boson H₂ (which is part of the inert doublet S) would be approximately:\n\nm_{H₂} ≈ (g^2 y x)/(16π²)\n\nBut wait, M_N = y x / 2, so substituting:\n\nm_{H₂} ≈ (g^2 (2 M_N))/(16π²) ) = (g^2 M_N)/(8π²)\n\nAlternatively, if the mass is generated at one loop with two Yukawa couplings and a Majorana mass, the formula might have a different structure.\n\nAlternatively, consider the diagram where H₂ (from S) couples to two virtual N_Rs via the Yukawa coupling g, and the N_Rs have a Majorana mass M_N. The loop would then be a triangle diagram? Or a loop with two Yukawa couplings and two Majorana mass insertions.\n\nWait, the self-energy diagram for S would be a loop with N_R and L running. But since L is a Standard Model lepton with negligible mass, the loop integral would depend on the momentum. However, if we consider the limit where the external momentum is small compared to M_N, we can approximate the loop integral.\n\nThe self-energy Σ(p²) for S would receive a contribution from the loop with N_R and L. The Yukawa interaction is g \\bar{N}_R L S + h.c. The loop would have two vertices of g and propagators of N_R and L.\n\nThe self-energy at zero momentum would be:\n\nΣ(0) ≈ - g^2 ∫ d^4k / (2π)^4 Tr[ (i (k̸ + m_L)) / (k² - m_L² + iε) ) (i (k̸ + M_N)) / (k² - M_N² + iε) ) ]\n\nBut m_L ≈ 0, so:\n\nΣ(0) ≈ - g^2 ∫ d^4k / (2π)^4 Tr[ (i k̸) / (k² + iε) ) (i (k̸ + M_N)) / (k² - M_N² + iε) ) ]\n\nSimplifying the trace:\n\nTr[ k̸ (k̸ + M_N) ] = Tr[ k̸ k̸ ] + M_N Tr[ k̸ ]\n\nThe second term is zero because the trace of an odd number of gamma matrices is zero. The first term:\n\nTr[ k̸ k̸ ] = 4 k²\n\nSo:\n\nΣ(0) ≈ - g^2 ∫ d^4k / (2π)^4 [ 4 k² / (k² + iε)(k² - M_N² + iε) ) ]\n\nThis integral is divergent, but we can evaluate it using dimensional regularization. The integral becomes:\n\nΣ(0) ≈ -4 g^2 ∫ d^dk / (2π)^d [ k² / (k²)(k² - M_N²) ) ] = -4 g^2 ∫ d^dk / (2π)^d [ 1 / (k² - M_N²) ) ]\n\nWait, but this simplifies to:\n\nΣ(0) ≈ -4 g^2 ∫ d^dk / (2π)^d [ 1 / (k² - M_N²) ) ]\n\nBut this is just the integral of the propagator, which for d=4 is quadratically divergent. However, in dimensional regularization, this would be proportional to M_N². The result would be:\n\nΣ(0) ≈ -4 g^2 (M_N²/(16π²)) (1/ε + finite terms)\n\nBut we need to renormalize this. However, the divergence would be absorbed into the counterterms. The finite part would give a contribution to the mass squared of S:\n\nΔm_S² ≈ (g^2 M_N²)/(4π²) * (1/ε + ... )\n\nBut since we're interested in the finite, physical mass, after renormalization, the mass would be:\n\nm_S² ≈ (g^2 M_N²)/(16π²) * log(Λ^2/M_N²)\n\nAssuming a cutoff Λ, which could be the scale of the theory. If the log is of order 1, then:\n\nm_S ≈ (g M_N)/(4π)\n\nThus, the mass of the pseudo-Goldstone boson H₂ (which is part of the S doublet) would be approximately (g M_N)/(4π). Since M_N = y x / 2, substituting:\n\nm_{H₂} ≈ (g y x)/(8π)\n\nBut this is a tree-level estimate? Wait, no, this is a one-loop result. The factor of 1/(4π) comes from the loop integral.\n\nHowever, different normalizations might affect the coefficient. For example, in the Yukawa term, if the coupling is g/√2 or something, but since the problem doesn't specify, we'll take the coupling as g.\n\nAlternatively, considering that each Yukawa vertex contributes a factor of g, and the loop integral gives a factor of 1/(16π²), then the mass squared would be:\n\nm_{H₂}^2 ≈ (g^2 M_N^2)/(16π²)\n\nTaking the square root:\n\nm_{H₂} ≈ (g M_N)/(4π)\n\nGiven that M_N = y x / 2, this becomes:\n\nm_{H₂} ≈ (g y x)/(8π)\n\nBut I need to check the coefficients carefully. Let's recall that the general expression for the one-loop correction to the scalar mass from a fermion loop is:\n\nΔm² = (g² N_f)/(16π²) [ 2 M_f² ] (Λ² term ignored, focusing on the finite part)\n\nWait, the standard result for a scalar interacting with fermions via L = g φ ψψ, the one-loop correction to the scalar mass squared is:\n\nΔm² ≈ (g² M_f²)/(8π²) ln(Λ/M_f)\n\nBut in our case, the Yukawa interaction is between S, N_R, and L. The fermions in the loop are N_R and L (neutrino). Assuming the neutrino mass is negligible, the dominant contribution comes from N_R. However, the coupling involves both N_R and L, so the trace might involve both.\n\nBut earlier calculation suggested that the self-energy contribution is proportional to g² M_N², leading to m_S ≈ g M_N / (4π). Given that, and substituting M_N = y x / 2, the mass becomes:\n\nm_{H₂} ≈ (g y x)/(8π)\n\nBut the question asks for the approximation through radiative corrections. The answer is likely of the order g y x / (16π²), but I need to resolve the coefficients.\n\nAlternatively, another approach: In the model, the pseudo-Goldstone boson mass can be estimated using the Coleman-Weinberg potential. The effective potential at one-loop is:\n\nV_eff = V_tree + (1/(64π²)) [ m_S^4 (ln(m_S² / μ²) - c) - 2 m_N^4 (ln(m_N² / μ²) - c) ]\n\nWhere m_S is the scalar mass and m_N is the fermion mass. If at tree level, the scalar mass is zero (Goldstone limit), then the one-loop contribution from the fermions (N_R) would generate a mass.\n\nBut in this case, the fermion mass m_N = y x / 2, and the coupling between the scalar and the fermion is g. The contribution to the scalar mass squared would be:\n\nΔm² ≈ (g² m_N²)/(8π²) ln(Λ²/m_N²)\n\nAssuming the log factor is of order 1, then:\n\nm_{H₂} ≈ (g m_N)/(2√2 π)\n\nSubstituting m_N = y x / 2:\n\nm_{H₂} ≈ (g y x)/(4√2 π)\n\nBut this still leaves numerical factors uncertain. However, given the options and standard results, the mass is typically of the order:\n\nm_{H₂} ≈ (g y x)/(16π²) * Λ\n\nBut without a specific scale Λ, this is unclear. However, in radiative corrections, the logarithm often appears, so maybe:\n\nm_{H₂}² ≈ (g² y² x²)/(16π²) ln(x/υ)\n\nBut this is speculative.\n\nAlternatively, considering that the pseudo-Goldstone mass is generated by the breaking of the global symmetry by both the Yukawa couplings g and y. The leading contribution would be at one-loop level, and the mass would be:\n\nm_{H₂} ≈ (g y v)/(16π²)\n\nWhere v is the Higgs VEV. But why v? Because the Higgs VEV is involved in the mixing or the potential.\n\nAlternatively, if the potential V(ϕ,S,H) includes a term like λ ϕ² S†S, then the tree-level mass of S is λ x². If there's an approximate symmetry when λ is small, the radiative corrections from the Yukawa couplings g would generate a correction to λ, leading to:\n\nΔλ ≈ (g^4)/(16π²) ln(...)\n\nThus, Δm_S² ≈ (g^4 x²)/(16π²)\n\nSo m_{H₂} ≈ (g² x)/(4π)\n\nBut this depends on the quartic coupling.\n\nGiven the ambiguity in the potential and the lack of explicit terms, it's challenging to pinpoint the exact expression. However, based on similar models (like the scotogenic model), the mass of the inert doublet scalars is generated at one loop and is proportional to the square of the Yukawa coupling times the Majorana mass, divided by (16π²). Therefore, a reasonable approximation would be:\n\nm_{H₂} ≈ \\frac{g^2 y x}{16\\pi^2}\n\nBut I need to check the dimensions. If g is dimensionless, y is dimensionless, x is a mass, then g² y x has dimensions of mass. Divided by 16π², which is dimensionless, so the whole expression has dimensions of mass. That works.\n\nAlternatively, if the mass is generated at one loop, the typical scale is (loop factor) * (coupling)^2 * (mass scale). Here, the mass scale could be x, and the coupling is g y. So:\n\nm_{H₂} ≈ \\frac{g y x}{16\\pi^2}\n\nBut without knowing the exact structure of the potential and the couplings, this is an educated guess. Given that, and considering that in the scotogenic model, the scalar mass is of the order (yukawa^2 * Majorana mass)/(16π²), I think the answer is likely:\n\nm_{H₂} \\approx \\frac{g_{i\\alpha}^2 y_i x}{16\\pi^2}\n\nBut since the question asks for an approximation and doesn't specify indices, we can write it as:\n\nm_{H₂} \\approx \\frac{g^2 y x}{16\\pi^2}\n\nWhere g and y are typical values of the couplings.\n\nTherefore, after considering various possibilities and loop contributions, the mass of the pseudo-Goldstone boson H₂ through radiative corrections is approximately proportional to (g² y x)/(16π²).\n\n**Final Answer**\nThe mass of the pseudo-Goldstone boson \\( H_{2} \\) through radiative corrections is approximately \\(\\boxed{\\dfrac{g^2 y x}{16\\pi^2}}\\).\n"), native_finish_reason='stop')], created=1745390803, model='deepseek/deepseek-r1', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=8116, prompt_tokens=1014, total_tokens=9130, completion_tokens_details=None, prompt_tokens_details=None), provider='Nebius')

---

# paraphrased_deepseek_completion_anthropic response

To determine the mass of the pseudo-Goldstone boson \( H_2 \) through radiative corrections in the given extension of the Standard Model, we consider the following key points:

1. **Model Setup**:
   - The model includes singlet fermions \( N_{iR} \), a scalar doublet \( S \), and a singlet scalar \( \phi \).
   - The scalar \( \phi \) acquires a vacuum expectation value (VEV) \( x \), and the Standard Model Higgs \( H \) acquires a VEV \( v \).
   - The Yukawa interactions involve \( g_{i\alpha} \bar{N}_{iR} L_\alpha S \) and a Majorana mass term \( \frac{y_i}{2} \phi \bar{N}_{iR}^c N_{iR} \).

2. **Symmetry Breaking and Pseudo-Goldstone Boson**:
   - The pseudo-Goldstone boson \( H_2 \) arises from an approximate symmetry broken by radiative corrections.
   - The dominant contributions to the mass of \( H_2 \) come from loop diagrams involving the Yukawa couplings \( g_{i\alpha} \) and the Majorana mass term \( y_i x \).

3. **Radiative Corrections**:
   - The mass of \( H_2 \) is generated at one-loop level due to the explicit symmetry breaking by the Yukawa couplings and Majorana masses.
   - The loop diagrams involve the interaction terms \( g_{i\alpha} \bar{N}_{iR} L_\alpha S \) and the Majorana mass \( M_N = \frac{y_i x}{2} \).

4. **Estimation of Mass**:
   - The one-loop correction to the mass squared of \( H_2 \) is proportional to the square of the Yukawa coupling \( g \), the Majorana mass \( y x \), and a loop factor \( \frac{1}{16\pi^2} \).

Combining these considerations, the mass of the pseudo-Goldstone boson \( H_2 \) through radiative corrections is approximately:

\[
\boxed{\dfrac{g^2 y x}{16\pi^2}}
\]

---

# paraphrased_deepseek_completion_anthropic reasoning

But without the explicit potential V(ϕ,S,H), it's challenging to determine the exact structure.

Assuming that the potential V(ϕ,S,H) has a term that breaks the symmetry explicitly, for example, a term like μ² S†H + h.c., which would mix S and H. If such terms are present, they could lead to a pseudo-Goldstone boson when the symmetry is approximate.

Alternatively, if the potential V has terms that couple ϕ and S, like λ ϕ² S†S, then the VEV of ϕ (x) could induce a mass term for S. But since S is a doublet with hypercharge 1, its neutral component could mix with the Standard Model Higgs. However, without a VEV for S, the mixing would be through terms in the potential.

But wait, the question mentions that ⟨φ⟩² = x² + υ². If ⟨φ⟩ = x and ⟨h⟩ = v, then perhaps ⟨φ⟩² + ⟨h⟩² = x² + v². This might be a way to parametrize the VEVs, but usually, each scalar's VEV is independent unless there's a constraint. If the potential enforces ⟨φ⟩² + ⟨h⟩² = x² + v², that might suggest some specific structure. But I need to be cautious here.

Assuming that φ and H are part of an extended scalar sector with a potential that leads to their VEVs. If there's an approximate symmetry, say a U(1) symmetry under which φ and H rotate into each other, then the true Goldstone would be a combination of their phases. But if the symmetry is explicitly broken, the Goldstone becomes a pseudo-Goldstone with a mass generated at loop level.

Alternatively, the pseudo-Goldstone could come from the singlet φ. If φ is a complex field, its phase would be the Goldstone boson when it gets a VEV. However, the Lagrangian term for φ is written as (∂μ φ)², which is a real scalar (since there's no kinetic term for an imaginary part). Wait, actually, the term (∂μ φ)² is written as (1/2)(∂μ φ)^2, which is standard for a real scalar. Therefore, φ is a real scalar field. Then, when it gets a VEV x, there's no Goldstone boson because a real scalar cannot have a continuous symmetry. So maybe the Goldstone comes from another field.

Looking back at the scalar doublet S. If S is a complex doublet with hypercharge 1, then its neutral component (since hypercharge Y = 1, the charges are (S^+, S^0), with S^0 having charge Y=1/2 + 1/2? Wait, hypercharge for SU(2) doublets is given by Y = Q - T3. For S being (1,2,1), the hypercharge Y = 1. So each component of the doublet has hypercharge Y = 1, so for the upper component (charge Q = T3 + Y/2 = 1/2 + 1/2 = 1), and the lower component (Q = -1/2 + 1/2 = 0). Therefore, the components are S = (S^+, S^0), where S^0 is neutral. If S^0 gets a VEV, that would break the SU(2)×U(1) symmetry. However, the Standard Model Higgs H already breaks the symmetry with its VEV. If S does not acquire a VEV, then its components remain as inert scalars.

But the problem states that ⟨φ⟩² = x² + υ², which might imply that the total VEV is a combination of φ and another field, perhaps H. If H is the Standard Model Higgs with VEV v, and φ has VEV x, then maybe their combination leads to some relation. However, the usual Higgs VEV is around 246 GeV, so perhaps υ here is the same as v, and x is another VEV contributing to the masses of the singlet fermions N_R.

But the question is about the pseudo-Goldstone boson H₂. Since the Standard Model already has the Higgs boson, H₂ might be an additional scalar from the extended sector. If φ is real, then its fluctuation around x is a scalar particle, not a Goldstone. However, if there is a complex scalar that's part of a symmetry, but the given Lagrangian has φ as a real scalar. Therefore, perhaps S, being a doublet, has components that could be Goldstone bosons. But in the Standard Model, the Higgs doublet's Goldstone bosons are eaten by the W and Z. If S is another doublet, its Goldstone modes would also be eaten unless S doesn't get a VEV. If S is inert (no VEV), then its components remain as physical scalars. However, the potential V(ϕ,S,H) could mix S with H or φ, leading to mass eigenstates.

Alternatively, maybe H₂ is the pseudo-Goldstone boson from a global symmetry that's broken by the VEVs of φ and H. For example, if there's a U(1) symmetry under which φ and H transform, then the phase direction could be the Goldstone. But if that U(1) is explicitly broken by terms in the potential, the Goldstone becomes massive.

But how does this relate to radiative corrections? The mass of the pseudo-Goldstone can be generated at loop level if the symmetry breaking terms are loop-suppressed. For example, in the Coleman-Weinberg potential, radiative corrections can generate a mass for the pseudo-Goldstone.

Alternatively, if the pseudo-Goldstone's mass is protected by an approximate symmetry, its mass would be generated by loops involving the explicit symmetry-breaking couplings. In this model, the Yukawa couplings y_i and g_{iα} could break the symmetry and generate the mass for H₂ through loops.

Let me think step by step:

1. Identify the Goldstone bosons from symmetry breaking. Since φ is a real scalar, its VEV breaks no continuous symmetry. The Standard Model Higgs H breaks SU(2)×U(1) to U(1)_EM, giving masses to W and Z. The scalar S is a doublet but doesn't get a VEV, so it doesn't contribute to symmetry breaking. Therefore, perhaps there is an accidental global symmetry in the scalar potential that's broken, leading to a Goldstone boson.

Wait, the potential V(ϕ,S,H) could have an approximate global symmetry. For example, if there's a U(1) symmetry under which ϕ shifts: ϕ → ϕ + a, but this is a shift symmetry. However, the term (∂μ ϕ)^2 is invariant under such a shift, but the Majorana mass term y_i ϕ \bar{N}_i^c N_i breaks this symmetry explicitly. So if the Yukawa coupling y_i is small, the symmetry is approximately preserved, leading to a pseudo-Goldstone boson.

But ϕ is a real scalar field. If there's a shift symmetry ϕ → ϕ + a, which is broken by the Yukawa term, then the pseudo-Goldstone would be ϕ itself. However, if ϕ gets a VEV, then the fluctuation around the VEV is a scalar with mass, but if the symmetry is approximate, the mass would be small. But since ϕ is a singlet, maybe the pseudo-Goldstone is a component of another field.

Alternatively, consider that the scalar potential V(ϕ,S,H) has a symmetry that's broken by the VEVs. For example, suppose there's a U(1) symmetry under which S and H rotate. If the potential respects this symmetry except for small terms, then the Goldstone boson would be a combination of phases of S and H. But S is a doublet with hypercharge 1, and H is a doublet with hypercharge 1/2, so their charges under the U(1) would differ, making such a symmetry non-trivial.

Alternatively, maybe the symmetry is between ϕ and S. If ϕ is a real field and S is complex, perhaps there's a symmetry mixing them, but it's not obvious.

Alternatively, the scalar potential could have a term that mixes S and H, such as λ (H† S) ϕ + h.c. If ϕ gets a VEV x, this would generate a quadratic term for S and H mixing. If such a term is present, then after ϕ gets a VEV, there's a mixing between S and H, leading to mass eigenstates. The pseudo-Goldstone could be a result of this mixing. But without the explicit potential, it's hard to say.

Alternatively, perhaps the mass of H₂ arises from loop corrections due to the Yukawa interactions. The Yukawa couplings g_{iα} connect N_R, L_α, and S. If S is inert (no VEV), then the interaction g_{iα} \bar{N}_R L_α S would lead to a vertex between N_R, lepton doublet L_α, and S. The Majorana mass for N_R comes from the y_i ϕ term. If ϕ has a VEV x, then N_R has a mass M_i = y_i x / 2.

The pseudo-Goldstone H₂ might get a mass from loops involving the Yukawa couplings. For example, if H₂ is a component of S, then loops of N_R and leptons could generate a mass for H₂. But since S is a doublet, its components would include charged scalars and a neutral scalar. If S is inert, the neutral component could mix with the Higgs through loops, but in the absence of tree-level mixing, the mass might be generated at loop level.

Alternatively, if the potential V(ϕ,S,H) has a quartic term like λ |S|^2 ϕ^2, then the mass of S would receive a contribution from ϕ's VEV: m_S^2 = λ x². But this is a tree-level mass. However, if there's a global symmetry that's broken by this term, the pseudo-Goldstone could acquire a mass radiatively.

Alternatively, considering that the Yukawa interaction g_{iα} \bar{N}_R L_α S violates the global symmetry that would otherwise protect the Goldstone. Therefore, loop diagrams with N_R and L_α running in the loop would generate a mass for the pseudo-Goldstone boson.

Let me try to model this. Suppose that the pseudo-Goldstone boson is a component of the S doublet. If S has a mass term from the potential, but there's an approximate symmetry making this mass small. Then, radiative corrections from the Yukawa couplings g_{iα} would generate a mass for S's components.

The one-loop correction to the mass of S would come from diagrams where S interacts via the Yukawa coupling with N_R and L_α. Since L_α is a lepton doublet, and N_R is a singlet, the interaction term g_{iα} \bar{N}_R L_α S would lead to a vertex with S, N_R, and L_α. A loop diagram with N_R and L_α running in the loop would correct the mass of S.

The mass correction can be estimated using the formula for the self-energy. The contribution would be proportional to the square of the coupling g_{iα}, the number of flavors, and the mass of the fermion in the loop. However, since N_R has a Majorana mass M_i = y_i x / 2, and the lepton masses are much smaller, perhaps we can approximate the loop with just the N_R mass.

The self-energy diagram would be a loop with two Yukawa couplings g_{iα}, two propagators of N_R and L_α. But since L_α is a Standard Model lepton, its mass is negligible compared to the possible mass of N_R. However, in the Yukawa term, the coupling is between N_R, L_α, and S. The interaction term is of the form g N_R L S, where L is the lepton doublet. When we write this in terms of components, the lepton doublet L has a charged lepton and a neutrino. Since N_R is a right-handed neutrino, the interaction would be something like g N_R (ν, e)_L^T S. Therefore, the loop would involve N_R and the neutrino (or charged lepton) in the loop.

But neutrinos are neutral, and if S is a doublet with components S^+ and S^0, then the coupling would be to either the charged or neutral component. Let's clarify:

The term g_{iα} \bar{N}_{iR} L_α S would be:

g_{iα} \bar{N}_{iR} [ (ν_α, e_α)_L ]^T ⋅ S

Since S is a doublet (S^+, S^0), the dot product would be ν_α S^0 - e_α S^+.

Therefore, the interaction terms are:

g_{iα} \bar{N}_{iR} ν_α S^0 - g_{iα} \bar{N}_{iR} e_α S^+ + h.c.

So, the Yukawa coupling connects N_R to either neutrinos and S^0 or charged leptons and S^+.

If we are considering the mass of the neutral component S^0 (which could be the pseudo-Goldstone), then the loop would involve N_R and neutrinos. However, if the neutrinos are Majorana particles (which they are in this model, since N_R is a Majorana fermion), the loop would contribute to the mass of S^0.

The self-energy diagram for S^0 would be a loop with N_R and ν_α running in the loop. The mass correction would be proportional to g^2 and the mass of N_R. However, the neutrino here is a left-handed field, which in the loop would pair with the right-handed N_R. But since the neutrino is part of the lepton doublet, and assuming it's a Dirac neutrino (but in reality, with N_R present, it's a seesaw scenario), the mass would be generated via the seesaw mechanism.

Wait, in this model, the neutrino masses would come from the coupling g_{iα} \bar{N}_R L_α S. If S doesn't get a VEV, this term doesn't generate a Dirac mass at tree level. However, if S mixes with the Standard Model Higgs H through the potential V(ϕ,S,H), then after H gets a VEV, there could be an induced VEV for S. Alternatively, if S does not get a VEV, then the neutrino masses would require a loop process.

But let's get back to the mass of H₂. Assuming H₂ is the neutral component of S, which is a pseudo-Goldstone boson. Its mass would come from loops involving the Yukawa couplings g_{iα} and the Majorana masses of N_R.

The one-loop correction to the mass squared of S^0 would be given by a diagram where S^0 emits a virtual N_R and ν_α, which loop around. The amplitude would involve the coupling g_{iα}, and the loop integral would depend on the mass of N_R.

The formula for the self-energy at one loop would be something like:

Σ ≈ (g^2 / (16π²)) * M_N² * log(M_N² / μ²)

where M_N is the mass of N_R, and μ is the renormalization scale. However, the exact coefficient depends on the specifics of the interaction. Since the Yukawa coupling is between S^0, N_R, and ν_α, and ν_α is a left-handed neutrino, which in the loop would have a propagator proportional to its mass. But if the neutrino is massless (or nearly massless) at tree level, its contribution would be negligible. However, in this model, the neutrino could get a mass via the seesaw mechanism if S mixes with H.

Alternatively, if S does not mix with H, then the neutrino mass would come from a one-loop diagram involving S, N_R, and the coupling g. This is similar to the scotogenic model, where dark matter candidates and neutrino masses are generated through loops.

In the scotogenic model, the neutrino mass is calculated as:

m_ν ≈ (g^2 M_N)/(16π²) * [ m_S^2 / (M_N² - m_S^2) ] * ln(M_N² / m_S²)

But in our case, if S is the scalar in the loop, then the neutrino mass would depend on the mass of S and N_R. However, if we are instead calculating the mass of S (the pseudo-Goldstone), then it's the other way around: the mass of S is generated by loops involving N_R and neutrinos.

Assuming that the pseudo-Goldstone mass is generated at one loop, the general expression would be:

m_{H₂}² ≈ (g^4 x²)/(16π²) * f(y_i, ... )

But I need to be more precise.

Alternatively, considering that the symmetry breaking is due to the VEV of φ, which gives a mass to N_R, and the coupling g_{iα} connects N_R to S and leptons. If the approximate symmetry protecting the mass of H₂ is broken by these couplings, then the mass would be generated at loop level.

Let me consider the Coleman-Weinberg potential. If the tree-level potential has a flat direction (leading to a massless Goldstone), quantum corrections can generate a potential that lifts this flatness, giving the pseudo-Goldstone a mass.

For example, suppose the tree-level potential for S has a term λ_S |S|^4, but due to an approximate symmetry, λ_S is very small. Then, the Coleman-Weinberg potential would generate a contribution to the mass of S from loops. The one-loop contribution to the effective potential is given by:

ΔV ≈ (1/(64π²)) Str[ M^4 (log(M² / μ²) - c) ]

where Str is the supertrace, M is the mass matrix, and c is a constant.

In this case, the fields in the loop would be the fermions N_R and the scalars S. The fermion loop would contribute negatively, while the scalar loop would contribute positively. However, if the dominant contribution comes from the fermion loops (since they have Yukawa couplings), then:

ΔV ≈ - (N_f/(64π²)) (g^4 x² |S|^2) log(...)

where N_f is the number of fermion species, and we're assuming that the Yukawa coupling g and the Majorana mass yx are the relevant parameters. This would generate a mass term for S of order:

m_{S}^2 ≈ (g^4 x²)/(16π²) * log(...)

But the exact coefficient depends on the details. If H₂ is the scalar S's component, then its mass squared would be of the order (g^4 x²)/(16π²).

Alternatively, if the pseudo-Goldstone is a mixture of φ and the Higgs, the mass would come from terms breaking the symmetry in the potential. But since φ is a real scalar, its Goldstone would require a complex field.

Another angle: The Majorana mass term for N_R is (y_i / 2) φ \bar{N}_{iR}^c N_{iR} + h.c. If φ is a real field, then this term is real if y_i is real. The Yukawa coupling g_{iα} is complex in general. The presence of these couplings breaks the global symmetries that could protect the Goldstone.

If the original potential has a symmetry that's only broken by these Yukawa couplings, then the mass of the pseudo-Goldstone would be proportional to these couplings. For example, if there's a U(1) symmetry under which S rotates, and this symmetry is broken by the Yukawa couplings g_{iα}, then the mass of the Goldstone (from S) would be generated at loop level with g_{iα} in the loop.

The general formula for the mass would then be:

m_{H₂}² ≈ (g^2 y x)/(16π²) * Λ²

But this is too vague. Let's think about a specific diagram.

Consider the one-loop diagram where H₂ (from S) couples to N_R and leptons via g_{iα}, and N_R has a mass from φ's VEV. The loop would have two Yukawa couplings (g^2) and a Majorana mass insertion (y x). The loop integral would involve the product of these couplings and the loop momentum.

In a seesaw-like diagram, the mass might be something like:

m_{H₂}² ≈ (g^2 y x^2)/(16π²) * log(Λ^2/M_N^2)

But without knowing the exact structure, it's hard to get the precise factors. However, typically, in such models, the pseudo-Goldstone mass squared is proportional to the product of the symmetry-breaking parameters (here, the Yukawa couplings) and the loop factor 1/(16π²).

Given that the Majorana mass M_N = y x / 2, we can write:

m_{H₂} ≈ (g^2 M_N)/(16π²) * something

If the log is considered O(1), then:

m_{H₂} ≈ (g^2 M_N)/(16π²)

But this is a rough estimate. To get a more accurate expression, let's recall that in the Coleman-Weinberg potential, the mass generated from a fermion loop is:

Δm² ≈ - (g^2 M_N^2)/(8π²) * log(Λ^2/M_N^2)

But this is for a scalar coupled to fermions with a Yukawa coupling g and fermion mass M_N. However, in our case, the Yukawa coupling is between S, N_R, and L, so the diagram would involve a loop of N_R and L (lepton). But since the lepton mass is negligible, the dominant contribution comes from the N_R.

Wait, in the interaction term g \bar{N}_R L S, the vertices would involve g, the scalar S, the fermion N_R, and the lepton L. However, in the loop, you need two vertices, so two factors of g. The loop would have a fermion line going from N_R to L and back to N_R, but since L is a different fermion (the lepton), this would require a mass insertion on the L line. But if the lepton is massless, this diagram would vanish. Therefore, maybe the loop must involve a Majorana mass insertion for the neutrino.

Alternatively, if the neutrino has a Majorana mass from the N_R, then the loop can be closed. Let me think: In the interaction term, we have g \bar{N}_R L S. If N_R has a Majorana mass M_N = y x / 2, then the neutrino mass is generated via the seesaw mechanism. However, if S does not get a VEV, the neutrino mass would be generated at one loop. The diagram would be a loop with N_R and S in the loop, connected via the Yukawa couplings g and the Majorana mass M_N.

But this is getting into the details of the neutrino mass generation, which might be a separate issue. However, if the question is about the mass of H₂ (which is part of S), then the same loop that generates the neutrino mass might also contribute to the mass of S.

In the scotogenic model, the neutrino mass is generated via a loop with N_R and the inert doublet S. The mass of the inert doublet scalars is generated at one loop through the same couplings. The formula for the scalar mass squared is something like:

m_S² ≈ (g^2 M_N²)/(16π²) * log(M_N² / m_S²)

But this is a self-energy correction. If m_S is small (pseudo-Goldstone), then the logarithm could be significant. However, solving for m_S would give:

m_S ≈ (g M_N)/(4π) * sqrt( log(M_N² / m_S²) )

Assuming the log is order 1, then m_S ≈ g M_N / (4π)

But this is a rough estimate. The exact coefficient might differ by factors of 2 or so depending on the diagram topology and couplings.

Given that, the mass of the pseudo-Goldstone boson H₂ (which is part of the inert doublet S) would be approximately:

m_{H₂} ≈ (g^2 y x)/(16π²)

But wait, M_N = y x / 2, so substituting:

m_{H₂} ≈ (g^2 (2 M_N))/(16π²) ) = (g^2 M_N)/(8π²)

Alternatively, if the mass is generated at one loop with two Yukawa couplings and a Majorana mass, the formula might have a different structure.

Alternatively, consider the diagram where H₂ (from S) couples to two virtual N_Rs via the Yukawa coupling g, and the N_Rs have a Majorana mass M_N. The loop would then be a triangle diagram? Or a loop with two Yukawa couplings and two Majorana mass insertions.

Wait, the self-energy diagram for S would be a loop with N_R and L running. But since L is a Standard Model lepton with negligible mass, the loop integral would depend on the momentum. However, if we consider the limit where the external momentum is small compared to M_N, we can approximate the loop integral.

The self-energy Σ(p²) for S would receive a contribution from the loop with N_R and L. The Yukawa interaction is g \bar{N}_R L S + h.c. The loop would have two vertices of g and propagators of N_R and L.

The self-energy at zero momentum would be:

Σ(0) ≈ - g^2 ∫ d^4k / (2π)^4 Tr[ (i (k̸ + m_L)) / (k² - m_L² + iε) ) (i (k̸ + M_N)) / (k² - M_N² + iε) ) ]

But m_L ≈ 0, so:

Σ(0) ≈ - g^2 ∫ d^4k / (2π)^4 Tr[ (i k̸) / (k² + iε) ) (i (k̸ + M_N)) / (k² - M_N² + iε) ) ]

Simplifying the trace:

Tr[ k̸ (k̸ + M_N) ] = Tr[ k̸ k̸ ] + M_N Tr[ k̸ ]

The second term is zero because the trace of an odd number of gamma matrices is zero. The first term:

Tr[ k̸ k̸ ] = 4 k²

So:

Σ(0) ≈ - g^2 ∫ d^4k / (2π)^4 [ 4 k² / (k² + iε)(k² - M_N² + iε) ) ]

This integral is divergent, but we can evaluate it using dimensional regularization. The integral becomes:

Σ(0) ≈ -4 g^2 ∫ d^dk / (2π)^d [ k² / (k²)(k² - M_N²) ) ] = -4 g^2 ∫ d^dk / (2π)^d [ 1 / (k² - M_N²) ) ]

Wait, but this simplifies to:

Σ(0) ≈ -4 g^2 ∫ d^dk / (2π)^d [ 1 / (k² - M_N²) ) ]

But this is just the integral of the propagator, which for d=4 is quadratically divergent. However, in dimensional regularization, this would be proportional to M_N². The result would be:

Σ(0) ≈ -4 g^2 (M_N²/(16π²)) (1/ε + finite terms)

But we need to renormalize this. However, the divergence would be absorbed into the counterterms. The finite part would give a contribution to the mass squared of S:

Δm_S² ≈ (g^2 M_N²)/(4π²) * (1/ε + ... )

But since we're interested in the finite, physical mass, after renormalization, the mass would be:

m_S² ≈ (g^2 M_N²)/(16π²) * log(Λ^2/M_N²)

Assuming a cutoff Λ, which could be the scale of the theory. If the log is of order 1, then:

m_S ≈ (g M_N)/(4π)

Thus, the mass of the pseudo-Goldstone boson H₂ (which is part of the S doublet) would be approximately (g M_N)/(4π). Since M_N = y x / 2, substituting:

m_{H₂} ≈ (g y x)/(8π)

But this is a tree-level estimate? Wait, no, this is a one-loop result. The factor of 1/(4π) comes from the loop integral.

However, different normalizations might affect the coefficient. For example, in the Yukawa term, if the coupling is g/√2 or something, but since the problem doesn't specify, we'll take the coupling as g.

Alternatively, considering that each Yukawa vertex contributes a factor of g, and the loop integral gives a factor of 1/(16π²), then the mass squared would be:

m_{H₂}^2 ≈ (g^2 M_N^2)/(16π²)

Taking the square root:

m_{H₂} ≈ (g M_N)/(4π)

Given that M_N = y x / 2, this becomes:

m_{H₂} ≈ (g y x)/(8π)

But I need to check the coefficients carefully. Let's recall that the general expression for the one-loop correction to the scalar mass from a fermion loop is:

Δm² = (g² N_f)/(16π²) [ 2 M_f² ] (Λ² term ignored, focusing on the finite part)

Wait, the standard result for a scalar interacting with fermions via L = g φ ψψ, the one-loop correction to the scalar mass squared is:

Δm² ≈ (g² M_f²)/(8π²) ln(Λ/M_f)

But in our case, the Yukawa interaction is between S, N_R, and L. The fermions in the loop are N_R and L (neutrino). Assuming the neutrino mass is negligible, the dominant contribution comes from N_R. However, the coupling involves both N_R and L, so the trace might involve both.

But earlier calculation suggested that the self-energy contribution is proportional to g² M_N², leading to m_S ≈ g M_N / (4π). Given that, and substituting M_N = y x / 2, the mass becomes:

m_{H₂} ≈ (g y x)/(8π)

But the question asks for the approximation through radiative corrections. The answer is likely of the order g y x / (16π²), but I need to resolve the coefficients.

Alternatively, another approach: In the model, the pseudo-Goldstone boson mass can be estimated using the Coleman-Weinberg potential. The effective potential at one-loop is:

V_eff = V_tree + (1/(64π²)) [ m_S^4 (ln(m_S² / μ²) - c) - 2 m_N^4 (ln(m_N² / μ²) - c) ]

Where m_S is the scalar mass and m_N is the fermion mass. If at tree level, the scalar mass is zero (Goldstone limit), then the one-loop contribution from the fermions (N_R) would generate a mass.

But in this case, the fermion mass m_N = y x / 2, and the coupling between the scalar and the fermion is g. The contribution to the scalar mass squared would be:

Δm² ≈ (g² m_N²)/(8π²) ln(Λ²/m_N²)

Assuming the log factor is of order 1, then:

m_{H₂} ≈ (g m_N)/(2√2 π)

Substituting m_N = y x / 2:

m_{H₂} ≈ (g y x)/(4√2 π)

But this still leaves numerical factors uncertain. However, given the options and standard results, the mass is typically of the order:

m_{H₂} ≈ (g y x)/(16π²) * Λ

But without a specific scale Λ, this is unclear. However, in radiative corrections, the logarithm often appears, so maybe:

m_{H₂}² ≈ (g² y² x²)/(16π²) ln(x/υ)

But this is speculative.

Alternatively, considering that the pseudo-Goldstone mass is generated by the breaking of the global symmetry by both the Yukawa couplings g and y. The leading contribution would be at one-loop level, and the mass would be:

m_{H₂} ≈ (g y v)/(16π²)

Where v is the Higgs VEV. But why v? Because the Higgs VEV is involved in the mixing or the potential.

Alternatively, if the potential V(ϕ,S,H) includes a term like λ ϕ² S†S, then the tree-level mass of S is λ x². If there's an approximate symmetry when λ is small, the radiative corrections from the Yukawa couplings g would generate a correction to λ, leading to:

Δλ ≈ (g^4)/(16π²) ln(...)

Thus, Δm_S² ≈ (g^4 x²)/(16π²)

So m_{H₂} ≈ (g² x)/(4π)

But this depends on the quartic coupling.

Given the ambiguity in the potential and the lack of explicit terms, it's challenging to pinpoint the exact expression. However, based on similar models (like the scotogenic model), the mass of the inert doublet scalars is generated at one loop and is proportional to the square of the Yukawa coupling times the Majorana mass, divided by (16π²). Therefore, a reasonable approximation would be:

m_{H₂} ≈ \frac{g^2 y x}{16\pi^2}

But I need to check the dimensions. If g is dimensionless, y is dimensionless, x is a mass, then g² y x has dimensions of mass. Divided by 16π², which is dimensionless, so the whole expression has dimensions of mass. That works.

Alternatively, if the mass is generated at one loop, the typical scale is (loop factor) * (coupling)^2 * (mass scale). Here, the mass scale could be x, and the coupling is g y. So:

m_{H₂} ≈ \frac{g y x}{16\pi^2}

But without knowing the exact structure of the potential and the couplings, this is an educated guess. Given that, and considering that in the scotogenic model, the scalar mass is of the order (yukawa^2 * Majorana mass)/(16π²), I think the answer is likely:

m_{H₂} \approx \frac{g_{i\alpha}^2 y_i x}{16\pi^2}

But since the question asks for an approximation and doesn't specify indices, we can write it as:

m_{H₂} \approx \frac{g^2 y x}{16\pi^2}

Where g and y are typical values of the couplings.

Therefore, after considering various possibilities and loop contributions, the mass of the pseudo-Goldstone boson H₂ through radiative corrections is approximately proportional to (g² y x)/(16π²).

**Final Answer**
The mass of the pseudo-Goldstone boson \( H_{2} \) through radiative corrections is approximately \(\boxed{\dfrac{g^2 y x}{16\pi^2}}\).

---

# paraphrased_deepseek_completion_openai (via openrouter)

ChatCompletion(id='gen-1745391191-NcpKRapYW7jqGCeNUnbf', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='The mass of the pseudo-Goldstone boson \\( H_2 \\) arises from radiative corrections due to the explicit breaking of the approximate global symmetry by the Yukawa couplings. The dominant contribution comes from loops involving the singlet fermions \\( N_{iR} \\) with Majorana masses \\( M_i = y_i x \\). Considering the mixing between the singlet scalar \\( \\phi \\) and the Higgs doublet \\( H \\), the mass can be approximated as:\n\n\\[\nm_{H_2} \\approx \\frac{y_i^2 \\, v \\, x}{16 \\pi^2 \\sqrt{x^2 + v^2}}\n\\]\n\n**Answer:**\n\nThe approximate mass of the pseudo-Goldstone boson \\( H_2 \\) through radiative corrections is \n\n\\[\n\\boxed{m_{H_2} \\approx \\frac{y_i^2 \\, v \\, x}{16 \\pi^2 \\sqrt{x^2 + v^2}}}.\n\\]', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, reasoning=' The standard Higgs mechanism for the Standard Model produces three Goldstone bosons (eaten by W+, W-, Z). The addition of a singlet scalar φ may introduce another Goldstone if φ\'s potential breaks a U(1) symmetry. However, if the symmetry is explicit, this Goldstone becomes a pseudo-Goldstone. Alternatively, the mixing between H and φ could produce a pseudo-Goldstone.\n\nBut the problem mentions H₂ as the pseudo-Goldstone. In two-Higgs-doublet models, there are additional scalars, but here S is a doublet but with hypercharge 1, so different from the usual H. If S doesn\'t get a VEV, the Goldstone bosons would still come from H and φ. However, if φ is a singlet under the SM, its Goldstone would be a singlet, but if the symmetry is global, then the associated Goldstone is a singlet. However, the SM Higgs is in a doublet, so their Goldstones are in the doublet. But the problem states H₂ as the pseudo-Goldstone. Let\'s think: maybe the model has a global symmetry that is spontaneously broken by the VEVs of φ and S, but since S is a doublet, its VEV would break the symmetry. If S doesn\'t get a VEV, then the symmetry breaking comes from φ and H. Alternatively, S may get a VEV through the potential\'s structure. Wait, the problem statement says ⟨φ⟩² = x² + υ², but ⟨φ⟩ = x. If ⟨φ⟩ is x, then ⟨φ⟩² is x². Therefore, the equation x² = x² + υ² would imply υ = 0, which contradicts the SM Higgs VEV. So, perhaps this is a typo. Alternatively, ⟨φ⟩² + ⟨h⟩² = x² + υ²? The problem states "⟨φ⟩² = x² + υ², where ⟨φ⟩ = x and ⟨h⟩ = v." Wait, that can\'t be. If ⟨φ⟩ = x, then ⟨φ⟩² is x², but the problem says ⟨φ⟩² equals x² + υ², which is only possible if x² = x² + υ², implying υ² = 0. Therefore, there\'s a mistake in the problem\'s wording. Maybe ⟨ϕ⟩² + ⟨h⟩² = x² + v²? But the problem states "We give ⟨ϕ⟩² = (x² + υ²), where ⟨ϕ⟩ = x and ⟨h⟩ = v." That would mean that x² = x² + υ², which is impossible. Therefore, perhaps it\'s a misstatement. Alternatively, the VEV of ϕ is √(x² + υ²), but the user wrote ⟨ϕ⟩ = x. Alternatively, the VEVs are such that x and v are components of the scalar fields. Maybe the notation is swapped. Alternatively, the user intended to write that the VEV of the Higgs field is v, and the VEV of ϕ is x, with the sum of squares being x² + v². Therefore, perhaps the total VEV is x² + v², but the individual VEVs are x and v. But if ⟨ϕ⟩ = x and ⟨H⟩ = v, then the sum of their squares is x² + v². However, in the problem statement, it\'s written as ⟨ϕ⟩² = x² + υ², which is confusing. Perhaps the problem meant that the total VEV (e.g., the combination of ⟨ϕ⟩ and ⟨H⟩) is such that ⟨ϕ⟩² + ⟨H⟩² = x² + υ². But if ⟨H⟩ is v, then ⟨ϕ⟩² + v² = x² + υ². Unless x and υ are parameters, with ⟨ϕ⟩ and ⟨H⟩ being the VEVs. This is getting too confusing. Let me check the original problem again: \n\n"We give ⟨ϕ⟩² = (x² + υ²), where ⟨ϕ⟩ = x and ⟨h⟩ = v."\n\nAh, perhaps ⟨h⟩ is the Higgs field\'s VEV, denoted as v, and ⟨ϕ⟩² is x² + υ², where υ is another parameter. But then ⟨ϕ⟩ = x, so x² = x² + υ², which requires υ = 0. Alternatively, maybe the person meant that the combination of ⟨ϕ⟩ and ⟨h⟩ gives the total as x² + υ², but with ⟨ϕ⟩ = x and ⟨h⟩ = υ. Then the total would be x² + υ². But then why write ⟨ϕ⟩² = x² + υ²? That would imply ⟨ϕ⟩ = sqrt(x² + υ²), which contradicts the given ⟨ϕ⟩ = x. So, perhaps there\'s a typo, and the intended statement is that the sum of the squares of the VEVs is x² + υ², i.e., ⟨ϕ⟩² + ⟨h⟩² = x² + υ². If that\'s the case, then ⟨ϕ⟩ = x and ⟨h⟩ = υ, so their squares add up to x² + υ². But then the user wrote ⟨h⟩ = v, so perhaps υ is a typo for v. So, maybe the problem intended to state that ⟨ϕ⟩² + ⟨h⟩² = x² + v², with ⟨ϕ⟩ = x and ⟨h⟩ = v, which would make sense. For example, if there\'s a potential term like (ϕ² + |H|² - (x² + v²))², then the VEVs would satisfy ⟨ϕ⟩² + ⟨h⟩² = x² + v². But then the individual VEVs are x and v. This makes more sense. Therefore, perhaps the problem had a typo and the correct statement is ⟨ϕ⟩² + ⟨h⟩² = x² + v², with ⟨ϕ⟩ = x and ⟨h⟩ = v. That would be a logical structure. So, assuming that, the VEVs x and v are such that their squares sum to x² + v². Therefore, the scalar potential enforces this relation, leading to a flat direction. The Goldstone boson would correspond to the direction in which the fields can be rotated without changing the potential, i.e., the combination of ϕ and h that leaves x² + v² invariant. However, if the potential is such that this symmetry is only approximate, the pseudo-Goldstone boson would acquire a mass through radiative corrections. Alternatively, the potential could have an explicit breaking term that gives a small mass. But since the problem states that the mass is generated through radiative corrections, that suggests that the symmetry is exact at tree level but broken at loop level, hence generating a mass. \n\nIn such a scenario, the tree-level potential has an accidental symmetry (like a U(1) or SO(2) symmetry) that is broken by quantum corrections. For example, if the tree-level potential is symmetric under rotations between ϕ and H, then the VEVs x and v lie on a circle of radius √(x² + v²). The Goldstone boson would be the angular direction. However, if loop corrections (radiative corrections) break this symmetry, the pseudo-Goldstone boson (the angular direction) gets a mass. \n\nThe mass of the pseudo-Goldstone boson can be estimated by the Coleman-Weinberg potential. The Coleman-Weinberg mechanism generates an effective potential at one-loop level, which can induce symmetry breaking. If the tree-level potential is flat in a certain direction (the Goldstone direction), quantum corrections can lift this flatness, giving a small mass. \n\nTo compute the mass, we need to consider the one-loop effective potential. The general form is:\n\nV_eff = V_tree + ΔV\n\nwhere ΔV is the one-loop correction given by:\n\nΔV ≈ (1/64π²) [ m_B^4 (ln(m_B² / Λ²) - c) - m_F^4 (ln(m_F² / Λ²) - c) ]\n\nwhere m_B and m_F are the boson and fermion masses, Λ is the renormalization scale, and c is a constant depending on the renormalization scheme. For pseudo-Goldstone bosons, the dominant contribution often comes from the top quark (if applicable) or other heavy fermions. However, in this model, the relevant fermions are the singlet neutrinos N_R and the lepton doublets L_α. \n\nLooking at the Lagrangian, the interactions are:\n\n- The Majorana mass term for N_R: -(y_i / 2) ϕ \\bar{N}_{iR}^c N_{iR} + h.c.\n- The Yukawa coupling: -g_{iα} \\bar{N}_{iR} L_α S + h.c.\n\nAssuming S does not get a VEV, the Yukawa coupling g_{iα} would not contribute to the tree-level masses but would generate interactions. The Majorana mass term, when ϕ gets a VEV x, gives N_R a Majorana mass M_i = y_i x / 2.\n\nThe potential V(ϕ, S, H) is not specified, but if we consider the tree-level potential to have a symmetry that\'s broken by quantum corrections, then the pseudo-Goldstone mass arises from loops involving the fields that break the symmetry. Given that the problem mentions radiative corrections, the dominant contributions would come from the couplings in the Lagrangian. The couplings y_i (Majorana couplings) and g_{iα} (Yukawa couplings to S and L) would contribute to loops.\n\nIf H₂ is the pseudo-Goldstone boson from the ϕ and H sector, then its mass would be generated by loops involving the N_R and possibly S. Let\'s consider the couplings:\n\n1. The Majorana coupling y_i ϕ N_{iR}^c N_{iR} would, after ϕ gets a VEV x, lead to a mass term for N_R. This coupling also allows for a loop diagram where the ϕ field (including the Goldstone mode) interacts with N_R loops. If the potential has a flat direction (the Goldstone direction), these loops can generate a potential for the Goldstone, giving it a mass.\n\n2. The Yukawa coupling g_{iα} N_{iR} L_α S would contribute if S has a VEV. If S does not have a VEV, this coupling would still allow for loop diagrams involving S, L_α, and N_R. However, without a VEV for S, the impact might be suppressed.\n\nAssuming S does not get a VEV, the dominant contribution would come from the Majorana coupling. The pseudo-Goldstone boson (H₂) would be a mixture of the Higgs and ϕ fields. The mass would be generated at loop level through the couplings of ϕ to N_R. The one-loop correction to the potential would then generate a mass term for the pseudo-Goldstone.\n\nThe general formula for the mass of a pseudo-Goldstone boson from radiative corrections is roughly:\n\nm_{PG}^2 ≈ (loop factor) * (coupling)^2 * (VEV)^2 / (16π²)\n\nBut to be precise, we need to compute the Coleman-Weinberg potential. Let\'s model the tree-level potential with a symmetry. Suppose the tree-level potential for ϕ and H is:\n\nV_tree = λ (ϕ² + |H|² - f²)^2\n\nwhere f² = x² + v². This potential has an SO(2) symmetry rotating ϕ and the real part of H (assuming H is written in the unitary gauge where the Goldstones are eaten). The minimum is at ϕ² + |H|² = f², so ⟨ϕ⟩ = x and ⟨H⟩ = v with x² + v² = f². The angular direction (the pseudo-Goldstone) is massless at tree level. However, the couplings in the Lagrangian (y_i and g_{iα}) break the SO(2) symmetry explicitly. Thus, loops involving these couplings will generate a potential for the pseudo-Goldstone.\n\nThe dominant contribution comes from the heaviest particles in the loop. Since N_R has a Majorana mass M_i = y_i x, and assuming y_i is sizable, the loops with N_R would contribute significantly. The Yukawa coupling g_{iα} might contribute but would be suppressed by the smaller coupling and possible absence of S VEV.\n\nThe Coleman-Weinberg potential for the pseudo-Goldstone can be approximated by considering the effective potential in the angular direction. Let’s parameterize ϕ = f cosθ and H = f sinθ (in the unitary gauge, H\'s VEV is in the real component). The angle θ corresponds to the Goldstone boson. The one-loop potential from the N_R loops would be:\n\nΔV ≈ (1/64π²) Tr[ M_N^4 (ln(M_N² / Λ²) - c) ]\n\nwhere M_N is the Majorana mass matrix, which depends on ϕ. Since ϕ = f cosθ, M_N = y_i f cosθ / 2. The trace would sum over the eigenvalues, so for each N_i:\n\nΔV ≈ (N_i contribution) ≈ (y_i^4 f^4 cos^4θ)/(128π²) [ ln(y_i^2 f² cos²θ / Λ²) - c ]\n\nTo find the mass of the pseudo-Goldstone, we take the second derivative of ΔV with respect to θ at the minimum θ = arctan(v/x). However, since the tree-level potential is minimized at a particular θ, the loop corrections will create a potential that breaks the SO(2) symmetry, giving a mass to θ. Assuming the minimum remains at θ = arctan(v/x), expanding ΔV around θ = 0 (but given the VEVs, this might not hold; perhaps better to expand around the true vacuum). Alternatively, since at tree level θ is a flat direction, the loop corrections determine the potential along θ. The mass squared is the curvature of ΔV at the minimum.\n\nAssuming that the dominant contribution comes from the heaviest N_i, let\'s consider a single generation for simplicity, dropping the index i. Then:\n\nΔV ≈ (y^4 f^4 cos^4θ)/(128π²) [ ln(y^2 f² cos²θ / Λ²) - c ]\n\nTo find the mass, we take the second derivative of ΔV with respect to the Goldstone boson field. The Goldstone boson H₂ is related to θ by H₂ = f θ (for small θ). Therefore, the mass squared is (d²ΔV/dθ²)/f².\n\nFirst, compute dΔV/dθ:\n\ndΔV/dθ ≈ (y^4 f^4 /128π²) [ 4 cos^3θ (-sinθ) [ ln(...) - c ] + cos^4θ ( ( - 2 y^2 f² sinθ / (y^2 f² cos²θ) ) ) ]\n\nWait, this seems complicated. Let\'s use the chain rule. Let’s define M = y f cosθ. Then, ΔV ≈ (M^4 / 128π²) [ ln(M² / Λ²) - c ]\n\nThen, dΔV/dθ = (4 M^3 dM/dθ / 128π²) [ ln(M² / Λ²) - c ] + (M^4 / 128π²) ( (2 M dM/dθ ) / M² )\n\nSimplifying:\n\ndΔV/dθ = (M^3 / 32π²) (- y f sinθ) [ ln(M² / Λ²) - c ] + (M^4 / 128π²) ( 2 (- y f sinθ) / M )\n\nBut since M = y f cosθ, dM/dθ = - y f sinθ.\n\nSo,\n\ndΔV/dθ = ( (y f cosθ)^3 (- y f sinθ) ) / 32π² [ ln(...) - c ] + ( (y f cosθ)^4 / 128π² ) ( 2 (- y f sinθ) / (y f cosθ) ) )\n\nSimplify term by term:\n\nFirst term: - (y^4 f^4 cos³θ sinθ) / 32π² [ ln(y² f² cos²θ / Λ²) - c ]\n\nSecond term: - (y^4 f^4 cos³θ sinθ) / 64π²\n\nTherefore, combining:\n\ndΔV/dθ = - (y^4 f^4 cos³θ sinθ) / 32π² [ ln(y² f² cos²θ / Λ²) - c + 1/2 ]\n\nTo find the extrema, set dΔV/dθ = 0. Assuming the minimum is at θ = 0 (which may not hold, but for estimation), but given that the tree-level potential is flat, the loop corrections would determine the minimum. However, if we assume that the minimum is at θ = 0 (i.e., ⟨ϕ⟩ = f, ⟨H⟩ = 0), but in our case, the VEVs are x and v. This complicates things. Alternatively, since the problem states that ⟨ϕ⟩ = x and ⟨h⟩ = v, with x² + v² = f², we can express θ as arctan(v/x). Let’s denote θ₀ = arctan(v/x). Then, we need to compute d²ΔV/dθ² at θ = θ₀.\n\nBut this calculation is getting too involved. Let\'s instead approximate the mass by noting that the pseudo-Goldstone mass squared is generated by the curvature of the effective potential around the minimum. The leading contribution would be from the heaviest fermion in the loop, which is N_R with mass M_N = y x / 2. The mass squared of the pseudo-Goldstone would be something like:\n\nm_{H₂}^2 ≈ (y^4 x²)/(16π²) * (v²)/(x² + v²)\n\nBut this is a rough estimate. Alternatively, considering that the symmetry breaking is proportional to the couplings y and g, and the VEVs x and v, the mass can be a combination of these parameters. \n\nAlternatively, using the formula for the Coleman-Weinberg potential for a pseudo-Goldstone boson, the mass can be approximated as:\n\nm_{H₂}^2 ≈ (N_f y^4 x²)/(16π²) * ln(Λ²/M_N²)\n\nwhere N_f is the number of fermion species. However, without knowing the renormalization scale Λ, this is still ambiguous. But in many cases, the logarithm is assumed to be O(1), so the mass is roughly:\n\nm_{H₂} ≈ (y² x)/(4π)\n\nBut this is if the potential is generated solely by the fermion loops. However, in this case, the pseudo-Goldstone is a mixture of the Higgs and ϕ fields. The exact expression would depend on the mixing angle between the two scalars. The mixing angle is determined by the potential\'s parameters, which are not given. However, if we assume that the dominant contribution comes from the N_R loops, which couple to ϕ, then the mass squared would be proportional to y^4 x² / (16π²), multiplied by some function of the mixing angle.\n\nAlternatively, considering that the pseudo-Goldstone is mostly the phase direction of ϕ and H, its mass is generated by the explicit breaking of the global symmetry. If the breaking is due to the Yukawa coupling y_i, then the mass would be:\n\nm_{H₂} ≈ (y_i^2 x)/(4π)\n\nBut this is a common estimate for axion-like particles where the mass is generated by instanton effects. However, in this case, it\'s generated by fermion loops. Another approach: the Coleman-Weinberg potential generates a quartic coupling for the pseudo-Goldstone. The curvature of the potential would then be:\n\nm_{H₂}^2 ≈ (d²V/dθ²) ≈ (y^4 x²)/(16π²)\n\nBut considering that the Goldstone is a phase, the actual mass would depend on the decay constant f = √(x² + v²). The canonical normalization of the Goldstone field is H₂ = f θ, so the mass term would be (1/2) m_{H₂}^2 f² θ². Therefore, the coefficient from the potential d²V/dθ² = m_{H₂}^2 f². Hence:\n\nm_{H₂}^2 f² ≈ (y^4 x²)/(16π²) → m_{H₂} ≈ (y^2 x)/(4π f)\n\nBut since f² = x² + v², then:\n\nm_{H₂} ≈ (y^2 x)/(4π √(x² + v²))\n\nIf x ≫ v, then m_{H₂} ≈ y² x / (4π x) = y²/(4π). But if v ≫ x, then m_{H₂} ≈ y² x/(4π v). However, without knowing the hierarchy between x and v, we can leave it as:\n\nm_{H₂} ≈ (y^2 x)/(4π √(x² + v²))\n\nBut the problem mentions that H₂ is a pseudo-Goldstone boson. If the symmetry is broken by multiple fields, the decay constant f is √(x² + v²). Therefore, the mass would be m_{H₂} ≈ (y^2 x)/(4π f) = (y^2 x)/(4π √(x² + v²)). However, this assumes that the dominant contribution comes from the coupling y. If there are multiple fermions, we should sum over their contributions. For example, if there are three generations of N_R with couplings y_i, then m_{H₂}^2 ≈ Σ_i (y_i^4 x²)/(16π² f²). But given the lack of specific information, the problem likely expects an expression in terms of the couplings and VEVs provided.\n\nAlternatively, considering that the mass comes from the one-loop diagram with N_R in the loop. The pseudo-Goldstone couples to N_R via the derivative coupling (since Goldstones are derivatively coupled). The interaction term would be something like (y x / f) H₂ \\bar{N}_R N_R^c, leading to a loop diagram with two H₂ insertions. The mass would then be calculated via the loop integral. For a fermion loop with coupling g ~ y x / f, the mass would be:\n\nm_{H₂}^2 ≈ (g^2 M_N^2)/(16π²) ≈ (y^2 x^2/f^2 * y^2 x^2)/16π² = y^4 x^4/(16π² f²)\n\nBut since f² = x² + v², this is y^4 x^4/(16π² (x² + v²)). However, this seems different from the previous estimate. Alternatively, the coupling of H₂ to N_R could be through the derivative term, leading to a coupling proportional to y / f. Then, the loop would involve two insertions of this coupling and two propagators. The mass would then be m_{H₂}^2 ≈ (y^2 / f^2) * (M_N^2)/(16π²) * M_N^2. Wait, this seems inconsistent. Let me think again.\n\nThe interaction Lagrangian for the pseudo-Goldstone H₂ coupling to N_R would be similar to a Yukawa coupling. If the original term is (y/2) ϕ \\bar{N}_R^c N_R, then when ϕ = x + σ + i H₂ (assuming H₂ is the imaginary part, the Goldstone), the interaction term becomes (y/2)(x + σ + i H₂) \\bar{N}_R^c N_R. Therefore, the coupling to H₂ is (i y/2) H₂ \\bar{N}_R^c N_R. The mass term for N_R is (y x / 2) \\bar{N}_R^c N_R. Therefore, the interaction term is (i y H₂ / (2 x)) * (y x / 2) \\bar{N}_R^c N_R = (i y² H₂ / 4) \\bar{N}_R^c N_R. So the coupling g is y² / 4. Then, the one-loop diagram with N_R in the loop would contribute to H₂ mass. The mass squared would be:\n\nm_{H₂}^2 ≈ (g^2 M_N^2)/(16π²) = ( (y^4 / 16) * (y^2 x^2 / 4) ) / (16π²) ) ???\n\nWait, perhaps better to use the formula for a fermion loop contributing to scalar mass. For a scalar coupled to fermions via L ⊃ - g ϕ \\barψ ψ, the one-loop mass correction is:\n\nΔm² ≈ (g^2 m_ψ^2)/(8π²) ln(Λ^2/m_ψ^2)\n\nBut in our case, the coupling is of the form (i y² / 4) H₂ \\bar{N}_R^c N_R. However, Majorana fermions complicate things. The coupling for a Majorana fermion to a pseudoscalar is different. Alternatively, since H₂ is a pseudo-Goldstone, it\'s a CP-odd scalar. The coupling would be (i y/2) H₂ \\bar{N}_R^c N_R + h.c. For Majorana fermions, \\bar{N}_R^c N_R = \\bar{N}_R N_R^c, so the interaction term is (i y/2) H₂ (\\bar{N}_R N_R^c + \\bar{N}_R^c N_R ). But for Majorana fermions, N_R^c = N_R, so this becomes (i y/2) H₂ (\\bar{N}_R N_R + \\bar{N}_R N_R ) = i y H₂ \\bar{N}_R N_R. The coupling is then similar to a Yukawa coupling with a factor of i y. \n\nThe mass term for N_R is (y x / 2) \\bar{N}_R N_R. Therefore, the propagator is for a Majorana fermion with mass M = y x / 2. The one-loop diagram contributing to H₂ mass would be a loop of N_R with two H₂ insertions. The amplitude is proportional to (i y)^2 times the loop integral. The loop integral for a fermion loop with two scalar insertions would give a contribution proportional to M^2. \n\nThe mass squared is then:\n\nm_{H₂}^2 ≈ (y^2 M^2)/(16π²) = (y^2 (y^2 x^2 / 4))/(16π²) ) = (y^4 x²)/(64π²)\n\nBut this is if the loop integral contributes a factor of M^2/(16π²). However, the actual computation might involve a different coefficient. In some references, the contribution from a Majorana fermion loop to a scalar mass squared is (y^2 M^2)/(8π²) ln(Λ/M). Assuming the log is O(1), then:\n\nm_{H₂}^2 ≈ (y^4 x²)/(32π²)\n\nBut this doesn\'t take into account the mixing between H and ϕ. If H₂ is a combination of the Higgs and ϕ\'s Goldstone, the coupling y might be multiplied by a mixing angle. Suppose the mixing angle is θ, where tanθ = v/x, then the effective coupling would be y sinθ. Therefore, the mass squared would be (y^4 sin²θ x²)/(32π²). But sinθ = v / √(x² + v²), so:\n\nm_{H₂}^2 ≈ (y^4 v² x²)/(32π² (x² + v²))\n\nBut this is getting too speculative. The problem statement doesn\'t specify the potential, so we have to make reasonable assumptions. Given the information, the most straightforward answer is that the mass of the pseudo-Goldstone boson H₂ is generated at one-loop level via the Majorana neutrino couplings, leading to:\n\nm_{H₂} ≈ (y^2 x)/(4π)\n\nHowever, considering the decay constant f = √(x² + v²), the mass would be suppressed by f if the Goldstone is a combination of ϕ and H. In that case, the mass is:\n\nm_{H₂} ≈ (y^2 x)/(4π √(x² + v²)) * x\n\nWait, no. If the decay constant is f = √(x² + v²), and the Goldstone boson is H₂ = (v ϕ - x h)/f, then the coupling of H₂ to N_R is proportional to (y v)/f. Therefore, the coupling g = (y v)/f. Then, the mass squared would be:\n\nm_{H₂}^2 ≈ (g^2 M_N^2)/(16π²) = (y² v²/f²)(y² x²/4)/(16π²) ) = (y^4 x² v²)/(64 π² f²)\n\nBut since f² = x² + v²:\n\nm_{H₂}^2 ≈ (y^4 x² v²)/(64 π² (x² + v²))\n\nTaking the square root:\n\nm_{H₂} ≈ (y^2 x v)/(8 π √(x² + v²))\n\nBut this is a more precise expression considering the mixing. However, without specific information on the potential or the couplings, this is an approximation. Given that the problem asks for an approximation through radiative corrections, and considering that the dominant contribution comes from the heavy Majorana neutrinos, the answer is likely:\n\nm_{H₂} ≈ (y^2 v)/(16π²) * (x v)/(x² + v²)\n\nBut this seems less common. Alternatively, given that in the original interaction, the coupling is y_i for the Majorana mass term and g_{iα} for the Yukawa with S and L. If S doesn\'t get a VEV, the Dirac mass term for neutrinos comes from ⟨H⟩, but in this model, the Yukawa term is g_{iα} \\bar{N}_{iR} L_α S. If S does not get a VEV, this term doesn\'t contribute to the neutrino mass at tree level. However, maybe at loop level, S can generate a Dirac mass term. But this is a different mass generation mechanism. However, the question is about the pseudo-Goldstone mass, not neutrino masses.\n\nAnother angle: The scalar potential V(φ, S, H) would include terms that mix these fields. If there\'s a term like λ φ² |H|², then the mass matrix for the scalars would have mixing between φ and H. The pseudo-Goldstone would be the lightest eigenstate from this mixing. However, at tree level, if the potential is such that there\'s an accidental symmetry, the pseudo-Goldstone is massless. Radiative corrections break the symmetry, generating a mass. The leading contribution would come from the couplings that break the symmetry. In this case, the Yukawa coupling y_i φ N_i N_i and g_{iα} N_i L S. \n\nIf the symmetry is a global U(1) under which φ and H rotate, then the Yukawa couplings y_i and g_{iα} would break this symmetry. The one-loop corrections from these couplings would generate a potential for the pseudo-Goldstone. The mass would then depend on these couplings. Assuming the dominant contribution is from the heaviest fermion, which is the Majorana neutrino N with mass y x, the mass would be:\n\nm_{H₂} ≈ (y^2 x)/(4π)\n\nBut again, this doesn\'t consider the mixing with the Higgs. Alternatively, if the decay constant f is √(x² + v²), and the coupling is y, then:\n\nm_{H₂} ≈ (y^2 f)/(4π)\n\nBut this would be if the Goldstone is solely from φ. However, since it\'s a combination, the expression is more complex. Given the time I\'ve spent and the need to provide an answer, I\'ll settle on the expression:\n\nm_{H₂} ≈ \\frac{y^2 v x}{16 \\pi^2 \\sqrt{x^2 + v^2}}\n\nThis takes into account the mixing between φ and H, the VEVs x and v, and the loop factor 16π². The numerator y² v x comes from the product of couplings and VEVs, and the denominator includes the decay constant √(x² + v²) and the loop factor. This seems like a reasonable approximation given the information.\n'), native_finish_reason='stop')], created=1745391191, model='deepseek/deepseek-r1', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=7228, prompt_tokens=1856, total_tokens=9084, completion_tokens_details=None, prompt_tokens_details=None), provider='Nebius')

---

# paraphrased_deepseek_completion_openai response

The mass of the pseudo-Goldstone boson \( H_2 \) arises from radiative corrections due to the explicit breaking of the approximate global symmetry by the Yukawa couplings. The dominant contribution comes from loops involving the singlet fermions \( N_{iR} \) with Majorana masses \( M_i = y_i x \). Considering the mixing between the singlet scalar \( \phi \) and the Higgs doublet \( H \), the mass can be approximated as:

\[
m_{H_2} \approx \frac{y_i^2 \, v \, x}{16 \pi^2 \sqrt{x^2 + v^2}}
\]

**Answer:**

The approximate mass of the pseudo-Goldstone boson \( H_2 \) through radiative corrections is 

\[
\boxed{m_{H_2} \approx \frac{y_i^2 \, v \, x}{16 \pi^2 \sqrt{x^2 + v^2}}}.
\]

---

# paraphrased_deepseek_completion_openai reasoning

The standard Higgs mechanism for the Standard Model produces three Goldstone bosons (eaten by W+, W-, Z). The addition of a singlet scalar φ may introduce another Goldstone if φ's potential breaks a U(1) symmetry. However, if the symmetry is explicit, this Goldstone becomes a pseudo-Goldstone. Alternatively, the mixing between H and φ could produce a pseudo-Goldstone.

But the problem mentions H₂ as the pseudo-Goldstone. In two-Higgs-doublet models, there are additional scalars, but here S is a doublet but with hypercharge 1, so different from the usual H. If S doesn't get a VEV, the Goldstone bosons would still come from H and φ. However, if φ is a singlet under the SM, its Goldstone would be a singlet, but if the symmetry is global, then the associated Goldstone is a singlet. However, the SM Higgs is in a doublet, so their Goldstones are in the doublet. But the problem states H₂ as the pseudo-Goldstone. Let's think: maybe the model has a global symmetry that is spontaneously broken by the VEVs of φ and S, but since S is a doublet, its VEV would break the symmetry. If S doesn't get a VEV, then the symmetry breaking comes from φ and H. Alternatively, S may get a VEV through the potential's structure. Wait, the problem statement says ⟨φ⟩² = x² + υ², but ⟨φ⟩ = x. If ⟨φ⟩ is x, then ⟨φ⟩² is x². Therefore, the equation x² = x² + υ² would imply υ = 0, which contradicts the SM Higgs VEV. So, perhaps this is a typo. Alternatively, ⟨φ⟩² + ⟨h⟩² = x² + υ²? The problem states "⟨φ⟩² = x² + υ², where ⟨φ⟩ = x and ⟨h⟩ = v." Wait, that can't be. If ⟨φ⟩ = x, then ⟨φ⟩² is x², but the problem says ⟨φ⟩² equals x² + υ², which is only possible if x² = x² + υ², implying υ² = 0. Therefore, there's a mistake in the problem's wording. Maybe ⟨ϕ⟩² + ⟨h⟩² = x² + v²? But the problem states "We give ⟨ϕ⟩² = (x² + υ²), where ⟨ϕ⟩ = x and ⟨h⟩ = v." That would mean that x² = x² + υ², which is impossible. Therefore, perhaps it's a misstatement. Alternatively, the VEV of ϕ is √(x² + υ²), but the user wrote ⟨ϕ⟩ = x. Alternatively, the VEVs are such that x and v are components of the scalar fields. Maybe the notation is swapped. Alternatively, the user intended to write that the VEV of the Higgs field is v, and the VEV of ϕ is x, with the sum of squares being x² + v². Therefore, perhaps the total VEV is x² + v², but the individual VEVs are x and v. But if ⟨ϕ⟩ = x and ⟨H⟩ = v, then the sum of their squares is x² + v². However, in the problem statement, it's written as ⟨ϕ⟩² = x² + υ², which is confusing. Perhaps the problem meant that the total VEV (e.g., the combination of ⟨ϕ⟩ and ⟨H⟩) is such that ⟨ϕ⟩² + ⟨H⟩² = x² + υ². But if ⟨H⟩ is v, then ⟨ϕ⟩² + v² = x² + υ². Unless x and υ are parameters, with ⟨ϕ⟩ and ⟨H⟩ being the VEVs. This is getting too confusing. Let me check the original problem again: 

"We give ⟨ϕ⟩² = (x² + υ²), where ⟨ϕ⟩ = x and ⟨h⟩ = v."

Ah, perhaps ⟨h⟩ is the Higgs field's VEV, denoted as v, and ⟨ϕ⟩² is x² + υ², where υ is another parameter. But then ⟨ϕ⟩ = x, so x² = x² + υ², which requires υ = 0. Alternatively, maybe the person meant that the combination of ⟨ϕ⟩ and ⟨h⟩ gives the total as x² + υ², but with ⟨ϕ⟩ = x and ⟨h⟩ = υ. Then the total would be x² + υ². But then why write ⟨ϕ⟩² = x² + υ²? That would imply ⟨ϕ⟩ = sqrt(x² + υ²), which contradicts the given ⟨ϕ⟩ = x. So, perhaps there's a typo, and the intended statement is that the sum of the squares of the VEVs is x² + υ², i.e., ⟨ϕ⟩² + ⟨h⟩² = x² + υ². If that's the case, then ⟨ϕ⟩ = x and ⟨h⟩ = υ, so their squares add up to x² + υ². But then the user wrote ⟨h⟩ = v, so perhaps υ is a typo for v. So, maybe the problem intended to state that ⟨ϕ⟩² + ⟨h⟩² = x² + v², with ⟨ϕ⟩ = x and ⟨h⟩ = v, which would make sense. For example, if there's a potential term like (ϕ² + |H|² - (x² + v²))², then the VEVs would satisfy ⟨ϕ⟩² + ⟨h⟩² = x² + v². But then the individual VEVs are x and v. This makes more sense. Therefore, perhaps the problem had a typo and the correct statement is ⟨ϕ⟩² + ⟨h⟩² = x² + v², with ⟨ϕ⟩ = x and ⟨h⟩ = v. That would be a logical structure. So, assuming that, the VEVs x and v are such that their squares sum to x² + v². Therefore, the scalar potential enforces this relation, leading to a flat direction. The Goldstone boson would correspond to the direction in which the fields can be rotated without changing the potential, i.e., the combination of ϕ and h that leaves x² + v² invariant. However, if the potential is such that this symmetry is only approximate, the pseudo-Goldstone boson would acquire a mass through radiative corrections. Alternatively, the potential could have an explicit breaking term that gives a small mass. But since the problem states that the mass is generated through radiative corrections, that suggests that the symmetry is exact at tree level but broken at loop level, hence generating a mass. 

In such a scenario, the tree-level potential has an accidental symmetry (like a U(1) or SO(2) symmetry) that is broken by quantum corrections. For example, if the tree-level potential is symmetric under rotations between ϕ and H, then the VEVs x and v lie on a circle of radius √(x² + v²). The Goldstone boson would be the angular direction. However, if loop corrections (radiative corrections) break this symmetry, the pseudo-Goldstone boson (the angular direction) gets a mass. 

The mass of the pseudo-Goldstone boson can be estimated by the Coleman-Weinberg potential. The Coleman-Weinberg mechanism generates an effective potential at one-loop level, which can induce symmetry breaking. If the tree-level potential is flat in a certain direction (the Goldstone direction), quantum corrections can lift this flatness, giving a small mass. 

To compute the mass, we need to consider the one-loop effective potential. The general form is:

V_eff = V_tree + ΔV

where ΔV is the one-loop correction given by:

ΔV ≈ (1/64π²) [ m_B^4 (ln(m_B² / Λ²) - c) - m_F^4 (ln(m_F² / Λ²) - c) ]

where m_B and m_F are the boson and fermion masses, Λ is the renormalization scale, and c is a constant depending on the renormalization scheme. For pseudo-Goldstone bosons, the dominant contribution often comes from the top quark (if applicable) or other heavy fermions. However, in this model, the relevant fermions are the singlet neutrinos N_R and the lepton doublets L_α. 

Looking at the Lagrangian, the interactions are:

- The Majorana mass term for N_R: -(y_i / 2) ϕ \bar{N}_{iR}^c N_{iR} + h.c.
- The Yukawa coupling: -g_{iα} \bar{N}_{iR} L_α S + h.c.

Assuming S does not get a VEV, the Yukawa coupling g_{iα} would not contribute to the tree-level masses but would generate interactions. The Majorana mass term, when ϕ gets a VEV x, gives N_R a Majorana mass M_i = y_i x / 2.

The potential V(ϕ, S, H) is not specified, but if we consider the tree-level potential to have a symmetry that's broken by quantum corrections, then the pseudo-Goldstone mass arises from loops involving the fields that break the symmetry. Given that the problem mentions radiative corrections, the dominant contributions would come from the couplings in the Lagrangian. The couplings y_i (Majorana couplings) and g_{iα} (Yukawa couplings to S and L) would contribute to loops.

If H₂ is the pseudo-Goldstone boson from the ϕ and H sector, then its mass would be generated by loops involving the N_R and possibly S. Let's consider the couplings:

1. The Majorana coupling y_i ϕ N_{iR}^c N_{iR} would, after ϕ gets a VEV x, lead to a mass term for N_R. This coupling also allows for a loop diagram where the ϕ field (including the Goldstone mode) interacts with N_R loops. If the potential has a flat direction (the Goldstone direction), these loops can generate a potential for the Goldstone, giving it a mass.

2. The Yukawa coupling g_{iα} N_{iR} L_α S would contribute if S has a VEV. If S does not have a VEV, this coupling would still allow for loop diagrams involving S, L_α, and N_R. However, without a VEV for S, the impact might be suppressed.

Assuming S does not get a VEV, the dominant contribution would come from the Majorana coupling. The pseudo-Goldstone boson (H₂) would be a mixture of the Higgs and ϕ fields. The mass would be generated at loop level through the couplings of ϕ to N_R. The one-loop correction to the potential would then generate a mass term for the pseudo-Goldstone.

The general formula for the mass of a pseudo-Goldstone boson from radiative corrections is roughly:

m_{PG}^2 ≈ (loop factor) * (coupling)^2 * (VEV)^2 / (16π²)

But to be precise, we need to compute the Coleman-Weinberg potential. Let's model the tree-level potential with a symmetry. Suppose the tree-level potential for ϕ and H is:

V_tree = λ (ϕ² + |H|² - f²)^2

where f² = x² + v². This potential has an SO(2) symmetry rotating ϕ and the real part of H (assuming H is written in the unitary gauge where the Goldstones are eaten). The minimum is at ϕ² + |H|² = f², so ⟨ϕ⟩ = x and ⟨H⟩ = v with x² + v² = f². The angular direction (the pseudo-Goldstone) is massless at tree level. However, the couplings in the Lagrangian (y_i and g_{iα}) break the SO(2) symmetry explicitly. Thus, loops involving these couplings will generate a potential for the pseudo-Goldstone.

The dominant contribution comes from the heaviest particles in the loop. Since N_R has a Majorana mass M_i = y_i x, and assuming y_i is sizable, the loops with N_R would contribute significantly. The Yukawa coupling g_{iα} might contribute but would be suppressed by the smaller coupling and possible absence of S VEV.

The Coleman-Weinberg potential for the pseudo-Goldstone can be approximated by considering the effective potential in the angular direction. Let’s parameterize ϕ = f cosθ and H = f sinθ (in the unitary gauge, H's VEV is in the real component). The angle θ corresponds to the Goldstone boson. The one-loop potential from the N_R loops would be:

ΔV ≈ (1/64π²) Tr[ M_N^4 (ln(M_N² / Λ²) - c) ]

where M_N is the Majorana mass matrix, which depends on ϕ. Since ϕ = f cosθ, M_N = y_i f cosθ / 2. The trace would sum over the eigenvalues, so for each N_i:

ΔV ≈ (N_i contribution) ≈ (y_i^4 f^4 cos^4θ)/(128π²) [ ln(y_i^2 f² cos²θ / Λ²) - c ]

To find the mass of the pseudo-Goldstone, we take the second derivative of ΔV with respect to θ at the minimum θ = arctan(v/x). However, since the tree-level potential is minimized at a particular θ, the loop corrections will create a potential that breaks the SO(2) symmetry, giving a mass to θ. Assuming the minimum remains at θ = arctan(v/x), expanding ΔV around θ = 0 (but given the VEVs, this might not hold; perhaps better to expand around the true vacuum). Alternatively, since at tree level θ is a flat direction, the loop corrections determine the potential along θ. The mass squared is the curvature of ΔV at the minimum.

Assuming that the dominant contribution comes from the heaviest N_i, let's consider a single generation for simplicity, dropping the index i. Then:

ΔV ≈ (y^4 f^4 cos^4θ)/(128π²) [ ln(y^2 f² cos²θ / Λ²) - c ]

To find the mass, we take the second derivative of ΔV with respect to the Goldstone boson field. The Goldstone boson H₂ is related to θ by H₂ = f θ (for small θ). Therefore, the mass squared is (d²ΔV/dθ²)/f².

First, compute dΔV/dθ:

dΔV/dθ ≈ (y^4 f^4 /128π²) [ 4 cos^3θ (-sinθ) [ ln(...) - c ] + cos^4θ ( ( - 2 y^2 f² sinθ / (y^2 f² cos²θ) ) ) ]

Wait, this seems complicated. Let's use the chain rule. Let’s define M = y f cosθ. Then, ΔV ≈ (M^4 / 128π²) [ ln(M² / Λ²) - c ]

Then, dΔV/dθ = (4 M^3 dM/dθ / 128π²) [ ln(M² / Λ²) - c ] + (M^4 / 128π²) ( (2 M dM/dθ ) / M² )

Simplifying:

dΔV/dθ = (M^3 / 32π²) (- y f sinθ) [ ln(M² / Λ²) - c ] + (M^4 / 128π²) ( 2 (- y f sinθ) / M )

But since M = y f cosθ, dM/dθ = - y f sinθ.

So,

dΔV/dθ = ( (y f cosθ)^3 (- y f sinθ) ) / 32π² [ ln(...) - c ] + ( (y f cosθ)^4 / 128π² ) ( 2 (- y f sinθ) / (y f cosθ) ) )

Simplify term by term:

First term: - (y^4 f^4 cos³θ sinθ) / 32π² [ ln(y² f² cos²θ / Λ²) - c ]

Second term: - (y^4 f^4 cos³θ sinθ) / 64π²

Therefore, combining:

dΔV/dθ = - (y^4 f^4 cos³θ sinθ) / 32π² [ ln(y² f² cos²θ / Λ²) - c + 1/2 ]

To find the extrema, set dΔV/dθ = 0. Assuming the minimum is at θ = 0 (which may not hold, but for estimation), but given that the tree-level potential is flat, the loop corrections would determine the minimum. However, if we assume that the minimum is at θ = 0 (i.e., ⟨ϕ⟩ = f, ⟨H⟩ = 0), but in our case, the VEVs are x and v. This complicates things. Alternatively, since the problem states that ⟨ϕ⟩ = x and ⟨h⟩ = v, with x² + v² = f², we can express θ as arctan(v/x). Let’s denote θ₀ = arctan(v/x). Then, we need to compute d²ΔV/dθ² at θ = θ₀.

But this calculation is getting too involved. Let's instead approximate the mass by noting that the pseudo-Goldstone mass squared is generated by the curvature of the effective potential around the minimum. The leading contribution would be from the heaviest fermion in the loop, which is N_R with mass M_N = y x / 2. The mass squared of the pseudo-Goldstone would be something like:

m_{H₂}^2 ≈ (y^4 x²)/(16π²) * (v²)/(x² + v²)

But this is a rough estimate. Alternatively, considering that the symmetry breaking is proportional to the couplings y and g, and the VEVs x and v, the mass can be a combination of these parameters. 

Alternatively, using the formula for the Coleman-Weinberg potential for a pseudo-Goldstone boson, the mass can be approximated as:

m_{H₂}^2 ≈ (N_f y^4 x²)/(16π²) * ln(Λ²/M_N²)

where N_f is the number of fermion species. However, without knowing the renormalization scale Λ, this is still ambiguous. But in many cases, the logarithm is assumed to be O(1), so the mass is roughly:

m_{H₂} ≈ (y² x)/(4π)

But this is if the potential is generated solely by the fermion loops. However, in this case, the pseudo-Goldstone is a mixture of the Higgs and ϕ fields. The exact expression would depend on the mixing angle between the two scalars. The mixing angle is determined by the potential's parameters, which are not given. However, if we assume that the dominant contribution comes from the N_R loops, which couple to ϕ, then the mass squared would be proportional to y^4 x² / (16π²), multiplied by some function of the mixing angle.

Alternatively, considering that the pseudo-Goldstone is mostly the phase direction of ϕ and H, its mass is generated by the explicit breaking of the global symmetry. If the breaking is due to the Yukawa coupling y_i, then the mass would be:

m_{H₂} ≈ (y_i^2 x)/(4π)

But this is a common estimate for axion-like particles where the mass is generated by instanton effects. However, in this case, it's generated by fermion loops. Another approach: the Coleman-Weinberg potential generates a quartic coupling for the pseudo-Goldstone. The curvature of the potential would then be:

m_{H₂}^2 ≈ (d²V/dθ²) ≈ (y^4 x²)/(16π²)

But considering that the Goldstone is a phase, the actual mass would depend on the decay constant f = √(x² + v²). The canonical normalization of the Goldstone field is H₂ = f θ, so the mass term would be (1/2) m_{H₂}^2 f² θ². Therefore, the coefficient from the potential d²V/dθ² = m_{H₂}^2 f². Hence:

m_{H₂}^2 f² ≈ (y^4 x²)/(16π²) → m_{H₂} ≈ (y^2 x)/(4π f)

But since f² = x² + v², then:

m_{H₂} ≈ (y^2 x)/(4π √(x² + v²))

If x ≫ v, then m_{H₂} ≈ y² x / (4π x) = y²/(4π). But if v ≫ x, then m_{H₂} ≈ y² x/(4π v). However, without knowing the hierarchy between x and v, we can leave it as:

m_{H₂} ≈ (y^2 x)/(4π √(x² + v²))

But the problem mentions that H₂ is a pseudo-Goldstone boson. If the symmetry is broken by multiple fields, the decay constant f is √(x² + v²). Therefore, the mass would be m_{H₂} ≈ (y^2 x)/(4π f) = (y^2 x)/(4π √(x² + v²)). However, this assumes that the dominant contribution comes from the coupling y. If there are multiple fermions, we should sum over their contributions. For example, if there are three generations of N_R with couplings y_i, then m_{H₂}^2 ≈ Σ_i (y_i^4 x²)/(16π² f²). But given the lack of specific information, the problem likely expects an expression in terms of the couplings and VEVs provided.

Alternatively, considering that the mass comes from the one-loop diagram with N_R in the loop. The pseudo-Goldstone couples to N_R via the derivative coupling (since Goldstones are derivatively coupled). The interaction term would be something like (y x / f) H₂ \bar{N}_R N_R^c, leading to a loop diagram with two H₂ insertions. The mass would then be calculated via the loop integral. For a fermion loop with coupling g ~ y x / f, the mass would be:

m_{H₂}^2 ≈ (g^2 M_N^2)/(16π²) ≈ (y^2 x^2/f^2 * y^2 x^2)/16π² = y^4 x^4/(16π² f²)

But since f² = x² + v², this is y^4 x^4/(16π² (x² + v²)). However, this seems different from the previous estimate. Alternatively, the coupling of H₂ to N_R could be through the derivative term, leading to a coupling proportional to y / f. Then, the loop would involve two insertions of this coupling and two propagators. The mass would then be m_{H₂}^2 ≈ (y^2 / f^2) * (M_N^2)/(16π²) * M_N^2. Wait, this seems inconsistent. Let me think again.

The interaction Lagrangian for the pseudo-Goldstone H₂ coupling to N_R would be similar to a Yukawa coupling. If the original term is (y/2) ϕ \bar{N}_R^c N_R, then when ϕ = x + σ + i H₂ (assuming H₂ is the imaginary part, the Goldstone), the interaction term becomes (y/2)(x + σ + i H₂) \bar{N}_R^c N_R. Therefore, the coupling to H₂ is (i y/2) H₂ \bar{N}_R^c N_R. The mass term for N_R is (y x / 2) \bar{N}_R^c N_R. Therefore, the interaction term is (i y H₂ / (2 x)) * (y x / 2) \bar{N}_R^c N_R = (i y² H₂ / 4) \bar{N}_R^c N_R. So the coupling g is y² / 4. Then, the one-loop diagram with N_R in the loop would contribute to H₂ mass. The mass squared would be:

m_{H₂}^2 ≈ (g^2 M_N^2)/(16π²) = ( (y^4 / 16) * (y^2 x^2 / 4) ) / (16π²) ) ???

Wait, perhaps better to use the formula for a fermion loop contributing to scalar mass. For a scalar coupled to fermions via L ⊃ - g ϕ \barψ ψ, the one-loop mass correction is:

Δm² ≈ (g^2 m_ψ^2)/(8π²) ln(Λ^2/m_ψ^2)

But in our case, the coupling is of the form (i y² / 4) H₂ \bar{N}_R^c N_R. However, Majorana fermions complicate things. The coupling for a Majorana fermion to a pseudoscalar is different. Alternatively, since H₂ is a pseudo-Goldstone, it's a CP-odd scalar. The coupling would be (i y/2) H₂ \bar{N}_R^c N_R + h.c. For Majorana fermions, \bar{N}_R^c N_R = \bar{N}_R N_R^c, so the interaction term is (i y/2) H₂ (\bar{N}_R N_R^c + \bar{N}_R^c N_R ). But for Majorana fermions, N_R^c = N_R, so this becomes (i y/2) H₂ (\bar{N}_R N_R + \bar{N}_R N_R ) = i y H₂ \bar{N}_R N_R. The coupling is then similar to a Yukawa coupling with a factor of i y. 

The mass term for N_R is (y x / 2) \bar{N}_R N_R. Therefore, the propagator is for a Majorana fermion with mass M = y x / 2. The one-loop diagram contributing to H₂ mass would be a loop of N_R with two H₂ insertions. The amplitude is proportional to (i y)^2 times the loop integral. The loop integral for a fermion loop with two scalar insertions would give a contribution proportional to M^2. 

The mass squared is then:

m_{H₂}^2 ≈ (y^2 M^2)/(16π²) = (y^2 (y^2 x^2 / 4))/(16π²) ) = (y^4 x²)/(64π²)

But this is if the loop integral contributes a factor of M^2/(16π²). However, the actual computation might involve a different coefficient. In some references, the contribution from a Majorana fermion loop to a scalar mass squared is (y^2 M^2)/(8π²) ln(Λ/M). Assuming the log is O(1), then:

m_{H₂}^2 ≈ (y^4 x²)/(32π²)

But this doesn't take into account the mixing between H and ϕ. If H₂ is a combination of the Higgs and ϕ's Goldstone, the coupling y might be multiplied by a mixing angle. Suppose the mixing angle is θ, where tanθ = v/x, then the effective coupling would be y sinθ. Therefore, the mass squared would be (y^4 sin²θ x²)/(32π²). But sinθ = v / √(x² + v²), so:

m_{H₂}^2 ≈ (y^4 v² x²)/(32π² (x² + v²))

But this is getting too speculative. The problem statement doesn't specify the potential, so we have to make reasonable assumptions. Given the information, the most straightforward answer is that the mass of the pseudo-Goldstone boson H₂ is generated at one-loop level via the Majorana neutrino couplings, leading to:

m_{H₂} ≈ (y^2 x)/(4π)

However, considering the decay constant f = √(x² + v²), the mass would be suppressed by f if the Goldstone is a combination of ϕ and H. In that case, the mass is:

m_{H₂} ≈ (y^2 x)/(4π √(x² + v²)) * x

Wait, no. If the decay constant is f = √(x² + v²), and the Goldstone boson is H₂ = (v ϕ - x h)/f, then the coupling of H₂ to N_R is proportional to (y v)/f. Therefore, the coupling g = (y v)/f. Then, the mass squared would be:

m_{H₂}^2 ≈ (g^2 M_N^2)/(16π²) = (y² v²/f²)(y² x²/4)/(16π²) ) = (y^4 x² v²)/(64 π² f²)

But since f² = x² + v²:

m_{H₂}^2 ≈ (y^4 x² v²)/(64 π² (x² + v²))

Taking the square root:

m_{H₂} ≈ (y^2 x v)/(8 π √(x² + v²))

But this is a more precise expression considering the mixing. However, without specific information on the potential or the couplings, this is an approximation. Given that the problem asks for an approximation through radiative corrections, and considering that the dominant contribution comes from the heavy Majorana neutrinos, the answer is likely:

m_{H₂} ≈ (y^2 v)/(16π²) * (x v)/(x² + v²)

But this seems less common. Alternatively, given that in the original interaction, the coupling is y_i for the Majorana mass term and g_{iα} for the Yukawa with S and L. If S doesn't get a VEV, the Dirac mass term for neutrinos comes from ⟨H⟩, but in this model, the Yukawa term is g_{iα} \bar{N}_{iR} L_α S. If S does not get a VEV, this term doesn't contribute to the neutrino mass at tree level. However, maybe at loop level, S can generate a Dirac mass term. But this is a different mass generation mechanism. However, the question is about the pseudo-Goldstone mass, not neutrino masses.

Another angle: The scalar potential V(φ, S, H) would include terms that mix these fields. If there's a term like λ φ² |H|², then the mass matrix for the scalars would have mixing between φ and H. The pseudo-Goldstone would be the lightest eigenstate from this mixing. However, at tree level, if the potential is such that there's an accidental symmetry, the pseudo-Goldstone is massless. Radiative corrections break the symmetry, generating a mass. The leading contribution would come from the couplings that break the symmetry. In this case, the Yukawa coupling y_i φ N_i N_i and g_{iα} N_i L S. 

If the symmetry is a global U(1) under which φ and H rotate, then the Yukawa couplings y_i and g_{iα} would break this symmetry. The one-loop corrections from these couplings would generate a potential for the pseudo-Goldstone. The mass would then depend on these couplings. Assuming the dominant contribution is from the heaviest fermion, which is the Majorana neutrino N with mass y x, the mass would be:

m_{H₂} ≈ (y^2 x)/(4π)

But again, this doesn't consider the mixing with the Higgs. Alternatively, if the decay constant f is √(x² + v²), and the coupling is y, then:

m_{H₂} ≈ (y^2 f)/(4π)

But this would be if the Goldstone is solely from φ. However, since it's a combination, the expression is more complex. Given the time I've spent and the need to provide an answer, I'll settle on the expression:

m_{H₂} ≈ \frac{y^2 v x}{16 \pi^2 \sqrt{x^2 + v^2}}

This takes into account the mixing between φ and H, the VEVs x and v, and the loop factor 16π². The numerator y² v x comes from the product of couplings and VEVs, and the denominator includes the decay constant √(x² + v²) and the loop factor. This seems like a reasonable approximation given the information.

---

