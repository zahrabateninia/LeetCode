# Dynamic Programming (DP)

## What is it?

Dynamic programming is a technique for solving problems by breaking them into **smaller overlapping subproblems**, solving each subproblem **only once**, and **storing the result** so it can be reused instead of recomputed.

> Think of it as "recursion + memory", or "brute force that remembers what it already did".

---

## When does DP apply?

A problem is a good fit when it has both of these properties:

1. **Overlapping subproblems**: the same smaller problem shows up many times.
   Example: `fib(5)` needs `fib(4)` and `fib(3)`, and `fib(4)` also needs `fib(3)`.
2. **Optimal substructure**: the answer to the big problem can be built from the answers to smaller problems.

If subproblems don't overlap, plain divide and conquer (e.g. merge sort) is enough. DP is not needed.

### Common signals in a problem statement

- "Count the number of ways to..."
- "Find the minimum / maximum / longest / shortest..."
- "Is it possible to...?"
- Choices at each step (take or skip, go left or right) where earlier choices affect later ones.

---

## The two styles

### 1. Top-down (Memoization)

Write the natural recursive solution, then add a cache.

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

- Easy to write: it mirrors the recurrence directly.
- Only computes the subproblems that are actually needed.
- Costs recursion stack space.

### 2. Bottom-up (Tabulation)

Start from the smallest cases and fill a table up to the answer.

```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

- No recursion, so no stack overflow.
- Often easier to optimize for space (see below).

### Space optimization

If `dp[i]` only depends on the last one or two entries, keep only those:

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

---

## Why DP is faster

Naive recursive Fibonacci recomputes the same values over and over: **O(2^n)** time.
With DP each value is computed once: **O(n)** time.

```
Naive:                    With DP:
        fib(5)                    fib(5)
       /      \                   /    \
   fib(4)    fib(3)           fib(4)  fib(3) <- reused
   /   \      /   \
fib(3) fib(2) fib(2) fib(1)
```

---

## How to solve a DP problem (step by step)

1. **Define the state.** What does `dp[i]` (or `dp[i][j]`) mean? Be precise.
2. **Write the recurrence.** How does a state depend on smaller states?
3. **Set the base cases.** The smallest states whose answers you know directly.
4. **Choose the order.** Bottom-up: fill so dependencies are computed first. Top-down: recurse and cache.
5. **Find the answer.** Which state holds the final result? (`dp[n]`, `max(dp)`, `dp[m][n]`, ...)
6. **Optimize space** if the recurrence only looks back a fixed number of steps.

---

## Example: Pascal's Triangle

**State:** `triangle[i][j]` is the value at row `i`, column `j`.
**Recurrence:** `triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]`
**Base case:** the first and last element of every row is `1`.

```python
def generate(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)              # ends are already 1

        for j in range(1, i):            # fill only the middle
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
```

- **Time:** O(n²)
- **Space:** O(n²) (the output itself)

---

## Common DP patterns

| Pattern | Typical state | Example problems |
|---|---|---|
| 1D linear | `dp[i]` = best answer up to index `i` | Climbing Stairs, House Robber, Fibonacci |
| 2D grid | `dp[i][j]` = answer at cell `(i, j)` | Unique Paths, Min Path Sum, Pascal's Triangle |
| Knapsack | `dp[i][w]` = best using first `i` items with capacity `w` | 0/1 Knapsack, Coin Change, Partition Equal Subset Sum |
| Subsequence / strings | `dp[i][j]` over two strings | LCS, Edit Distance, Longest Increasing Subsequence |
| Interval | `dp[i][j]` = answer for subarray `i..j` | Burst Balloons, Palindromic Substrings |

---

## DP vs. other approaches

| Approach | Idea | Reuses subproblems? |
|---|---|---|
| Brute force / plain recursion | Try everything | No |
| Divide and conquer | Split into independent subproblems | No |
| **Dynamic programming** | Split into overlapping subproblems, cache results | **Yes** |
| Greedy | Take the locally best choice, never reconsider | N/A (no table) |

---

## Quick checklist

- [ ] Can I describe the problem in terms of smaller versions of itself?
- [ ] Do the same subproblems repeat?
- [ ] Can I define `dp[...]` clearly in one sentence?
- [ ] Do I have the recurrence and base cases?
- [ ] Can I reduce the space?

---
