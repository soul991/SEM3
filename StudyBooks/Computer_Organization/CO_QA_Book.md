# COMPUTER ORGANIZATION — The Question-Answer Book
### MAKAUT PCC-CS302 · Every real PYQ of 2022-23, 2023-24, 2024-25 solved · sequenced to teach the subject front-to-back

> Group A (definitions/one-liners) → Group B (mechanisms, 5 marks) → Group C (design/derivation, 15 marks) inside each unit. Every answer ends with a **Concept bridge**. Tags: [22] [23] [24] = real paper session (2022-23 etc.); [TB] textbook-fill; [P-26] pattern-based prediction.

---

# UNIT 1 — BASIC ORGANIZATION: QUESTIONS

## A. One-markers

**Q1. [22][24] What is a program counter? / Where is the address of the next instruction stored?**
**Answer:** The PC — the register **holding the address of the next instruction to execute**; incremented each fetch, overwritten by branches.
*Bridge:* The PC is the thread the stored-program machine hangs on: fetching = "read M[PC], PC←PC+1."

**Q2. [22] A self-contained sequence of instructions performing a task is called —**
**Answer: a routine (subroutine/procedure).**

**Q3. [23] Which program acts as intermediary between user and hardware? — The operating system.**

**Q4. [24] The OS is categorized as which type of software? — System software.**

**Q5. [23] What is an interpreter? — A translator that converts and executes source code line-by-line, without producing a stored object program** (compiler = whole-unit translation first).
*Bridge for 3-5:* Software stack layers: hardware ← OS ← translators ← applications; MAKAUT mines this boundary for Group A yearly.

**Q6. [22] The addressing mode of ADD X, Y is — direct (absolute) addressing** — the instruction carries the operands' memory addresses themselves.

**Q7. [22] 16 registers of 32 bits on a MUX bus — selection inputs per MUX? — 4** (2⁴ = 16 sources; 32 MUXes share the selects).

**Q8. [22] M[AR] ← R3 specifies which memory operation? — A memory write** (store R3 at address AR).

**Q9. [22] Parameters influencing a microprocessor's characteristics — word length, clock frequency, instruction set/addressing modes, register/cache complement, bus widths.**

**Q10. [23] Which bus is bidirectional? — the data bus.**

**Q11. [24] During processor–memory transfer we use — the memory buffer/data register (MDR/MBR)** (with MAR supplying the address).

## B. Five-markers

**Q12. [22] Explain Flynn's classification with examples.**
**Answer.** Classify by number of simultaneous Instruction and Data streams: **SISD** — one instruction, one data stream (a classic uniprocessor). **SIMD** — one instruction applied to many data lanes (vector units, GPUs). **MISD** — many instructions on one data stream (rare; fault-tolerant/pipelined signal chains cited). **MIMD** — many independent instruction+data streams (multicore, clusters). Draw the 2×2 grid; one example each; note modern CPUs mix SIMD units inside MIMD systems.
*Bridge:* The taxonomy is about *streams*, not processor counts — say "stream" in every definition.

**Q13. [23] What is the Von Neumann bottleneck?**
**Answer.** In the stored-program organization, instructions **and** data share one memory and one CPU–memory path; total performance is capped by that channel's bandwidth, not by CPU speed — the processor idles waiting for words. Aggravated by the CPU-DRAM speed gap. Remedies: cache hierarchies, split I/D (Harvard) caches, prefetch, wider/multiple buses.
*Bridge:* This question is the *cost* of the stored-program idea whose *benefit* (flexibility) defines the machine — pair them in your head.

**Q14. [24] Define instruction cycle, machine cycle and T-state.**
**Answer.** T-state: one clock period — the atomic control step. Machine cycle: one complete memory or I/O access (opcode fetch, memory read/write), several T-states. Instruction cycle: full fetch-decode-execute of one instruction = one or more machine cycles (e.g. a memory-operand ADD = fetch + read + execute cycles). Diagram the nesting.
*Bridge:* Three clocks nested like gears — signal-level, access-level, instruction-level.

## C. Fifteen-markers

**Q15. [22 Q9, 15 marks; repeated 24 Q8(c) for 6] Explain 0-, 1-, 2-, 3-address instruction formats with examples.**
**Answer.** Use one running computation, X = (A+B)·(C+D), and write all four programs (3-addr: 3 lines; 2-addr: 6; 1-addr accumulator: 7 with a temporary; 0-addr stack: postfix ABCD+·... i.e. PUSH A, PUSH B, ADD, PUSH C, PUSH D, ADD, MUL, POP X). Then the trade-off paragraph: instruction width vs program length vs hardware (stack machines need no operand fields but serialize through the stack; accumulator machines bottleneck on AC; 3-address needs wide instructions but fewest of them). Close: real ISAs are hybrids (x86 two-address, RISC three-register).
*Bridge:* One worked expression in all four styles *is* the complete answer — memorize the programs, not prose.

**Q16. [24 Q8, 15 marks] (a) Functional diagram of a computer, each block explained [6]; (b) signed vs unsigned numbers [1]; (c) the four address formats [6]; (d) (1101101110)₂ → hex [1]; (e) 16-bit representation of −6 [1].**
**Answer.** (a) Input, Memory, ALU, Control (CU+ALU = CPU), Output; describe the instruction path (memory→CU) and data paths; control signals radiate from CU to all blocks. (b) Unsigned: all bits are magnitude (0…2ⁿ−1); signed: MSB carries sign (2's complement −2ⁿ⁻¹…2ⁿ⁻¹−1). (c) As Q15. (d) Group from right: 11 0110 1110 → **36E₁₆**. (e) +6 = 0000000000000110 → invert+1 → **1111111111111010**.

---

# UNIT 2 — ARITHMETIC: QUESTIONS

## A. One-markers

**Q17. [23] The 2's complement of 15 is — 10001₂ in 5 bits (11110001 in 8 bits — state your width).**

**Q18. [24] The maximum n-bit 2's complement number is — 2ⁿ⁻¹ − 1** (asymmetric range; minimum is −2ⁿ⁻¹).

**Q19. [24] (−7) − (+1) in 2's complement — −8 = 1000₂ (4-bit)** — the most negative value, no overflow since −8 is representable.

**Q20. [22] (2FA0C)₁₆ in binary — 0010 1111 1010 0000 1100.**

**Q21. [22] XOR of (4AC0)₁₆ and (B53F)₁₆ — FFFF₁₆** (they are bitwise complements).

**Q22. [22] Boolean: AB + AB' = A** (factor B + B' = 1).

**Q23. [23] Carry and Overflow are also called — status (condition-code) flags.**

**Q24. [22] Floating point stores what type of values? — Real numbers (very large/small, fractional) with sign, exponent, mantissa.**

**Q25. [22] Is Excess-3 a weighted code? — No** (non-weighted, self-complementing).

**Q26. [23] Which algorithms are add/subtract-and-shift based? — Booth's multiplication and restoring/non-restoring division.**

**Q27. [24] Booth's algorithm uses which signed representation? — 2's complement.**

**Q28. [22] A 10-bit counter at 1001100111: how many FFs complement on the next count? — 4** (…0111 + 1 toggles the three trailing 1s and the first 0).

## B. Five-markers

**Q29. [22][23 — asked twice] Describe the IEEE 754 floating-point standard.**
**Answer.** 32-bit single: sign 1 | exponent 8 (bias 127) | fraction 23, value $(-1)^s \cdot 1.F \cdot 2^{E-127}$; 64-bit double: 1|11|52, bias 1023. Normalized hidden 1; E all-0 → zero/denormals, all-1 → ±∞ / NaN. Worked example: −13.25 → 1 10000010 10101000...0. Why bias: makes exponent comparison unsigned-order.
*Bridge:* Sign-magnitude mantissa + biased exponent = lexicographically comparable floats — that design choice explains every field.

**Q30. [22] Describe sign extension.**
**Answer.** Widening a signed number preserves value by **replicating the sign bit**: 4-bit 0101(+5) → 00000101; 1011(−5) → 11111011. Proof sketch for 2's complement: the value −2ⁿ⁻¹bₙ₋₁ + Σ...; replicating the MSB adds bits whose weights telescope to the original sign term. Needed whenever narrow immediates/registers meet wider ALUs.

**Q31. [22] 32-bit instructions, 64 registers, 45 opcodes, one immediate + two register operands — max unsigned immediate?**
**Solution.** Budget the 32-bit word field by field:

```{=latex}
\begin{align*}
\text{opcode} &= \lceil\log_2 45\rceil = 6\ \text{bits}\\
\text{registers} &= 2\times\log_2 64 = 12\ \text{bits}\\
\text{immediate} &= 32 - 6 - 12 = 14\ \text{bits}
\end{align*}
```

$$\therefore\ \text{max unsigned immediate} = 2^{14}-1 = \mathbf{16383}$$

*Bridge:* field-budget questions are always word-width arithmetic; draw the partition diagram first.

**Q32. [24] Design a 4-bit adder–subtractor composite unit.**
**Answer.** Four FAs rippled; each Bᵢ enters through XOR with mode M; C₀ = M. M=0 → A+B; M=1 → A+B̄+1 = A−B. Show V = C₄⊕C₃ for signed overflow. Diagram + one worked case each mode.

**Q33. [24] Draw the flowchart of the restoring division algorithm.**
**Answer.** Boxes: init A=0, load Q, M, count=n → shift A:Q left → A←A−M → test sign(A): ≥0 → Q₀=1; <0 → Q₀=0, A←A+M (restore) → count−− → loop until 0 → Q=quotient, A=remainder. State the 7÷3 result as verification (Q=0010, A=0001).

## C. Fifteen-markers

**Q34. [23 Q7, 7+8] Advantages of carry look-ahead over ripple carry; explain with diagram.**
**Answer.** Ripple: Cᵢ₊₁ depends on Cᵢ → delay ∝ n. CLA: define Gᵢ=AᵢBᵢ, Pᵢ=Aᵢ⊕Bᵢ; unroll Cᵢ₊₁ = Gᵢ + PᵢCᵢ into two-level expressions (write C₁…C₄ fully). All carries in ~2 gate delays; sums Sᵢ = Pᵢ⊕Cᵢ arrive in constant time. Advantages: delay O(1) per block vs O(n); deterministic timing. Costs: gate count/fan-in; hierarchical group-CLA for wide words. Diagrams: 4-FA ripple chain vs CLA block (G/P generators → carry logic → sum XORs).

**Q35. [22 Q7, 15] (a) 4-bit ripple-carry adder from full adders [5]; (b) 0.011010₂ → decimal [5]; (c) 0.6875₁₀ → binary [5].**
**Answer.** (a) Diagram, C₀ in, C₄ out; delay argument. (b) 1/4+1/8+1/32 = **0.40625**. (c) ×2 chain: 0.6875→1(.375)→0(.75)→1(.5)→1(.0) = **0.1011₂**.

**Q36. [24 Q9, 5+6+4] (a) Booth flowchart; (b) −9 × +6 in 5 bits; (c) 4-bit CLA operation.**
**Answer.** (a) Flowchart: examine Q₀Q₋₁ → 01: A+M / 10: A−M / else skip → ASR(A,Q,Q₋₁) → count. (b) The full 5-step table (Concept Book Ch. 5) → product 1111001010 = **−54**. (c) As Q34 compressed: G/P definitions, unrolled C₁-C₄, constant-depth claim.

**Q37. [22 Q10, 9+6] (a) Fixed-point signed number systems; (b) 4-bit table of sign-magnitude / 1's / 2's complement.**
**Answer.** (a) Radix-point fixed; three encodings of sign; ranges (±(2ⁿ⁻¹−1), ±(2ⁿ⁻¹−1), −2ⁿ⁻¹…2ⁿ⁻¹−1); double-zero problem in the first two; arithmetic simplicity argument for 2's. (b) Tabulate all 16 patterns × three columns (the ±0 rows and the extra −8 are what the examiner checks).

---

# UNIT 3 — MEMORY: QUESTIONS

## A. One-markers

**Q38. [23] Fastest memory in the hierarchy — registers** (then cache → main → auxiliary).

**Q39. [23] Categories of memory/storage — primary (RAM/ROM), secondary/auxiliary, cache, registers.**

**Q40. [23] Auxiliary memory devices — magnetic disk, magnetic tape, SSD, optical disc.**

**Q41. [24] Principle of locality justifies — cache memory.**

**Q42. [24] Locations in a 2K RAM chip — 2048.**

**Q43. [24] Decoder to build 32K×16 from 8K-chip rows — 2×4 decoder** (32K/8K = 4 row-groups; 2 high address bits select).

## B. Five-markers

**Q44. [23] Explain SRAM read and write operations.**
**Answer.** 6T cell: cross-coupled inverters + two access transistors on word line, complementary bit lines. Read: precharge lines, assert word line, cell tips the differential, sense amp resolves — non-destructive. Write: drive lines to forced complementary levels, assert word line, overpower the latch. No refresh; static while powered. (Add the DRAM contrast line for the fifth mark.)

**Q45. [24] Three-level memory: cache 15 ns (h=0.96), main 25 ns (h=0.9), disk 40 ns. Find AMAT.**
**Solution.** State the hierarchical-miss model, then substitute:

```{=latex}
\begin{align*}
\text{AMAT} &= h_1t_1 + (1-h_1)\big[h_2t_2 + (1-h_2)t_3\big]\\
 &= 0.96\times15 + 0.04\,(0.9\times25 + 0.1\times40)\\
 &= 14.4 + 1.06 = \mathbf{15.46\ \text{ns}}
\end{align*}
```


## C. Fifteen-markers

**Q46. [22 Q8, 7+8] (a) 4-way set-associative, 128 lines, 64-word lines, 20-bit addresses → TAG/SET/WORD = 9/5/6 (worked in Concept Ch. 9). (b) Explain virtual memory with example.**

**Q47. [23 Q8, 8+7] Virtual memory concept; page fault** — mapping walk-through, VA=(p,d)→PA=(f,d), TLB; fault sequence: trap → fetch from disk → victim (dirty? write back) → restart. Example with 4 KB pages and a 2-frame toy trace.

**Q48. [22 Q11(a), 7] 8 KB direct-mapped write-back cache, 32 B blocks, 32-bit addresses, tag store size — 256 × (19+1+1) = 5376 bits = 672 B** (full field arithmetic in Concept Ch. 9).

**Q49. [23 Q11, 8+7] Fully associative vs direct mapping; write-through vs write-back.**
**Answer.** Mapping table (placement freedom, comparators, thrashing, cost) + policy contrast (traffic vs staleness, buffer vs dirty bit); close with why set-associative is the engineering compromise.

**Q50. [22 Q9, 15] Static vs dynamic MOS cell diagrams; memory read/write process; daisy chaining; DMA transfer [2+7+2+4]** — 6T latch vs 1T1C charge cell + refresh; then the arbitration and DMA components from Unit 4 (cross-unit composite — MAKAUT does this; answer from both chapters).

---

# UNIT 4 — CONTROL, PIPELINE, RISC, I/O: QUESTIONS

## A. One-markers

**Q51. [23] One advantage of pipelining — higher instruction throughput (≈1 instruction/cycle).**

**Q52. [23] Full form of CISC — Complex Instruction Set Computer.**

**Q53. [24] DMA transfers data between — main memory and I/O device (option i only).**

**Q54. [24] "CPU always sits idle during DMA" — False** (cycle stealing; CPU continues, briefly yielding bus slots).

**Q55. [24] Polling with 8 lines — 2⁸ = 256 distinct grant responses.**

## B. Five-markers

**Q56. [22][24 — twice] Differences between hardwired and microprogrammed control.**
**Answer.** The six-row table (implementation, speed, flexibility, ISA complexity, debugging, typical use) + one-line definitions of microinstruction/control memory. Two real appearances make this the single safest Group B preparation in CO.

**Q57. [23] Explain the DMA controller.**
**Answer.** Registers (address, word-count, control/status), HRQ/HLDA bus handshake, modes (burst vs cycle-steal), sequence: CPU programs DMAC → device ready → DMAC takes bus → transfers block memory↔device → interrupt on completion. Diagram with CPU, DMAC, memory, device on the bus.

**Q58. [23] Explain handshaking in I/O.**
**Answer.** Two-signal four-phase asynchronous protocol (DATA VALID / DATA ACCEPTED), both initiation directions, timing diagram, why: no common clock, speed mismatch tolerance, positive confirmation.

## C. Fifteen-markers

**Q59. [23 Q9, 15] Instruction pipeline vs arithmetic pipeline** — what flows (instructions vs operands), stage anatomy (IF-ID-EX-MEM-WB vs FP-add stages), location, hazards, speed-up S = nk/(k+n−1) → k; two diagrams + contrast table.

**Q60. [23 Q10, 15] What is an OS? Roles?** — definition (resource manager + interface), then paragraphs: process management/scheduling, memory management (paging → ties to VM), file systems, device/I-O management, protection & security, user interface; one example per role.

**Q61. [24 Q7, 2+5+2+6] Bus arbitration; daisy chaining + diagram; its disadvantages; polling as the fix** — fully worked in Concept Ch. 14: positional priority & chain fragility vs programmable $2^{k}$ poll codes.

**Q62. [P-26 banker] (a) RISC vs CISC full comparison with why-RISC-pipelines-better [8]; (b) interrupt-driven I/O vs programmed I/O with ISR sequence [7].** — The one high-frequency Unit-4 pairing the last three papers haven't yet asked as a 15 whole; pattern says due.

---

# THE 3-YEAR PATTERN MAP (CO)

| Topic | 22-23 | 23-24 | 24-25 | 2026 verdict |
|---|---|---|---|---|
| IEEE 754 | B | B | — | **Due — near-certain** |
| Hardwired vs microprogrammed | B | — | B | **Certain-class** |
| Address formats (0/1/2/3) | C(15) | — | C(6) | **Near-certain** |
| Virtual memory / page fault | C | C | — | **Due — certain-class** |
| Cache mapping + numericals | C×2 | C | (C 10(a)) | **Certain** |
| Booth's (flowchart/worked) | — | A | C(11) | Likely |
| CLA vs ripple | C(a) | C(15) | C(4) | **Certain** |
| DMA / arbitration | (Q9d) | B | A×2 + C(15) | **Certain** |
| Pipelining | — | A + C(15) | — | Due |
| AMAT numerical | — | — | B | Likely repeat |

*— End of the Computer Organization Question-Answer Book: 62 questions solved; every real CO question of three cycles included. —*
