# ECONOMICS FOR ENGINEERS — The Question-Answer Book
### MAKAUT HSMC-301 · Every real PYQ of 2022-23, 2023-24, 2024-25 solved in full · sequenced to teach the subject front-to-back

> Group A → B → C inside each unit. Numericals carry complete working — in this paper the numericals are where the 45 Group-C marks live. Tags: [22] [23] [24] real papers; [TB] textbook-fill; [P-26] prediction.

---

# UNIT 1 — DECISIONS, COSTS, ESTIMATION: QUESTIONS

## A. One-markers

**Q1. [24] Which better describes variable cost? — Constant per unit, total varies with output** (fixed cost is the mirror image).

**Q2. [24] Production 7,80,000 units, fixed costs ₹32,00,000 → average fixed cost = 32,00,000/7,80,000 = ₹4.10 per unit.**

**Q3. [24] Selling price ₹10, variable ₹6, fixed ₹5,000 → BEP = 5000/(10−6) = 1,250 units.**

**Q4. [24] Sales ₹1,50,000, P/V ratio 40% → Contribution = ₹60,000.**

**Q5. [23] Sensitivity of demand to price change — (price) elasticity of demand.**

**Q6. [23] Usage of the power-sizing model — scaling equipment/plant cost with capacity: C₂ = C₁(S₂/S₁)^x.**

**Q7. [23] A firm buys but doesn't pay suppliers instantly — recorded as accounts payable (a current liability).**

**Q8. [22] What is working capital? — Current assets − current liabilities.**

## B. Five-markers

**Q9. [24] Distinguish variable cost and fixed cost.**
**Model answer.** Definition pair + behaviour (total vs per-unit) + graphs (horizontal total-fixed line, rising total-variable line) + examples (rent/depreciation vs materials/direct labour) + role in break-even (only contribution = p − v absorbs fixed cost). Note semi-variable costs exist (electricity) for the fifth mark.

**Q10. [23] What are recurring and non-recurring costs?**
**Model answer.** Recurring — repetitive, anticipated, period-by-period (maintenance, salaries, utilities); enter analyses as annuities. Non-recurring — one-off (purchase, installation, R&D, disposal); enter as single payments. One engineering example each and how each maps onto a cash-flow diagram.

**Q11. [22] "Estimation is the foundation of economic analysis" — explain.**
**Model answer.** Every criterion (PW, EUAC, IRR, B/C) computes on *estimated* future cash flows, lives, salvage, rates; decision quality is bounded by estimate quality. Present estimate grades (rough/budget/detailed with accuracy bands), the estimating models (per-unit, segmenting, indexes, power-sizing, learning curve — one line each), and close: structured models + updated indexes discipline the guesswork.

**Q12. [22] What is Green Engineering?**
**Model answer.** Design of products/processes minimizing environmental burden over the whole life cycle: source reduction, energy/resource efficiency, benign materials, recyclability, end-of-life recovery; economically framed via life-cycle costing — cheap-to-build but dirty-to-run loses on LCC. Example: pump chosen on energy cost, not price tag.

**Q13. [24] Cost-index + power-sizing numerical (1982 machinery ₹30 L, 300 MW, M:L:O = 5:3:2, indexes 250/300/240, doubling capacity, x = 0.8).**
**Model answer.** Split 15L/9L/6L → present same-capacity cost = 15×2.5 + 9×3.0 + 6×2.4 = **₹78.90 L**; double capacity ×$2^{0.8}$ = 1.7411 → **≈ ₹1.374 crore**. (Weighted index check: 263 → 30L×2.63 = 78.9L ✓.)

**Q14. [24] Cost sheet of Yuvraj & Co. (March 2005): materials 4,000; direct labour 6,000; factory OH 500; admin OH 20% of works cost; S&D OH 6 paise/unit; produced 20,000; sold 18,000 at 20% profit on selling price.**
**Model answer (the cost-sheet ladder):**
Prime cost = 4,000+6,000 = 10,000 · Works cost = +500 = 10,500 · Admin OH = 2,100 → **Cost of production = 12,600** (per unit = 12,600/20,000 = ₹0.63).
Cost of goods sold (18,000 units) = 18,000×0.63 = 11,340 · S&D = 18,000×0.06 = 1,080 → **Cost of sales = 12,420**.
Profit 20% on SP ⇒ SP = cost/0.8 = 15,525 ⇒ **Profit = ₹3,105** (SP per unit ≈ ₹0.8625). Present as a formatted cost sheet — the format itself carries marks.

## C. Fifteen-markers

**Q15. [23 C10(a)] Steps of the rational decision-making process.** — The nine steps (Concept Ch. 1) with one line + an engineering example threaded through all nine.

**Q16. [22 C9] (a) Improvement with the learning curve [7]; (b) What is triangulation? [8].**
**Model answer.** (a) $T_{N}$ = T₁N^b, b = log(learning rate)/log 2; 80% curve ⇒ each doubling cuts unit time to 80%; worked micro-example (T₁=100 h: T₂=80, T₄=64, T₈=51.2); sources: skill, setup, methods, tooling; use in bidding/scheduling repetitive production. (b) Three-point estimation: optimistic O, most-likely M, pessimistic P treated as a (triangular/beta) distribution; triangular mean = (O+M+P)/3, beta/PERT mean = (O+4M+P)/6, plus variance ((P−O)/6)² — converts single guesses into a distribution for risk analysis; tiny worked example.

---

# UNIT 2 — CASH FLOW, INTEREST, EVALUATION: QUESTIONS

## A. One-markers

**Q17. [24 — twice!] Nominal 10% p.a., quarterly compounding → effective rate = (1+0.10/4)⁴ − 1 = 10.38%.**

**Q18. [24] A fixed cash flow each year for n years — an annuity.**

**Q19. [24] "Value of a future rupee < today's rupee" — time value of money (discounting).**

**Q20. [22] Cash-flow diagram? — timeline with up-arrows (receipts) and down-arrows (payments) at their periods; the skeleton of every problem.**

**Q21. [22] The cash-flow method used by IRR and NPV — discounted cash flow (DCF).**

**Q22. [22] T/F: money now is more valuable than the same money later — True.**

**Q23. [22] Minimum expected return to persuade an investor at given risk — MARR (minimum attractive rate of return) — True as stated.**

## B/C. The evaluation questions

**Q24. [22 C8, 15 marks] (a) Time value of money [2]; (b) annual vs continuous compounding [4]; (c) net present value [5]; (d) why TVM matters [4].**
**Model answer.** (a) A rupee today can earn interest → worth more than a future rupee. (b) Annual: credited once, F = P(1+i)ⁿ; continuous: $m\to\infty$, $F = Pe^{rn}$; same nominal rate, continuous > annual (10%: 10.517% vs 10%). (c) NPV = Σ CFₜ/(1+i)ᵗ − C₀; >0 = value created at rate i; the standard accept/reject and ranking basis. (d) Enables comparison of cash flows at different times, correct lease/buy & invest/defer decisions, inflation-aware planning; without it, adding rupees across years is adding unlike quantities.

**Q25. [22 C7, 15 marks] The BCR quartet: definition [6], use [1], BCR > 1 meaning [2], limitations [6].**
**Model answer.** BCR = PW(benefits)/PW(costs) (variants: net vs disbenefit placement; incremental ΔB/ΔC). Use: public-project justification. >1: benefits exceed costs at the chosen discount rate — economically justified. Limitations: ratio hides scale (₹1.1 cr/₹1 cr beats ₹15 cr/₹10 cr on ratio, loses on net worth); classification of disbenefits changes the ratio; mutually exclusive projects need incremental BCR; monetizing social benefits subjective; discount-rate sensitivity. 

**Q26. [22 C10, 15 marks] Advantages [8] and disadvantages [7] of future worth analysis.**
**Model answer.** Advantages: natural for wealth-at-a-target-date questions (retirement, sinking funds); same decision as PW (consistent); compounding forward is intuitive for accumulation; easy comparison of terminal values. Disadvantages: distant-future values feel abstract; requires same analysis horizon; sensitive to rate & horizon estimates; less standard in industry (PW/IRR dominate) so communication suffers; inflation makes far-future rupees misleading unless real rates used.

**Q27. [24 C8, 15 marks] IRR from a table (worked): outlay 20,000; inflows 5,000/8,000/10,000/4,000; PV factors given for 12-16%.**
**Solution.** IRR is the rate at which PV(inflows) = outlay. Try the bracketing rates:

*At 13%:*

```{=latex}
\begin{align*}
\text{PV} &= 5000(.885) + 8000(.783) + 10000(.693) + 4000(.613)\\
 &= 4425 + 6264 + 6930 + 2452 = 20{,}071 \quad (> 20{,}000)
\end{align*}
```

*At 14%:*

```{=latex}
\begin{align*}
\text{PV} &= 5000(.877) + 8000(.770) + 10000(.675) + 4000(.592)\\
 &= 4385 + 6160 + 6750 + 2368 = 19{,}663 \quad (< 20{,}000)
\end{align*}
```

*Interpolate between 13% (NPV $= +71$) and 14% (NPV $= -337$):*

```{=latex}
\begin{align*}
\text{IRR} &= 13 + \frac{71}{71 + 337}\times1 = 13 + \frac{71}{408}
\end{align*}
```

$$\therefore\ \text{IRR} \approx \mathbf{13.17\%}$$

*(The two PV computations line by line are 10 of the 15 marks.)*

**Q28. [P-26] EUAC/annual-cost comparison of two machines with different lives.** — Convert each to EUAC = (P−S)(A/P,i,n) + S·i + annual costs; choose lower; state why EUAC beats PW for unequal lives (no LCM gymnastics).

---

# UNIT 3 — INFLATION & UNCERTAINTY: QUESTIONS

## A. One-markers

**Q29. [24] "Too much money chasing too few goods" — demand-pull inflation.**

**Q30. [24] Inflation from rising factor/input prices — cost-push inflation.**

**Q31. [23] Stagnation + inflation — stagflation.**

**Q32. [23] What is WPI? — Wholesale Price Index: price level of bulk/wholesale transactions; India's headline index historically.**

**Q33. [22] What is inflation? — sustained rise in general price level = falling purchasing power.**

**Q34. [22] How does inflation redistribute income? — from savers/lenders/fixed-income earners to borrowers/real-asset holders (debts repaid in cheaper rupees).**

**Q35. [24] High inflation leads the authority to ______ money supply — reduce (tighten).**

**Q36. [23] A two-security portfolio becomes riskless if — returns are perfectly negatively correlated (ρ = −1).**

**Q37. [23] Decision-tree algorithm belongs to the ______ family — supervised learning.**

**Q38. [22] Risk-return correlation over the long period — highly positive (True).**

## B/C. The worked set

**Q39. [24 B3] State the causes of inflation.** — Demand-pull, cost-push, monetary expansion, structural/supply shocks, imported inflation, expectations spiral; one line + one example each.

**Q40. [23 C8, 6+9] (a) The golfer: i = 5.5%, f = 2% → identify i, f, i′; repeat for f = 8%. (b) What is CPI/retail inflation?**
**Model answer.** (a) i (market) = 5.5%; f = 2%; real i′ = 1.055/1.02 − 1 = **3.43%**. For f = 8%: i′ = 1.055/1.08 − 1 = **−2.31%** — purchasing power shrinks despite nominal interest. Relation: (1+i) = (1+i′)(1+f). (b) CPI: weighted price of a fixed consumer basket (food, housing, fuel, clothing…) relative to a base year; its % change = retail inflation; used for DA/wage indexation, monetary policy targeting, converting actual→real rupees.

**Q41. [22 C11, 5+2+8] (a) How is CPI used to measure inflation? (b) Does a CPI increase mean inflation? (c) Probability distributions for annual benefit (most-likely 8000 @60%, 5000 @30%, highest 10000) and life (6 yr twice as likely as 9 yr).**
**Model answer.** (a) inflation rate = (CPIₜ − CPIₜ₋₁)/CPIₜ₋₁ × 100 on the fixed-basket index. (b) Not necessarily — a one-month uptick or a basket/seasonal effect isn't *sustained general* price rise; inflation needs persistence. (c) Benefit: P(8000) = 0.6, P(5000) = 0.3, P(10000) = 0.1 (sums to 1 ✓); EV = 4800+1500+1000 = **$7,300**. Life: P(6) = 2/3, P(9) = 1/3; EV = 4+3 = **7 years**. Present both as distribution tables; the EVs feed any subsequent PW analysis.

---

# UNIT 4 — DEPRECIATION, REPLACEMENT, ACCOUNTING: QUESTIONS

## A. One-markers (the T/F harvest)

**Q42. [22] Market value > book value ⇒ depreciation not charged — False** (allocation, not valuation).

**Q43. [22] Adequate maintenance ⇒ no depreciation — False** (obsolescence continues).

**Q44. [22] Depreciation's main objective is net-profit calculation — True** (cost-revenue matching + tax).

**Q45. [24] In replacement analysis the defender is — a) existing equipment.**

**Q46. [23] Debenture owner is entitled to fixed-rate interest — True.**

**Q47. [23] In bankruptcy, recorded above common stock, below debt — preferred stock.**

**Q48. [23] Accruals, notes payable, accounts payable are current liabilities — True.**

**Q49. [23] Issuing stocks and bonds results in — raising capital (financing activity).**

**Q50. [22] Sale of investment by a non-financial enterprise = investing activity — True.**

## B. Five-markers

**Q51. [23] What is an income statement?** — Period statement: revenues − expenses = net income; structure (revenue, COGS, gross profit, operating expenses, EBIT, interest, tax, net income); links to balance sheet through retained earnings; contrast with the balance sheet's point-in-time nature.

**Q52. [23] What is a patent?** — Statutory exclusive right to an invention (~20 yrs); an intangible asset; capitalized and amortized over legal/useful life; economic role: appropriating R&D returns.

**Q53. [23] How can GST relieve overall tax burden?** — One destination-based tax replacing cascading excise/VAT/service layers; input-tax credit removes tax-on-tax; uniform rates cut compliance and logistics costs; formalization widens the base allowing lower effective rates.

**Q54. [22] Expenditures on depreciable assets — short note.** — Capital expenditures (asset cost + installation + freight) are capitalized, not expensed; recovered over life via depreciation; contrast revenue expenditures (repairs) expensed immediately; the classification drives taxable income timing.

**Q55. [22] Necessity of discrete probability distributions?** — As Q41(c): they turn uncertain futures into computable EV/variance and power decision trees & simulation.

## C. Fifteen-markers (the numerical heart of the paper)

**Q56. [24 C7, 15 marks — the factory break-even suite, fully worked.]**
Data: sales 4,000 units @ ₹25 = 1,00,000; materials 40,000; variable OH 10,000; labour 20,000; fixed OH 18,000; profit 12,000.

**Solution.** *First build the contribution table — every sub-part reads off it:*

```{=latex}
\begin{align*}
\text{Variable cost} &= 40{,}000 + 10{,}000 + 20{,}000 = 70{,}000 \;\Rightarrow\; v = 17.50/\text{unit}\\
\text{Contribution/unit} &= p - v = 25 - 17.50 = 7.50 \;\Rightarrow\; \text{P/V} = 7.5/25 = 30\%
\end{align*}
```

**(a) Break-even units:**

```{=latex}
\begin{align*}
\text{BEP} &= \frac{F}{p-v} = \frac{18{,}000}{7.50} = \mathbf{2{,}400\ \text{units}}
\end{align*}
```

**(b) Sales for a profit of 20% on sales:**

```{=latex}
\begin{align*}
0.30\,S &= 18{,}000 + 0.20\,S\\
0.10\,S &= 18{,}000 \;\Rightarrow\; S = \mathbf{1{,}80{,}000}\ (7{,}200\ \text{units})
\end{align*}
```

**(c) Extra units for the present profit (12,000) after cutting SP:**

*SP down 20% ($p = 20$, $c = 2.50$):*

```{=latex}
\begin{align*}
\text{units} &= \frac{18{,}000+12{,}000}{2.50} = 12{,}000 \;\Rightarrow\; \text{extra} = \mathbf{8{,}000}
\end{align*}
```

*SP down 25% ($p = 18.75$, $c = 1.25$):*

```{=latex}
\begin{align*}
\text{units} &= \frac{30{,}000}{1.25} = 24{,}000 \;\Rightarrow\; \text{extra} = \mathbf{20{,}000}
\end{align*}
```

**(d) Selling price for BEP = 500 units:**

```{=latex}
\begin{align*}
500 &= \frac{18{,}000}{p - 17.50} \;\Rightarrow\; p - 17.50 = 36
\end{align*}
```

$$\therefore\ p = \mathbf{53.50}\ \text{(₹)}$$

**Q57. [24 C9, 5+10] Depreciation: meaning + methods.** — Definition/causes (deterioration, obsolescence) then SL, declining balance/DDB, (sum-of-years, units-of-production for completeness) each with formula + a shared worked example (P = 1,00,000, S = 10,000, n = 5) and a comparison table (charge pattern, book-value path, tax effect).

**Q58. [23 C7, 5+4+6] Types of property; "almost all tangible property can be depreciated"; "land is never depreciated".**
**Answer.** Real vs personal tangible property, intangibles; tangible assets wear out/obsolesce over determinable lives ⇒ depreciable when used for production/business with life > 1 yr; land: unlimited life, no consumption of value through use ⇒ never depreciated (improvements ARE); note land may still *appreciate* — irrelevant to depreciation, which is cost allocation.

**Q59. [23 C9, 8+7] (a) Bonus-depreciation tax numerical — dep = $800,000; taxable = 1.25M − 360k − 800k = $90,000; tax @21% = $18,900. (b) Model of a balance sheet** — two-sided layout with sample numbers, Assets = Liabilities + Equity, current/fixed and current/long-term splits.

**Q60. [24 C10, 15 marks — Mr. Singh's ten taxis, fully worked.]**
**Solution.** Work *per taxi per month* throughout, then scale.

*Step 1 — fixed/standing charges (per taxi, per month):*

```{=latex}
\begin{align*}
\text{office staff } 1500/10 &= 150 & \text{supervisor } 2000/10 &= 200\\
\text{garage rent } 1000/10 &= 100 & \text{driver} &= 400\\
\text{road tax/repairs } 2160/12 &= 180 & \text{insurance } \tfrac{0.04\times75{,}000}{12} &= 250
\end{align*}
```

$$\text{Fixed total} = 150+200+100+400+180+250 = \mathbf{1{,}280}$$

*Step 2 — running charges for 4,000 km/month:*

```{=latex}
\begin{align*}
\text{petrol} &= \frac{4{,}000}{9}\times6.30 = 2{,}800\\
\text{oil etc.} &= \frac{10}{100}\times4{,}000 = 400\\
\text{depreciation} &= \frac{75{,}000-15{,}000}{3{,}00{,}000}\times4{,}000 = 0.20\times4{,}000 = 800
\end{align*}
```

$$\text{Total monthly cost} = 1{,}280 + 2{,}800 + 400 + 800 = \mathbf{5{,}280}$$

*Step 3 — cost per EFFECTIVE kilometre* (20% runs empty ⇒ paid km $= 0.8\times4{,}000 = 3{,}200$):

```{=latex}
\begin{align*}
\text{cost/km} &= \frac{5{,}280}{3{,}200} = \mathbf{1.65}\ \text{₹/km}
\end{align*}
```

*Step 4 — profit at hire rate ₹1.80/km:*

```{=latex}
\begin{align*}
\text{margin} &= 1.80 - 1.65 = 0.15/\text{km}\\
\text{per taxi, per month} &= 3{,}200\times0.15 = 480\\
\text{fleet, year 1} &= 480\times10\times12
\end{align*}
```

$$\therefore\ \text{Expected profit} = \text{₹}\,\mathbf{57{,}600}$$

*The one trap: divide by paid kilometres, not total — the 20% empty running is why the answer is 1.65, not 1.32.*


# THE PATTERN MAP (Economics)

| Topic | 22-23 | 23-24 | 24-25 | 2026 verdict |
|---|---|---|---|---|
| Break-even / P-V / contribution | — | — | A×3 + B + C(15) | **Certain** |
| Effective interest / TVM | A×2 + C(15) | — | A×3 | **Certain (Group A)** |
| Inflation types & indices | A×2 + C(7) | A + C(9) | A×4 + B | **Certain** |
| Depreciation theory + T/F | A×3 + B | C(15) | C(15) | **Certain** |
| BCR / NPV / IRR / FW | C×3 (45!) | — | C(15) | **Certain — one big evaluator every year** |
| Cost estimation models | B + C(7) | A | B(5) | Near-certain |
| Accounting statements | A + B | A×4 + B + C(7) | — | Due |
| Uncertainty / EV / distributions | B + C(8) | A×2 | — | Due |
| Replacement analysis | — | — | A | Likely (theory 5-marker) |
| Cost sheet / unit costing | — | — | B + C(15) | Likely repeat |

*— End of the Economics for Engineers Question-Answer Book: 60 questions solved; every real question of three cycles included. —*
