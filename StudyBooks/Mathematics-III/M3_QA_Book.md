# MATHEMATICS-III — The Question-Answer Book
### MAKAUT BSC-301 · Real PYQs of 2022-23 & 2024-25 solved in full (2023-24's paper was image-set; its recoverable questions are folded in) · sequenced to teach from first question to last

> Group A → B → C inside each unit; every answer shows complete working (maths marks are working marks) and ends with a **Concept bridge**. Tags: [22] [24] real papers; [TB] textbook-fill; [P-26] pattern prediction.

---

# UNIT 1 — SEQUENCES & SERIES: QUESTIONS

**Q1. [24] The series Σ 1/nᵖ is convergent if ______.**
**Answer: p > 1.**
*Bridge:* The p-series is the measuring stick for the comparison test — internalize 1/n diverges, 1/n² converges.

**Q2. [22] On which region can log(1+x) be expanded in an infinite series?**
**Answer: −1 < x ≤ 1** (log(1+x) = x − x²/2 + x³/3 − …; diverges at x = −1, conditionally converges at x = 1).

**Q3. [22] Nature of the series Σ 1/√n?**
**Answer: divergent** (p = ½ ≤ 1).

**Q4. [24] Coefficient of the cubic term when sin x is expanded about x = π/2?**
**Answer: 0.** sin x = cos(x−π/2) = 1 − (x−π/2)²/2! + (x−π/2)⁴/4! − … — only even powers.
*Bridge:* Expansion "about a" means powers of (x−a); check parity before computing anything.

**Q5. [24 B5] Find the Taylor's series expansion of sin x.**
**Model answer.** f = sin x, derivatives cycle (cos, −sin, −cos, sin); at 0: 0,1,0,−1,… → $\sin x = x - \tfrac{x^3}{3!} + \tfrac{x^5}{5!} - \cdots = \sum(-1)^n\tfrac{x^{2n+1}}{(2n+1)!}$. Radius: ratio of successive terms → 0 for all x ⇒ **converges everywhere**. [State f⁽ⁿ⁾(0) table + general term + radius — that's the 5-mark anatomy.]

**Q6. [22 B2] Test the convergence of Σ nⁿxⁿ/n! (x > 0).**
**Model answer.** Ratio test: aₙ₊₁/aₙ = x·(1+1/n)ⁿ → x·e. Converges for **x < 1/e**, diverges for x > 1/e; at x = 1/e the ratio → 1 with aₙ ~ 1/√(2πn) (Stirling) → terms ↛ fast enough — **diverges**. 

**Q7. [22 C7(a,b)] Test convergence: (a) nth term uₙ = [√(n+1) − √n]; (b) Σ (n!)²/(2n)! xⁿ-type.**
**Model answer.** (a) uₙ = 1/(√(n+1)+√n) ~ 1/(2√n): limit-compare with Σ1/√n → **divergent**. (b) Ratio: ((n+1)!)²(2n)!/((n!)²(2n+2)!) = (n+1)²/((2n+1)(2n+2)) → 1/4 → converges for x < 4, diverges x > 4 (test x = 4 separately by Raabe if asked).
*Bridge:* Rationalize-then-compare and factorial-ratio-cancellation are the two Group-C reflexes for series.

**Q8. [22 C7(c), 7 marks] Assuming validity of expansion, show that** (a standard identity, e.g. log(1+x) manipulated to a given series).
**Method.** Start from the known Maclaurin series, substitute/integrate/differentiate term-by-term inside the radius, and match coefficients — always cite "term-by-term operation valid within the interval of convergence" for the final 2 marks.

---

# UNIT 2 — PARTIAL DERIVATIVES & VECTORS: QUESTIONS

**Q9. [24] f(x,y) = x² + xy: find fₓ and $f_{y}$. — fₓ = 2x + y, $f_{y}$ = x.**

**Q10. [24] u + v = x, uv = y: find ∂(x,y)/∂(u,v).**
**Answer.** |∂x/∂u ∂x/∂v; ∂y/∂u ∂y/∂v| = |1 1; v u| = **u − v**.
*Bridge:* When (x,y) are given in terms of (u,v), differentiate directly; if the inverse is wanted, use J·J' = 1.

**Q11. [22] If u = f(y/x)-type homogeneous relation holds, then u is called — a homogeneous function** (Euler's theorem applies: x uₓ + y $u_{y}$ = nu).

**Q12. [24 B2, 5 marks] Show (∂/∂x + ∂/∂y + ∂/∂z)² u = −9/(x+y+z)² for u = log(x³+y³+z³−3xyz).**
**Model answer.** Factor: x³+y³+z³−3xyz = (x+y+z)(x²+y²+z²−xy−yz−zx). Key computation: uₓ+$u_{y}$+$u_{z}$. Each uₓ = (3x²−3yz)/(x³+y³+z³−3xyz); summing numerators: 3(x²+y²+z²−xy−yz−zx) → sum = 3(x²+y²+z²−xy−yz−zx)/[(x+y+z)(x²+y²+z²−xy−yz−zx)] = **3/(x+y+z)**. Then (∂ₓ+∂_y+∂_z) applied to 3/(x+y+z): each partial gives −3/(x+y+z)², three of them → **−9/(x+y+z)²**. ∎
*Bridge:* The operator (∂ₓ+∂_y+∂_z) acting on any g(x+y+z) equals 3g′(x+y+z) — spot the pattern once and this 5-marker takes four lines.

**Q13. [22 C8(a)] u = log r, r² = x²+y²(+z²): prove the stated Laplacian identity.**
**Method.** rₓ = x/r; uₓ = x/r²; uₓₓ = (r² − 2x²)/r⁴; sum over variables → ∇²u = (n−2)/r² for n variables (⇒ 0 in 2D — log r is harmonic). Show the chain rule steps explicitly.

**Q14. [24 C7(a), 10 marks] Maxima/minima/saddle of f = x³ + y³ − 3x − 12y + 20.**
**Model answer (complete working in Concept Ch. 2.3):** stationary points (±1, ±2); D = 36xy; **min at (1,2), f = 2; max at (−1,−2), f = 38; saddles at (1,−2), (−1,2)**.

**Q15. [22 C8(b)] Show f(x,y) has neither max nor min at (0,0) (D = 0 case).**
**Method.** When rt − s² = 0 the test is silent: examine paths — e.g. for f = x³y² or x⁴−y⁴-type, find one approach where f > f(0,0) and another where f < f(0,0) ⇒ saddle behaviour ⇒ neither. The path argument IS the answer.

**Q16. [22 C8(c), 5 marks] Determine m so that F = (mx − 3y)i + (2y + z)j + (x − 2z)k-type is solenoidal.**
**Model answer.** Solenoidal ⇔ div F = 0: ∂ₓF₁ + ∂_yF₂ + ∂_zF₃ = m + 2 − 2 = m ⇒ **m = 0** (adapt constants to the given F; method identical).

**Q17. [24 C7(b), 5 marks] F = grad(x³+y³+z³−3xyz): find div F and curl F.**
**Answer.** F = (3x²−3yz, 3y²−3zx, 3z²−3xy). div F = 6x+6y+6z = **6(x+y+z)**. curl F = **0** — curl of a gradient vanishes identically; verify one component: ∂_y F₃ − ∂_z F₂ = −3x − (−3x) = 0 ✓.

**Q18. [22 B3] z = f(u,v), u = sin xy (chain-rule composite): find ∂z/∂x.**
**Method.** ∂z/∂x = $z_{u}$·uₓ + $z_{v}$·vₓ with uₓ = y cos xy etc. Write the dependency tree first, then one term per branch — the tree diagram earns marks.

---

# UNIT 3 — MULTIPLE INTEGRALS & THEOREMS: QUESTIONS

**Q19. [24] ∫₀¹∫₀¹ (x+y) dx dy = ?**
**Solution.**

```{=latex}
\begin{align*}
I &= \int_0^1\!\!\int_0^1 (x+y)\,dx\,dy
   = \int_0^1\Big[\frac{x^2}{2} + xy\Big]_0^1 dy && \text{(inner integration w.r.t.\ }x\text{)}\\[2pt]
  &= \int_0^1\Big(\frac12 + y\Big)dy
   = \frac12 + \frac12
\end{align*}
```

$$\therefore\ I = \mathbf{1}$$

**Q20. [24]** $\int_0^{\pi/2}\!\int_0^1 r\sin\theta\,dr\,d\theta = [-\cos\theta]_0^{\pi/2}\cdot\big[\tfrac{r^2}{2}\big]_0^1 = \mathbf{\tfrac12}$.

**Q21. [22] Area bounded by y = eˣ, x-axis, x = 0, x = 1 → ∫₀¹eˣdx = **e − 1**.**
**Solution.**

```{=latex}
\begin{align*}
A &= \int_0^1 e^x\,dx = \big[e^x\big]_0^1 = e - 1
\end{align*}
```

$$\therefore\ A = \mathbf{e-1}\ \text{square units (a Group A speed mark).}$$

**Q22. [22] If C is the circle $x^2+y^2=4$, value of $\oint(x\,dy - y\,dx)$?**
**Answer.** Green: $= \iint(1-(-1))\,dA = 2\cdot\text{Area} = 2\cdot4\pi = 8\pi$.
*Bridge:* $\tfrac12\oint(x\,dy-y\,dx)$ = area — one of the two Green's corollaries MAKAUT tests; the other is turning nasty line integrals into trivial double integrals.

**Q23. [24 B3, 5 marks] Evaluate ∫∫ xy(x+y) dxdy over the region between y = x² and y = x.**
**Model answer.** Intersect at $(0,0),(1,1)$;
$$\int_0^1\!\!\int_{x^2}^{x}\!(x^2y+xy^2)\,dy\,dx = \int_0^1\!\Big[\tfrac{x^2y^2}{2}+\tfrac{xy^3}{3}\Big]_{x^2}^{x}dx = \int_0^1\!\Big(\tfrac{5x^4}{6}-\tfrac{x^6}{2}-\tfrac{x^7}{3}\Big)dx = \tfrac16-\tfrac1{14}-\tfrac1{24} = \mathbf{\tfrac{3}{56}}$$
*(Arithmetic: LCM 168: 28/168 − 12/168 − 7/168 = 9/168 = 3/56.)*

**Q24. [24 C8(a), 8 marks] ∫∫ y dxdy over the region between y = x and y = 4x − x².**
**Solution.**

*Step 1 — intersections.* $x = 4x - x^2 \Rightarrow x(x-3) = 0 \Rightarrow x = 0,\ 3$; for $0\le x\le3$ the parabola lies above the line.

*Step 2 — set up and integrate the inner $y$:*

```{=latex}
\begin{align*}
I &= \int_0^3\!\!\int_{x}^{4x-x^2} y\,dy\,dx
   = \int_0^3 \Big[\frac{y^2}{2}\Big]_{x}^{4x-x^2} dx
   = \frac12\int_0^3\big[(4x-x^2)^2 - x^2\big]\,dx
\end{align*}
```

*Step 3 — expand and integrate:*

```{=latex}
\begin{align*}
I &= \frac12\int_0^3 \big(15x^2 - 8x^3 + x^4\big)\,dx
   = \frac12\Big[5x^3 - 2x^4 + \frac{x^5}{5}\Big]_0^3\\[2pt]
  &= \frac12\Big(135 - 162 + \frac{243}{5}\Big)
   = \frac12\cdot\frac{108}{5}
\end{align*}
```

$$\therefore\ I = \mathbf{\dfrac{54}{5}} = 10.8$$

**Q25. [24 C8(b), 7 marks] Change the order and evaluate $I = \int_0^1\!\int_{e^x}^{e}\frac{dy\,dx}{y\log y}$ (inner $dy$ from $e^x$ to $e$).**
**Solution.**

*Step 1 — describe the region both ways.*

```{=latex}
\begin{align*}
R:\quad 0\le x\le 1,\ \ e^{x}\le y\le e
\qquad\Longleftrightarrow\qquad
1\le y\le e,\ \ 0\le x\le \log y
\end{align*}
```

*Step 2 — reverse the order (the original inner integral has no elementary antiderivative):*

```{=latex}
\begin{align*}
I &= \int_1^e\!\!\int_0^{\log y} \frac{dx\,dy}{y\log y}
   = \int_1^e \frac{[\,x\,]_0^{\log y}}{y\log y}\,dy && \text{(inner integral is just a length)}\\[2pt]
  &= \int_1^e \frac{\log y}{y\log y}\,dy
   = \int_1^e \frac{dy}{y} = \big[\log y\big]_1^e
\end{align*}
```

$$\therefore\ I = \mathbf{1}$$

*State the observation explicitly in the exam: swapping the order collapses the impossible inner integral — that sentence carries marks.*

**Q26. [TB] Statements of Green's, Stokes' and Gauss' theorems (syllabus: statements only).**
**Answer.** As boxed in Concept Ch. 3.3 — memorize with the "dimension ladder": Green (1D boundary ↔ 2D region), Stokes (curve ↔ surface), Gauss (surface ↔ volume).

---

# UNIT 4 — DIFFERENTIAL EQUATIONS: QUESTIONS

**Q27. [22] General form of Clairaut's equation? — y = px + f(p).**

**Q28. [24] General solution of y = px + a/p? — y = cx + a/c.**

**Q29. [24] Singular solution of y = px + a√(1+p²)? — x² + y² = a²** (envelope of the line family).

**Q30. [24] (1/D)(x²) = ? — x³/3** (1/D = integration).

**Q31. [24] D(sin 3x) = ? — 3 cos 3x.**

**Q32. [24 B4, 5 marks] Solve xp² + (y − x)p − y = 0.**
**Solution.** Treat the equation as a quadratic in $p$ and factor:

```{=latex}
\begin{align*}
xp^2 + (y-x)p - y &= 0\\
xp^2 + yp - xp - y &= 0\\
p(xp + y) - (xp + y) &= 0\\
(p-1)(xp+y) &= 0
\end{align*}
```

*Factor 1:* $p = 1$

```{=latex}
\begin{align*}
\frac{dy}{dx} = 1 \;\Rightarrow\; \mathbf{y = x + c} \tag{i}
\end{align*}
```

*Factor 2:* $xp = -y$

```{=latex}
\begin{align*}
\frac{dy}{y} = -\frac{dx}{x} \;\Rightarrow\; \log y = -\log x + \log c \;\Rightarrow\; \mathbf{xy = c} \tag{ii}
\end{align*}
```

$$\therefore\ \text{General solution: } (y - x - c)(xy - c) = 0$$

*Bridge:* "solvable for $p$" = factor the polynomial in $p$; each linear factor is a first-order ODE; multiply the solutions.

**Q33. [24 B6, 5 marks] Solve y″ + a²y = cos ax by variation of parameters.**
**Solution.** The CF of $y'' + a^2y = 0$ is

```{=latex}
\begin{align*}
y_c &= A\cos ax + B\sin ax, \qquad y_1 = \cos ax,\ y_2 = \sin ax
\end{align*}
```

*Step 1 — Wronskian:*

```{=latex}
\begin{align*}
W &= y_1y_2' - y_2y_1' = a\cos^2 ax + a\sin^2 ax = a
\end{align*}
```

*Step 2 — variation-of-parameters formula* with $X = \cos ax$:

```{=latex}
\begin{align*}
y_p &= -y_1\!\int\!\frac{y_2X}{W}dx + y_2\!\int\!\frac{y_1X}{W}dx\\[2pt]
    &= -\cos ax\int\frac{\sin ax\cos ax}{a}\,dx + \sin ax\int\frac{\cos^2 ax}{a}\,dx\\[2pt]
    &= -\cos ax\cdot\frac{\sin^2 ax}{2a^2} + \sin ax\cdot\frac{1}{a}\Big(\frac{x}{2} + \frac{\sin 2ax}{4a}\Big)
\end{align*}
```

*Step 3 — simplify* (terms proportional to the CF are absorbed into $A, B$):

$$\boxed{\,y = A\cos ax + B\sin ax + \frac{x\sin ax}{2a}\,}$$

*Bridge:* RHS $\in$ CF $\Rightarrow$ resonance $\Rightarrow$ the $x$-multiplied particular solution. Memorize $y_p = -y_1\!\int\! y_2X/W + y_2\!\int\! y_1X/W$.

**Q34. [24 C9(a), 8 marks] Solve (2x + 3y + 7)dx + (3x − 5y + 2)dy = 0.**
**Solution.**

*Step 1 — test exactness.* $M = 2x+3y+7$, $N = 3x-5y+2$:

```{=latex}
\begin{align*}
\frac{\partial M}{\partial y} = 3 = \frac{\partial N}{\partial x} \quad\Rightarrow\quad \text{exact.}
\end{align*}
```

*Step 2 — integrate $M$ w.r.t. $x$ (holding $y$):*

```{=latex}
\begin{align*}
\int M\,dx &= x^2 + 3xy + 7x
\end{align*}
```

*Step 3 — add the terms of $N$ free of $x$:*

```{=latex}
\begin{align*}
\int(-5y+2)\,dy &= -\frac{5y^2}{2} + 2y
\end{align*}
```

$$\therefore\quad \boxed{\,x^2 + 3xy + 7x - \frac{5y^2}{2} + 2y = c\,}$$

*(Verify by taking the total differential — 1 mark.)*

**Q35. [24 C9(b), 7 marks] Orthogonal trajectories of x² + y² = r².**
**Solution.**

*Step 1 — ODE of the family.* Differentiate $x^2 + y^2 = r^2$:

```{=latex}
\begin{align*}
2x + 2y\frac{dy}{dx} = 0 \;\Rightarrow\; \frac{dy}{dx} = -\frac{x}{y}
\end{align*}
```

*Step 2 — orthogonality: replace $\dfrac{dy}{dx}$ by $-\dfrac{1}{dy/dx}$:*

```{=latex}
\begin{align*}
\frac{dy}{dx}\;\longrightarrow\;-\frac{1}{dy/dx}:\qquad -\frac{1}{dy/dx} = -\frac{x}{y} \;\Rightarrow\; \frac{dy}{dx} &= \frac{y}{x}
\end{align*}
```

*Step 3 — separate and integrate:*

```{=latex}
\begin{align*}
\frac{dy}{y} = \frac{dx}{x} \;\Rightarrow\; \log y = \log x + \log c
\end{align*}
```

$$\therefore\quad \boxed{\,y = cx\,}\ \text{— straight lines through the origin (radii cut circles at right angles ✓).}$$

**Q36. [24 C10, 15 marks] Solve (x²D² + 3xD + 2)y = cos(log x).**
**Solution (Cauchy–Euler, full 15-mark working).**

*Step 1 — substitute* $x = e^t$, $\theta \equiv \dfrac{d}{dt}$, so $xD = \theta$, $x^2D^2 = \theta(\theta-1)$:

```{=latex}
\begin{align*}
\big[\theta(\theta-1) + 3\theta + 2\big]y &= \cos t\\
(\theta^2 + 2\theta + 2)\,y &= \cos t \tag{1}
\end{align*}
```

*Step 2 — complementary function.* Auxiliary equation:

```{=latex}
\begin{align*}
m^2 + 2m + 2 = 0 \;\Rightarrow\; m = -1 \pm i\\
y_c = e^{-t}\,(A\cos t + B\sin t)
\end{align*}
```

*Step 3 — particular integral.* Put $\theta^2 \to -1$ in (1):

```{=latex}
\begin{align*}
y_p &= \frac{1}{\theta^2+2\theta+2}\cos t
     = \frac{1}{2\theta+1}\cos t && (\theta^2\to-1)\\[2pt]
    &= \frac{2\theta-1}{4\theta^2-1}\cos t && \text{(multiply by }\tfrac{2\theta-1}{2\theta-1}\text{)}\\[2pt]
    &= \frac{-2\sin t - \cos t}{-5} = \frac{\cos t + 2\sin t}{5} && (4\theta^2-1 \to -5)
\end{align*}
```

*Step 4 — back-substitute* $t = \log x$:

$$\boxed{\,y = \frac1x\big(A\cos(\log x) + B\sin(\log x)\big) + \frac{\cos(\log x) + 2\sin(\log x)}{5}\,}$$

*Marks anatomy: substitution 3 · CF 4 · PI 6 · back-substitution 2.*

**Q37. [TB — completes the unit] Solve a Bernoulli equation: dy/dx + y/x = y² log x-type.**
**Method.** Divide by y², set v = 1/y ⇒ linear in v: −v′ + v/x = log x → IF = 1/x … The recipe (divide by $y^n$, $v = y^{1-n}$, linear) is what the 5 marks buy.

---

# UNIT 5 — GRAPH THEORY: QUESTIONS

**Q38. [24] If a path is a subgraph, the degree of intermediate vertices is — 2** (end vertices 1).

**Q39. [22] Adjacency matrix size for 5 vertices, 7 edges — 5×5** (vertex count only; the incidence matrix would be 5×7).

**Q40. [22] Eccentricity of the vertex of a one-vertex graph — 0.**

**Q41. [24] A binary tree has exactly — one root** (equivalently: a full binary tree has an odd number of vertices; give the completion the blank asks).

**Q42. [TB] State the Euler-circuit criterion and contrast Euler vs Hamiltonian.**
**Answer.** Euler circuit ⇔ connected + every vertex of even degree (trail: exactly 0 or 2 odd vertices). Euler visits every **edge** once; Hamiltonian every **vertex** once; Euler has a clean degree test, Hamiltonicity has no simple criterion (NP-complete) — the asymmetry is the point of the question.

**Q43. [TB] Prove: a tree with n vertices has n − 1 edges.**
**Method.** Induction on n: removing a leaf (exists in every finite tree) gives a tree with n−1 vertices and, by hypothesis, n−2 edges; re-attach the leaf: n−1 edges. Base n=1 trivial. ∎

**Q44. [24 C11, 15 marks] Describe Kruskal's and Prim's algorithms for minimal spanning tree, with examples.**
**Model answer.** 
**Kruskal:** sort edges ascending; scan, adding any edge that joins two different components (no cycle — union-find); stop at n−1 edges. **Prim:** start at any vertex; repeatedly add the minimum-weight edge from tree to non-tree vertex until all vertices in.
**Worked example (use this 5-vertex graph):** V = {A,B,C,D,E}, weights AB=1, BC=2, AC=3, BD=4, CD=5, CE=6, DE=7.
Kruskal: AB(1)✓, BC(2)✓, AC(3)✗ cycle, BD(4)✓, CD(5)✗ cycle, CE(6)✓ → MST {AB,BC,BD,CE}, weight **13**.
Prim from A: A–B(1), B–C(2), B–D(4), C–E(6) → same tree, weight 13 ✓.
Present both runs as step tables (edge / accept-reject / reason), state both always agree on total weight (MST uniqueness when weights distinct), and close: Kruskal O(E log E), edge-driven, best sparse; Prim O(E log V) with a heap, vertex-driven, best dense.

---

# THE PATTERN MAP (Maths-III)

| Topic | 22-23 | 24-25 | 2026 verdict |
|---|---|---|---|
| Series convergence tests | A + B + C | A | **Certain** |
| Taylor/Maclaurin | C(c) | A + B | **Certain** |
| Euler's theorem / composite identity | C(a) | B | Near-certain |
| Jacobian | A | A | **Certain (Group A)** |
| Maxima/minima/saddle | C(b) | C(10) | **Certain** |
| grad/div/curl/solenoidal | C(c) | C(5) | **Certain** |
| Double integral over parabola-line region | — | B + C(8) | Near-certain |
| Change of order | — | C(7) | Likely |
| Green/circle line integrals | A×2 | — | Due |
| Clairaut general+singular | A + B | A×2 | **Certain (Group A)** |
| Solvable for p | — | B | Likely |
| Cauchy-Euler / variation of parameters | — | B + C(15) | **Near-certain** |
| Kruskal & Prim | — | C(15) | Likely repeat |
| Graph one-liners | A×3 | A×2 | **Certain (Group A)** |

*— End of the Mathematics-III Question-Answer Book: 44 questions with full working. —*
