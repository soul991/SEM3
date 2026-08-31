# MATHEMATICS-III (DIFFERENTIAL CALCULUS) — The Complete Concept Book
### MAKAUT BSC-301 · Built from Kreyszig + B.S. Grewal + the real MAKAUT papers of 2022-25

> Maths marks are method marks. Every section here is *method → fully worked real-exam example → traps*. Format: 70 marks; A 10×1, B 3×5, C 3×15.

---

# UNIT 1 — SEQUENCES AND SERIES

## 1.1 Convergence: the vocabulary

A sequence {aₙ} converges to L if aₙ→L. A series Σaₙ converges if its partial sums do. **Necessary condition:** aₙ → 0 (if not, divergence — the fastest first check). The condition is NOT sufficient: Σ1/n diverges though 1/n→0.

## 1.2 The tests, in the order you should try them

1. **p-series benchmark:** Σ1/nᵖ converges **iff p > 1** (2024-25 Group A, verbatim fill-in). Geometric Σrⁿ: iff |r| < 1.
2. **Comparison / Limit comparison:** compare with a p-series; lim aₙ/bₙ = finite nonzero → same fate.
3. **D'Alembert's ratio test:** lim |aₙ₊₁/aₙ| = L: L<1 converge, L>1 diverge, L=1 silent.
4. **Cauchy's root test:** $\lim_{n\to\infty} (a_n)^{1/n} = L$, same verdicts — use when nth powers appear.
5. **Leibniz (alternating):** terms decreasing to 0 → converges. Absolute vs conditional: Σ(−1)ⁿ/n converges conditionally.

**Worked (2022-23 B2-pattern):** test $\sum \frac{n^n x^n}{n!}$: ratio $= \frac{(n+1)^{n+1}x\,n!}{(n+1)!\,n^n} = x\left(1+\tfrac1n\right)^n \to xe$. Converges for $x < 1/e$, diverges for $x > 1/e$ (at x = 1/e, deeper test → diverges). *State the boundary case — that's the 5th mark.*

**Worked (2022-23 A(X)-pattern):** nature of Σ1/√n: p = 1/2 ≤ 1 → **divergent**.

## 1.3 Power and Taylor series

Power series Σaₙxⁿ has radius R = 1/lim|aₙ₊₁/aₙ|; converges absolutely inside, test endpoints separately.

**Taylor about a:** f(x) = Σ f⁽ⁿ⁾(a)(x−a)ⁿ/n!  · **Maclaurin** = a = 0.

The five expansions to know cold:
eˣ = Σxⁿ/n! (all x) · sin x = x − x³/3! + x⁵/5! − … · cos x = 1 − x²/2! + … · **log(1+x) = x − x²/2 + x³/3 − … valid on −1 < x ≤ 1** (2022-23 Group A: the region of expansion) · (1+x)ᵐ binomial for |x|<1.

**Worked (2024-25 B5): Taylor series of sin x** — derive by the derivative cycle sin→cos→−sin→−cos, evaluate at 0: sin x = x − x³/6 + x⁵/120 − …; radius ∞ (ratio test on terms).

**Worked (2024-25 A(XII)): coefficient of (x−π/2)³ for sin x about π/2:** sin x = cos(x−π/2) = 1 − (x−π/2)²/2! + (x−π/2)⁴/4! …; odd powers absent → coefficient of the cube term = **0**.
*Trap: "about x = π/2" means powers of (x−π/2) — never re-expand in x.*

---

# UNIT 2 — PARTIAL DERIVATIVES & VECTOR DIFFERENTIAL OPERATORS

## 2.1 Partial derivatives, chain rule, implicit functions

fₓ = ∂f/∂x holds other variables constant. **Worked (2024-25 A(I)):** f = x² + xy → fₓ = 2x + y, $f_{y}$ = x.

**Chain rule:** z = f(u,v), u = u(x,y)…: $\frac{\partial z}{\partial x} = z_u u_x + z_v v_x$. **Implicit F(x,y)=0:** dy/dx = −Fₓ/F_y.

**Euler's theorem (homogeneous of degree n):** $x\,u_x + y\,u_y = n\,u$. Extension: x²uₓₓ + 2xy·uₓ_y + y²u_yy = n(n−1)u.
**Worked (2024-25 B2, the classic):** u = log(x³+y³+z³−3xyz). The argument is homogeneous of degree 3 → (x∂ₓ+y∂_y+z∂_z)u = 3. The asked form: (∂ₓ+∂_y+∂_z)²u = −9/(x+y+z)². Route: x³+y³+z³−3xyz = (x+y+z)(x²+y²+z²−xy−yz−zx) and each first derivative sums to 3/(x+y+z); applying the operator again differentiates 3/(x+y+z) along (1,1,1): d/ds[3/s]·(1+1+1)… → −9/(x+y+z)². *Learn this factorization — MAKAUT reuses this exact u in both units (it returns in 7(b) 2024-25 as grad/div/curl fodder).*

## 2.2 Jacobians

$J = \frac{\partial(u,v)}{\partial(x,y)} = \begin{vmatrix} u_x & u_y \\ v_x & v_y \end{vmatrix}$. Inverse pair: ∂(x,y)/∂(u,v) = 1/J.
**Worked (2024-25 A(VII)):** $u+v = x$, $uv = y$ → $x_u{=}1$, $x_v{=}1$, $y_u{=}v$, $y_v{=}u$ → ∂(x,y)/∂(u,v) = u·1 − v·1 = **u − v**.

## 2.3 Maxima, minima, saddle points

Stationary: $f_x = f_y = 0$. Second-derivative test with $r = f_{xx}$, $s = f_{xy}$, $t = f_{yy}$, $D = rt - s^2$:
D > 0, r < 0 → max · D > 0, r > 0 → min · **D < 0 → saddle** · D = 0 → inconclusive (test directly).

**Worked in full (2024-25 C7(a), 10 marks):** f = x³ + y³ − 3x − 12y + 20.
$f_x = 3x^2 - 3 = 0 \Rightarrow x = \pm1$; $f_y = 3y^2 - 12 = 0 \Rightarrow y = \pm2$. Four stationary points.
r = 6x, s = 0, t = 6y → D = 36xy.
(1,2): D>0, r>0 → **minimum**, f = 1+8−3−24+20 = 2. (−1,−2): D>0, r<0 → **maximum**, f = −1−8+3+24+20 = 38. (1,−2) and (−1,2): D<0 → **saddle points**. 
*Presentation: stationary points table → D per point → verdicts + values. This exact structure = the 10 marks.*

**(2022-23 C8(b)-pattern):** f = x³y²-type at (0,0) with D = 0 → show along one path f>0, along another f<0 → neither max nor min.

## 2.4 Gradient, divergence, curl

∇φ = (φₓ, φ_y, φ_z) — direction of steepest ascent; directional derivative along û = ∇φ·û.
div F = ∇·F (scalar) · curl F = ∇×F (vector) · **solenoidal: div F = 0** · **irrotational: curl F = 0** · curl(grad φ) = 0 always · div(curl F) = 0 always.

**Worked (2022-23 C8(c)):** find m so F = (mx+3y)i + (2y+... )j + ...k is solenoidal → set ∂ₓF₁+∂_yF₂+∂_zF₃ = 0, solve the resulting constant equation for m.
**Worked (2024-25 C7(b), 5 marks):** F = grad(x³+y³+z³−3xyz) = (3x²−3yz, 3y²−3xz, 3z²−3xy). div F = 6x+6y+6z = **6(x+y+z)**; curl F = **0** (curl of a gradient — quote the identity, then verify one component to show method).

---

# UNIT 3 — MULTIPLE INTEGRALS & THE THREE THEOREMS

## 3.1 Double integrals over regions

∫∫_R f dA: fix the outer variable, find the inner limits from the region's boundary curves. **Sketch the region first — always.**

**Worked (2024-25 B3):** ∫∫ xy(x+y) dxdy over region between y = x² and y = x. Curves meet at (0,0),(1,1); x from 0 to 1, y from x² to x:
$$\int_0^1\!\!\int_{x^2}^{x}\!(x^2y + xy^2)\,dy\,dx = \int_0^1\!\Big[\tfrac{x^2y^2}{2}+\tfrac{xy^3}{3}\Big]_{x^2}^{x}dx = \int_0^1\!\Big(\tfrac{5x^4}{6}-\tfrac{x^6}{2}-\tfrac{x^7}{3}\Big)dx = \tfrac16-\tfrac1{14}-\tfrac1{24} = \mathbf{\tfrac{3}{56}}$$
```{=latex}
\begin{center}\begin{tikzpicture}
\begin{axis}[width=6.8cm,height=5.8cm,axis lines=middle,xlabel=$x$,ylabel=$y$,xmin=-0.12,xmax=1.28,ymin=-0.12,ymax=1.28,xtick={1},ytick={1},title={\small The parabola--line lens}]
\addplot[name path=up,thick,accent,domain=0:1]{x};
\addplot[name path=dn,thick,mintedge,domain=0:1]{x^2};
\addplot[accentlight] fill between[of=up and dn];
\node at (axis cs:0.6,0.47) {\scriptsize $\mathcal{R}$};
\node[right] at (axis cs:0.72,0.86) {\scriptsize $y=x$};
\node[right] at (axis cs:0.88,0.62) {\scriptsize $y=x^2$};
\end{axis}\end{tikzpicture}\end{center}
```

*(Do the arithmetic on paper twice; MAKAUT's favourite region is exactly this parabola-line lens.)*

**Worked (2024-25 C8(a), 8 marks):**

*Find $\iint y\,dxdy$ over the region between $y = x$ and $y = 4x - x^2$.*

**Solution.** Intersections: $x = 4x - x^2 \Rightarrow x(x-3) = 0 \Rightarrow x \in [0,3]$, parabola above the line.

```{=latex}
\begin{align*}
I &= \int_0^3\!\!\int_x^{4x-x^2} y\,dy\,dx
   = \frac12\int_0^3\big[(4x-x^2)^2 - x^2\big]dx\\[2pt]
  &= \frac12\int_0^3\big(15x^2 - 8x^3 + x^4\big)dx
   = \frac12\Big[5x^3 - 2x^4 + \frac{x^5}{5}\Big]_0^3\\[2pt]
  &= \frac12\Big(135 - 162 + \frac{243}{5}\Big) = \frac12\cdot\frac{108}{5}
   = \mathbf{\frac{54}{5}}
\end{align*}
```

## 3.2 Change of order and change of variables

**Change of order:** re-describe the region with the other variable outside. The 2024-25 C8(b) classic: $I = \int_0^1\big[\int_{e^x}^{e}\frac{dy}{y\log y}\big]dx$. Reversed: $y$ runs $1\to e$, and for fixed $y$, $x$ runs $0$ to $\log y$:
$$I = \int_1^e\Big[\int_0^{\log y}\!dx\Big]\frac{dy}{y\log y} = \int_1^e\frac{\log y}{y\log y}\,dy = \int_1^e\frac{dy}{y} = \mathbf{1}$$
*The whole point: the inner integral was impossible in the original order; after swapping it collapses. State that observation — it carries marks.*

```{=latex}
\begin{center}\begin{tikzpicture}
\begin{axis}[width=6.8cm,height=5.4cm,axis lines=middle,xlabel=$x$,ylabel=$y$,xmin=-0.12,xmax=1.32,ymin=0,ymax=3.15,xtick={1},ytick={1,2.718},yticklabels={$1$,$e$},title={\small Swap: $e^x\le y\le e \;\Rightarrow\; 0\le x\le\log y$}]
\addplot[name path=up,thick,accent,domain=0:1]{2.71828};
\addplot[name path=dn,thick,mintedge,domain=0:1]{exp(x)};
\addplot[accentlight] fill between[of=up and dn];
\node[right] at (axis cs:0.3,1.2) {\scriptsize $y=e^x$};
\end{axis}\end{tikzpicture}\end{center}
```

**Polar:** $dA = r\,dr\,d\theta$. **Worked (2024-25 A(VIII)):** $\int_0^{\pi/2}\!\int_0^1 r\sin\theta\,dr\,d\theta = [-\cos\theta]_0^{\pi/2}\cdot\big[\tfrac{r^2}{2}\big]_0^1 = 1\times\tfrac12 = \mathbf{\tfrac12}$.

**Cartesian→polar for $\iint e^{-(x^2+y^2)}$, circles, lemniscates** — substitute $x = r\cos\theta$, $y = r\sin\theta$, Jacobian $r$.

## 3.3 Green, Gauss, Stokes (statements + circle applications)

- **Green (plane):** $\oint_C (M\,dx + N\,dy) = \iint_R (N_x - M_y)\,dA$ — line integral ↔ area integral.
- **Stokes:** $\oint_C \vec F\cdot d\vec r = \iint_S (\nabla\times\vec F)\cdot\hat n\,dS$ — circulation ↔ flux of curl.
- **Gauss divergence:** $\oiint_S \vec F\cdot\hat n\,dS = \iiint_V (\nabla\cdot\vec F)\,dV$ — flux ↔ volume integral.

Syllabus says **statement only** + problems. The recurring problem type (2022-23 A(XII), A(VII)): evaluate $\oint$ around $x^2+y^2=4$ by Green — e.g. $\oint(x\,dy - y\,dx) = \iint(1+1)\,dA = 2\cdot\text{Area} = 2\pi\cdot4 = 8\pi$ (radius 2). Area via Green: $A = \tfrac12\oint(x\,dy - y\,dx)$.

**Worked area (2022-23 A(I)):** region under $y = e^x$, $x\in[0,1]$: $\int_0^1 e^x\,dx = \mathbf{e-1}$ (simple definite integral — Group A speed mark).

---

# UNIT 4 — DIFFERENTIAL EQUATIONS

## 4.1 First order, first degree

**Exact:** M dx + N dy = 0 is exact iff $M_y = N_x$. Solution: ∫M dx (y fixed) + ∫(terms of N without x) dy = c.
**Worked (2024-25 C9(a), 8 marks):**

*Solve $(2x+3y+7)\,dx + (3x-5y+2)\,dy = 0$.*

**Solution.**

```{=latex}
\begin{align*}
\frac{\partial M}{\partial y} = 3 = \frac{\partial N}{\partial x}
  &\quad\Rightarrow\quad \text{exact} \tag{test}\\[4pt]
\int M\,dx = x^2 + 3xy + 7x,
  &\qquad \int(-5y+2)\,dy = -\frac{5y^2}{2} + 2y
\end{align*}
```

$$\therefore\quad \boxed{\,x^2 + 3xy + 7x - \frac{5y^2}{2} + 2y = c\,}$$

**Linear:** $\tfrac{dy}{dx} + P(x)y = Q(x)$ → IF $= e^{\int P\,dx}$, $\;y\cdot\mathrm{IF} = \int Q\cdot\mathrm{IF}\,dx + c$.
**Bernoulli:** $\tfrac{dy}{dx} + Py = Qy^n$ → divide by $y^n$, substitute $v = y^{1-n}$ → linear.

**Orthogonal trajectories (2024-25 C9(b), 7 marks):** family x² + y² = r²: differentiate → x + y y' = 0 → y' = −x/y; orthogonal: replace y' by −1/y' → −1/y' = −x/y → y' = y/x → dy/y = dx/x → **y = cx** (radial lines — geometrically obvious: lines ⊥ circles; say so).

## 4.2 First order, higher degree (p-equations) — a MAKAUT fixture

p ≡ dy/dx.
**Solvable for p:** factor the polynomial in p; solve each linear factor; multiply the solutions.
**Worked (2024-25 B4):**

*Solve $xp^2 + (y-x)p - y = 0$.*

**Solution.** Factor as a quadratic in $p$:

```{=latex}
\begin{align*}
xp^2 + yp - xp - y &= p(xp+y) - (xp+y) = (p-1)(xp+y) = 0\\[4pt]
p = 1 &\;\Rightarrow\; y = x + c \tag{i}\\
xp = -y \;\Rightarrow\; \frac{dy}{y} = -\frac{dx}{x} &\;\Rightarrow\; xy = c \tag{ii}
\end{align*}
```

$$\therefore\quad (y - x - c)(xy - c) = 0$$

**Solvable for y / for x:** differentiate w.r.t. x (or y), reduce to an equation in p.

**Clairaut's form (Group A guaranteed):** **y = px + f(p)** (2022-23 A(II): the general form). General solution: replace p by c → y = cx + f(c). **Singular solution:** eliminate c between y = cx + f(c) and 0 = x + f'(c) — the envelope.
**Worked (2024-25 A(IX)):** y = px + a√(1+p²): singular → x = −ap/√(1+p²); eliminate → **x² + y² = a²** (the circle enveloping all those lines).
**Worked (2024-25 A(III)):** y = px + a/p → general: **y = cx + a/c**.
**Worked (2022-23 B6-pattern):** general and singular solution of a given Clairaut — always the two-step above.

## 4.3 Second order linear, constant coefficients

$(aD^2 + bD + c)y = X$. **CF:** roots of $am^2+bm+c=0$ — real distinct: $Ae^{m_1x}+Be^{m_2x}$; repeated: $(A+Bx)e^{mx}$; complex $\alpha\pm i\beta$: $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$.
**PI shortcuts (1/f(D) acting on X):**
$e^{ax} \to \tfrac{1}{f(a)}$ (if $f(a)\ne0$; else multiply by $x$, differentiate $f$) · $\sin ax/\cos ax$ → put $D^2 = -a^2$ · $x^n$ → expand $\tfrac{1}{f(D)}$ binomially · $e^{ax}V$ → shift: $e^{ax}\tfrac{1}{f(D+a)}V$.
**Group A one-liners (2024-25):** D(sin 3x) = **3cos 3x**; (1/D)(x²) = **x³/3** (1/D = integrate).

**Variation of parameters (asked 2024-25 B6):**

For $y'' + a^2y = \cos ax$ (resonant: RHS lies in the CF):

```{=latex}
\begin{align*}
y_1 &= \cos ax, \quad y_2 = \sin ax, \quad W = y_1y_2' - y_2y_1' = a\\[4pt]
y_p &= -y_1\!\int\!\frac{y_2 X}{W}dx + y_2\!\int\!\frac{y_1 X}{W}dx
     && (X = \cos ax)\\[2pt]
    &= -\cos ax\cdot\frac{\sin^2 ax}{2a^2}
       + \sin ax\cdot\frac1a\Big(\frac{x}{2}+\frac{\sin 2ax}{4a}\Big)\\[2pt]
    &= \frac{x\sin ax}{2a} \;+\; (\text{CF-absorbable terms})
\end{align*}
```

$$\therefore\quad y = A\cos ax + B\sin ax + \frac{x\sin ax}{2a}$$

*The $x$-multiplied term is the signature of resonance — point it out for the last mark.*

## 4.4 Cauchy-Euler equation (the 2024-25 15-marker, solved in full)

x²D² + axD + b type: substitute **x = e^t** (t = log x), let θ = d/dt: xD = θ, x²D² = θ(θ−1).

**(x²D² + 3xD + 2)y = cos(log x):**

**Solution.**

*Step 1 — substitute* $x = e^t$, $\theta \equiv d/dt$ (so $xD = \theta$, $x^2D^2 = \theta(\theta-1)$):

```{=latex}
\begin{align*}
(\theta^2 + 2\theta + 2)\,y &= \cos t \tag{1}
\end{align*}
```

*Step 2 — CF.* $m^2+2m+2 = 0 \Rightarrow m = -1\pm i$:

```{=latex}
\begin{align*}
y_c &= e^{-t}(A\cos t + B\sin t)
\end{align*}
```

*Step 3 — PI.* Put $\theta^2 \to -1$ in (1), then rationalize:

```{=latex}
\begin{align*}
y_p &= \frac{1}{2\theta+1}\cos t
     = \frac{2\theta-1}{4\theta^2-1}\cos t
     = \frac{-2\sin t-\cos t}{-5}
     = \frac{\cos t + 2\sin t}{5}
\end{align*}
```

*Step 4 — back-substitute* $t = \log x$:

$$\boxed{\,y = \frac1x\big(A\cos(\log x)+B\sin(\log x)\big) + \frac{\cos(\log x)+2\sin(\log x)}{5}\,}$$

---

# UNIT 5 — GRAPH THEORY

## 5.1 The vocabulary (Group A harvest — all real)

Graph G(V,E); degree = edges at a vertex; Σdeg = 2|E| (handshake). **Walk** — any vertex-edge alternation; **trail** — no repeated edge; **path** — no repeated vertex; **circuit/cycle** — closed. **Digraph** — directed edges (in/out-degrees).
**(2024-25 A(V)):** in a path, every **intermediate vertex has degree 2** (ends have 1).
**(2022-23 A(IX)):** eccentricity of the single vertex of a one-vertex graph = **0** (e(v) = max distance to any vertex).
**Euler circuit:** uses every **edge** once — exists iff connected and every degree even (trail: exactly 0 or 2 odd). **Hamiltonian circuit:** every **vertex** once — no easy criterion (contrast is a 5-marker).

## 5.2 Matrix representations

**Adjacency matrix:** n×n, aᵢⱼ = 1 if edge — **a 5-vertex, 7-edge graph has a 5×5 adjacency matrix** (2022-23 A(III): size depends only on vertices). Symmetric for undirected; row sum = degree.
**Incidence matrix:** n×m (vertices × edges) — the same graph: 5×7; each column has exactly two 1s (or ±1 directed).

## 5.3 Trees and minimal spanning trees

**Tree:** connected, acyclic; n vertices ⟹ **n−1 edges**; any two vertices joined by exactly one path. **Binary tree:** each node ≤ 2 children; **has exactly one root** and an **odd number of vertices** when full — (2024-25 A(XI) fill-in: "exactly one root"). **Spanning tree:** subgraph, tree, touching all n vertices; a connected graph has ≥1.

**Kruskal's algorithm (2024-25 C11, 15 marks with Prim):** sort edges ascending; add the cheapest edge that creates **no cycle**; stop at n−1 edges. Edge-driven, needs cycle detection (union-find), great for sparse graphs.
**Prim's algorithm:** grow one tree from any start vertex; repeatedly add the **cheapest edge leaving the tree**; vertex-driven, great for dense graphs.
```{=latex}
\begin{center}\begin{tikzpicture}[v/.style={draw,circle,thick,fill=accentlight,inner sep=2pt,minimum size=6.5mm}]
\node[v] (A) at (0,1.6) {A}; \node[v] (B) at (2,2.6) {B}; \node[v] (C) at (2.3,0.4) {C};
\node[v] (D) at (4.3,2.4) {D}; \node[v] (E) at (4.6,0.6) {E};
\draw[ultra thick,mintedge] (A)--node[above left]{\scriptsize 1}(B);
\draw[ultra thick,mintedge] (B)--node[left]{\scriptsize 2}(C);
\draw[gray] (A)--node[below]{\scriptsize 3}(C);
\draw[ultra thick,mintedge] (B)--node[above]{\scriptsize 4}(D);
\draw[gray] (C)--node[above]{\scriptsize 5}(D);
\draw[ultra thick,mintedge] (C)--node[below]{\scriptsize 6}(E);
\draw[gray] (D)--node[right]{\scriptsize 7}(E);
\node at (2.3,-0.6) {\scriptsize thick = MST edges (total 13); gray = rejected (cycle or heavier)};
\end{tikzpicture}\end{center}
```

**Exam presentation (worth the full 15):** state both algorithms stepwise, then run BOTH on one 5-6 vertex weighted example showing every intermediate choice in a table (edge considered / accepted-rejected / why), confirm both reach the same total weight (MSTs may differ, weight cannot), and close with the contrast paragraph + complexities O(E log E) vs O(E log V).

---

# FORMULA SHEET (BSC-301)

Σ1/nᵖ ⇔ p>1 · ratio/root: L<1 ✓ · log(1+x): −1<x≤1 · Taylor: Σf⁽ⁿ⁾(a)(x−a)ⁿ/n! · Euler: x uₓ + y u_y = nu · D = rt−s²: >0 min/max by r, <0 saddle · ∂(x,y)/∂(u,v) = 1/[∂(u,v)/∂(x,y)] · solenoidal div=0, irrotational curl=0, curl grad = 0 · polar dA = r dr dθ · Green: ∮M dx+N dy = ∫∫(Nₓ−M_y)dA; Area = ½∮(x dy−y dx) · exact iff M_y = Nₓ; IF $= e^{\int P}$ · Clairaut y = cx+f(c); singular = envelope · x=e^t: xD=θ, x²D²=θ(θ−1) · 1/f(D)e^{ax}=e^{ax}/f(a); D²→−a² for sin/cos · tree: n−1 edges; Σdeg=2E; Euler ⇔ all even · Kruskal edges-up, Prim tree-out.

*— End of the Mathematics-III Concept Book —*


---

# 📺 VIDEO COMPANION — topic-wise (from your chosen playlists)

> Not covered by this playlist: Power/Taylor series (thin) — the book chapter covers it fully.


### Unit1: Sequences & series convergence
- [Roadmap for Differential Calculus | MAKAUT | BSC 301 | Strategy for 9 SGPA](https://www.youtube.com/watch?v=fbYz2BhO4wg) (18:29)
- [09 | Cauchy Euler Equation | 2nd Order Differential Equation | Differential Calculus | Makaut](https://www.youtube.com/watch?v=MlMNiGd1C-A) (56:43)
- [Lec-05 | Isomorphic Graphs in 1 Shot | Isomorphism Tricks | Graph Theory | Discrete Mathematics](https://www.youtube.com/watch?v=CAc-bGcQr3Y) (61:36)
- [Gradient | Divergence | Curl | PYQ | 2 & 3 variables | Functions of Several Variables](https://www.youtube.com/watch?v=yR5l12_KsOA) (61:29)
- [Line Integral | Surface Integral | Volume Integral | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=av74NB19qM4) (66:48)
- [Green's Theorem | Line Integral | PYQs | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=gI7b-fEolss) (56:36)

### Unit2: Partial derivatives & Euler
- [09 | Cauchy Euler Equation | 2nd Order Differential Equation | Differential Calculus | Makaut](https://www.youtube.com/watch?v=MlMNiGd1C-A) (56:43)
- [Lec-04 | Eulerian & Hamiltonian Graph | Distance & Diameter | Graph Theory | Discrete Mathematics](https://www.youtube.com/watch?v=y7M8fw4jxyY) (49:08)
- [Pt.1 | Partial Derivative | PYQ | Definition | 1st Order | Function of Several Variables](https://www.youtube.com/watch?v=YP-KfMSH2KI) (52:36)
- [Pt. 2 | Partial Derivative | PYQ | Definition | 2nd Order | Function of Several Variables](https://www.youtube.com/watch?v=5N2X8BLd2To) (33:56)
- [Chain Rule | PYQ | 1st & 2nd order Partial Derivatives | Function of Several Variables](https://www.youtube.com/watch?v=qZ7qG3R78UI) (57:30)
- [Jacobian | PYQ | 1st & 2nd order Partial Derivatives | Function of Several Variables](https://www.youtube.com/watch?v=a35BcGzuT9Y) (34:24)

### Unit2: Jacobian
- [Jacobian | PYQ | 1st & 2nd order Partial Derivatives | Function of Several Variables](https://www.youtube.com/watch?v=a35BcGzuT9Y) (34:24)
- [Suggestion | BSC 301 | Differential Calculus | MAKAUT | Odd Sem | CSE](https://www.youtube.com/watch?v=BNWvmchDFWM) (21:16)

### Unit2: Maxima minima saddle
- [Prim's Algorithm | Minimal Spanning Tree | Tree | MAKAUT PYQ | Graph Traversals| Graph Theory](https://www.youtube.com/watch?v=yj-36QsYnxA) (30:50)
- [Kruskal's Algorithm | Minimal Spanning Tree | Graph Traversals | MAKAUT PYQ | Graph Theory](https://www.youtube.com/watch?v=VJGJB1sA96o) (23:51)
- [Maxima | Minima | Saddle Point | Best Technique | PYQ | Function of Several Variables](https://www.youtube.com/watch?v=PI-GZdLtqzk) (55:09)

### Unit2: Gradient divergence curl
- [Directional Derivative | PYQ | All Problems Discussed | Function of Several Variables](https://www.youtube.com/watch?v=gxYbFEDl3b8) (32:11)
- [Gradient | Divergence | Curl | PYQ | 2 & 3 variables | Functions of Several Variables](https://www.youtube.com/watch?v=yR5l12_KsOA) (61:29)
- [Line Integral | Surface Integral | Volume Integral | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=av74NB19qM4) (66:48)
- [Green's Theorem | Line Integral | PYQs | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=gI7b-fEolss) (56:36)
- [Gauss Theorem | Divergence Theorem | MAKAUT PYQ | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=unKE6aJGX-c) (46:08)
- [Stoke's Theorem | Surface Integral | MAKAUT PYQ | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=8wLLjTXqlC8) (23:21)

### Unit3: Double & triple integrals
- [Roadmap for Differential Calculus | MAKAUT | BSC 301 | Strategy for 9 SGPA](https://www.youtube.com/watch?v=fbYz2BhO4wg) (18:29)
- [Double Integration | Evaluation of Double Integral | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=_ke4Ux65rFs) (62:04)
- [Double Integral | Change of Order | PYQs | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=NcvZGk-FC98) (43:25)
- [Double Integral | Change of Variables | PYQs | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=tiwV_WqHR5Q) (45:31)
- [Triple Integral | Evaluation of Triple Integral | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=nOgwfYKkZXA) (28:34)
- [Line Integral | Surface Integral | Volume Integral | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=av74NB19qM4) (66:48)

### Unit3: Change of order/variables, polar
- [Double Integral | Change of Order | PYQs | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=NcvZGk-FC98) (43:25)
- [Double Integral | Change of Variables | PYQs | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=tiwV_WqHR5Q) (45:31)
- [MAKAUT | BSC 301 | 2023-24 Complete Solution | CSE | IT | Data Science 2nd Year](https://www.youtube.com/watch?v=gQTX1ropytk) (311:21)

### Unit3: Green Gauss Stokes
- [Line Integral | Surface Integral | Volume Integral | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=av74NB19qM4) (66:48)
- [Green's Theorem | Line Integral | PYQs | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=gI7b-fEolss) (56:36)
- [Gauss Theorem | Divergence Theorem | MAKAUT PYQ | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=unKE6aJGX-c) (46:08)
- [Stoke's Theorem | Surface Integral | MAKAUT PYQ | Multiple Integral | Differential Calculus](https://www.youtube.com/watch?v=8wLLjTXqlC8) (23:21)

### Unit4: First order ODE (exact/linear/Bernoulli)
- [02 | First Order First Degree Ordinary Differential Equation | Differential Calculus](https://www.youtube.com/watch?v=j-1O0HbwRBo) (30:55)
- [03 | Exact Equation | Integrating Factor | First Order First Degree ODE | Differential Calculus](https://www.youtube.com/watch?v=KHtEr2mwkJA) (54:13)
- [04 | Linear Equation | Bernoulli's Equation | 1st Order 1st Degree ODE | Differential Calculus](https://www.youtube.com/watch?v=t_TZzMEZAJU) (34:20)
- [05 | 1st Order Higher Degree Differential Equation | Clairaut's equation | Differential Calculus](https://www.youtube.com/watch?v=VU233e8mZRc) (58:50)
- [06 | 2nd Order Linear Differential Equation | Complementary Function | Differential Calculus](https://www.youtube.com/watch?v=NI3UNRSfa0Q) (44:30)
- [07 | D-Operator Method in 1 Shot | 2nd Order Linear Differential Equation | Differential Calculus](https://www.youtube.com/watch?v=1Zg5vmYkjGM) (97:56)

### Unit4: Higher degree p, Clairaut
- [05 | 1st Order Higher Degree Differential Equation | Clairaut's equation | Differential Calculus](https://www.youtube.com/watch?v=VU233e8mZRc) (58:50)
- [MAKAUT | BSC 301 | 2024-25 Complete Solution | Differential Calculus](https://www.youtube.com/watch?v=us_CqtnMnV4) (156:35)

### Unit4: Second order, D-operator, variation, Cauchy-Euler
- [06 | 2nd Order Linear Differential Equation | Complementary Function | Differential Calculus](https://www.youtube.com/watch?v=NI3UNRSfa0Q) (44:30)
- [07 | D-Operator Method in 1 Shot | 2nd Order Linear Differential Equation | Differential Calculus](https://www.youtube.com/watch?v=1Zg5vmYkjGM) (97:56)
- [08 | Method of Variation of Parameter | Wronskian | Differential Equation | Differential Calculus](https://www.youtube.com/watch?v=udK6Q6C8V6k) (51:07)
- [09 | Cauchy Euler Equation | 2nd Order Differential Equation | Differential Calculus | Makaut](https://www.youtube.com/watch?v=MlMNiGd1C-A) (56:43)
- [MAKAUT | BSC 301 | 2023-24 Complete Solution | CSE | IT | Data Science 2nd Year](https://www.youtube.com/watch?v=gQTX1ropytk) (311:21)

### Unit5: Graph theory basics
- [Roadmap for Differential Calculus | MAKAUT | BSC 301 | Strategy for 9 SGPA](https://www.youtube.com/watch?v=fbYz2BhO4wg) (18:29)
- [01 | Order and degree of Ordinary Differential Equation | Introduction | Differential Calculus](https://www.youtube.com/watch?v=-WfAIocM0XM) (36:52)
- [02 | First Order First Degree Ordinary Differential Equation | Differential Calculus](https://www.youtube.com/watch?v=j-1O0HbwRBo) (30:55)
- [03 | Exact Equation | Integrating Factor | First Order First Degree ODE | Differential Calculus](https://www.youtube.com/watch?v=KHtEr2mwkJA) (54:13)
- [04 | Linear Equation | Bernoulli's Equation | 1st Order 1st Degree ODE | Differential Calculus](https://www.youtube.com/watch?v=t_TZzMEZAJU) (34:20)
- [05 | 1st Order Higher Degree Differential Equation | Clairaut's equation | Differential Calculus](https://www.youtube.com/watch?v=VU233e8mZRc) (58:50)

### Unit5: Incidence/adjacency matrix
- [Lec-01 | Introduction to Graph Theory | Important Terminologies | Vertex Edge | Discrete Mathematics](https://www.youtube.com/watch?v=2L-A1Ex6a7I) (36:57)
- [Lec-06 | Incidence Matrix | Isomorphism Tricks | Directed Graph | Graph Theory | Discrete Mathematic](https://www.youtube.com/watch?v=Hf1rOFY5R-E) (52:04)
- [Lec-07 | Adjacency Matrix | Directed Graph  | Graph Theory | Discrete Mathematics| Makaut PYQs](https://www.youtube.com/watch?v=ho4YKJ4FVsg) (38:21)

### Unit5: Trees, spanning, Kruskal, Prim
- [Prim's Algorithm | Minimal Spanning Tree | Tree | MAKAUT PYQ | Graph Traversals| Graph Theory](https://www.youtube.com/watch?v=yj-36QsYnxA) (30:50)
- [Kruskal's Algorithm | Minimal Spanning Tree | Graph Traversals | MAKAUT PYQ | Graph Theory](https://www.youtube.com/watch?v=VJGJB1sA96o) (23:51)
- [MAKAUT PYQ Solution | CA4 | Problems | MCQ | BSC 301 | 2021-22](https://www.youtube.com/watch?v=tCcKqrn3H0g) (163:08)
- [MAKAUT | BSC 301 | 2023-24 Complete Solution | CSE | IT | Data Science 2nd Year](https://www.youtube.com/watch?v=gQTX1ropytk) (311:21)
- [MAKAUT | BSC 301 | 2024-25 Complete Solution | Differential Calculus](https://www.youtube.com/watch?v=us_CqtnMnV4) (156:35)
