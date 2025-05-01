# Original Question

We have a solution containing Co(II) ions and thiocyanate, where the total cobalt concentration is c(Co) = 10^-2 M and the [SCN-] concentration is 0.1 M. The stability constants of the cobalt(II) thiocyanato complexes are β1=9, β2=40, β3=63 and β4=16. What will be the percentage of the blue dithiocyanato cobalt(II) complexes among all cobalt containing species in the solution? 

---

# DeepSeek response (via openrouter)



---

# DeepSeek reasoning (via openrouter)

To solve for the percentage of the blue dithiocyanato cobalt(II) complexes among all cobalt-containing species in the solution, we need to identify what the dithiocyanato cobalt(II) complex is and calculate its concentration compared to the total cobalt concentration.

The question specifies that the total cobalt concentration $c(\text{Co}) = 10^{-2} \text{ M}$ and total thiocyanate concentration $[\text{SCN}^-]_{\text{total}} = 0.1 \text{ M}$. Additionally, the stability constants for the cobalt(II) thiocyanato complexes are given such that:
$$
\beta_1 = 9, \beta_2 = 40, \beta_3 = 63, \text{ and } \beta_4 = 16.
$$
Here, $\beta_n$ refers to the overall stability constant for the reaction where $n$ thiocyanate ions bind to a cobalt(II) ion:
$$
\text{Co}^{2+} + n \text{SCN}^- \rightleftharpoons \text{Co}(\text{SCN})_n^{(2-n)+} \text{ where } (n=1,2,3,4).
$$
Thus:
$$
\beta_1 = \frac{[\text{Co(SCN)}^+]}{[\text{Co}^{2+}][\text{SCN}^-]} = 9,
$$
$$
\beta_2 = \frac{[\text{Co(SCN)}_2]}{[\text{Co}^{2+}][\text{SCN}^-]^2} = 40,
$$
$$
\beta_3 = \frac{[\text{Co(SCN)}_3^-]}{[\text{Co}^{2+}][\text{SCN}^-]^3} = 63,
$$
$$
\beta_4 = \frac{[\text{Co(SCN)}_4^{2-}]}{[\text{Co}^{2+}][\text{SCN}^-]^4} = 16.
$$
However, the question mentions that "the blue dithiocyanato cobalt(II) complex" should be identified among all species. Thus, the "dithiocyanato cobalt(II) complex" most likely corresponds to $\text{Co(SCN)}_2$, since `dithiocyanato` implies that two thiocyanate ions are coordinated to the cobalt(II) ion.

Let us define the free cobalt ion concentration $[\text{Co}^{2+}]$ as $x$. The total cobalt concentration $c(\text{Co})$ is the sum of the concentrations of the various cobalt species formed from cobalt(II) ions and thiocyanate:
$$
c(\text{Co}) = [\text{Co}^{2+}] + [\text{Co(SCN)}^+] + [\text{Co(SCN)}_2] + [\text{Co(SCN)}_3^-] + [\text{Co(SCN)}_4^{2-}].
$$
This can be written explicitly as:
$$
c(\text{Co}) = [\text{Co}^{2+}] + \beta_1 [\text{Co}^{2+}][\text{SCN}^-] + \beta_2 [\text{Co}^{2+}][\text{SCN}^-]^2 + \beta_3 [\text{Co}^{2+}][\text{SCN}^-]^3 + \beta_4 [\text{Co}^{2+}][Zr(\text{SCN}^-]^4.
$$
Factoring out $[\text{Co}^{2+}]$, we get:
$$
c(\text{Co}) = [\text{Co}^{2+}] (1 + \beta_1 [\text{SCN}^-] + \beta_2 [\text{SCN}^-]^2 + \beta_3 [\text{SCN}^-]^3 + \beta_4 [\text{SCN}^-]^4).
$$
The question now is what the concentration of the free thiocyanate ion $[\text{SCN}^-]$ is. To find out what this is, we need to write the total thiocyanate concentration $c(\text{SCN}^-)$ given:
$$
c(\text{SCN}^-) = [\text{SCN}^-]_{\text{free}} + [\text{Co(SCN)}^+] + 2\cdot [\text{Co(SCN)}_2] + 3\cdot [\text{Co(SCN)}_3^-] + 4\cdot [\text{Co(SCN)}_4^{2-}].
$$
This equation represents all the thiocyanate molecules that are bound in different complexes. However, a more convenient way to write this is:
$$
[\text{SCN}^-]_{\text{total}} = [\text{SCN}^-]_{\text{free}} + [\text{Co(SCN)}^+] + 2 \cdot[\text{Co(SCN)}_2] + 3 \cdot[\text{Co(SCN)}_3^-] + 4 \cdot[\text{Co(SCN)}_4^{2-}],
$$
where $[\text{SCN}^-]_{\text{total}}$ is given as $0.1 \text{ M}$.

However, given that $[\text{SCN}^-]_{\text{total}} = 0.1 \text{ M}$ which is much larger than $c(\text{Co}) = 10^{-2} \text{ M}$, and the binding of Co(II) ions to thiocyanate may be treated approximately such that:
$$
[\text{SCN}^-]_{\text{free}} \approx [\text{SCN}^-]_{\text{total}} = 0.1 \text{ M}.
$$
This approximation assumes that most of the $\text{SCN}^-$ remains free because the total thiocyanate concentration is an order of magnitude larger than the total cobalt concentration. Yet another part of thiocyanate is used in forming the complexes such as $\text{Co(SCN)}^+$, $\text{Co(SCN)}_2$, $\text{Co(SCN)}_3^-$, and $\text{Co(SCN)}_4^{2-}$. However, the actual free thiocyanate concentration should be slightly less than $0.1 \text{M}$. Let us refine this part:
$$
[\text{SCN}^-]_{\text{total}} = [\text{SCN}^-]_{\text{free}} + [\text{Co(SCN)}^+] + 2\cdot [\text{Co(SCN)}_2] + 3\cdot [\text{CoSCN}_3^-] + 4\cdot [\text{Co(SCN)}_4^{2-}].
$$
However, another way to draw a boundary here is by directly using the previous relation:
$$
[\text{SCN}^-]_{\text{total}} = [\text{SCN}^-] + [\text{Co(SCN)}^_] + \color{red}{2}[\text{Co(SCN)}_2] + \color{red}{3}[\text{Co(SCN)}_3^-] + \color{red}{4}[\text{Co(SCN)}_4^{2-}].
$$
But, let us here define:
$$
\alpha_{\text{SCN}} = [\text{SCN}^-] + [\text{Co(SCN)}^+] + \color{red}{2}[\text{Co(SCN)}_2] + \color{red}{3}[\text{Co(SCN)}_3^-] + \color{red}{4}[\text{Co(SCN)}_4^{2-}],
$$
where $[\text{SCN}^{-}]_{\text{total}} = 0.1 \text{ M}$. However, we need the free thiocyanate concentration $[\text{SCN}^-]$, which appears in the expressions for the concentration of various complexes formed.

Nevertheless, one major assumption might make the analysis simpler - that $c(\text{SCN}^-) \gg c(\text{Co})$, so that the thiocyanate consumed in forming complexes is relatively insignificant compared to the total thiocyanate added. Another part that makes this reasoning a bit more complex is that $[\text{SCN}^-]_{\text{total}}$ is ten times larger than $c(\text{Co})$, so an initial approximation could be that $|\text{SCN}^-| \approx 0.1 \text{ M}$. 

Another way to make a more rigorous calculation is to solve explicitly for $[\text{SCN}^-]_{\text{free}}$. However, once again, one should check how much thiocyanate is bound in complexes. Given that:
$$
c(\text{Co}) = [\text{Co}^{2+}] + [\text{Co(SCN)}^+] + [\text{Co(SCN)}_2] + [\text{Co(SCN)}_3^-] + [\text{Co(SCN)}_4^{2-}]\\
\text{or } c(\text{Co})=[\text{Co}^{2+}]\left(1 + \beta_1 [\text{SCN}^-] + \beta_2 [\text{SCN}^{]^2} + \beta_3 [\text{SCN}^-]^3 + \beta_4 [\text{SCN}^-]^4\right).
$$
Let us fill in the given stability constants and assume $[\text{SCN}^-] \approx 0.1 \text{ M}$ (initially):
$$
c(\text{Co}) = [\text{Co}^{2+}] \left(1 + 9 \times 0.1 + 40 \times (0.1)^2 + 63 \times (0.1)^3 + 16 \times (0.1)^4\right).
$$
Let us calculate the polynomial part:
$$
= 1 + 9 \times 0.1 + 40 \times 0.01 + 63 \times 0.001 + 16 \times 0.0001,
$$
$$
= 1 + 0.9 + 0.4 + 0.063 + 0.0016,
$$
$$
\approx 2.3646.
$$
Therefore, the total cobalt concentration is:
$$
c(\text{Co}) = [\text{Co|^{2+}}] \times 2.3646.
$$
However, $c(\text{Co}) = 10^{-2} \text{ M}$, so:
$$
10^{-2} = [\text{Co}^{2+}] \times 2.3646,
$$
$$
[\text{Co}^{2+}] = \frac{10^{-2}}{2.3646} \approx 4.23 \times 10^{-3} \text{ M}.
$$
#### To find the concentrations of the species:
$$
\text{[Co(SCN)}^+] = \beta_1 [\text{Co}^{2+}][\text{SCN}^-] = 9 \times 4.23 \times 10^{-3} \times 0.1 = 9 \times 4.23 \times 10^{-4} = 3.807 \times 10^{-3} \text{ M}.
$$
$$
[\text{Co(SCN)}_2] = \beta_2 [\text{Co}^{2+}][\text{SCN}^-]^2 = 40 \times 4.23 \times 10^{-3} \times (0.1)^2 = 40 \times 4.23 \times 10^{-5} = 1.692 \times 10^{-3} \text{ M}.
$$
$$
[\text{Co(] = \beta_3 [\text{Co}^{2+}][\text{SCN}^-]^3 = 63 \times 4.23 \times 10^{-3} \times (0.1)^3 = 63 \times 4.23 \times 10^{-6} = 2.6649 \times 10^{-4} \text{ M}.
$$
$$
[\text{Co(SCN)}_4^{2-}] = \beta_4 [\text{Co}^{2+}][\text{SCN}^-]^4 = 16 \times 4.23 \times 10^{-3} \times (0.1)^4 = 16 \times 4.23 \times 10^{-7} = 6.768 \times 10^{-6} \text{ M}.
$$
#### Verification by summing up:
Total cobalt concentration should be:
$$
= [\text{Co}^{2+}] + [\text{Co(SCN)}^+] + [\text{Co(SCN)}_2] + [\text{Co(SCN)}_3^-] + [\text{Co(SCN)}_4^{2-}]\\
\approx 4.23 \times 10^{-3} + 3.807 \times 10^{-3} + 1.692 \times 10^{-3} + 2.6649 \times 10^{-4} + 6.768 \times 10^{-6},\\
\approx (4.23 + 3.807 + 1.692 + 0.26649 + 0.006768) \times 10^{-3}.
$$
$$
\approx 10.002 \times 10^{-3} = 1.0002 \times 10^{-2} \approx 10^{-2} \text{ M}.
$$
This validates that the total cobalt concentration is correctly distributed among the various species formed.

#### To find the percentage of $\text{Co(SCN)}_2$ among all cobalt-containing species:
Total cobalt-containing species’ concentration is:
$$
[c(\text{Co})]_{\text{total}} = [\text{Co}^{2+}] + [\text{Co(SCN)}^+] + [\text{Co(SCN)}_2] + [\text{Co(SCN)}_3^-] + [\text{Co(SCN)}_4^{2-}] = 10^{-2} \text{ M}.
$$
The question now is what fraction of total cobalt is in the form of $[\text{Co(SCN)}_2]$. We need:
$$
\text{Percentage of } [\text{Co(SCN)}_2] = \frac{[\text{Co(SCN)}_2]}{c(\text{Co})} \times 100\%.
$$
This is:
$$
\frac{[\text{Co(SCN)}_2]}{10^{-2}} \times 100\%.
$$
We previously calculated:
$$
[\text{Co(SCN)}_2] = 1.692 \times 10^{-3} \text{ M}.
$$
Thus, the percentage is:
$$
\frac{1.692 \times 10^{-3}}{10^{-2}} \times 100\% = \frac{1.692 \times 10^{-3}}{1 \times 10^{-2}} \times 100\% = \frac{1.692}{10} \times 100\% \approx 16.92\%.
$$

Another shorter way to directly solve for the fraction $\varphi[\text{Co(SCN)}_2]$ is by using distribution calculations derived from the polynomial used previously:
$$
\varphi[\text{Co}^{2+}] = \frac{[\text{Co}^{2+}]}{c(\text{Co})} = \frac{1}{1 + \beta_1 [\text{SCN}^-] + \beta_2 [\text{SCN}^-]^2 + \beta_3 [\text{SC + \beta_4 [\text{SCN}^-]^4}.
$$
$$
\varphi[\text{Co(SCN)}^+] = \frac{\beta_1 [\text{SCN}^-]}{1 + \beta_1 [\text{SCN}^-] + \beta_2 [\text{SCN^*]^2} + \beta_3 [\text{SCN}^-]^3 + \beta_4 [\text{SCN}^-]^4}.
$$
$$
\varphi[\text{Co(SCN)}_2] = \frac{\beta_2 [\text{SCN}^-]^2}{1 + \beta_1 [\text{SCN}^-] + \beta_2 [\text{SCN}^-]^2 + \beta_3 [\text{SCN}^-]^3 + \beta_4 [\text{SCN}^-]^4}.
$$
$$
\varphi[\text{Co(SCN)}_3^-] = \frac{\beta_3 [\text{SCN}^-]^3}{1 + \beta_1 [\text{SCN}^-] + \beta_2 [\text{SCN}^-]^2 + \beta_3 [\text{SCN}^-]^3 + \beta_4 [\text{SCN}^-]^4}.
$$
$$
\varphi[\text{Co(SCN)}_4^{2-}] = \frac{\beta_4 [\text{SCN}^-]^4}{1 + \beta_1 [\text{SCN}^-] + \beta_2 [\text + \beta_3 [\text{SCN}^-]^3 + \beta_4 [\text{SCN}^-]^4}.
$$

We need the fraction of $\text{Co(SCN)}_2$ specifically:
$$
\varphi[\text{Co(SCN)}_2] = \frac{\beta_2 [\text{SCN}^-]^2}{1 + \beta_1 [\text{SCN}^-] + \beta_2 [\text{SCN}^-]^2 + \beta_3 [\text{SCN}^-]^3 + \beta_4 [\text{SCN}^-]^4}.
$$
Based on our previous calculations:
$$
1 + \beta_1 [\text{SCN}^-] + \beta_2 [\text{SCN}^-]^2 + \beta_3 [\text{SCN}^-]^3 + \beta_4 [\text{SCN}^-]^4 \approx 1 + 0.9 + 0.4 + 0.063 + 0.0016 \approx 2.3646.
$$
The part corresponding to $\text{Co(SCN)}_2$

---

