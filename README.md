# Banker's Algorithm Simulator (Deadlock Avoidance)

**PT 101 - Platform Technologies | Final Project | Topic 5**
Batangas State University, College of Informatics and Computing Sciences, Alangilan Campus
1st Semester AY 2026-2027

A Python console program that simulates the **Banker's Safety Algorithm** and the **Resource-Request Algorithm**. Every computation is shown step by step: Need, Available, each Work comparison and update, the Finish flags, and the safe sequence (or UNSAFE STATE). For requests it shows Request <= Need, Request <= Available, the tentative state, the safety result and the GRANT / WAIT decision.

All results are computed by the program from the inputs. Nothing is hard-coded.

---

## Project information

| Item | Details |
|---|---|
| Course | PT 101 - Platform Technologies |
| Project | Final Project, Topic 5: Banker's Algorithm Simulator (Deadlock Avoidance) |
| Group | Group 8 |
| School / College | Batangas State University, College of Informatics and Computing Sciences, Alangilan Campus |
| Term | 1st Semester, AY 2026-2027 |
| Repository | https://github.com/Ranzel-pixel/GROUP-8_DEADLOCK-AVOIDANCE |
| Program file | [`BANKERS_ALGO-GROUP-8.py`](BANKERS_ALGO-GROUP-8.py) |
| Language | Python 3.8+ (standard library only) |

---

## Contents

- [Features](#features)
- [Deliverables checklist](#deliverables-checklist)
- [Group members](#group-members)
- [Repository structure](#repository-structure)
- [1. Requirements](#1-requirements)
- [2. How to run](#2-how-to-run)
- [3. Inputs](#3-inputs)
- [4. Reading the output](#4-reading-the-output)
- [5. The algorithms](#5-the-algorithms)
- [6. Testing](#6-testing)
- [7. Code structure](#7-code-structure)
- [8. Presentation and demo](#8-presentation-and-demo)
- [9. Troubleshooting](#9-troubleshooting)
- [10. Assumptions and limitations](#10-assumptions-and-limitations)
- [11. References](#11-references)
- [12. Assistance disclosure](#12-assistance-disclosure)

---

## Features

- Safety Algorithm with a full step-by-step trace (every pass, every comparison, every Work update).
- Resource-Request Algorithm with its checks (Request <= Need, Request <= Available, tentative state safe) and a final GRANT / WAIT / ERROR decision.
- Computes Need and Available from your inputs. You never type them.
- Three ready-made sample data sets, or enter your own system (1 to 20 processes, 1 to 10 resource types).
- Input validation: bad input shows a message and asks again instead of crashing.
- The algorithm code is separate from input and output, so it is covered by automated tests.
- No external libraries. Runs on Windows, macOS and Linux.

---

## Deliverables checklist

| # | Deliverable (from the project guidelines) | Where to find it | Status |
|---|---|---|---|
| 1 | Complete, organized source code (GitHub repository) | [`BANKERS_ALGO-GROUP-8.py`](BANKERS_ALGO-GROUP-8.py), [`test_banker.py`](test_banker.py), this repository | Done |
| 2 | User guide: execution, inputs, output interpretation | This README, sections [2](#2-how-to-run), [3](#3-inputs) and [4](#4-reading-the-output) | Done |
| 3 | Testing evidence: at least 3 test cases, expected vs actual | [`docs/TEST_CASES.md`](docs/TEST_CASES.md) (8 cases) and [`test_evidence/`](test_evidence/) | Done |
| 4 | Contribution record in the instructor's Google Spreadsheet | Fill in the table in [`docs/CONTRIBUTIONS.md`](docs/CONTRIBUTIONS.md), then copy it into the instructor's sheet | **Group to fill in** |
| 5 | Demo / presentation materials | [`docs/DEMO_SCRIPT.md`](docs/DEMO_SCRIPT.md) is ready. Slides: **group to add** to `docs/presentation/` | Script done, slides pending |

---

## Group members

| Name | Role | Main tasks |
|---|---|---|
| HIDALGO, PERSHEY RANZEL JAMINA | Leader | *(fill in: what this member did)* |
| BATHAN, EMMANUEL | Member | *(fill in)* |
| ABANTE, SER JAMES | Member | *(fill in)* |
| GUIZZAGAN, CHRISTIAN | Member | *(fill in)* |

Full task record: [`docs/CONTRIBUTIONS.md`](docs/CONTRIBUTIONS.md)

---

## Repository structure

```
GROUP-8_DEADLOCK-AVOIDANCE/
├── BANKERS_ALGO-GROUP-8.py    # the program (run this)
├── test_banker.py             # automated test cases
├── README.md                  # user guide (this file)
├── .gitignore
├── docs/
│   ├── TEST_CASES.md          # test cases: expected vs actual results
│   ├── CONTRIBUTIONS.md       # contribution record
│   └── DEMO_SCRIPT.md         # demo flow and oral defense review
└── test_evidence/             # saved program output for every test case
    ├── TC1_safe_state.txt
    ├── TC2_unsafe_state.txt
    ├── TC3_to_TC6_requests.txt
    ├── TC7_four_resource_types.txt
    ├── TC8_invalid_inputs.txt
    └── automated_tests_output.txt
```

Slides (`docs/presentation/`) will be added by the group when they are ready.

---

## 1. Requirements

- Python **3.8 or newer**. No extra libraries needed.
- Works on Windows, macOS and Linux.

Check your version:

```
python --version
```

## 2. How to run

1. Download this repository: click **Code > Download ZIP** on GitHub and unzip it, or clone it:
   ```
   git clone https://github.com/Ranzel-pixel/GROUP-8_DEADLOCK-AVOIDANCE.git
   ```
2. Open a terminal in the project folder (Windows: open the folder, type `cmd` in the address bar, press Enter).
3. Start the program:
   ```
   python BANKERS_ALGO-GROUP-8.py
   ```
   If `python` is not found, try `py BANKERS_ALGO-GROUP-8.py` (Windows) or `python3 BANKERS_ALGO-GROUP-8.py` (macOS/Linux).
4. Choose options from the menu by typing the number and pressing Enter. After each option the program waits for Enter before showing the menu again.

To run the automated tests:

```
python test_banker.py
```

The last lines should be `Ran 16 tests` and `OK`.

The main menu looks like this:

```
================================================================
 BANKER'S ALGORITHM SIMULATOR  (Deadlock Avoidance)
================================================================
 Current data: (none loaded yet)

 1. Enter new system state
 2. Load sample data set
 3. Show system state (Total, Allocation, Max, Need, Available)
 4. Run Safety Algorithm
 5. Resource Request (GRANT / WAIT)
 6. Exit

Select an option:
```

| Option | What it does |
|---|---|
| 1. Enter new system state | Type your own processes, Total, Allocation and Max |
| 2. Load sample data set | Load one of 3 ready-made inputs |
| 3. Show system state | Show Total, Allocation, Max, Need and Available |
| 4. Run Safety Algorithm | Step-by-step trace and the SAFE / UNSAFE result |
| 5. Resource Request | Check a request and decide GRANT / WAIT / ERROR |
| 6. Exit | Close the program |

Options 3 to 5 need data first. If you choose them before loading data, the program tells you to use option 1 or 2 first.

---

## 3. Inputs

### Option 1: Enter new system state

The program asks for these, in order:

| Prompt | What to type | Example |
|---|---|---|
| Number of processes (1-20) | a whole number from 1 to 20 | `5` |
| Number of resource types (1-10) | a whole number from 1 to 10 | `3` |
| Total vector | total instances of each resource type | `10 5 7` |
| Allocation matrix | one row per process (what it holds now) | `P0: 0 1 0` |
| Max matrix | one row per process (the most it may ever need) | `P0: 7 5 3` |

- Separate numbers with **spaces or commas** (`10 5 7` or `10,5,7`).
- Processes are named **P0, P1, P2 ...** and resource types **A, B, C ...**
- Need and Available are **computed** by the program. You do not type them.
- If your problem gives **Available** instead of Total, compute Total first: Total = Available + column sums of Allocation.

**Input validation.** The program shows a message and asks again instead of crashing when:

- a value is not a whole number, is negative, or the count of values is wrong;
- a menu choice or process number is out of range;
- the column sums of Allocation are more than Total (you must re-enter the whole Allocation matrix);
- a Max value is less than the matching Allocation value (you must re-enter that row).

### Option 2: Sample data sets

| # | Data set | Result |
|---|---|---|
| 1 | Textbook example, 5 processes, 3 resources | SAFE |
| 2 | Unsafe state, 5 processes, 3 resources (same Max as set 1, different Allocation) | UNSAFE |
| 3 | 4 resource types, 5 processes, 4 resources | SAFE |

These are **inputs only**. Every result is computed by the program.

### Option 5: Resource request

| Prompt | What to type | Example |
|---|---|---|
| Requesting process number | the process index | `1` (for P1) |
| Request vector | one number per resource type | `1 0 2` |

---

## 4. Reading the output

### System state (option 3)

Output for sample data set 1:

```
Total         A    B    C
             10    5    7

Process  | Allocation  |     Max     |    Need
         |   A   B   C |   A   B   C |   A   B   C
---------------------------------------------------
P0       |   0   1   0 |   7   5   3 |   7   4   3
P1       |   2   0   0 |   3   2   2 |   1   2   2
P2       |   3   0   2 |   9   0   2 |   6   0   0
P3       |   2   1   1 |   2   2   2 |   0   1   1
P4       |   0   0   2 |   4   3   3 |   4   3   1

Need = Max - Allocation
Available = Total - column sums of Allocation
  Column sums of Allocation = [7 2 5]
Available     A    B    C
              3    3    2
```

| Item | Meaning | Formula |
|---|---|---|
| Total | All instances of each resource type in the system | (input) |
| Allocation | What each process holds right now | (input) |
| Max | The most each process may ever ask for | (input) |
| Need | What each process may still ask for | Need = Max - Allocation |
| Available | What is free right now | Available = Total - column sums of Allocation |

### Safety algorithm trace (option 4)

Output for sample data set 1:

```
Step 1: Work = Available = [3 3 2]
        Finish = P0=F P1=F P2=F P3=F P4=F

--- Pass 1 ---
P0: Need [7 4 3] <= Work [3 3 2] ?  NO
    P0 must wait (not enough resources)
P1: Need [1 2 2] <= Work [3 3 2] ?  YES
    Work = [3 3 2] + Allocation [2 0 0] = [5 3 2]
    Finish[P1] = True  ->  P0=F P1=T P2=F P3=F P4=F
...
--- Pass 2 ---
P0: Need [7 4 3] <= Work [7 4 5] ?  YES
    Work = [7 4 5] + Allocation [0 1 0] = [7 5 5]
    Finish[P0] = True  ->  P0=T P1=T P2=F P3=T P4=T
P2: Need [6 0 0] <= Work [7 5 5] ?  YES
    Work = [7 5 5] + Allocation [3 0 2] = [10 5 7]
    Finish[P2] = True  ->  P0=T P1=T P2=T P3=T P4=T

Final Finish flags: P0=T P1=T P2=T P3=T P4=T
----------------------------------------------------------------
 RESULT: SAFE STATE
 Safe sequence: < P1, P3, P4, P0, P2 >
----------------------------------------------------------------
```

The full output is saved in [`test_evidence/TC1_safe_state.txt`](test_evidence/TC1_safe_state.txt).

| Output line | Meaning |
|---|---|
| `Step 1: Work = Available = [..]` | Work starts as a copy of Available. All Finish flags start as F. |
| `--- Pass N ---` | One scan through every unfinished process, P0 to the last. |
| `Pn: Need [..] <= Work [..] ?  YES` | Every value of Need is <= the matching value of Work, so this process can finish. |
| `Pn: Need [..] <= Work [..] ?  NO` | At least one value of Need is bigger than Work. The process must wait for now. |
| `Work = Work + Allocation [..] = [..]` | The finished process returns everything it holds, so more is free. |
| `Finish[Pn] = True -> P0=F P1=T ...` | Updated Finish flags. T = can finish, F = not yet. |
| `RESULT: SAFE STATE` + safe sequence | All processes can finish in this order. No deadlock. |
| `RESULT: UNSAFE STATE (possible deadlock)` | A full pass picked no process and some Finish flags are still F. The system **may** deadlock. |

The program keeps scanning until all processes finish or a whole pass picks nobody.

> **Note:** UNSAFE does not mean deadlock has already happened. It means the system cannot guarantee that every process can finish, so a deadlock is possible. That is why the Banker's Algorithm refuses to move into an unsafe state.

### Resource request (option 5)

**Granted request** (P1 requests `1 0 2` on sample data set 1):

```
 P1 requests [1 0 2]
Check 1: Request [1 0 2] <= Need(P1) [1 2 2] ?  YES
Check 2: Request [1 0 2] <= Available [3 3 2] ?  YES

Step 3: Tentative state (pretend the request is granted)
  Available  = Available - Request = [2 3 0]
  Allocation(P1) = Allocation + Request = [3 0 2]
  Need(P1)       = Need - Request = [0 2 0]
...
 DECISION: GRANT
 Tentative state is SAFE. Request is granted.
 The system state has been UPDATED with this allocation.
```

**Request that must wait** (then P0 requests `0 2 0`):

```
 P0 requests [0 2 0]
Check 1: Request [0 2 0] <= Need(P0) [7 4 3] ?  YES
Check 2: Request [0 2 0] <= Available [2 3 0] ?  YES
...
 RESULT: UNSAFE STATE  (possible deadlock)
...
 DECISION: WAIT
 Tentative state is UNSAFE. Request is not granted; state is rolled back and the process must wait.
 The system state was NOT changed.
```

The full output of both is saved in [`test_evidence/TC3_to_TC6_requests.txt`](test_evidence/TC3_to_TC6_requests.txt).

| Output | Meaning | Decision |
|---|---|---|
| `Check 1: Request <= Need ?  NO` | The process asked for more than its declared maximum. | **ERROR** (rejected) |
| `Check 2: Request <= Available ?  NO` | Not enough free resources right now. | **WAIT** |
| `Step 3: Tentative state` | The program pretends to grant: Available - Request, Allocation + Request, Need - Request. | |
| Tentative state is SAFE | Granting keeps the system safe. The new state is kept. | **GRANT** |
| Tentative state is UNSAFE | Granting could lead to deadlock. The tentative state is thrown away. | **WAIT** |

After a **GRANT**, later options use the updated state. After **WAIT** or **ERROR**, nothing changes.

---

## 5. The algorithms

### Safety Algorithm

1. `Work = Available` and `Finish[i] = False` for every process.
2. Find a process `i` where `Finish[i] == False` and `Need[i] <= Work` (every resource type).
3. If found: `Work = Work + Allocation[i]`, `Finish[i] = True`, add `Pi` to the safe sequence, go back to step 2.
4. If none is found: the state is **SAFE** if every `Finish[i]` is True, otherwise **UNSAFE**.

### Resource-Request Algorithm (process `i` asks for `Request`)

1. If `Request > Need[i]` for any resource type: **ERROR** (exceeds its maximum claim).
2. If `Request > Available` for any resource type: **WAIT**.
3. Pretend to allocate: `Available -= Request`, `Allocation[i] += Request`, `Need[i] -= Request`.
4. Run the Safety Algorithm on this tentative state. SAFE: **GRANT**. UNSAFE: roll back and **WAIT**.

### Worked example (sample data set 1)

- Total = [10 5 7], column sums of Allocation = [7 2 5], so **Available = [3 3 2]**.
- Work goes [3 3 2] → [5 3 2] (P1) → [7 4 3] (P3) → [7 4 5] (P4) → [7 5 5] (P0) → [10 5 7] (P2).
- **SAFE**, safe sequence **< P1, P3, P4, P0, P2 >**. The final Work equals Total, which is a good self-check.

Full hand computation: [`docs/TEST_CASES.md`](docs/TEST_CASES.md#tc1-hand-computation-safety-algorithm).

---

## 6. Testing

8 test cases were run on the live program, and 16 automated tests check the same behavior. **All passed.**

| TC | What is tested | Expected | Actual | Status |
|---|---|---|---|---|
| 1 | Safe state | SAFE < P1, P3, P4, P0, P2 > | Same | PASS |
| 2 | Unsafe state | UNSAFE STATE | Same | PASS |
| 3 | P1 requests [1 0 2] | GRANT | GRANT | PASS |
| 4 | Then P0 requests [0 2 0] | WAIT (unsafe) | WAIT | PASS |
| 5 | Then P4 requests [3 3 0] | WAIT (not available) | WAIT | PASS |
| 6 | Then P0 requests [8 0 0] | ERROR (exceeds Need) | ERROR | PASS |
| 7 | 4 resource types + request | SAFE < P0, P2, P3, P4, P1 >, GRANT | Same | PASS |
| 8 | Invalid inputs | Rejected with a message, no crash | Same | PASS |

- Inputs, hand computations and full results: [`docs/TEST_CASES.md`](docs/TEST_CASES.md)
- Saved program output for each case: [`test_evidence/`](test_evidence/)

**How to reproduce:** run `python test_banker.py` for the automated tests, or type the inputs from `docs/TEST_CASES.md` into the live program and compare with the files in `test_evidence/`.

---

## 7. Code structure

`BANKERS_ALGO-GROUP-8.py` is split into 7 commented sections:

| Section | Functions | What it does |
|---|---|---|
| 1. Preset data | `PRESETS` | Sample inputs for demos (inputs only) |
| 2. Vector helpers | `vec_add`, `vec_sub`, `vec_leq`, `vec_str`, `flags_str` | Element-by-element math and printing |
| 3. Core computations | `compute_need`, `column_sums`, `compute_available`, `safety_algorithm`, `resource_request`, `validate_state` | The algorithms. They return results and a text trace, and print nothing. |
| 4. System state | `resource_names`, `SystemState` | Keeps Total, Allocation and Max together |
| 5. Output | `banner`, `pause`, `print_vector`, `print_state_table`, `show_state`, `show_safety`, `print_result`, `show_request` | Tables and trace on screen |
| 6. Input | `read_line`, `read_int`, `read_vector`, `read_matrix`, `enter_new_state`, `load_preset` | Reads and validates user input |
| 7. Main menu | `main` | Menu loop |

The algorithm code (section 3) is kept apart from input and output (sections 5 and 6). That is why `test_banker.py` can test the algorithms directly.

Key line, the "component-wise" comparison in `vec_leq`:

```python
return all(x <= y for x, y in zip(a, b))
```

`[1 2 2] <= [3 3 2]` is True because 1<=3, 2<=3 and 2<=2. `[7 4 3] <= [3 3 2]` is False because 7>3.

Note: the program file name has a hyphen, so `test_banker.py` loads it with `importlib` instead of a normal `import`.

---

## 8. Presentation and demo

- Demo script, speaking parts and oral defense review: [`docs/DEMO_SCRIPT.md`](docs/DEMO_SCRIPT.md)
- Slides: to be added by the group in `docs/presentation/`.

Quick demo flow (5 to 10 minutes):

1. Option 2 → data set 1 → explain Need and Available.
2. Option 4 → walk through Pass 1 and Pass 2 → safe sequence.
3. Option 5 → P1 requests `1 0 2` → GRANT.
4. Option 5 → P0 requests `0 2 0` → UNSAFE → WAIT.
5. Option 1 → type the instructor's own inputs live.

Before the demo: run `python test_banker.py` on the presenting laptop and keep a backup copy of the code on a USB drive.

---

## 9. Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| `'python' is not recognized` or `command not found` | Python is not installed or not on PATH | Install Python 3.8+ from python.org (tick "Add Python to PATH" on Windows), or try `py` / `python3` instead of `python` |
| `SyntaxError` on start | Python older than 3.8 | Check `python --version` and upgrade |
| `can't open file 'BANKERS_ALGO-GROUP-8.py'` | Terminal is in the wrong folder | `cd` into the folder that contains the file |
| `No data yet. Choose option 1 or 2 first.` | No system state loaded | Use option 1 or 2 first |
| `Column sums of Allocation ... exceed Total` | Allocated amount is more than Total | Re-check Total, or the Allocation rows |
| `Max must be >= Allocation` | A Max value is smaller than what the process already holds | Fix that Max row so Max >= Allocation |
| `Enter exactly N numbers` | Row has too few or too many numbers | Type exactly one number per resource type |
| `Use whole numbers that are 0 or greater only` | A value is a letter, a decimal or negative | Type whole numbers, 0 or greater |
| Program closes at once when double-clicked | Windows closes the window when the program ends | Run it from a terminal, as in section 2 |

---

## 10. Assumptions and limitations

- Resources are **reusable** and each type has a **fixed** number of instances (the textbook model).
- Every process declares its **Max** claim in advance and never exceeds it.
- Processes are checked in index order (P0, P1, ...). Other valid safe sequences may exist, so the sequence shown is one of possibly several.
- One request is handled at a time. There is no simulation of several requests arriving together or of time passing.
- The program does not model deadlock **detection** or **recovery**, only avoidance.
- Limits: 1 to 20 processes and 1 to 10 resource types.
- Only a GRANT changes the saved state. Processes never release resources in the simulator. Use option 1 or 2 to start a new scenario.
- The program is a console simulator for learning. It is not connected to a real operating system scheduler.

---

## 11. References

- Silberschatz, A., Galvin, P. B., & Gagne, G. *Operating System Concepts* (10th ed.). Wiley. Chapter 8: Deadlocks, Section 8.6 Deadlock Avoidance (Banker's Algorithm).
- Dijkstra, E. W. *Een algorithme ter voorkoming van de dodelijke omarming* (EWD108). The original Banker's Algorithm.
- Python Software Foundation. *Python 3 Documentation*: `unittest`. https://docs.python.org/3/library/unittest.html
- PT 101 Final Project Guidelines, BatStateU CICS, AY 2026-2027.

## 12. Assistance disclosure

| Tool / source | What it was used for | Reviewed by the group? |
|---|---|---|
| Claude (AI assistant by Anthropic) | Drafting and correcting this README, writing `test_banker.py`, `docs/TEST_CASES.md`, `docs/CONTRIBUTIONS.md` (template), `docs/DEMO_SCRIPT.md` and `.gitignore`, and running the program to save `test_evidence/` | **Group to confirm** |
| Silberschatz et al., *Operating System Concepts* | Algorithm definitions and the textbook sample data | Yes |

**Group to confirm before submitting:** if any other tool, AI assistant, tutorial or classmate helped with `BANKERS_ALGO-GROUP-8.py` or anything else, add a row above. Follow your instructor's policy on AI use.

Statement: all members have read the code and documents in this repository and can explain them during the oral defense.
