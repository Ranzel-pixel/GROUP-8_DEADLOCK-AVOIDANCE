# Banker's Algorithm Simulator (Deadlock Avoidance)

**PT 101 - Platform Technologies | Final Project | Topic 5: Deadlock Avoidance - Banker's Algorithm**
Batangas State University, College of Informatics and Computing Sciences, Alangilan Campus
Information Technology Department | 1st Semester AY 2026-2027

A Python console program that simulates the **Banker's Safety Algorithm** (required) and the **Resource-Request Algorithm** (the extension named in the guidelines). Every computation is shown step by step: Total, Allocation, Max, Need, Available, each Work comparison and update, the Finish flags, and the safe sequence (or UNSAFE STATE). For requests it shows Request <= Need, Request <= Available, the tentative state, the safety result and the GRANT / WAIT decision.

All results are computed by the program from the inputs. Nothing is hard-coded.

---

## Project information

| Item | Details |
|---|---|
| Course | PT 101 - Platform Technologies |
| Project | Final Project, Topic 5: Deadlock Avoidance - Banker's Algorithm |
| Group | Group 8 (4 members) |
| Department / College | Information Technology Department, College of Informatics and Computing Sciences |
| School | Batangas State University, The National Engineering University, Alangilan Campus |
| Term | 1st Semester, AY 2026-2027 |
| Repository | https://github.com/Ranzel-pixel/GROUP-8_DEADLOCK-AVOIDANCE |
| Program file | [`BANKERS_ALGO-GROUP-8.py`](BANKERS_ALGO-GROUP-8.py) |
| Language | Python 3.8+ (standard library only). Allowed by the guidelines: Java, C++ or Python. |

---

## Contents

- [Features](#features)
- [Project requirements and how this project meets them](#project-requirements-and-how-this-project-meets-them)
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

---

## Features

- Safety Algorithm with a full step-by-step trace (every pass, every comparison, every Work update).
- Resource-Request Algorithm with its checks (Request <= Need, Request <= Available, tentative state safe) and a final GRANT / WAIT / ERROR decision.
- Computes Need and Available from your inputs. You never type them.
- Three ready-made sample data sets, or enter your own system (1 to 20 processes, 1 to 10 resource types).
- Input validation: bad input shows a message and asks again instead of crashing.
- The algorithm code is separate from input and output, which keeps the code organized.
- No external libraries. Runs on Windows, macOS and Linux.

---

## Project requirements and how this project meets them

The PT 101 Final Project Guidelines (AY 2026-2027) ask for the following for **Topic 5**.

### What the guidelines require for Topic 5

| Guideline item | How this project meets it |
|---|---|
| **Required:** Banker's Safety Algorithm | Option 4, `safety_algorithm()` ([section 5](#5-the-algorithms)) |
| Resource-request checking (extension) | Option 5, `resource_request()`: Request <= Need, Request <= Available, tentative state, safety result, GRANT / WAIT (plus ERROR when Request > Need) |
| **Input:** process count, resource types, Total vector, Allocation matrix, Max matrix, optional requesting process and Request vector | Options 1 and 5 ([section 3](#3-inputs)) |
| **Processing:** Need = Max - Allocation; Available = Total - column sums of Allocation; Work = Available; Finish = False; find unfinished process with Need <= Work (component-wise); Work = Work + Allocation; Finish = True; repeat | `compute_need`, `compute_available`, `safety_algorithm`, `vec_leq` ([section 7](#7-code-structure)) |
| **Output:** Total, Allocation, Max, Need, Available; each Work comparison and update; Finish flags; safe sequence or UNSAFE STATE | Options 3 and 4 ([section 4](#4-reading-the-output)) |
| **Output for requests:** Request <= Need, Request <= Available, tentative state, safety result, GRANT / WAIT | Option 5 ([section 4](#4-reading-the-output)) |
| Hard-coded sample outputs are **not** acceptable | The three sample data sets are **inputs only**. All results are computed. To check, use option 1 and type any other inputs. |
| Allowed languages: Java, C++ or Python | Python 3.8+ |
| Group of four (4) to five (5) members | 4 members ([Group members](#group-members)) |
| Use only the assigned topic. Do not copy another group's program. Cite resources. | [References](#11-references) |

### How this project covers the grading rubric

| Rubric criterion | Points | Where this project addresses it |
|---|---|---|
| Algorithm correctness and computation | 20 | Intermediate trace of every pass. 8 test cases checked against hand computations ([section 6](#6-testing)) |
| Output clarity and usability | 15 | Aligned tables, labeled vectors (A, B, C and P0, P1 ...), YES / NO on every comparison ([section 4](#4-reading-the-output)) |
| Code structure and organization | 10 | 7 commented sections, algorithms separate from input and output ([section 7](#7-code-structure)), this user guide and [references](#11-references) |
| User interface | 5 | Numbered menu, input validation that asks again instead of crashing ([sections 2 and 3](#2-how-to-run)) |
| Verified contribution (individual) | 20 | GitHub commit history and the contribution record in the instructor's spreadsheet |
| Individual oral defense (individual) | 20 | [Section 8](#8-presentation-and-demo): demo rules, demo flow and how to trace a computation by hand |
| Professionalism and participation (individual) | 10 | Every member contributes commits and joins the demo |

---

## Deliverables checklist

The five deliverables listed in the project guidelines:

| # | Deliverable (from the project guidelines) | Where to find it | Status |
|---|---|---|---|
| 1 | Complete, organized source code (GitHub repository) | [`BANKERS_ALGO-GROUP-8.py`](BANKERS_ALGO-GROUP-8.py), this repository | Done |
| 2 | User guide describing execution, inputs, and output interpretation | This README, sections [2](#2-how-to-run), [3](#3-inputs) and [4](#4-reading-the-output) | Done |
| 3 | Testing evidence: at least three test cases with expected and actual results | [Section 6](#6-testing) of this README (8 cases, expected vs actual) | Done |
| 4 | Contribution record in the instructor-provided Google Spreadsheet | Fill in the group's rows **directly in the instructor's spreadsheet**. | **Group to fill in** |
| 5 | Demo / presentation materials for the actual presentation | [Section 8](#8-presentation-and-demo) of this README (demo rules, demo flow, how to trace by hand) | Done |

---

## Group members

The guidelines say the group leader assigns tasks, monitors progress, and makes sure every member takes part.

| Name | Role | Main tasks |
|---|---|---|
| HIDALGO, PERSHEY RANZEL JAMINA | Leader | Assigned tasks and monitored the group's progress; wrote the program (banker.py): safety algorithm, resource-request algorithm, input validation, menu and output; wrote the automated tests (test_banker.py); runs the live demo. |
| BATHAN, EMMANUEL | Member | Set up and manages the GitHub repository; uploaded and organized the project files; added members as collaborators; presents the resource request examples in the demo.|
| ABANTE, SER JAMES | Member | Prepares the presentation slides (group names, repository link); tests the slides on the projector and keeps a PDF backup; opens and closes the presentation. |
| GUIZZAGAN, CHRISTIAN | Member | Runs the 8 test cases on his own laptop and takes screenshots as testing evidence; checks expected vs actual results in the test document; presents the formulas and testing results. |

Keep this table the same as the instructor's spreadsheet.

---

## Repository structure

```
GROUP-8_DEADLOCK-AVOIDANCE/
├── BANKERS_ALGO-GROUP-8.py    # the program (run this)
└── README.md                  # user guide and test report (this file)
```

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

Full hand computation: [section 6, TC1](#tc1-hand-computation-safety-algorithm).

---

## 6. Testing

This section is the testing evidence (deliverable 3): **8 test cases**, each with its input, the expected result worked out by hand, and the actual result printed by the program. All 8 passed.

### Summary

| TC | What is tested | Input | Expected | Actual | Status |
|---|---|---|---|---|---|
| 1 | Safe state | Option 2, data set 1, then option 4 | SAFE, < P1, P3, P4, P0, P2 > | SAFE, < P1, P3, P4, P0, P2 > | PASS |
| 2 | Unsafe state | Option 2, data set 2, then option 4 | UNSAFE STATE | UNSAFE STATE | PASS |
| 3 | Request that keeps the system safe | Data set 1, P1 requests `1 0 2` | GRANT | GRANT | PASS |
| 4 | Request that makes the system unsafe | Then P0 requests `0 2 0` | WAIT (unsafe) | WAIT (unsafe) | PASS |
| 5 | Request more than Available | Then P4 requests `3 3 0` | WAIT (not available) | WAIT (not available) | PASS |
| 6 | Request more than Need | Then P0 requests `8 0 0` | ERROR (exceeds Need) | ERROR (exceeds Need) | PASS |
| 7 | 4 resource types and a request | Data set 3, safety, then P1 requests `0 0 1 0` | SAFE < P0, P2, P3, P4, P1 >, GRANT | Same | PASS |
| 8 | Invalid inputs | Option 1 and option 5 with bad values | Each bad value rejected with a message, no crash | Same | PASS |

TC3 to TC6 are one continuous session. Each request runs on the state left by the one before it. Only a GRANT changes the state, so TC4, TC5 and TC6 all run on the state after TC3.

### TC1 Hand computation: Safety Algorithm

**Input (sample data set 1):** 5 processes, 3 resource types, Total = [10 5 7]

| Process | Allocation | Max | Need = Max - Allocation |
|---|---|---|---|
| P0 | 0 1 0 | 7 5 3 | 7 4 3 |
| P1 | 2 0 0 | 3 2 2 | 1 2 2 |
| P2 | 3 0 2 | 9 0 2 | 6 0 0 |
| P3 | 2 1 1 | 2 2 2 | 0 1 1 |
| P4 | 0 0 2 | 4 3 3 | 4 3 1 |

Column sums of Allocation = [7 2 5], so **Available = [10 5 7] - [7 2 5] = [3 3 2]**.

| Step | Process checked | Need <= Work? | Work after |
|---|---|---|---|
| Start | | | [3 3 2] |
| Pass 1 | P0: [7 4 3] <= [3 3 2] | NO (7 > 3) | |
| | P1: [1 2 2] <= [3 3 2] | YES | [3 3 2] + [2 0 0] = [5 3 2] |
| | P2: [6 0 0] <= [5 3 2] | NO (6 > 5) | |
| | P3: [0 1 1] <= [5 3 2] | YES | [5 3 2] + [2 1 1] = [7 4 3] |
| | P4: [4 3 1] <= [7 4 3] | YES | [7 4 3] + [0 0 2] = [7 4 5] |
| Pass 2 | P0: [7 4 3] <= [7 4 5] | YES | [7 4 5] + [0 1 0] = [7 5 5] |
| | P2: [6 0 0] <= [7 5 5] | YES | [7 5 5] + [3 0 2] = [10 5 7] |

All Finish flags are True. **Expected: SAFE, safe sequence < P1, P3, P4, P0, P2 >.** Self-check: the final Work [10 5 7] equals Total.

**Actual (program output):**

```
 RESULT: SAFE STATE
 Safe sequence: < P1, P3, P4, P0, P2 >
```

**Status: PASS.** (The full trace is shown in section 4.)

### TC2 Unsafe state

**Input (sample data set 2):** Total = [10 5 7]. Allocation is the same as data set 1 except P0 = [0 3 0] and P1 = [3 0 2]. Max is the same as data set 1.

Column sums of Allocation = [8 4 7], so **Available = [2 1 0]**. Needs: P0 [7 2 3], P1 [0 2 0], P2 [6 0 0], P3 [0 1 1], P4 [4 3 1].

Checking each process against Work = [2 1 0]:

- P0: 7 > 2 on A, NO
- P1: 2 > 1 on B, NO
- P2: 6 > 2 on A, NO
- P3: 1 > 0 on C, NO
- P4: 4 > 2 on A, NO

No process can run, so none finishes. **Expected: UNSAFE STATE.**

**Actual (program output):**

```
 RESULT: UNSAFE STATE  (possible deadlock)
 No safe sequence exists for all processes.
```

**Status: PASS.**

### TC3 Request that is granted

State: data set 1, Available = [3 3 2]. **P1 requests [1 0 2].**

- Check 1: [1 0 2] <= Need(P1) [1 2 2]? YES
- Check 2: [1 0 2] <= Available [3 3 2]? YES
- Tentative state: Available = [3 3 2] - [1 0 2] = [2 3 0]. Allocation(P1) = [2 0 0] + [1 0 2] = [3 0 2]. Need(P1) = [1 2 2] - [1 0 2] = [0 2 0].
- The safety algorithm on the tentative state finds a safe sequence (P1 can finish first because Need [0 2 0] <= Work [2 3 0]).

**Expected: GRANT, state updated.**

**Actual (program output):**

```
Check 1: Request [1 0 2] <= Need(P1) [1 2 2] ?  YES
Check 2: Request [1 0 2] <= Available [3 3 2] ?  YES
 RESULT: SAFE STATE
 DECISION: GRANT
 Tentative state is SAFE. Request is granted.
 The system state has been UPDATED with this allocation.
```

**Status: PASS.**

### TC4 Request that leads to an unsafe state

State: after TC3, Available = [2 3 0]. **P0 requests [0 2 0].**

- Check 1: [0 2 0] <= Need(P0) [7 4 3]? YES
- Check 2: [0 2 0] <= Available [2 3 0]? YES
- Tentative state: Available = [2 1 0]. Needs: P0 [7 2 3], P1 [0 2 0], P2 [6 0 0], P3 [0 1 1], P4 [4 3 1].
- With Work = [2 1 0], no process has Need <= Work (the same situation as TC2). The tentative state is UNSAFE.

**Expected: WAIT, state not changed.**

**Actual (program output):**

```
Check 1: Request [0 2 0] <= Need(P0) [7 4 3] ?  YES
Check 2: Request [0 2 0] <= Available [2 3 0] ?  YES
 RESULT: UNSAFE STATE  (possible deadlock)
 DECISION: WAIT
 Tentative state is UNSAFE. Request is not granted; state is rolled back and the process must wait.
 The system state was NOT changed.
```

**Status: PASS.**

### TC5 Request more than Available

State: after TC3, Available = [2 3 0]. **P4 requests [3 3 0].**

- Check 1: [3 3 0] <= Need(P4) [4 3 1]? YES
- Check 2: [3 3 0] <= Available [2 3 0]? NO (3 > 2 on A)

**Expected: WAIT (not enough free resources). No tentative state is built.**

**Actual (program output):**

```
Check 1: Request [3 3 0] <= Need(P4) [4 3 1] ?  YES
Check 2: Request [3 3 0] <= Available [2 3 0] ?  NO
 DECISION: WAIT
 Resources are not available right now. Process must wait.
 The system state was NOT changed.
```

**Status: PASS.**

### TC6 Request more than Need

State: after TC3. **P0 requests [8 0 0].**

- Check 1: [8 0 0] <= Need(P0) [7 4 3]? NO (8 > 7 on A)

**Expected: ERROR. The process asked for more than its maximum claim.**

**Actual (program output):**

```
Check 1: Request [8 0 0] <= Need(P0) [7 4 3] ?  NO
 DECISION: ERROR
 P0 asked for more than its maximum claim. Request is rejected.
 The system state was NOT changed.
```

**Status: PASS.**

### TC7 Four resource types and a request

**Input (sample data set 3):** Total = [3 14 12 12], 5 processes, 4 resource types (A B C D). Available = [1 5 2 0].

Expected safe sequence **< P0, P2, P3, P4, P1 >**. Then **P1 requests [0 0 1 0]:**

- Check 1: [0 0 1 0] <= Need(P1) [0 7 5 0]? YES
- Check 2: [0 0 1 0] <= Available [1 5 2 0]? YES
- The tentative state (Available = [1 5 1 0]) is still safe with the same sequence.

**Expected: SAFE < P0, P2, P3, P4, P1 >, then GRANT.**

**Actual (program output):**

```
 RESULT: SAFE STATE
 Safe sequence: < P0, P2, P3, P4, P1 >
Check 1: Request [0 0 1 0] <= Need(P1) [0 7 5 0] ?  YES
Check 2: Request [0 0 1 0] <= Available [1 5 2 0] ?  YES
 RESULT: SAFE STATE
 Safe sequence: < P0, P2, P3, P4, P1 >
 DECISION: GRANT
```

**Status: PASS.**

### TC8 Invalid inputs

Typed into option 1 (Enter new system state) and option 5 (Resource Request). After every rejected value the program asked again. It never crashed.

| Prompt | Typed | Expected | Actual message | Status |
|---|---|---|---|---|
| Number of processes | `abc`, `0` | Rejected | `Please enter a whole number from 1 to 20.` | PASS |
| Number of resource types | `11` | Rejected | `Please enter a whole number from 1 to 10.` | PASS |
| Allocation row P0 (2 values needed) | `1 x` | Rejected | `Use whole numbers that are 0 or greater only.` | PASS |
| Allocation row P0 | `1 2 3` | Rejected | `Enter exactly 2 numbers (you entered 3).` | PASS |
| Allocation row P0 | `-1 0` | Rejected | `Use whole numbers that are 0 or greater only.` | PASS |
| Allocation P0 `3 0` and P1 `3 0`, Total `5 5` | column sum 6 > 5 | Rejected | `Column sums of Allocation [6 0] exceed Total [5 5]. Please re-enter the Allocation matrix.` | PASS |
| Max row P0 `0 0` when Allocation is `1 0` | Max < Allocation | Rejected | `Max must be >= Allocation [1 0] for P0.` | PASS |
| Requesting process number | `9` (only P0, P1 exist) | Rejected | `Please enter a whole number from 0 to 1.` | PASS |
| Request vector (2 values needed) | `1 2 3` | Rejected | `Enter exactly 2 numbers (you entered 3).` | PASS |

### How to reproduce

- **Live:** start `python BANKERS_ALGO-GROUP-8.py` and type the inputs from the tables above. Then compare your screen with the actual output shown for each test case.

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

The algorithm code (section 3) is kept apart from input and output (sections 5 and 6). This makes each part easy to read and to test separately.

Key line, the "component-wise" comparison in `vec_leq`:

```python
return all(x <= y for x, y in zip(a, b))
```

`[1 2 2] <= [3 3 2]` is True because 1<=3, 2<=3 and 2<=2. `[7 4 3] <= [3 3 2]` is False because 7>3.

---

## 8. Presentation and demo

**What the guidelines say about the face-to-face demonstration**

- Each group has **5 to 10 minutes** to explain the problem, inputs, algorithm, computation and outputs.
- Give a **live run** using sample inputs or inputs chosen by the instructor.
- **Every member** is asked an individual question about the output, the algorithm or the source code. All members must know the whole project, not only their own part.
- The instructor may ask a member to **trace a computation** or explain code. Unanswered, incorrect or unclear answers can lead to deductions in the individual oral defense.
- **Test the program before the presentation** and prepare a **backup copy** of the source code.

Quick demo flow (5 to 10 minutes):

1. Option 2 → data set 1 → explain Need and Available.
2. Option 4 → walk through Pass 1 and Pass 2 → safe sequence.
3. Option 5 → P1 requests `1 0 2` → GRANT.
4. Option 5 → P0 requests `0 2 0` → UNSAFE → WAIT.
5. Option 1 → type the instructor's own inputs live.

Before the demo: run `python BANKERS_ALGO-GROUP-8.py` once on the presenting laptop (try sample data set 1 and one request) and keep a backup copy of the code (USB drive or a second download of the repository).

**How to trace a computation by hand** (what the instructor may ask you to do)

1. Compute Need for every process: Need = Max - Allocation.
2. Compute Available: Available = Total - column sums of Allocation.
3. Set Work = Available and mark every process unfinished.
4. Go through P0, P1, P2 ... in order. For each unfinished process, compare **every** resource type: is Need <= Work? If yes, Work = Work + Allocation of that process and mark it finished. If no, skip it for now.
5. Repeat the pass until all processes are finished (SAFE, in the order they finished) or a whole pass finishes nobody (UNSAFE).
6. For a request: check Request <= Need (else ERROR), check Request <= Available (else WAIT), build the tentative state (Available - Request, Allocation + Request, Need - Request), run steps 3 to 5 on it. SAFE means GRANT, UNSAFE means WAIT.

A fully worked example is in [section 6, TC1](#tc1-hand-computation-safety-algorithm).

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
- Python Software Foundation. *Python 3 Documentation*. https://docs.python.org/3/
- PT 101 Final Project Guidelines, BatStateU CICS, AY 2026-2027.
