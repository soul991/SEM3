# ECONOMICS FOR ENGINEERS — The Complete Concept Book
### MAKAUT HSMC-301 (Humanities-II) · Built from Newnan (Engineering Economic Analysis) + Panneerselvam + 3 years of real MAKAUT papers

> Economics answers are definitions + numericals. Every chapter: *why → the concept in plain words → the formulas → worked real-exam numericals → Exam Focus → rapid recall.* Format: 70 marks; A 10×1, B 3×5, C 3×15.

---

# UNIT 1 — ECONOMIC DECISIONS, COSTS & ESTIMATION

## Chapter 1: Economic Decision Making

### 1.1 Why engineers need economics

Every design competes for money. Engineering economics is the toolkit for choosing among alternatives whose costs and benefits arrive at *different times* — which is why the time value of money (Unit 2) is its beating heart.

**The rational decision process (2023-24 Group C 10(a)):** 1 recognize the problem → 2 define the goal/objective → 3 assemble relevant data → 4 identify feasible alternatives → 5 select the decision criterion → 6 construct the model → 7 predict each alternative's outcomes → 8 choose the best alternative → 9 audit the result. Present as a numbered list with one line each; add an engineering example (choosing a pump/machine) for the top marks.

**Ethics in engineering economy (2023-24 Group B):** honest estimates (no biased data), safety not traded for cost, lifecycle/environmental responsibility, transparent comparison of alternatives — link each to a stage of the decision process.
**Green engineering (2022-23 Group B):** designing products/processes that minimize environmental burden across the life cycle — resource efficiency, waste minimization, benign materials, end-of-life recovery; tie to life-cycle costing.

## Chapter 2: Engineering Costs — the vocabulary MAKAUT farms for Group A/B

| Cost | Meaning | The exam hook |
|---|---|---|
| **Fixed** | doesn't change with output (rent, salaries, depreciation) | total constant, **per-unit falls** with volume |
| **Variable** | proportional to output (materials, direct labour) | **per-unit constant**, total rises — "better describes variable cost" (2024-25 A(VII)): constant per unit |
| Marginal | cost of one more unit | decision-making at the margin |
| Average | total ÷ units | **2024-25 A(XII) worked:** fixed 32,00,000 ÷ 7,80,000 units = **Rs 4.10/unit average fixed cost** |
| Sunk | already spent, unrecoverable | **irrelevant to future decisions** — the trap answer |
| Opportunity | value of the best forgone alternative | the "cost" of using your own resources |
| Incremental | difference between alternatives | basis of replacement analysis |
| Recurring / Non-recurring | repetitive (maintenance) vs one-off (purchase, R&D) | 2023-24 Group B definition pair |
| Cash vs Book | actual outlay vs accounting entry (depreciation) | book costs don't move cash |
| Life-cycle | total from design → disposal | argues for spending early to save later |

**Break-even analysis (numericals every single year):**
BEP(units) = **F / (p − v)** where contribution/unit = p − v; BEP(₹) = F/(P/V ratio); **P/V ratio = contribution/sales**; Margin of safety = actual sales − BEP sales (= profit/(P/V ratio)).

```{=latex}
\begin{center}\begin{tikzpicture}
\begin{axis}[width=9cm,height=6cm,xlabel={\scriptsize units (thousands)},ylabel={\scriptsize amount (thousand ₹)},xmin=0,xmax=4.4,ymin=0,ymax=115,legend style={font=\scriptsize,at={(0.02,0.98)},anchor=north west},title={\small Break-even: revenue crosses total cost}]
\addplot[very thick,accent,domain=0:4.4]{25*x}; \addlegendentry{Total revenue}
\addplot[very thick,mintedge,domain=0:4.4]{18+17.5*x}; \addlegendentry{Total cost}
\addplot[dashed,gray,domain=0:4.4]{18}; \addlegendentry{Fixed cost}
\addplot[only marks,mark=*] coordinates {(2.4,60)};
\node at (axis cs:2.4,70) {\scriptsize BEP};
\end{axis}\end{tikzpicture}\end{center}
```

**Worked (2024-25 A(III)):** p = 10, v = 6, F = 5000 → BEP = 5000/4 = **1250 units**.
**Worked (2024-25 A(X)):** sales 1,50,000, P/V 40% → contribution = **60,000**.
**Worked — the two-year P/V classic (2024-25 B5, 5 marks):**

*Sales/profit — 2009: ₹2,70,000 / ₹6,000; 2010: ₹3,00,000 / ₹15,000. Cost structure and prices unchanged. Find (a) P/V ratio, (b) fixed cost, (c) break-even point, (d) margin of safety at a profit of ₹24,000.*

**Solution.**

*(a) P/V ratio from the change between the two years:*

```{=latex}
\begin{align*}
\text{P/V} &= \frac{\Delta\text{Profit}}{\Delta\text{Sales}} = \frac{15{,}000-6{,}000}{3{,}00{,}000-2{,}70{,}000} = \frac{9{,}000}{30{,}000} = \mathbf{30\%}
\end{align*}
```

*(b) Fixed cost from 2009 (contribution = fixed cost + profit):*

```{=latex}
\begin{align*}
\text{Contribution}_{2009} &= 0.30\times2{,}70{,}000 = 81{,}000\\
F &= 81{,}000 - 6{,}000 = \mathbf{75{,}000}
\end{align*}
```

*(c) Break-even sales:*

```{=latex}
\begin{align*}
\text{BEP} &= \frac{F}{\text{P/V}} = \frac{75{,}000}{0.30} = \mathbf{2{,}50{,}000}
\end{align*}
```

*(d) Margin of safety at profit ₹24,000:*

```{=latex}
\begin{align*}
\text{Required sales} &= \frac{F+\text{profit}}{\text{P/V}} = \frac{99{,}000}{0.30} = 3{,}30{,}000\\
\text{MoS} &= 3{,}30{,}000 - 2{,}50{,}000 = \mathbf{80{,}000}
\end{align*}
```

*Check:* MoS $=$ profit/(P/V) $= 24{,}000/0.3 = 80{,}000$ ✓ — quote this for the final mark.

## Chapter 3: Estimation

**"Estimation is the foundation of economic analysis" (2022-23 Group B):** every criterion (PW, IRR, B/C) consumes *estimates* of future costs/benefits/lives; garbage in → garbage out; hence estimate types (rough ±30-60%, budget ±15%, detailed ±5%) and structured models:

- **Per-unit model:** cost = unit rate × quantity (₹/km, ₹/m²).
- **Segmenting model:** decompose into components, estimate each, sum.
- **Cost indexes:** cost_now = cost_then × (index_now/index_then) — inflation-adjusts historical data.
- **Power-sizing model:** cost₂ = cost₁ × (size₂/size₁)^x, x = power-sizing exponent (<1 ⇒ economies of scale). **(2023-24 A(VII): its usage — scaling equipment cost with capacity.)**
- **Learning curve (2022-23 C9(a)):** each doubling of cumulative output cuts unit time/cost to a fixed % (e.g. 80% curve): $T_{N}$ = T₁·$N^{b}$, b = log(rate)/log 2.

**The 2024-25 B2 numerical (cost index + power sizing combined) — worked in full:**

*1982 machinery cost ₹30,00,000 (300 MW); material : labour : overhead = 5 : 3 : 2; present indexes 250/300/240; find the present cost of machinery of double capacity, power-sizing exponent $x = 0.8$.*

**Solution.**

*Step 1 — split the 1982 cost in the ratio 5 : 3 : 2:* Material 15 L, Labour 9 L, Overheads 6 L.

*Step 2 — escalate each component by its own index:*

```{=latex}
\begin{align*}
\text{Present cost (same capacity)} &= 15\times\tfrac{250}{100} + 9\times\tfrac{300}{100} + 6\times\tfrac{240}{100}\\
 &= 37.5 + 27 + 14.4 = \mathbf{78.90\ \text{lakh}}
\end{align*}
```

*Step 3 — scale to double capacity (power-sizing):*

```{=latex}
\begin{align*}
C_2 &= C_1\left(\frac{S_2}{S_1}\right)^{x} = 78{,}90{,}000\times 2^{0.8} = 78{,}90{,}000\times1.7411
\end{align*}
```

$$\therefore\ C_2 \approx \mathbf{1{,}37{,}37{,}279} \approx \text{₹}1.374\ \text{crore}$$

*Check (weighted index):* $(250\times5+300\times3+240\times2)/10 = 263 \Rightarrow 30\,\text{L}\times2.63 = 78.9\,\text{L}$ ✓


---

# UNIT 2 — CASH FLOW, INTEREST & RATE-OF-RETURN ANALYSIS

## Chapter 4: Time Value of Money

**The principle (asked as T/F and definition every year):** a rupee today > a rupee tomorrow, because today's rupee can earn interest (and inflation erodes tomorrow's). The 2024-25 A(IX) name for it: **time value of money / discounting concept**.

**Cash-flow diagram (2022-23 A(III)):** a timeline of arrows — up = receipts, down = disbursements — at their occurrence periods; the *discounted* cash-flow method (2022-23 A(IV)) underlies both NPV and IRR.

```{=latex}
\begin{center}\begin{tikzpicture}[xscale=1.15]
\draw[thick,->] (-0.4,0)--(6.2,0) node[right]{\scriptsize years};
\foreach \x in {0,...,5}{\draw (\x,-0.07)--(\x,0.07) node[below=4pt]{\scriptsize \x};}
\draw[very thick,red!70!black,->] (0,0)--(0,-1.25) node[below]{\scriptsize $-P$ (investment)};
\foreach \x in {1,...,5}{\draw[very thick,mintedge,->] (\x,0)--(\x,0.8);}
\node[mintedge] at (3,1.15) {\scriptsize $+A$ each year (annuity receipts)};
\end{tikzpicture}\end{center}
```

**Interest formulas (single payment):** F = P(1+i)ⁿ · P = F/(1+i)ⁿ.
**Annuity A (2024-25 A(V): "fixed cash flow each year" = annuity):**
F = A[((1+i)ⁿ−1)/i] · P = A[((1+i)ⁿ−1)/(i(1+i)ⁿ)] — sinking fund and capital recovery are the inverses.

**Nominal vs effective interest (2024-25 asked it TWICE in Group A):**
r nominal annual, m compoundings: **$i_{eff}$ = (1 + r/$m)^{m}$ − 1**.
**Worked (2024-25 A(I)/(VIII)):** 10% nominal, quarterly: (1.025)⁴ − 1 = **10.38%**.
Continuous: $i_{eff}$ = $e^{r}$ − 1.

**Annual vs continuous compounding (2022-23 C8(b)):** annually interest is credited once/period; continuously it compounds at every instant (limit $m\to\infty$), $F = Pe^{rn}$; for the same r, continuous yields the most.

## Chapter 5: Evaluating Alternatives

**Present worth (NPV) (2022-23 C8(c)):** NPV = Σ CFₜ/(1+i)ᵗ − initial cost; accept if > 0; compare alternatives at the same analysis period (LCM of lives if needed); end-of-year convention.
**Future worth:** same comparison compounded forward.
**Annual cash flow (EUAC/EUAW):** convert everything to equivalent uniform annual amounts via capital recovery — best for unequal lives.
**IRR:** the i making NPV = 0; found by interpolation between trial rates; **incremental analysis** for mutually exclusive alternatives (compare ΔIRR to MARR, don't rank by raw IRR). MARR (2022-23 A(IX)): minimum attractive/required rate of return an investor demands at given risk.
**Salvage value treatment:** enters as a positive cash flow at end of life (or reduces capital recovery: CR = (P−S)(A/P,i,n) + S·i).

**Benefit-cost ratio (2022-23 Group C 7 — an entire 15-marker):**
**BCR = PW(benefits)/PW(costs)** (conventional; or ΔB/ΔC incrementally).
Used for: public-sector project screening (2022-23 7(b)). **BCR > 1 ⇒ PW of benefits exceeds costs ⇒ economically justified** (7(c)). Limitations (7(d)): sensitive to classifying disbenefits (numerator vs denominator), ignores project *scale*, needs incremental analysis for mutually exclusive projects, monetizing social benefits is subjective, discount-rate choice drives the answer.
**Sensitivity & breakeven analysis:** vary one estimate; find the value at which the decision flips — report the range over which the recommendation is stable.

---

# UNIT 3 — INFLATION, PRICE INDICES & UNCERTAINTY

## Chapter 6: Inflation

**Definition (2022-23 A(V)):** a sustained rise in the general price level = fall in purchasing power of money.
**Causes (2024-25 B3):** **demand-pull** — "too much money chasing too few goods" (2024-25 A(II) verbatim); **cost-push** — input prices push output prices (2024-25 A(XI)); monetary expansion; structural/supply shocks; imported inflation.
**Stagflation (2023-24 A(I)):** stagnation (low growth/high unemployment) + inflation together.
**Redistribution effect (2022-23 A(I)):** inflation transfers real wealth from lenders/savers/fixed-income earners to borrowers and holders of real assets — debts are repaid in cheaper rupees.
**High inflation → the central bank tightens (reduces) money supply** (2024-25 A(IV) direction question).

**Indices:** **WPI (2023-24 A(III))** — wholesale price index, bulk-transaction basket; **CPI (2023-24 C8(b))** — consumer/retail basket measuring cost of living ("retail inflation"); composite (many goods, weighted) vs commodity (single good) indexes; use in analysis: convert actual (then-current) rupees ↔ real (constant) rupees: real = actual/(index ratio).

**Real vs market interest (the golfer problem — 2023-24 C8(a), worked):**

*Bank rate 5.5% compounded annually; inflation 2%/yr. Identify $i$, $f$, $i'$. Repeat for 8% inflation.*

**Solution.** Market rate $i = 5.5\%$; inflation $f = 2\%$. Real rate from $(1+i) = (1+i')(1+f)$:

```{=latex}
\begin{align*}
i' &= \frac{1+i}{1+f} - 1 = \frac{1.055}{1.02} - 1 = \mathbf{3.43\%}\\[4pt]
\text{for } f = 8\%: \quad i' &= \frac{1.055}{1.08} - 1 = \mathbf{-2.31\%}
\end{align*}
```

A negative real rate means the deposit *loses* purchasing power despite earning nominal interest. ($i' \approx i - f$ only for small rates — state both forms.)

## Chapter 7: Uncertainty in Future Events

Estimates are ranges, not points: optimistic/most-likely/pessimistic; **mean = (O + 4M + P)/6** (beta approximation).
**Expected value:** EV = Σ pᵢ·xᵢ — the workhorse.
**Worked (2022-23-adjacent, the Gemini-verified pattern):** annual benefit $8,000 (p=0.6), $5,000 (p=0.3), $10,000 (p=0.1): EV = 4800+1500+1000 = **$7,300**; life 6 yr twice as likely as 9 yr → p = 2/3, 1/3 → EV(life) = 7 yr.
**Discrete probability distributions — "any necessity?" (2022-23 B5):** yes — future cash flows/lives are uncertain; distributions let us compute EV, variance (risk), and feed decision trees/simulation; without them analysis pretends certainty it doesn't have.
**Decision trees:** decision nodes (□), chance nodes (○), roll back EVs from leaves; **(2023-24 A(V) crossover MCQ: the decision-tree algorithm belongs to the supervised-learning family)**.
**Risk vs return (2022-23 A(XII)):** positively correlated over the long run — higher expected return prices higher risk; a two-security portfolio can be made riskless only if returns are **perfectly negatively correlated (ρ = −1)** (2023-24 A(IX)). Simulation (Monte Carlo) and real options close the toolkit.

---

# UNIT 4 — DEPRECIATION, REPLACEMENT & ACCOUNTING

## Chapter 8: Depreciation

**What/why:** systematic allocation of a tangible asset's cost over its useful life — caused by **deterioration** (physical wear) and **obsolescence** (technological/functional aging). Book value = cost − accumulated depreciation.
**The True/False bank (2022-23 asked three):** "market value > book value ⇒ no depreciation charged" — **False** (depreciation is cost allocation, not valuation). "Adequate maintenance ⇒ no depreciation needed" — **False** (obsolescence still runs). "Main objective is net-profit calculation" — **True in accounting terms** (matching cost to revenue; also tax computation).

**Types of property (2023-24 C7):** tangible — real (land, buildings) vs personal (machines, vehicles); intangible (patents, goodwill). Almost all tangible property depreciates; **land never** — unlimited useful life, no wear-out, value typically appreciates; only improvements on land depreciate.

**Methods:**
**Straight line:** Dₜ = (P − S)/n every year; BVₜ = P − t·(P−S)/n.
**Declining balance:** Dₜ = α·BVₜ₋₁ (α = 2/n for DDB); book value decays geometrically; switch to SL when advantageous; salvage not subtracted up-front.
**(Worked micro-example: P = 1,00,000, S = 10,000, n = 5: SL D = 18,000/yr; DDB α = 40%: D₁ = 40,000, D₂ = 24,000…)**
**Bonus depreciation (2023-24 C9(a), the US-tax numerical — worked):** equipment $800,000, revenue $1.25M, operating expenses $360,000, 100% bonus:
(i) first-year depreciation = **$800,000** (whole cost in year 1);
(ii) taxable income = 1,250,000 − 360,000 − 800,000 = **$90,000**;
(iii) federal tax at 21% = **$18,900**.
**Capital allowance:** the tax-law name for allowable depreciation deductions; common elements across regimes: defined life/class, method, salvage convention, recapture on sale.

## Chapter 9: Replacement Analysis

**Defender = the existing asset; challenger = the proposed replacement (2024-25 A(VI): defender = existing equipment).**
Rules: sunk costs of the defender are irrelevant; compare defender's *marginal cost* of keeping one more year against the challenger's **minimum EUAC**; **economic (minimum-cost) life** = the n minimizing EUAC = capital recovery (falling with n) + operating/maintenance (rising with n) — the U-curve. Replace when marginal cost of the defender exceeds the challenger's minimum EUAC. The replacement decision map (when data are/aren't marginal-cost computable) structures the 15-mark version.

## Chapter 10: Accounting Fundamentals

**Balance sheet (2023-24 C9(b): illustrate the model):** snapshot at a date — **Assets = Liabilities + Owners' Equity**; assets: current (cash, receivables, inventory) + fixed; liabilities: current (**accruals, notes payable, accounts payable — True, they're current liabilities**, 2023-24 A(X)) + long-term debt; equity: capital + retained earnings. Draw the two-column model with sample figures.
**Income statement (2023-24 B2):** performance over a period — revenue − expenses = net income; links to balance sheet via retained earnings.
**Cash-flow statement's three sections (2022-23 B2):** operating, investing, financing activities. (Sale of investment by a non-financial enterprise = investing activity — the 2022-23 T/F.)
**Working capital (2022-23 A(XI)):** current assets − current liabilities.
**Financial ratios:** liquidity (current = CA/CL, quick), profitability (net margin, ROA/ROE), leverage (debt/equity), activity (inventory turnover) — one formula + meaning each.
**Cost accounting & the cost sheet (2024-25 B6, worked in the QA book):** prime cost (materials + direct labour) → + factory OH = works cost → + admin OH = cost of production → + selling & distribution OH = cost of sales → + profit = sales.
**Odd-ones from the papers:** patent (2023-24 B3) — exclusive statutory right to an invention (20 yrs), an intangible asset, amortized; GST (2023-24 B5) — one destination-based tax replacing cascading multi-taxes, input-tax credit reduces effective burden; preferred stock sits above common stock, below debt in bankruptcy (2023-24 A(II)); issuing stocks and bonds = raising capital/financing activity (2023-24 A(XI)); credit purchase recorded as **accounts payable** (2023-24 A(VI)); price sensitivity of demand = **elasticity** (2023-24 A(IV)).

---

# FORMULA SHEET (HSMC-301)

BEP = F/(p−v) · P/V = contribution/sales = ΔProfit/ΔSales · MoS = profit/(P/V) · F = P(1+i)ⁿ · P(annuity) = A[((1+i)ⁿ−1)/(i(1+i)ⁿ)] · $i_{eff}$ = (1+r/$m)^{m}$ − 1; continuous $e^{r}$ − 1 · NPV = ΣCF/(1+i)ᵗ − C₀; IRR: NPV=0; BCR = PW(B)/PW(C) > 1 accept · cost index: now = then × $I_{now}$/$I_{then}$ · power sizing: C₂ = C₁(S₂/S₁)^x · learning: $T_N = T_1 N^{\log r/\log 2}$ · real rate i′ = (1+i)/(1+f) − 1 · EV = Σpx · SL: (P−S)/n; DDB: α = 2/n on BV · Assets = Liabilities + Equity · WC = CA − CL · cost sheet: prime → works → production → sales.

*— End of the Economics for Engineers Concept Book —*
