# COMPUTER ORGANIZATION — The Complete Concept Book
### MAKAUT PCC-CS302 · B.Tech Sem-3 · Built from Mano (Computer System Architecture) + Hamacher (Computer Organization) + 3 years of real MAKAUT papers

> Same contract as every book in this series: master this and you need no other source. Chapters follow *why → theory with every derivation → worked examples → Exam Focus (real years, real groups) → traps → rapid recall*. Format: 70 marks; Group A 10×1, Group B 3×5, Group C 3×15.

---

# UNIT 1 — BASIC ORGANIZATION OF THE STORED-PROGRAM COMPUTER

## Chapter 1: The Stored-Program Idea

### 1.1 Why it exists

Before von Neumann, "programming" meant rewiring. The stored-program concept — **instructions live in the same memory as data, encoded as numbers** — turned the computer into a general machine: change the program, not the wiring. Every question in this subject traces back to this one idea and its plumbing.

**The functional diagram (2024-25 Group C 8(a), 6 marks — draw and explain):** five blocks — Input → Memory ← → ALU + Control (together the CPU/processor) → Output; the control unit issues signals to every other block. Explain each block's one-line role and the instruction/data paths between them.

```{=latex}
\begin{center}\begin{tikzpicture}[blk/.style={draw,thick,rounded corners,minimum width=2.1cm,minimum height=0.95cm,fill=accentlight}]
\node[blk] (mem) {Memory};
\node[blk,below left=10mm and 5mm of mem] (alu) {ALU};
\node[blk,below right=10mm and 5mm of mem] (cu) {Control Unit};
\node[blk,left=15mm of mem] (in) {Input};
\node[blk,right=15mm of mem] (out) {Output};
\draw[<->,thick] (mem)--(alu); \draw[<->,thick] (mem)--(cu); \draw[<->,thick] (alu)--(cu);
\draw[->,thick] (in)--(mem); \draw[->,thick] (mem)--(out);
\node[draw,dashed,fit=(alu)(cu),inner sep=4pt,label={[font=\scriptsize]below:CPU}] {};
\end{tikzpicture}\end{center}
```

**Von Neumann bottleneck (2023-24 Group B, 5 marks):** one shared memory and one bus carry *both* instructions and data → the CPU stalls waiting on memory traffic; the processor-memory speed gap makes the single channel the system's rate limiter. Mitigations: caches, Harvard-style split instruction/data paths, prefetching, wider buses.

### 1.2 The registers that run the show (Group A bank)

| Register | Role |
|---|---|
| **PC (program counter)** | **holds the address of the next instruction** — the 2022-23 and 2024-25 Group A answer verbatim |
| IR | holds the current instruction being decoded |
| MAR | address to be accessed in memory |
| MDR/MBR | data on its way to/from memory |
| AC | accumulator — implicit operand of 1-address machines |
| SP | stack pointer — implicit operand of 0-address machines |

**Register-transfer language (2022-23 Group A):** M[AR] ← R3 means "write R3's contents into the memory word whose address is in AR" — a **memory write**.

### 1.3 Instruction cycle, machine cycle, T-state (2024-25 Group B, 5 marks — define all three)

- **T-state:** one period of the system clock — the atomic time unit of the control unit.
- **Machine cycle:** one complete memory/I-O access (fetch, memory read, memory write…), built from several T-states.
- **Instruction cycle:** everything needed to fetch-decode-execute one instruction — one or more machine cycles.

**Fetch-decode-execute in register transfers (learn as a sequence):**
T0: MAR ← PC · T1: MDR ← M[MAR], PC ← PC+1 · T2: IR ← MDR · decode · then execute microoperations depend on the opcode (possible further operand fetches). Interrupt check closes each cycle.

### 1.4 The common-bus MCQ (2022-23 Group A, classic numerical)

*16 registers of 32 bits share a bus built from multiplexers — how many selection inputs per MUX?* Choosing 1 of 16 sources needs **4 select lines** (2⁴ = 16); the bus uses 32 such 16:1 MUXes, one per bit, all sharing the 4 selects. (The counterpart: a 10-bit counter at 1001100111 → next count flips the trailing 0111+? — count the flipped FFs: adding 1 to …0111 toggles the low 4 bits: **4 flip-flops complemented**.)

## Chapter 2: Instruction Formats and Addressing Modes

### 2.1 Zero/one/two/three-address instructions (a full 15-marker in 2022-23; 6 marks in 2024-25 — appears in some form EVERY year)

Evaluate X = (A+B)×(C+D) in each style:

**3-address:** ADD R1, A, B · ADD R2, C, D · MUL X, R1, R2 — shortest program, longest instructions.
**2-address:** MOV R1, A · ADD R1, B · MOV R2, C · ADD R2, D · MUL R1, R2 · MOV X, R1 — destination doubles as a source.
**1-address (accumulator):** LOAD A · ADD B · STORE T · LOAD C · ADD D · MUL T · STORE X — AC implicit everywhere.
**0-address (stack):** PUSH A · PUSH B · ADD · PUSH C · PUSH D · ADD · MUL · POP X — operands implicit on the stack; expressions must be in **reverse Polish (postfix)** order.

**The trade-off sentence that earns the "compare" marks:** fewer addresses per instruction → shorter instructions but more of them; the program-length vs instruction-width trade is the whole story of ISA width design.

**2022-23 Group B numerical (5 marks) — worked:**

*32-bit instructions; 64 registers; 45 opcodes; instructions carry one immediate + two register operands. Find the maximum unsigned immediate.*

**Solution.** Budget the 32 bits field by field:

```{=latex}
\begin{align*}
\text{opcode bits} &= \lceil \log_2 45 \rceil = 6\\
\text{register fields} &= 2 \times \log_2 64 = 2\times6 = 12\\
\text{immediate bits} &= 32 - 6 - 12 = 14
\end{align*}
```

$$\therefore\ \text{max unsigned immediate} = 2^{14} - 1 = \mathbf{16383}$$

### 2.2 Addressing modes (Group C staple: "discuss with examples" — 2022-23 Q10-pattern)

| Mode | Effective address / operand | Example & use |
|---|---|---|
| Immediate | operand inside the instruction | MOV R1, #5 — constants |
| Direct (absolute) | EA given in instruction | **ADD X, Y — the 2022-23 Group A answer: direct/absolute mode** |
| Indirect | instruction points to a word holding EA | pointers |
| Register | operand in a register | fastest |
| Register indirect | EA in a register | array walking via pointer |
| Indexed / Base | EA = base + index register | arrays, relocation |
| Relative | EA = PC + offset | branches, position-independent code |
| Auto-inc/dec | register indirect, then ±1 | stack/stream access |

For 15 marks: define + one example + one line of "why it exists" per mode, then the classic single-accumulator program (2022-23: *evaluate X = A − B + C − D with load/store/add/sub*: LOAD A · SUB B · ADD C · SUB D · STORE X) and the zero-vs-one-address contrast.

### 2.3 Software context questions (cheap Group A marks, all real)

- Program acting between user and hardware: **operating system** (2023-24). OS = resource manager + user/hardware interface; roles: process, memory, file, device management, protection (the 2023-24 15-marker enumerates these with a paragraph each).
- **Interpreter** (2023-24): translates and executes a program line-by-line without producing an object file (contrast compiler: whole-program translation).
- OS is **system software** (2024-25).
- Self-contained instruction sequence doing a task: a **routine/subroutine** (2022-23).
- Microprocessor characteristics (2022-23): word length, clock speed, instruction set, addressing capability, on-chip cache/registers.
- **Flynn's classification (2022-23 Group B, 5 marks):** by instruction/data stream counts — SISD (classic uniprocessor), SIMD (vector/GPU lanes), MISD (rare/pipelined redundancy), MIMD (multiprocessors). One example each is the full answer.

### 1-Unit rapid recall

PC → next instruction · IR current · instruction ⊃ machine ⊃ T-state · ADD X,Y = direct mode · postfix ↔ stack machines · immediate-field arithmetic: bits left over after opcode+registers · Flynn = S/M × I/D.

---

# UNIT 2 — COMPUTER ARITHMETIC

## Chapter 3: Number Representation

### 3.1 Signed integers, three ways (2022-23 Group C 10, 9+6 marks)

For 4-bit words:

| Decimal | Sign-mag | 1's comp | 2's comp |
|---|---|---|---|
| +5 | 0101 | 0101 | 0101 |
| −5 | 1101 | 1010 | 1011 |
| −0 | 1000 | 1111 | (none — single 0) |
| range | ±7 | ±7 | **−8…+7** |

2's complement wins: unique zero, subtraction = addition of complement, natural overflow rule.

**Real Group A one-liners:** 2's comp of 15 (5-bit) = 10001 (2023-24) · max n-bit 2's-comp number = **2ⁿ⁻¹ − 1** (2024-25) · −7 − 1 = −8 → 1000 in 4-bit 2's comp (2024-25: "subtract 1 from −7") · 16-bit rep of −6 = 1111111111111010 (2024-25) · (2FA0C)₁₆ → 0010 1111 1010 0000 1100₂ (2022-23) · (1101101110)₂ = 36E₁₆ (2024-25) · Carry & Overflow are **status/condition-code flags** (2023-24) · sign extension (2022-23 Group B): replicate the sign bit into the new high-order positions — 4-bit 1011 (−5) → 8-bit 11111011; preserves value for both signs because the replicated bits add (for negatives) a geometric series that telescopes to the same magnitude.

### 3.2 Fixed vs floating point (Group A + B every year)

Fixed point: binary point at a fixed position; fractions like 0.011010₂ = 0.40625₁₀ (2022-23 Group C 7(b): 1/4 + 1/8 + 1/32 = 0.40625); 0.6875₁₀ = 0.1011₂ (7(c)). Floating point stores **real numbers with fractional parts across a huge dynamic range** (2022-23 Group A answer).

**IEEE 754 (asked as a 5-marker in BOTH 2022-23 and 2023-24 — guaranteed):**
Single precision, 32 bits: **1 sign + 8 exponent (bias 127) + 23 mantissa**, value $= (-1)^s \times 1.M \times 2^{E-127}$. Double: 1 + 11 (bias 1023) + 52.
Special encodings: E=0 → denormals/zero; E=255 → ±∞ (M=0) or NaN (M≠0).
**Worked conversion (write one in every IEEE answer):** −13.25 = −1101.01₂ = −1.10101×2³ → s=1, E = 127+3 = 130 = 10000010, M = 10101000…0 → 1 10000010 10101000000000000000000 = **0xC1540000**.

## Chapter 4: Adders — Ripple Carry vs Carry Look-Ahead

### 4.1 Ripple carry (2022-23 Group C 7(a))

n full adders chained through their carries. Delay grows linearly: the MSB's sum isn't valid until the carry ripples through every stage — T ≈ n·$t_{FA}$. Draw 4 FAs, label C₀→C₄.

### 4.2 Carry look-ahead — the 7+8-mark Group C of 2023-24, and 4 marks again in 2024-25

Define per bit: **generate Gᵢ = AᵢBᵢ** (produces a carry regardless of $C_{in}$) and **propagate Pᵢ = Aᵢ⊕Bᵢ** (passes an incoming carry).

Carry recurrence: Cᵢ₊₁ = Gᵢ + PᵢCᵢ. **Unroll it** (this is the derivation the marks want):

```{=latex}
\begin{align*}
C_1 &= G_0 + P_0C_0\\
C_2 &= G_1 + P_1G_0 + P_1P_0C_0\\
C_3 &= G_2 + P_2G_1 + P_2P_1G_0 + P_2P_1P_0C_0\\
C_4 &= G_3 + P_3G_2 + P_3P_2G_1 + P_3P_2P_1G_0 + P_3P_2P_1P_0C_0
\end{align*}
```

Every carry is now a **two-level function of the inputs** — all carries appear in constant time (~4 gate delays for sums) instead of rippling. Cost: the AND-OR trees widen with n (fan-in limits), so real designs cascade 4-bit CLA blocks (74182-style group G*, P*). Sum: Sᵢ = Pᵢ ⊕ Cᵢ.
**Advantage sentence:** delay O(1)-ish vs O(n); the price is gate count/fan-in — speed bought with silicon.

### 4.3 Adder-subtractor composite (2024-25 Group B, 5 marks; also the lab)

XOR each Bᵢ with mode M feeding a ripple/CLA adder, C₀ = M. M=0: B passes, adds. M=1: B inverted and +1 via C₀ → A + B̄ + 1 = A − B. One circuit, both operations; overflow flag V = Cₙ ⊕ Cₙ₋₁.

## Chapter 5: Multiplication — Booth's Algorithm

### 5.1 Why Booth

Naive shift-and-add handles only unsigned numbers and wastes cycles on runs of 1s. Booth recodes runs ($\dots0\underbrace{11\dots1}_{} = 2^{k+1} - 2^m$) so a run of 1s costs one subtraction + one addition, and — the exam's favourite fact — **it works directly on 2's-complement signed numbers** (2024-25 Group A: "Booth's uses 2's-complement representation").

### 5.2 The algorithm (flowchart = 5 marks in 2024-25)

Registers: A (accumulator, 0), Q (multiplier), Q₋₁ (0), M (multiplicand), count n.
Loop n times: examine **Q₀Q₋₁**:
- 01 → A ← A + M
- 10 → A ← A − M
- 00/11 → nothing
then **arithmetic shift right** (A,Q,Q₋₁ together, sign of A preserved); decrement count. Product = A:Q (2n bits).

### 5.3 The real numerical, fully worked (2024-25 Group C 9(b): −9 × +6, 5-bit)

M = −9 = 10111, −M = 01001, Q = +6 = 00110, A = 00000, Q₋₁ = 0, n = 5.

| Step | Q₀Q₋₁ | Action | A after | Q after | Q₋₁ |
|---|---|---|---|---|---|
| 1 | 0,0 | shift only | 00000 | 00011 | 0 |
| 2 | 1,0 | A−M = A+01001 → 01001; shift | 00100 | 10001 | 1 |
| 3 | 1,1 | shift only | 00010 | 01000 | 1 |
| 4 | 0,1 | A+M = A+10111 → 11001; shift | 11100 | 10100 | 0 |
| 5 | 0,0 | shift only | 11110 | 01010 | 0 |

Product = A:Q = 11110 01010₂ (10-bit 2's comp) = −(00001 10110)₂ = **−54** ✓ (= −9×6).
*Presentation rule: show the table exactly like this — step, bit-pair, action, registers — the table IS the marks.*

## Chapter 6: Division — Restoring and Non-Restoring

### 6.1 Restoring division (flowchart = 2024-25 Group B, 5 marks)

Registers A (remainder, 0), Q (dividend), M (divisor), n steps:
1. Shift A:Q left 1.
2. A ← A − M.
3. If A ≥ 0: Q₀ ← 1. Else: Q₀ ← 0 and **restore** A ← A + M.
4. Repeat n times. Q = quotient, A = remainder.
Worst case ~2 operations per bit (subtract + restore).

### 6.2 Non-restoring

Skip the restore; carry the negative remainder forward and *add* next round instead of subtracting:
If A ≥ 0: shift, A ← A − M; else: shift, A ← A + M. Then Q₀ ← (A ≥ 0 ? 1 : 0). Final fix-up: if A < 0, A ← A + M. One operation per bit — the efficiency argument between the two is the standard 5-mark compare.

**Worked micro-example (7 ÷ 3, 4-bit, restoring):** A=0000 Q=0111 M=0011 → after 4 iterations Q = 0010, A = 0001 → quotient 2 remainder 1 ✓. (Practice writing the per-step table as in Booth.)

### Unit-2 rapid recall

IEEE 754: 1/8/23 bias 127; 1/11/52 bias 1023 · CLA: Cᵢ₊₁ = Gᵢ + PᵢCᵢ unrolled to 2 levels · Booth pairs: 01 add, 10 subtract, else shift; ASR keeps sign · restoring: subtract-test-restore; non-restoring: alternate ± · sub via adder: XOR + C₀ = 1 · V = Cₙ ⊕ Cₙ₋₁.

*(End of Units 1–2)*


---

# UNIT 3 — MEMORY

## Chapter 7: The Memory Hierarchy

### 7.1 Why a hierarchy

You cannot buy memory that is simultaneously fast, large and cheap — so build layers: **registers → cache (SRAM) → main memory (DRAM) → auxiliary storage (disk/SSD/tape)**, each larger, slower and cheaper per bit than the one above. It works because programs exhibit **locality of reference** — temporal (reuse what you just used) and spatial (use neighbours next) — which is *the* principle that "justifies the use of cache memory" (2024-25 Group A, verbatim).

```{=latex}
\begin{center}\begin{tikzpicture}[yscale=0.8]
\draw[thick,fill=accentlight] (-1.1,3)rectangle(1.1,3.85); \node at (0,3.42){\scriptsize Registers};
\draw[thick,fill=mintbg] (-2,2)rectangle(2,2.85); \node at (0,2.42){\scriptsize Cache (SRAM)};
\draw[thick,fill=boxamber] (-2.9,1)rectangle(2.9,1.85); \node at (0,1.42){\scriptsize Main memory (DRAM)};
\draw[thick,fill=rowalt] (-3.8,0)rectangle(3.8,0.85); \node at (0,0.42){\scriptsize Auxiliary storage (disk / SSD / tape)};
\draw[->,thick] (4.3,0)--(4.3,3.8) node[midway,right,align=left]{\scriptsize faster,\\\scriptsize costlier per bit};
\draw[->,thick] (-4.3,3.8)--(-4.3,0) node[midway,left,align=right]{\scriptsize larger,\\\scriptsize cheaper per bit};
\end{tikzpicture}\end{center}
```

**Group A bank (all real):** fastest memory in the hierarchy → **registers** (2023-24) · categories of storage → primary/secondary/cache/registers (2023-24) · auxiliary devices → magnetic disk, tape, SSD, optical (2023-24) · 2K RAM chip → **2048 locations** (2024-25) · 32K×16 built from 8K×8 chips → 4 rows of chips → needs a **2×4 decoder** (2024-25).

### 7.2 Average memory access time (2024-25 Group B numerical — worked)

*Three-level system: cache 15 ns (hit ratio 0.96), main memory 25 ns (hit ratio 0.9 of the misses), disk 40 ns.*

**Solution.** State the hierarchical-miss model, then substitute:

```{=latex}
\begin{align*}
\text{AMAT} &= h_1t_1 + (1-h_1)\big[h_2t_2 + (1-h_2)t_3\big]\\[2pt]
 &= 0.96\times15 + 0.04\times(0.9\times25 + 0.1\times40)\\[2pt]
 &= 14.4 + 0.04\times26.5 = 14.4 + 1.06
\end{align*}
```

$$\therefore\ \text{AMAT} = \mathbf{15.46\ \text{ns}}$$

*(State the hierarchical-miss model before substituting — the formula is worth 2 of the 5.)*

## Chapter 8: SRAM, DRAM and the Memory Cell

### 8.1 Static RAM (2023-24 Group B: "explain SRAM read and write")

Cell = **6 transistors: cross-coupled inverter pair (latch) + two access transistors** gated by the word line onto complementary bit lines B, B̄.
**Read:** precharge both bit lines; raise word line; the cell pulls one line low; a sense amplifier detects the differential → data out. Non-destructive.
**Write:** drive B, B̄ hard to the desired complementary values; raise word line; the drivers overpower the latch, flipping it.
Static = holds data while powered, no refresh; fast; expensive (6T) → caches.

### 8.2 Dynamic RAM (pairs with 2022-23 Group C 9: static vs dynamic MOS cell)

Cell = **1 transistor + 1 capacitor**; the bit is charge. Read is destructive (charge shares onto the bit line) → sense-and-rewrite; leakage requires **refresh every few ms** (row-by-row). Slow-ish, but ~6× denser and cheaper → main memory. The compare table (cell size, speed, refresh, cost, use) is a permanent 5-mark asset.

## Chapter 9: Cache Memory — the highest-scoring topic in this subject

### 9.1 Mapping: where can a block go?

Address = | TAG | LINE/SET | WORD offset |

```{=latex}
\begin{center}\begin{tikzpicture}
\draw[thick,fill=accentlight] (0,0) rectangle (3.4,0.8); \node at (1.7,0.4){\small TAG};
\draw[thick,fill=mintbg] (3.4,0) rectangle (5.4,0.8); \node at (4.4,0.4){\small SET/LINE};
\draw[thick,fill=boxamber] (5.4,0) rectangle (7.4,0.8); \node at (6.4,0.4){\small WORD};
\draw[decorate,decoration={brace,mirror}] (0,-0.15)--(7.4,-0.15) node[midway,below]{\scriptsize the CPU address, split by the cache geometry};
\node[above] at (1.7,0.82) {\scriptsize identifies the block};
\node[above] at (4.4,0.82) {\scriptsize picks the set};
\node[above] at (6.4,0.82) {\scriptsize offset in block};
\end{tikzpicture}\end{center}
```

- **Direct mapping:** block J → line J mod L. One comparator; cheap; but two hot blocks mapping to one line thrash. 
- **Fully associative:** block anywhere; TAG = whole block number; needs a comparator per line (expensive, no thrash).
- **k-way set-associative:** the compromise — line group (set) chosen by index, block anywhere within the set; k comparators.

**The 2023-24 Group C (8+7): "full associative vs direct mapping + write-through vs write-back"** — answer with the table above plus: **write-through** = update cache *and* memory on every write (simple, consistent, more bus traffic; add a write buffer); **write-back** = update cache only, mark the line **dirty/modified**, write memory on eviction (fast, but memory stale until then — needs the modified bit).

### 9.2 The two real numericals, fully worked — this pattern repeats

**(2022-23 Group C 8(a), 7 marks):**

*4-way set-associative cache, 128 lines, 64 words/line, 20-bit word address. Find the TAG/SET/WORD field widths.*

**Solution.**

```{=latex}
\begin{align*}
\text{sets} &= \frac{128\ \text{lines}}{4\ \text{ways}} = 32 &&\Rightarrow\ \text{SET} = \log_2 32 = 5\ \text{bits}\\[2pt]
\text{WORD} &= \log_2 64 = 6\ \text{bits}\\[2pt]
\text{TAG} &= 20 - 5 - 6 = \mathbf{9\ \text{bits}}
\end{align*}
```

$$\therefore\ \text{TAG/SET/WORD} = \mathbf{9/5/6}$$

**(2022-23 Group C 11(a), 7 marks):**

*8 KB direct-mapped write-back cache, 32-byte blocks, 32-bit addresses; each line's tag store holds 1 valid bit + 1 modified bit + minimum tag bits. Find the tag-store size.*

**Solution.**

```{=latex}
\begin{align*}
\text{lines} &= \frac{8\,\text{KB}}{32\,\text{B}} = 256 &&\Rightarrow\ \text{LINE} = 8\ \text{bits}\\[2pt]
\text{OFFSET} &= \log_2 32 = 5\ \text{bits}\\[2pt]
\text{TAG} &= 32 - 8 - 5 = 19\ \text{bits}\\[2pt]
\text{per line} &= 19 + 1 + 1 = 21\ \text{bits}\\[2pt]
\text{tag store} &= 256\times21 = \mathbf{5376\ \text{bits}} = \mathbf{672\ \text{B}}
\end{align*}
```

*(Tie every counted bit to its purpose: valid marks a line as holding real data after cold start; modified marks it dirty for write-back.)*

## Chapter 10: Virtual Memory

### 10.1 The idea (15-mark regular: 2022-23 8(b), 2023-24 8, 2024-25 10-adjacent)

Give every process the illusion of a large private memory. **Virtual (logical) addresses** — what the program generates — are translated per **page** (fixed block, e.g. 4 KB) to **physical frames** via the **page table**; pages not resident live on disk. "Virtual" because the address space exists as a mapping, not as physical storage (the direct 2022-23 sub-question "why is it called virtual?").

**Translation walk-through (draw + narrate):** VA = (page number p, offset d) → page table[p] → frame f (+ valid bit) → PA = (f, d). A **TLB** caches recent translations to avoid doubling memory accesses.

**Page fault (2023-24 7 marks of Q8):** valid bit = 0 → trap to OS → locate page on disk → choose a victim frame (replacement policy) → if victim dirty, write it back → load page, update tables, restart the instruction. 

**Replacement policies (needed for "how page replacement takes place"):** FIFO (simple; Belady's anomaly), **LRU** (approximates optimal by locality; hardware-assisted with reference bits), Optimal (theoretical benchmark). Also mention thrashing: too few frames → the system pages continuously.

**Virtual memory vs cache in one line:** same locality principle, different level — cache hides DRAM latency in hardware; VM hides disk latency under OS control.

### Unit-3 rapid recall

AMAT = h₁t₁ + (1−h₁)(h₂t₂ + (1−h₂)t₃) · SRAM 6T no refresh; DRAM 1T1C refresh, destructive read · address split: TAG | SET | OFFSET; sets = lines/ways · write-back needs dirty bit; write-through needs buffer · VA→PA via page table; fault → OS loads page; LRU beats FIFO by locality.

---

# UNIT 4 — CONTROL UNIT, PIPELINING, RISC & I/O

## Chapter 11: Control Unit Design

### 11.1 Hardwired vs microprogrammed (asked as 5 marks in BOTH 2022-23 and 2024-25 — a guaranteed question)

The control unit generates, every T-state, the set of control signals (register loads, ALU ops, bus grants) that execute the current step.

| | Hardwired | Microprogrammed |
|---|---|---|
| Implementation | combinational logic (decoders, sequencer, gates) | **control memory** holding microinstructions |
| Speed | fastest | slower (control-memory read each step) |
| Flexibility | rigid — change = redesign hardware | change = rewrite microcode |
| Complexity handling | explodes for rich ISAs | scales gracefully |
| Typical home | RISC cores | CISC (legacy x86 microcode) |
| Errors/cost | hard to debug | easy to patch, supports emulation |

**Microprogram vocabulary (for the 15-mark version):** microinstruction (one control word: control fields + next-address info), microroutine per machine instruction, control address register, sequencer; horizontal (wide, one bit per signal, parallel, fast) vs vertical (encoded, narrow, needs decoding) microinstructions.

## Chapter 12: Instruction Pipelining

### 12.1 The assembly-line idea

Split instruction processing into stages — classically **IF, ID, EX, MEM, WB** — and overlap different instructions in different stages. With k stages and n instructions: T = (k + n − 1)·τ vs n·k·τ unpiped → **speed-up → k** as n grows; throughput approaches one instruction per cycle. "One advantage of pipelining" (2023-24 Group A): increased instruction throughput.

```{=latex}
\begin{center}\small\begin{tabular}{l|ccccccc}
 & $t_1$ & $t_2$ & $t_3$ & $t_4$ & $t_5$ & $t_6$ & $t_7$\\\hline
$I_1$ & \cellcolor{accentlight}IF & \cellcolor{accentlight}ID & \cellcolor{accentlight}EX & \cellcolor{accentlight}MEM & \cellcolor{accentlight}WB & &\\
$I_2$ & & \cellcolor{mintbg}IF & \cellcolor{mintbg}ID & \cellcolor{mintbg}EX & \cellcolor{mintbg}MEM & \cellcolor{mintbg}WB &\\
$I_3$ & & & \cellcolor{boxamber}IF & \cellcolor{boxamber}ID & \cellcolor{boxamber}EX & \cellcolor{boxamber}MEM & \cellcolor{boxamber}WB\\
\end{tabular}\\[3pt]
{\scriptsize three instructions overlapping in a 5-stage pipeline — after fill-up, one completes every cycle}
\end{center}
```

**Derivation to memorize:** S = nk/(k + n − 1) → lim(n→∞) S = k. Efficiency = S/k; throughput = n/[(k+n−1)τ].

### 12.2 Hazards (the "drawbacks" half of every pipelining question)

- **Structural** — two stages need the same resource (one memory port): stall or duplicate.
- **Data** — instruction needs a result not yet written (RAW is the common one): forwarding/bypass paths, stalls, compiler scheduling.
- **Control** — branches invalidate fetched instructions: flush, delayed branch slots, branch prediction.

### 12.3 Instruction vs arithmetic pipeline (the 2023-24 15-marker, verbatim)

**Instruction pipeline:** stages = phases of the instruction cycle (IF…WB); every instruction flows through; goal = instruction throughput; hazards = data/control/structural.
**Arithmetic pipeline:** stages = phases of one arithmetic operation (e.g. floating-point add: compare exponents → align mantissas → add → normalize); streams of *operands* flow through; lives inside the ALU/FPU; hazards mostly absent (pure data streaming). Frame the answer as: what flows through, what the stages are, where each lives, one diagram each — then a 4-row contrast table.

## Chapter 13: RISC vs CISC

CISC — **Complex Instruction Set Computer** (the 2023-24 Group A full-form) — rich multi-cycle instructions, many addressing modes, memory-operand arithmetic, microprogrammed control, compact code (x86 heritage).
RISC — Reduced ISA: fixed-length instructions, **load/store architecture** (ALU ops touch registers only), few modes, large register file, hardwired control, 1 instruction/cycle target, heavy pipelining (ARM/RISC-V).
The comparison table + "why RISC pipelines better" (uniform length & simple decode) is the reliable 8-mark core; add that modern x86 decodes CISC into RISC-like micro-ops to show perspective.

## Chapter 14: Input/Output Organization

### 14.1 The three I/O strategies (build the answer as an escalation)

1. **Programmed I/O (polling):** CPU loops reading the device's status flag — simple, but burns CPU cycles proportional to device slowness.
2. **Interrupt-driven I/O:** device raises an interrupt when ready; CPU works meanwhile, then runs the ISR (save state → identify source → service → restore). Good for keyboards; still CPU-copied data.
3. **DMA (Direct Memory Access):** a DMA controller moves blocks **between I/O and main memory directly**, stealing bus cycles; the CPU sets up (address, count, direction), then is interrupted once at completion.

**2024-25 Group A pair:** DMA transfers data between main memory and I/O device — option **(i) only**; and "CPU always sits idle during DMA" → **False** (cycle stealing interleaves; the CPU keeps executing from cache/other cycles).
**2023-24 Group B: "explain the DMA controller" (5):** registers (address, word count, control), bus request/grant (HRQ/HLDA) handshake, cycle-stealing vs burst modes, one-interrupt-per-block completion.

### 14.2 Handshaking (2023-24 Group B, 5 marks)

Asynchronous transfer needs agreement without a shared clock: source asserts **DATA VALID**; destination latches and answers **DATA ACCEPTED**; source drops valid; destination drops accepted — a two-wire, four-phase exchange that self-paces to the slower party (draw the two-signal timing diagram both directions: source-initiated and destination-initiated).

### 14.3 Bus arbitration: daisy chain vs polling (the full 2024-25 Group C 7, 15 marks — worked)

**(a) Bus arbitration [2]:** deciding which of several requesting masters gets the shared bus next.
**(b) Daisy chaining [5]:** one common bus-request line; the grant signal threads device 1 → 2 → 3…; the first requesting device absorbs the grant (blocks propagation) and uses the bus. Draw: arbiter → BG into device chain, common BR and BUSY lines.
**(c) Disadvantages [2]:** fixed priority by position (starvation of far devices); a failed device breaks the chain; grant propagation delay.
**(d) Polling fix [6]:** arbiter broadcasts addresses on **poll-count lines**; each device compares; the requesting device whose address matches takes the bus. Priority becomes programmable (rotate the starting count), a dead device is skipped, no chain to break. With **8 poll lines → 2⁸ = 256 distinct grant responses/devices** (the 2024-25 Group A numerical). Cost: more lines and a sequencing controller.
*(Complete the family with independent-request arbitration — per-device BR/BG pairs, fastest, most lines — one line for perspective.)*

**Bidirectional bus (2023-24 Group A): the data bus** (address bus is one-way CPU→memory; control lines are individually one-way).

### Unit-4 rapid recall

Hardwired fast/rigid; microprogrammed flexible/slower · pipeline S → k; hazards structural/data/control · instruction pipe = stages of the cycle; arithmetic pipe = stages of an FP op · RISC = load/store, fixed length, hardwired · PIO → interrupt → DMA escalation · DMA: mem↔I/O, cycle stealing, CPU not idle · daisy chain = positional priority, chain fragility; polling = $2^{k}$ codes, programmable · handshake = valid/accepted four-phase.

---

# APPENDIX — CO FORMULA & FACT SHEET

Immediate width = word − opcode − register fields · max unsigned = 2^bits − 1 · IEEE 754: 1/8/23 (bias 127), 1/11/52 (bias 1023) · CLA: Cᵢ₊₁ = Gᵢ + PᵢCᵢ, two-level after unrolling · Booth: 01 → +M, 10 → −M, shift ASR; signed-safe · Restoring: sub, test, restore; non-restoring: alternate add/sub · AMAT = h₁t₁ + (1−h₁)(h₂t₂ + (1−h₂)t₃) · Cache fields: TAG | SET | OFFSET; sets = lines/ways; tag store = lines × (tag + status bits) · Pipeline: S = nk/(k+n−1) → k · Poll lines k → $2^{k}$ devices · V-flag = Cₙ ⊕ Cₙ₋₁ · PC holds next-instruction address.

*— End of the Computer Organization Concept Book —*


---

# 📺 VIDEO COMPANION — topic-wise (from your chosen playlists)

> Not covered by this playlist: Booth's algorithm, IEEE 754/number representation, restoring/non-restoring division, virtual memory — study these from the book chapters (they are fully derived there).


### Unit1: Stored program, instruction cycle
- [L-1.2: Von Neumann's Architecture | Stored Memory Concept in Computer Architecture](https://www.youtube.com/watch?v=j8NnE1YeSN0) (9:40)
- [L-2.3: Immediate Addressing Mode | Computer Organisation and Architecture](https://www.youtube.com/watch?v=mtr7oumkwuk) (6:35)
- [L-2.6: Auto Increment and Decrement Addressing Modes | Computer Organisation and Architecture](https://www.youtube.com/watch?v=7RP8SLdW0S0) (6:51)
- [L-4.3: Pipelining Vs Non-Pipelining | Instruction Execution | Speedup, Efficiency, Utilization | COA](https://www.youtube.com/watch?v=R9s34-lnd9k) (13:03)
- [Interrupts in 8085 microprocessor | Types of Interrupts in Computer Organization](https://www.youtube.com/watch?v=1aG3aFEKxyA) (9:36)

### Unit1: Instruction formats & addressing modes
- [L-1.11: Shift Instructions(Data Manipulation) in Computer Organisation and Architecture](https://www.youtube.com/watch?v=i2UKe6lgrqg) (13:27)
- [L-1.13: What is Instruction Format | Understand Computer Organisation with Simple Story](https://www.youtube.com/watch?v=WAO_W6Hpzyk) (10:40)
- [L-1.14: Question on Instruction Format | Computer Organization | UGC NTA NET June 2021](https://www.youtube.com/watch?v=GZz9nz7Vgb0) (8:51)
- [L-1.15: Single Accumulator CPU Organisation | Single Address Instructions in Computer Organisation](https://www.youtube.com/watch?v=k5YMLXPy1SE) (8:02)
- [L-1.16: General Register CPU Organisation | Two and Three Address Instructions | COA](https://www.youtube.com/watch?v=Za7ozdjE8VI) (7:18)
- [L-1.17: Register Stack Organisation | Zero Address Instructions | COA](https://www.youtube.com/watch?v=u-sp4gBAJKI) (11:50)

### Unit2: Adders (ripple/CLA) & ALU
- [L-1.1: Computer Organization and Architecture Syllabus Discussion for GATE and UGC NTA NET](https://www.youtube.com/watch?v=L9X7XXfHYdU) (13:40)
- [L-1.2: Von Neumann's Architecture | Stored Memory Concept in Computer Architecture](https://www.youtube.com/watch?v=j8NnE1YeSN0) (9:40)
- [L-1.9: Arithmetic Instructions(Data Manipulation) in Computer Organisation and Architecture](https://www.youtube.com/watch?v=M0znE3jqaxs) (8:44)
- [L-1.13: What is Instruction Format | Understand Computer Organisation with Simple Story](https://www.youtube.com/watch?v=WAO_W6Hpzyk) (10:40)
- [L-4.7: Structural Hazards in Pipelining | Types of Hazards with Example in Hindi](https://www.youtube.com/watch?v=qn7zf_OSLsk) (9:33)

### Unit3: Memory hierarchy & organization
- [L-1.1: Computer Organization and Architecture Syllabus Discussion for GATE and UGC NTA NET](https://www.youtube.com/watch?v=L9X7XXfHYdU) (13:40)
- [L-1.2: Von Neumann's Architecture | Stored Memory Concept in Computer Architecture](https://www.youtube.com/watch?v=j8NnE1YeSN0) (9:40)
- [L-1.3:Various General Purpose Registers in Computer Organization and Architecture](https://www.youtube.com/watch?v=2mowjC3dCqk) (15:10)
- [L-1.7: Types of Instructions in General Purpose Computer | Computer Organization and Architecture](https://www.youtube.com/watch?v=r6PChksvxp8) (5:11)
- [L-1.12: Program Control Instructions(Types of Control Instructions) | Computer Organization](https://www.youtube.com/watch?v=OXz7wKHr0_I) (10:51)
- [L-1.18:Memory Stack Organisation | Memory stack Vs Register stack  | COA](https://www.youtube.com/watch?v=C1H5gurIcJk) (6:03)

### Unit3: Cache memory & mapping
- [L-3.1: Memory Hierarchy in Computer Architecture | Access time, Speed, Size, Cost | All Imp Points](https://www.youtube.com/watch?v=zwovvWfkuSg) (7:32)
- [L-3.4: GATE 2004 Question on 3-Level Memory Organisation || Computer Organisation and Architecture](https://www.youtube.com/watch?v=_VNY-nhkMhw) (5:50)
- [L-3.5: What is Cache Mapping || Cache Mapping techniques || Computer Organisation and Architecture](https://www.youtube.com/watch?v=m1dA7D6c3C0) (7:40)
- [L-3.6: Direct Mapping with Example in Hindi | Cache Mapping | Computer Organisation and Architecture](https://www.youtube.com/watch?v=eObN3u3eAnU) (22:03)
- [L-3.7: GATE 2005 Question on Direct Mapping | Cache Mapping Questions | Computer Organization](https://www.youtube.com/watch?v=jZ2jRBVhgSY) (7:22)
- [L-3.8: Fully Associative Mapping with examples in Hindi | Cache Mapping | Computer Organisation](https://www.youtube.com/watch?v=sLCJJdz0WAg) (9:55)

### Unit4: Control unit design
- [L-1.1: Computer Organization and Architecture Syllabus Discussion for GATE and UGC NTA NET](https://www.youtube.com/watch?v=L9X7XXfHYdU) (13:40)
- [L-1.2: Von Neumann's Architecture | Stored Memory Concept in Computer Architecture](https://www.youtube.com/watch?v=j8NnE1YeSN0) (9:40)
- [L-2.8: Indirect Addressing Mode | Computer Organisation and Architecture](https://www.youtube.com/watch?v=l7QV6FBTGdE) (6:05)
- [L-2.13: RISC vs CISC | Computer Organization & Architecture](https://www.youtube.com/watch?v=ZW1gb3h-f9k) (8:21)

### Unit4: Pipelining
- [L-1.1: Computer Organization and Architecture Syllabus Discussion for GATE and UGC NTA NET](https://www.youtube.com/watch?v=L9X7XXfHYdU) (13:40)
- [L-4.1: Pipelining with real life example| Need of Pipelining | COA](https://www.youtube.com/watch?v=Al95Owan9Ck) (8:17)
- [L-4.2: Pipelining Introduction and structure | Computer Organisation](https://www.youtube.com/watch?v=nv0yAm5gc-E) (3:53)
- [L-4.3: Pipelining Vs Non-Pipelining | Instruction Execution | Speedup, Efficiency, Utilization | COA](https://www.youtube.com/watch?v=R9s34-lnd9k) (13:03)
- [L-4.4: Stage Delay in Pipeline | Previous Year GATE Question | Computer Organisation & Architecture](https://www.youtube.com/watch?v=-YtmPoGCdfM) (10:53)
- [L-4.5: Numerical Question on Pipelining | Previous year GATE Question | COA](https://www.youtube.com/watch?v=BlnI-eZSt4M) (4:25)

### Unit4: RISC vs CISC
- [L-2.13: RISC vs CISC | Computer Organization & Architecture](https://www.youtube.com/watch?v=ZW1gb3h-f9k) (8:21)

### Unit4: I/O, interrupts, DMA
- [L-1.1: Computer Organization and Architecture Syllabus Discussion for GATE and UGC NTA NET](https://www.youtube.com/watch?v=L9X7XXfHYdU) (13:40)
- [L-1.8: Data Transfer Instructions in Computer Organisation and Architecture](https://www.youtube.com/watch?v=bNkiChXPRhM) (7:45)
- [L-1.10: Logical Instructions(Data Manipulation) in Computer Organisation and Architecture](https://www.youtube.com/watch?v=_YJU5WFT9qw) (9:12)
- [L-2.8: Indirect Addressing Mode | Computer Organisation and Architecture](https://www.youtube.com/watch?v=l7QV6FBTGdE) (6:05)
- [I/O Interface in Computer Organization](https://www.youtube.com/watch?v=PM728r4oGcE) (5:45)
- [Interrupts in 8085 microprocessor | Types of Interrupts in Computer Organization](https://www.youtube.com/watch?v=1aG3aFEKxyA) (9:36)
