# Original Question

Consider a system with Hamiltonian operator $H = \varepsilon \vec{\sigma}.\vec{n}$. Here, $\vec{n}$ is an arbitrary unit vector, $\varepsilon $ is a constant of dimension energy, and components of $\vec{\sigma}$ are the Pauli spin matrices. What are the eigenvalues of the Hamiltonian operator?


---

# DeepSeek response (via openrouter)

\boxed{\varepsilon \text{ and } -\varepsilon}

---

# DeepSeek reasoning (via openrouter)

To solve for the eigenvalues of the Hamiltonian operator $H = \varepsilon \vec{\sigma} \cdot \vec{n}$, where $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli spin matrices defined as:

$$
\sigma_x = \begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}, \quad
\sigma_y = \begin{pmatrix}
0 & -i \\
i & 0
\end{pmatrix}, \quad
\sigma_z = \begin{pmatrix}
1 & 0 \\
0 & -1
\end{pmatrix}
$$
and $\vec{n}$ is an arbitrary unit vector such that:
$$
\vec{n} = (n_x, n_y, n_z) = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta),
$$
where $n_x^2 + n_y^2 + n_z^2 = 1$.

However, for this question, it suffices to keep $\vec{n}$ as a general unit vector $(n_x, n_y, n_z)$ such that $|\vec{n}|^2 = n_x^2 + n_y^2 + n_z^2 = 1$. 

Hence, the Hamiltonian operator can be written explicitly as:
$$
H = \varepsilon \vec{\sigma} \cdot \vec{n} = \varepsilon (n_x \sigma_x + n_y \sigma_y + n_z \sigma_z).
$$
Substitute the Pauli matrices into this expression:
$$
H = \varepsilon \left( n_x \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix} + n_y \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix} + n_z \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix} \right).
$$
The Hamiltonian thus becomes:
$$
H = \varepsilon \left(\begin{pmatrix}
0 & n_x \\
n_x & 0
\end{pmatrix} +
\begin{pmatrix}
0 & -in_y \\
in_y & 0
\end{pmatrix} +
\begin{pmatrix}
n_z & 0 \\
0 & -n_z
\end{pmatrix}\right).
$$
Combine the matrices entry by entry:
$$
H = \varepsilon\begin{pmatrix}
0 + 0 + n_z & n_x - in_y \\
n_x + in_y & 0 + 0 - n_z
\end{pmatrix} = \varepsilon\begin{pmatrix}
n_z & n_x - in_y\\
n_x + in_y & -n_z
\end{pmatrix}.
$$
To find the eigenvalues of $H$, we need to solve the characteristic equation $\det(H - \lambda I) = 0$, where $I$ is the $2 \times 2$ identity matrix $I = \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$:

$$
\det\left(\varepsilon\begin{pmatrix}
n_z & n_x - in_y\\
n_x + in_y & -n_z
\end{pmatrix} - \lambda\begin{pmatrix}
1 & 0 \\ 0 & 1
\end{pmatrix}\right) = 0,
$$
which translates to:
$$
\det\begin{pmatrix}
\varepsilon n_z - \lambda & \varepsilon(n_x - in_y) \\
\varepsilon(n_x + in_y) & -\varepsilon n_z - \lambda
\end{pmatrix} = 0.
$$
The determinant calculation is:
$$
(\varepsilon n_z - \lambda)(-\varepsilon n_z - \lambda) - (\varepsilon(n_x - in_y))(\varepsilon(n_x + in_y)) = 0.
$$
This simplifies to:
$$
(\lambda^2 - \varepsilon^2 n_z^2) - \varepsilon^2 (n_x - i n_y)(n_x + i n_y) = 0.
$$
Since:
$$
(n_x - i n_y)(n_x + i n_y) = n_x^2 + n_y^2,
$$
we substitute back into the characteristic equation:
$$
\lambda^2 - \varepsilon^2 n_z^2 - \varepsilon^2(n_x^2 + n_y^2) = 0.
$$
But $n_x^2 + n_y^2 + n_z^2 = 1$:
$$
\lambda^2 = \varepsilon^2 (n_x^2 + n_y^2 + n_z^2) = \varepsilon^2.
$$
Therefore:
$$
\lambda^2 = \varepsilon^2.
$$
$$
\lambda = \pm \varepsilon.
$$

Thus the eigenvalues of the Hamiltonian $H$ are:
$$
\boxed{\varepsilon} \text{ and } \boxed{-\varepsilon}.
$$

#### Verification by explicitly diagonalizing the matrix:
To make a concrete verification, let us directly compute the eigenvalues of the matrix:
$$
\varepsilon \begin{pmatrix}
n_z & n_x - in_y \\
n_x + in_y & -n_z
\end{pmatrix}.
$$
To find the eigenvalues directly from the matrix $$A = \begin{pmatrix}
\varepsilon n_z & \varepsilon (n_x - in_y) \\
\varepsilon(n_x + in_y) & -\varepsilon n_z
\end{pmatrix},$$
solve for $\lambda$ such that:
$$
\det(\begin{pmatrix}
\varepsilon n_z - \lambda & \varepsilon(n_x - in_y) \\
\varepsilon(n_x + in_y) & -\varepsilon n_z - \lambda
\end{pmatrix}) = 0.
$$
This can again be solved explicitly by solving:
$$
\lambda^2 - (\varepsilon n_z)(-\varepsilon n_z) - \varepsilon^2(n_x + in_y)(n_x - in_y) = 0,
$$
which leads us once again to:
$$
\lambda^2 = \varepsilon^2(n_z^2 + n_x^2 + n_y^2) = \varepsilon^2.
$$
However, if you need to solve explicitly what the eigenvectors might be, you solve:
$$
\begin{pmatrix}
\varepsilon n_z & \varepsilon(n_x - in_y) \\
\varepsilon(n_x + in_y) ( -\varepsilon n_z)
\end{pmatrix} \begin{pmatrix}
u_1 \\ u_2
\end{pmatrix} = \pm \varepsilon\begin{pmatrix}
u_1 \\ u_2
\end{pmatrix}.
$$
For $\lambda = +\varepsilon$:
$$
\varepsilon\begin{pmatrix}
n_z & n_x - in_y \\
n_x + in_y & -n_z
\end{pmatrix}\begin{pmatrix}
u_1 \\ u_2
\end{pmatrix} = \varepsilon\begin{pmatrix}
u_1 \\ u_2
\end{pmatrix},
$$
which simplifies to solving:
$$
\begin{pmatrix}
n_z & n_x - in_y \\
n_x + in_y & -n_z
\end{pmatrix}\begin{pmatrix}
u_1 \\ u_2
\end{pmatrix} = \begin{pmatrix}
u_1 \\ u_2
\end{pmatrix}.
$$
This gives us the system of equations:
$$
n_z u_1 + (n_x - in_y) u_2 = u_1,
$$
$$
(n_x + in_y) u_1 - n_z u_2 = usu_2.
$$
From $(n_z - 1)u_1 + (n_x - in_y)u_2 = 0$ and $(n_x + in_y)u_1 - (n_z + 1)u_2 =$, we need to solve only one of those equations (since they are linearly dependent). For instance, from the first equation,
$$
(n_x - in_y)u_2 = (1 - n_z)u_1,
$$
thus if $ n_x - in_y \neq 0$:
$$
u_2 = \frac{1 - n_z}{n_x - in_y}u_1.
$$
Similarly using the second equation,
$$
(n_x + in_y)u_1 = (1 + n_z)u_2,
$$
which means if $n_x + in_y \neq 0$:
$$
u_1 = \frac{1 + n_z}{n_x + in_y}u_2.
$$
However, a usually more intuitive way to write eigenvectors can be found by using polar coordinates for $\vec{n}$ where $n_z = \cos\theta$, $n_x = \sin\theta\cos\phi$, $n_y = \sin\theta\sin\phi$.

However, solving for the eigenvalues themselves typically does not require us to solve for the eigenvectors explicitly. From our reasoning thus far, the eigenvalues should be verified once again explicitly:

We need to solve the equation $\det(H - \lambda I) = 0$ explicitly:
$$
\det\begin{pmatrix}
\varepsilon n_z - \lambda & \varepsilon(n_x - in_y) \\
\varepsilon(n_x + in_y) & -\varepsilon n-z - \lambda
\end{pmatrix} = (\varepsilon n_z - \lambda)(-\varepsilon n_z - \lambda) - \varepsilon^2(n_x + in_y)(n_x - in_y) = 0,
$$
which results in:
$$
\lambda^2 - \varepsilon^2 n_z^2 - \varepsilon^2(n_x^2 + n_y^2) = 0.
$$
$$
\lambda^2 - -\varepsilon^2 n_z^2 - \varepsilon^2(1 - n_z^2) = 0.
$$
$$
\lambda^2 - \varepsilon^2 = 0.
$$
$$
\lambda = \pm \varepsilon.
$$

So indeed our previous reasoning checks out completely. Therefore, the Hamiltonian $H = \varepsilon \vec{\sigma} \cdot \vec{n}$ has eigenvalues $ \pm \varepsilon$.


---

