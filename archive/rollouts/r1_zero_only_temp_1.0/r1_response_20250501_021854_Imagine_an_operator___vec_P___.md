# Original Question

Imagine an operator $\vec{P}$ of a system have components $P_x, P_y$ and $P_z$. The matrix form of the  operator $P_x$ has components in the first row as $(0, \hbar/\sqrt{2}, 0)$, that in the second row as $(\hbar/\sqrt{2}, 0, \hbar/\sqrt{2})$ and that in the third row as $(0,\hbar/\sqrt{2},0)$.  The matrix form of the  operator $P_y$ has components in the first row as $(0, -i \hbar/\sqrt{2}, 0)$, that in the second row as $(i \hbar/\sqrt{2}, 0, -i \hbar/\sqrt{2})$ and that in the third row as $(0,i \hbar/\sqrt{2},0)$. Similarly, matrix form of the  operator $P_z$ has components in the first row as $(\hbar, 0, 0)$, that in the second row as $(0, 0, 0)$ and that in the third row as $(0,0, -\hbar)$. The basis vectors here are the eigenvectors of $P_z$. The system is found in the eigenstate of $P_x$ corresponding to the eigenvalue $-\hbar$. To be more specific, the explicit form of the state of the system is given by the column vector having elements $(-1/2, 1/\sqrt{2}, -1/2)$. What is the uncertainty $\Delta P_z $ of $P_z$

---

# DeepSeek response (via openrouter)

\boxed{\frac{\hbar}{\sqrt{2}}}

---

# DeepSeek reasoning (via openrouter)

To solve for the uncertainty $\Delta P_z$ of the operator $P_z$ when the system is in a given state which is an eigenstate of $P_x$ with eigenvalue $-\hbar$, we need to first recall that the uncertainty $\Delta P_z$ is defined as:

$$
\Delta P_z = \sqrt{\langle P_z^2 \rangle - \langle P_z \rangle^2}.
$$

The question provides us with the matrix representations of $P_x$, $P_y$, and $P_z$ in a basis where the basis vectors are the eigenvectors of $P_z$. The question states that the system is in an eigenstate of $P_x$ corresponding to the eigenvalue $-\hbar$, which is given explicitly as the column vector:
$$
|\psi\rangle = \begin{pmatrix} -1/2 \\ 1/\sqrt{2} \\ -1/2 \end{pmatrix}.
$$
This state is normalized because:
$$
\left|\left(\frac{-1}{2}\right)\right|^2 + \left|\frac{1}{\sqrt{2}}\right|^2 + \left|\left(\frac{-1}{2}\right)\right|^2 = \left(\frac{1}{4}\right) + \left(\frac{1}{2}\right) + \left(\frac{1}{4}\right) = 1.
$$
However, we need to verify that this state is indeed an eigenstate of $P_x$ with eigenvalue $-\hbar$. 

The matrix representation of $P_x$ is given as:
$$
P_x = \begin{pmatrix}
0 & \frac{\hbar}{\sqrt{2}} & 0 \\
\frac{\hbar}{\sqrt{2}} & 0 & \frac{\hbar}{\sqrt{2}} \\
0 & \frac{\hbar}{\sqrt{2}} & 0
\end{pmatrix}.
$$
Let us verify that $|\psi\rangle$ is an eigenstate of $P_x$ with eigenvalue $-\hbar$:
$$
P_x |\psi\rangle = \begin{pmatrix}
0 & \frac{\hbar}{\sqrt{2}} & 0 \\
\frac{\hbar}{\sqrt{2}} & 0 & \frac{\hbar}{\sqrt{2}} \\
0 & \frac{\hbar}{\sqrt{2}} & 0
\end{pmatrix} \begin{pmatrix} -1/2 \\ 1/\sqrt{2} \\ -1/2 \end{pmatrix}.
$$
Calculating the matrix multiplication:
$$
\begin{pmatrix}
0 & \frac{\hbar}{\sqrt{2}} & 0 \\
\frac{\hbar}{\sqrt{2}} & 0 & \frac{\hbar}{\sqrt{2}} \\
0 & \frac{\hbar}{\sqrt{2}} & 0
\end{pmatrix} \begin{pmatrix} -1/2 \\ 1/\sqrt{2} \\ -1/2 \end{pmatrix} = \begin{pmatrix}
0 \cdot (-1/2) + \frac{\hbar}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} + 0 \cdot (-1/2) \\
\frac{\hbar}{\sqrt{2}} \cdot (-1/2) + 0 \cdot \frac{1}{\sqrt{2}} + \frac{\hbar}{\sqrt{2}} \cdot (-1/2) \\
0 \cdot (-1/2) + \frac{\hbar}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} + 0 \cdot (-1/2)
\end{pmatrix} = \begin{pmatrix}
\frac{\hbar}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} \\
\frac{\hbar}{\sqrt{2}} \cdot (-1/2) + \frac{\hbar}{\sqrt{2}} \cdot (-1/2) \\
\frac{\hbar}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}
\end{pmatrix} = \begin{pmatrix}
\frac{\hbar}{2} \\
\frac{\hbar}{\sqrt{2}} \left(\frac{-1}{2} - \frac{1}{2}\right) \\
\frac{\hbar}{2}
\end{pmatrix} = \begin{pmatrix}
\frac{\hbar}{2} \\
\frac{\hbar}{\sqrt{2}} \cdot (-1) \\
\frac{\hbar}{2}
\end{pmatrix} = \begin{pmatrix}
\frac{\hbar}{2} \\
-\frac{\hbar}{\sqrt{2}} \\
\frac{\hbar}{2}
\end{pmatrix}.
$$
However, what we need to check is if this result is equal to $-\hbar |\psi\rangle$:
$$
-\hbar |\psi\rangle = -\hbar \begin{pmatrix} -1/2 \\ 1/\sqrt{2} \\ -1/2 \end{pmatrix} = \begin{pmatrix} -\hbar \cdot (-1/2) \\ -\hbar \cdot (1/\sqrt{2}) \\ -\hbar \cdot (-1/2) \end{pmatrix} = \begin{pmatrix} \hbar/2 \\ -\hbar/\sqrt{2} \\ \hbar/2 \end{pmatrix}.
$$
This matches the result of $P_x |\psi\rangle$, so $|\psi\rangle$ is indeed an eigenstate of $P_x$ with eigenvalue $-\hbar$.

To find the uncertainty $\Delta P_z$, we need to calculate $\langle P_z \rangle$ and $\langle P_z^2 \rangle$. The matrix representation of $P_z$ is given as:
$$
P_z = \begin{pmatrix}
\hbar & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & -\hbar
\end{pmatrix}.
$$
To find $\langle P_z \rangle$, we need to compute:
$$
\langle P_z \rangle = \langle \psi | P_z | \psi \rangle.
$$
First, let us find $P_z |\psi\rangle$:
$$
P_z |\psi\rangle = \begin{pmatrix}
\hbar & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & -\hbar
\end{pmatrix} \begin{pmatrix} -1/2 \\ 1/\sqrt{2} \\ -1/2 \end{pmatrix} = \begin{pmatrix}
\hbar \cdot (-1/2) + 0 \cdot (1/\sqrt{2}) + 0 \cdot (-1/2) \\
0 \cdot (-1/2) + 0 \cdot (1/\sqrt{2}) + 0 \cdot (-1/2) \\
0 \cdot (-1/2) + 0 \cdot (1/\sqrt{2}) - \hbar \cdot (-1/2)
\end{pmatrix} = \begin{pmatrix}
-\hbar/2 \\
0 \\
\hbar/2
\end{pmatrix}.
$$
The bra vector $\langle \psi|$ is the conjugate transpose of $|\psi\rangle$:
$$
\langle \psi| = \begin{pmatrix} -1/2 & 1/\sqrt{2} & -1/2 \end{pmatrix}^\dagger = \begin{pmatrix} -1/2 \\ 1/\sqrt{2} \\ -1/2 \end{pmatrix}^\dagger = \begin{pmatrix} -1/2 & 1/\sqrt{2} & -1/2 \end{pmatrix}.
$$
(Note that the components here are real, so the complex conjugate is the same as the original components.)

To find $\langle P_z \rangle$:
$$
\langle P_z \rangle = \langle \psi | P_z | \psi \rangle = \begin{pmatrix} -1/2 & 1/\sqrt{2} & -1/2 \end{pmatrix} \begin{pmatrix} -\hbar/2 \\ 0 \\ \hbar/2 \end{pmatrix} = \left(-\frac{1}{2}\right) \cdot \left(-\frac{\hbar}{2}\right) + \frac{1}{\sqrt{2}} \cdot 0 + \left(-\frac{1}{2}\right) \cdot \left(\frac{\hbar}{2}\right) = \frac{\hbar}{4} + 0 - \frac{\hbar}{4} = 0.
$$
To find $\langle P_z^2 \rangle$, we need to first find $P_z^2$:
$$
P_z^2 = \begin{pmatrix}
\hbar & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & -\hbar
\end{pmatrix} \begin{pmatrix}
\hbar & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & -\hbar
\end{pmatrix} = \begin{pmatrix}
\hbar^2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & (-\hbar)^2
\end{pmatrix} = \begin{pmatrix}
\hbar^2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & \hbar^2
\end{pmatrix}.
$$
(Note that $P_z^2$ is a diagonal matrix where the diagonal elements are $\hbar^2$, $0$, and $\hbar^2$.)

To find $\langle P_z^2 \rangle$:
$$
\langle P_z^2 \rangle = \langle \psi | P_z^2 | \psi \rangle.
$$
First, let us find $P_z^2 |\psi\rangle$:
$$
P_z^2 |\psi\rangle = \begin{pmatrix}
\hbar^2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & \hbar^2
\end{pmatrix} \begin{pmatrix} -1/2 \\ 1/\sqrt{2} \\ -1/2 \end{pmatrix} = \begin{pmatrix}
\hbar^2 \cdot (-1/2) + 0 \cdot (1/\sqrt{2}) + 0 \cdot (-1/2) \\
0 \cdot (-1/2) + 0 \cdot (1/\sqrt{2}) + 0 \cdot (-1/2) \\
0 \cdot (-1/2) + 0 \cdot (1/\sqrt{2}) + \hbar^2 \cdot (-1/2)
\end{pmatrix} = \begin{pmatrix}
-\hbar^2/2 \\
0 \\
-\hbar^2/2
\end{pmatrix}.
$$
To find $\langle P_z^2 \rangle$:
$$
\langle P_z^2 \rangle = \langle \psi | P_z^2 | \psi \rangle = \begin{pmatrix} -1/2 & 1/\sqrt{2} & -1/2 \end{pmatrix} \begin{pmatrix} -\hbar^2/2 \\ 0 \\ -\hbar^2/2 \end{pmatrix} = \left(-\frac{1}{2}\right) \cdot \left(-\frac{\hbar^2}{2}\right) + \frac{1}{\sqrt{2}} \cdot 0 + \left(-\frac{1}{2}\right) \cdot \left(-\frac{\hbar^2}{2}\right) = \frac{\hbar^2}{4} + 0 + \frac{\hbar^2}{4} = \frac{\hbar^2}{2}.
$$
Finally, we need to find the uncertainty $\Delta P_z$:
$$
\Delta P_z = \sqrt{\langle P_z^2 \rangle - \langle P_z \rangle^2} = \sqrt{\frac{\hbar^2}{2} - 0^2} = \sqrt{\frac{\hbar^2}{2}} = \frac{\hbar}{\sqrt{2}} = \frac{\hbar \sqrt{2}}{2}.
$$
Thus, the uncertainty $\Delta P_z$ is:
$$
\boxed{\frac{\hbar}{\sqrt{2}}} \text{ (or equivalently, } \frac{\hbar \sqrt{2}}{2}).
$$

### Verification of the eigenvalues of $P_x$

To make sure that the given state is indeed an eigenstate of $P_x$ with eigenvalue $-\hbar$, let us solve for the eigenvalues and eigenvectors of $P_x$ explicitly. The matrix for $P_x$ is:
$$
P_x = \begin{pmatrix}
0 & \frac{\hbar}{\sqrt{2}} & 0 \\
\frac{\hbar}{\sqrt{2}} & 0 & \frac{\hbar}{\sqrt{2}} \\
0 & \frac{\hbar}{\sqrt{2}} & 0
\end{pmatrix} = \frac{\hbar}{\sqrt{2}} \begin{pmatrix}
0 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 0
\end{pmatrix}.
$$
To find the eigenvalues $\lambda$ of the matrix $P_x$, solve the characteristic equation:
$$
\det \left( \frac{\hbar}{\sqrt{2}} \begin{pmatrix}
0 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 0
\end{pmatrix} - \lambda I \right) = 0.
$$
However, it is easier to solve for the eigenvalues of the matrix $A = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$ first where $P_x = \frac{\hbar}{\sqrt{2}} A$. The characteristic equation for $A$ is:
$$
\det \begin{pmatrix}
-\lambda & 1 & 0 \\
1 & -\lambda & 1 \\
0 & 1 & -\lambda
\end{pmatrix} = 0.
$$
This expands to:
$$
-\lambda \det \begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} - 1 \det \begin{pmatrix} 1 & 1 \\ 0 & -\lambda \end{pmatrix} = 0,
$$
which is:
$$
-\lambda [(-\lambda)(-\lambda) - 1] - [1 \cdot (-\lambda) - 0] = 0,
$$
$$
-\lambda (\lambda^2 - 1) + \lambda = 0,
$$
$$
-\lambda^3 + \lambda + \lambda = 0,
$$
$$
-\lambda^3 + 2\lambda = 0,
$$
$$
\lambda(\lambda^2 - 2) = 0.
$$
The eigenvalues for $A$ are thus:
$$
\lambda = 0, \pm \sqrt{2}.
$$
The eigenvalues for $P_x$ are thus:
$$
\lambda = 0 \cdot \frac{\hbar}{\sqrt{2}} = 0, \quad \sqrt{2} \cdot \frac{\hbar}{\sqrt{2}} = \hbar, \quad -\sqrt{2} \cdot \frac{\hbar}{\sqrt{2}} = -\hbar.
$$
So, the three eigenvalues of $P_x$ are $0$, $\hbar$, and $-\hbar$. The question states that the system is in the eigenstate of $P_x$ corresponding to the eigenvalue $-\hbar$, which makes sense given the verification that $|\psi\rangle$ is indeed an eigenstate of $P_x$ with eigenvalue $-\hbar$.

### Verification of the eigenvector for $P_x$ with eigenvalue $-\hbar$

To find the eigenvector for $A$ corresponding to $\lambda = -\sqrt{2}$:
$$
\begin{pmatrix}
0 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 0
\end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix} = -\sqrt{2} \begin{pmatrix} a \\ b \\ c \end{pmatrix}.
$$
This gives us the system of equations:
$$
b = -\sqrt{2}a,
$$
$$
a + c = -\sqrt{2}b,
$$
$$
b = -\sqrt{2}c.
$$
From $b = -\sqrt{2}a$ and $b = -\sqrt{2}c$, it follows that $a = c$ (since $a = -\frac{b}{\sqrt{2}}$ and $c = -\frac{b}{\sqrt{2}}$). Using $a + c = -\sqrt{2}b$ and $a = c$, we get:
$$
2a = -\sqrt{2}b,
$$
$$
b = -\sqrt{2}a.
$$
This is a redundant equation (same as the first one). To find a specific eigenvector, let $a = 1$ (which makes $c = 1$ as well), so:
$$
b = -\sqrt{2}a = -\sqrt{2}.
$$
Thus, an eigenvector for $A$ with eigenvalue $-\sqrt{2}$ is:
$$
\begin{pmatrix} 1 \\ -\sqrt{2} \\ 1 \end{pmatrix}.
$$
Normalizing this eigenvector:
$$
\left|\begin{pmatrix} 1 \\ -\sqrt{2} \\ 1 \end{pmatrix}\right|^2 = 1^2 + (-\sqrt{2})^2 + 1^2 = 1 + 2 + 1 = 4.
$$
The normalized eigenvector is thus:
$$
\frac{1}{2} \begin{pmatrix} 1 \\ -\sqrt{2} \\ 1 \end{pmatrix} = \begin{pmatrix} 1/2 \\ -\sqrt{2}/2 \\ 1/2 \end{pmatrix} = \begin{pmatrix} 1/2 \\ -1/\sqrt{2} \\ 1/2 \end{pmatrix}.
$$
However, the question states that the given state is:
$$
\begin{pmatrix} -1/2 \\ 1/\sqrt{2} \\ -1/2 \end{pmatrix}.
$$
This is the negative of the normalized eigenvector we found for $A$ with eigenvalue $-\sqrt{2}$ (which makes sense because any scalar multiple of an eigenvector is still an eigenvector for the same eigenvalue, and here the negative sign is a scalar multiple of $-1$). Thus, the given state is indeed a valid normalized eigenvector of $P_x$ for the eigenvalue $-\hbar$.

This reasoning makes us confident that our calculations for $\langle P_z \rangle$ and $\langle P_z^2 \rangle$ are correct. Thus, the uncertainty $\Delta P_z$ is:
$$
\boxed{\frac{\hbar}{\sqrt{2}}}.
$$
(which is approximately $0.707\hbar$).


---

