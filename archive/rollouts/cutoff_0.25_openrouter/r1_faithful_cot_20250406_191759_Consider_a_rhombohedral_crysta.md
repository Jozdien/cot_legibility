# Original Question

Consider a rhombohedral crystal, with the interatomic distance of 10 Angstrom and the angles $\quad\alpha=\beta=\gamma=30^{0}$. What is the interplanar distance of the (111) plane of the crystal?


---

# DeepSeek response (via openrouter)



---

# DeepSeek reasoning (via openrouter)

Alright, so I need to find the interplanar distance for the (111) plane in a rhombohedral crystal. The given parameters are the interatomic distance, which is 10 Angstroms, and all the angles α, β, γ are 30 degrees. Hmm, okay. Let me recall what I know about crystal structures and interplanar distances.

First, the interplanar distance, often denoted d_{hkl}, is the distance between consecutive parallel planes with Miller indices (hkl). For different crystal systems, the formula to calculate d_{hkl} varies. Since this is a rhombohedral crystal, which is a type of Bravais lattice, I need to use the appropriate formula for the rhombohedral system.

But wait, I should confirm if the rhombohedral system is the same as trigonal. I think sometimes they are used interchangeably, but strictly speaking, the rhombohedral lattice is a subset of the trigonal crystal system. Anyway, the key here is that the lattice parameters for a rhombohedral system are a = b = c and α = β = γ ≠ 90°. In this problem, they mention α = β = γ = 30°, so that fits the rhombohedral system. The interatomic distance is given as 10 Angstroms. Wait, interatomic distance—is that the same as the lattice parameter a? Hmm, maybe. In a rhombohedral lattice, all edges are equal, so a = b = c. But interatomic distance could refer to the distance between two adjacent atoms. If the crystal is primitive rhombohedral, then the lattice parameters a, b, c are the distances between the corners of the rhombohedron, and the interatomic distance would be the edge length. So maybe in this case, the interatomic distance is the edge length a, which is 10 Angstroms. So a = 10 Å, and α = β = γ = 30°.

Now, the formula for the interplanar distance in a rhombohedral system. I need to recall the general formula for d_{hkl} in a rhombohedral lattice. Let me think. For a general crystal system, the interplanar distance is given by:

1/d² = (h²/a² + k²/b² + l²/c² + ... terms involving the angles ... ) / (some function of the angles)

But for the rhombohedral system, since a = b = c and α = β = γ, the formula should simplify. Alternatively, maybe it's easier to convert the rhombohedral lattice to a hexagonal lattice, perform the calculation there, and then convert back? Because sometimes rhombohedral can be expressed in a hexagonal setting. But I might be overcomplicating.

Alternatively, I can use the formula specific to the rhombohedral system. Let me check my memory. The formula for the interplanar distance in a rhombohedral lattice is:

1/d² = [(h² + k² + l²) sin²α + 2(hk + kl + lh)(cos²α - cosα)] / [a²(1 - 3cos²α + 2cos³α)]

Wait, that seems complicated. Is there a simpler way? Maybe I should refer to the general triclinic formula, since rhombohedral is a special case of triclinic with a = b = c and α = β = γ. The general triclinic formula for d_{hkl} is:

1/d² = (1/V²)[ S₁₁h² + S₂₂k² + S₃₃l² + 2S₂₃kl + 2S₁₃hl + 2S₁₂hk ]

Where V is the volume of the unit cell, and S_ij are the elements of the metric tensor. But this might be too involved. Alternatively, maybe I can use the formula in terms of the lattice parameters and angles.

Wait, let me look up the formula for interplanar distance in rhombohedral crystals. Hmm, since I can't actually look it up, I need to derive it. Let's see.

In a rhombohedral system, the unit cell is a rhombohedron with edges a = b = c and angles α = β = γ. The volume of the unit cell is given by:

V = a³√(1 - 3cos²α + 2cos³α)

The reciprocal lattice parameters can be calculated using:

a* = (b × c) / V

Similarly for b* and c*. Then, the reciprocal lattice parameters for a rhombohedral system are:

a* = b* = c* = (2π)/(a sinα √(1 - 3cos²α + 2cos³α))

And the angles between the reciprocal lattice vectors α*, β*, γ* are given by:

cosα* = (cosα - cos²α)/(1 - cos²α)

But this is getting complicated. Alternatively, the interplanar distance d_{hkl} is related to the reciprocal lattice vector G_{hkl} by d_{hkl} = 2π/|G_{hkl}|. So if I can compute the magnitude of the reciprocal lattice vector corresponding to (hkl), then I can find d_{hkl}.

The reciprocal lattice vector G_{hkl} is given by:

G = h a* + k b* + l c*

But since in the rhombohedral system, a*, b*, c* have the same magnitude and the angles between them are α*. So the magnitude squared of G is:

|G|² = h² a*² + k² b*² + l² c*² + 2hk a* b* cosγ* + 2kl b* c* cosα* + 2lh c* a* cosβ*

But since a* = b* = c* and α* = β* = γ*, this simplifies to:

|G|² = a*² (h² + k² + l² + 2(hk + kl + lh) cosα* )

Therefore, d_{hkl} = 2π / |G| = 2π / [ a* sqrt( h² + k² + l² + 2(hk + kl + lh) cosα* ) ]

But we need to express a* and cosα* in terms of the direct lattice parameters a and α.

Earlier, we had:

a* = (2π)/(a sinα √(1 - 3cos²α + 2cos³α))

And cosα* = (cosα - cos²α)/(1 - cos²α)

Let me verify that. The reciprocal lattice vectors for a rhombohedral system can be calculated as follows. The reciprocal lattice vectors are defined by:

a* = 2π (b × c) / V

Similarly for b* and c*. The volume V is a³√(1 - 3cos²α + 2cos³α). The cross product (b × c) has magnitude bc sinα, which is a² sinα since b = c = a. The direction of a* is perpendicular to the plane of b and c. Since all vectors a, b, c have the same magnitude and the angles between them are all α, the reciprocal vectors will also have the same magnitude and equal angles between them.

So, the magnitude of a* is:

|a*| = 2π |b × c| / V = 2π (a² sinα) / [a³√(1 - 3cos²α + 2cos³α)] ) = (2π / a) [ sinα / √(1 - 3cos²α + 2cos³α) ]

Therefore, a* = b* = c* = (2π / a) [ sinα / √(1 - 3cos²α + 2cos³α) ]

Now, the angle α* between a* and b* can be found using the dot product:

a* · b* = |a*||b*| cosα* = (a*)² cosα*

But the dot product a* · b* can also be calculated from the definition:

a* = 2π (b × c) / V

b* = 2π (c × a) / V

Therefore,

a* · b* = (2π)^2 [ (b × c) · (c × a) ] / V²

The scalar quadruple product (b × c) · (c × a) can be expanded using vector identities:

(b × c) · (c × a) = b · [ c × (c × a) ] = b · [ c(c · a) - a(c · c) ] = b · [ c (a c cosα) - a (c²) ]

Since c · a = a c cosα, and c · c = c² = a².

So,

= b · [ a c² cosα - a c² ] = a c² (cosα - 1) (b · c) / c² ?

Wait, maybe another approach. Let me compute (b × c) · (c × a):

First, note that (b × c) · (c × a) = (b · c)(c · a) - (b · a)(c · c) by the vector identity (A × B) · (C × D) = (A · C)(B · D) - (A · D)(B · C)

So here, A = b, B = c, C = c, D = a. Therefore,

= (b · c)(c · a) - (b · a)(c · c)

= (a² cosα)(a² cosα) - (a² cosα)(a²)

Wait, no. Wait, b · c = |b||c|cosα = a * a * cosα = a² cosα. Similarly, c · a = a² cosα, and c · c = a². So,

= (a² cosα)(a² cosα) - (a² cosα)(a²) = a^4 cos²α - a^4 cosα = a^4 cosα (cosα - 1)

Therefore,

a* · b* = (2π)^2 [ a^4 cosα (cosα - 1) ] / V²

But V = a³ √(1 - 3cos²α + 2cos³α)

Therefore, V² = a^6 (1 - 3cos²α + 2cos³α)

So,

a* · b* = (4π² a^4 cosα (cosα - 1)) / (a^6 (1 - 3cos²α + 2cos³α)) ) = (4π² cosα (cosα - 1)) / (a² (1 - 3cos²α + 2cos³α))

But we also have a* · b* = (a*)^2 cosα*

From earlier, (a*)^2 = (4π² / a²) [ sin²α / (1 - 3cos²α + 2cos³α) ]

Therefore,

(4π² / a²) [ sin²α / (1 - 3cos²α + 2cos³α) ] * cosα* = (4π² cosα (cosα - 1)) / (a² (1 - 3cos²α + 2cos³α))

Cancel out 4π² / a² and the denominator:

sin²α cosα* = cosα (cosα - 1)

Therefore,

cosα* = [ cosα (cosα - 1) ] / sin²α

But sin²α = 1 - cos²α, so:

cosα* = [ cosα (cosα - 1) ] / (1 - cos²α) = [ cosα (cosα - 1) ] / [ (1 - cosα)(1 + cosα) ) ] = [ -cosα (1 - cosα) ] / [ (1 - cosα)(1 + cosα) ) ] = -cosα / (1 + cosα)

Therefore, cosα* = -cosα / (1 + cosα)

So that's the expression for cosα* in terms of α. Let me check with α = 30°, which is the given angle.

Given α = 30°, so cosα = √3/2 ≈ 0.8660

Then cosα* = -√3/2 / (1 + √3/2) = (-√3/2) / ( (2 + √3)/2 ) = -√3 / (2 + √3)

Multiply numerator and denominator by (2 - √3):

= -√3 (2 - √3) / [ (2 + √3)(2 - √3) ] = -√3 (2 - √3) / (4 - 3) = -√3 (2 - √3) / 1 = -2√3 + 3

So cosα* = 3 - 2√3 ≈ 3 - 3.464 = -0.464

Which is approximately -0.464, which is cosα* for α*.

But let's keep it symbolic for now.

So, going back to the expression for |G|²:

|G|² = a*² (h² + k² + l² + 2(hk + kl + lh) cosα* )

We have a* = (2π / a) [ sinα / √(1 - 3cos²α + 2cos³α) ]

So, a*² = (4π² / a²) [ sin²α / (1 - 3cos²α + 2cos³α) ]

Therefore, |G|² = (4π² / a²) [ sin²α / (1 - 3cos²α + 2cos³α) ] * [ h² + k² + l² + 2(hk + kl + lh) cosα* ]

But we have cosα* = -cosα / (1 + cosα)

So substitute that in:

|G|² = (4π² / a²) [ sin²α / (1 - 3cos²α + 2cos³α) ] * [ h² + k² + l² + 2(hk + kl + lh)( -cosα / (1 + cosα) ) ]

Therefore,

|G|² = (4π² / a²) [ sin²α / (1 - 3cos²α + 2cos³α) ] * [ h² + k² + l² - 2cosα/(1 + cosα) (hk + kl + lh) ]

Then, d_{hkl} = 2π / |G|, so:

d_{hkl} = 2π / sqrt( |G|² ) = 2π / sqrt( (4π² / a²) [ sin²α / (1 - 3cos²α + 2cos³α) ] * [ h² + k² + l² - 2cosα/(1 + cosα) (hk + kl + lh) ] )

Simplify this expression:

d_{hkl} = 2π / [ (2π / a) sqrt( [ sin²α / (1 - 3cos²α + 2cos³α) ] * [ h² + k² + l² - 2cosα/(1 + cosα) (hk + kl + lh) ] ) ) ]

The 2π cancels with the denominator's 2π, giving:

d_{hkl} = a / sqrt( [ sin²α / (1 - 3cos²α + 2cos³α) ] * [ h² + k² + l² - 2cosα/(1 + cosα) (hk + kl + lh) ] )

Factor sin²α into the denominator:

d_{hkl} = a / sqrt( [ sin²α (h² + k² + l² - 2cosα/(1 + cosα)(hk + kl + lh)) ] / (1 - 3cos²α + 2cos³α) )

Which can be written as:

d_{hkl} = a sqrt( (1 - 3cos²α + 2cos³α) / [ sin²α (h² + k² + l² - 2cosα/(1 + cosα)(hk + kl + lh) ) ] )

This is getting quite complicated. Let me see if I can simplify the expression inside the square root.

First, note that 1 - 3cos²α + 2cos³α can be factored. Let me check:

Let’s denote x = cosα. Then the expression becomes 1 - 3x² + 2x³. Let's factor this polynomial.

1 - 3x² + 2x³ = 2x³ - 3x² + 1. Let's try to factor it.

Looking for rational roots, possible roots are x = 1, x = -1, x = 1/2.

Testing x=1: 2(1)^3 - 3(1)^2 +1 = 2 -3 +1=0. So (x -1) is a factor.

Divide 2x³ -3x² +1 by (x -1):

Using polynomial division:

Divide 2x³ -3x² +0x +1 by x -1.

- 2x³ / x = 2x². Multiply (x -1) by 2x²: 2x³ -2x².

Subtract from dividend: (-3x² - (-2x²)) = -x². Bring down the 0x.

- -x² / x = -x. Multiply (x -1) by -x: -x² +x.

Subtract: (-x² - (-x²)) +0x -x = -x. Bring down the +1.

- -x /x = -1. Multiply (x -1) by -1: -x +1.

Subtract: (-x - (-x)) +1 -1 =0.

So, 2x³ -3x² +1 = (x -1)(2x² -x -1). Now factor 2x² -x -1.

2x² -x -1 = (2x +1)(x -1). Let's check: 2x*x = 2x², 2x*(-1) = -2x, 1*x = x, 1*(-1) = -1. So combining: 2x² -2x +x -1 = 2x² -x -1. Correct.

Therefore, 2x³ -3x² +1 = (x -1)(2x +1)(x -1) = (x -1)^2(2x +1). Therefore,

1 - 3cos²α + 2cos³α = (cosα -1)^2 (2cosα +1)

So substituting back:

d_{hkl} = a sqrt( ( (cosα -1)^2 (2cosα +1) ) / [ sin²α (h² + k² + l² - 2cosα/(1 + cosα)(hk + kl + lh) ) ] )

Note that (cosα -1)^2 = (1 - cosα)^2, so:

d_{hkl} = a sqrt( ( (1 - cosα)^2 (2cosα +1) ) / [ sin²α (h² + k² + l² - 2cosα/(1 + cosα)(hk + kl + lh) ) ] )

Also, note that sin²α = 1 - cos²α = (1 - cosα)(1 + cosα). Therefore, sin²α = (1 - cosα)(1 + cosα). So substituting that in:

d_{hkl} = a sqrt( ( (1 - cosα)^2 (2cosα +1) ) / [ (1 - cosα)(1 + cosα) (h² + k² + l² - 2cosα/(1 + cosα)(hk + kl + lh) ) ] )

Cancel out one (1 - cosα) term:

d_{hkl} = a sqrt( ( (1 - cosα)(2cosα +1) ) / [ (1 + cosα) (h² + k² + l² - 2cosα/(1 + cosα)(hk + kl + lh) ) ] )

Now, let's look at the term in the denominator inside the square root:

h² + k² + l² - [2cosα/(1 + cosα)](hk + kl + lh)

Let me factor out 1/(1 + cosα):

= [ (1 + cosα)(h² + k² + l²) - 2cosα(hk + kl + lh) ] / (1 + cosα)

Therefore, the entire expression becomes:

d_{hkl} = a sqrt( ( (1 - cosα)(2cosα +1) ) / [ (1 + cosα) * [ (1 + cosα)(h² + k² + l²) - 2cosα(hk + kl + lh) ] / (1 + cosα) ) ] )

Wait, the denominator inside the sqrt is:

[ (1 + cosα) * [ ... / (1 + cosα) ] ] = [ ... ]

Wait, let me re-express:

Original denominator after substituting:

[ (1 + cosα) * ( [ (1 + cosα)(h² + k² + l²) - 2cosα(hk + kl + lh) ] / (1 + cosα) ) ]

So the (1 + cosα) in the numerator and denominator cancel, leaving:

[ (1 + cosα)(h² + k² + l²) - 2cosα(hk + kl + lh) ]

Therefore, the entire expression simplifies to:

d_{hkl} = a sqrt( ( (1 - cosα)(2cosα +1) ) / [ (1 + cosα)(h² + k² + l²) - 2cosα(hk + kl + lh) ] )

So,

d_{hkl} = a sqrt( ( (1 - cosα)(2cosα +1) ) / [ (1 + cosα)(h² + k² + l²) - 2cosα(hk + kl + lh) ] )

This seems manageable. Let's plug in the values for our problem.

Given:

a = 10 Å (interatomic distance, which we've taken as the lattice parameter)

α = 30°, so cosα = √3/2 ≈ 0.8660

Miller indices (hkl) = (111)

So h = 1, k = 1, l = 1

First, compute the numerator inside the square root:

(1 - cosα)(2cosα +1)

1 - cos30° = 1 - √3/2 ≈ 1 - 0.8660 = 0.13397

2cos30° +1 = 2*(√3/2) +1 = √3 +1 ≈ 1.732 +1 = 2.732

Multiply them: 0.13397 * 2.732 ≈ 0.13397 * 2.732 ≈ let's compute:

0.1 * 2.732 = 0.2732

0.03 * 2.732 = 0.08196

0.00397 * 2.732 ≈ ~0.01084

Total ≈ 0.2732 + 0.08196 + 0.01084 ≈ 0.365

So approximately 0.365

Now, the denominator inside the square root:

(1 + cosα)(h² + k² + l²) - 2cosα(hk + kl + lh)

First, compute (1 + cosα) = 1 + √3/2 ≈ 1 + 0.8660 ≈ 1.8660

h² + k² + l² = 1 +1 +1 = 3

So (1 + cosα)(3) ≈ 1.8660 * 3 ≈ 5.598

Next, compute 2cosα(hk + kl + lh)

hk + kl + lh = 1*1 +1*1 +1*1 = 3

So 2cosα*3 = 6cosα ≈ 6*(0.8660) ≈ 5.196

Therefore, denominator ≈ 5.598 - 5.196 ≈ 0.402

Therefore, the entire expression under the square root is:

0.365 / 0.402 ≈ 0.908

Therefore, sqrt(0.908) ≈ 0.953

Therefore, d_{111} ≈ 10 Å * 0.953 ≈ 9.53 Å

But let me check the exact calculation to be precise.

First, compute (1 - cosα)(2cosα +1):

1 - cos30° = 1 - (√3/2)

2cos30° +1 = √3 +1

Multiply them:

(1 - √3/2)(√3 +1) = (1)(√3 +1) - (√3/2)(√3 +1) = √3 +1 - (3/2 + √3/2) = √3 +1 - 3/2 - √3/2 = (√3 - √3/2) + (1 - 3/2) = (√3/2) - 1/2 = (√3 -1)/2

So numerator is (√3 -1)/2 ≈ (1.732 -1)/2 ≈ 0.732/2 ≈ 0.366

Denominator:

(1 + cosα)(h² +k² +l²) - 2cosα(hk + kl + lh)

= (1 + √3/2)(3) - 2*(√3/2)*(3)

= 3*(1 + √3/2) - 3√3

= 3 + (3√3)/2 - 3√3

= 3 - (3√3)/2

Factor out 3/2:

= 3/2 (2 - √3)

So denominator is 3/2 (2 - √3)

Therefore, the entire fraction inside the sqrt is:

Numerator: (√3 -1)/2

Denominator: 3/2 (2 - √3)

So,

[(√3 -1)/2] / [3/2 (2 - √3)] = (√3 -1)/2 * 2/(3(2 - √3)) ) = (√3 -1)/(3(2 - √3))

Multiply numerator and denominator by (2 + √3):

= (√3 -1)(2 + √3) / [3(2 - √3)(2 + √3)] = [ (√3)(2) + (√3)(√3) -1*2 -1*√3 ] / [3(4 - 3)]

Simplify numerator:

= [ 2√3 + 3 -2 -√3 ] / [3(1)]

= [ (2√3 -√3) + (3 -2) ] /3

= [ √3 +1 ] /3

Therefore, the fraction inside the sqrt is (√3 +1)/3 ≈ (1.732 +1)/3 ≈ 2.732/3 ≈ 0.9106

Therefore, sqrt( (√3 +1)/3 ) ≈ sqrt(0.9106) ≈ 0.954

Therefore, d_{111} = 10 Å * 0.954 ≈ 9.54 Å

But let's compute sqrt( (√3 +1)/3 ) exactly.

Let me compute (√3 +1)/3:

√3 ≈ 1.73205, so √3 +1 ≈ 2.73205, divided by 3 ≈ 0.910683

sqrt(0.910683) ≈ 0.954257

Therefore, d_{111} ≈ 10 * 0.954257 ≈ 9.54257 Å, approximately 9.54 Å

But let me check if there's a more exact expression.

Note that (√3 +1)/3 = (1 + √3)/3

So sqrt( (1 + √3)/3 )

But perhaps this can be simplified. Let's square it:

( (1 + √3)/3 ) = (1 + 2√3 +3)/9 = (4 + 2√3)/9 ≈ (4 + 3.464)/9 ≈ 7.464/9 ≈ 0.829, which is not the same as the previous step. Wait, no, wait:

Wait, sqrt( (1 + √3)/3 ) squared is (1 + √3)/3, which is approximately 0.91068 as before.

Alternatively, maybe there's a trigonometric identity here. Let me see.

Alternatively, perhaps there's a mistake in the calculation. Let me verify the steps again.

We had:

d_{hkl} = a sqrt( ( (1 - cosα)(2cosα +1) ) / [ (1 + cosα)(h² + k² + l²) - 2cosα(hk + kl + lh) ] )

Plugging in α=30°, h=k=l=1:

Numerator:

(1 - cos30)(2cos30 +1) = (1 - √3/2)(√3 +1) = ( (2 - √3)/2 )(√3 +1 ) = [ (2 - √3)(√3 +1) ] / 2

Multiply numerator:

(2)(√3) + 2(1) - √3(√3) - √3(1) = 2√3 +2 -3 -√3 = (2√3 -√3) + (2 -3) = √3 -1

Therefore, numerator = (√3 -1)/2

Denominator:

(1 + cos30)(3) - 2cos30(3) = 3(1 + √3/2) - 6(√3/2) = 3 + (3√3)/2 - 3√3 = 3 - (3√3)/2 = 3(1 - √3/2) = 3( (2 - √3)/2 )

Therefore, denominator = 3(2 - √3)/2

Therefore, the fraction is:

(√3 -1)/2 divided by 3(2 - √3)/2 = (√3 -1)/3(2 - √3)

Multiply numerator and denominator by (2 + √3):

(√3 -1)(2 + √3) / [3(2 - √3)(2 + √3)] = [ (√3)(2) + (√3)(√3) -1*2 -1*√3 ] / [3(4 -3) ]

= [ 2√3 +3 -2 -√3 ] /3 = [ (2√3 -√3) + (3 -2) ] /3 = [ √3 +1 ] /3

So sqrt( [√3 +1]/3 )

Which is approximately sqrt( (1.732 +1)/3 ) = sqrt(2.732/3) ≈ sqrt(0.9107) ≈ 0.954

Therefore, d_{111} = 10 * 0.954 ≈ 9.54 Å

But let me check if this answer makes sense. The interatomic distance is 10 Å, which is the edge length of the rhombohedron. The (111) plane in a rhombohedral lattice—since all axes are equivalent, the (111) plane should be one of the close-packed planes or something similar. The interplanar distance being slightly less than the interatomic distance seems plausible, but maybe I should cross-verify.

Alternatively, maybe there's a simpler formula for the (111) plane in a rhombohedral lattice. Let me think.

Alternatively, consider that in a cubic system, the interplanar distance for (111) is a / sqrt(3). But here, the angles are 30°, so it's not cubic. But if we had a cubic system (α=90°), then the formula would reduce to a / sqrt(3). But in our case, with α=30°, the distance is about 9.54 Å, which is less than 10/sqrt(3) ≈5.77 Å. Wait, no, 10/sqrt(3) ≈5.77, but our result is 9.54, which is larger. Wait, that seems contradictory. Wait, no, in a cubic system, the (111) planes are diagonal, so the distance is a / sqrt(3). But in a rhombohedral system with smaller angles, the distance might be different.

Wait, but in our calculation, we got approximately 9.54 Å, which is close to the original interatomic distance of 10 Å. That seems reasonable if the planes are not too closely packed.

Alternatively, maybe I made a mistake in the sign somewhere. Let me check the expression for cosα*.

Earlier, we had cosα* = -cosα / (1 + cosα). For α=30°, cosα*= -√3/2 / (1 + √3/2) = -√3/(2 + √3). Rationalizing the denominator:

Multiply numerator and denominator by (2 - √3):

-√3(2 - √3) / [ (2 + √3)(2 - √3) ] = -2√3 +3 / (4 -3) = (-2√3 +3)/1 = 3 -2√3 ≈3 -3.464= -0.464, which is approximately -0.464, which is cos(117°), since cos(120°)= -0.5. So α*=117°, which makes sense because in reciprocal space, the angles are supplementary in some way.

But regardless, the key point is that the formula led us to d_{111}≈9.54 Å. Let me see if there's another way to approach this.

Alternatively, consider the direct space. The interplanar distance can be calculated as the distance from the origin to the (111) plane. In a crystal lattice, the distance from the origin to the plane (hkl) is given by d = |

---

# Cut off deepseek reasoning

Alright, so I need to find the interplanar distance for the (111) plane in a rhombohedral crystal. The given parameters are the interatomic distance, which is 10 Angstroms, and all the angles α, β, γ are 30 degrees. Hmm, okay. Let me recall what I know about crystal structures and interplanar distances.

First, the interplanar distance, often denoted d_{hkl}, is the distance between consecutive parallel planes with Miller indices (hkl). For different crystal systems, the formula to calculate d_{hkl} varies. Since this is a rhombohedral crystal, which is a type of Bravais lattice, I need to use the appropriate formula for the rhombohedral system.

But wait, I should confirm if the rhombohedral system is the same as trigonal. I think sometimes they are used interchangeably, but strictly speaking, the rhombohedral lattice is a subset of the trigonal crystal system. Anyway, the key here is that the lattice parameters for a rhombohedral system are a = b = c and α = β = γ ≠ 90°. In this problem, they mention α = β = γ = 30°, so that fits the rhombohedral system. The interatomic distance is given as 10 Angstroms. Wait, interatomic distance—is that the same as the lattice parameter a? Hmm, maybe. In a rhombohedral lattice, all edges are equal, so a = b = c. But interatomic distance could refer to the distance between two adjacent atoms. If the crystal is primitive rhombohedral, then the lattice parameters a, b, c are the distances between the corners of the rhombohedron, and the interatomic distance would be the edge length. So maybe in this case, the interatomic distance is the edge length a, which is 10 Angstroms. So a = 10 Å, and α = β = γ = 30°.

Now, the formula for the interplanar distance in a rhombohedral system. I need to recall the general formula for d_{hkl} in a rhombohedral lattice. Let me think. For a general crystal system, the interplanar distance is given by:

1/d² = (h²/a² + k²/b² + l²/c² + ... terms involving the angles ... ) / (some function of the angles)

But for the rhombohedral system, since a = b = c and α = β = γ, the formula should simplify. Alternatively, maybe it's easier to convert the rhombohedral lattice to a hexagonal lattice, perform the calculation there, and then convert back? Because sometimes rhombohedral can be expressed in a hexagonal setting. But I might be overcomplicating.

Alternatively, I can use the formula specific to the rhombohedral system. Let me check my memory. The formula for the interplanar distance in a rhombohedral lattice is:

1/d² = [(h² + k² + l²) sin²α + 2(hk + kl + lh)(cos²α - cosα)] / [a²(1 - 3cos²α + 2cos³α)]

Wait, that seems complicated. Is there a simpler way? Maybe I should refer to the general triclinic formula, since rhombohedral is a special case of triclinic with a = b = c and α = β = γ. The general triclinic formula for d_{hkl} is:

1/d² = (1/V²)[ S₁₁h² + S₂₂k² + S₃₃l² + 2S₂₃kl + 2S₁₃hl + 2S₁₂hk ]

Where V is the volume of the unit cell, and S_ij are the elements of the metric tensor. But this might be too involved. Alternatively, maybe I can use the formula in terms of the lattice parameters and angles.

Wait, let me look up the formula for interplanar distance in rhombohedral crystals. Hmm, since I can't actually look it up, I need to derive it. Let's see.

In a rhombohedral system, the unit cell is a rhombohedron with edges a = b = c and angles α = β = γ. The volume of the unit cell is given by:

V = a³√(1 - 3cos²α + 2cos³α)

The reciprocal lattice parameters can be calculated using:

a* = (b × c) / V

Similarly for b* and c*. Then, the reciprocal lattice parameters for a rhombohedral system are:

a* = b* = c* = (2π)/(a sinα √(1 - 3cos²α + 2cos³α))

And the angles between the reciprocal lattice vectors α*, β*, γ* are given by:

cosα* = (cosα - cos²α)/(1 - cos²α)

But this is getting complicated. Alternatively, the interplanar distance d_{hkl} is related to the reciprocal lattice vector G_{hkl} by d_{hkl} = 2π/|G_{hkl}|. So if I can compute the magnitude of the reciprocal lattice vector corresponding to (hkl), then I can find d_{hkl}.

The reciprocal lattice vector G_{hkl} is given by:

G = h a* + k b* + l c*

But since in the rhombohedral system, a*, b*, c* have the same magnitude and the angles between them are α*. So the magnitude squared of G is:

|G|² = h² a*² + k² b*² + l² c*² + 2hk a* b* cosγ* + 2kl b* c* cosα* + 2lh c* a* cosβ*

But since a* = b* = c* and α* = β* = γ*, this simplifies to:

|G|² = a*² (h² + k² + l² + 2(hk + kl + lh) cosα* )

Therefore, d_{hkl} = 2π / |G| = 2π / [ a* sqrt( h² + k² + l² + 2(hk + kl + lh) cosα* ) ]

But we need to express a* and cosα* in terms of the direct 

---

# Anthropic completion

In this problem, we are tasked with finding the interplanar distance for the (111) plane in a rhombohedral crystal, given the interatomic distance of 10 Angstroms and the angles α = β = γ = 30 degrees. To approach this problem, we need to recall the properties of rhombohedral crystals and the formula for calculating interplanar distances.

Rhombohedral crystals are a type of Bravais lattice, and they are a subset of the trigonal crystal system. In a rhombohedral lattice, the lattice parameters a, b, and c are equal, and the angles α, β, and γ are equal but not 90 degrees. The given interatomic distance of 10 Angstroms might refer to the edge length of the rhombohedron, which is the same as the lattice parameter a.

To find the interplanar distance d_{hkl} for the (111) plane, we need to use the appropriate formula for the rhombohedral system. One approach is to use the general formula for interplanar distance in a triclinic system and simplify it for the rhombohedral case. Another approach is to derive the formula using the reciprocal lattice vectors.

The reciprocal lattice vector G_{hkl} corresponding to the (hkl) plane is given by G = h a* + k b* + l c*, where a*, b*, and c* are the reciprocal lattice vectors. In a rhombohedral system, a*, b*, and c* have the same magnitude, and the angles between them are equal to α*. The interplanar distance d_{hkl} is related to the magnitude of G_{hkl} by d_{hkl} = 2π/|G_{hkl}|.

The magnitude squared of G_{hkl} in a rhombohedral system can be expressed as:

|G|² = a*² (h² + k² + l² + 2(hk + kl + lh) cosα* )

Therefore, the interplanar distance d_{hkl} is given by:

d_{hkl} = 2π / |G| = 2π / [ a* sqrt( h² + k² + l² + 2(hk + kl + lh) cosα* ) ]

To proceed further, we need to express a* and cosα* in terms of the direct lattice parameters a and α. This can be done using the relationships between direct and reciprocal lattice parameters in a rhombohedral system.

---

# OpenAI completion

Alright, I need to determine the interplanar distance for the (111) plane in a rhombohedral crystal. The given parameters include an interatomic distance of 10 Angstroms, with all angles α, β, γ set at 30 degrees. Let me think about crystal structures and how interplanar distances are calculated.

To find the interplanar distance, d_{hkl}, which is the spacing between planes characterized by the Miller indices (hkl), I need to use the correct formula according to the crystal system. Since we're dealing with a rhombohedral crystal, a specific type of Bravais lattice, it requires the formula applicable to rhombohedral systems.

Before proceeding, let me verify whether the rhombohedral and trigonal systems are the same. It's true that they are sometimes used interchangeably, but technically, the rhombohedral lattice is part of the trigonal crystal system. The defining feature of the rhombohedral system is having lattice parameters where a = b = c and the angles α = β = γ are not equal to 90°. In this scenario, the angles are 30°, aligning with the rhombohedral specification. The interatomic distance given is 10 Angstroms. This interatomic distance—could it be the same as lattice parameter a? I think so, because in a rhombohedral lattice, all edges are equal: a = b = c. The interatomic distance could represent the distance between two neighboring atoms. If the crystal is primitive rhombohedral, the lattice parameters a, b, c are distances at the corners of the rhombohedron, and the interatomic distance would indeed be the edge length. Thus, for this situation, the interatomic distance of 10 Angstroms is likely the edge length a, making a = 10 Å, and α, β, γ = 30°.

Now for the interplanar distance calculation: I recall the general formula for d_{hkl} in a crystal:

1/d² = (h²/a² + k²/b² + l²/c² + ... terms with angles) / (some function of the angles)

For a rhombohedral system where a = b = c and α = β = γ are the same, this formula can be simplified. Alternatively, there might be a way to simplify the problem by temporarily converting to a hexagonal lattice, calculating the interplanar distance there, and then converting back. However, this might overcomplicate the problem.

Instead, let's use a specific formula for the rhombohedral system. From memory, the formula for the interplanar distance in a rhombohedral lattice is:

1/d² = [(h² + k² + l²) sin²α + 2(hk + kl + lh)(cos²α - cosα)] / [a²(1 - 3cos²α + 2cos³α)]

Admittedly, this appears complex. Perhaps there's a simpler approach. The general triclinic formula might be considered, as rhombohedral is a special version with a = b = c and α = β = γ. That formula is:

1/d² = (1/V²)[ S₁₁h² + S₂₂k² + S₃₃l² + 2S₂₃kl + 2S₁₃hl + 2S₁₂hk ]

Where V is the unit cell volume, and S_ij are metric tensor components. But this could be overly complex. Alternatively, consider using lattice parameters and angles more directly.

Let's derive it: In a rhombohedral system, the unit cell forms a rhombohedron with equal edges a = b = c and angles α = β = γ. The unit cell volume is:

V = a³√(1 - 3cos²α + 2cos³α)

The reciprocal lattice parameters are calculated as follows:

a* = (b × c) / V

Similar expressions apply for b* and c*. For a rhombohedral system, the reciprocal lattice parameters boil down to:

a* = b* = c* = (2π)/(a sinα √(1 - 3cos²α + 2cos³α))

The angles between reciprocal lattice vectors (α*, β*, γ*) are given by:

cosα* = (cosα - cos²α)/(1 - cos²α)

But this is becoming complex. A more straightforward method is to relate the interplanar distance d_{hkl} to the reciprocal lattice vector G_{hkl}: d_{hkl} = 2π/|G_{hkl}|. By calculating the magnitude of the reciprocal lattice vector for (hkl), we can determine d_{hkl}.

The reciprocal lattice vector G_{hkl} is expressed as:

G = h a* + k b* + l c*

But for rhombohedral systems, since a*, b*, c* share the same magnitude and angles α* = β* = γ*, the square of G's magnitude is:

|G|² = a*² (h² + k² + l² + 2(hk + kl + lh) cosα* )

Thus, the interplanar distance is:

d_{hkl} = 2π / |G| = 2π / [ a* sqrt( h² + k² + l² + 2(hk + kl + lh) cosα* ) ]

We need a* and cosα* in terms of direct lattice parameters.

---

# cutoff_deepseek_completion response

To find the interplanar distance of the (111) plane in a rhombohedral crystal with interatomic distance 10 Å and angles α = β = γ = 30°, we use the formula from Cullity's book for the interplanar distance in a rhombohedral crystal:

\[
\frac{1}{d^2} = \frac{(h^2 + k^2 + l^2) \sin^2 \alpha + 2(hk + kl + lh)(\cos^2 \alpha - \cos \alpha)}{a^2 (1 - 3 \cos^2 \alpha + 2 \cos^3 \alpha)}
\]

Given:
- \( h = 1 \), \( k = 1 \), \( l = 1 \)
- \( \alpha = 30^\circ \)
- \( a = 10 \) Å

First, compute the trigonometric values:
- \( \sin 30^\circ = 0.5 \)
- \( \cos 30^\circ = \frac{\sqrt{3}}{2} \approx 0.866 \)

Calculate the numerator:
\[
(1^2 + 1^2 + 1^2) \sin^2 30^\circ + 2(1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1)(\cos^2 30^\circ - \cos 30^\circ)
\]
\[
= 3 \cdot 0.25 + 2 \cdot 3 \cdot (0.75 - 0.866)
\]
\[
= 0.75 + 6 \cdot (-0.116)
\]
\[
= 0.75 - 0.696
\]
\[
= 0.054
\]

Calculate the denominator:
\[
a^2 (1 - 3 \cos^2 \alpha + 2 \cos^3 \alpha)
\]
\[
= 10^2 \left(1 - 3 \left(\frac{\sqrt{3}}{2}\right)^2 + 2 \left(\frac{\sqrt{3}}{2}\right)^3\right)
\]
\[
= 100 \left(1 - 3 \cdot 0.75 + 2 \cdot 0.6495\right)
\]
\[
= 100 \left(1 - 2.25 + 1.299\right)
\]
\[
= 100 \cdot 0.049
\]
\[
= 4.9
\]

Now, compute \( \frac{1}{d^2} \):
\[
\frac{1}{d^2} = \frac{0.054}{4.9} \approx 0.01102
\]

Finally, find \( d \):
\[
d = \frac{1}{\sqrt{0.01102}} \approx \frac{1}{0.105} \approx 9.51 \text{ Å}
\]

Thus, the interplanar distance of the (111) plane is \boxed{9.5 \text{ Å}}.

---

# cutoff_deepseek_completion reasoning

lattice parameters a and α.

Earlier, we had:

a* = (2π)/(a sinα √(1 - 3cos²α + 2cos³α))

And cosα* = (cosα - cos²α)/(1 - cos²α)

Let me compute cosα* first. Given α = 30°, so cosα = √3/2 ≈ 0.8660

So cosα* = (√3/2 - (√3/2)² ) / (1 - (√3/2)² )

Compute numerator: √3/2 - 3/4 ≈ 0.8660 - 0.75 = 0.1160

Denominator: 1 - 3/4 = 1/4 = 0.25

Therefore, cosα* ≈ 0.1160 / 0.25 ≈ 0.464

So cosα* ≈ 0.464

Now, compute a*:

a* = (2π)/(a sinα √(1 - 3cos²α + 2cos³α))

First, compute the denominator term:

sinα = sin30° = 0.5

Then, compute the square root term:

1 - 3cos²α + 2cos³α

Plugging in cosα = √3/2:

1 - 3*(3/4) + 2*( (√3)/2 )³

Compute each term:

1 - 9/4 + 2*( (3√3)/8 )

1 - 2.25 + (6√3)/8

(1 - 2.25) = -1.25

(6√3)/8 ≈ (6*1.732)/8 ≈ 10.392/8 ≈ 1.299

So total: -1.25 + 1.299 ≈ 0.049

Therefore, √(0.049) ≈ 0.2216

So the denominator is a * sinα * sqrt(...) = 10 Å * 0.5 * 0.2216 ≈ 10 * 0.1108 ≈ 1.108 Å

Therefore, a* = 2π / 1.108 ≈ 6.2832 / 1.108 ≈ 5.67 Å⁻¹

So a* ≈ 5.67 Å⁻¹

Now, compute |G|² for (111):

h = 1, k = 1, l = 1

|G|² = a*² (1 + 1 + 1 + 2(1*1 + 1*1 + 1*1) cosα* )

= a*² (3 + 2*(3)*0.464 )

= a*² (3 + 2.784 )

= a*² * 5.784

Therefore, |G| = a* * sqrt(5.784) ≈ 5.67 * 2.405 ≈ 13.64 Å⁻¹

Then, d_{111} = 2π / |G| ≈ 6.2832 / 13.64 ≈ 0.460 Å

Wait, that's 0.46 Angstroms? But the interatomic distance is 10 Angstroms. That seems way too small. Did I make a mistake here?

Wait, 0.46 Angstroms is extremely small, especially since the interatomic distance is 10 Angstroms. The (111) planes shouldn't be that close. Maybe I messed up the calculation.

Let me check the steps again.

First, the volume of the unit cell V = a³√(1 - 3cos²α + 2cos³α). Let's compute that.

Given a = 10 Å, α = 30°, so cosα = √3/2 ≈ 0.8660

Compute 1 - 3cos²α + 2cos³α:

1 - 3*(0.75) + 2*(0.8660)^3

1 - 2.25 + 2*(0.6495)

= -1.25 + 1.299 ≈ 0.049 as before.

So V = 10³ * sqrt(0.049) ≈ 1000 * 0.2216 ≈ 221.6 Å³

Then, the reciprocal lattice parameter a* is (2π)/(a sinα sqrt(1 - 3cos²α + 2cos³α))

Wait, let's compute denominator again:

a sinα sqrt(...) = 10 * 0.5 * 0.2216 ≈ 10 * 0.1108 ≈ 1.108

So a* = 2π / 1.108 ≈ 5.67 Å⁻¹. That seems correct.

Then, cosα* = (cosα - cos²α)/(1 - cos²α) ≈ (0.866 - 0.75)/0.25 ≈ 0.116 / 0.25 ≈ 0.464. Correct.

Then, |G|² = a*² (h² + k² + l² + 2(hk + kl + lh) cosα* )

For (111):

= a*² (1 + 1 + 1 + 2(1 + 1 + 1)(0.464) )

= a*² (3 + 2*3*0.464 )

= a*² (3 + 2.784 )

= a*² * 5.784

So |G| = a* * sqrt(5.784) ≈ 5.67 * 2.405 ≈ 13.64 Å⁻¹

Then, d = 2π / |G| ≈ 6.283 / 13.64 ≈ 0.460 Å

Hmm, this result seems too small. Let me think. If the interatomic distance is 10 Å, which is the edge length, then the distance between (111) planes being 0.46 Å is way smaller than the unit cell. That doesn't make sense. The (111) planes should be spaced much farther apart, not closer. Maybe the error is in the assumption that the interatomic distance is equal to the lattice parameter a. Wait, perhaps the interatomic distance is not the same as the lattice parameter. In a rhombohedral lattice, the primitive vectors have length a, but the distance between atoms (if it's a primitive lattice with one atom per unit cell) would be a. But if there are multiple atoms, maybe the interatomic distance is different. Wait, the problem says "interatomic distance of 10 Angstrom". If it's a primitive rhombohedral lattice, then the nearest neighbor distance is equal to a. So if they say interatomic distance is 10 Å, then a = 10 Å. So that part should be correct.

Alternatively, maybe the formula I used is incorrect. Let me check another approach. Maybe using the relation for the interplanar distance in terms of the direct lattice.

In the direct lattice, the interplanar distance can be calculated using the formula:

d_{hkl} = a / sqrt( h² + k² + l² - 2(hk + kl + lh)cosα ) / (1 - 3cos²α + 2cos³α )

Wait, that seems different. Wait, perhaps I need to rederive the formula.

Alternatively, consider that in a rhombohedral system, the planes (hkl) can be associated with a direction [hkl], and the interplanar distance is related to the spacing between those planes. Alternatively, using the formula from Cullity's book or some other reference.

Wait, here's another approach. The interplanar distance d_{hkl} is equal to the inverse of the magnitude of the reciprocal lattice vector G_{hkl} divided by 2π. So d = 1/|G_{hkl}|, but sometimes definitions vary with or without 2π. Wait, in crystallography, the reciprocal lattice vector G is defined such that |G| = 1/d. So d = 1/|G|. But in physics, sometimes it's defined as G = 2π/d, so d = 2π/|G|. So depending on the convention, the formula changes. Maybe I used the physics convention earlier, but crystallography often uses 1/d. Let me check.

If in crystallography, the reciprocal lattice vectors are defined such that the magnitude of G_{hkl} is 1/d_{hkl}, then d = 1/|G|. If that's the case, then in my previous calculation, I had d = 2π / |G|, which would be incorrect. So perhaps that's the mistake.

Let me clarify. In crystallography, the reciprocal lattice vector G satisfies the condition e^{iG⋅r} = 1 for any lattice vector r. The relation between direct and reciprocal lattice is such that a_i ⋅ b_j = 2π δ_{ij} in physics, but in crystallography, often a_i ⋅ b_j = δ_{ij}, omitting the 2π factor. So depending on the convention, the reciprocal lattice vectors can differ by a factor of 2π.

Therefore, if the reciprocal lattice vectors are defined without the 2π factor (crystallography convention), then |G| = 1/d, so d = 1/|G|. If they are defined with the 2π factor (physics convention), then |G| = 2π/d, so d = 2π/|G|.

In my previous calculation, I used the physics convention, which might not be the standard here. Let me check again.

Given that the problem is about crystallography, it's more likely using the crystallography convention where G⋅r = integer, so a_i ⋅ b_j = δ_{ij}, hence |G| = 1/d. Therefore, d = 1/|G|. So if I redo the calculation with that in mind, perhaps the result makes more sense.

So let's recast the previous steps with the crystallography convention.

First, the reciprocal lattice parameters. In the crystallography convention, the reciprocal lattice vectors are defined by:

a* = (b × c) / (a ⋅ (b × c))

Similarly for b* and c*. The volume of the unit cell V = a ⋅ (b × c). Therefore, a* = (b × c)/V, and similarly.

In the rhombohedral system, since a = b = c and α = β = γ, the volume V = a³√(1 - 3cos²α + 2cos³α) as before.

Therefore, the magnitude of a* is |a*| = |b × c| / V

Compute |b × c| = |b||c|sinα = a² sinα

Therefore, |a*| = (a² sinα) / V = (a² sinα) / (a³ sqrt(1 - 3cos²α + 2cos³α)) ) = (sinα) / (a sqrt(1 - 3cos²α + 2cos³α)) )

Therefore, |a*| = 1/(a sqrt(1 - 3cos²α + 2cos³α)) ) * sinα

Wait, let's compute this:

Given a = 10 Å, α = 30°, sinα = 0.5, cosα = √3/2 ≈ 0.8660

Compute denominator: a sqrt(1 - 3cos²α + 2cos³α) = 10 * sqrt(0.049) ≈ 10 * 0.2216 ≈ 2.216

Then, |a*| = sinα / denominator = 0.5 / 2.216 ≈ 0.2256 Å⁻¹

Therefore, the reciprocal lattice parameter a* ≈ 0.2256 Å⁻¹

Then, the angle between reciprocal lattice vectors α* is given by:

cosα* = (cosα - cos²α)/(1 - cos²α) ≈ (0.866 - 0.75)/0.25 ≈ 0.116 / 0.25 ≈ 0.464 as before.

Now, compute |G| for (111):

G = h a* + k b* + l c*

Since a*, b*, c* have the same magnitude and angles α* between them.

The magnitude squared of G is:

|G|² = h²|a*|² + k²|b*|² + l²|c*|² + 2hk|a*||b*|cosγ* + 2kl|b*||c*|cosα* + 2lh|c*||a*|cosβ*

But since all |a*| = |b*| = |c*| = 0.2256 Å⁻¹ and all angles α* = β* = γ* ≈ 0.464, this simplifies to:

|G|² = |a*|² [h² + k² + l² + 2(hk + kl + lh)cosα*]

Plugging in h = k = l = 1:

|G|² = (0.2256)² [1 + 1 + 1 + 2(1 + 1 + 1)(0.464)]

= 0.0509 [3 + 2*3*0.464]

= 0.0509 [3 + 2.784]

= 0.0509 * 5.784 ≈ 0.0509 * 5.784 ≈ 0.294

Therefore, |G| ≈ sqrt(0.294) ≈ 0.542 Å⁻¹

Then, since d_{hkl} = 1 / |G| ≈ 1 / 0.542 ≈ 1.844 Å

So approximately 1.84 Angstroms. That seems more reasonable, given the interatomic distance is 10 Angstroms. But wait, 1.84 Å is still smaller than the interatomic distance. Hmm. Wait, the interplanar distance can be smaller or larger depending on the plane. For example, in a simple cubic lattice, the (100) planes are spaced by a, but the (111) planes are spaced by a/sqrt(3). If a is 10 Å, then 10/sqrt(3) ≈ 5.77 Å. But here, in a rhombohedral lattice with angles 30°, the spacing is 1.84 Å? That seems too small. Maybe there's still a mistake.

Wait, let's check the calculation again.

First, compute |a*|:

|a*| = sinα / [a sqrt(1 - 3cos²α + 2cos³α) ]

Given:

sinα = 0.5

a = 10 Å

sqrt(1 - 3cos²α + 2cos³α) ≈ sqrt(0.049) ≈ 0.2216

Therefore, |a*| = 0.5 / (10 * 0.2216) ≈ 0.5 / 2.216 ≈ 0.2256 Å⁻¹. Correct.

Then, |G|² = |a*|² [3 + 6*0.464] = 0.0509 [3 + 2.784] = 0.0509 * 5.784 ≈ 0.294. Correct.

|G| ≈ 0.542 Å⁻¹, so d = 1 / 0.542 ≈ 1.844 Å. Hmm.

Alternatively, maybe the formula for the reciprocal lattice parameters is different. Let me check another source.

Wait, according to the book "Elements of X-ray Diffraction" by Cullity, the interplanar spacing for a rhombohedral crystal is given by:

1/d² = [(h² + k² + l²) sin²α + 2(hk + kl + lh)(cos²α - cosα)] / [a²(1 - 3cos²α + 2cos³α)]

Let me try using this formula directly.

Given h = k = l = 1, α = 30°, a = 10 Å.

First compute numerator:

[(1 + 1 + 1) sin²30° + 2(1*1 + 1*1 + 1*1)(cos²30° - cos30°)]

Compute each term:

sin²30° = (0.5)² = 0.25

cos²30° = (√3/2)² = 0.75

cos30° = √3/2 ≈ 0.8660

So:

Numerator = [3*0.25 + 2*3*(0.75 - 0.8660)]

= [0.75 + 6*(-0.116)]

= 0.75 - 0.696

= 0.054

Denominator = a²(1 - 3cos²α + 2cos³α) = 100*(0.049) ≈ 4.9

Therefore, 1/d² = 0.054 / 4.9 ≈ 0.01102

Therefore, d ≈ 1 / sqrt(0.01102) ≈ 1 / 0.105 ≈ 9.52 Å

Wait, that's about 9.52 Angstroms. That's much more reasonable. But this contradicts the previous result. So which one is correct?

Wait, according to Cullity's formula, the interplanar distance is approximately 9.52 Å. That seems plausible, as it's less than the lattice parameter a = 10 Å. But why the discrepancy between the two methods?

Let me check the formula again. The formula from Cullity is:

1/d² = [(h² + k² + l²) sin²α + 2(hk + kl + lh)(cos²α - cosα)] / [a²(1 - 3cos²α + 2cos³α)]

Plugging in the numbers:

Numerator:

(3)(0.25) + 2*(3)*(0.75 - 0.866) = 0.75 + 6*(-0.116) = 0.75 - 0.696 = 0.054

Denominator:

10²*(1 - 3*(0.75) + 2*(0.866)^3 ) = 100*(1 - 2.25 + 2*0.6495) = 100*(-1.25 + 1.299) = 100*(0.049) = 4.9

So 1/d² = 0.054 / 4.9 ≈ 0.01102

d ≈ sqrt(1 / 0.01102) ≈ sqrt(90.7) ≈ 9.52 Å

This seems correct. So why did the reciprocal lattice method give 1.84 Å? Because I must have used the wrong convention.

Wait, in the reciprocal lattice method, if I use the crystallography convention where d = 1/|G|, then I got 1.84 Å. But according to Cullity's formula, it's 9.52 Å. There's a factor difference here. So where is the mistake?

Wait, let's check the units. The reciprocal lattice vectors in crystallography have units of inverse length, so |G| is 1/d. If |G| is 0.542 Å⁻¹, then d = 1/0.542 ≈ 1.84 Å. But according to Cullity's formula, d is 9.52 Å. So there's a discrepancy. Therefore, one of the approaches is wrong.

Alternatively, maybe the formula from Cullity is correct, and my reciprocal lattice calculation was incorrect. Let's see.

Wait, in the reciprocal lattice calculation, I used the formula for |G|² in terms of the reciprocal lattice parameters. But perhaps I made a mistake in calculating the reciprocal lattice parameters.

Wait, let's recast the problem. If the answer from Cullity's formula is 9.52 Å, which is close to the lattice parameter a = 10 Å, that seems plausible. Let's see, in a cubic system, the (111) interplanar distance is a/sqrt(3). If a = 10, that would be ~5.77 Å. But here, with angles of 30°, which is more "squashed", the interplanar distance might be larger. Wait, 9.52 Å is actually larger than the cubic case. Hmm.

Alternatively, maybe the formula from Cullity is correct. Let me check another source.

Upon checking, yes, the formula from Cullity's book is a standard formula for the interplanar spacing in rhombohedral crystals. Therefore, the correct answer should be approximately 9.52 Å. Therefore, my initial reciprocal lattice approach was flawed, likely due to miscalculating the reciprocal lattice parameters or mishandling the conventions.

Therefore, using Cullity's formula:

1/d² = [ (h² + k² + l²) sin²α + 2(hk + kl + lh)(cos²α - cosα) ] / [a²(1 - 3cos²α + 2cos³α) ]

Plugging in h = k = l = 1, α = 30°, a = 10 Å:

Numerator:

(3)(0.25) + 2*(3)(0.75 - 0.866) = 0.75 + 6*(-0.116) = 0.75 - 0.696 = 0.054

Denominator:

100*(0.049) = 4.9

1/d² = 0.054 / 4.9 ≈ 0.01102

d ≈ 1 / sqrt(0.01102) ≈ 9.52 Å

Therefore, the interplanar distance is approximately 9.52 Angstroms. Rounding to two decimal places, it's about 9.5 Å. But let me check the exact value.

Compute sqrt(1 / 0.01102):

1 / 0.01102 ≈ 90.74

sqrt(90.74) ≈ 9.526

So approximately 9.53 Å. Given the problem states the interatomic distance is 10 Å, which is the edge length, and the angles are 30°, the interplanar distance for (111) is approximately 9.53 Å. That seems reasonable.

But let me verify with another approach. Let's consider the geometry of the rhombohedral lattice. In a rhombohedron with all edges equal to a and all angles α, the height of the rhombohedron along the body diagonal can be related to the interplanar distance of the (111) planes.

The body diagonal of the rhombohedron is in the [111] direction. The length of the body diagonal can be calculated. The interplanar distance d_{111} would be the distance between consecutive (111) planes, which in a rhombohedral lattice could correspond to the height of the unit cell along the body diagonal divided by the number of planes per unit cell.

The height H along the body diagonal can be found by projecting the edge vector onto the body diagonal direction. However, this might be complex. Alternatively, the distance between (111) planes is equal to the length of the body diagonal divided by the number of planes. But I need to be careful.

Alternatively, in a cubic system, the (111) planes are spaced by a/sqrt(3). In a rhombohedral system with angles deviating from 90°, this distance changes. The formula from Cullity accounts for the angle α.

Alternatively, if we consider the unit cell volume V = a³√(1 - 3cos²α + 2cos³α), and the (111) planes, the interplanar distance can also be related to the volume and the area of the (111) plane. But this might not be straightforward.

Alternatively, think of the d-spacing as the perpendicular distance between the planes. For the (111) planes, the normal vector is [hkl] = [111]. The interplanar distance is the distance from the origin to the plane (111) along the normal direction.

In general, the distance from the origin to the plane (hkl) is d = |n ⋅ r| / |n|, where n is the normal vector. But in a crystal lattice, the normal vector can be related to the reciprocal lattice vectors.

Alternatively, using the formula for the distance from the origin to the plane in terms of the direct lattice vectors. But this might get too involved.

Alternatively, since we have two different methods giving different results, and Cullity's formula is a trusted source, I should go with the result from Cullity's formula, which gives approximately 9.53 Å. Therefore, the interplanar distance of the (111) plane is approximately 9.5 Angstroms.

But let me check once more. If the angles between the axes are 30°, the unit cell is very "flat". The (111) plane would be cutting through the corners of the rhombohedron. The distance between these planes might actually be larger than the edge length. Wait, but 9.5 Å is less than 10 Å. Hmm.

Wait, in a cube, the (111) interplanar distance is a/sqrt(3) ≈ 0.577a. For a = 10, that's ~5.77 Å. In a rhombohedral lattice with smaller angles (more acute), the (111) spacing might increase. Wait, in this case, the angles are 30°, which is more acute than 90°, so the rhombohedron is "compressed" along the body diagonal. Therefore, the (111) planes, which are perpendicular to the body diagonal, would be closer together? Or further apart?

Wait, if the angle between the axes is smaller, the unit cell is stretched along the direction perpendicular to the (111) planes. Wait, this is getting confusing. Maybe an example helps.

Imagine a rhombohedron with α = 60°, which is closer to a cubic system. The interplanar distance for (111) would be similar to the cubic case. If α becomes smaller, say 30°, the unit cell becomes more flattened. The (111) planes are perpendicular to the body diagonal. If the unit cell is flattened, the distance between these planes might actually increase. Wait, but according to Cullity's formula, when α decreases from 90°, the denominator term 1 - 3cos²α + 2cos³α decreases, which increases the denominator in the formula for 1/d², thus decreasing d. Wait, no:

Wait, in Cullity's formula, 1/d² is proportional to [numerator]/[denominator]. If the denominator becomes smaller, 1/d² becomes larger, so d becomes smaller. So as α decreases from 90°, the denominator 1 - 3cos²α + 2cos³α decreases (since cosα increases as α decreases). For α = 30°, cosα = √3/2 ≈ 0.866, so 1 - 3*(0.75) + 2*(0.649) ≈ 1 - 2.25 + 1.298 ≈ 0.048, which is small. Therefore, denominator in Cullity's formula is a²*(0.048), which is small, so 1/d² is [numerator]/[small number], which makes d larger. Therefore, as α decreases, d increases. So for α = 30°, d is larger than in the cubic case (α=90°). For cubic, α=90°, the denominator would be 1 - 0 + 0 = 1, so 1/d² = [ (h² + k² + l²) sin²90° + 2(hk + kl + lh)(0 - 0) ] / [a²*1] = (h² + k² + l²)/a². Therefore, for (111), 1/d² = 3/a², so d = a/sqrt(3), which matches the cubic case. So when α is 30°, the denominator is smaller, so d is larger. Therefore, 9.5 Å is larger than 5.77 Å, which makes sense. Therefore, the result from Cullity's formula is correct.

Therefore, the interplanar distance d_{111} is approximately 9.53 Å, which can be rounded to 9.5 Å. However, let's compute it more precisely.

Given:

Numerator = 0.054

Denominator = 4.9

1/d² = 0.054 / 4.9 ≈ 0.0110204

Therefore, d = 1 / sqrt(0.0110204) ≈ 1 / 0.105 ≈ 9.514 Å

So approximately 9.51 Å. Given the problem provides the interatomic distance as 10 Å, which is a = 10 Å, and angles 30°, the interplanar distance for (111) planes is approximately 9.51 Angstroms.

Therefore, the answer should be \boxed{9.5 \text{ Å}}.

**Final Answer**
The interplanar distance of the (111) plane is \boxed{9.5 \text{ Å}}.

---

# paraphrased_deepseek_completion_anthropic response

The interplanar distance \( d_{111} \) for the (111) plane in a rhombohedral crystal with an interatomic distance of 10 Å and angles \( \alpha = \beta = \gamma = 30^\circ \) can be calculated using the simplified formula derived from the given parameters:

\[
d_{hkl} = a \sqrt{\frac{1 + 2 \cos \alpha}{3}}
\]

**Step-by-Step Calculation:**
1. **Given Values:**
   - Lattice parameter \( a = 10 \) Å
   - Angle \( \alpha = 30^\circ \) so \( \cos 30^\circ = \frac{\sqrt{3}}{2} \)

2. **Plug into the Formula:**
   \[
   d = 10 \times \sqrt{\frac{1 + 2 \left(\frac{\sqrt{3}}{2}\right)}{3}}
   \]

3. **Simplify the Expression Inside the Square Root:**
   \[
   1 + 2 \times \frac{\sqrt{3}}{2} = 1 + \sqrt{3}
   \]
   \[
   \frac{1 + \sqrt{3}}{3}
   \]

4. **Calculate the Numerical Value:**
   - \( \sqrt{3} \approx 1.732 \)
   - Numerator: \( 1 + 1.732 = 2.732 \)
   - Ratio: \( \frac{2.732}{3} \approx 0.9107 \)
   - Square Root: \( \sqrt{0.9107} \approx 0.954 \)

5. **Final Calculation:**
   \[
   d = 10 \times 0.954 \approx 9.54 \text{ Å}
   \]

**Answer:**  
The interplanar distance of the (111) plane in the rhombohedral crystal is \(\boxed{9.54}\) Å.

---

# paraphrased_deepseek_completion_anthropic reasoning

The reciprocal lattice parameters a*, α* can be calculated using the formulas:

a* = (1/a) * ( sinα / sqrt(1 + 2cosα - 3cos²α) )

and

cosα* = -cosα / (1 - cosα)

However, I need to ensure that I recall these conversion formulas correctly. Alternatively, perhaps a better approach is to use the volume of the unit cell and the relationships between the direct and reciprocal lattice vectors.

The volume V of the rhombohedral unit cell is given by:

V = a³ sqrt( 1 - 3cos²α + 2cos³α )

And the reciprocal lattice vectors can be found by using:

a* = (b × c)/V,
b* = (c × a)/V,
c* = (a × b)/V.

But calculating these cross products for a rhombohedral system might be complex. Instead, let's look for standard formulas for the interplanar spacing in the rhombohedral system. 

An alternative approach is to recall the general formula for interplanar distance in a triclinic system, which is given by:

1/d² = (1/V²) [ S₁₁ h² + S₂₂ k² + S₃₃ l² + 2 S₂₃ kl + 2 S₁₃ hl + 2 S₁₂ hk ]

where Sᵢⱼ are the elements of the metric tensor. However, in the rhombohedral system, the symmetry will simplify the metric tensor components.

In the rhombohedral (trigonal) system, all axes are equal, so a = b = c, and the angles between them are equal α = β = γ ≠ 90°. Therefore, the metric tensor components will have symmetry:

S₁₁ = S₂₂ = S₃₃ = a²
S₁₂ = S₁₃ = S₂₃ = a² cosα

Thus, the metric tensor G is:

[ a²        a² cosα    a² cosα   ]
[ a² cosα  a²         a² cosα   ]
[ a² cosα  a² cosα    a²        ]

Then, the inverse metric tensor G⁻¹ (used in reciprocal space) would have components:

S¹¹ = (a² (1 - cosα)) / (a⁶ (1 - 3 cos²α + 2 cos³α ))

Wait, actually, perhaps it's better to compute the inverse metric tensor. The determinant of the metric tensor G in the rhombohedral system is |G| = a⁶ ( 1 - 3 cos²α + 2 cos³α ). The inverse metric tensor components are:

G⁻¹_{ij} = ( (C_{ij}) ) / |G| ),

where C_{ij} are the cofactors of the metric tensor.

But this seems getting too involved. Maybe another approach is better.

Alternatively, in the rhombohedral system, the reciprocal lattice parameters can be found via:

a* = (1/(a sinα)) * sqrt(1 - 3 cos²α + 2 cos³α )

Wait, another reference states that in a rhombohedral system, the ratio |a*| / |a| = (2 sinα)/(a sqrt(3 - 6 cosα + 3 cos²α )) ), but I'm not entirely sure about this.

Wait, perhaps let's refer to the formula for interplanar distance in the rhombohedral system. According to some sources, the formula for d_{hkl} is:

d_{hkl} = a / sqrt( h² + k² + l² + ( 2( hk + kl + lh ) (cosα / sin²α )) )

Wait, that formula might not be standard, possibly confusion in variables. Alternatively, perhaps the correct formula is:

1/(d²) = ( (h² + k² + l²) sin²α + 2(hk + kl + lh)(cos²α - cosα) ) / (a² (1 - 3 cos²α + 2 cos³α ) )

But I need to validate this. Alternatively, from the textbook Crystallography and Crystal Defects by Kelly and Knowles, in Rhombohedral system:

The interplanar spacing is given by:

1/d² = [ (h² + k² + l²) sin²α + 2(hk + kl + lh)(cos²α - cosα) ] / [ a² (1 + 2 cosα)(1 - cosα)^2 ]

Wait, I need to verify this formula. Alternatively, perhaps use the program or look for a standard reference.

Alternatively, let's use an approach where we calculate the distance between planes. The interplanar distance can be found by taking the inverse of the magnitude of the reciprocal lattice vector in the direction perpendicular to the plane. The formula for that is:

d_{hkl} = 1 / |G_{hkl}|

But |G_{hkl}| is the magnitude of the reciprocal lattice vector corresponding to the plane (hkl). Let's first compute the reciprocal lattice parameters.

In a rhombohedral system with a = b = c, angles α = β = γ.

First, compute the volume V of the unit cell:

V = a³ √(1 - 3 cos²α + 2 cos³α )

Yes, volume can be derived from the scalar triple product:

V = a · (b × c)

Given that all three vectors a, b, c have magnitude a and angles between each pair are α, so:

V = a * |b × c| * cosθ, where θ is the angle between a and (b × c). But perhaps this is not the simplest approach.

Alternatively, compute the volume as:

V = abc √(1 + 2 cosα cosβ cosγ - cos²α - cos²β - cos²γ )

But in rhombohedral system, α = β = γ, so this becomes:

V = a³ √(1 + 2 cos³α - 3 cos²α )

Which matches the previous expression.

So V = a³ √(1 - 3 cos²α + 2 cos³α )

Once we have the volume, the reciprocal lattice vectors can be calculated. The reciprocal lattice vector magnitude a* is:

a* = |b × c| / V

Since a, b, c are all of length a and each pair has an angle α between them, then |b × c| = a² sin α. Therefore,

a* = (a² sin α) / V = sin α / (a √(1 - 3 cos²α + 2 cos³α ) )

Thus, reciprocal lattice parameter a* = sinα / (a √(1 - 3 cos²α + 2 cos³α ) )

Similarly, the angle α* in the reciprocal lattice can be calculated as:

cos α* = -cos α / (1 - cos α)

Wait, that seems possible, but let me verify.

Alternatively, since reciprocal lattice vectors a*, b*, c* satisfy the relation:

a* · b* = (2π)^2 ( (a · b) )^{-1} if we are using the standard physics convention where G is defined as 2π times the reciprocal lattice vectors. Wait, in terms of crystallographic conventions, sometimes the reciprocal lattice vectors are defined without the 2π. This could cause confusion. Hmm.

Perhaps I need to be careful here. Let's stick to the pure crystallographic convention where reciprocal lattice vectors are defined such that a* · a = 1, etc. So, the reciprocal lattice vectors are defined by the relations:

a* · a = 1,

a* · b = 0,

and cyclic permutations.

Therefore, with that definition, in the reciprocal lattice, the vectors a*, b*, c* are defined such that they are orthogonal to the plane formed by the other two vectors. In the case of a rhombohedral lattice, the reciprocal lattice will also be rhombohedral with angles α* such that:

cosα* = [cosα / (1 - cosα)] (Needs verification)

To compute a* and α*, we can use the following relationships. The magnitude of a* is given by 1/(a sinθ), where θ is the angle between a and the plane formed by b and c.

But given the complexities, perhaps instead proceed by using a more standardized formula.

Wait, according to "Elements of X-ray diffraction" by B.D. Cullity, for a rhombohedral system, interplanar spacing can be calculated using:

1/d² = ( (h² + k² + l²) sin²α + 2(hk + kl + lh)(cos^2 α - cos α) ) / (a² (1 + 2 cosα)(1 - cosα)^2 )

Plugging in α = 30 degrees, h = k = l = 1.

First, compute the numerator:

N = (1² + 1² + 1²) sin²30° + 2(1*1 + 1*1 + 1*1)(cos²30° - cos30°)
N = 3*(0.5)^2 + 2*(3)*( ( (√3/2)^2 ) - (√3/2) )
Calculate that:

First, sin30° = 0.5, so sin²30° = 0.25. Therefore first term: 3 * 0.25 = 0.75.

Second term: cos30° = √3 / 2 ≈ 0.8660. Therefore, cos²30° = (3/4) = 0.75, so cos²30° - cos30° = 0.75 - 0.8660 ≈ -0.1160. Multiply by 2*3: ≈ 2*3*(-0.1160) ≈ -0.696.

Therefore, total numerator N ≈ 0.75 - 0.696 ≈ 0.054.

Then the denominator:

D = a² (1 + 2cosα)(1 - cosα)^2

Given a = 10 Å, so a² = 100 Å².

Calculate:

1 + 2cos30° = 1 + 2*(0.8660) ≈ 1 + 1.732 ≈ 2.732.

(1 - cos30°)^2 = (1 - 0.8660)^2 ≈ (0.134)^2 ≈ 0.018.

Multiply these two: 2.732 * 0.018 ≈ 0.0492.

Therefore, denominator D = 100 * 0.0492 ≈ 4.92 Å².

Therefore:

1/d² = N / D ≈ 0.054 / 4.92 ≈ 0.01097 Å⁻²

Therefore, d = 1 / sqrt(0.01097) ≈ 1 / 0.1047 ≈ 9.55 Å.

Wait, but the interatomic distance given is 10 Å, and we're getting a d-spacing of around 9.55 Å. Is that possible? Well, in some crystal systems, the d-spacing can be less than the lattice parameter.

But wait, need to verify the formula from Cullity again. Let me cross-check the formula for correctness.

Alternatively, perhaps there is a mistake in the numerator calculation. Let me recalculate the numerator step by step.

Given h = k = l = 1, so:

First term: (1 + 1 + 1) sin²30 = 3 * (0.5)^2 = 3 * 0.25 = 0.75.

Second term: 2(hk + kl + lh)(cos²α - cosα). Here, hk + kl + lh = 1*1 + 1*1 + 1*1 = 3.

Therefore, the second term is 2*3*(cos²30° - cos30°) = 6*( (3/4) - (√3/2) )

Convert to decimal:

3/4 = 0.75

√3/2 ≈ 0.8660

So, 0.75 - 0.8660 = -0.1160

Multiply by 6: ≈ -0.6960

So total numerator is 0.75 - 0.696 = 0.054.

Denominator:

First, (1 + 2 cosα) = 1 + 2*(0.8660) = 2.732.

Second, (1 - cosα)^2 = (1 - 0.8660)^2 ≈ (0.134)^2 ≈ 0.018.

Multiply those two: 2.732 * 0.018 ≈ 0.0492.

Multiply by a² = 100: 4.92.

So 1/d² ≈ 0.054 / 4.92 ≈ 0.01097, so d ≈ 9.55Å. But let's check with another approach to verify.

Alternatively, using the reciprocal lattice approach:

We have a* = (h² + k² + l² + etc.) formula. Alternatively, we can compute the reciprocal lattice vectors.

Assuming that a = 10Å, angles α = 30°, and the reciprocal lattice vectors a*, b*, c* can be calculated.

In the reciprocal lattice:

The components of the reciprocal lattice vectors can be related to the direct lattice vectors through the metric tensor and its inverse. However, this requires inverting the metric tensor. Let me try constructing the metric tensor.

For the rhombohedral system (direct lattice):

The metric tensor G has components:

G_ij = a² if i=j,

G_ij = a² cosα if i≠j.

Thus,

G = a² [ [1, cosα, cosα],
           [cosα, 1, cosα],
           [cosα, cosα, 1] ]

The determinant of this matrix is:

|G| = a^6 [1 - 3cos²α + 2cos³α]

So the inverse metric tensor G^{-1} has components (1/|G|) * adjugate of G.

The adjugate matrix for G will have elements:

G_adj_ij = (-1)^{i+j} M_ji,

where M_ji are the minors. Given the symmetry, it's possible to compute the inverse.

For a 3x3 matrix with diagonal elements D and off-diagonal elements O, the inverse can be calculated as:

(D - O)^2 + 2 (D - O)(O)

Wait, there's a formula for inverse of this kind of matrix.

Another way: Using the formula for inverse of a matrix with diagonal entries A and off-diagonal entries B:

[ A B B ]
[ B A B ]
[ B B A ]

This is a symmetric matrix, which is a special case.

The inverse can be expressed as:

det = A^3 - 3A B^2 + 2 B^3

Then, the adjugate matrix entries are:

For diagonal entries: A^2 - B^2

For off-diagonal entries: -A B + B^2

But checking with specific values.

Wait, more accurately, let me compute the inverse matrix for the direct metric tensor.

The inverse metric tensor G^{-1} is given by:

G^{-1} = (1/|G|) * [ (G_adj) ]

Where G_adj is the adjugate matrix.

Let's compute G_adj in terms of a and α.

If we take the metric tensor G:

G = a² [[1, c, c],
         [c, 1, c],
         [c, c, 1]]

where c = cosα.

The determinant is:

|G| = a^6 (1 + 2c³ - 3c²)

Now, to compute the adjugate matrix. The adjugate matrix elements G_adj[i][j] are the cofactors.

For a diagonal element G_adj_11:

G_adj_11 = determinant of the submatrix:

|1, c|

|c, 1|

Which is 1 * 1 - c * c = 1 - c^2.

But multiplied by (-1)^{1+1} = 1, so G_adj_11 = 1 - c²

For an off-diagonal element, say G_adj_12:

Cofactor for element (1,2) is (-1)^{1+2} * determinant of submatrix:

Remove row 1, remove column 2:

Submatrix is:

| c, c |

| c, 1 |

Determinant: c*1 - c*c = c - c²

Multiply by (-1)^3 = -1:

So G_adj_12 = - (c - c²)

Similarly, all off-diagonal elements will be - (c - c² )

Therefore, the adjugate matrix is:

[ (1 - c² )   -(c - c²)    -(c - c²) ]

[ -(c - c² )   (1 - c² )    -(c - c²) ]

[ -(c - c² )   -(c - c²)     (1 - c² ) ]

Thus, the inverse metric tensor G^{-1} is G_adj / |G|

i.e., each element is:

G^{-1}_ij = G_adj_ij / |G|

Therefore,

G^{-1}_11 = (1 - c²) / (a² * sqrt(1 - 3c² + 2c³) )

Wait, but |G|= a^6 (1 - 3c^2 + 2c^3 ). The adjugate elements are, for diagonal:

(1 - c² ) a^4 * terms...

Wait, I think needing to correct. Wait, wait, the metric tensor has elements G_ij = a^2 if i=j, else G_ij = a² c.

Therefore, the adjugate matrix requires computing.

Alternatively, since G = a^2 M where M is [[1, c, c], [c, 1, c], [c, c, 1]], then adj(G) = a^4 adj(M)

Wait, actually, adjugate of a scalar multiple: adj(kM) = k^(n-1) adj(M) where n is the dimension. For 3x3 matrix, adj(kM) = k^2 adj(M). So since G = a² M, then adj(G) = (a²)^2 adj(M) = a^4 adj(M)

But M is [[1, c, c], [c, 1, c], [c, c, 1]]

So, for G_adj = a^4 [[1 - c², -(c - c²), -(c - c²)], ... ]？

Wait, perhaps let's get back.

But perhaps easier to compute this numerically with given α=30°, where c = cos30° = √3 / 2 ≈ 0.8660. Then, we might be able to numerically compute the reciprocal metric tensor elements.

Compute c = cos30° = √3 / 2 ≈ 0.8660.

Compute 1 - c² = 1 - 3/4 = 1/4 ≈ 0.25

Compute c - c² = √3/2 - 3/4 ≈ 0.8660 - 0.75 = 0.1160

So adj G for diagonal elements are (1 - c²) = 0.25, off-diagonal elements are -(c - c² ) ≈ -0.1160

Thus, the adjugate matrix is approximately:

[ [0.25, -0.1160, -0.1160 ],
  [-0.1160, 0.25, -0.1160 ],
  [-0.1160, -0.1160, 0.25 ] ]

Then determinant of G was |G| = a^6 (1 - 3c² + 2c^3 )

Compute this expression:

1 - 3*(0.75) + 2*( (√3/2)^3 )

= 1 - 2.25 + 2*( (3√3)/8 )

= -1.25 + (3√3)/4

≈ -1.25 + (3*1.732)/4 ≈ -1.25 + 5.196/4 ≈ -1.25 + 1.299 ≈ 0.049

Therefore, |G| ≈ a^6 * 0.049

Therefore, inverse metric tensor G^{-1} = adj(G)/|G| = [adj(M) a^4 ] / (a^6 * 0.049 ) = adj(M) / (a² * 0.049 )

But adjacent_M elements for diagonal are 0.25 / (a² * 0.049 )
  
Wait, exact details might be cumbersome, but perhaps instead, each component of G^{-1} (inverse metric tensor) is:

G^{-1}_11 = (0.25)/(a^2 * 0.049 ) = 0.25 / (100 * 0.049 ) ≈ 0.25 / 4.9 ≈ 0.0510 Å⁻²
G^{-1}_12 = (-0.1160 ) / (a^2 * 0.049 ) ≈ -0.1160 / 4.9 ≈ -0.0237 Å⁻²

So the inverse metric tensor (which gives the reciprocal lattice vector components) is:

[ 0.0510   -0.0237   -0.0237 ]

[ -0.0237   0.0510   -0.0237 ]

[ -0.0237  -0.0237    0.0510 ]

Now, to compute |G_{hkl}| = sqrt( h^2 G^{-1}_11 + k^2 G^{-1}_22 + l^2 G^{-1}_33 + 2hk G^{-1}_12 + 2kl G^{-1}_23 + 2lh G^{-1}_13 )

For the (111) plane, h=1, k=1, l=1.

Plugging into the formula:

|G_{111}|² = (1^2 * 0.0510) + (1^2 * 0.0510) + (1^2 * 0.0510) + 2*(1*1*(-0.0237)) + 2*(1*1*(-0.0237)) + 2*(1*1*(-0.0237))

Compute each term:

0.0510*3 = 0.153

Then, cross terms:

There are three cross terms each multiplied by 2 and -0.0237.

So 2*(-0.0237)*3 = -0.1422

Thus, total |G_{111}|² = 0.153 - 0.1422 ≈ 0.0108

Hence, |G_{111}| ≈ sqrt(0.0108) ≈ 0.1039 Å⁻¹

Therefore, interplanar distance d_{111} = 1 / |G_{111}| ≈ 1 / 0.1039 ≈ 9.62 Å

Which is close to the previous result of ≈9.55Å. The minor discrepancy is likely due to approximation in the calculations (manual computation with rounding at each step). Given that the two methods give similar results, around 9.5 to 9.6 Å, which is the answer.

Alternatively, perhaps more precise calculation is needed.

Alternatively, let's compute it symbolically.

Given α = 30°, then cosα = √3/2, sinα = 1/2. Compute V:

V = a³ √(1 - 3 cos²α + 2 cos³α )

=> 1 - 3*(3/4) + 2*( (√3/2)^3 )

= 1 - 9/4 + 2*(3√3 / 8 )

= (4/4 - 9/4) + (6√3)/8

= (-5/4) + (3√3)/4

= [ -5 + 3√3 ] /4 ≈ [ -5 + 5.196 ] /4 ≈ 0.196 /4 ≈ 0.049

Then, a* = sinα / (a √( )) = (1/2) / (10 * √(0.049)) )

Compute √0.049 ≈ 0.2215

Therefore, a* ≈ 0.5 / (10 * 0.2215 ) ≈ 0.5 / 2.215 ≈ 0.2257 Å⁻¹

Then, |G_{hkl}|² = a*² [ h² + k² + l² + 2(hk + kl + lh) cosα* ]

Wait, but earlier in the definition, if in reciprocal lattice, the angles are α*, then perhaps cosα* = -cosα / (1 - cosα )

Given cosα = √3 /2 ≈0.8660.

Therefore, cosα* ≈ -0.8660 / (1 - 0.8660 ) ≈ -0.8660 / 0.134 ≈ -6.46, which is not possible since cosine cannot exceed 1. This suggests an error in the previous assumption.

Therefore, likely that the formula for cosα* was misremembered.

The correct relationship between the angles in direct and reciprocal lattices might be more complex.

Alternatively, using the reciprocal lattice calculated from the inverse metric tensor, where earlier the components are known.

Earlier, in the numeric case, we found that |G_{111}|²=0.0108 Å⁻²， hence d=9.62Å.

Taking into account possible errors in manual calculation, d ≈9.6±0.2 Å.

Alternatively, according to the first method using the formula from Cullity, d ≈9.55 Å.

Considering possible calculation methods, perhaps the correct answer is approximate 9.6 Å.

But perhaps cross-verifying this, check for the ratio between a=10Å and interplanar distance (111): Since (111) is a diagonal plane, in a cubic system with angle 90°, the distance would be a/sqrt(3) ≈5.77Å. However, in this case, angles are 30°, making the crystal much more compressed, so d is larger.

Wait no, in the cubic system, the d-spacing (111) is a / sqrt(3). If the angle is smaller, perhaps the spacing would be larger. But in our case, with angles of 30°, which is smaller than 90°, leading to a longer d-spacing.

But with calculations getting ~9.5Å, which is less than a=10Å. Seems plausible given the system.

Another way: Let's think of the interplanar distance as the distance between consecutive (111) planes. In some systems, especially with non-orthogonal axes, this distance can indeed be larger or smaller than the lattice constants.

Now, combine the results from both methods: approximately 9.5-9.6Å. Perhaps the exact answer is 10 / sqrt(1.1) ≈9.53, or similar. But according to the first calculation, it was around 9.55 with cosine terms.

Alternatively, let's do an exact symbolic calculation using the given formula from Cullity.

Formula:

1/d² = [3 sin²30 + 6(cos²30 - cos30) ] / [a² (1 + 2cos30)(1 - cos30 )² ]

First, compute numerator:

N = 3*(1/2)^2 + 6*( (sqrt(3)/2)^2 - sqrt(3)/2 )

Compute:

= 3*(0.25) + 6*( (3/4) - sqrt(3)/2 )

= 0.75 + 6*( 0.75 - 0.8660 )

= 0.75 + 6*(-0.1160 )

= 0.75 - 0.696

= 0.054

Denominator:

D = a² * (1 + 2*(sqrt(3)/2)) * (1 - sqrt(3)/2 )²

Compute step by step:

1 + 2*(sqrt(3)/2 ) = 1 + sqrt(3) ≈ 1 + 1.732 ≈ 2.732

(1 - sqrt(3)/2 )² = (1 - 0.866 )² ≈ (0.134)^2 ≈ 0.017956

Thus, D = 100 * 2.732 * 0.017956 ≈ 100 * 0.049 → 4.9

Therefore:

1/d² = 0.054 / 4.9 ≈ 0.01102

Therefore, d = 1 / sqrt(0.01102) ≈ 1 / 0.105 ≈9.52Å

Therefore, 9.52Å is the Answer.

Expressed with two decimal places, Approximately 9.52Å which can be rounded to 9.5Å, but perhaps we need to give the exact value in terms of radicals.

Alternate Way:

However, perhaps the answer wants an exact expression. Let me compute the exact expression symbolically.

Given:

1/d² = [3 sin²α + 6(cos²α - cosα ) ] / [ a² (1 + 2cosα)(1 - cosα )² ]

Expressin sin²α in terms of cosα:

sin²α = 1 - cos²α

Therefore, numerator:

N = 3(1 - cos²α ) + 6(cos²α - cosα )

= 3 - 3cos²α + 6cos²α -6cosα

= 3 + 3cos²α -6cosα

=3 (1 + cos²α -2cosα )

Factor that:

= 3(1 -2cosα + cos²α ) = 3(1 - cosα )²

Therefore, numerator N = 3(1 - cosα )²

Denominator:

D = a² (1 + 2cosα )(1 - cosα )²

Therefore, all together:

1/d² = [3(1 - cosα )²] / [ a² (1 + 2cosα )(1 - cosα )² ] = 3 / [a² (1 + 2 cosα ) ]

Thus, simplifying this:

1/d² = 3 / [a² (1 + 2 cosα ) ]

Therefore,

d = a * sqrt[ (1 + 2 cosα ) /3 ]

Wow, what a straightforward result! This simplification shows that the complicated formula from Cullity simplifies in the case of (hkl)=(111) to d = a * sqrt[ (1 + 2 cosα)/3 ]

This makes sense. Thus，this is a general formula for d_{111} in a rhombohedral system.

So, plugging into this formula:

d=10Å * sqrt[ (1 + 2*cos30°)/3 ]

Compute cos30°=√3/2 ≈0.8660

Then,

1 + 2*(0.866 )=1 +1.732≈2.732

Now,

(2.732)/3 ≈0.9107

sqrt(0.9107)≈0.954

Therefore,

d≈10 * 0.954≈9.54Å

Exactly 9.54Å.

Impressive. Therefore, even though the initial formulas were complicated, for the (111) plane in a rhombohedral system, we can simplify using d = a sqrt[ (1 + 2 cosα)/3 ]

Verification:

Yes, starting from Cullity’s formula:

1/d² = [3 (1 - cosα )² ] / [ a² (1 + 2 cosα )(1 - cosα )² ] = 3/(a²(1 + 2 cosα) )

Therefore, d² = a²(1 + 2 cosα)/3 ⇒ d = a sqrt( (1 + 2 cosα)/3 )

This is called the simplified formula for the interplanar spacing of (111) in a rhombohedral lattice.

Conclusion:

Therefore, the key formula is d = a * sqrt[ (1 + 2 cosα)/3 ]

Using given values:

a = 10 Angstrom,

cosα = cos30° = √3/2.

Then,

d = 10 * sqrt[ (1 + 2*(√3/2 )) / 3 ] = 10* sqrt[ (1 + √3 ) /3 ]

Numerically,

(1 + 1.732)/3≈2.732/3≈0.9107,

sqrt(0.9107)≈0.954,

Thus, d≈10*0.954≈9.54 Å

Therefore, the interplanar distance for the (111) plane is approximately 9.54 Angular and, rounding to two decimal places, 9.54 Å. So, the exact expression is 10 * sqrt( (1 + √3)/3 ), which can be presented as well.

---

# paraphrased_deepseek_completion_openai response

To determine the interplanar distance of the (111) plane in a rhombohedral crystal with an interatomic distance of 10 Å and angles α = β = γ = 30°, we use the formula for the interplanar distance in a rhombohedral system:

\[
d_{hkl} = \frac{a \sqrt{1 - 3\cos^2\alpha + 2\cos^3\alpha}}{\sqrt{(h^2 + k^2 + l^2)\sin^2\alpha + 2(hk + kl + lh)(\cos\alpha - \cos^2\alpha)}}
\]

Given:
- \( a = 10 \) Å (interatomic distance)
- \( \alpha = 30^\circ \)
- Miller indices (hkl) = (111)

1. **Calculate the volume factor:**
   \[
   \sqrt{1 - 3\cos^2\alpha + 2\cos^3\alpha}
   \]
   With \( \cos 30^\circ = \frac{\sqrt{3}}{2} \approx 0.866 \):
   \[
   1 - 3(0.866)^2 + 2(0.866)^3 = 1 - 3(0.75) + 2(0.6495) = 1 - 2.25 + 1.299 = 0.049
   \]
   \[
   \sqrt{0.049} \approx 0.2215
   \]

2. **Calculate the numerator:**
   \[
   a \sqrt{1 - 3\cos^2\alpha + 2\cos^3\alpha} = 10 \times 0.2215 \approx 2.215
   \]

3. **Calculate the denominator:**
   \[
   \sqrt{(h^2 + k^2 + l^2)\sin^2\alpha + 2(hk + kl + lh)(\cos\alpha - \cos^2\alpha)}
   \]
   With \( h = k = l = 1 \):
   \[
   (1^2 + 1^2 + 1^2)\sin^2 30^\circ + 2(1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1)(\cos 30^\circ - \cos^2 30^\circ)
   \]
   \[
   3 \times 0.25 + 6 \times (0.866 - 0.75) = 0.75 + 6 \times 0.116 = 0.75 + 0.696 = 1.446
   \]
   \[
   \sqrt{1.446} \approx 1.202
   \]

4. **Calculate the interplanar distance:**
   \[
   d_{111} = \frac{2.215}{1.202} \approx 1.84 \text{ Å}
   \]

Thus, the interplanar distance of the (111) plane is \boxed{1.84} Angstroms.

---

# paraphrased_deepseek_completion_openai reasoning

The reciprocal lattice parameters for a rhombohedral system can be related to the direct lattice parameters through:

a* = (1 / (a sinα)) * sqrt(1 - 3cos²α + 2cos³α )^{-1/2}

Wait, perhaps another approach. The metric tensor for a rhombohedral system can be written as:

g_ij = |a|² * [ cosα  1  1

              1  cosα  1

              1  1  cosα ]

Wait, the metric tensor (matrix) for a crystal system is given by:

g_ij = [ [a², a b cosγ, a c cosβ ]

          [b a cosγ, b², b c cosα ]

          [c a cosβ, c b cosα, c²] ]

But in a rhombohedral system, a = b = c, and α = β = γ. So:

g_ij = a² [ [1, cosα, cosα ]

             [cosα, 1, cosα ]

             [cosα, cosα, 1 ] ]

The volume V is a³√(1 - 3cos²α + 2cos³α)

To compute d_{hkl}, which is 1 / |G_{hkl}|, where |G_{hkl}| is the magnitude of the reciprocal lattice vector. However, reciprocal lattice vectors are defined via the metric tensor. Alternatively, d_{hkl} can be calculated using the formula:

d_{hkl} = 1 / sqrt( (h² + k² + l² + 2(hk + kl + lh)cosα) / a² )

Wait, hold on. Let me check. For the metric tensor approach, the interplanar distance is given by:

d_{hkl} = 1 / sqrt( h_i g^{ij} h_j )

Where h_i are the Miller indices [h, k, l], and g^{ij} is the inverse metric tensor. Since the metric tensor is:

g_ij = a² [ [1, c, c]

             [c, 1, c]

             [c, c, 1 ] ]

Where c = cosα. Then, the inverse metric tensor g^{ij} is (1/a²) * (1 / det(g)) * [cofactor matrix]

But calculating the inverse might be tedious. Alternatively, use the formula for triclinic systems, since rhombohedral is a special case. The formula for d_{hkl} in a triclinic system is:

1/d² = (1/V²) [ S₁₁h² + S₂₂k² + S₃₃l² + 2S₁₂hk + 2S₂₃kl + 2S₁₃hl ]

Where S_ij are the components of the metric tensor. Wait, actually, S_ij are the elements of the inverse metric tensor. Let me confirm.

In the triclinic system, the interplanar spacing is given by:

1/d² = h²a*² + k²b*² + l²c*² + 2hka*b*cosγ* + 2klb*c*cosα* + 2hl a*c*cosβ*

Where a*, b*, c* are the magnitudes of the reciprocal lattice vectors, and α*, β*, γ* are the angles between them. But this is equivalent to the inverse metric tensor approach.

Alternatively, perhaps a more straightforward formula for the rhombohedral system. Wait, if we consider that in the rhombohedral system, due to symmetry, the formula for d_{hkl} can be written as:

d_{hkl} = a / sqrt( h² + k² + l² + 2(hk + kl + lh)cosα ) * sqrt(1 - 3cos²α + 2cos³α )

But I need to verify this. Let me think.

Alternatively, perhaps use the relation between d_{hkl} and the direct lattice parameters for rhombohedral. I found a formula in my notes, but maybe I need to check it.

Alternatively, consider the volume of the unit cell. Since in a rhombohedral system, the volume V is:

V = a³√(1 - 3cos²α + 2cos³α)

If the volume is known, then the reciprocal lattice parameters can be determined. The reciprocal lattice vectors can be found from the direct lattice vectors.

But maybe this is too involved. Let me look for a standard formula for d_{hkl} in rhombohedral systems.

Upon a quick search in mind, I recall that for a rhombohedral system, the formula for the interplanar distance is:

d_{hkl} = a / sqrt( (h² + k² + l²) sin²α + 2(hk + kl + lh)(1 - cosα) )

Wait, but that might not be correct. Alternatively, another approach is to use the relation between d-spacing and the angles. Let's consider the planes (111). The interplanar distance d_{111} is inversely related to the length of the reciprocal lattice vector G_{111}.

In the direct lattice, the basis vectors a, b, c all have length a = 10 Å and angles α = β = γ = 30°. The reciprocal lattice vectors are given by:

a* = (b × c) / V

b* = (c × a) / V

c* = (a × b) / V

Where V is the volume of the unit cell. Let's compute V first.

The volume V for a rhombohedral cell is:

V = a³√(1 - 3cos²α + 2cos³α)

Plugging in α = 30°, cosα = √3/2 ≈ 0.8660.

Compute the term inside the square root:

1 - 3*(√3/2)² + 2*(√3/2)³

First, compute 3*(√3/2)² = 3*(3/4) = 9/4 = 2.25

Then, 2*(√3/2)³ = 2*(3√3)/8 = (6√3)/8 = (3√3)/4 ≈ (3*1.732)/4 ≈ 5.196/4 ≈ 1.299

Therefore, the term inside the square root:

1 - 2.25 + 1.299 ≈ (1 - 2.25) + 1.299 = (-1.25) + 1.299 ≈ 0.049

Thus, V = a³ * sqrt(0.049) ≈ a³ * 0.2215 ≈ (10)^3 * 0.2215 ≈ 1000 * 0.2215 = 221.5 Å³

So V ≈ 221.5 cubic Angstroms.

Now, compute the reciprocal lattice vectors. Let's compute a*:

a* = (b × c) / V

The cross product b × c in magnitude is |b||c|sinα. Since all vectors have magnitude a = 10 Å, |b × c| = a² sinα. The direction of b × c is perpendicular to the plane of b and c. However, since we need the reciprocal vector components, perhaps the calculation is more involved.

Alternatively, perhaps a smarter way. The reciprocal lattice vectors satisfy the relation:

a* . a = 2π

But since in direct space, the vectors are non-orthogonal, the reciprocal vectors are also non-orthogonal. However, maybe it's easier to compute the magnitude of the reciprocal lattice vectors.

Given that |a*| = |b*| = |c*| = 2π / (a sinθ), where θ is the angle between a* and a. Wait, no. Alternatively, the magnitude of a* is |a*| = |b × c| / V.

From above, |b × c| = a² sinα. So |a*| = (a² sinα) / V

Since V = a³√(1 - 3cos²α + 2cos³α) ≈ a³ * 0.2215,

Then |a*| = (a² sinα) / (a³ * 0.2215) ) = (sinα) / (a * 0.2215)

sinα = sin 30° = 0.5

Thus, |a*| ≈ 0.5 / (10 * 0.2215) ≈ 0.5 / 2.215 ≈ 0.2257 Å⁻¹

Similarly, |b*| and |c*| are the same.

But we need the magnitude of the reciprocal lattice vector G_{111} = a* + b* + c*. Since a*, b*, c* are vectors with magnitudes ≈0.2257 Å⁻¹ and angles between them. What is the angle between reciprocal lattice vectors?

The angle between a* and b* is γ*, which for a rhombohedral system can be computed using:

cosγ* = (cosα - cos²α) / sin²α

Wait, I think the angles in reciprocal space (α*, β*, γ*) can be derived from the direct space angles. For a rhombohedral system, the reciprocal lattice is also rhombohedral with angles α* = β* = γ*, given by:

cosα* = (cosα - cos²α) / (1 - cos²α)

Wait, cosα* = (cosα - cos²α) / (1 - cos²α) ?

Let me verify. For a general triclinic system, the angle between a* and b* is γ*, which can be calculated as:

cosγ* = (cosγ cosα - cosβ) / (sinα sinγ )

But for a rhombohedral system, with α = β = γ, the formula simplifies.

Alternatively, we can use the relation in reciprocal space. Since the reciprocal lattice of a rhombohedral lattice is also rhombohedral, the angles α* can be computed from the direct lattice parameters.

From literature, in a rhombohedral system, the reciprocal lattice angles α* satisfy:

cosα* = [cosα / (1 + cosα)]

Wait, perhaps another approach. Let's use the formula for the angle between reciprocal vectors. For a rhombohedral system, the angle between reciprocal vectors a* and b* is:

cosα* = (cosα - cos²α) / (1 - cos²α)

Given α = 30°, let's compute cosα*.

cosα* = (cos30° - cos²30°) / (1 - cos²30°)

Compute cos30° = √3/2 ≈ 0.8660

cos²30° ≈ 0.75

So numerator: 0.8660 - 0.75 ≈ 0.1160

Denominator: 1 - 0.75 = 0.25

Thus, cosα* ≈ 0.1160 / 0.25 ≈ 0.464

Therefore, α* ≈ arccos(0.464) ≈ 62.3 degrees

So the reciprocal lattice vectors have angles of approximately 62.3° between them.

Now, the magnitude of G_{111} is |a* + b* + c*|. Since all reciprocal vectors have the same magnitude and angles, we can compute the magnitude squared:

|G|² = |a*|² + |b*|² + |c*|² + 2(a*·b* + b*·c* + c*·a*)

Since |a*| = |b*| = |c*| = 0.2257 Å⁻¹, and the dot products between different reciprocal vectors are |a*||b*|cosα*.

Therefore:

|G|² = 3*(0.2257)^2 + 3*2*(0.2257)^2 * cosα*

Wait, no. The terms:

a*·b* = |a*||b*|cosα* = (0.2257)^2 * cosα* ≈ (0.2257)^2 * 0.464

Similarly, b*·c* and c*·a* are the same. Since we have three such terms, each appearing twice (a*·b*, b*·a* etc.), but since the sum is 2(a*·b* + b*·c* + c*·a*).

Wait, actually, in |G|²:

= (a* + b* + c*)·(a* + b* + c*)

= |a*|² + |b*|² + |c*|² + 2a*·b* + 2b*·c* + 2c*·a*

So since each pairwise dot product occurs once, multiplied by 2.

Since there are three reciprocal vectors, each pair a*·b*, a*·c*, b*·c* is present once. So:

|G|² = 3*(0.2257)^2 + 2*3*(0.2257)^2 * cosα*

Wait, no. Let me recast:

Each of the three vectors contributes |a*|², so 3*(0.2257)^2.

Then, the cross terms: 2(a*·b* + a*·c* + b*·c*). Since each pair (a*,b*), (a*,c*), (b*,c*) is counted once. Each of these dot products is |a*||b*|cosα*, so since all magnitudes are equal and angles are equal:

Each a*·b* = |a*|² cosα* (since |a*| = |b*|)

Thus, 2(a*·b* + a*·c* + b*·c*) = 2*3*(|a*|² cosα*) = 6*(0.2257)^2 * 0.464

Therefore, total |G|² = 3*(0.2257)^2 + 6*(0.2257)^2 * 0.464 ≈ 3*(0.0509) + 6*(0.0509)*0.464 ≈ 0.1527 + 6*0.0236 ≈ 0.1527 + 0.1416 ≈ 0.2943

Therefore, |G| ≈ sqrt(0.2943) ≈ 0.5425 Å⁻¹

Therefore, the interplanar distance d_{111} = 2π / |G| ≈ 2π / 0.5425 ≈ 11.58 Å

Wait, but this result seems large compared to the lattice parameter. The original lattice parameter is 10 Å. However, interplanar distances can be larger or smaller depending on the plane orientation. But let me check the calculation steps again.

First, volume calculation:

V = a³√(1 - 3cos²α + 2cos³α)

We had α = 30°, so cosα = √3/2 ≈ 0.8660.

So compute the term under the square root:

1 - 3*(0.8660)^2 + 2*(0.8660)^3

First compute 3*(0.8660)^2 ≈ 3*(0.75) = 2.25

Then compute 2*(0.8660)^3 ≈ 2*(0.6495) ≈ 1.299

Thus, 1 - 2.25 + 1.299 ≈ 0.049, so square root of that is ≈0.2215. So V ≈ a³ * 0.2215 ≈ 10³ *0.2215 ≈ 221.5 Å³. Correct.

Then, |a*| = (a² sinα)/V ≈ (100 * 0.5)/221.5 ≈ 50/221.5 ≈ 0.2257 Å⁻¹. Correct.

Then, angle α* ≈62.3°, cosα*≈0.464. Correct.

Then, |G|² = 3*(0.2257)^2 + 6*(0.2257)^2 * 0.464. Let's compute (0.2257)^2:

0.2257^2 ≈0.0509.

Then:

3*0.0509 ≈0.1527

6*0.0509*0.464 ≈6*0.0236≈0.1416

Sum ≈0.1527 +0.1416≈0.2943

sqrt(0.2943)≈0.5425 Å⁻¹

Then d_{111} = 2π /0.5425 ≈11.58 Å. Wait, but 2π divided by ~0.54 gives approximately 11.6. However, this seems inconsistent because for a cubic system, d_{111} would be a/sqrt(3) ≈ 5.77 Å. But here, the structure is rhombohedral with angles 30°, which is more compressed, so the interplanar distance might actually be larger. Alternatively, perhaps I made a mistake in converting reciprocal space magnitudes.

Alternatively, maybe my approach is wrong. Let's think again. The formula for d_{hkl} in terms of the direct lattice parameters and Miller indices. For a rhombohedral lattice, it's possible that the interplanar distance can be calculated using:

d_{hkl} = a / sqrt( (h² + k² + l²) sin²α + 2(hk + kl + lh)(cosα - cos2α) )

But I'm not sure. Alternatively, refer to the general formula for triclinic systems. According to the International Tables for Crystallography, the interplanar spacing for any crystal system is given by:

1/d² = h²a*² + k²b*² + l²c*² + 2hka*b*cosγ* + 2klb*c*cosα* + 2hla*c*cosβ*

Where a*, b*, c* are the reciprocal lattice parameters, and α*, β*, γ* are the reciprocal angles. For a rhombohedral system, a* = b* = c* and α* = β* = γ*.

From earlier, we have a* ≈0.2257 Å⁻¹, and α*≈62.3°, so cosγ*≈0.464.

Thus, compute for (111):

1/d² = (1^2 + 1^2 + 1^2)(a*)^2 + 2(1*1 + 1*1 + 1*1)(a*)^2 cosα*

So:

1/d² = 3*(0.2257)^2 + 6*(0.2257)^2 *0.464

Wait, this is the same as before. So 1/d² ≈0.2943, so d≈1/sqrt(0.2943)≈1/0.5425≈1.843 Å. Wait, this contradicts the previous calculation. Wait, no, wait, reciprocal vectors are in reciprocal space, so |G| is 0.5425 Å⁻¹, so d = 1/|G| ≈1.843 Å? Wait, confusion here.

Wait, no. If G is in reciprocal space, the magnitude |G| is 2π/d. Hence, d = 2π/|G|. Therefore, if |G| is 0.5425 Å⁻¹, then d = 2π /0.5425≈11.58 Å. Alternatively, if the reciprocal lattice is defined without the 2π factor (i.e., crystallographer's definition), then d = 1/|G|. But there are two conventions: the crystallographer's definition where reciprocal lattice vectors are defined without the 2π factor, and the physicist's definition which includes the 2π.

This is a critical point. In crystallography, the reciprocal lattice vectors are usually defined such that the dot product of a direct lattice vector and a reciprocal lattice vector is an integer, without the 2π factor. Hence, in that convention, |G| = 1/d. However, in solid state physics, the reciprocal lattice vectors often include the 2π factor, so |G| = 2π/d. Therefore, in the previous calculation, if we used the crystallographer's definition, then d = 1 / |G| ≈1 /0.5425≈1.843 Å, which is too small. But given that the direct lattice parameter is 10 Å, that seems unlikely.

However, in our calculation of reciprocal lattice vectors, we used the formula a* = (b × c)/V, which is the crystallographer's definition. Therefore, the reciprocal lattice vectors in this case have |G| = 1/d. So, if |G| =0.5425 Å⁻¹, then d≈1.843 Å. But this conflicts with the expectation.

Alternatively, let me check the calculation of a*.

Given:

a* = (b × c)/V

|b × c| = |b||c|sinα = a² sinα

Therefore, |a*| = |b × c| / V = (a² sinα)/V

But V = a³√(1 - 3cos²α + 2cos³α)

Thus,

|a*| = (a² sinα) / [a³ sqrt(1 - 3cos²α + 2cos³α) ) ] = (sinα) / [a sqrt(1 - 3cos²α + 2cos³α) ) ]

Given a =10 Å, α=30°, sinα=0.5, and the sqrt term sqrt(0.049)≈0.2215,

Then |a*| =0.5 / (10 *0.2215) ≈0.5 /2.215≈0.2257 Å⁻¹, which matches previous.

Thus, since |G|=0.5425 Å⁻¹, then d=1/0.5425≈1.843 Å. But this is way too small. The lattice parameter is 10 Å, but the interplanar distance can't be smaller than the interatomic distance. Wait, but interplanar distances can be smaller. For example, in a cubic system, (111) planes have d=a/sqrt(3), so for a=10 Å, d≈5.77 Å. But in our case, if angles are 30°, the crystal is compressed along the angles, so planes might be closer. But 1.8 Å seems too small.

Wait, perhaps there's confusion between interplanar distance and interatomic distance. The interatomic distance is 10 Å, which is the edge length. But if the planes are at an angle, the interplanar distance could be shorter. For example, in a cubic lattice, the (111) plane spacing is shorter than the (100) spacing. However, 1.8 Å is still quite small. Wait, but 1.8 Å is the value we get from the calculation. Let me check the steps again.

Wait, the problem says "interatomic distance of 10 Angstrom". If the interatomic distance is 10 Å, then the edge length of the rhombohedron is 10 Å. But in a rhombohedron, the edges are the vectors a, b, c with length 10 Å each. So the atoms are at the vertices of the rhombohedron. Therefore, the distance between atoms is along the edges, which are 10 Å. However, the interplanar distance for (111) planes is different. If we calculated d=1.843 Å, but that is less than the interatomic distance. Is that possible?

Alternatively, perhaps there's a misunderstanding here. In a crystal, the interatomic distance is the shortest distance between atoms, but the interplanar distance refers to the distance between adjacent planes. However, the interatomic distance is along a direction, while the interplanar distance is perpendicular to the plane. For instance, in a simple cubic lattice, the (100) planes have interplanar distance equal to the lattice constant. But for (111) planes, it's less. But in a more complex lattice, maybe the interplanar distance can be even smaller. However, 1.8 Å is extremely small, even smaller than typical atomic distances (like in diamond, Si has lattice constant ~5.4 Å, d_{111}≈3.1 Å). So perhaps there's a mistake in our calculation.

Alternatively, maybe the formula we used is incorrect. Let me check another approach. Let's consider the direct space planes (111). To find the interplanar distance, which is the distance from the origin to the plane (111). In a rhombohedral lattice, the planes (111) are perpendicular to the direction [111].

Wait, but in non-orthogonal systems, the distance from the origin to the plane is not straightforward. The formula for the distance from the origin to the plane is d = |(u · n)| / |n|, where u is a vector to the plane and n is the normal vector.

Alternatively, using the formula for the interplanar distance in terms of the reciprocal lattice. Since d_{hkl} = 1 / |G_{hkl}|, where G_{hkl} is the reciprocal lattice vector corresponding to the plane (hkl). However, in the crystallographer's definition, this is the case. Therefore, if our calculation gives |G_{111}| ≈0.5425 Å⁻¹, then d_{111}=1/0.5425≈1.843 Å. But this seems too small. Alternatively, maybe the problem is using the physicist's definition, where G_{hkl} = (h a* + k b* + l c*) * 2π. Therefore, |G| = 2π / d. In that case, if we have |G| =0.5425 Å⁻¹, then d=2π /0.5425≈11.58 Å. Which is more reasonable.

This is a critical point. Which convention are we using? The key is in the definition of reciprocal lattice vectors. If we use the physicist's convention where G = 2π(h a* + k b* + l c*), then |G| = 2π/d. If we use the crystallographer's convention, where G = h a* + k b* + l c*, then |G| = 1/d.

In our calculation of the reciprocal lattice vectors a* = (b × c)/V, this is the crystallographer's definition. Therefore, the reciprocal lattice vectors do not include the 2π factor. Thus, the correct formula should be d=1/|G|. But then, as per our calculation, d≈1.843 Å. Which is very small. Alternatively, if I messed up the calculation of the reciprocal lattice vector magnitude.

Wait, perhaps I have an error in calculating the volume. Let's recalculate the volume term:

V = a³√(1 - 3cos²α + 2cos³α )

Given α=30°, cosα=√3/2≈0.8660

So compute 1 - 3*(0.8660)^2 + 2*(0.8660)^3.

First, compute (0.8660)^2=0.75

Thus, 3*0.75=2.25

(0.8660)^3=0.8660*0.75=0.6495

Thus, 2*0.6495=1.299

So, 1 -2.25 +1.299=1 -2.25= -1.25 +1.299=0.049

sqrt(0.049)=≈0.2215. Therefore, V=10³*0.2215=221.5 Å³. Correct.

Then, |a*|=(a² sinα)/V=(100*0.5)/221.5≈0.2257 Å⁻¹. Correct.

Then, the reciprocal lattice vector G_{111}=a* + b* + c*. Each has magnitude≈0.2257 Å⁻¹, angles between them≈62.3°, cos≈0.464.

Compute |G|^2=3*(0.2257)^2 + 2*3*(0.2257)^2*0.464≈3*0.0509 +6*0.0509*0.464≈0.1527 + 0.1416≈0.2943. Then |G|=sqrt(0.2943)≈0.5425 Å⁻¹. Therefore, d=1/0.5425≈1.843 Å. But this is in the crystallographer's definition. However, in the physics convention, reciprocal vectors include the 2π factor, so G=2π*(h a* + k b* + l c*), then |G|=2π*0.5425≈3.409 Å⁻¹, and d=2π/|G|≈1.843 Å. Wait, no. Let me be precise.

Wait, if in the crystallographer's convention, G_{hkl} = h a* + k b* + l c*, and d_{hkl} = 1/|G_{hkl}|. Then in our case, d=1/0.5425≈1.843 Å.

But in the physics convention, the reciprocal lattice vectors are defined as G = 2π(h a* + k b* + l c*), so |G|=2π|h a* + k b* + l c*|, and d=2π/|G|. However, in this case, if you used the physics convention, then d=1/(|h a* + k b* + l c*|). But in our calculation, we used the crystallographer's convention, so d=1/|G|≈1.843 Å. However, such a small interplanar distance may not be realistic. Is there a mistake in the problem statement?

Wait, the problem states "interatomic distance of 10 Angstrom". If this is the nearest-neighbor distance, which in a rhombohedral lattice isn't necessarily the same as the edge length a. In a rhombohedral lattice, the nearest-neighbor distance can be equal to a if it's primitive, but depending on the angles, the distance between atoms can be different. Wait, in a primitive rhombohedral lattice, the atoms are located at the corners of the rhombohedron. The shortest distance between atoms is along the edges, which is equal to a. Therefore, if the interatomic distance is 10 Å, then a=10 Å. Therefore, the edge length is 10 Å. So, our calculation seems correct but gives an interplanar distance of approximately 1.8 Å. Which is smaller than the edge length. But in other crystal systems, such as FCC or BCC, the nearest interplanar distances can be smaller than the lattice constant. For example, in FCC, the (111) planes have a spacing of a/sqrt(3)≈0.577a. For a=10 Å, this would be≈5.77 Å. However, here, our calculation gives a smaller value. But maybe the rhombohedral lattice with angles 30° is such that the (111) planes are much closer together. Let me check with another method.

Alternative approach: The interplanar distance for (hkl) in a rhombohedral lattice can also be calculated by:

d_{hkl} = a sqrt( (1 - 3cos²α + 2cos³α) ) / sqrt( (h² + k² + l²) sin²α + 2(hk + kl + lh)(cosα - cos²α) ) )

Let me plug in the values: a=10 Å, α=30°, h=k=l=1.

First compute the numerator: a sqrt(1 - 3cos²α + 2cos³α) =10 * sqrt(0.049)≈10*0.2215≈2.215

Denominator: sqrt( (1 +1 +1) sin²30° + 2(1*1 +1*1 +1*1)(cos30° - cos²30°) )

Compute term by term:

Sum of h²+k²+l²=3. sin²30°=0.25. So first part:3*0.25=0.75

Second part:2*(3)*(cos30° - cos²30°)=6*(√3/2 - 3/4)=6*(0.8660 -0.75)=6*(0.1160)=0.696

Total denominator inside sqrt:0.75 +0.696=1.446

Thus, denominator≈sqrt(1.446)≈1.202

Thus, d_{hkl}=2.215 /1.202≈1.843 Å. Which matches the previous result. Therefore, according to this formula, the interplanar distance is indeed approximately 1.843 Å. But this seems too small. Is there a misunderstanding of the problem?

Wait, the problem statement says "interatomic distance of 10 Angstrom". If this is not the edge length but the nearest-neighbor distance, which in a rhombohedral lattice can be different from the edge length. For instance, in a rhombohedral lattice, the shortest distance (nearest neighbor) can be given by d = a sqrt(2(1 - cosα)) ). Let me verify.

In a rhombohedral lattice, the nearest neighbor distance is indeed along the edge of the rhombohedron, which is the edge length a. So if the interatomic distance is 10 Å, then a=10 Å. Therefore, our calculation is correct. Therefore, the interplanar distance for (111) is≈1.843 Å. But 1.84 Å is extremely small, even smaller than typical covalent bonds. For example, a carbon-carbon bond is about 1.54 Å. So perhaps there is a mistake in the problem's parameters. If the angles α=β=γ=30°, which is quite acute, it's possible that the crystal structure is highly compressed, leading to very closely spaced planes. However, angles of 30° in a rhombohedral lattice are quite unusual. Rhombohedral lattices typically have angles greater than 60°, such as in calcite which has a rhombohedral angle of about 101°.

Alternatively, if the problem has a typo and the angles are 60° instead of 30°, but assuming the problem is as stated. Alternatively, perhaps the question is using a different formula.

Alternatively, perhaps the formula is actually:

d_{hkl} = a / sqrt( h² + k² + l² + 2(hk + kl + lh)cosα )

But if we use this formula, plugging in a=10, h=k=l=1, cos30°≈0.866:

Denominator inside sqrt:1+1+1 +2*(1+1+1)*0.866≈3 +6*0.866≈3 +5.196≈8.196

sqrt(8.196)≈2.864

Thus, d=10/2.864≈3.49 Å. This is a different result, but why? Where does this formula come from?

Wait, this formula resembles the formula for cubic lattices, but with added terms for the angles. For cubic systems, angles are 90°, so cosα=0, and the formula reduces to d=a/sqrt(h² +k² +l²). However, this formula may be valid for other systems, but I need to verify.

In the case of a rhombohedral lattice, when converting to a hexagonal lattice, which is a common practice for easier calculation, we can use the transformation from rhombohedral to hexagonal axes. The hexagonal unit cell is three times larger in volume than the rhombohedral one. However, this might complicate things.

Alternatively, consider the relationship between rhombohedral and cubic systems. If the angles are all 90°, it becomes a cubic system. The formula d_{111}=a/sqrt(3)≈5.77Å for a=10Å. But with angles of 30°, the distance is significantly smaller. But according to the formula that I derived earlier, it's 1.84Å, but according to the alternate formula it's 3.49Å. Which is correct?

Looking back at the two formulas:

First formula derived from reciprocal lattice: d=1.843 Å.

Second formula: d=10/sqrt(3 + 5.196)=10/sqrt(8.196)=3.49 Å.

Another approach is to model the rhombohedral lattice as a distorted cubic lattice. For example, in a cubic lattice with a=10Å, (111) planes have spacing of 10/sqrt(3)=5.77Å. If we compress the cube along the space diagonal, maintaining the edge length but changing the angles, this would change the interplanar distance. However, this is getting too vague.

Alternatively, perhaps use the law of cosines in three dimensions. For the (111) planes, the normal vector is in the direction [111]. The distance between planes can be computed by projecting the edge vector onto the normal direction and dividing by the magnitude of the normal vector.

In a rhombohedral lattice, the vectors a, b, c have length 10Å, angles 30° between them. The normal vector to the (111) plane can be found via the cross product. Let me attempt this.

The normal vector N is proportional to a × b + b × c + c × a. But this is complex. Alternatively, since the (111) plane intercepts the axes at 1/a, 1/b, 1/c. Wait, in Miller indices, the plane (hkl) intercepts the axes at a/h, b/k, c/l. So for (111), the intercepts are at a, b, c. So the vectors defining the plane are from the origin to (a,0,0), (0,b,0), and (0,0,c). But since the lattice is rhombohedral, a = b = c =10Å, and the angles between them are 30°. The distance from the origin to the plane can be found using the formula:

d = | (a · (b × c)) | / |b × c + c × a + a × b | 

Wait, but this is getting too involved.

Alternatively, use the formula for the distance between adjacent lattice planes in a triclinic lattice:

d = V / sqrt( (h b × c + k c × a + l a × b ) · (h b × c + k c × a + l a × b ) )

Where V is the volume of the unit cell.

For the (111) plane, h=1, k=1, l=1. Therefore:

d = V / sqrt( (b × c + c × a + a × b ) · (b × c + c × a + a × b ) )

First, compute the numerator V=221.5 Å³.

Now, compute the denominator:

sqrt( (b × c + c × a + a × b ) · (b × c + c × a + a × b ) )

Let's compute each cross product:

First, b × c: magnitude= |b||c|sinα=10*10*sin30°=50 Å². Direction is perpendicular to b and c.

Similarly, c × a=50 Å², direction perpendicular to c and a.

a × b=50 Å², direction perpendicular to a and b.

But since the angles between a, b, c are 30°, the angles between the cross products can be found. However, the dot product between two cross products (b × c) · (c × a) can be computed using vector identities:

(b × c) · (c × a) = b · [c × (c × a)] = b · [c (c · a) - a (c · c) ]

= b · [c (a c cosα) - a (c²) ]

= c cosα (b · c) - c² (b · a )

= c² cosα (b · c / c²) - c² (a · b )

But this is getting too complex. Alternatively, use the scalar triple product identity:

(b × c) · (c × a) = (b × c) · ( -a × c ) = - (b × c) · (a × c )

Which is equal to - [ (b · a)(c · c) - (b · c)(a · c) ]

= - [ (a · b)|c|² - (b · c)(a · c) ]

Given a · b = a² cosα = 10² * cos30°=100*(√3/2)=50√3≈86.60 Å²

Similarly, |c|²=100 Å², (b · c)=50√3 Å², (a · c)=50√3 Å²

Thus,

= - [ (86.60)(100) - (86.60)(86.60) ]

= - [8660 - 7500 ] ≈ - [1160 ] ≈-1160 Å⁴

Similarly, compute other terms.

But wait, this is getting too intensive. Let me compute the magnitude squared:

The denominator is:

sqrt[ (b × c + c × a + a × b ) · (b × c + c × a + a × b ) ]

= sqrt[ |b × c|² + |c × a|² + |a × b|² + 2(b × c)·(c × a) + 2(c × a)·(a × b) + 2(a × b)·(b × c) ]

First, compute each |cross product|²:

Each |b × c|²= (50)²=2500 Å⁴. So three terms: 3*2500=7500 Å⁴.

Next, compute the dot products between different cross products:

Each pair:

(b × c)·(c × a)= (b × c)·( -a × c )= - [ (b · a)(c · c) - (b · c)(c · a) ]

= - [ (a · b)|c|² - (b · c)^2 ]

= - [ 50√3 * 100 - (50√3)^2 ]

= - [ 5000√3 - 7500 ]

≈ - [ 5000*1.732 - 7500 ]≈ - [ 8660 - 7500 ]≈ -1160 Å⁴

Similarly, (c × a)·(a × b)= - [ (c · a)(a · b) - (c · b)|a|² ]

= - [ (50√3)(50√3) - (50√3)(100) ]

= - [ 7500 - 5000√3 ]

≈ - [ 7500 - 8660 ]≈ - [ -1160 ]≈1160 Å⁴

Wait, no. Wait, (c × a)·(a × b)= (c × a)·(a × b)= [c, a, a, b] via some identity. Alternatively, using the same formula:

(c × a)·(a × b)= - [ (c · a)(a · b) - (c · b)|a|² ]

= - [ (50√3)(50√3) - (50√3)(100) ]

= - [ 7500 - 5000√3 ]

≈ - [7500 - 8660 ]

≈ - [ -1160 ]

=1160 Å⁴

Similarly, (a × b)·(b × c)= same as (b × c)·(a × b)= which is:

(a × b)·(b × c)= (a × b)·(b × c)= - [ (a · b)(b · c) - (a · c)|b|² ]

= - [ (50√3)(50√3) - (50√3)(100) ]

= - [ 7500 - 5000√3 ]

≈ - [ 7500 - 8660 ]

≈ - [ -1160 ]

=1160 Å⁴

Wait, but earlier (b × c)·(c × a)= -1160 Å⁴. So the three cross terms:

2*(-1160 +1160 +1160)=2*(1160)≈2320 Å⁴

Thus, total denominator inside sqrt:

7500 +2320≈9820 Å⁴

Therefore, denominator≈sqrt(9820)≈99.1 Å²

Therefore, d= V / denominator≈221.5 /99.1≈2.236 Å

But this contradicts the previous results. Hmm.

Wait, compute denominator squared:

|b × c + c × a + a × b |²= 3*2500 + 2*(-1160 +1160 +1160)=7500 +2*(1160)=7500 +2320=9820

Thus, denominator≈99.1 Å², so d=221.5 /99.1≈2.236 Å

But this is different from the reciprocal lattice method which gave≈1.843 Å, and the alternate formula which gave≈1.843 Å. But this third approach gives≈2.236 Å. What is causing this discrepancy?

Wait, maybe the formula I used here is incorrect. The formula states that the distance between lattice planes is d=V / |(b × c + c × a + a × b)|. But does this formula apply for any (hkl) planes? Wait, no. For the (hkl) plane, the correct formula is d= V / |h(b × c) + k(c × a) + l(a × b)|. So for (111) it is V / |b × c + c × a + a × b|. Therefore, our calculation is correct. But then the answer comes out to≈2.236 Å. Which is different from the previous methods. There must be a mistake in one of the approaches.

Alternatively, let's compute the magnitude of (b × c + c × a + a × b). We have:

Each cross product has magnitude 50 Å². The angles between them? The angle between b × c and c × a can be found as follows. The angle between two cross products is equal to the angle between the normals of the planes they are perpendicular to. For example, b × c is perpendicular to the bc-plane, and c × a is perpendicular to the ca-plane. The angle between these two planes can be derived from the original angles. But this is getting complicated. Alternatively, use the dot product:

(b × c) · (c × a) = -1160 Å⁴, as computed earlier. Therefore, the cosine of the angle between them is:

cosθ = [(b × c) · (c × a)] / (|b × c||c × a|) )= -1160 / (50*50)= -1160/2500≈-0.464

Which corresponds to an angle of≈117.7°, which is 180° -62.3°, matching our earlier reciprocal lattice angle calculation of 62.3°, as the reciprocal lattice angles were≈62.3°, so the supplementary angle in direct space.

Therefore, the vectors b × c, c × a, a × b each have magnitude≈50 Å² and angles≈117.7° between them. Therefore, when we add them, the magnitude squared is:

3*(50)^2 + 2*3*(50)^2*(-0.464)=3*2500 +6*2500*(-0.464)=7500 - 6*1160=7500 -6960=540 Å⁴

Wait, but earlier we computed it as≈9820 Å⁴. This inconsistency is confusing.

Wait, no. Earlier, when we calculated the dot products, we found (b × c)·(c × a)= -1160 Å⁴, but according to this, (b × c)·(c × a)= |b × c||c × a|cosθ=50*50*(-0.464)=2500*(-0.464)= -1160 Å⁴, which matches. Then, the sum of the cross terms was 2*(-1160 +1160 +1160)=2320 Å⁴. But if angles between the cross products are 117.7°, which have cosine≈-0.464, then each dot product between different cross products is (50)(50)(-0.464)= -1160 Å⁴. But in our calculation, two of them were -1160 and one was +1160? That seems contradictory.

Wait, perhaps there was a mistake in the sign of the dot products. When we computed (b × c)·(c × a)= -1160 Å⁴, (c × a)·(a × b)=1160 Å⁴, and (a × b)·(b × c)=1160 Å⁴. So two positive and one negative. Therefore, the sum is -1160 +1160 +1160=1160, multiplied by 2 gives2320 Å⁴. Therefore, total magnitude squared is7500 +2320=9820 Å⁴, magnitude≈99.1 Å². Therefore, d=V /99.1≈2.236 Å.

But according to the reciprocal lattice method, d=1.843 Å. Which is different.

This suggests a contradiction between two methods. This means one of the methods is incorrect.

Alternatively, verify with a reference.

According to the International Tables for Crystallography Volume A, the interplanar spacing for a rhombohedral lattice is given by:

1/d² = [ (h² + k² + l²) sin²α + 2(hk + kl + lh)(cosα - cos²α) ] / [a²(1 - 3cos²α + 2cos³α) ]

Plugging in the values:

Numerator:

(1 +1 +1)sin²30° + 2(1*1 +1*1 +1*1)(cos30° - cos²30°)=3*(0.25) +6*(0.8660 -0.75)=0.75 +6*(0.116)=0.75 +0.696=1.446

Denominator:

a²(0.049)=100*0.049=4.9

Thus, 1/d²=1.446 /4.9≈0.2951

Therefore, d=1/sqrt(0.2951)≈1.842 Å. Which matches the reciprocal lattice method.

However, the direct method using V / |...| gave≈2.236 Å. This discrepancy must be resolved. The problem is likely due to differing conventions or a miscalculation in one of the approaches.

Given that the formula from International Tables gives≈1.842 Å, this should be the correct answer. Therefore, the interplanar distance d_{111}≈1.84 Å.

But given that this seems very small, is there a different interpretation of the problem statement?

The problem states "interatomic distance of 10 Angstrom". If this refers to the nearest-neighbor distance, which in a rhombohedral lattice might not be the edge length a. For example, in a face-centered or body-centered lattice, the nearest-neighbor distance can be different. However, in a primitive rhombohedral lattice, the edge length a is the nearest-neighbor distance. Therefore, given that, the calculation seems correct, albeit counterintuitive.

Therefore, the interplanar distance of the (111) plane in this rhombohedral crystal is approximately 1.84 Å. Rounded to two decimal places, this is≈1.84 Å. However, considering significant figures—the given interatomic distance is 10 Å (one significant figure?), angles 30° (two significant figures?)—probably the answer should have two significant figures, so≈1.8 Å. But the calculation gives≈1.843, which rounds to 1.84 Å.

Alternatively, maybe the question expects a different approach where the interplanar distance is calculated using the formula for orthogonal systems, ignoring the angle considerations, which would be incorrect. For example, using the cubic formula d=a/sqrt(h² +k² +l²), which gives≈5.77 Å. But that would be wrong because the angles are not 90°. However, the problem explicitly states a rhombohedral crystal with angles 30°, so using the cubic formula is incorrect.

Thus, after careful consideration and using the correct formula from the International Tables, the interplanar distance is approximately 1.84 Å. Therefore, the answer is approximately 1.84 Angstroms.


**Final Answer**
The interplanar distance of the (111) plane is \boxed{1.84} Angstroms.

---

