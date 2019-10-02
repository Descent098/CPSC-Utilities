# Tower of Hanoi

The tower of hanoi is a Vedic puzzle in which there 3 pillars (typically labeled A, B, and C) there are an arbitrary number of discs (*n*) stacked in ascending order by size on one of the pillars (usually A).

Looks something like this:

![Tower of Hanoi](https://miro.medium.com/max/558/1*VtB0QS-7iB6RSJ0yS5PQ2g.jpeg)

The goal of the game is to take the contents of pillar A to pillar C, but with these three rules:

1. You may only move 1 disc at a time
2. You can only move a disc to an empty stack, or on top of an existing stack
3. Discs **MUST** be stacked in ascending order (bigger ones on the bottom) at all times

## Solution

This problem is commonly used to show off recursion because the recursive solution is significantly simpler than the [iterative](https://cs.stackexchange.com/questions/96624/how-to-solve-tower-of-hanoi-iteratively/96669)

See ```solution.py``` for a recursive solution to the problem implemented in python.
See ```solution.go``` for a recursive solution to the problem implemented in go.
see ```solution.java``` for a recursive solution to the problem implemented in java

With this problem the solution can always be found in (2^n)-1 where n is the amount of discs on the initial pillar.
