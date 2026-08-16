"""
Print Sentences as Table — domain-flavored variant of Text Justification
(LC 68), logged by prachub as an Airbnb screen question (Feb 2026).

Given a list of words and a fixed tableWidth, lay them out as rows of a
table: pack words into a row greedily (never split a word across rows,
and every word individually fits within tableWidth). Unlike Text
Justification, do NOT distribute extra space evenly between words —
every row (not just the last) is left-justified: words joined by a
single space, then padded with trailing spaces out to tableWidth.

This drops the space-distribution logic entirely and keeps only the
greedy line-packing half of Text Justification — the point of this rep
is noticing that a table's column borders already do the visual
alignment work, so stretching spaces to fill the row isn't needed here.
"""

from typing import List


class Solution:
    def printSentencesAsTable(self, words: List[str], tableWidth: int) -> List[str]:
        res = []
        currentSentence = []
        for word in words:
            currentWordLength = len(word)
            # if this word gets appended, currentSentence goes from k words to
            # k+1, which means k internal gaps — one space per already-placed word
            spacesNeeded = len(currentSentence)
            currentSentenceLength = 0
            for w in currentSentence:
                currentSentenceLength += len(w)
            if currentSentenceLength + spacesNeeded + currentWordLength <= tableWidth:
                currentSentence.append(word)
            else:
                # word doesn't fit: close out currentSentence as its own row.
                # unlike Text Justification, no space distribution — always a
                # single space between words, with all slack dumped as
                # trailing padding (this row behaves like Text Justification's
                # "last line" case, every time)
                sentence = ""
                gaps = len(currentSentence) - 1  # gaps *within* the closed row (no new word added)
                spacesLeft = tableWidth - (currentSentenceLength + gaps)
                for i in range(gaps):
                    sentence += currentSentence[i] + " "
                sentence += currentSentence[-1]
                sentence += " " * spacesLeft
                res.append(sentence)
                currentSentence = [word]  # the word that didn't fit starts the next row

        # the last row never triggers the else branch above (no further word
        # ever fails to fit into it, since the loop just ends), so it has to
        # be flushed here the same way — single-spaced, padded to tableWidth
        lastline = " ".join(currentSentence)
        lastline += " " * (tableWidth - len(lastline))
        res.append(lastline)
        return res


if __name__ == "__main__":
    sol = Solution()

    def show(rows):
        for row in rows:
            print(f"|{row}|")
        print()

    words1 = ["This", "is", "an", "example", "of", "printing", "words", "as", "a", "table"]
    show(sol.printSentencesAsTable(words1, 10))
    # expect [
    #   "This is an",
    #   "example of",
    #   "printing  ",
    #   "words as a",
    #   "table     ",
    # ]

    words2 = ["A", "single", "long", "row"]
    show(sol.printSentencesAsTable(words2, 20))
    # expect ["A single long row   "]

    words3 = ["one"]
    show(sol.printSentencesAsTable(words3, 5))
    # expect ["one  "]
