"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this (numRows = 3):

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that takes a string and makes this conversion given a
number of rows.

numRows == 1 should just return s unchanged.
"""

from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.convert("PAYPALISHIRING", 3))
    # expect "PAHNAPLSIIGYIR"

    print(sol.convert("PAYPALISHIRING", 4))
    # expect "PINALSIGYAHRPI"

    print(sol.convert("A", 1))
    # expect "A"
