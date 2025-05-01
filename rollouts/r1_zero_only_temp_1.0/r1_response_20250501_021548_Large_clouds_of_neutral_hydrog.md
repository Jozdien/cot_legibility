# Original Question

Large clouds of neutral hydrogen in deep space absorb the light from background quasars at Lyman alpha wavelength ~1216 Angstrom. Estimate the lower limit on the redshift of this objects such that they can be detected with optical ground-based telescopes? 

---

# DeepSeek response (via openrouter)

\boxed{z \geq 1.5}

---

# DeepSeek reasoning (via openrouter)

To solve for the lower limit on the redshift $z$ such that the Lyman alpha absorption line (which has a rest wavelength of $\lambda_{\text{rest}} = 1216$ Å) can be detected with optical ground-based telescopes, we need to understand what "optical" refers to in this context. The optical window for ground-based telescopes typically spans the wavelength range from approximately $3000$ Angstroms (or 300 nm) to $7000$ Angstroms (or 700 nm); however, a more commonly quoted range for visible light is approximately $4000$ to $7000$ Angstroms (400 nm to 700 nm). However, ground-based telescopes can sometimes detect light slightly outside this "visible" range due to the atmosphere transmitting some ultraviolet (UV) and infrared (IR) light, although absorption by the atmosphere (especially ozone) typically cuts off light at wavelengths shorter than about $3000$ to $3100$ Angstroms. 

However, a broader "optical window" might be defined as roughly between $3000$ Angstroms (300 nm, which is UV light close to the visible spectrum boundary) to beyond $7000$ Angstroms (which extends into the near-infrared region), although this part might be a bit of a stretch because what matters most here is the "longest observable wavelength" which is usually viewed as about $7000$ Angstroms or possibly $8000$ Angstroms for some broader definitions. However, what is important here is that the rest wavelength of the Lyman alpha line is at $1216$ Angstroms, which is deep in the UV part of the spectrum (well outside the optical range). 

The question requires estimating the lower limit on the redshift such that the Lyman alpha line gets redshifted into the "optical" window such that it can be detected by optical ground-based telescopes. Let us denote:
$$
\lambda_{\text{observed}} = \lambda_{\text{rest}}(1+z)
$$
where:
- $\lambda_{\text{observed}}$ is the observed wavelength due to the redshift $z$.
- $\lambda_{\text{rest}}$ is the rest wavelength of the Lyman alpha line, which is $1216$ Angstroms.

To find the lower limit on $z$ such that the Lyman alpha absorption line can be detected, the observed wavelength needs to be at least equal to the shortest wavelength that can be detected by optical ground-based telescopes. We need to solve:
$$
\lambda_{\text{observed}} \geq 3000 \text{ Å} \text{ (assuming a lower limit of $3000$ Å for optical ground-based telescopes)}
$$
and simultaneously, the observed wavelength should ideally also be within the visible part until $7000$ Angstroms (although again, what matters here is that we need the redshifted Lyman-alpha line to be at least at $3000$ Å to fit into the "optical window").

However, the problem statement mentions $3000$ Angstroms as a lower limit for optical ground-based telescopes (since anything below $3000$ Å is mostly absorbed by the Earth's atmosphere). Thus:
$$
\lambda_{\text{rest}}(1+z) \geq 3000 \text{ Å}.
$$
Where $\lambda_{\text{rest}} = 1216$ Å:
$$
1216(1+z) \geq 3000.
$$
Solving for $z$:
$$
1+z \geq \frac{3000}{1216} \approx 2.467,
$$
$$
z \geq 1.467.
$$
However, there seems to be another part here which requires us to make sure that the redshifted Lyman alpha line lies within the part of the spectrum that can be observed by ground-based telescopes until $7000$ Å (the limit for visible light). However, what we need here is only the "lower limit" on the redshift such that the observation can be made from the ground. Thus, if the Lyman alpha wavelength is redshifted such that it reaches a wavelength of $3000$ Å or higher (which is part of the "optical ground-based" window mentioned previously), that seems to be what we need.

However, given that the maximum detectable wavelength could be $7000$ Å (visible light up to $7000$ Å), it makes sense to check what would be the redshift required such that the Lyman alpha line is redshifted such that it exactly reaches the $3000$ Å wavelength limit (since any redshift that makes $\lambda_{\text{observed}}$ greater than $3000$ Å makes it also potentially detectable until about $7000$ Å).

However, now let us make a robust verification once again. The question seems to make an assumption that ground-based optical telescopes can observe light roughly in the range $3000 \text{ Å} - 7000 \text{ Å}$. Hence, another part of verifying this reasoning is to make sure that once redshifted beyond some limit such that the Lyman alpha line is at least $3000$ Å, we need to verify what is the "lower limit" for $z$ such that the observed wavelength falls within the optical window.

Thus, if $3000$ Å is indeed the lower limit, our reasoning thus far appears valid. However, we need to make sure what the "greater-than" part means for the other edge of the optical wavelength window ($7000$ Å). However, there is no upper limit mentioned explicitly except what might be "detectable" by ground-based optical telescopes, which means anything redshifted such that its observed wavelength is within the given "optical" wavelength range should be fine until some practical upper limit.

However, a redshift which makes the Lyman alpha line $3000$ Å means that any additional redshift makes the wavelength even longer (i.e., $1216(1+z) > 3000$ Å for $z > 1.467$). Thus, if $z = 1.467$, $\lambda_{\text{observed}} \approx 3000$ Å. Thus, anything such that $z > 1.467$ should make the observed wavelength longer and thus makes the Lyman alpha line observable if $3000$ Å to $7000$ Å is the "optical" window range we need to verify when the line goes past $7000$ Å. 

Another verification here is what happens if the observed wavelength shifts past the $7000$ Å range (since anything shorter than $3000$ Å is not in the "optical" window). If $\lambda_{\text{rest}}$ redshifts to $7000$ Å,
$$
\lambda_{\text{rest}}(1+z) = 7000,
$$
which implies:
$$
1216(1+z) = 7000,
$$
$$
1+z = \frac{7000}{1216} \approx 5.757,
$$
$$
z \approx 4.757.
$$

This means redshifts such that $1.467 \leq z\leq 4.757$ should make the Lyman alpha line appear somewhere within the $3000$ Å to $7000$ Å window. However, that should not be our main goal here because what is asked is the "lower limit" on the redshift such that the Lyman alpha line can be detected.

Thus, what matters here is that once $z \geq 1.467$, the observed line could be detected (the line will move into the $3000$ Å to $7000$ Å window as soon as $z$ reaches $1.467$, although it might go outside the $3000$ Å to $7000$ Å window once $z$ gets too large such that the line redshifts beyond $7000$ Å).

However, what really matters here appears to be primarily making sure that the Lyman-alpha line (which starts at $1216$ Å in the rest frame) is redshifted such that it can be observed from earth-based telescopes where the lower limit on the detectable wavelength is roughly $3000$ Å, thus our reasoning thus far indicates that:
$$
z \geq 1.467,
$$
which rounds to about $1.5$.

However, a more common lower wavelength cutoff for ground-based optical telescopes is closer to $3800$ Angstroms because the atmosphere blocks most UV light below about $3200$ Å due to ozone absorption. Thus, a more realistic typical lower limit might be taken as $3500$ Å or even strictly $4000$ Å is sometimes used (which is where the visible spectrum usually starts). Therefore, let us recalculate that same reasoning for $4000$ Å instead:
$$
1216(1+z) \geq 4000.
$$
$$
1+z \geq \frac{4000}{1216} \approx 3.289,
$$
$$
z \geq 2.289.
$$

However, it seems a little bit too stringent. Another useful part of the "optical" window for ground-based telescopes sometimes reaches until around $10000$ Å (1 micron), which is usually part of the "near-infrared" region where some optical telescopes (equipped with infrared detectors) could still detect. Such a broader definition makes the "upper edge" of the "optical" window a bit ambiguous. 

Generally, though, most optical telescopes are limited strictly within visible light $4000$ Å to $7000$ Å. Thus, a lower limit of $4000$ Å could be valid. However, for $3500$ Å:
\begin{align}
\lambda_{\text{observed}} \geq 3500,
\\
1216(1+z) \geq 3500,
\\
1+z \geq \frac{3500}{1216} \approx 2.878,
\\
z \geq 1.878.
\end{align}
Additionally verifying for $3000$ Å seems like a reasonable "safe" lower limit where some part of the "near-UV" light might still be detectable.

Hence, an acceptable "lower limit" on the redshift should be such that the redshifted Lyman alpha line at least reaches the lower edge of the ground-based optical window. Thus, a lower limit appears to be $z \geq 1.467$. Another way to interpret the question might be what is needed for the Lyman-alpha line to reach the "visible part" of the electromagnetic spectrum which starts at approximately $4000$ Å (400 nm), which would make the lower limit on $z$ higher such that:
$$
z \geq 2.47,
$$
if "visible light" is strictly interpreted as $400$ nm (4000 Å) to $700$ nm (7000 Å).

However, a more "typical" answer could be rounded based on a $3000$ Å lower endpoint for $z \geq 1.47$ (round up to $1.5$), or if we round $4000$ Å as the actual lower edge of the visible spectrum, then $z \geq 2.29$ (round up to $2.3$). However, an established answer seems to round the "lower limit optical window" to $3100$ Å which implies:
$$
1216(1+z) \geq 3100,
$$
giving:
$$
1+z \geq \frac{3100}{1216} \approx 2.55,
$$
$$
z \geq 1.55,
$$
which might round to $z \geq 1.5$.

Yet, if assuming a "conservative" lower wavelength boundary of $4000$ Å might be too stringent and a more common lower wavelength limit for ground-based optical telescopes might be around $3200$ Angstroms (since anything below $3200$ Angstroms is mostly absorbed by the Earth's ozone layer). Thus, here we need to solve for:
$$
1216(1+z) \geq 3200.
$$
Solving again:
$$
1+z \geq \frac{3200}{1216} \approx 2.63,
$$
$$
z \geq 1.63.
$$
This rounds to $z \geq 1.6$.

However, a round figure for round-off errors needs a round figure such that:
$$
z \geq (3000 / 1216) - 1 \approx 1.5.
$$
Thus, a round answer of $1.5$ seems a reasonable "lower limit" for $z$.

However, a lower limit should thus be when the Lyman alpha line is shifted to the lower edge of the "optical" window which seems to be $3000$ Å if we include the "near-UV" part which is still detectable. Thus, a round figure such as $z \geq 1.5$ seems a safe lower limit of redshift such that the Lyman alpha line is observed within optical ground-based telescopes.

However, a round figure makes sense here. So, a well-accepted answer could be:
$$
z \geq \frac{3000 \, \text{Å}}{1216 \, \text{Å}} - 1 \approx 1.47.
$$
However, a bit safer might be:
$$
z \geq \frac{3500 \, \text{Å}}{1216 \, \text{Å}} - 1 \approx 1.88.
$$
So, a round figure such as $2$ seems a valid round answer because anything less than $z=2$ might make the Lyman alpha line still in the near-UV which is not entirely ideal for all ground-based telescopes capability.

Thus, a realistic (and a bit rounded) answer for the lower limit on the redshift such that the Lyman alpha absorption line can be detected by optical ground-based telescopes seems to be:
$$
\boxed{1.5} \text{ (rounded from $1.467$)}.
$$

However, a commonly derived answer for such a ("lower limit") problem is usually:
$$
z \geq 1.5.
$$

However, it makes sense to round it to the nearest round numbers such as $1.5$ or $2$, but a more "conservative" round-off could be around $2$. 

Hence, a more stringent check could be:
$$1216(1+z) \geq 3800 \text{Å}$$
since visibility starts effectively around $3800$ Å (which gives $z \geq 2.1$). Another round number would be $2$.

However, a round answer like $z \geq 2$ would make:
$$
\lambda_{\text{observed}} = 1216 \times (1+2) = 3648 \text{Å}
$$
which is well within the visible range (which makes sense indeed if we define the visible range as roughly $4000$ Å to $7000$ Å, so $z \geq 2$ makes sure that the Lyman alpha line is well into the ultraviolet-to-visible transition or solidly in the visible part if $z > 2$.

However, taking a "round" (and more commonly given range $4000-7000$ Å):
$$
1216(1+z) \geq 4000,
$$
$$
z \geq 2.29.
$$

**Note:** Therefore, a round answer might be interpreted as:
$$
\text{"Approximately $z \geq 1.5$ (more conservative could be $z\geq2$)."}
$$
However, a more rigorous rounded numerical solve leads us to round off more strictly $1.5$.

Thus, a round answer such as:
$$
\boxed{1.5},
$$
seems reasonable and close to the round-off of $1.5$ is thus a well-defined lower limit on the redshift.

However, another common round up is just checking whether the reasoning stands correct for:

$$
z \approx 1.5,
$$
$$
\lambda_{\text{observed}} = 1216 \times (1+1.5) = 1216 \times 2.5 = 3040 \text{Å}.
$$
Which is close to the $3000$ Angstrom cutoff previously assumed.

Hence, any object with redshift $z \geq 1.5$ should make the Lyman alpha line enter the "optical" window defined for lengths from roughly $3000$ Angstroms upwards. For a more conservative estimate, a round answer of $z \geq 2.5$ might make the Lyman alpha line appear at:
$$
1216 \times (1+2.5) = 1216 \times 3.5 = 4256 \text{Å}.
$$
Hence, a redshift bigger than $1.5$ seems adequate here.

Considering the answer might be verified with some standard typical ranges used in astronomy, a round answer should be verified here again where:
$$
\lambda_{\text{observed}} = \lambda_{\text{rest}} (1+z).
$$
The lower optical limit is taken as $380 \, \text{nm} = 3800 \, \text{Å}$ (which rounds up roughly often):
$$
\lambda_{\text{observed}} = 3800\, \text{Å}.
$$
Hence:
$$
3800 = 1216 \times(1+z),
$$
$$
1+z = \frac{3800}{1216} \approx 3.125,
$$
$$
z \approx 3.125 - 1 = 2.125,
$$
rounding to $z \geq 2.1$.

Thus, $z \geq 1.5$ seems reasonable for a lower limit such that the Lyman alpha line at $1216$ Å could be detected from ground-based optical telescopes where the window is $3000$ to $7000$ Å typically defined (lower ends such as $3000$ Å are a bit stringent so rounding could make us verify that $1.5$ seems a solid round figure such that the Lyman alpha line shifts sufficiently into the ground-based observable range.

Thus $z\geq1.5$ seems a well-rounded "lower limit" on redshift here.
However, a round limit such as $z\geq1.467$ might round properly to $1.5$, thus $1.5$ appears a valid round estimate such that the Lyman alpha line is redshifted sufficiently into the optical detection region.


---

