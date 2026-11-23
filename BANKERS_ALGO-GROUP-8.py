"""
===========================================================================
 BANKER'S ALGORITHM SIMULATOR  (Deadlock Avoidance)
 PT 101 - Platform Technologies | Final Project | Topic 5
===========================================================================
 What this program does
   1. Reads the system state: number of processes, number of resource
      types, Total vector, Allocation matrix and
      Max matrix.
   2. Computes  Need      = Max - Allocation
                Available = Total - (column sums of Allocation)
   3. Runs the Banker's SAFETY ALGORITHM and prints every step:
        Work = Available, Finish = False for all
        find an unfinished process with Need <= Work (component-wise)
        Work = Work + Allocation of that process, Finish = True
        repeat until no process can be picked
      -> prints the SAFE SEQUENCE, or UNSAFE STATE.
   4. (Extension) Runs the RESOURCE-REQUEST ALGORITHM:
        Request <= Need?  Request <= Available?
        build the tentative state, run the safety algorithm on it
        -> GRANT (keep new state) or WAIT (roll back).

 How to run:   python banker.py
 Requirements: Python 3.8 or newer, no extra libraries.

 Nothing is hard-coded as output. The preset data sets in PRESETS are
 only INPUTS; every result is computed by the functions below.
===========================================================================
"""

import sys


# ---------------------------------------------------------------------------
# 1. PRESET INPUT DATA (for quick demos and testing only)
# ---------------------------------------------------------------------------
# Each preset gives Total, Allocation and Max. The program still computes
# Need, Available, the trace and the safe sequence by itself.
PRESETS = [
    {
        "name": "Textbook example (5 processes, 3 resources) - SAFE",
        "total": [10, 5, 7],
        "allocation": [[0, 1, 0],
                       [2, 0, 0],
                       [3, 0, 2],
                       [2, 1, 1],
                       [0, 0, 2]],
        "max": [[7, 5, 3],
                [3, 2, 2],
                [9, 0, 2],
                [2, 2, 2],
                [4, 3, 3]],
    },
    {
        "name": "Unsafe state (5 processes, 3 resources) - UNSAFE",
        "total": [10, 5, 7],
        "allocation": [[0, 3, 0],
                       [3, 0, 2],
                       [3, 0, 2],
                       [2, 1, 1],
                       [0, 0, 2]],
        "max": [[7, 5, 3],
                [3, 2, 2],
                [9, 0, 2],
                [2, 2, 2],
                [4, 3, 3]],
    },
    {
        "name": "4 resource types (5 processes, 4 resources) - SAFE",
        "total": [3, 14, 12, 12],
        "allocation": [[0, 0, 1, 2],
                       [1, 0, 0, 0],
                       [1, 3, 5, 4],
                       [0, 6, 3, 2],
                       [0, 0, 1, 4]],
        "max": [[0, 0, 1, 2],
                [1, 7, 5, 0],
                [2, 3, 5, 6],
                [0, 6, 5, 2],
                [0, 6, 5, 6]],
    },
]


# ---------------------------------------------------------------------------
# 2. VECTOR HELPERS  (a "vector" is just a Python list of integers)
# ---------------------------------------------------------------------------
def vec_add(a, b):
    """Element-by-element addition: [1,2] + [3,4] = [4,6]."""
    return [x + y for x, y in zip(a, b)]


def vec_sub(a, b):
    """Element-by-element subtraction: [5,5] - [1,2] = [4,3]."""
    return [x - y for x, y in zip(a, b)]


def vec_leq(a, b):
    """True if EVERY element of a is <= the matching element of b."""
    return all(x <= y for x, y in zip(a, b))


def vec_str(v):
    """Format a vector for printing, e.g. [3 3 2]."""
    return "[" + " ".join(str(x) for x in v) + "]"


def flags_str(finish, names):
    """Format the Finish array, e.g. P0=F P1=T P2=F."""
    return " ".join(f"{p}={'T' if f else 'F'}" for p, f in zip(names, finish))


# ---------------------------------------------------------------------------
# 3. CORE COMPUTATIONS
# ---------------------------------------------------------------------------
def compute_need(max_matrix, allocation):
    """Need[i][j] = Max[i][j] - Allocation[i][j]."""
    return [vec_sub(max_matrix[i], allocation[i]) for i in range(len(allocation))]


def column_sums(matrix, m):
    """Sum each column (resource type) of a matrix."""
    sums = [0] * m
    for row in matrix:
        sums = vec_add(sums, row)
    return sums


def compute_available(total, allocation):
    """Available = Total - column sums of Allocation."""
    return vec_sub(total, column_sums(allocation, len(total)))


def safety_algorithm(allocation, need, available, names):
    """
    Banker's SAFETY ALGORITHM.

    Returns (is_safe, safe_sequence, trace)
      is_safe       -> True / False
      safe_sequence -> list of process names in the order they finish
      trace         -> list of text lines describing every step
    """
    n = len(allocation)
    work = available[:]              # Step 1: Work = Available (a copy)
    finish = [False] * n             #         Finish[i] = False for all i
    sequence = []
    trace = []

    trace.append(f"Step 1: Work = Available = {vec_str(work)}")
    trace.append(f"        Finish = {flags_str(finish, names)}")

    pass_no = 0
    while True:
        pass_no += 1
        found_in_this_pass = False
        trace.append("")
        trace.append(f"--- Pass {pass_no} ---")

        # Step 2: look for an unfinished process with Need <= Work
        for i in range(n):
            if finish[i]:
                continue             # already finished, skip it

            ok = vec_leq(need[i], work)
            trace.append(f"{names[i]}: Need {vec_str(need[i])} <= Work "
                         f"{vec_str(work)} ?  {'YES' if ok else 'NO'}")

            if ok:
                # Step 3: pretend the process finishes and returns
                #         everything it holds: Work = Work + Allocation
                new_work = vec_add(work, allocation[i])
                trace.append(f"    Work = {vec_str(work)} + Allocation "
                             f"{vec_str(allocation[i])} = {vec_str(new_work)}")
                work = new_work
                finish[i] = True
                sequence.append(names[i])
                found_in_this_pass = True
                trace.append(f"    Finish[{names[i]}] = True  ->  "
                             f"{flags_str(finish, names)}")
            else:
                trace.append(f"    {names[i]} must wait (not enough resources)")

        # Step 4: stop when all are finished or nothing changed this pass
        if all(finish):
            break
        if not found_in_this_pass:
            trace.append("No unfinished process can be satisfied in this pass.")
            break

    is_safe = all(finish)
    trace.append("")
    trace.append(f"Final Finish flags: {flags_str(finish, names)}")
    return is_safe, sequence, trace


def resource_request(allocation, max_matrix, available, pid, request, names):
    """
    Banker's RESOURCE-REQUEST ALGORITHM (extension).

    Returns a dictionary with:
      decision -> "GRANT", "WAIT" or "ERROR"
      reason   -> short explanation
      checks   -> text lines for the two checks
      tentative -> (allocation, need, available) after pretending to grant
      safety   -> (is_safe, sequence, trace) of the tentative state
    The caller decides whether to keep the tentative state (only on GRANT).
    """
    need = compute_need(max_matrix, allocation)
    result = {"checks": [], "tentative": None, "safety": None}

    # Check 1: Request <= Need  (cannot ask for more than the declared max)
    ok1 = vec_leq(request, need[pid])
    result["checks"].append(f"Check 1: Request {vec_str(request)} <= Need({names[pid]}) "
                            f"{vec_str(need[pid])} ?  {'YES' if ok1 else 'NO'}")
    if not ok1:
        result["decision"] = "ERROR"
        result["reason"] = (f"{names[pid]} asked for more than its maximum claim. "
                            "Request is rejected.")
        return result

    # Check 2: Request <= Available  (are the resources free right now?)
    ok2 = vec_leq(request, available)
    result["checks"].append(f"Check 2: Request {vec_str(request)} <= Available "
                            f"{vec_str(available)} ?  {'YES' if ok2 else 'NO'}")
    if not ok2:
        result["decision"] = "WAIT"
        result["reason"] = "Resources are not available right now. Process must wait."
        return result

    # Step 3: build the TENTATIVE state (pretend the request was granted)
    new_alloc = [row[:] for row in allocation]          # copy the matrix
    new_alloc[pid] = vec_add(allocation[pid], request)  # Allocation += Request
    new_avail = vec_sub(available, request)             # Available -= Request
    new_need = compute_need(max_matrix, new_alloc)      # Need -= Request
    result["tentative"] = (new_alloc, new_need, new_avail)

    # Step 4: is the tentative state safe?
    safety = safety_algorithm(new_alloc, new_need, new_avail, names)
    result["safety"] = safety
    if safety[0]:
        result["decision"] = "GRANT"
        result["reason"] = "Tentative state is SAFE. Request is granted."
    else:
        result["decision"] = "WAIT"
        result["reason"] = ("Tentative state is UNSAFE. Request is not granted; "
                            "state is rolled back and the process must wait.")
    return result


def validate_state(total, allocation, max_matrix):
    """Return a list of error messages (empty list means the data is valid)."""
    errors = []
    m = len(total)
    for i, (a_row, m_row) in enumerate(zip(allocation, max_matrix)):
        for j in range(m):
            if a_row[j] > m_row[j]:
                errors.append(f"P{i}: Allocation ({a_row[j]}) > Max ({m_row[j]}) "
                              f"for resource {resource_names(m)[j]}")
    sums = column_sums(allocation, m)
    for j in range(m):
        if sums[j] > total[j]:
            errors.append(f"Resource {resource_names(m)[j]}: allocated {sums[j]} "
                          f"but Total is only {total[j]}")
    return errors


# ---------------------------------------------------------------------------
# 4. SYSTEM STATE  (keeps the current data together)
# ---------------------------------------------------------------------------
def resource_names(m):
    """Resource type labels: A, B, C, ... (R1, R2 ... if more than 26)."""
    if m <= 26:
        return [chr(ord("A") + j) for j in range(m)]
    return [f"R{j + 1}" for j in range(m)]


class SystemState:
    def __init__(self, total, allocation, max_matrix):
        self.total = total
        self.allocation = allocation
        self.max = max_matrix
        self.n = len(allocation)                       # number of processes
        self.m = len(total)                            # number of resource types
        self.proc = [f"P{i}" for i in range(self.n)]   # P0, P1, ...
        self.res = resource_names(self.m)              # A, B, C, ...

    def need(self):
        return compute_need(self.max, self.allocation)

    def available(self):
        return compute_available(self.total, self.allocation)


# ---------------------------------------------------------------------------
# 5. OUTPUT / DISPLAY
# ---------------------------------------------------------------------------
LINE = "=" * 64
DASH = "-" * 64


def banner(title):
    print()
    print(LINE)
    print(" " + title)
    print(LINE)


def pause():
    try:
        input("\nPress Enter to return to the menu...")
    except EOFError:
        pass


def print_vector(label, vec, res):
    header = "  ".join(f"{r:>3}" for r in res)
    values = "  ".join(f"{v:>3}" for v in vec)
    print(f"{label:<12}{header}")
    print(f"{'':<12}{values}")


def print_state_table(state, need=None, allocation=None):
    """Print Allocation | Max | Need side by side, one row per process."""
    allocation = allocation if allocation is not None else state.allocation
    need = need if need is not None else compute_need(state.max, allocation)
    w = 3                                            # width of one number
    block = max(len(state.res) * (w + 1) - 1, 10)    # width of one block

    def row_text(vec):
        return f"{' '.join(f'{v:>{w}}' for v in vec):>{block}}"

    res_head = row_text(state.res)
    print(f"{'Process':<9}| {'Allocation':^{block}} | {'Max':^{block}} | {'Need':^{block}}")
    print(f"{'':<9}| {res_head} | {res_head} | {res_head}")
    print("-" * (9 + 3 * (block + 3)))
    for i in range(state.n):
        print(f"{state.proc[i]:<9}| {row_text(allocation[i])} | "
              f"{row_text(state.max[i])} | {row_text(need[i])}")


def show_state(state):
    banner("CURRENT SYSTEM STATE")
    print(f"Processes: {state.n}    Resource types: {state.m} "
          f"({', '.join(state.res)})\n")
    print_vector("Total", state.total, state.res)
    print()
    print_state_table(state)
    print()
    print("Need = Max - Allocation")
    print("Available = Total - column sums of Allocation")
    print(f"  Column sums of Allocation = "
          f"{vec_str(column_sums(state.allocation, state.m))}")
    print_vector("Available", state.available(), state.res)


def show_safety(state):
    banner("BANKER'S SAFETY ALGORITHM")
    need, avail = state.need(), state.available()
    print_vector("Total", state.total, state.res)
    print_vector("Available", avail, state.res)
    print()
    print_state_table(state)
    print()
    print(DASH)
    print(" STEP-BY-STEP TRACE")
    print(DASH)
    is_safe, seq, trace = safety_algorithm(state.allocation, need, avail, state.proc)
    for line in trace:
        print(line)
    print_result(is_safe, seq)


def print_result(is_safe, seq):
    print(DASH)
    if is_safe:
        print(" RESULT: SAFE STATE")
        print(" Safe sequence: < " + ", ".join(seq) + " >")
    else:
        print(" RESULT: UNSAFE STATE  (possible deadlock)")
        if seq:
            print(" Processes that could finish: " + ", ".join(seq))
        print(" No safe sequence exists for all processes.")
    print(DASH)


def show_request(state):
    banner("RESOURCE-REQUEST ALGORITHM")
    print_vector("Available", state.available(), state.res)
    print()
    print_state_table(state)
    print()

    pid = read_int(f"Requesting process number (0 to {state.n - 1}): ", 0, state.n - 1)
    request = read_vector(f"Request vector for {state.proc[pid]} "
                          f"({state.m} values for {' '.join(state.res)}): ", state.m)

    result = resource_request(state.allocation, state.max, state.available(),
                              pid, request, state.proc)
    print()
    print(DASH)
    print(f" {state.proc[pid]} requests {vec_str(request)}")
    print(DASH)
    for line in result["checks"]:
        print(line)

    if result["tentative"] is not None:
        new_alloc, new_need, new_avail = result["tentative"]
        print()
        print("Step 3: Tentative state (pretend the request is granted)")
        print(f"  Available  = Available - Request = {vec_str(new_avail)}")
        print(f"  Allocation({state.proc[pid]}) = Allocation + Request "
              f"= {vec_str(new_alloc[pid])}")
        print(f"  Need({state.proc[pid]})       = Need - Request "
              f"= {vec_str(new_need[pid])}")
        print()
        print_state_table(state, need=new_need, allocation=new_alloc)
        print()
        print("Step 4: Run the safety algorithm on the tentative state")
        print()
        is_safe, seq, trace = result["safety"]
        for line in trace:
            print(line)
        print_result(is_safe, seq)

    print()
    print(f" DECISION: {result['decision']}")
    print(f" {result['reason']}")
    print(DASH)

    if result["decision"] == "GRANT":
        state.allocation = result["tentative"][0]     # commit the new state
        print(" The system state has been UPDATED with this allocation.")
    else:
        print(" The system state was NOT changed.")


# ---------------------------------------------------------------------------
# 6. INPUT (with validation: the program never crashes on bad input)
# ---------------------------------------------------------------------------
def read_line(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("\nInput ended. Goodbye.")
        sys.exit(0)


def read_int(prompt, low, high):
    while True:
        text = read_line(prompt).strip()
        if text.lstrip("-").isdigit():
            value = int(text)
            if low <= value <= high:
                return value
        print(f"  ! Please enter a whole number from {low} to {high}.")


def read_vector(prompt, m):
    """Read m non-negative integers separated by spaces or commas."""
    while True:
        parts = read_line(prompt).replace(",", " ").split()
        if len(parts) != m:
            print(f"  ! Enter exactly {m} numbers (you entered {len(parts)}).")
            continue
        if not all(p.isdigit() for p in parts):
            print("  ! Use whole numbers that are 0 or greater only.")
            continue
        return [int(p) for p in parts]


def read_matrix(title, n, m, res, lower=None):
    """Read an n x m matrix one process (row) at a time.
    If 'lower' is given, every value must be >= the matching value in it
    (used so that Max is never smaller than Allocation)."""
    print(f"\nEnter the {title} matrix ({m} values per process: {' '.join(res)})")
    matrix = []
    for i in range(n):
        while True:
            row = read_vector(f"  P{i}: ", m)
            if lower is not None and not vec_leq(lower[i], row):
                print(f"  ! Max must be >= Allocation {vec_str(lower[i])} for P{i}.")
                continue
            matrix.append(row)
            break
    return matrix


def enter_new_state():
    banner("ENTER NEW SYSTEM STATE")
    n = read_int("Number of processes (1-20): ", 1, 20)
    m = read_int("Number of resource types (1-10): ", 1, 10)
    res = resource_names(m)

    total = read_vector(f"Total vector ({m} values for {' '.join(res)}): ", m)

    while True:
        allocation = read_matrix("Allocation", n, m, res)
        sums = column_sums(allocation, m)
        if not vec_leq(sums, total):
            print(f"  ! Column sums of Allocation {vec_str(sums)} exceed Total "
                  f"{vec_str(total)}. Please re-enter the Allocation matrix.")
            continue
        break

    max_matrix = read_matrix("Max", n, m, res, lower=allocation)

    state = SystemState(total, allocation, max_matrix)
    print("\nData saved.")
    show_state(state)
    return state


def load_preset():
    banner("LOAD SAMPLE DATA SET")
    for k, p in enumerate(PRESETS, start=1):
        print(f"  {k}. {p['name']}")
    choice = read_int(f"Choose 1-{len(PRESETS)}: ", 1, len(PRESETS))
    p = PRESETS[choice - 1]
    state = SystemState(p["total"][:],
                        [row[:] for row in p["allocation"]],
                        [row[:] for row in p["max"]])
    errors = validate_state(state.total, state.allocation, state.max)
    if errors:                                    # safety net for edited presets
        print("Preset data is invalid:")
        for e in errors:
            print("  - " + e)
        return None
    print(f"\nLoaded: {p['name']}")
    show_state(state)
    return state


# ---------------------------------------------------------------------------
# 7. MAIN MENU
# ---------------------------------------------------------------------------
def main():
    state = None
    while True:
        banner("BANKER'S ALGORITHM SIMULATOR  (Deadlock Avoidance)")
        if state is None:
            print(" Current data: (none loaded yet)")
        else:
            print(f" Current data: {state.n} processes, {state.m} resource types")
        print()
        print(" 1. Enter new system state")
        print(" 2. Load sample data set")
        print(" 3. Show system state (Total, Allocation, Max, Need, Available)")
        print(" 4. Run Safety Algorithm")
        print(" 5. Resource Request (GRANT / WAIT)")
        print(" 6. Exit")
        choice = read_int("\nSelect an option: ", 1, 6)

        if choice == 6:
            print("\nThank you for using the Banker's Algorithm Simulator.")
            break
        if choice == 1:
            state = enter_new_state()
        elif choice == 2:
            state = load_preset() or state
        elif state is None:
            print("\n  ! No data yet. Choose option 1 or 2 first.")
        elif choice == 3:
            show_state(state)
        elif choice == 4:
            show_safety(state)
        elif choice == 5:
            show_request(state)
        pause()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram stopped by user. Goodbye.")