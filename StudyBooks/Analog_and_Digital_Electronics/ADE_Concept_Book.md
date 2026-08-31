# ANALOG & DIGITAL ELECTRONICS — The Complete Concept Book
### MAKAUT ESC-301 · B.Tech Sem-3 (CSE/IT) · Built from Boylestad & Nashelsky + Morris Mano + 3 years of real MAKAUT papers

> **How this book works.** Every chapter follows the same pattern: *why the topic exists → theory from first principles with every derivation shown → worked examples → an Exam Focus box telling you exactly how MAKAUT asked it in 2022-23, 2023-24 and 2024-25 → common traps → a rapid-recall summary.* If you master this book, you do not need any other source for ESC-301.

> **Exam format reminder (all MAKAUT theory papers):** 70 marks, 3 hours. Group A: answer 10 of 12 (1 mark each). Group B: answer 3 of 5 (5 marks each). Group C: answer 3 of 5 (15 marks each).

---

# UNIT 1 — ANALOG ELECTRONICS

## Chapter 1: Amplifier Classes (A, B, AB, C)

### 1.1 Why this topic exists

A transistor amplifier takes a small signal and reproduces it larger. But there is a cost: the transistor draws power from the DC supply *even when amplifying nothing*. The **class** of an amplifier describes *what fraction of the input cycle the transistor conducts*, and this single choice fixes the trade-off between **fidelity** (how faithfully the wave is reproduced) and **efficiency** (how much supply power becomes useful output instead of heat). Every audio system, RF transmitter, and power stage you will ever meet is designed around this trade-off — and MAKAUT asks it *every single year*.

### 1.2 The conduction-angle picture

Define the **conduction angle** θ = the portion of a 360° input cycle during which collector current actually flows.

| Class | Conduction angle | Q-point location | Fidelity | Max theoretical efficiency |
|---|---|---|---|---|
| A | 360° (full cycle) | Centre of active region | Best (no distortion) | 25% (series-fed), 50% (transformer-coupled) |
| B | 180° (half cycle) | At cut-off | Needs push-pull pair; crossover distortion | 78.5% |
| AB | Slightly more than 180° | Just above cut-off | Removes crossover distortion | Between 50% and 78.5% |
| C | Much less than 180° | Below cut-off | Severe distortion — only for tuned RF | Above 78.5% (up to ~90%+) |

**Memory anchor:** as the transistor conducts for *less* of the cycle, it wastes *less* idle power → efficiency rises; but it reproduces *less* of the wave → distortion rises. A→B→C is a slide from fidelity toward efficiency.

### 1.3 Class A — full derivation of efficiency

**Setup (series-fed, resistive load $R_C$).** The Q-point is set mid-way so the output can swing equally both ways:

```{=latex}
\begin{align*}
V_{CEQ} &= \tfrac{1}{2}V_{CC}, \qquad I_C = I_{CQ}\ \text{(constant)} 
\end{align*}
```

**Step 1 — DC input power drawn from the supply** (flows whether or not a signal is present):

```{=latex}
\begin{align*}
P_{dc} &= V_{CC}\, I_{CQ} \tag{1}
\end{align*}
```

**Step 2 — Maximum possible AC output.** The collector voltage can swing at most from $V_{CC}$ down to $0$, i.e. a peak swing $V_{CC}/2$; the current swings a peak of $I_{CQ}$:

```{=latex}
\begin{align*}
P_{ac}(\text{max}) &= V_{rms}\cdot I_{rms}
  = \frac{V_{CC}/2}{\sqrt2}\cdot\frac{I_{CQ}}{\sqrt2} && \text{(RMS of each peak)}\\[2pt]
 &= \frac{(V_{CC}/2)\,I_{CQ}}{2} = \frac{V_{CC}\,I_{CQ}}{4} \tag{2}
\end{align*}
```

**Step 3 — Efficiency.** Dividing (2) by (1):

```{=latex}
\begin{align*}
\eta(\text{max}) &= \frac{P_{ac}(\text{max})}{P_{dc}}
 = \frac{V_{CC}I_{CQ}/4}{V_{CC}I_{CQ}} = \frac14
\end{align*}
```

$$\boxed{\eta_{\max}(\text{series-fed Class A}) = 25\%}$$

**Transformer-coupled Class A.** The transformer primary has almost zero DC resistance, so the *average* collector voltage equals $V_{CC}$ — but the AC swing can now reach $2V_{CC}$ peak-to-peak on the primary. Repeating Steps 2–3 with the doubled swing doubles the output for the same DC draw:

$$\boxed{\eta_{\max}(\text{transformer-coupled}) = 50\%}$$

That factor of two is exactly why the transformer-coupled circuit exists — MAKAUT's 2024-25 Group C asked "explain the operation of a transformer-coupled Class A amplifier" for 5 marks.

### 1.4 Class B push-pull — the star derivation (asked in 2024-25 Group C, and as MCQ every single year)

**Idea.** Bias the transistor exactly at cut-off ($I_{CQ}=0$): it conducts only on half-cycles, so idle power is zero. Use *two* transistors in **push-pull** — one amplifies the positive half, the other the negative half — and the load receives the stitched-together full wave.

**Derivation of maximum efficiency — reproduce these exact lines in the exam.**

Let the output be a sine of peak $V_m$ across load $R_L$, driven from supply $V_{CC}$.

*Step 1 — AC output power:*

```{=latex}
\begin{align*}
P_{ac} &= \frac{V_m^2}{2R_L} \tag{1}
\end{align*}
```

*Step 2 — DC power drawn.* Each transistor conducts half-sine pulses of peak

```{=latex}
\begin{align*}
I_m &= \frac{V_m}{R_L}
\end{align*}
```

The average of a half-sine pulse train over a full cycle is $I_m/\pi$ per transistor, so the pair draws an average supply current $2I_m/\pi$:

```{=latex}
\begin{align*}
P_{dc} &= V_{CC}\cdot\frac{2I_m}{\pi} = \frac{2\,V_{CC}V_m}{\pi R_L} \tag{2}
\end{align*}
```

*Step 3 — Efficiency.* Dividing (1) by (2):

```{=latex}
\begin{align*}
\eta &= \frac{P_{ac}}{P_{dc}}
    = \frac{V_m^2/(2R_L)}{2V_{CC}V_m/(\pi R_L)}
    = \frac{\pi}{4}\cdot\frac{V_m}{V_{CC}} \tag{3}
\end{align*}
```

*Step 4 — Maximum.* $\eta$ grows with the swing; the largest possible swing is $V_m = V_{CC}$. Substituting in (3):

$$\boxed{\eta_{\max} = \frac{\pi}{4} = 0.785 \;\Rightarrow\; \mathbf{78.5\%}}$$

**Companion results you must also know:**

- **Worst-case transistor dissipation is NOT at full swing.** From (1) and (2), $P_{diss} = P_{dc}-P_{ac}$; differentiating w.r.t. $V_m$ and setting to zero gives the worst case at $V_m = 2V_{CC}/\pi$, where

```{=latex}
\begin{align*}
P_{diss}(\text{max, both}) &= \frac{2V_{CC}^2}{\pi^2 R_L} \;\approx\; 0.4\,P_{ac}(\text{max})
\end{align*}
```

  i.e. each transistor must be rated for about one-fifth of the maximum output power.
- **Crossover distortion:** near zero-crossing neither base–emitter junction is forward-biased (each needs $\approx 0.7$ V), so the output has a flat "dead zone." **Class AB fixes it** by pre-biasing both transistors slightly into conduction (diode / $V_{BE}$-multiplier network), trading a little efficiency for a clean crossover. The pairing "derive Class B efficiency (8) + explain crossover distortion and the Class AB cure (7)" is a 15-mark Group C classic.

```{=latex}
\begin{center}\begin{tikzpicture}
\begin{axis}[width=10.5cm,height=4.8cm,axis lines=middle,xlabel={$\omega t$},ylabel={$v_o$},xtick=\empty,ytick=\empty,domain=0:720,samples=300,title={\small Class B output: dead-band at each zero crossing (dashed = ideal sine)}]
\addplot[gray,dashed,thin]{sin(x)};
\addplot[accent,very thick]{(sin(x)>0.18)*(sin(x)-0.18)/0.82 + (sin(x)<-0.18)*(sin(x)+0.18)/0.82};
\end{axis}\end{tikzpicture}\end{center}
```

### 1.5 Class C in two sentences (all MAKAUT ever asks)

Biased well below cut-off; conducts in short pulses (θ ≪ 180°); the massive distortion is repaired by a *tuned LC tank* at the collector that rings at the fundamental — usable only for RF at a single frequency, in exchange for efficiency approaching 90%+. Q-point for Class B sits **at cut-off** (2024-25 Group A MCQ: answer "cut off").

### 1.6 Worked numericals (real exam patterns)

**W1 (2024-25 Group A).** *A Class B amplifier has load (AC output) power 300 W and DC input power 500 W. Find the efficiency.*

**Solution.**

```{=latex}
\begin{align*}
\eta &= \frac{P_{ac}}{P_{dc}} = \frac{300}{500} = 0.60
\end{align*}
```

$$\therefore\ \eta = \mathbf{60\%}$$

**W2 (2024-25 Group B, 5 marks).** *A Class B push-pull amplifier delivers 10 W AC output at maximum efficiency. Find the DC input power drawn from the supply.*

**Solution.** At maximum efficiency, $\eta = \pi/4 = 0.785$. Since $\eta = P_{ac}/P_{dc}$,

```{=latex}
\begin{align*}
P_{dc} &= \frac{P_{ac}}{\eta} = \frac{10}{0.785}
\end{align*}
```

$$\therefore\ P_{dc} = \mathbf{12.74\ \text{W}}$$

**W3.** *Series-fed Class A with $V_{CC} = 20$ V, $I_{CQ} = 500$ mA. Find $P_{dc}$, $P_{ac}(\max)$, $\eta$.*

**Solution.**

```{=latex}
\begin{align*}
P_{dc} &= V_{CC}I_{CQ} = 20 \times 0.5 = 10\ \text{W}\\[2pt]
P_{ac}(\text{max}) &= \frac{P_{dc}}{4} = \frac{10}{4} = 2.5\ \text{W}\\[2pt]
\eta &= \frac{2.5}{10} = \mathbf{25\%}
\end{align*}
```

### 1.7 Exam Focus — how MAKAUT asked this

- **2022-23:** Group A MCQ on conduction angle; Group C: efficiency derivation of Class B.
- **2023-24:** Group A: Q-point of Class B; Group B: push-pull operation sketch.
- **2024-25:** Group A: max η of Class B (78.5%), efficiency numerical, Q-point location; Group B: 10 W / max-η numerical (W2 above); Group C: derive Class B max efficiency (5) + transformer-coupled Class A (5).
- **Verdict: guaranteed marks. Learn the 78.5% derivation cold.**

### 1.8 Traps

- Efficiency formula uses **peak** $V_{m}$ in η = (π/4)($V_{m}$/$V_{CC}$) — students mix RMS and peak and get π/8.
- "Maximum transistor dissipation occurs at maximum output" — **false**; it occurs at $V_{m}$ = $2V_{CC}$/π.
- Transformer-coupled Class A is 50%, series-fed is 25% — the MCQ options always contain both.

### 1.9 Rapid recall

- $\eta_{A}$(series) 25% · $\eta_{A}$(transformer) 50% · $\eta_{B}$ 78.5% = π/4 · Class C ~90% tuned only
- Class B: $P_{dc}$ = $2V_{CC}$ $I_{m}$/π; $P_{ac}$ = $V_{m}$ $I_{m}$/2; crossover distortion → Class AB pre-bias
- Conduction angles: A 360°, B 180°, AB >180°, C <180°

---

## Chapter 2: Feedback and the Barkhausen Criterion

### 2.1 Why feedback

Take a fraction β of an amplifier's output and add it back to the input. If it *opposes* the input (**negative feedback**), gain drops but everything else improves — stability, bandwidth, distortion, noise. If it *reinforces* the input (**positive feedback**), gain grows without bound until the circuit supplies its own input: an **oscillator**.

**Closed-loop gain:** $A_{f}$ = A / (1 + Aβ)  (negative feedback; loop gain Aβ)

For positive feedback the sign flips: $A_{f}$ = A/(1 − Aβ) — and as Aβ → 1, $A_{f}$ → ∞: output with no input.

### 2.2 Effects of negative feedback (5-mark list, asked 2023-24)

With desensitivity factor D = 1 + Aβ:
- Gain: ÷D (reduced, but stabilized: $dA_{f}$/$A_{f}$ = (dA/A)/D)
- Bandwidth: ×D (gain-bandwidth product conserved)
- Distortion & noise: ÷D
- Input impedance: ×D (series mixing) — Output impedance: ÷D (voltage sampling)

### 2.3 Barkhausen criterion (Group A regular)

Sustained oscillations require, around the complete loop:
1. **|Aβ| = 1** (unity loop-gain magnitude), and
2. **Total loop phase shift = 0° or 360°.**

In practice design |Aβ| slightly > 1; amplitude grows until circuit non-linearity trims it back to exactly 1.

---

## Chapter 3: Oscillators — Phase-Shift and Wien Bridge

### 3.1 RC Phase-Shift Oscillator

**Construction:** one inverting amplifier (180° phase shift) + a cascade of three identical RC high-pass sections, each contributing 60° at one particular frequency → extra 180°. Total 360° ✓ Barkhausen satisfied at exactly that frequency.

**Frequency of oscillation:**

f = 1 / (2πRC√6)   (three identical RC sections)

**Gain condition:** the RC ladder attenuates by 1/29 at f, so the amplifier must supply |A| ≥ **29**.

*(With BJT loading corrections f = 1/[2πRC√(6+4K)], K = $R_{C}$/R — state only if asked "with derivation"; the √6 form plus |A|=29 earns full marks at 5-mark level.)*

**Why 29?** At the oscillation frequency the transfer of the 3-section ladder is β = −1/29. For |Aβ|=1 → |A|=29.

### 3.2 Wien Bridge Oscillator (Group B favourite — asked 2023-24 and predicted every cycle)

**Construction:** a *non-inverting* amplifier (0° shift) with a **lead-lag network**: series RC (Z₁ = R + 1/jωC) feeding parallel RC (Z₂ = R/(1+jωRC)) as a voltage divider back to the + input.

**Derivation of frequency.** β = Z₂/(Z₁+Z₂). Substituting and simplifying:

β = 1 / [3 + j(ωRC − 1/ωRC)]

β is real (zero phase) when ωRC = 1/ωRC → ω = 1/RC:

**f = 1/(2πRC)**

At that frequency β = 1/3, so the amplifier needs **A = 3**, i.e. a non-inverting op-amp stage with $R_{f}$/R₁ = 2. Amplitude is stabilized in practice with a thermistor/lamp in the gain leg.

**Exam answer skeleton (5 marks):** circuit sketch (2) + β derivation to f = 1/2πRC (2) + gain ≥ 3 condition (1).

### 3.3 Comparison table (1-mark ammunition)

| | Phase-shift | Wien bridge |
|---|---|---|
| Amplifier type | Inverting (180°) | Non-inverting (0°) |
| Network | 3×RC high-pass, 60° each | Lead-lag bridge |
| f | 1/(2πRC√6) | 1/(2πRC) |
| Min gain | 29 | 3 |
| Use | Fixed audio frequency | Variable-frequency lab oscillators |

---

## Chapter 4: Multivibrators and the Schmitt Trigger

### 4.1 The multivibrator family

Two-state regenerative switching circuits:

- **Astable** — *no* stable state; flips forever between HIGH and LOW → free-running **square-wave generator** (clock source). *"Justify: an astable multivibrator generates a square wave"* was a 5-mark 2024-25 Group B question: because each RC timing branch alternately charges toward a supply and discharges through a threshold, the output spends T₁ HIGH and T₂ LOW indefinitely with no external trigger, producing a rectangular wave; with symmetric timing it is a square wave.
- **Monostable** — one stable state; a trigger flips it for a fixed time T set by RC, then it returns. "One-shot" pulse generator / pulse-width standardizer.
- **Bistable** — two stable states; needs a trigger for every change. This is the flip-flop — the memory element of Unit 3.

### 4.2 Schmitt Trigger

A comparator with **positive feedback**, creating two different switching thresholds: Upper Trip Point (UTP) and Lower Trip Point (LTP). The gap UTP − LTP is the **hysteresis**.

**Why it matters:** a slow or noisy input crossing a single threshold makes a plain comparator chatter (multiple false transitions). With hysteresis, once the output flips at UTP, the effective threshold jumps down to LTP — noise smaller than the hysteresis cannot flip it back. The Schmitt trigger is thus a **squaring circuit / wave-shaper**: any slow waveform in → clean fast-edged rectangular wave out.

For the standard op-amp inverting Schmitt with divider R₁,R₂ from output to + input: UTP/LTP = ±$V_{sat}$·R₂/(R₁+R₂).

---

## Chapter 5: The 555 Timer — guaranteed marks every year

### 5.1 Inside the chip (draw this for any 8+ mark question)

Three internal 5 kΩ resistors (the name "555") divide $V_{CC}$ into two references: (2/3)$V_{CC}$ and (1/3)$V_{CC}$. These feed two comparators:

- **Threshold comparator** (pin 6 vs 2/3 $V_{CC}$) → RESETS an internal SR flip-flop
- **Trigger comparator** (pin 2 vs 1/3 $V_{CC}$) → SETS the flip-flop

The flip-flop drives the output stage (pin 3) and an internal **discharge transistor** (pin 7) that shorts the timing capacitor to ground when the output is LOW. Pin 4 = master reset, pin 5 = control voltage (overrides 2/3 $V_{CC}$ reference), pin 8/1 = $V_{CC}$/GND.

**Pin-2 function (2024-25 Group A MCQ): trigger input.**

### 5.2 Monostable operation + derivation

Stable state: output LOW, discharge transistor ON, capacitor empty. A negative edge on pin 2 ($< \tfrac13 V_{CC}$) sets the flip-flop → output HIGH, transistor off, and $C$ charges through $R$ toward $V_{CC}$:

```{=latex}
\begin{align*}
v_C(t) &= V_{CC}\left(1 - e^{-t/RC}\right) \tag{1}
\end{align*}
```

The HIGH state ends when $v_C$ reaches the threshold $\tfrac23 V_{CC}$. Putting $v_C(T) = \tfrac23 V_{CC}$ in (1):

```{=latex}
\begin{align*}
\tfrac23 V_{CC} &= V_{CC}\left(1 - e^{-T/RC}\right)\\[2pt]
e^{-T/RC} &= \tfrac13\\[2pt]
T &= RC\,\ln 3
\end{align*}
```

$$\boxed{T = 1.1\,RC}$$

### 5.3 Astable operation + derivation (the single most-asked derivation in Unit 1)

Wiring: $R_A$ from $V_{CC}$ to pin 7, $R_B$ from pin 7 to pins 6+2, $C$ from there to ground. $C$ charges through **$R_A + R_B$** and discharges through **$R_B$ alone** (into pin 7), shuttling forever between $\tfrac13 V_{CC}$ and $\tfrac23 V_{CC}$.

*Charging (output HIGH):* from $V_{CC}/3$ toward $V_{CC}$, stopping at $2V_{CC}/3$. Solving the RC exponential between these limits:

```{=latex}
\begin{align*}
T_H &= 0.693\,(R_A + R_B)\,C \tag{1}
\end{align*}
```

*Discharging (output LOW):* from $2V_{CC}/3$ toward $0$, stopping at $V_{CC}/3$:

```{=latex}
\begin{align*}
T_L &= 0.693\,R_B\,C \tag{2}
\end{align*}
```

*Adding (1) and (2):*

```{=latex}
\begin{align*}
T &= T_H + T_L = 0.693\,(R_A + 2R_B)\,C\\[2pt]
f &= \frac{1}{T} = \frac{1.44}{(R_A + 2R_B)\,C} \tag{3}\\[4pt]
D &= \frac{T_H}{T} = \frac{R_A + R_B}{R_A + 2R_B} \tag{4}
\end{align*}
```

From (4), $D > 50\%$ always in this basic circuit — a classic 1-mark trap.

```{=latex}
\begin{center}\begin{tikzpicture}[xscale=1.05]
\draw[gray,dashed] (0,2)node[left,black]{\scriptsize $\tfrac23 V_{CC}$}--(9,2);
\draw[gray,dashed] (0,1)node[left,black]{\scriptsize $\tfrac13 V_{CC}$}--(9,1);
\draw[->] (0,0)--(9.3,0) node[right]{\scriptsize $t$};
\draw[->] (0,0)--(0,3.5);
\draw[very thick,accent] (0,1) to[out=60,in=200] (2.2,2) to[out=-70,in=160] (3.2,1) to[out=60,in=200] (5.4,2) to[out=-70,in=160] (6.4,1) to[out=60,in=200] (8.6,2);
\node[accent] at (4.5,0.5) {\scriptsize $v_C$: charges through $R_A{+}R_B$, discharges through $R_B$};
\draw[very thick,mintedge] (0,3.2)--(2.2,3.2)--(2.2,2.7)--(3.2,2.7)--(3.2,3.2)--(5.4,3.2)--(5.4,2.7)--(6.4,2.7)--(6.4,3.2)--(8.6,3.2);
\node[mintedge] at (9.1,3.2) {\scriptsize OUT};
\node at (1.1,3.36){\scriptsize $T_H$}; \node at (2.7,2.52){\scriptsize $T_L$};
\end{tikzpicture}\end{center}
```

### 5.4 The real 2024-25 Group B numerical, fully worked

*An astable 555 has $C = 10$ nF. Design $R_A$ and $R_B$ for $f = 10$ kHz and duty cycle $0.75$.*

**Solution.**

*Step 1 — split the period.*

```{=latex}
\begin{align*}
T &= \frac1f = \frac{1}{10\,\text{kHz}} = 100\ \mu\text{s}\\[2pt]
T_H &= D\cdot T = 0.75 \times 100 = 75\ \mu\text{s}\\[2pt]
T_L &= T - T_H = 25\ \mu\text{s}
\end{align*}
```

*Step 2 — find $R_B$ from $T_L = 0.693\,R_B C$:*

```{=latex}
\begin{align*}
R_B &= \frac{T_L}{0.693\,C} = \frac{25\times10^{-6}}{0.693 \times 10\times10^{-9}} = \mathbf{3.61}\ \text{kΩ}
\end{align*}
```

*Step 3 — find $R_A$ from $T_H = 0.693\,(R_A+R_B)\,C$:*

```{=latex}
\begin{align*}
R_A + R_B &= \frac{75\times10^{-6}}{0.693\times10\times10^{-9}} = 10.82\ \text{kΩ}\\[2pt]
R_A &= 10.82 - 3.61 = \mathbf{7.21}\ \text{kΩ}
\end{align*}
```

*Step 4 — verify.*

```{=latex}
\begin{align*}
D &= \frac{10.82}{10.82+3.61} = 0.75\ \checkmark &
f &= \frac{1.44}{(7.21+7.22)\,\text{kΩ}\times10\,\text{nF}} \approx 10\ \text{kHz}\ \checkmark
\end{align*}
```

### 5.5 Exam Focus & rapid recall

- Asked in **all three years** of your PYQs (pin functions, T = 1.1RC, astable derivation, the design numerical, Schmitt-from-555).
- **Monostable T = 1.1 RC · Astable f = 1.44/($R_{A}$+$2R_{B}$)C · D = ($R_{A}$+$R_{B}$)/($R_{A}$+$2R_{B}$) · thresholds 1/3 & 2/3 $V_{CC}$.**
- Trap: forgetting C discharges through $R_{B}$ *only* → wrong $T_{L}$.
- A 555 with pins 2 and 6 tied together and two threshold references acts as a **Schmitt trigger** (lab experiment 3 in your syllabus — a Group B "design" favourite).

*(End of Unit 1)*


---

# UNIT 2 — NUMBER SYSTEMS, BOOLEAN ALGEBRA & COMBINATIONAL CIRCUITS

## Chapter 6: Number Systems and Codes

### 6.1 Why this topic exists

Digital circuits know only two voltages, so *everything* — numbers, text, signals — must be encoded in binary. Different jobs need different encodings: arithmetic wants positional binary; displays want BCD; error-prone mechanical encoders want Gray code; text wants ASCII/EBCDIC. Conversions between these are pure Group-A/1-mark territory and appear in **every** MAKAUT paper.

### 6.2 Positional systems and conversions

A number in base r: value = Σ dᵢ·rⁱ. The four bases that matter: binary (2), octal (8), decimal (10), hexadecimal (16).

**Decimal → binary:** repeated division by 2 for the integer part (remainders read bottom-up); repeated multiplication by 2 for the fraction (integer parts read top-down).

**Worked:** 45.6875₁₀ → integer: 45 = 101101₂; fraction: .6875×2=1.375(1), .375×2=0.75(0), .75×2=1.5(1), .5×2=1.0(1) → .1011. So 45.6875₁₀ = **101101.1011₂**.

**Binary ↔ octal:** group bits in 3s from the point. **Binary ↔ hex:** group in 4s.
10111011₂ = 10 111 011 = 273₈ = 1011 1011 = BB₁₆.

**PYQ (2024-25 Group B):** "What is the octal value of the binary…" — this is exactly the group-in-3s mechanic. Hex XOR also appears in CO papers: (4AC0)₁₆ ⊕ (B53F)₁₆ = FFFF₁₆ (they are bitwise complements).

### 6.3 Codes: BCD, Excess-3, Gray, ASCII, EBCDIC

**BCD (8421):** each *decimal digit* separately as 4 bits. 259₁₀ = 0010 0101 1001. Weighted code. Note 1010–1111 are invalid BCD. BCD ≠ binary of the whole number (259₁₀ = 100000011₂ — different!).

**Weighted vs non-weighted (1-marker, 2024-25):** weighted: 8421 BCD, 2421, 5211. Non-weighted: **Excess-3, Gray**. "An example of a weighted code is → 2421" (Gray and XS-3 are the distractors).

**Excess-3:** decimal digit + 3, then binary. Self-complementing: 9's complement = bitwise inversion.

**Gray code:** successive values differ in exactly **one bit** (unit-distance code). Use: shaft encoders, K-map ordering.
- Binary → Gray: g₃ = b₃; gᵢ = bᵢ₊₁ ⊕ bᵢ. Example 1011₂ → g = 1(1⊕0)(0⊕1)(1⊕1) = 1110.
- Gray → binary: b₃ = g₃; bᵢ = bᵢ₊₁ ⊕ gᵢ. Example 1110 → 1011.

**ASCII:** 7-bit alphanumeric code (128 chars) — 'A' = 65 = 1000001. **EBCDIC:** IBM's 8-bit code. Both are *alphanumeric*, not arithmetic, codes.

### 6.4 Signed numbers: sign-magnitude, 1's and 2's complement

For n bits, MSB = sign (0 = +, 1 = −).

| Representation | −N encoding | Range (n bits) | Zeros |
|---|---|---|---|
| Sign-magnitude | sign bit + |N| | −(2ⁿ⁻¹−1) … +(2ⁿ⁻¹−1) | two (+0, −0) |
| 1's complement | invert all bits of +N | −(2ⁿ⁻¹−1) … +(2ⁿ⁻¹−1) | two |
| 2's complement | invert + add 1 | **−2ⁿ⁻¹ … +(2ⁿ⁻¹−1)** | one |

**Why 2's complement wins:** unique zero, and subtraction becomes addition of the complement with the end carry simply *discarded*.

**Worked subtraction (Group B pattern):** 23 − 48 in 8-bit 2's complement.
+23 = 00010111; +48 = 00110000 → −48 = 11010000. Sum: 00010111 + 11010000 = 11100111. MSB=1 → negative; magnitude = 2's comp of 11100111 = 00011001 = 25. Answer **−25** ✓.

**1's complement quirk:** end-around carry (carry out is added back to LSB).

**Overflow rule (feeds into CO too):** adding same-sign numbers and getting the opposite sign = overflow; formally V = $C_{in}$(MSB) ⊕ $C_{out}$(MSB).

### 6.5 Rapid recall

- 2's comp of 15 (8-bit): 11110001 (asked verbatim in CO 2022-23 Group A)
- Gray: XOR neighbours · BCD invalid codes 1010-1111 · XS-3 = BCD+0011 · ASCII 7-bit

---

## Chapter 7: Boolean Algebra and Minimization

### 7.1 The axioms you actually use

Over {0,1} with AND(·), OR(+), NOT('):

- Identity: A+0=A, A·1=A · Null: A+1=1, A·0=0 · Idempotent: A+A=A · Complement: A+A'=1, A·A'=0
- Commutative, Associative, Distributive — **including the dual** A+BC = (A+B)(A+C)
- Absorption: A + AB = A · A + A'B = A + B  ← the two workhorses of algebraic minimization
- **De Morgan:** (A+B)' = A'B' ; (AB)' = A'+B'. Generalizes to any number of variables; "break the bar, change the sign."

**Consensus theorem (silent simplifier):** AB + A'C + BC = AB + A'C (the BC term is redundant).

**Duality:** swap +↔·, 0↔1 → every identity has a valid dual. **Complement of a function:** apply De Morgan recursively, or take the dual and complement each literal.

### 7.2 Canonical forms: SOP, POS, minterms, maxterms

- **Minterm mᵢ:** AND term containing every variable once (true for exactly one input row). **SOP canonical:** F = Σm(...)
- **Maxterm Mᵢ:** OR term, false for exactly one row. **POS canonical:** F = ΠM(...)
- Relation: Mᵢ = mᵢ′, and F = Σm(S) ⇔ F = ΠM(complement set of S).

**Worked:** F(A,B,C) = Σm(1,3,5,7) → F = A'B'C + A'BC + AB'C + ABC = C(A'B'+A'B+AB'+AB) = **C**. The same F as POS: ΠM(0,2,4,6).

### 7.3 Karnaugh maps — the exam's favourite tool

A K-map is a truth table folded so that **adjacent cells differ in one variable** (Gray-code ordering: 00, 01, 11, 10). Groups of 1s that span 2ᵏ adjacent cells eliminate k variables.

**Rules:** groups must be rectangles of size 1,2,4,8,16; the map **wraps** left-right and top-bottom (corners are adjacent!); take groups as large as possible; every 1 must be covered; overlap is allowed; **diagonal cells can never be grouped** (2024-25 Group A MCQ: "diagonal corners cannot be combined").

**Group-size effect (2026-predicted 1-marker):** in a 4-variable map, a group of 8 eliminates 3 variables, leaving a single-literal term.

**Don't-cares (d):** input combinations that can't occur (e.g. BCD 1010–1111). Treat each X as 1 *if it enlarges a group*, else 0.

**Fully worked 4-variable example (Group C pattern):**
F(A,B,C,D) = Σm(0,1,2,4,5,6,8,9,12,13,14) —

Map (rows AB = 00,01,11,10; cols CD = 00,01,11,10):

```
        CD=00  01   11   10
AB=00     1    1    0    1
AB=01     1    1    0    1
AB=11     1    1    0    1
AB=10     1    1    0    0
```

```{=latex}
\begin{center}\small
\begin{tabular}{c|cccc}
 & \textbf{CD=00} & \textbf{01} & \textbf{11} & \textbf{10}\\\hline
\textbf{AB=00} & \cellcolor{accentlight}1 & \cellcolor{accentlight}1 & 0 & \cellcolor{mintbg}1\\
\textbf{AB=01} & \cellcolor{accentlight}1 & \cellcolor{accentlight}1 & 0 & \cellcolor{mintbg}1\\
\textbf{AB=11} & \cellcolor{accentlight}1 & \cellcolor{accentlight}1 & 0 & \cellcolor{boxamber}1\\
\textbf{AB=10} & \cellcolor{accentlight}1 & \cellcolor{accentlight}1 & 0 & 0\\
\end{tabular}\qquad
\begin{tabular}{l}
\scriptsize \colorbox{accentlight}{~~}\; 8-cell group $\to C'$\\[2pt]
\scriptsize \colorbox{mintbg}{~~}\; $\{m_0,m_2,m_4,m_6\}\to A'D'$ (wraps left)\\[2pt]
\scriptsize \colorbox{boxamber}{~~}\; $\{m_4,m_6,m_{12},m_{14}\}\to BD'$\\
\end{tabular}
\end{center}
```

Group systematically:
1. Columns CD=00 and CD=01 are entirely 1s → one **8-cell group** → eliminates A, B, D → term **C'**.
2. The remaining 1s sit in column CD=10 at rows AB=00, 01, 11 (m2, m6, m14). m10 is 0, so no 4-cell group exists *within* that column — instead extend sideways into column CD=00 (adjacent by wrap):
   - {m0, m2, m4, m6} (A=0, D=0 throughout) → **A'D'** — covers m2 and m6.
   - {m4, m6, m12, m14} (B=1, D=0 throughout) → **BD'** — covers m14.

**F = C' + A'D' + BD'**

*Verify cell-by-cell (do this in the exam — it earns method marks and catches slips): C' covers all eight 1s in columns 00/01; A'D' covers m0,m2,m4,m6 ✓; BD' covers m4,m6,m12,m14 ✓. Every listed minterm covered, no 0 included ✓.*

### 7.4 Quine-McCluskey in brief

Tabular, algorithmic version of K-map for >4 variables: group minterms by number of 1s → repeatedly combine pairs differing in one bit (mark with −) → unpaired terms are **prime implicants** → build a PI chart, pick **essential PIs** (sole coverers of some minterm), cover the rest minimally. Know the flow + a 4-variable demo; it appears as an occasional Group C alternative to K-maps.

---

## Chapter 8: Combinational Building Blocks

*Combinational = output depends only on present inputs (no memory). This chapter is the highest-density source of Group B "design" questions.*

### 8.1 Half adder and full adder

**Half adder (2 in, 2 out):** S = A ⊕ B, C = AB. Cannot accept an incoming carry.

**Full adder (3 in: A,B,$C_{in}$):**
S = A ⊕ B ⊕ $C_{in}$
$C_{out}$ = AB + $C_{in}$(A ⊕ B) = AB + $BC_{in}$ + $AC_{in}$ (majority function)

**Full adder from two half adders + one OR gate** (5-mark classic, predicted 2026): HA1 takes A,B → s₁ = A⊕B, c₁ = AB. HA2 takes s₁, $C_{in}$ → S = s₁⊕$C_{in}$, c₂ = s₁C_in. $C_{out}$ = c₁ + c₂.

**PYQ 1-marker (2024-25):** "How many half adders to add two 8-bit numbers?" Ripple structure needs 8 full adders; each FA = 2 HAs, and the LSB stage can be a single HA → the intended answer from the given options is **15**.

### 8.2 Half and full subtractor

Half: D = A ⊕ B, Borrow = A'B. Full: D = A ⊕ B ⊕ $B_{in}$; **$B_{out}$ = A'B + A'$B_{in}$ + B·$B_{in}$** (the "majority function with A complemented" — compare $C_{out}$ of the adder). Equivalent two-half-subtractor form: $B_{out}$ = A'B + (A ⊕ B)'$B_{in}$. Design of full adder *and* full subtractor with basic gates is lab experiment 4 and a recurring Group B pair.

**Adder-subtractor composite:** XOR each B bit with a mode line M (M=0 add, M=1 subtract) feeding a ripple adder with C₀ = M — this implements A + B or A + B'+1 = A − B with one hardware block.

### 8.3 Decoder, Encoder

**Decoder n→2ⁿ:** activates exactly one output line per input code; internally one AND per minterm. **Any Boolean function = OR of the decoder outputs for its minterms** — e.g. *implement a full adder with a 3:8 decoder + two OR gates* (S = Σm(1,2,4,7), C = Σm(3,5,6,7)) — a 2023-24 Group B question.

**Decoder trees (2023-24 Group B):** build 5:32 from 3:8 + 2:4: use the 2:4 on the two MSBs to enable four 3:8 decoders (via their enable pins) handling the 3 LSBs.

**Encoder 2ⁿ→n:** inverse; **priority encoder** adds a validity bit and resolves multiple active inputs by priority.

### 8.4 Multiplexer and Demultiplexer

**MUX 2ⁿ→1:** n select lines choose one data input: Y = Σ (data_i · minterm_i(selects)). **16:1 needs 4 select lines** (2026-predicted 1-marker).

**Function realization with MUX (the most reliable Group C sub-question of this unit — appeared 2024-25):**
Implement F(A,B,C,D) with an 8:1 MUX, A,B,C on selects: for each select combination, F reduces to one of {0, 1, D, D'} — fill that as the data input. Method: write the truth table in pairs of rows sharing A,B,C; compare F across D=0/D=1.

**Worked (2024-25 Group C, 8 marks):** F(A,B,C,D) = Σm(0,2,4,6,9,11,13,15), A MSB, selects A,B,C.
With A,B,C on the selects and D as the leftover variable, each select combination ABC owns the minterm pair (2·ABC, 2·ABC + 1), i.e. (D=0, D=1). Read F off each pair:
ABC=000 → (m0,m1) = (1,0) → **D'** · 001 → (m2,m3) = (1,0) → **D'** · 010 → (m4,m5) = (1,0) → **D'** · 011 → (m6,m7) = (1,0) → **D'** · 100 → (m8,m9) = (0,1) → **D** · 101 → (m10,m11) = (0,1) → **D** · 110 → (m12,m13) = (0,1) → **D** · 111 → (m14,m15) = (0,1) → **D**.
Data inputs: I₀..I₃ = D', I₄..I₇ = D. (Elegant check: F = A ⊕ D' ... indeed F = A'D' + AD = (A⊕D)'.)

**DEMUX 1→2ⁿ:** routes one input to a selected output; hardware-identical to a decoder with enable used as data.

### 8.5 Comparator

1-bit: (A>B) = AB', (A<B) = A'B, (A=B) = (A ⊕ B)' = XNOR. n-bit magnitude comparators cascade from MSB; equality = AND of all bitwise XNORs. IC 7485 = 4-bit comparator (lab experiment 1).

### 8.6 Parity generator / checker

Even-parity bit over n data bits = XOR of them all (makes total count of 1s even). Checker: XOR of data+parity → 0 if OK (even parity). **Trap-turned-MCQ (2024-25):** "output of an even parity *generator* is 1 when the number of data 1s is **odd**" (it must add a 1 to even things out).

### 8.7 Exam Focus + rapid recall (Unit 2)

- Every year, Group A: K-map grouping rules, weighted codes, half-adder counts, MUX select-line counts, parity logic.
- Group B rotation: full adder from decoder / from half adders; subtractor design; decoder trees; K-map with don't-cares.
- Group C: MUX function realization (came in 2024-25 for 8 marks) and multi-part K-map + implementation questions.
- **Formulas:** FA: S=A⊕B⊕C, $C_{out}$ = majority · MUX 2ⁿ:1 has n selects · group of 2ᵏ kills k variables · XOR = parity.

*(End of Unit 2)*


---

# UNIT 3 — SEQUENTIAL CIRCUITS

*Sequential = output depends on present inputs AND stored past (memory). One flip-flop stores one bit. This unit supplies the "design a counter / register" questions that anchor Group C.*

## Chapter 9: Latches and Flip-Flops

### 9.1 The SR latch — where memory begins

Two cross-coupled NOR gates (or NAND with active-low inputs). Inputs S (set), R (reset); outputs Q and Q'.

| S | R | Q(next) | Meaning |
|---|---|---|---|
| 0 | 0 | Q | hold (memory!) |
| 1 | 0 | 1 | set |
| 0 | 1 | 0 | reset |
| 1 | 1 | — | **invalid/forbidden** (both outputs forced same; race on release) |

**PYQ 1-marker (2024-25): the invalid state of an SR latch occurs when S and R are both HIGH** (for the NOR version; for the NAND version it is both LOW — say which latch you mean).

**Latch vs flip-flop (1-marker):** a latch is level-sensitive (transparent while enable is high); a flip-flop is **edge-triggered** — it samples inputs only on a clock edge. Edge triggering is what makes large synchronous systems possible: every FF updates at one crisp instant.

### 9.2 The four flip-flop types — characteristic behaviour

| FF | Inputs | Next state Q⁺ | One-line job |
|---|---|---|---|
| SR | S,R | S + R'Q (SR=11 forbidden) | set/reset memory |
| **JK** | J,K | **JQ' + K'Q** | SR with 11 legalized → toggle |
| D | D | D | capture/delay one bit |
| T | T | TQ' + T'Q = T ⊕ Q | toggle when T=1 |

**JK vs SR (2024-25 MCQ):** the functional difference is that **JK accepts J=K=1** (it toggles) — that's the whole point of JK.

**Excitation tables (needed for counter design — memorize):**

| Q→Q⁺ | S R | J K | D | T |
|---|---|---|---|---|
| 0→0 | 0 X | 0 X | 0 | 0 |
| 0→1 | 1 0 | 1 X | 1 | 1 |
| 1→0 | 0 1 | X 1 | 0 | 1 |
| 1→1 | X 0 | X 0 | 1 | 0 |

*(Pattern: JK is the laziest table — an X in every row — which is why JK designs give the simplest logic.)*

### 9.3 Race-around and the Master-Slave JK (Group C every other year)

**The problem:** with J=K=1 and a level clock, the JK toggles; if the clock pulse width $t_{p}$ is longer than the propagation delay $t_{pd}$, the output toggles *again and again* during one pulse — final state unpredictable. This is the **race-around condition**. It occurs when **$t_{pd}$ < $t_{p}$** (and toggling is enabled).

**The fix — Master-Slave JK:** two SR/JK latches in series; master clocked by CLK, slave by CLK'. While CLK is high the master follows inputs (slave frozen); when CLK falls, the master freezes and the slave copies it. Output changes only once, at the falling edge → race eliminated. Timing diagram to draw: clock, master output (changes during high), slave/Q (steps once per falling edge).

*(Modern answer to finish with: pure edge-triggered FFs also eliminate race-around; master-slave is the classical solution the syllabus names.)*

### 9.4 Flip-flop conversions (Group B staple — 2023-24 asked JK→SR)

**Method (works for every pair):** write the target FF's excitation table → for each (Q, target-inputs) row, look up what the *available* FF's inputs must be → K-map the available inputs in terms of Q and target inputs.

**JK → D (2026-predicted MCQ):** D = JQ' + K'Q must equal D... solve: **J = D, K = D'** — a single **NOT gate** between J and K.

**JK → T:** J = K = T. **D → JK:** D = JQ' + K'Q. **SR → JK:** S = JQ', R = KQ (guarantees SR≠11 ✓).

**JK → SR:** J = S, K = R satisfies all rows where SR≠11 (with the forbidden row excluded by specification).

### 9.5 D flip-flop as a delay element

Q⁺ = D: the bit appears at Q one clock later — a **delay switch** (2024-25 MCQ answer). Chain n of them = n-clock delay = the shift register of the next chapter.

---

## Chapter 10: Registers

### 10.1 What a register is

n flip-flops sharing a clock = an n-bit register. A **shift register** additionally passes each FF's output to the next FF's input, moving the word one position per clock.

### 10.2 The four data-movement modes (know the timing for each)

| Mode | Load | Read | Clocks for n bits (in→out) |
|---|---|---|---|
| SISO | serial | serial | n to load, n to read |
| SIPO | serial | parallel | n to load, read at once |
| PISO | parallel | serial | 1 to load, n to read |
| PIPO | parallel | parallel | 1 and 1 |

**Design detail for PISO/parallel load:** each FF's D input comes through a 2:1 MUX: select line chooses (load ? parallel bit : previous FF's Q). "Design a 4-bit shift register using D/JK flip-flops" = lab experiment 7 and a 5-mark regular; drawing four D-FFs in chain with the MUX-per-stage for load mode is a complete answer.

**Uses (1-mark list):** serial↔parallel conversion, delay lines, multiplication/division by 2 (shift left/right), keyboard scanning, communication links.

---

## Chapter 11: Counters

### 11.1 Asynchronous (ripple) counters

Chain T/JK FFs (all inputs tied to 1); each FF clocks from the *previous FF's output*. Each stage divides frequency by 2 → n stages count 0…2ⁿ−1.

**The speed limit — and the numerical MAKAUT loves (2024-25 Group C, 5 marks):** clock edges *ripple* through the chain, so the worst-case settling time is n·$t_{pd}$.

**Worked (the actual PYQ):** *4-bit (mod-16) ripple counter, each FF has $t_{pd}$ = 50 ns. Maximum clock frequency?*
$f_{max}$ = 1/(n·$t_{pd}$) = 1/(4 × 50 ns) = 1/200 ns = **5 MHz**.
*(General formula: $f_{max}$ = 1/(n·$t_{pd}$). If a strobe/decode time $t_{s}$ is given: $f_{max}$ = 1/(n·$t_{pd}$ + $t_{s}$).)*

```{=latex}
\begin{center}\begin{tikzpicture}[ff/.style={draw,thick,minimum width=1.4cm,minimum height=1cm,fill=accentlight}]
\node[ff] (f0) {JK$_0$}; \node[ff,right=8mm of f0] (f1) {JK$_1$}; \node[ff,right=8mm of f1] (f2) {JK$_2$}; \node[ff,right=8mm of f2] (f3) {JK$_3$};
\draw[->,thick] (-1.1,0)node[left]{\scriptsize CLK}--(f0);
\foreach \a/\b in {f0/f1,f1/f2,f2/f3}{\draw[->,thick] (\a)--node[above]{\scriptsize $Q$}(\b);}
\foreach \f/\q in {f0/{Q_0},f1/{Q_1},f2/{Q_2},f3/{Q_3}}{\draw[->] (\f.north)--++(0,0.4) node[above]{\scriptsize $\q$};}
\node at (3.3,-0.95) {\scriptsize ripple counter: worst-case settling $=4\,t_{pd}$ — each stage waits for the previous edge};
\end{tikzpicture}\end{center}
```

**Decoding glitches:** intermediate ripple states cause momentary false outputs — the other standard "disadvantage of asynchronous counters" (2023-24 Group B: sync vs async differences).

### 11.2 Synchronous counters

All FFs share the clock; next-state logic (from excitation tables) feeds each input → no cumulative delay, $f_{max}$ = 1/($t_{pd}$ + t_logic) regardless of length.

**Design recipe (the Group C money-procedure — MOD-6 with T-FFs asked 2023-24):**
1. State diagram: 000→001→010→011→100→101→000 (states 110, 111 unused).
2. State table with present → next state.
3. Excitation table columns for each FF input via the FF's excitation rules.
4. K-map each input (unused states = don't-cares).
5. Draw the circuit; state that unused states must be checked to re-enter the cycle (self-correcting design).

**MOD-6 with T-FFs, fully derived.** T = 1 exactly where the bit must flip between present and next state:

| Present Q₂Q₁Q₀ | Next | T₂ T₁ T₀ |
|---|---|---|
| 000 | 001 | 0 0 1 |
| 001 | 010 | 0 1 1 |
| 010 | 011 | 0 0 1 |
| 011 | 100 | 1 1 1 |
| 100 | 101 | 0 0 1 |
| 101 | 000 | 1 0 1 |

K-maps (states 110, 111 = don't-cares): T₀ is 1 in every used row → **T₀ = 1**. T₁ has minterms {1, 3} + d{6,7} → **T₁ = Q₂'Q₀**. T₂ has minterms {3, 5} + d{6,7} → group m3 with d7 (giving Q₁Q₀) and m5 with d7 (giving Q₂Q₀) → **T₂ = Q₀(Q₁ + Q₂)**.

In the exam, present the full 5-step recipe with this table and your K-maps — the method carries most of the 15 marks; bare final equations earn little.

**MOD-N general rule:** need n FFs where 2ⁿ⁻¹ < N ≤ 2ⁿ. **Ripple-counter shortcut for MOD-N:** decode state N with a NAND → hit all CLEAR pins (e.g. MOD-10: NAND of Q₃Q₁ clears at 1010). Lab experiment 9.

### 11.3 Ring and Johnson counters (shift-register counters)

**Ring counter:** SIPO ring — last Q feeds first D; initialize with a single 1. n FFs → **n states**, one-hot outputs (no decoding needed).
1000 → 0100 → 0010 → 0001 → 1000…

**Johnson (twisted-ring/switch-tail):** feed back the *complement* Q'(last) to the first D. n FFs → **2n states**, decodable with 2-input ANDs.
For 4 FFs: 0000→1000→1100→1110→1111→0111→0011→0001→0000 (8 states).

**Comparison (5-mark half, asked with "design a 4-bit Johnson counter using D-FFs" — 2024-25-adjacent Group C):**

| | Ring | Johnson |
|---|---|---|
| States from n FFs | n | 2n |
| Feedback | Q → D₀ | **Q' → D₀** |
| Decoding | free (one-hot) | 2-input gates |
| Unused states | 2ⁿ−n (must self-correct) | 2ⁿ−2n |

**1-mark counts:** ring with 5 FFs → 5 states; Johnson with 5 FFs → 10 states; MOD-60 (digital clock seconds) needs 6 FFs.

### 11.4 Exam Focus + rapid recall (Unit 3)

- **Every year, guaranteed:** flip-flop truth/characteristic tables (Group A), race-around + master-slave (Group B/C), one counter design (Group C), register modes (Group A/B).
- **$f_{max}$(ripple) = 1/(n·$t_{pd}$)** — the one formula that converts directly into 5 marks.
- Excitation-table Xs make JK cheapest; D is simplest to think in; T is the counter's natural FF.
- Johnson = twisted ring, 2n states; Ring = n states, one-hot.
- FF count for MOD-N: ⌈log₂N⌉.

*(End of Unit 3)*


---

# UNIT 4 — DATA CONVERTERS & LOGIC FAMILIES

*The bridge unit: converters connect the analog world (Unit 1) to the digital world (Units 2-3); logic families are the physics underneath every gate you've drawn. Only 6 lecture-hours, but it contributes 2-3 Group A questions and one Group B in every real paper.*

## Chapter 12: Digital-to-Analog Conversion (syllabus: R-2R only)

### 12.1 Why DACs

Every digitally stored signal (audio, video, control setpoints) must eventually drive an analog world. A DAC converts an n-bit word into a proportional voltage: $V_{out}$ = K × (binary value).

### 12.2 The weighted-resistor DAC — and why it fails

One resistor per bit: R, R/2, R/4, … summing into an op-amp. Problem: for 8+ bits the resistor spread (R to R/128) makes matched precision impossible in IC form. It exists in the book only to justify the R-2R ladder.

### 12.3 The R-2R ladder — full analysis (Group B/C regular: "explain R-2R DAC and why it is preferred")

**Only two resistor values (R and 2R)** arranged as a ladder; each bit switches its 2R leg between ground and $V_{ref}$.

**The key insight (state it, then use it):** looking left from any ladder node, the equivalent resistance is always **2R**. Proof by induction: at the leftmost node, 2R ∥ 2R = R, which adds in series with the next R to give 2R again — the pattern telescopes down the ladder.

**Consequence:** each bit's contribution, propagated through the ladder to the output node, is halved relative to the bit above it — exactly the binary weighting 1/2, 1/4, 1/8, … With an op-amp buffer:

$V_{out}$ = −$V_{ref}$ × ($R_{f}$/2R)... in the standard inverting configuration with $R_{f}$ = 2R:

**$V_{out}$ = −$V_{ref}$ × (D/2ⁿ)**, D = decimal value of the input word.

**Why preferred over weighted-resistor (the 5-mark contrast):** only two values → easy IC matching and trimming; impedance seen by every switch is constant; extendable to any n without exotic resistor values.

**Worked numerical:** 4-bit R-2R, $V_{ref}$ = 16 V, input 1010 (D=10): |$V_{out}$| = 16 × 10/16 = **10 V**. (Resolution/LSB step = $V_{ref}$/2ⁿ = 1 V.)

### 12.4 DAC specs (1-markers)

- **Resolution** = $V_{FS}$/(2ⁿ − 1) (smallest step) — an 8-bit DAC with 10 V FS: 39.2 mV.
- **Accuracy, linearity, settling time, monotonicity** — one-line definitions each.
- Lab experiment 10 = "Study of DAC."

## Chapter 13: Analog-to-Digital Conversion (syllabus: successive approximation)

### 13.1 The ADC landscape (comparison MCQs guaranteed)

| Type | Conversion time | Hardware | Note |
|---|---|---|---|
| **Flash** | fastest (1 clock) | 2ⁿ−1 comparators — most expensive | **"simplest, fastest, most expensive" — 2024-25 MCQ** |
| Successive approximation | n clocks, fixed | 1 comparator + DAC + SAR | the industry workhorse; **syllabus focus** |
| Counter/ramp | up to 2ⁿ clocks | minimal | slow |
| **Dual-slope** | slowest (ms) | integrator | best noise/**hum rejection** — **2024-25 Group B: "which ADC for hum rejection?" → dual-slope**, because integrating over a mains period averages 50 Hz noise to zero |

### 13.2 Successive approximation — the algorithm (know it as a story *and* a table)

Binary search on the DAC's output. The SAR (successive-approximation register) proposes bits MSB-first:

1. Set MSB=1 → DAC outputs $V_{FS}$/2 → comparator: is $V_{in}$ ≥ $V_{DAC}$? keep the 1 : reset to 0.
2. Set next bit, DAC now at (kept bits + new bit) → compare → keep/clear.
3. Repeat for all n bits → conversion complete in exactly **n clock cycles**, independent of $V_{in}$.

**Worked (Group B pattern):** 4-bit SAR, $V_{FS}$ = 16 V, $V_{in}$ = 10.4 V.
b₃: try 8 V → 10.4 ≥ 8 keep → 1000 (8V). b₂: try 8+4=12 → 10.4 < 12 clear → 1000. b₁: try 8+2=10 → 10.4 ≥ 10 keep → 1010. b₀: try 8+2+1=11 → 10.4 < 11 clear → **1010** (= 10 V, error 0.4 V < 1 LSB ✓).

**Specs:** conversion time = n·$T_{clk}$ (fixed — its big advantage over counter-type); needs a sample-and-hold in front (input must not change mid-search).

**ADC-frequency MCQ from 2024-25 Group A:** "range of frequency measured by ADC" → **bandwidth**.

## Chapter 14: Logic Families — TTL, ECL, MOS, CMOS

### 14.1 What a "family" is and the six figures of merit

A logic family = a standard circuit technology for gates, characterized by:
**propagation delay $t_{pd}$ · power dissipation $P_{D}$ · noise margin · fan-out · fan-in · speed-power product (figure of merit, pJ)**. Define each in one line — a 5-mark "define the parameters" question recurs.

Noise margins: $NM_{H}$ = $V_{OH}$(min) − $V_{IH}$(min); $NM_{L}$ = $V_{IL}$(max) − $V_{OL}$(max).

### 14.2 The four families, one paragraph each

**TTL (Transistor-Transistor Logic, 74xx):** multi-emitter BJT input + totem-pole output. $t_{pd}$ ≈ 10 ns, $P_{D}$ ≈ 10 mW/gate, fan-out ~10, $V_{CC}$ = 5 V. Saturated logic (transistors driven into saturation → storage delay limits speed). Subfamilies: 74LS (Schottky-clamped — a Schottky diode across B-C stops saturation, per your Unit-1 prerequisite on Schottky diodes), 74S, 74F.

**ECL (Emitter-Coupled Logic):** differential pair steered *without saturation* → **fastest family, $t_{pd}$ ≈ 1-2 ns** — the answer to the perennial MCQ (2024-25: "fastest logic family → ECL"). Price: highest power (~25-40 mW/gate), poor noise margin (~0.2-0.3 V), negative supply (−5.2 V), complementary outputs free.

**MOS (NMOS/PMOS):** MOSFET-only gates; excellent density (memories, calculators), slow-ish, cheap. Historically the LSI family before CMOS took over.

**CMOS (Complementary MOS, 4000/74HC):** PMOS pull-up network + NMOS pull-down network — **only one network conducts at a time → essentially zero static power** (µW). Dissipation is dynamic: P ≈ C·V²·f (grows with frequency — the classic trap: "CMOS is always lowest power" is false at very high f). Widest supply range (3-15 V), best noise margin (~0.45 $V_{DD}$), fan-out >50, but $t_{pd}$ is load-dependent. All modern processors are CMOS.

### 14.3 The comparison table (reproduce for any 5-mark "compare families")

| Parameter | TTL | ECL | CMOS |
|---|---|---|---|
| Basic device | BJT (saturated) | BJT (non-saturated) | MOSFETs |
| $t_{pd}$ | ~10 ns | **~1-2 ns (fastest)** | ~10-50 ns (load-dep.) |
| Power/gate | ~10 mW | ~25-40 mW (highest) | ~µW static (**lowest**) |
| Noise margin | ~0.4 V | ~0.25 V (worst) | ~0.45·$V_{DD}$ (**best**) |
| Fan-out | 10 | 25 | >50 (**best**) |
| Supply | +5 V | −5.2 V | 3-15 V |

**Interfacing note (occasional 1-marker):** TTL→CMOS needs a pull-up resistor; CMOS→TTL may need a buffer for current drive.

### 14.4 Exam Focus + rapid recall (Unit 4)

- Group A bank: fastest family (ECL) · lowest power (CMOS) · flash = fastest ADC · dual-slope = hum rejection · SAR takes n clocks · R-2R uses only two values · resolution formulas.
- Group B bank: R-2R explanation + preference argument · SAR algorithm with worked example · family comparison table · ADC-type comparison.
- **Formulas:** $V_{out}$(R-2R) = $V_{ref}$·D/2ⁿ · resolution = $V_{FS}$/(2ⁿ−1) · SAR time = n·$T_{clk}$ · $NM_{H}$ = $V_{OH}$ − $V_{IH}$ · $P_{CMOS}$ ≈ CV²f.

*(End of Unit 4)*

---

# APPENDIX A — THE ONE-SITTING FORMULA SHEET (ESC-301)

**Unit 1:** $\eta_{A}$ = 25% (series) / 50% (transformer) · $\eta_{B}$(max) = π/4 = 78.5% · $P_{dc}$(B) = 2V_CC $I_{m}$/π · Barkhausen |Aβ|=1, ∠360° · f(phase-shift) = 1/2πRC√6, A ≥ 29 · f(Wien) = 1/2πRC, A ≥ 3 · 555: $T_{mono}$ = 1.1RC; $T_{H}$ = 0.693($R_{A}$+$R_{B}$)C; $T_{L}$ = 0.693R_B C; f = 1.44/($R_{A}$+2R_B)C; D = ($R_{A}$+$R_{B}$)/($R_{A}$+2R_B); thresholds $V_{CC}$/3, 2V_CC/3.

**Unit 2:** 2's comp = invert+1; range −2ⁿ⁻¹…2ⁿ⁻¹−1 · overflow V = $C_{in}$⊕$C_{out}$ (MSB) · Gray gᵢ = bᵢ₊₁⊕bᵢ · De Morgan: break bar, change sign · K-map group 2ᵏ kills k variables · FA: S = A⊕B⊕$C_{in}$, $C_{out}$ = AB+$BC_{in}$+$AC_{in}$ · MUX 2ⁿ:1 → n selects · even-parity bit = XOR of data.

**Unit 3:** Q⁺(JK) = JQ'+K'Q · Q⁺(T) = T⊕Q · race-around iff $t_{p}$ > $t_{pd}$ with J=K=1; cure = master-slave (or edge triggering) · $f_{max}$(ripple) = 1/(n·$t_{pd}$) · ring: n states; Johnson: 2n states · FFs for MOD-N: ⌈log₂N⌉ · JK→D: J=D, K=D'.

**Unit 4:** $V_{out}$(R-2R) = $V_{ref}$·D/2ⁿ · resolution = $V_{FS}$/(2ⁿ−1) · SAR: n clocks · flash: 2ⁿ−1 comparators · ECL fastest, CMOS lowest static power, best noise margin · $P_{CMOS}$ ≈ CV²f.

*— End of the ADE Concept Book —*


---

# 📺 VIDEO COMPANION — topic-wise (from your chosen playlists)

> Not covered by these playlists: 555 timer/multivibrators/Schmitt, amplifier classes (thin), DAC/ADC (thin), logic families (thin) — study these from the book chapters; the Neso Analog playlist covers device fundamentals outside this syllabus (its extra videos are omitted).


### Unit1: Amplifier classes & power amplifiers
- [Half Wave Rectifier (Efficiency & PIV)](https://www.youtube.com/watch?v=XLBtAmcXYKA) (4:54)
- [Full Wave Rectifier (Efficiency & PIV)](https://www.youtube.com/watch?v=NzxjUGk_pFE) (7:00)
- [Diode Rectifier Circuits (Numerical Problem)](https://www.youtube.com/watch?v=UQVAFcCLoKo) (7:06)

### Unit1: Feedback & oscillators
- [Collector Feedback Biasing](https://www.youtube.com/watch?v=wg0OqrUXDjI) (7:43)
- [Collector Feedback Biasing (Solved Problem)](https://www.youtube.com/watch?v=9KzApMILLU0) (5:31)
- [Collector Feedback Bias with Emitter Resistance](https://www.youtube.com/watch?v=wah516ZoPtQ) (7:07)
- [Stability Factor for Collector Feedback Biasing](https://www.youtube.com/watch?v=6RReE_J7fbA) (9:21)
- [re Model (Fixed-Bias Configuration) | Part 3](https://www.youtube.com/watch?v=1YCSoDQSBiU) (9:42)

### Unit2: Number systems & codes
- [Introduction to Boolean Algebra (Part 1)](https://www.youtube.com/watch?v=WW-NPtIzHwk) (18:11)
- [Complement Meaning and Examples](https://www.youtube.com/watch?v=bY8o35iCyGQ) (7:00)
- [Introduction to Number Systems](https://www.youtube.com/watch?v=crSGS1uBSNQ) (9:15)
- [Binary Number System](https://www.youtube.com/watch?v=w7ZLvYAi6pY) (8:25)
- [Decimal to Binary Conversion](https://www.youtube.com/watch?v=2U9b76JRz7s) (9:53)
- [Decimal to Octal Conversion](https://www.youtube.com/watch?v=1J89-aWI-5Y) (4:43)

### Unit2: Boolean algebra & K-map
- [Full Wave Bridge Rectifier](https://www.youtube.com/watch?v=Kl8IOESVWlM) (12:43)
- [Full Wave Center-Tapped Rectifier](https://www.youtube.com/watch?v=CGZ0yHaAmjs) (6:23)
- [Positive & Negative Clamper Circuits](https://www.youtube.com/watch?v=zFdy23F-pEM) (6:34)
- [Touch Sensor Using Darlington Pair](https://www.youtube.com/watch?v=curtlVdY94w) (3:29)
- [Pinch-off Voltage](https://www.youtube.com/watch?v=-o39YVNMYVs) (11:43)
- [Working of Depletion-Type MOSFET](https://www.youtube.com/watch?v=XbVybFiL69s) (14:22)

### Unit2: Adders/subtractors
- [Half Adder](https://www.youtube.com/watch?v=aLUY-s7LSns) (5:10)
- [Full Adder](https://www.youtube.com/watch?v=RK3P9L2ZXk4) (13:37)
- [Full Adder using Half Adder](https://www.youtube.com/watch?v=Z_DYRgtAXfw) (7:19)
- [4 Bit Parallel Adder using Full Adders](https://www.youtube.com/watch?v=NO7Gt8IDSGA) (10:27)
- [Half Subtractor](https://www.youtube.com/watch?v=SV4VTYWxKV4) (6:56)
- [Full Subtractor | Easy Explanation](https://www.youtube.com/watch?v=dBXGGWbtt6U) (7:41)

### Unit2: Encoder/decoder/MUX/comparator/parity
- [What is Parity?](https://www.youtube.com/watch?v=DdMcAUlxh1M) (8:32)
- [4-Bit Even Parity Generator](https://www.youtube.com/watch?v=RfTGvpY2Z5Y) (10:18)
- [Seven Segment Display Decoder](https://www.youtube.com/watch?v=smeUN1Bxj3M) (6:58)
- [Seven Segment Display Decoder (Part 2)](https://www.youtube.com/watch?v=_qGFpgpqf7s) (8:35)
- [Seven Segment Display Decoder (Part 3)](https://www.youtube.com/watch?v=vZKRs_1jPeI) (7:56)
- [Introduction to Multiplexers | MUX Basic](https://www.youtube.com/watch?v=FKvnmxte98A) (12:26)

### Unit3: Flip-flops & latches
- [SR Latch | NOR and NAND SR Latch](https://www.youtube.com/watch?v=kt8d3CYWGH4) (16:41)
- [Triggering Methods in Flip Flops](https://www.youtube.com/watch?v=Pi_MHyMoenA) (4:39)
- [Difference between Latch and Flip Flop](https://www.youtube.com/watch?v=m1QBxTeVaNs) (5:32)
- [Introduction to SR Flip Flop](https://www.youtube.com/watch?v=HZg7fNu-l24) (8:23)
- [Truth Table, Characteristic Table and Excitation Table for SR Flip Flop](https://www.youtube.com/watch?v=uiKKRPZbuXA) (8:56)
- [Introduction to D flip flop](https://www.youtube.com/watch?v=dnfXXpW7tIw) (4:35)

### Unit3: Registers
- [Introduction to Registers](https://www.youtube.com/watch?v=-paFaxtTCkI) (7:14)
- [Data Formats and Classification of Registers](https://www.youtube.com/watch?v=b43_I4r1R2c) (7:26)
- [Shift Register (SISO Mode)](https://www.youtube.com/watch?v=unorn9n-UpE) (11:30)
- [Shift Register (SIPO & PIPO Mode)](https://www.youtube.com/watch?v=HGFGQ3D3iJ8) (11:53)
- [Shift Register (PISO Mode)](https://www.youtube.com/watch?v=7LmBcGiiYwk) (7:26)
- [Bidirectional Shift Register](https://www.youtube.com/watch?v=zoEeQgQkPLA) (7:57)

### Unit3: Counters
- [Introduction to Counters | Important](https://www.youtube.com/watch?v=iaIu5SYmWVM) (11:40)
- [Types of Counters | Comparison between Ripple and Synchronous counters](https://www.youtube.com/watch?v=yqg1sqhZG3M) (7:06)
- [3 Bit Asynchronous Up Counter](https://www.youtube.com/watch?v=s1DSZEaCX_g) (11:47)
- [4 Bit Asynchronous Up Counter](https://www.youtube.com/watch?v=eEeBh8jfDjg) (9:32)
- [3 bit & 4 bit Asynchronous Down Counter](https://www.youtube.com/watch?v=noUcCs2zNaI) (10:22)
- [3 Bit & 4 Bit UP/DOWN Ripple Counter](https://www.youtube.com/watch?v=5Um3NDvsYjQ) (10:19)

### Unit4: DAC/ADC
- [Half Wave Rectifier (RMS Load Current & RMS Load Voltage)](https://www.youtube.com/watch?v=XTfWAYuyfVU) (6:53)

### Unit4: Logic families
- [Biased Series Clippers](https://www.youtube.com/watch?v=pieY6wUEGbU) (9:03)
- [Positive & Negative Clamper Circuits](https://www.youtube.com/watch?v=zFdy23F-pEM) (6:34)
