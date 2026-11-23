# Banker's Algorithm Simulator (Deadlock Avoidance)

**PT 101 - Platform Technologies | Final Project | Topic 5**
Batangas State University, College of Informatics and Computing Sciences, Alangilan Campus
1st Semester AY 2026-2027

A Python console program that simulates the **Banker's Safety Algorithm** and the **Resource-Request Algorithm**. Every computation is shown step by step: Need, Available, each Work comparison and update, the Finish flags, and the safe sequence (or UNSAFE STATE). For requests it shows Request <= Need, Request <= Available, the tentative state, the safety result and the GRANT / WAIT decision.

All results are computed by the program from the inputs. Nothing is hard-coded.

![Safety algorithm trace](docs/screenshots/03_safety_trace.png)

---

## Contents

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
- [9. Uploading to GitHub](#9-uploading-to-github)
- [10. References](#10-references)
- [11. Assistance disclosure](#11-assistance-disclosure)

---

## Deliverables checklist

| # | Deliverable (from the project guidelines) | Where to find it | Status |
|---|---|---|---|
| 1 | Complete, organized source code (GitHub repository) | [`banker.py`](banker.py), [`test_banker.py`](test_banker.py), this repository | Done |
| 2 | User guide: execution, inputs, output interpretation | This README, sections [2](#2-how-to-run), [3](#3-inputs) and [4](#4-reading-the-output) | Done |
| 3 | Testing evidence: at least 3 test cases, expected vs actual | [`docs/TEST_CASES.md`](docs/TEST_CASES.md) (8 cases) and [`test_evidence/`](test_evidence/) | Done |
| 4 | Contribution record in the instructor's Google Spreadsheet | Copy from [`docs/CONTRIBUTIONS.md`](docs/CONTRIBUTIONS.md) into the instructor's sheet | **Group to fill in** |
| 5 | Demo / presentation materials | [`docs/presentation/`](docs/presentation/) (slides) and [`docs/DEMO_SCRIPT.md`](docs/DEMO_SCRIPT.md) | Done |

---

## Group members

| Name | Role | Main tasks |
|---|---|---|
| | Leader | |
| | | |
| | | |
| | | |
| | | |

Full task record: [`docs/CONTRIBUTIONS.md`](docs/CONTRIBUTIONS.md)

---

## Repository structure

```
bankers-algorithm/
├── banker.py                  # the program (run this)
├── test_banker.py             # automated test cases
├── README.md                  # user guide (this file)
├── .gitignore
├── docs/
│   ├── TEST_CASES.md          # test cases: expected vs actual results
│   ├── CONTRIBUTIONS.md       # contribution record template
│   ├── DEMO_SCRIPT.md         # demo flow, speaking parts, oral defense review
│   ├── presentation/
│   │   └── Bankers_Algorithm_Presentation.pptx
│   └── screenshots/           # real program output used in this guide
└── test_evidence/             # saved program output for every test case
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
   git clone <repository-url>
   ```
2. Open a terminal in the project folder (Windows: open the folder, type `cmd` in the address bar, press Enter).
3. Start the program:
   ```
   python banker.py
   ```
   If `python` is not found, try `py banker.py` (Windows) or `python3 banker.py` (macOS/Linux).
4. Choose options from the menu by typing the number and pressing Enter.

To run the automated tests:

```
python test_banker.py
```

![Main menu](docs/screenshots/01_main_menu.png)

| Option | What it does |
|---|---|
| 1. Enter new system state | Type your own processes, Total, Allocation and Max |
| 2. Load sample data set | Load one of 3 ready-made inputs |
| 3. Show system state | Show Total, Allocation, Max, Need and Available |
| 4. Run Safety Algorithm | Step-by-step trace and the SAFE / UNSAFE result |
| 5. Resource Request | Check a request and decide GRANT / WAIT |
| 6. Exit | Close the program |

Options 3 to 5 need data first, so start with option 1 or 2.

---

## 3. Inputs

### Option 1: Enter new system state

The program asks for these, in order:

| Prompt | What to type | Example |
|---|---|---|
| Number of processes | 1 to 20 | `5` |
| Number of resource types | 1 to 10 | `3` |
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
- the column sums of Allocation are more than Total;
- a Max value is less than the matching Allocation value.

### Option 2: Sample data sets

| # | Data set | Result |
|---|---|---|
| 1 | Textbook example, 5 processes, 3 resources | SAFE |
| 2 | Same system, different allocation | UNSAFE |
| 3 | 5 processes, 4 resources | SAFE |

These are **inputs only**. Every result is computed by the program.

### Option 5: Resource request

| Prompt | What to type | Example |
|---|---|---|
| Requesting process number | the process index | `1` (for P1) |
| Request vector | one number per resource type | `1 0 2` |

---

## 4. Reading the output

### System state

![System state](docs/screenshots/02_system_state.png)

| Item | Meaning | Formula |
|---|---|---|
| Total | All instances of each resource type in the system | (input) |
| Allocation | What each process holds right now | (input) |
| Max | The most each process may ever ask for | (input) |
| Need | What each process may still ask for | Need = Max - Allocation |
| Available | What is free right now | Available = Total - column sums of Allocation |

### Safety algorithm trace

See the screenshot at the top of this guide.

| Output line | Meaning |
|---|---|
| `Step 1: Work = Available` | Work starts as a copy of Available. All Finish flags start as F. |
| `--- Pass N ---` | One scan through every unfinished process, P0 to the last. |
| `Need [..] <= Work [..] ? YES` (green) | Every value of Need is <= the matching value of Work, so this process can finish. |
| `Need [..] <= Work [..] ? NO` (red) | At least one value of Need is bigger than Work. The process must wait for now. |
| `Work = Work + Allocation` | The finished process returns everything it holds, so more is free. |
| `Finish[Pn] = True -> P0=F P1=T ...` | Updated Finish flags. T = can finish, F = not yet. |
| `RESULT: SAFE STATE` + safe sequence | All processes can finish in this order. No deadlock. |
| `RESULT: UNSAFE STATE` | A full pass picked no process and some Finish flags are still F. The system **may** deadlock. |

The program keeps scanning until all processes finish or a whole pass picks nobody.

### Resource request

**Granted request** (P1 requests `1 0 2` on sample data set 1):

![Request granted](docs/screenshots/04_request_grant.png)

**Request that must wait** (then P0 requests `0 2 0`):

![Request must wait](docs/screenshots/05_request_wait.png)

| Output | Meaning | Decision |
|---|---|---|
| `Check 1: Request <= Need ? NO` | The process asked for more than its declared maximum. | **ERROR** (rejected) |
| `Check 2: Request <= Available ? NO` | Not enough free resources right now. | **WAIT** |
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

8 test cases were run on the live program and as automated tests. **All passed.**

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

---

## 7. Code structure

`banker.py` is split into 7 commented sections:

| Section | Functions | What it does |
|---|---|---|
| 1. Preset data | `PRESETS` | Sample inputs for demos (inputs only) |
| 2. Vector helpers | `vec_add`, `vec_sub`, `vec_leq`, `vec_str`, `flags_str` | Element-by-element math and printing |
| 3. Core computations | `compute_need`, `column_sums`, `compute_available`, `safety_algorithm`, `resource_request`, `validate_state` | The algorithms. They return results and a text trace, and print nothing. |
| 4. System state | `resource_names`, `SystemState` | Keeps Total, Allocation and Max together |
| 5. Output | `show_state`, `show_safety`, `show_request`, `print_state_table`, `print_result` | Tables and trace on screen |
| 6. Input | `read_int`, `read_vector`, `read_matrix`, `enter_new_state`, `load_preset` | Reads and validates user input |
| 7. Main menu | `main` | Menu loop |

The algorithm code (section 3) is kept apart from input and output (sections 5 and 6). That is why `test_banker.py` can test the algorithms directly.

Key line, the "component-wise" comparison in `vec_leq`:

```python
return all(x <= y for x, y in zip(a, b))
```

`[1 2 2] <= [3 3 2]` is True because 1<=3, 2<=3 and 2<=2. `[7 4 3] <= [3 3 2]` is False because 7>3.

---

## 8. Presentation and demo

- Slides: [`docs/presentation/Bankers_Algorithm_Presentation.pptx`](docs/presentation/) (speaker notes included)
- Demo script, speaking parts and oral defense review: [`docs/DEMO_SCRIPT.md`](docs/DEMO_SCRIPT.md)

Quick demo flow (5 to 10 minutes):

1. Option 2 → data set 1 → explain Need and Available.
2. Option 4 → walk through Pass 1 and Pass 2 → safe sequence.
3. Option 5 → P1 requests `1 0 2` → GRANT.
4. Option 5 → P0 requests `0 2 0` → UNSAFE → WAIT.
5. Option 1 → type the instructor's own inputs live.

Before the demo: run `python test_banker.py` on the presenting laptop and keep a backup copy of the code on a USB drive.

---

## 9. Uploading to GitHub

**Option A: GitHub website (no Git needed)**

1. Sign in at github.com and click **New repository**. Name it, e.g. `pt101-bankers-algorithm`. Set it to Public (or as your instructor says). Click **Create repository**.
2. Click **uploading an existing file**.
3. Drag in **everything inside** the project folder, including the `docs` and `test_evidence` folders.
4. Click **Commit changes**.
5. Open the repository page and check that this README shows with its screenshots.

**Option B: Git command line**

```
cd bankers-algorithm
git init
git add .
git commit -m "Banker's Algorithm Simulator - PT 101 Topic 5"
git branch -M main
git remote add origin https://github.com/<username>/pt101-bankers-algorithm.git
git push -u origin main
```

Add every group member as a collaborator (**Settings > Collaborators**) so each person can commit their own part. Commits by each member also count as contribution evidence.

---

## 10. References

- Silberschatz, A., Galvin, P. B., & Gagne, G. *Operating System Concepts* (10th ed.). Wiley. Chapter 8: Deadlocks, Section 8.6 Deadlock Avoidance (Banker's Algorithm).
- Dijkstra, E. W. *Een algorithme ter voorkoming van de dodelijke omarming* (EWD108). The original Banker's Algorithm.
- Python Software Foundation. *Python 3 Documentation*: `unittest`. https://docs.python.org/3/library/unittest.html
- PT 101 Final Project Guidelines, BatStateU CICS, AY 2026-2027.

## 11. Assistance disclosure

(Fill this in according to your course policy. List any tools, AI assistants or outside help used, and what each was used for.)
