"""
Maximum Candies You Can Get from Boxes — LC 1298.

You have `n` boxes, given as parallel arrays of length n:
- status[i]: 1 if box i is open, 0 if closed
- candies[i]: candies inside box i
- keys[i]: list of box indices — keys found inside box i (each opens that box)
- containedBoxes[i]: list of box indices found inside box i

You start by possessing every box in `initialBoxes`. You can open a box and
collect its candies/keys/contained-boxes only once you both **possess** it
and it is **open** (status 1, or opened later via a found key). Opening a
box may reveal new boxes you now possess (still possibly locked) and new
keys (which may retroactively unlock a box you already possess but
couldn't open yet).

Return the maximum total candies obtainable.

Pattern: BFS with dynamic unlocking — a box becomes processable once two
independent conditions are both met (possessed AND open), and finding a
key for an already-possessed-but-locked box must requeue it.
"""

from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()

    print(
        sol.maxCandies(
            status=[1, 0, 1, 0],
            candies=[7, 5, 4, 100],
            keys=[[], [], [1], []],
            containedBoxes=[[1, 2], [3], [], []],
            initialBoxes=[0],
        )
    )
    # expect 16  (open box0: +7, get boxes 1,2; box1 locked, box2 open: +4,
    # get key to box1; now box1 opens: +5; box3 found but never unlocked)

    print(
        sol.maxCandies(
            status=[1, 0, 0, 0, 0, 0],
            candies=[1, 1, 1, 1, 1, 1],
            keys=[[1, 2, 3, 4, 5], [], [], [], [], []],
            containedBoxes=[[1, 2, 3, 4, 5], [], [], [], [], []],
            initialBoxes=[0],
        )
    )
    # expect 6  (box0 gives keys+boxes for everything else)

    print(
        sol.maxCandies(
            status=[1, 1, 1],
            candies=[100, 1, 100],
            keys=[[], [0, 2], []],
            containedBoxes=[[], [], []],
            initialBoxes=[0],
        )
    )
    # expect 100  (boxes 1,2 are open but you never possess them)
