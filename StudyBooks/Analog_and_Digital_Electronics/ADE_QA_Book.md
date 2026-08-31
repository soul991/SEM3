# ANALOG & DIGITAL ELECTRONICS — The Question-Answer Book
### MAKAUT ESC-301 · Every real PYQ from 2022-23, 2023-24, 2024-25, solved in full — arranged to teach the subject from first question to last

> **How this book works.** Questions are grouped by syllabus unit, and inside each unit sequenced Group A (1-mark) → Group B (5-mark) → Group C (15-mark), so working front-to-back *is* a course: definitions first, mechanisms next, design and derivation last. Every answer carries a **Concept bridge** — the two or three sentences of theory the answer rests on — so even if you never open the Concept Book, finishing this one builds the same mastery.
> **Tags:** [2022-23] [2023-24] [2024-25] = the real MAKAUT paper the question appeared in. [TB] = textbook-bank question filling a syllabus topic PYQs haven't touched yet. [P-2026] = high-probability prediction derived from the 3-year pattern. Where an original PYQ referred to a printed figure, the question is restated self-contained with the standard circuit named.

---

# UNIT 1 — ANALOG ELECTRONICS: THE QUESTIONS

## A. One-markers (Group A level)

**Q1. [2024-25] What is the maximum efficiency of a Class B power amplifier?**
**Answer: 78.5%** (= π/4).
*Concept bridge:* Class B conducts 180° per device; averaging its half-sine supply current gives $P_{dc}$ = $2V_{CC}$ $I_{m}$/π, and the ratio $P_{ac}$/$P_{dc}$ peaks at π/4 when the swing $V_{m}$ reaches $V_{CC}$.

**Q2. [2024-25] Where does the Q-point lie for a Class B amplifier?**
**Answer: at cut-off.**
*Concept bridge:* Zero quiescent current is precisely what kills idle dissipation and buys the high efficiency; the price is that each transistor reproduces only half the wave — hence push-pull pairs.

**Q3. [2023-24] Arrange the power-amplifier classes by efficiency, low to high.**
**Answer: A < AB < B < C.**
*Concept bridge:* Efficiency rises as conduction angle falls (360° → >180° → 180° → <180°); fidelity falls in the same order.

**Q4. [2024-25] A Class B amplifier has load power 300 W and DC input power 500 W. Efficiency?**
**Answer: η = 300/500 = 60%.**
*Concept bridge:* η is always $P_{ac}$(load)/$P_{dc}$(supply) — no formula gymnastics needed when both powers are given.

**Q5. [2023-24] The AC output power of a Class B push-pull amplifier is 10 W. What DC input power is drawn at maximum efficiency?**
**Answer: $P_{dc}$ = 10/0.785 ≈ 12.74 W.**
*Concept bridge:* At maximum swing the conversion runs at 78.5%; dividing output by efficiency recovers the supply draw.

**Q6. [2022-23] In the astable multivibrator (555), up to what voltage does the capacitor charge?**
**Answer: (2/3)$V_{CC}$** (it shuttles between $V_{CC}$/3 and $2V_{CC}$/3).
*Concept bridge:* The two internal comparators referenced at ⅓ and ⅔ $V_{CC}$ define the entire timing geometry of every 555 circuit.

**Q7. [2023-24] Statement 1: an astable multivibrator can generate a square wave. Statement 2: a bistable multivibrator can store binary information. True or false?**
**Answer: both true.**
*Concept bridge:* No stable state → free-running rectangular output; two stable states → holds one bit until triggered — the bistable *is* the flip-flop.

**Q8. [2022-23] A sawtooth wave is fed to a Schmitt trigger. Output shape?**
**Answer: a rectangular (pulse) wave.**
*Concept bridge:* The Schmitt trigger snaps HIGH when the input crosses UTP and LOW at LTP — any slow waveform becomes clean fast edges; unequal rise/fall of the sawtooth just makes an asymmetric pulse train.

**Q9. [2024-25] The 555's pin 2 is designated for which function? [P-2026 recurring]**
**Answer: Trigger input** (starts the timing cycle when pulled below $V_{CC}$/3).

**Q10. [P-2026] State the Barkhausen criterion.**
**Answer: loop gain |Aβ| = 1 and total loop phase shift 0°/360°.**
*Concept bridge:* Satisfied at exactly one frequency in RC oscillators — that's what selects f₀.

## B. Five-markers (Group B level)

**Q11. [2023-24 Group A(VI) — a 5-mark design compressed into 1 mark; do it in full] An astable 555 has C = 10 nF. Find $R_{A}$ and $R_{B}$ for f = 10 kHz, duty cycle 0.75.**
**Solution.**

*Step 1 — split the period between HIGH and LOW:*

```{=latex}
\begin{align*}
T &= \frac1f = 100\ \mu\text{s}, & T_H &= 0.75\times100 = 75\ \mu\text{s}, & T_L &= 25\ \mu\text{s}
\end{align*}
```

*Step 2 — $R_B$ from the discharge equation $T_L = 0.693\,R_B C$:*

```{=latex}
\begin{align*}
R_B &= \frac{25\times10^{-6}}{0.693\times10\times10^{-9}} = \mathbf{3.61}\ \text{kΩ}
\end{align*}
```

*Step 3 — $R_A$ from the charge equation $T_H = 0.693(R_A+R_B)C$:*

```{=latex}
\begin{align*}
R_A + R_B &= \frac{75\times10^{-6}}{0.693\times10\times10^{-9}} = 10.82\ \text{kΩ}\\[2pt]
\therefore\ R_A &= 10.82 - 3.61 = \mathbf{7.21}\ \text{kΩ}
\end{align*}
```

*Check:* $D = 10.82/(10.82+3.61) = 0.75$ ✓ · $f = 1.44/[(R_A+2R_B)C] \approx 10$ kHz ✓.

*Concept bridge:* $C$ charges through $R_A+R_B$ but discharges through $R_B$ alone into pin 7 — that asymmetry is why $D > 0.5$ always and why the two equations decouple.
*Marks split:* period split 1 · $R_B$ 2 · $R_A$ 1 · check 1.

**Q12. [2022-23] Find the oscillation frequency of a phase-shift oscillator with R = 10 kΩ, C = 6.5 nF.**
**Solution.** For the three-section RC phase-shift oscillator,

```{=latex}
\begin{align*}
f &= \frac{1}{2\pi RC\sqrt{6}}
   = \frac{1}{2\pi \times (10\times10^{3})\times(6.5\times10^{-9})\times 2.449}
   = \frac{1}{1.0006\times10^{-3}}
\end{align*}
```

$$\therefore\ f \approx \mathbf{1.0\ \text{kHz}}$$

*Concept bridge:* three identical RC sections each contribute $60^{\circ}$ at $f_0$, completing the $360^{\circ}$ loop with the inverting amplifier; the same analysis fixes the $1/\sqrt6$ factor and the gain-29 requirement.
*Marks split:* formula 2 · substitution 2 · value 1.

**Q13. [2023-24] Derive the maximum efficiency of a Class B amplifier.**
**Solution.** (Reproduce these five steps.)

*Step 1 — AC output power* (sine of peak $V_m$ across $R_L$):

```{=latex}
\begin{align*}
P_{ac} &= \frac{V_m^2}{2R_L} \tag{1}
\end{align*}
```

*Step 2 — average supply current.* Each device conducts half-sines of peak $I_m = V_m/R_L$; the average per device is $I_m/\pi$, so for the pair:

```{=latex}
\begin{align*}
I_{dc} &= \frac{2I_m}{\pi}
\end{align*}
```

*Step 3 — DC input power:*

```{=latex}
\begin{align*}
P_{dc} &= V_{CC}\cdot\frac{2I_m}{\pi} = \frac{2V_{CC}V_m}{\pi R_L} \tag{2}
\end{align*}
```

*Step 4 — dividing (1) by (2):*

```{=latex}
\begin{align*}
\eta &= \frac{P_{ac}}{P_{dc}} = \frac{\pi}{4}\cdot\frac{V_m}{V_{CC}}
\end{align*}
```

*Step 5 — maximum at $V_m = V_{CC}$:*

$$\boxed{\eta_{\max} = \frac{\pi}{4} = \mathbf{78.5\%}}$$

*Marks split:* 1 per step. *Concept bridge:* the derivation is "RMS power over average current" — the $\pi$ comes from averaging a half-sine.

**Q14. [2023-24] Explain the operation of a transformer-coupled Class A amplifier.**

**Model answer.** Circuit: CE stage, primary of an output transformer as collector load; secondary drives $R_{L}$; turns ratio n = N₁/N₂ reflects the load as R'_L = n²R_L for optimum matching. DC: the primary's near-zero winding resistance drops almost nothing, so $V_{CEQ}$ ≈ $V_{CC}$; the DC load line is nearly vertical. AC: the reflected R'_L defines the AC load line, letting $v_{CE}$ swing between ~0 and ~2V_CC — twice the series-fed swing. Since the transformer blocks DC from the load and stores/releases energy each half-cycle, no supply power is burnt in a collector resistor. Result: $\eta_{max}$ rises from 25% to **50%**; costs are transformer bulk, cost, and low-frequency/ high-frequency roll-off from winding inductances.
*Concept bridge:* Same Class A transistor operation — the transformer merely doubles usable swing and removes resistor loss; efficiency doubles.
*Marks split:* circuit + DC picture 2 · AC swing argument 2 · η = 50% + trade-offs 1.

**Q15. [TB — completes oscillators] Draw and explain the Wien bridge oscillator; state frequency and gain conditions.**

**Model answer.** Non-inverting amplifier (gain A = 1 + $R_{f}$/R₁); lead-lag network: series R-C from output to + input, parallel R-C from + input to ground. Feedback fraction β = Z₂/(Z₁+Z₂) = 1/[3 + j(ωRC − 1/ωRC)]. Imaginary part vanishes at ω = 1/RC → **f₀ = 1/2πRC**, where β = 1/3 ⟹ A ≥ 3 ($R_{f}$ = 2R₁). Amplitude stabilization: thermistor or lamp in the gain divider. Used in variable-frequency audio generators (gang-tuned R or C).
*Concept bridge:* At f₀ the lead-lag network is purely resistive — zero phase — so a non-inverting gain of exactly 3 closes the Barkhausen loop.

## C. Fifteen-markers (Group C level)

**Q16. [2022-23, 15 marks] (a) Define voltage, current and power amplifiers. [3] (b) List the classes of power amplifiers. [3] (c) Draw the Class B push-pull circuit and explain its operation. [5] (d) Derive its maximum efficiency. [4]**

**Model answer.**
(a) Voltage amplifier: maximizes $V_{out}$/$V_{in}$ (small-signal, high $R_{in}$, moderate $R_{out}$). Current amplifier: maximizes $I_{out}$/$I_{in}$ (low $R_{in}$, high $R_{out}$). Power amplifier: maximizes power delivered to a low-impedance load (large-signal operation, efficiency and dissipation are the design axes).
(b) Class A (360° conduction), Class B (180°), Class AB (slightly >180°), Class C (<180°); efficiency ascends A→AB→B→C while fidelity descends.
(c) Circuit: center-tapped input (or complementary-symmetry) driving Q₁ (npn) for positive half-cycles and Q₂ for negative; both biased at cut-off; outputs recombine in the load (via output transformer or direct in complementary form). Operation: each device idles at zero current, conducts alternately; the load sees the stitched full sine. Mention crossover distortion near zero volts ($V_{BE}$ dead-band) and its Class AB cure.
(d) The five-step derivation of Q13 → $\eta_{max}$ = π/4 = 78.5%.

**Q17. [2022-23, 15 marks] (a) Draw the astable multivibrator using IC 555. [6] (b) Derive duty cycle and frequency. [6] (c) Why is it called a free-running oscillator? [3]**

**Model answer.**
(a) Draw: 555 with $R_{A}$ ($V_{CC}$→pin 7), $R_{B}$ (pin 7→pins 6,2 tied), C (pins 6,2→GND), pin 4→$V_{CC}$, pin 5→0.01 µF to GND, output pin 3. Show internal blocks if time allows: two comparators (⅔, ⅓ references from the 3×5 kΩ divider), SR flip-flop, discharge transistor.
(b) Charging (output HIGH): C rises from $V_{CC}$/3 toward $V_{CC}$ through $R_{A}$+$R_{B}$; time to reach 2V_CC/3: **$T_{H}$ = 0.693($R_{A}$+$R_{B}$)C**. Discharging (output LOW): C falls from 2V_CC/3 toward 0 through $R_{B}$ into pin 7: **$T_{L}$ = 0.693 $R_{B}$ C**. Hence **f = 1/($T_{H}$+$T_{L}$) = 1.44/(($R_{A}$+2R_B)C)**, **D = $T_{H}$/T = ($R_{A}$+$R_{B}$)/($R_{A}$+2R_B)**. (Full marks need the exponential-charging setup: $v_C(t) = V_{\mathrm{final}} + (V_{\mathrm{init}} - V_{\mathrm{final}})e^{-t/\tau}$ applied to both intervals — show one solved instance.)
(c) Free-running because it has **no stable state and needs no external trigger**: the capacitor's own excursion between the two comparator thresholds retriggers the internal flip-flop indefinitely — oscillation is self-sustaining from power-up.

**Q18. [P-2026 — assembled from the 3-year pattern] (a) Explain crossover distortion and how Class AB removes it. [7] (b) A Class B push-pull stage runs from $V_{CC}$ = 20 V into $R_{L}$ = 8 Ω. Find maximum $P_{ac}$, the $P_{dc}$ at that drive, and each transistor's worst-case dissipation. [8]**

**Model answer.**
(a) Near the zero crossing neither base-emitter junction of the push-pull pair exceeds ~0.7 V, so for a band of input around zero *neither* device conducts — the output holds a flat dead-zone each crossing (sketch). The distortion is worst at low signal levels. Class AB pre-biases both bases (diode pair or $V_{BE}$ multiplier tracking temperature) so a small quiescent current flows; the devices hand over smoothly and the dead-band vanishes, at slight cost in idle power.
(b) Max swing $V_{m}$ = $V_{CC}$ = 20 V: $P_{ac}$ = V_m²/$2R_{L}$ = 400/16 = **25 W**. $I_{m}$ = 20/8 = 2.5 A → $P_{dc}$ = $2V_{CC}$ $I_{m}$/π = 2×20×2.5/π = **31.8 W** (η = 25/31.8 = 78.5% ✓). Worst-case *total* device dissipation occurs at $V_{m}$ = $2V_{CC}$/π = 12.73 V: $P_{diss}$(total) = 2V_CC²/(π²R_L) = 800/78.96 = **10.13 W → 5.07 W per transistor** (≈ $P_{ac}$,max/5 each — quote this rule).

*(Unit 1 questions complete: 18 solved, covering every analog question MAKAUT has asked in three years plus the two textbook/predicted fills.)*


---

# UNIT 2 — NUMBER SYSTEMS, BOOLEAN ALGEBRA & COMBINATIONAL LOGIC: THE QUESTIONS

## A. One-markers

**Q19. [2022-23] The state 1110 is a valid state in an 8-4-2-1 BCD counter. True/False?**
**Answer: False.** BCD uses only 0000–1001; 1010–1111 are invalid.
*Concept bridge:* BCD encodes each decimal digit separately in 4 bits, so six of the sixteen patterns can never occur — those six become don't-cares in BCD circuit design.

**Q20. [2022-23] If (212)ₓ = (23)₁₀, find the base X.**
**Answer:** 2X² + X + 2 = 23 ⟹ 2X² + X − 21 = 0 ⟹ (2X + 7)(X − 3) = 0 ⟹ **X = 3**.
*Concept bridge:* Positional value Σdᵢrⁱ turns every unknown-base puzzle into a small polynomial equation; discard the negative root.

**Q21. [2023-24] What is the octal value of (26)₁₀?**
**Answer: 32₈** (26 = 3×8 + 2).
*Concept bridge:* Repeated division by 8 — or go through binary (11010 → group in 3s: 011 010).

**Q22. [2024-25] An example of a weighted code is: (2421 / Gray / XS-3 / all)?**
**Answer: 2421.** Gray and Excess-3 are non-weighted.
*Concept bridge:* Weighted = each bit position carries a fixed decimal weight; Gray's defining property is unit-distance, XS-3's is self-complementing — neither has positional weights.

**Q23. [2023-24] A cascade of 20 XOR gates has input X (each gate's other input as in the standard chain where successive gates take the previous output and X... the classic version: each stage XORs with X). What is Y?**
**Answer:** Twenty XORs with the same X: pairs of XOR-with-X cancel (X⊕X = 0 acts as identity chaining), so an even count returns the **input X unchanged (Y = X)** — with the common alternate wiring (first gate's inputs tied to X and logic-1 etc.) state the parity argument: **an even number of identical XOR stages cancels; an odd number inverts.** Write the parity rule and apply it to the figure's wiring.
*Concept bridge:* XOR is associative and X⊕X=0, X⊕0=X — every XOR-chain question is a parity count, never a gate-by-gate trace.

**Q24. [2022-23] Minimum number of NAND gates to build a full adder?**
**Answer: 9.**
*Concept bridge:* NAND is universal; the known minimal full-adder realization uses nine 2-input NANDs (two XOR pairs cost 4 each sharing structure, plus carry logic).

**Q25. [2024-25] How many half adders are needed to add two 8-bit numbers?**
**Answer: 15** (8 full adders = 16 HAs, but the LSB stage needs no carry-in → 1 HA + 7 FA = 1 + 14 = 15).
*Concept bridge:* FA = 2 HA + 1 OR; the LSB position never receives a carry, so it downgrades to a single HA.

**Q26. [2024-25] Which combinations cannot be grouped in a K-map?**
**Answer: diagonal cells.**
*Concept bridge:* Grouping requires single-variable adjacency (Gray-coded neighbours, including wrap-around edges/corners); diagonal moves change two variables at once.

**Q27. [2023-24] Minimum number of 2:1 MUXes to build a 4:1 MUX?**
**Answer: 3** (two select among pairs, one selects between them — a MUX tree).
*Concept bridge:* Generally a 2ⁿ:1 MUX needs 2ⁿ−1 two-input MUXes, the nodes of a binary tree.

**Q28. [P-2026] How many select lines does a 16:1 MUX need? — **4** (2⁴ = 16).

**Q29. [2024-25] The output of an even-parity generator (XOR tree) is HIGH when the number of 1s in the data is:**
**Answer: odd** (it must add a 1 to make the total even).
*Concept bridge:* Generator output = XOR of the data bits = 1 iff odd count; the *checker* over data+parity outputs 0 when parity is intact.

## B. Five-markers

**Q30. [2022-23] Design a 5:32 decoder using 3:8 and 2:4 decoders.**

**Model answer.** Split the 5 address bits: A₄A₃ (MSBs) → the 2:4 decoder; A₂A₁A₀ → four 3:8 decoders. Each 2:4 output drives the **enable** pin of one 3:8; all 32 outputs = 4 × 8. Sketch: 2:4 on the left, four 3:8 stacked on the right, enables wired from the 2:4's Y₀..Y₃. Only the enabled 3:8 fires, so exactly one of 32 lines goes active — the decoder-tree principle: an $(m{+}n){\to}2^{m+n}$ decoder $= 2^m$ enables $\times$ $n$-bit decoders.
*Marks:* split idea 2 · enable wiring 2 · diagram 1.

**Q31. [2022-23] A 4:1 MUX must realize the sum S of a full adder, inputs P, Q on the selects, $C_{in}$ available. Find I₀…I₃.**

**Model answer.** S = P⊕Q⊕$C_{in}$. Enumerate selects: PQ=00: S = $C_{in}$ → I₀ = **$C_{in}$**. PQ=01: S = $C_{in}$' → I₁ = **$C_{in}$'**. PQ=10: S = $C_{in}$' → I₂ = **$C_{in}$'**. PQ=11: S = $C_{in}$ → I₃ = **$C_{in}$**.
*Concept bridge:* Function-on-a-MUX = partial evaluation: fix the select variables, what's left (a residue in $C_{in}$) is the data input. This is the single most reusable technique in the whole unit.

**Q32. [2023-24] Design a full subtractor (D and Borrow) with a 4:1 MUX (X,Y on selects, $B_{in}$ as residue).**

**Model answer.** D = X⊕Y⊕$B_{in}$; $B_{out}$ = X'Y + X'$B_{in}$ + Y·$B_{in}$.
XY=00: D = $B_{in}$, $B_{out}$ = $B_{in}$ → I₀(D)=$B_{in}$, I₀(B)=$B_{in}$.
XY=01: D = $B_{in}$'; $B_{out}$(0,1,$B_{in}$) = X'Y + X'$B_{in}$ + $YB_{in}$ = 1 + $B_{in}$ + $B_{in}$ = **1** (the X'Y term alone forces it) → I₁(B) = 1, I₁(D) = $B_{in}$'.
XY=10: D = $B_{in}$'; $B_{out}$(1,0,$B_{in}$) = 0 + 0 + 0 = **0** → I₂(B) = 0, I₂(D) = $B_{in}$'.
XY=11: D = $B_{in}$, $B_{out}$ = $YB_{in}$ = $B_{in}$ → I₃(B) = $B_{in}$, I₃(D) = $B_{in}$.
Two 4:1 MUXes (one per output) with data inputs ($B_{in}$, $B_{in}$', $B_{in}$', $B_{in}$) and ($B_{in}$, 1, 0, $B_{in}$).
*Marks:* expressions 2 · residue table 2 · wiring 1.

**Q33. [TB] Convert (45.6875)₁₀ to binary, and (10111011)₂ to octal and hexadecimal.**
**Model answer.** 45.6875₁₀ = 101101.1011₂ (divisions & multiplications shown in Concept Ch. 6). 10111011₂ = 273₈ = BB₁₆.

**Q34. [TB] Perform 23 − 48 using 8-bit 2's complement; state how the sign is read.**
**Model answer.** −48 = 11010000; 00010111 + 11010000 = 11100111; MSB 1 → negative; re-complement → 25; answer **−25**. No end carry → result negative and in complement form (contrast 1's complement's end-around carry).

## C. Fifteen-markers

**Q35. [2023-24, 15 marks] (a) A 4-bit comparator circuit compares A₃A₂A₁A₀ with B₃B₂B₁B₀; find a pair (A,B) giving Y = 0. [5] (b) A MUX-based logic circuit — find the Boolean function realized. [5] (c) Ripple counter numerical (solved as Q47 below). [5]**

**Model answer (a).** The standard XNOR-tree equality comparator outputs Y = Π(Aᵢ ⊙ Bᵢ) = 1 iff A = B; therefore **any A ≠ B gives Y = 0** — e.g. A = 0000, B = 0001. Justify: one differing bit makes its XNOR = 0, zeroing the AND.
**(b) method:** for each select code of the MUX, write the residue connected at that data pin; OR the (minterm-of-selects · residue) products; simplify. Practice instance: 4:1 MUX, selects A,B, data I₀=C, I₁=C', I₂=0, I₃=1 → F = A'B'C + A'BC' + AB = A'(B⊕C) + AB.

**Q36. [2023-24, 15 marks] (a) Z in terms of X and Y from a two-MUX cascade. [8] (b) F(A,B,C,D) = ΠM(1,5,12,15) on an 8×1 MUX, A MSB, selects S₂S₁S₀ = A,B,C. Find pins 0–7. [7]**

**Model answer (b) — do this one cold.** ΠM(1,5,12,15) means F = 0 at minterms {1,5,12,15}, F = 1 elsewhere. Pair rows by (ABC, D):
ABC=000 → (m0,m1) = (1,0) → pin0 = **D'** · 001 → (m2,m3)=(1,1) → **1** · 010 → (m4,m5)=(1,0) → **D'** · 011 → (m6,m7)=(1,1) → **1** · 100 → (m8,m9)=(1,1) → **1** · 101 → (m10,m11)=(1,1) → **1** · 110 → (m12,m13)=(0,1) → **D** · 111 → (m14,m15)=(1,0) → **D'**.
Pins in order: **D', 1, D', 1, 1, 1, D, D'**.
*(a) method:* label the first MUX's output as an intermediate W(X,Y…), substitute into the second MUX's residue table — cascaded MUXes compose functions; expect an XOR/XNOR to emerge.

**Q37. [2023-24, 15 marks] (a) F = Σm(0,2,3,5,7) with don't-care m1, inputs A(MSB),B,C — simplify. [10] (b) Prime implicants of F(X,Y,Z) = Σ(2,3,4,5). [5]**

**Model answer.**
(a) 3-variable K-map, minterms {0,2,3,5,7}, d{1}: cells — m0=1, m1=X, m2=1, m3=1, m5=1, m7=1, m4=0, m6=0. Groups: {m0,m1,m2,m3} (A'=0 row complete with the X) → **A'**; {m1,m3,m5,m7} (C column, using X) → **C**. Cover check: m0,m2 ∈ A'; m5,m7 ∈ C ✓. **F = A' + C**.
(b) Map {2,3,4,5}: pairs {2,3} = X'Y, {4,5} = XY'. No larger groups; both are prime and essential. **PIs: X'Y and XY'** (F = X'Y + XY').

**Q38. [2022-23, 15 marks] (a) Simplify Y = (A'BC + D)(A'D + B'C'). [8] (b) Decoder-with-OR realization → Boolean expression. [7]**

**Model answer (a).** Expand: A'BC·A'D + A'BC·B'C' + D·A'D + D·B'C' = A'BCD + 0 + A'D + B'C'D. A'BCD absorbs into A'D. **Y = A'D + B'C'D = D(A' + B'C')**.
*(b) principle:* active-high decoder outputs are minterms; the OR of connected outputs is F = Σm(those lines). For active-LOW decoders (2023-24 10(b) variant): each output is (mᵢ)'; feeding a NAND of the *unconnected* terms yields the POS form — state F as ΠM of the low-active lines and simplify.

**Q39. [2023-24, 8 marks] A 3-bit Gray counter (A₂ MSB) controls an 8:1 MUX whose data pins are wired: the output pulled high through the sequence — find the MUX output sequence from state 000.**

**Model answer (method, since the wiring is figure-specific).** Write the Gray sequence 000→001→011→010→110→111→101→100→000; at each state the MUX passes the data pin with that index; list the pin values in Gray order — the output is that 8-step periodic bit stream. The examiner's point: **the select sequence is Gray, not binary** — enumerate in Gray order or every subsequent value is wrong.

*(Unit 2 questions complete: 21 solved.)*


---

# UNIT 3 — SEQUENTIAL CIRCUITS: THE QUESTIONS

## A. One-markers

**Q40. [2024-25] The functional difference between an SR and a JK flip-flop is:**
**Answer: the JK accepts J = K = 1** (toggles instead of entering an invalid state).
*Concept bridge:* JK = SR with the forbidden input legalized by feeding Q, Q' back into the input gating — the toggle is the bonus.

**Q41. [2024-25] The invalid state of an SR latch (NOR type) occurs when:**
**Answer: S = R = 1 (both high).** For the NAND latch it is both low.
*Concept bridge:* Both outputs are forced to the same level, violating Q/Q' complementarity; releasing both inputs at once races unpredictably.

**Q42. [2024-25] A D flip-flop can be used as a: (divider / differentiator / delay switch / toggle)?**
**Answer: delay switch** — Q⁺ = D means the input reappears one clock later.
*(To make a D-FF divide by two, you must wire Q'→D — then it toggles. As given, delay.)*

**Q43. [2022-23] In asynchronous circuits, race conditions always arise. True/False?**
**Answer: False.** Races *can* arise (when multiple state variables change together); careful design (race-free assignments, one-variable-at-a-time coding) avoids them.

**Q44. [2023-24] NAND latch with unequal gate delays, P = Q = 0 (both outputs forced 1), inputs change simultaneously to P = Q = 1. Outputs?**
**Answer: indeterminate / race** — the faster gate wins and the latch settles in an unpredictable one of its two states. This is precisely why simultaneous release of the forbidden input is banned.

**Q45. [2022-23] Five JK FFs cascade as a ripple chain, 1 MHz clock. Frequency at Q₃ (the 4th output)?**
**Answer:** each stage divides by 2; Q₃ is after 4 divisions: 1 MHz/2⁴ = **62.5 kHz**.
*Concept bridge:* A toggling FF is a ÷2 — a ripple chain is a binary frequency divider; count stages from the clock.

**Q46. [2022-23] A synchronous binary up-counter with synchronous CLEAR decodes state N through an AND into CLEAR (figure gave the decoded state). Mod value?**
**Answer (method):** with *synchronous* clear, the counter shows states 0…N and clears on the next clock ⟹ **mod = N + 1**; with asynchronous clear the state N is transient ⟹ mod = N. Identify which pin the figure uses, then count. (The examiners are testing exactly this sync/async fencepost.)

## B. Five-markers

**Q47. [2023-24 — and 2022-23 Group A with 100 ns] A 4-bit mod-16 ripple counter uses JK FFs with $t_{pd}$ = 50 ns per FF. Find the maximum clock frequency.**

**Model answer.** Worst case: a clock edge must ripple through all 4 FFs before the next edge: $T_{min}$ = 4 × 50 ns = 200 ns ⟹ **$f_{max}$ = 5 MHz**. (2022-23 variant, 100 ns: $f_{max}$ = 2.5 MHz.)
*Concept bridge:* Ripple counters trade hardware simplicity for cumulative delay: $f_{max}$ = 1/(n·$t_{pd}$). A synchronous counter's $f_{max}$ is 1/($t_{pd}$ + t_logic), independent of length — quote this comparison for the fifth mark.

**Q48. [2022-23] Convert a D flip-flop to a JK flip-flop.**

**Model answer.** Target behaviour Q⁺ = JQ' + K'Q. Since the D-FF obeys Q⁺ = D, feed **D = JQ' + K'Q** (two ANDs + OR, with Q, Q' from the FF). Verify all four (J,K) rows against the JK truth table. Diagram: combinational block ahead of D, feedback from Q/Q'.
*Concept bridge:* Every FF conversion is the same recipe — equate the target's characteristic equation to the host's input.

**Q49. [2022-23] Convert an SR flip-flop to a JK flip-flop.**

**Model answer.** Choose **S = JQ', R = KQ**. Check: J=K=1 → S=Q', R=Q — only one asserts at a time, so SR=11 can never occur ✓, and the state toggles ✓. Other rows reduce to set/reset/hold correctly (show the 4-row verification table).
*Concept bridge:* The Q/Q' gating simultaneously legalizes the toggle *and* guarantees the SR safety constraint — one stone, two birds.

**Q50. [2023-24] A JK FF has J = Q', K = 1, initially cleared, clocked 6 times. Give the Q sequence.**

**Model answer.** Q=0: J=1,K=1 → toggle → 1. Q=1: J=0,K=1 → reset → 0. Then repeat. Sequence after each pulse: **1, 0, 1, 0, 1, 0** — a divide-by-2 square wave.
*Concept bridge:* Feeding state back into the inputs turns a truth-table question into a short simulation — tabulate (Q, J, K, Q⁺) per pulse and march.

**Q51. [2023-24] Find the modulus of the counter in the figure (decode-and-clear ripple counter).**

**Model answer (method).** Read which Qs enter the clearing NAND: the counter resets when that state N first appears. Asynchronous (ripple) clear → state N is transient → **mod = N**. E.g. NAND of Q₃,Q₁ → clears at 1010 = 10 → MOD-10 decade counter. State the sync-clear contrast (mod = N+1) for full marks.

**Q52. [TB] Compare ring and Johnson counters; design a 4-bit Johnson counter with D FFs and list its state sequence.**

**Model answer.** Wiring: shift register Q₀→D₁, Q₁→D₂, Q₂→D₃, feedback **Q₃' → D₀**. From 0000: 1000, 1100, 1110, 1111, 0111, 0011, 0001, 0000 — **8 states (2n)** vs the ring's n; decoding needs 2-input ANDs vs the ring's none; both must be checked for lockout of unused states (add self-correcting logic or preset).

## C. Fifteen-markers

**Q53. [2022-23, 15 marks] (a) To realize a given truth table with a JK FF, find J in terms of A,B. [7] (b) Identify the equivalent flip-flop of the circuit (JK with tied inputs). [4] (c) 1 kHz clock, T-FF initially 0 — output frequency? [4]**

**Model answer.**
(a) Method: treat J as an unknown output; for each (A,B,Q) row of the required table use the JK excitation rules (0→1 needs J=1; 0→0 needs J=0; 1→x rows leave J = don't-care) → K-map J over A,B,Q → minimal J(A,B). The symmetric procedure gives K.
(b) A JK with **J = K tied = T input** is a **T flip-flop**; with **K = J' through an inverter** it is a **D flip-flop** — name whichever the figure shows and prove via the characteristic equation (substitute into Q⁺ = JQ' + K'Q).
(c) A T-FF with T=1 toggles every clock: output = clock/2 = **0.5 kHz** square wave.

**Q54. [P-2026 — the unit's banker Group C] (a) Explain the race-around condition of the JK flip-flop and its elimination by the master-slave configuration, with timing diagrams. [8] (b) Design a MOD-6 synchronous counter using T flip-flops. [7]**

**Model answer.**
(a) With J=K=1 and a level clock of width $t_{p}$ > $t_{pd}$, the output toggles repeatedly within one pulse (draw: clock high interval with Q flipping every $t_{pd}$) — final state depends on $t_{p}$/$t_{pd}$, i.e. indeterminate. Master-slave: master latch admits inputs while CLK is high; slave copies the master only when CLK falls. One toggle per pulse, at the falling edge (draw the three-trace timing: CLK, Q_master, Q_slave). Also mention: edge-triggered FFs solve it in modern practice.
(b) Full 5-step design as in the Concept Book Ch. 11: state table 000→…→101→000, T-excitations, K-maps with d{6,7} → **T₀ = 1, T₁ = Q₂'Q₀, T₂ = Q₀(Q₁+Q₂)**; circuit sketch; note unused-state recovery (check 110→? apply T's → returns into the cycle; if not, add clearing logic).

---

# UNIT 4 — CONVERTERS & LOGIC FAMILIES: THE QUESTIONS

## A. One-markers

**Q55. [2022-23] Which ADC is the slowest of all? — Dual-slope (integrating)** (milliseconds per conversion).

**Q56. [2022-23] Which ADCs are used for high-speed operation? — Flash (parallel-comparator)**, then pipelined/SAR.

**Q57. [2024-25] Which ADC is simplest, fastest and most expensive? — Flash** (2ⁿ−1 comparators buy 1-clock conversion).

**Q58. [2023-24] Which ADC is used for hum rejection? — Dual-slope**, because integrating the input over a mains period (20 ms for 50 Hz) averages the hum to zero — the reason every digital multimeter uses it.

**Q59. [2024-25] Which parameter describes the range of frequency measured by an ADC? — Bandwidth.**

**Q60. [2024-25] The fastest logic family is: — ECL** (non-saturating differential switching, $t_{pd}$ ~1-2 ns).

**Q61. [P-2026] Which family has the lowest static power? — CMOS** (only leakage flows at rest; dynamic power CV²f dominates instead).

**Q62. [P-2026] Number of comparators in an n-bit flash ADC? — 2ⁿ − 1** (255 for 8 bits — hence "most expensive").

## B. Five-markers

**Q63. [TB → Group B regular] Explain the R-2R ladder DAC; why is it preferred over the weighted-resistor DAC?**
**Model answer.** Ladder of only R and 2R; every node looking toward the terminated end presents 2R (prove by collapsing 2R∥2R = R, + series R = 2R, telescoping). Each bit's switch injects $V_{ref}$ into its 2R leg; successive nodes halve each contribution → binary weights 1/2, 1/4, … With the op-amp: **$V_{out}$ = −$V_{ref}$·D/2ⁿ**. Preferred because: two resistor values only (IC-matchable), constant switch impedance, arbitrary n, easy trimming — versus the weighted design's R…R/2ⁿ⁻¹ spread which is unmanufacturable beyond ~6 bits. Numerical close: 4-bit, $V_{ref}$ = 16 V, D = 1010 → 10 V.

**Q64. [TB] Explain the successive-approximation ADC with a worked 4-bit conversion.**
**Model answer.** SAR + DAC + one comparator; binary search MSB-first; n clocks fixed. Work $V_{in}$ = 10.4 V, $V_{FS}$ = 16 V: try 8 (keep) → 12 (clear) → 10 (keep) → 11 (clear) ⟹ **1010**. Advantages: fixed n·$T_{clk}$ time, one comparator; needs S/H. Compare one line each vs flash (speed) and dual-slope (noise).

**Q65. [TB] Define the figures of merit of a logic family and compare TTL, ECL, CMOS.**
**Model answer.** Define $t_{pd}$, power/gate, speed-power product, fan-out, fan-in, noise margins ($NM_{H}$ = $V_{OH}$−$V_{IH}$, $NM_{L}$ = $V_{IL}$−$V_{OL}$) — then the table: TTL 10 ns/10 mW/fan-out 10; ECL 1-2 ns/25-40 mW/poor NM/−5.2 V; CMOS µW static/best NM (~0.45V_DD)/fan-out >50/P = CV²f. One-line verdicts: speed → ECL, power & density → CMOS, legacy general logic → TTL.

## C. Fifteen-marker

**Q66. [P-2026 — composite of the recurring parts] (a) Draw and explain the internal block diagram of the 555 (both comparator references). [5] (b) Explain the monostable mode and derive T = 1.1RC. [5] (c) A dual-slope ADC integrates the input for exactly one mains cycle — explain why this rejects 50 Hz hum. [5]**

**Model answer.** (a) Voltage divider 3×5 kΩ → references 2V_CC/3 (threshold comparator, pin 6) and $V_{CC}$/3 (trigger comparator, pin 2) → SR FF → output + discharge transistor (pin 7); pins 4 (reset), 5 (control). (b) Trigger < $V_{CC}$/3 sets FF; C charges via R: $V_{CC}(1-e^{-t/RC})$ reaches $\tfrac23 V_{CC} \Rightarrow e^{-T/RC} = \tfrac13 \Rightarrow \mathbf{T = RC\ln 3 = 1.1RC}$; output returns LOW, C discharges. (c) Hum adds a sinusoid of period 20 ms to $V_{in}$; the integral of a full sine period is zero, so integrating for exactly 20 ms (or a multiple) makes the hum's net contribution vanish — rejection is mathematically exact at the mains frequency, which is why integrating ADCs dominate precision metering.

---

# CLOSING: THE 3-YEAR PATTERN MAP (what to bet on)

| Topic | 22-23 | 23-24 | 24-25 | Verdict for 2026 |
|---|---|---|---|---|
| Class B efficiency (MCQ/derivation) | C | A+B | A×3, B, C | **Certain** |
| 555 astable (derivation/design) | C (15) | A (design) | B | **Certain** |
| K-map simplification | C | A + C×2 | A, C | **Certain** |
| MUX function realization | B + C | C×2 | C | **Near-certain** |
| Flip-flop conversion | B×2 | — | A | Likely |
| Race-around / master-slave | A | A (variant) | — | Likely (due) |
| Ripple counter $f_{max}$ | A | C(c) | — | Likely (due) |
| ADC comparisons | A×2 | A | A×2 | **Certain (Group A)** |
| Logic families speed/power | — | — | A×2 | Likely |
| Decoder/adder design | B | B | — | Likely |

*Study order if time is short: rows marked Certain, top to bottom, Group C versions first.*

*— End of the ADE Question-Answer Book: 66 solved questions, every real MAKAUT ADE question of the last three cycles included. —*
