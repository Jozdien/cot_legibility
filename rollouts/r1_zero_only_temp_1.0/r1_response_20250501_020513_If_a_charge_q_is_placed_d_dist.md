# Original Question

If a charge q is placed d distance away from the center of a grounded conducting sphere of radius R. Calculate the net potential energy of this system.

---

# DeepSeek response (via openrouter)

\boxed{-\frac{q^2 R}{4 \pi \epsilon_0 (d^2 - R^2)}}

---

# DeepSeek reasoning (via openrouter)

To solve for the net potential energy of the system where a point charge $q$ is placed at a distance $d$ (where $d > R$) away from the center of a grounded conducting sphere of radius $R$, we need to find the total charge induced on the sphere and use an appropriate formula for potential energy.

The well-studied problem involves placing a point charge $q$ outside a grounded conducting sphere of radius $R$ such that the charge is located at a distance $d$ from the center of the sphere where $d > R$. The goal is to find the potential energy stored in the "system," which typically includes the charge $q$ and whatever charge distribution arises on the sphere due to the "method of images."

### Step 1: Finding the image charge(s)
Using the method of images, a charge $q$ located outside a grounded conducting sphere induces an image charge $q'$ inside the sphere such that the potential on the surface of the sphere is zero (since it's grounded). The image charge should be placed on the line connecting the charge $q$ and the center of the sphere such that:
$$
q' = -\frac{Rq}{d}.
$$
The image charge $q'$ is placed at a distance $d'$ from the center of the sphere such that:
$$
d' = \frac{R^2}{d}.
$$
This makes the imaginary charge $q'$ appear inside the sphere at a distance $d'$ from the center such that $d' < R$ (since $d > R$, it follows that $d' < R$).

### Step 2: Total potential energy calculation
The potential energy of a system of charges can typically be computed as follows:
$$
U = \frac{1}{2} \sum_{i} q_i V_i,
$$
where $V_i$ is the potential due to all charges except charge $q_i$. For a system of two point charges $q$ (actual charge) and $q'$ (image charge), the potential energy can alternatively be defined as:
$$
U = \frac{1}{2} \left( q V_q + q' V_{q'} \right).
$$
However, the question here is a bit more ambiguous because usually we need to find the self-energy of charge $q$ in the presence of the sphere. Another well-known expression for the potential energy of a system of two charges $q_1$ and $q_2$ separated by a distance $r$ is:
$$
U = q_1 \times ( \text{potential due to charge } q_2 \text{ at charge } q_1 \text{'s position}) = q_1 \cdot \frac{k q_2}{r_{12}}.
$$
However, this seems to ignore the energy required to assemble the charges themselves which might need another part mentioning self energy (which usually excludes the energy needed to create the charge itself, focusing only on the interaction energy).

However, what we need here appears to be the "interaction energy" between the charge $q$ and the grounded conducting sphere.

The most common way to interpret the "potential energy of a system" here is the work done to bring the charge $q$ from infinity to a distance $d$ from the center of the grounded sphere. Another part of the work here is the part required to assemble the charge itself (self-energy), but usually, the self-energy of a single point charge is ignored because it could be infinite unless it's specified how the charge was "assembled." Thus, what makes sense here is probably the interaction energy because the question says "net potential energy of this system."

### Interaction energy between charge $q$ and the sphere can be computed as follows:
To find the interaction energy $U_{\text{interaction}}$ between charge $q$ and the sphere, let us recall that the interaction energy can be defined as $q \times V_{\text{(due to sphere)}}$, where $V_{\text{(due to sphere)}}$ is the potential due to the charges on the grounded sphere evaluated at the location of charge $q$.

#### Finding the potential at the location of charge $q$
The potential at the location of charge $q$ (distance $d$ from the center of the sphere) has two contributions: one from the actual charge $q$ itself (which isn't part of the potential "felt" by charge $q$ due to the sphere), and one from the image charge $q'$ (located at a distance $d'$ from the center of the sphere, which is $d' = R^2/d$).
The total potential at the location of $q$ due to the image charge $q'$ (since charge $q$ itself doesn’t contribute a potential "felt" by itself) is evaluated as follows:

The distance between charge $q$ (located at $d$) and the image charge $q'$ (located at $d'$) is:
$$
r_{\text{q to q'}} = d - d' = d - \frac{R^2}{d} = \frac{d^2 - R^2}{d}.
$$
The potential at the position of charge $q$ (which is caused by charge $q'$) is given by:
$$
V_{\text{at q due to q'}} = \frac{q'}{4\pi\epsilon_0 (d - d')} = \frac{q'}{4\pi\epsilon_0 \left(\frac{d^2 - R^2}{d}\right)}.
$$
Recall that:
$$
q' = -\frac{R q}{d}.
$$
Thus:
$$
V_{\text{at q due to q'}} = \frac{-\frac{R q}{d}}{4\pi\epsilon_0 \left(\frac{d^2 - R^2}{d}\right)} = \frac{-\frac{Rq}{d}}{4\pi\epsilon_0 (d^2 - R^2)/d} = \frac{- Rq}{4\pi\epsilon_0 (d^2 - R^2)/d} \times \frac{d}{d} = -\frac{R q}{4\pi\epsilon_0 (d^2 - R^2)}.
$$

Another way to find this directly might be using the formula for electric potential:
$$
V = \frac{k q'}{\text{distance}}.
$$
This gives:
$$
V_{\text{at q}} = \frac{1}{4\pi\epsilon_0} \left( \frac{q'}{d - \frac{R^2}{d}} \right).
$$
Therefore, using $q' = - \frac{Rq}{d}$:
$$
V_{\text{at q}} = \frac{q'}{4\pi\epsilon_0 (d - d')} = \frac{k(-Rq/d)}{d - R^2/d} = \frac{k(-Rq)}{d(d - R^2/d)} \implies -\frac{kRq}{d^2 - R^2}.
$$
where $k = \frac{1}{4 \pi \epsilon_0}$.

#### Interaction energy $qV_{\text{(due to sphere)}}$:
The potential seen by charge $q$ due to the induced charges on the sphere can be interpreted as the potential caused by the image charge $q'$. Thus:
$$
U_{\text{interaction}} = q \times \text{(Potential at charge q due ONLY to charge $q'$)}.
$$
So substitute $V_{\text{at q due to q'}}$ into the interaction energy formula:
$$
U_{\text{interaction}} = q \times \left(-\frac{k Rq}{d^2 - R^2}\right).
$$
$$
\text{where } k =\frac{1}{4 \pi \epsilon_0}, \text{ so:}\\
U_{\text{interaction}} = q \times \left(-\frac{1}{4 \pi \epsilon_0} \cdot \frac{R q}{d^2 - R^2}\right) = -\frac{1}{4 \pi \epsilon_0} \times \frac{R q^2}{d^2 - R^2}.
$$
Thus:
$$
U_{\text{interaction}} = -\frac{R q^2}{4 \pi \epsilon_0 (d^2 - R^2)}.
$$

However, the interaction energy itself should be equal to the negative of the work done by the electric field when bringing charge $q$ from infinity to a distance $d$ from the sphere's center. Thus, if we need to bring charge $q$ from infinity to a distance $d$ from the center once the grounded conductor is already there forming an image charge $q'$, the work performed should be:
$$
W = \int_{\infty}^{d} F \cdot dr.
$$
The force on charge $q$ due to the grounded sphere is equivalent to the force between charge $q$ and the image charge $q'$, which is:
$$
F = -\frac{1}{4 \pi \epsilon_0} \frac{q \cdot q'}{\left(d - d'\right)^2}.
$$
However, the force can also be written explicitly:
$$
F = -\frac{1}{4 \pi \epsilon_0} \frac{q \left(-\frac{R q}{d}\right)}{\left(d - \frac{R^2}{d}\right)^2} = \frac{q \cdot R q}{4 \pi \epsilon_0 d \left(d - \frac{R^2}{d}\right)^2}.
$$
$$
= \frac{q \cdot R q}{4 \pi \epsilon_0 d \cdot \left[\frac{(d^2 - R^2)^2}{d^2}\right]} = \frac{q \cdot R q}{4 \pi \epsilon_0 d \cdot\left(\frac{d^4 - 2 d^2 R^2 + R^4}{d^2}\right)} = \frac{q^2 R d}{4 \pi \epsilon_0 (d^4 - 2d^2 R^2 + R^4)}.
$$
Another way to visualize this force is by using the charge $q$ and $q'$, explicitly:
$$
F = \frac{1}{4\pi\epsilon_0} \left[ \frac{q \left(-\frac{Rq}{d}\right)}{\left(d - \frac{R^2}{d}\right)^2}\right] = \frac{q \times q'}{4\pi\epsilon_0 (d-d')^2}.
$$
However, what matters most for work done is:
$$
W = \int_{\infty}^d F \cdot dr.
$$

However, this force should be solved explicitly for a variable distance $|z|$ (distance from the center of the sphere to the charge $q$ with $z > R$). When we solve for interaction energy, another common way to find the potential energy is through the integral of the force doing work on the charge $q$:
$$
W = -\int_{\infty}^{d} F \cdot dr.
$$
However, a more intuitive integral would be:
$$
U_{\text{interaction}} = \int_{\infty}^d F_{\text{attractive}} dx.
$$
However, our real interest here is a bit more abstract. Another valid way to understand the potential energy of the system might be defined as such:
$$
U = \frac{q}{8\pi\varepsilon_0} \int_{E^2}\,dV,
$$
which treats the total electromagnetic field energy in space. However, that might be a much more complicated calculation here.

However, what seems to be most standard here is that interaction energy should be computed simply as:
$$
U = \frac{q}{2} V_{\text{induced}}(d).
$$
However, this seems a bit off here because $V_{\text{induced}}$ here equals zero (since any potential should be zero including the induced part when the charge is "anywhere" outside the sphere which makes the "system interaction" here zero. However, the question seems to be asking instead for the energy required to place charge $q$ outside the grounded sphere.

However, a more standard way to define the "total electrostatic potential energy" of a charge $q$ placed $d$ units from a grounded conducting sphere should involve the force on charge $q$ only due to the induced charge on the sphere (which behaves as if caused by an imaginary charge $q'$ inside the sphere).

Another way often used for interaction energy is simply:
$$
U_{\text{interaction}} = \frac{1}{4\pi\varepsilon_0} \frac{qq'}{(\text{distance between }q\text{ and }q')}.
$$
Since $q' = -\frac{Rq}{d}$:
$$
U_{\text{interaction}} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{q \left(\frac{-Rq}{d}\right)}{ \left(d - \frac{R^2}{d}\right)} = \frac{1}{4\pi\varepsilon_0} \times \frac{-Rq^2}{d\left(d - \frac{R^2}{d}\right)} = \frac{-Rq^2}{4 \pi\epsilon_0 d \left(d - \frac{R^2}{d}\right)}.
$$
$$
= \frac{-Rq^2}{4 \pi \epsilon_0 (d^2 - R^2)}.
$$
Thus another way looks pretty consistent:
$$
U_{\text{interaction}} = -\frac{q^2 R}{4\pi \epsilon_0 (d^2 - R^2)}.
$$

Thus that seems indeed to be the interaction energy between $q$ and the induced charges on the sphere. Another check might be finding total induced charge:
$$
\text{Total induced charge on sphere} = q' = -\frac{qR}{d}.
$$
However, verifying the volume integral might be another approach:
However, another well-known general formula for electrostatic energy is given by $U_E = \frac{\epsilon_0}{2} \int E^2 \, d\tau$, which makes us check fields explicitly. Yet what we need here is a well-defined answer:
$$ 
U_{\text{interaction}} = \frac{q}{2} V_{\text{inside}} + \frac{Q_{\text{sphere}}}{2} V_{\text{sphere}},
$$
where $V_{\text{sphere}}=0$ for a grounded sphere. However, for a grounded sphere, another known result is that the answer seems to be:
$$
U = -\frac{1}{4\pi\varepsilon_0} \frac{R q^2}{d^2 - R^2}.
$$
However, the most reliable verified formula seems consistently negative for interaction energy which makes sense because bringing charge $q$ to the grounded sphere would be an attractive force if the charge $q$ is positive (negative interaction energy means that work must be done to remove charge $q$ from the sphere).

However, one needs to confirm what the question means by asking for the "net potential energy." The interaction itself is usually described well by:
$$
\boxed{-\frac{1}{4\pi\epsilon_0}\frac{R q^2}{d^2 - R^2}}.
$$
However, it might make sense to double-check units.
$$
\frac{\varepsilon_0 \text{[farad/m]} \times q^2)}{\text{[meter]}},
$$
which makes sense for an energy term ($\frac{F \times C^2}{m} = \frac{J}{C^2} \times C^2 \approx J$).

Hence, the “net potential energy” seems reasonable given as:
$$
\boxed{-\frac{q^2 R}{4 \pi \epsilon_0 (d^2 - R^2)}}.
$$
However, some might write $k = \frac{1}{4 \pi \epsilon_0}$ so that:
$$
U_{\text{int}} = -\frac{k R q^2}{d^2 - R^2}.
$$
This is the main contribution from analyzing the charge interaction between $q$ and the grounded sphere's charge distribution. Another part of the potential energy due to the charge itself (self-energy) is typically not included here unless specifically mentioned.

It appears that reasoning here correctly addresses the question of interaction energy for charge $q$ in the presence of a grounded spherical conductor. 

So this reasoning leads us to a well-defined negative potential energy which indicates that bringing the charge closer to the sphere releases energy because there is an attractive interaction because the induced charge on the sphere is opposite in sign to $q$.

However, one might need to check again what the "potential energy of the system" means if it might also implicitly include any stored energy within the sphere itself. However, while the grounded sphere is at zero potential, that part could be zero. Another part might check the total energy required once the grounded sphere is also taken into account. 

Nevertheless, given the question seems to be solely focused on placing charge $q$ at a distance $d$ from the center of a grounded conducting sphere of radius $R$, the above answer seems consistent and well-reasoned. 

Hence, we should verify we made no mistakes in the logic and that the answer makes physical sense where an attractive interaction results in negative interaction energy.


---

