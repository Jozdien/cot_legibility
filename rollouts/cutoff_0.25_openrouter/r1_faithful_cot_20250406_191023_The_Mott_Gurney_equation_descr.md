# Original Question

The Mott-Gurney equation describes the dark current (J) versus voltage (V) behavior of a semiconductor device in the space-charge-limited current (SCLC) regime. The equation can be expressed as
$ J = \frac{9}{8} \epsilon \mu \frac{V^2}{L^3}$
where $\epsilon$ is the dielectric constant, $\mu$ is the charge carrier mobility, and L is the length of the device. Which of the following statements is true about the validity of this equation?


---

# DeepSeek response (via openrouter)

The Mott-Gurney equation, \( J = \frac{9}{8} \epsilon \mu \frac{V^2}{L^3} \), is valid under specific conditions in the space-charge-limited current (SCLC) regime. Key assumptions for its validity include:

1. **Trap-Free Material**: The semiconductor must lack charge-trapping defects. Traps would immobilize carriers, reducing current and invalidating the equation, as it assumes all injected charges contribute to conduction.

2. **Ohmic Contacts**: The electrodes must inject charges freely (ohmic behavior). Blocking contacts would limit current via injection barriers, shifting the regime from SCLC to injection-limited.

3. **Constant Mobility**: The charge carrier mobility (\(\mu\)) must be independent of electric field. Field-dependent mobility (common in disordered materials) would alter the \(J \propto V^2\) dependence.

4. **Unipolar Transport**: Only one type of carrier (electrons or holes) dominates. Ambipolar transport (both carriers) or significant recombination invalidates the model.

5. **Negligible Diffusion Current**: The derivation assumes drift dominates over diffusion, valid at high voltages where electric fields drive transport.

**True Statement**: The equation is valid in trap-free semiconductors with ohmic contacts, constant mobility, and unipolar dominance, where space charge—not injection or traps—limits current.

---

# DeepSeek reasoning (via openrouter)

Okay, so I need to figure out which statement is true about the validity of the Mott-Gurney equation for the space-charge-limited current (SCLC) regime. Hmm, I remember that the Mott-Gurney equation relates the current density J to the voltage V squared, right? The equation given is J = (9/8) * ε * μ * V² / L³. Let me think about when this equation is supposed to hold true. 

First, I think SCLC occurs when the current is limited by the space charge effect rather than the injection of charges. That is, when the electrodes can inject enough charges that the current isn't limited by thermionic emission or something else. So the SCLC regime is when the injected charge density is so high that it creates a significant electric field opposing the injection. Therefore, the current becomes space-charge limited.

Now, the Mott-Gurney equation... I believe it assumes that the material is trap-free. Like, if there are traps (defects that can capture charge carriers), then the current would be lower because some charges get trapped and don't contribute to conduction. So maybe if the material has a lot of traps, the Mott-Gurney equation isn't valid. That could be one condition. 

Also, I think there's a condition on the mobility. The equation includes μ, which is the mobility. But I vaguely recall that Mott-Gurney assumes that the mobility is constant, not dependent on the electric field. However, in reality, especially in disordered materials, the mobility can be field-dependent. So if the mobility varies with the electric field, then the equation might not hold. But is that part of the assumptions here?

Wait, the equation is derived under the assumption of constant mobility. Because if the mobility changes with the electric field (which would be with voltage), then integrating the Poisson equation and the current equation might give a different dependence. Mott-Gurney probably requires that charge carriers have a mobility that isn't affected by the electric field, so ohmic-like conduction with μ being a constant.

Another thing: is the dielectric constant ε here the static dielectric constant or something else? I think in the derivation of SCLC, they use the permittivity of the material. Probably, the equation is valid when the material's permittivity is isotropic and homogeneous. If there are interfaces or varying dielectric constants, this might complicate things, but that's maybe beyond basic assumptions.

Oh, another important factor: the presence of ohmic contacts. For SCLC to hold, the contacts must be ohmic, meaning they can supply as much charge as needed. If the contacts are not ohmic (like blocking contacts), then the current might be limited by injection rather than space charge. So, one of the validity conditions for the Mott-Gurney equation is that contacts are ohmic.

Also, the current is in the regime where space charge dominates. So prior to reaching SCLC, there's a transition from ohmic current (where J is proportional to V) to SCLC (where J is proportional to V²). Hence, the Mott-Gurney equation applies in the SCLC regime, after crossing over from the ohmic regime. Therefore, if the voltage is low, you might be in the ohmic region, but at higher voltages, you enter SCLC. So the equation is only valid when the voltage is high enough that the current is space-charge limited.

Other possible factors: the device is a single-carrier device, i.e., only one type of charge carrier (either holes or electrons) is contributing significantly to the current. If there are both carriers (like in ambipolar devices), then the equation would not hold. I think Mott-Gurney is derived for unipolar SCLC. So only holes or electrons are present in significant numbers, and recombination isn't a major factor here.

Additionally, diffusion current is neglected in the SCLC derivation. The standard Mott-Gurney equation comes from solving the Poisson equation and the current equation (which is drift only, J = qμnE, where E is electric field) and neglecting diffusion. If diffusion is non-negligible compared to drift, the equation might not be valid. But at high voltages, drift dominates, so diffusion can be neglected.

Putting this all together, the correct statements about the validity must relate to:

1. Ohmic contacts (so that injection is not limiting)

2. Trap-free material (no traps to capture carriers, otherwise, the current would follow Child's law or another form with trap parameters)

3. Constant mobility (meaning mobility is independent of electric field)

4. Unipolar current (only one type of carrier)

5. Steady-state conditions? Not sure, but maybe that's another assumption.

So when looking at possible answer choices (even though they're not listed here), I need to see which one matches these conditions. For example, an answer might say "The equation is valid only if the contacts can inject sufficient charge carriers," which would relate to ohmic contacts. Or "The equation assumes the absence of carrier traps," which would be the trap-free condition. If an option mentions these, then it's true.

Since the problem is a multiple-choice question with options not shown, and the user is asking which statement is true, my job is to recall common options and their correctness. But given that SCLC requires trap-free, ohmic contacts, unipolar transport, constant mobility, thus blocks of these would be validity conditions. Therefore, the true statement is likely among these. For example, a common validity condition is that the semiconductor is trap-free and has ohmic contacts. Alternatively, another valid statement is that it holds when the current is not limited by charge injection but by space charge effects, which is the SCLC regime as opposed to injection-limited.

Thus, the correct answer would be a statement that aligns with these conditions. Like, "The equation is valid in trap-free materials with ohmic contacts" or "Valid when the mobility is constant and space charge effects dominate."

---

# Cut off deepseek reasoning

Okay, so I need to figure out which statement is true about the validity of the Mott-Gurney equation for the space-charge-limited current (SCLC) regime. Hmm, I remember that the Mott-Gurney equation relates the current density J to the voltage V squared, right? The equation given is J = (9/8) * ε * μ * V² / L³. Let me think about when this equation is supposed to hold true. 

First, I think SCLC occurs when the current is limited by the space charge effect rather than the injection of charges. That is, when the electrodes can inject enough charges that the current isn't limited by thermionic emission or something else. So the SCLC regime is when the injected charge density is so high that it creates a significant electric field opposing the injection. Therefore, the current becomes space-charge limited.

Now, the Mott-Gurney equation... I believe it assumes that the material is trap-free. Like, if there are traps (defects that can capture charge carriers), then the current would be lower because some charges get trapped and don't contribute to conduction. So maybe if the material has a lot of traps, the Mott-Gurney equation isn't valid. That could be one condition. 

Also, I think there's a condition on the mobility. The equation includes μ, which is the mobility. But I vaguely recall that Mott-Gurney assumes that the mobility is constant, not dependent on the electric field. However, in reality, especially in disordered materials, the mobility can be field-dependent. So i

---

# Anthropic completion

Alright, let me consider the validity of the Mott-Gurney equation for the space-charge-limited current (SCLC) regime. If I recall correctly, the Mott-Gurney equation expresses the relationship between the current density J and the voltage V squared, given by J = (9/8) * ε * μ * V² / L³. Now, it's important to understand the conditions under which this equation holds true.

To begin with, the SCLC regime occurs when the current is restricted by the space charge effect rather than the injection of charges from the electrodes. In other words, the electrodes are capable of injecting a sufficient amount of charges, and the current is not constrained by factors such as thermionic emission. In this scenario, the injected charge density becomes so substantial that it generates a significant electric field that counteracts the injection process, resulting in the current becoming space-charge limited.

However, the validity of the Mott-Gurney equation relies on certain assumptions. One key assumption is that the material is free of traps, meaning there are no defects that can capture and immobilize charge carriers. If the material contains a significant number of traps, the current would be lower than predicted by the Mott-Gurney equation because some charges would be trapped and unable to contribute to conduction. Consequently, the presence of traps could render the Mott-Gurney equation invalid.

Furthermore, the Mott-Gurney equation assumes that the mobility, denoted as μ, is constant and independent of the electric field. However, in real-world scenarios, particularly in disordered materials, the mobility can exhibit a dependence on the electric field. If the mobility varies with the electric field, the Mott-Gurney equation may not accurately describe the current-voltage relationship.

---

# OpenAI completion

I need to determine which statement is correct regarding the validity of the Mott-Gurney equation for the space-charge-limited current (SCLC) regime. I remember that the Mott-Gurney equation connects the current density J to the square of the voltage V, right? The equation is J = (9/8) * ε * μ * V² / L³. Let's consider when this equation is applicable.

First, I think SCLC occurs when the current is limited by the effect of space charge rather than by the injection of charges. This means that the electrodes inject enough charges that the current isn't constrained by thermionic emission or any other factor. Thus, the SCLC regime is when the injected charge density is so high that it generates a significant electric field opposing further injection, leading to space-charge-limited current.

Now, regarding the Mott-Gurney equation... I believe it assumes the material is free of traps. If there are traps (defects that can capture charge carriers), the current would be reduced because some charges get trapped and don't aid in conduction. Therefore, if the material has many traps, the Mott-Gurney equation might not be applicable. This could be one condition.

Additionally, I think there's a consideration regarding mobility. The equation includes μ, which represents mobility. I vaguely remember that the Mott-Gurney equation assumes mobility is constant and not reliant on the electric field. However, in reality, particularly in disordered materials, the mobility may be dependent on the field.

---

# cutoff_deepseek_completion response

The Mott-Gurney equation for space-charge-limited current (SCLC) is valid under specific conditions. The key assumptions for its applicability are:

1. **Trap-Free Material**: The semiconductor must lack charge carrier traps (defects that immobilize carriers). Traps would reduce the effective mobility and invalidate the equation.
2. **Ohmic Contacts**: The electrodes must supply an unlimited charge density, ensuring current is limited by space charge rather than injection barriers.
3. **Constant Mobility**: The charge carrier mobility (μ) is assumed independent of the electric field. Field-dependent mobility (e.g., in disordered materials) would violate this assumption.
4. **Drift-Dominated Transport**: Diffusion currents are negligible compared to drift currents, which holds in high-field SCLC regimes.
5. **Steady-State Conditions**: The equation applies to steady-state behavior, not transient dynamics.

**True Statement**: The Mott-Gurney equation is valid only for trap-free semiconductors with ohmic contacts and constant charge carrier mobility. If traps are present, contacts are non-ohmic, or mobility varies with field, the equation does not hold.

---

# cutoff_deepseek_completion reasoning

F the mobility varies with the electric field, then the equation might not hold. 

Another thing is the presence of ohmic contacts. For SCLC, you need the contacts to be ohmic, meaning they can supply as much charge as needed. If the contacts are not ohmic, like if they're blocking contacts, then the current would be limited by the contact rather than the space charge, so the equation wouldn't apply. 

Also, the equation is derived under the assumption of steady-state conditions, right? So transient effects or time-dependent voltages might not fit into this model. But the question is about the general validity, not time-dependent cases. 

Temperature might also play a role. If the temperature is such that there's significant thermal generation of carriers, then maybe the dark current (which is the current in the absence of light) would have contributions from both injected charges and thermally generated charges. But the Mott-Gurney equation probably assumes that the injected carriers dominate, so if thermal carriers are significant, the equation might not be valid. 

Wait, the question mentions "dark current," so that's the current without illumination. So in the dark, the main sources of carriers would be injection from electrodes and thermal generation. If the device is in the SCLC regime, then injection is sufficient, but if thermal generation is non-negligible, maybe that affects the validity. But I think the Mott-Gurney equation specifically considers only injected carriers, so if thermal carriers are present, the equation might not hold. 

Another point: the Mott-Gurney equation is derived for a planar geometry with two electrodes separated by a distance L, and it assumes that the electric field is uniform? Wait, no, actually, in the Child-Langmuir law for vacuum diodes, the electric field isn't uniform, and the same applies here. The SCLC in solids leads to a non-uniform electric field. But the derivation of Mott-Gurney would take that into account. 

Wait, the original Child's law in vacuum is J = (4/9)ε₀√(2e/m) V^(3/2)/d², but in the Mott-Gurney case, for solids with mobility μ instead of ballistic transport, it's J proportional to V²/L³. So the derivation would involve solving Poisson's equation with the current density equation. 

So the key assumptions would be: 

1. Trap-free material (no shallow or deep traps that can capture charge carriers).
2. Ohmic contacts that can supply unlimited charge carriers.
3. Constant mobility (i.e., mobility is independent of the electric field).
4. Steady-state conditions.
5. Negligible diffusion current compared to drift current. Because SCLC is a drift-dominated regime.
6. Non-degenerate carrier concentration (so Boltzmann statistics apply, but maybe in SCLC, the concentration is high enough that this isn't valid? Hmm, not sure. Maybe the equation assumes that the carrier density is high but non-degenerate.)

So, considering all these assumptions, the validity of the Mott-Gurney equation would require these conditions to be met. Therefore, any statement that points out that the equation is valid only under these conditions would be true. 

Looking at the possible options (even though they aren't listed here), but since the user hasn't provided the options, I need to think about what the common pitfalls or correct statements are. 

For example, a common true statement would be: "The Mott-Gurney equation is valid only in the absence of traps and for ohmic contacts." Another could be: "The equation assumes that the mobility is independent of the electric field." Or "The equation is applicable when the current is limited by space charge rather than contact injection or traps."

Alternatively, a statement that is false might say the equation applies when mobility is field-dependent, or when traps are present, or when contacts are blocking.

Since the user hasn't provided the options, but given that I need to state which is true, perhaps the key points are traps, ohmic contacts, and constant mobility. So the correct answer would be a statement that says the equation is valid when the semiconductor is trap-free, has ohmic contacts, and mobility is constant. 

Alternatively, if the options are like:

A) Valid only for materials with ohmic contacts

B) Valid when traps are present

C) Assumes field-dependent mobility

D) Applies to both electrons and holes contributing equally

Then the correct answer would be A. But since I don't have the options, I need to recall common knowledge.

Wait, the standard SCLC Mott-Gurney law is derived under the assumptions of trap-free material, ohmic contacts, and constant mobility. So any of these conditions not being met would invalidate the equation. Therefore, the true statements would be those that align with these assumptions. So if the question's options include something like "The equation is valid only for trap-free materials with ohmic contacts," that would be correct. Alternatively, "The equation assumes that the charge carrier mobility is constant and independent of electric field," that's another correct statement.

Since the user hasn't provided the options, but given the nature of the question, the answer is likely related to the necessity of trap-free material and ohmic contacts. So the correct answer is that the Mott-Gurney equation is valid when the semiconductor is trap-free and has ohmic contacts, and mobility is constant. But since the user is asking which statement is true, and given that in the absence of the options, I need to recall that the primary conditions are trap-free and ohmic contacts. So the answer is probably that the equation is valid when there are no traps and contacts are ohmic. 

Alternatively, another possible point is that the Mott-Gurney equation neglects diffusion current. In the derivation of SCLC, you typically use the drift-only current, ignoring diffusion. So if the diffusion current is significant, the equation isn't valid. But in the SCLC regime, the electric field is high enough that drift dominates, so diffusion is negligible. 

But again, without the options, I need to focus on the most critical assumptions. The key ones are trap-free, ohmic contacts, and constant mobility. So the correct statement would be one that mentions these. Since the user hasn't given the options, but given the standard knowledge, the answer is that the Mott-Gurney equation is valid under the assumptions of trap-free material, ohmic contacts, and constant mobility. Therefore, any of these conditions not being met would invalidate the equation. So the true statement would be about these conditions.

---

# paraphrased_deepseek_completion_anthropic response

The Mott-Gurney equation, \( J = \frac{9}{8} \epsilon \mu \frac{V^2}{L^3} \), is valid under specific conditions in the space-charge-limited current (SCLC) regime. The key requirements for its validity include:

1. **Trap-Free Material**: The semiconductor must be free of charge-trapping defects. Traps would immobilize carriers, reducing the current below the predicted value.  
2. **Ohmic Contacts**: The electrodes must inject charge carriers efficiently without limiting the current (i.e., Ohmic boundary conditions).  
3. **Constant Mobility**: The charge carrier mobility (\(\mu\)) must be independent of the electric field. The equation breaks down in materials where \(\mu\) varies with field strength (e.g., disordered systems).  
4. **Steady-State Conditions**: The equation assumes steady-state operation, not transient or time-dependent voltages.  
5. **Planar Geometry**: Derived for one-dimensional planar devices. Non-planar geometries (e.g., cylindrical) may alter the space-charge distribution.  

**Correct Statement**:  
"The Mott-Gurney equation applies to trap-free semiconductors with Ohmic contacts, constant carrier mobility, and planar geometry under steady-state conditions."

---

# paraphrased_deepseek_completion_anthropic reasoning

In such cases, different models, perhaps involving field-dependent mobility, would be more appropriate.

Another critical assumption is that the semiconductor is operating under steady-state conditions. If the device is subject to transient effects or fast-varying voltages, the SCLC behavior might deviate from the Mott-Gurney equation's predictions, which are derived under steady-state conditions.

Additionally, the equation is derived for a planar, one-dimensional geometry. If the device has a significantly different geometry, such as being cylindrical or having varying cross-sectional areas, the space-charge distribution could differ, leading to modifications in the current-voltage relationship. Therefore, the Mott-Gurney equation is most accurate when applied to devices with simple planar electrodes separated by a uniform semiconductor layer of length L.

Temperature effects might also play a role. If the mobility μ is temperature-dependent, variations in temperature could affect the validity of the equation. However, strictly within the model's assumptions, the equation doesn't account for temperature dependencies beyond the inherent properties captured by μ.

Considering these factors, the correct statement about the validity of the Mott-Gurney equation should indicate that it's applicable only under specific conditions. The equation is valid when the semiconductor is trap-free, the mobility is constant (not field-dependent), steady-state conditions prevail, and the device has a planar geometry with Ohmic contacts capable of supplying an unlimited amount of charge carriers. Any deviation from these conditions would likely invalidate the simple J ∝ V² relationship predicted by the Mott-Gurney law.

---

# paraphrased_deepseek_completion_openai response

The Mott-Gurney equation is valid under specific conditions related to the semiconductor material and operating regime. The correct statement about its validity is:

**The equation is valid only when the semiconductor is trap-free (no charge carrier traps) and the charge carrier mobility (μ) is constant (independent of electric field).**

### Key Assumptions of the Mott-Gurney Equation:
1. **Trap-Free Material**: The absence of defects or traps that could capture charge carriers is critical. Traps reduce the effective carrier density and alter the current-voltage relationship, leading to deviations from the \( J \propto V^2 \) behavior.
2. **Constant Mobility**: The equation assumes carrier mobility (μ) does not depend on the electric field. In materials where mobility varies with field (e.g., disordered systems with Poole-Frenkel behavior), the equation does not hold.
3. **Ohmic Contacts**: The contacts must inject sufficient charge carriers to maintain the space-charge-limited regime, ensuring current is not limited by injection barriers.
4. **Unipolar Transport**: Only one type of charge carrier (electrons or holes) contributes significantly to the current.
5. **Negligible Diffusion Current**: The electric field must dominate over diffusion effects, a condition typically met at high voltages.

If any of these assumptions are violated (e.g., traps are present, mobility is field-dependent, or contacts are non-ohmic), the Mott-Gurney equation no longer accurately describes the \( J \)-\( V \) behavior.

---

# paraphrased_deepseek_completion_openai reasoning

For instance, in materials with Poole-Frenkel behavior, mobility increases with the electric field. If μ varies with E (the electric field), then the equation might not hold, right?

Also, the equation has a V squared dependence. So, in the SCLC regime, the current should scale as V squared. But if there's a different scaling, like V cubed or something else, that would indicate a different regime. For example, in trap-limited SCLC, the current might scale as V to a higher power. So the Mott-Gurney equation is only valid when traps are absent and mobility is constant.

Another point: the dielectric constant ε is part of the equation. If the material's permittivity isn't uniform or is anisotropic, maybe the equation would need modification. But the question is about standard validity conditions. The standard case would assume a uniform dielectric constant.

Also, the length L is in the denominator cubed. So the equation is valid for a specific geometry, probably a one-dimensional planar structure. If the device has a different geometry, like a cylinder or sphere, the dependence on L would change, but the question is probably about a standard case.

Wait, let's recap the key assumptions behind the Mott-Gurney equation. From what I recall:

1. The material is trap-free (no shallow or deep traps that can capture charge carriers).
2. The current is unipolar (only one type of charge carrier, either electrons or holes, contributes to the current).
3. The mobility μ is constant (independent of the electric field and charge density).
4. The electric field is high enough that diffusion current is negligible compared to drift current.
5. The contacts are ohmic and can supply unlimited charge carriers (space charge limited condition).

So, the equation doesn't apply if there are traps, if the mobility isn't constant, or if the contacts are not ohmic (i.e., they can't inject sufficient charge).

Looking at possible answer options (even though I don't have them here), the true statement would relate to one of these assumptions. For example, a statement saying "The equation is valid only when the material is trap-free" would be true. Alternatively, "The equation holds when carrier mobility is independent of electric field" would also be valid.

Another possible consideration is the presence of both electrons and holes. The Mott-Gurney equation is for unipolar transport. If there's significant bipolar conduction (both carriers contributing), the equation might not apply. But usually, SCLC can also be considered in bipolar cases, but the equation might differ. Wait, but Mott-Gurney specifically is for unipolar.

But since the question gives the equation as J = (9/8) ε μ V² / L³, this form is indeed for trap-free, unipolar SCLC with constant mobility.

So any statement that points out that the equation assumes trap-free material, constant mobility, ohmic contacts, etc., would be correct. For example, if one of the options is "The equation is valid only in the absence of charge traps," that's true. Alternatively, "The equation assumes that the carrier mobility is independent of the electric field," which is also a true statement.

Since the original question asks which statement is true about the validity, and given that I don't have the options, but based on standard knowledge, the Mott-Gurney equation's key validity conditions are trap-free material and constant mobility. So the correct answer would relate to one of these two. If the choices include both, but in the typical multiple-choice setup, only one is correct. Probably, the key point is about traps. Let me check textbooks.

In Sze's "Physics of Semiconductor Devices," the SCLC theory is discussed. The Child-Langmuir law is for vacuum diodes, while Mott-Gurney adapts it for solids considering mobility. The key assumptions include: (1) ohmic contacts, (2) trap-free insulator, (3) non-zero mobility, (4) one-carrier injection, (5) electric field high enough that diffusion is negligible. Also, they mention that the presence of traps leads to different J-V dependencies (like traps-filled limit, etc.), so the Mott-Gurney equation is invalid when traps are present.

Therefore, the correct statement should be that the equation is valid only when the semiconductor is trap-free. Alternatively, another true statement could be that the mobility must be field-independent. Depending on the options given. Since the user hasn't provided the options, but given that I need to answer based on general knowledge, the answer is that the Mott-Gurney equation is valid when there are no traps and mobility is constant. However, since the user is expecting me to pick from possible options (which they haven't listed here), but since in the original instruction, the user might have forgotten to include the options. Wait, no, the user actually wrote the question as presented, so maybe they intended for this to be a free-response question where I have to deduce based on the given equation.

Wait, the user says "Which of the following statements is true about the validity of this equation?" but since the options are not here, perhaps the user is presenting a made-up question and expects me to think through the possible answers. Wait, no. Wait, the user has presented the question as written, but in the original context (if this is a transcribed image or something), maybe the options were not included. Wait, but the user's instruction is to answer based on the given information. Hmm, perhaps this is a mistake. Alternatively, maybe the user is from a non-English background and didn't paste the options. Alternatively, perhaps this is an example where the user is testing the system's knowledge. Given that, I need to state the correct validity conditions.

Given that, the correct answer is that the Mott-Gurney equation is valid under the conditions of trap-free material and constant mobility. So the true statement would be either related to absence of traps or constant mobility. Since both are key assumptions.

Therefore, if the options (which are not here) include such statements, those are correct. But in the absence of options, the answer is that the equation is valid in a trap-free semiconductor with constant mobility. So the true statement is that the Mott-Gurney equation applies when the semiconductor is trap-free and carrier mobility is independent of electric field. But since the user might have given options, but they are missing here, perhaps the original question in their source had options like:

A) It applies when there are traps present.

B) It requires the material to have zero mobility.

C) It is valid only in the absence of charge carrier traps.

D) It holds when the current is limited by thermionic emission.

In that case, C would be correct. Therefore, if I have to pick, option C is correct. But since I don't have the options, but given the standard knowledge, the answer is that the equation is valid only in trap-free materials and when mobility is constant. So the user should check for such options. But in the original question, since the user hasn't provided the options, but according to the structure of the problem, the answer must be presented here. So the conclusion is that the correct answer is that the Mott-Gurney equation is valid when the semiconductor is trap-free. Hence, the true statement is about the absence of traps.

---

