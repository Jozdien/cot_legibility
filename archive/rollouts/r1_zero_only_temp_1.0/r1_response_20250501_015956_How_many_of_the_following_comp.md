# Original Question

How many of the following compounds will exhibit optical activity?

(Z)-1-chloro-2-methylbut-1-ene
(3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione
(2R,3S)-2,3-dimethylsuccinic acid
(2R,3R)-2,3-dimethylsuccinic acid
(R)-cyclohex-3-en-1-ol
(1s,3s,5s)-cyclohexane-1,3,5-triol
1-cyclopentyl-3-methylbutan-1-one

---

# DeepSeek response (via openrouter)



---

# DeepSeek reasoning (via openrouter)

To solve for the optical activity of each given compound, recall that a compound exhibits optical activity if it has a chiral center (excluding meso compounds where the molecule has chiral centers but is still optically inactive due to internal plane of symmetry making the molecule achiral) or if the molecule itself is chiral due to other factors such as axial chirality or overall molecular chirality (as in the case of some allenes or spiro compounds).

1. **(Z)-1-chloro-2-methylbut-1-ene**

   The structural formula for this compound is:

   $$CH_3-CH(CH_3)-CH=CHCl$$

   To make it easier to analyze, let's write out the carbon skeleton explicitly:
    
$$
\text{(Z)-1-chloro-2-methylbut-1-ene can be written as: } CH_3-CH(CH_3)-CH=CHCl.
$$
The "Z" stereochemistry implies that the higher priority groups on either side of the double bond are on the same side of the double bond. However, what matters here is whether the molecule itself is chiral.

   First, identify carbon atoms and check for chirality:
   
   For a carbon atom to be chiral, it should be bonded to four different groups. Let us label the chain from right to left:
   
   $\text{CHCl=CH-CH(CH}_3\text{)-CH}_3$
   
   Where:
   Carbon 1 is connected to Cl, H, and the second carbon atom (which is bonded to another carbon atom and a hydrogen atom).
   Carbon 2 has a methyl group (CH$_3$), a hydrogen atom, Carbon 1 (which connects to Cl and H), and Carbon 3 (which connects to another CH$_3$ group).
   Carbon 3 (which is the carbon atom labeled CH(CH$_3$)), has a CH$_3$ group, a hydrogen atom, Carbon 2 (connected to CH$_3$, H, Carbon 1), and Carbon 4 (which is a CH$_3$ group).
   Carbon 4 is simply a methyl group (CH$_3$ group connected to Carbon 3).
   
   Analyzing carbon 2 (which is connected to CH$_3$, H, the rest-part of the chain including Carbon 1 which includes Cl and H, and another part connected to Carbon 3 which includes a CH$_3$ group):
   The groups are:
   - CH$_3$
   - H
   - $CH=CHCl$ group (which can be treated as a single group here until further broken down)
   - CH$_3$ (which is part of Carbon 3 being part of the chain CH$_3-CH_2-CH_...$)

   However, to determine if carbon 2 could be chiral, we need to check if it is connected to four different groups. The groups include:
   - CH$_3$ group
   - H atom
   - CH$_3$CH(CHCl=CH) group (this part should be split into two groups: one part goes towards CHCl=CH and another part goes towards the other CH$_3$ group attached to Carbon 3).
   
   To make this clearer, explicitly identify the groups attached to Carbon 2 (let us call it C2):
   - A methyl group (CH$_3$).
   - A hydrogen atom (H).
   - A rest group ending in C1 where C1 connects to Cl and H (which makes this group "CH=CHCl").
   - Another part that starts with another carbon (let's call it C3) which connects to another methyl group (CH$_3$).
   
   Now, checking if carbon 2 is a chiral center requires us to check whether these four groups are distinct. Here, the next part is CH(CH$_3$)-CH$_3$. Since carbon 2 connects to CH$_askedusinstead check if the group $-$CH=CHCl is different from $-$CH$_3$. Both need to be different for C2 to be chiral. Thus, if one part goes $-$CH=CHCl (which is an ethenyl group where carbon has a double bond with another carbon that connects to chlorine) and the other part goes $-$CH$_3$, these two groups are indeed different so far. Another part is a proton (H), which is clearly different from either $-$CH=CHCl or $-$CH$_3$.

   Thus, the four groups attached to carbon 2 are:
   - $-$CH$_3$ group (which contains three hydrogen atoms)
   - $-$H
   - $-$CH=CHCl group (which is substantially different from $-$CH$_3$)
   - $-$CH(CH$_3$)-CH$_3$ which defines the rest of the chain beyond carbon 2.

   Another way to check groups explicitly is by ordering them based on priority (Cahn-Ingold-Prelog rules).
   The groups are:
    CH$_3$ (priority 1 because it connects [C,H,H]), H (priority 4), $-$CH=CHCl has a higher priority since it includes a double bond with a carbon that connects to a chlorine atom (which has a higher priority due to chlorine atom). 

   However, a primary check makes it seem like carbon 2 could potentially be a chiral center unless some part of the $-$CH=CHCl makes one part symmetric with another. Therefore, let us check the whole molecule for chirality explicitly:
   
   The given compound is defined explicitly as (Z)-1-chloro-2-methylbut-1-ene. The "Z" indicates that the two groups on the double bond (which are chlorine on carbon 1 and methyl on carbon 2) are on the same side (relative to the double bond).
   
   To check chirality more explicitly, if configuration is given as "Z":

   The structure thus might be described as follows where $C_4$ is carbon 4 (methyl group), $C_3$ is carbon 3 (methylene group linked directly to both $C_2$ and $C_4$ methyl group), $C_2$ is the second carbon atom connected to $C_3$ and $C_1$, and $C_1$ connects to $C_2$, chlorine, and hydrogen atom on the double bond.

   Checking for a plane of symmetry might provide a clearer confirmation. To verify if the molecule is chiral:
   
   Draw the molecule such that:
   - $C1$ has a double bond to another carbon (let's call it $C2$, here $C2$ also has a connection to a methyl group (CH$_3$) and a proton(H).
   - $C2$ is connected to $C1$, $C3$, a methyl group, and a hydrogen atom.
   - $C3$ is connected to $C2$, another methyl group (CH$_3$), and a proton.

   To make a more descriptive drawing:
   
   Draw out the structure explicitly:
$$
\begin{array}{c}
    \text{CH}_3 \\
    | \\
    \text{H}_3\text{C} - \underset{|}{\overset{H}{\text{C}}} - \text{CH} = \underset{|}{\text{CH}} - \text{Cl} \\
    \text{(Z) configuration means that the CH}_3 (on C2) and Cl (on C1) are on the same side of the double bond.}
\end{array}
$$
To make a stereochemistry understanding:
$$
\ce{CH3-CH(CH3)-CH=CHCl} \text{ where CH3-CH(CH3) part means CH3-CH-CH3 where the middle CH has a CH3 and a H}
$$
We need to draw the actual Z isomer for the double bond:
$$
\ce{
    CH3-CH-CH-CHCl\\
       | |    || \\
    CH3 H     H
}
$$
However, the given representation should be clearer. Another way to draw it correctly is:
$$
\ce{
        \text{H} \\
          |\\
    \text{CH3}$-$C$=$CH$-$Cl\\
          |\\
          \text{CH3}
}
$$
The main question here is whether there is a plane of symmetry. Checking chirality for all carbons again:
   - Carbon 2 is a chiral center because:
       - It is bonded to CH$_3$, H, a chain with a double bond (including a Cl), and another part of the chain (branch CH$_turn on CH$_3$ group attached to it).
   So, carbon 2 is attached to:
   - CH$_3$-group,
   - $-$$CH$(CH$_3$)-remark{CH}$=CHCl$ (simplify this into $-$CH=CHCl because it has priority issues).
   - A hydrogen atom.
   - The CH$_3$ group connected to carbon 3 also affects the chirality.

   Another check should verify if the molecule itself lacks a plane of symmetry overall. Upon checking again, there is no internal plane of symmetry due to:
      
Hence **(Z)-1-chloro-2-methylbut-1-ene should indeed exhibit optical activity.**

2. **(3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione**

   For such a complex name, break it down:
   
   The compound name suggests specific stereochemistry "3aR, 7aS" and an "E" configuration for the "chloromethylene" part. However, what should be done here is to analyze whether the compound will be chiral. 

   Because the compound has defined stereoconfigurations such as (3aR,7aS), the "3aR" and "7aS" parts indicate chiral centers with specific stereochemical configurations. However, whether the compound itself is chiral needs to be confirmed.

   This compound name says "E" and "8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione" which is a bicyclic compound where specific stereo-configurations can make a compound chiral overall. However, one should check whether there is any internal plane of symmetry which could make it a meso compound.

   To verify if it is optically active, given "chloromethylene" part has an "E" configuration and given stereocenters are "3aR" and "7aS". However, without an actual structural drawing, it could be challenging to visualize if there exists a plane of symmetry. 

   Yet, one thing is sure: three stereocenters are mentioned here ("3aR, 7aS" and E-configuration). Hence, if the molecule does not have a plane of symmetry, it should be chiral and optically active. Based purely on the provided stereochemical assignments "3aR, 7aS", which implies two defined stereocenters with defined configurations, this compound appears to be asymmetric and thus optically active.

3. **(2R,3S)-2,3-dimethylsuccinic acid**

   For the compound "2,3-dimethylsuccinic acid," the structure is:
$$HOOC-CH(CH_3)-CH(CH_3)-COOH$$

Specific stereochemistry given is (2R,3S).
To check optical activity, let us draw out the structure explicitly such that:
1. Carbon 2 is chiral and has R-configuration.
2. Carbon 3 is chiral and has S-configuration.

The compound structure thus could be:
$$
\begin{array}{c}
    \text{HOOC} - \underset{(2R)-\text{carbon}}{\text{CH}(\text{CH}_3)} - \underset{(3S)-\text{carbon}}{\text{CH}(\text{CH}_3)} - \text{COOH}
\end{array}
$$
    
To verify chirality or optical activity, if the compound has chiral centers but still has an internal plane of symmetry, it would be a meso compound and optically inactive.

Let us check for such a plane of symmetry:
1. For a compound HOOC-CH(CH$_3$)-CH(CH$_3$)-COOH to be potentially meso, it needs to contain chiral centers such that they are mirror images within the same Koch implies that its mirror-image should be superimposable on itself. 

   To find any plane of symmetry, rotate the molecule such that the two carboxyl groups are on opposite ends:
  
   A molecule labeled specifically as (2R,3S)-2,3-dimethylsuccinic acid has two chiral centers where one center is R-configuration and the other is S-configuration. This makes the molecule a potential candidate for being a meso compound if the two chiral centers mirror each other and there is a plane of symmetry.

   To validate, let us draw a Fischer projection considering (2R, 3S)-2,3-dimethylsuccinic acid:
$$
\begin{array}{ccc}
    & \text{COOH} & \\
    \text{(2R)-CH(CH$_3$)} & \text{H} & \\
    \text{(3S)-CH(CH$_3$)} & - & \text{H} \\
    & \text{COOH} &
\end{array}
$$

   The Fischer projection should show:
$$
\begin{array}{ccc}
    & \text{COOH} & \\
    \text{(2R)} &\text{-CH(CH}_3)& \text{H} \\
    \text{(3S)} &\text{-} & \text{H} \text{CH(CH$_3$)} \\
    & \text{COOH} &
\end{array}
$$
By rotating this structure about any axis should not make the molecule superimposable to its mirror image if there wasn't any plane of symmetry. However, for a meso compound, the composed stereoisomer should be a symmetric internally.

If we reflect this structure over a plane that cuts perpendicularly in the middle of the C2-C3 bond, one half should be a mirrored version of the other half (because one part would be (2R,3S) while mirrored version would be (2S,3R) yet claims look symmetric if the molecule is indeed symmetric).

However, (2R,3S)-2,3-dimethylsuccinic acid indeed has two chiral centers where one is R-configuration and the other is S-configuration. Such a compound is indeed a meso compound (because R and S neutralize one another if there exists a plane of symmetry dividing the molecule into two mirror-image halves).

So, **(2R,3S)-2,3-dimethylsuccinic acid is optically inactive**.

4. **(2R,3R)-2,3-dimethylsuccinic acid**

   From the previous part, the structure for "(2R,3R)-2,3-dimethylsuccinic acid" is:
$$
\begin{array}{c}
    \text{HOOC} - \underset{(2R)}{\text{CH}(\text{CH}_3)} - \underset{(3R)}{\text{CH}(\text{CH}_3)} - \text{COOH}
\end{array}
$$
Similar to (2R,3S)-2,3-dimethylsuccinic acid, check whether this compound has a plane of symmetry.
    
   For (2R,3R), there is no plane of symmetry since both chirality centers have the same R-configuration. There exists no internal symmetric plane dividing the molecule into two mirror-image halves where each part balances out chirality.

   Therefore, (2R,3R)-2,3-dimethylsuccinic acid is not meso and hence should be chiral and exhibit optical activity.

5. **(R)-cyclohex-3-en-1-ol:**

   "(R)-cyclohex-3-en-1-ol" refers to a cyclohexene molecule substituted by an alcohol group at position 1 such that carbon 1 has an R-configuration (cyclohex-3-en-1-ol means that there is a double bond from carbon 3 to carbon 4 in the cyclohexane ring, while there is an alcohol group on carbon 1).

   The parent compound is:
$$
\begin{array}{c}
    \text{cyclohex-3-en-1-ol with an R-configuration at carbon 1}.
\end{array}
$$
Let us draw out the cyclohex-3-en-1-ol structure first,
$$
\ce{
      \underset{1}{\overset{OH}{\mkern2mu\underline{\ce{C}}H}}-\underset{2}{\ce{CH2}}-\underset{3}{\overset{\text{(double bond starts here)}}{\ce{CH}}}=\underset{4}{\ce{CH}}-\underset{5}{\ce{CH2}}-\underset{6}{\ce{CH2}}
}
$$
Which makes a 6-membered ring with a double bond between carbons 3 and 4.

The question now is whether (R)-cyclohex-3-en-1-ol is chiral specifically due to the chiral center labeled as "R" on carbon 1. 

   However, an important realization here is that the double bond "locks" part of the ring such that carbons 3 and 4 cannot freely rotate. This kind of "locking" might make one part of the ring different from another part.

   To verify if carbon 1 can be a chiral center and if the molecule is overall chiral excluding meso compound situations:
   Carbon 1 is connected to:
   - An OH group
   - A carbon (which is part of a chain that extends to form a ring)
   - Another carbon (which is also part of the ring)
   - A hydrogen atom.
   
   To make carbon 1 a chiral center, the other two carbon parts connection should indeed be different. Since carbon 1 connects to carbon 6 and carbon 2 as part of the ring, let us closely compare the "left" part (which goes from carbon 1 to carbon 6 towards couchylotag round to carbon 4) versus the "right" part (which goes from carbon 1 towards carbon 2 to carbon 3):
   
   The part going from carbon 1 through carbon 2 to carbon 3 (which includes a double bond) is different from the part going from carbon 1 through carbon相手6 to carbon 5 and then to carbon 4. The double bond makes carbon 3 be sp2 hybridized and hence makes one part of the ring distinctly different from the other part.
   Thus, carbon 肌肉1 is indeed a chiral center with R-configuration, making the molecule chiral and hence this compound should be optically active.

6. **(1s,3s,5s)-cyclohexane-1,3,5-triol**

   The label "$1s, 3s, 5s$" should actually be written as $(1\text{s},3\text{s},5\text{s})$ for "1s," "3s," and "5s" stereocenters on cyclohexane-1,3,5-triol where "s" might be a typo for "S" indicating $S$ configuration:
   $$
   \text{(1s,3s,5s)-cyclohexane-1,3,5-triol}
   $$
   However, "s" usually denotes "sinister" which corresponds to "S" configuration. Let assume they mean $(1S, 3S, 5S)$.

   Cyclohexane-1,3,5-triol means three hydroxyl groups at positions cis positions:
  

---

