# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# a variation of the Fibonacci sequence :)




def climbStairs(n: int) -> int:
    prev1, prev2 = 1, 1

    for _ in range(2, n + 1):
        prev1, prev2 = prev2, prev1 + prev2

    return prev2