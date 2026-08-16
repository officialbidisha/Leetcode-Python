"""
Given a list of words and a target line width maxWidth, format the text
into lines that are fully (left and right) justified.

Pack as many words per line as possible greedily. Then pad each line so
it's exactly maxWidth characters:
- For a line with more than one word, distribute extra spaces as evenly
  as possible between words; if it doesn't divide evenly, the leftmost
  gaps get one extra space each.
- The last line, and any line with only one word, is left-justified:
  words separated by a single space, padded with trailing spaces to
  maxWidth.
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        currentSentence = []
        wordCount = 0

        def distributeSpace(currentSentence):
            print("Current Sentence", currentSentence)
            totalLength = sum(len(word) for word in currentSentence)
            remainingSpaces = maxWidth - totalLength
            gaps = len(currentSentence) - 1

            # single word on the line: no gaps to divide into, so it's just
            # the word plus all the slack as trailing padding
            if gaps == 0:
                return currentSentence[0] + " " * remainingSpaces

            equalDistribution = remainingSpaces // gaps
            extra = remainingSpaces % gaps

            finalSentence = ""
            # words before the last one: equal share of spaces, leftmost `extra` gaps get +1
            for i in range(gaps):
                # gap indices run left to right (0, 1, 2, ...), and extra < gaps always,
                # so "i < extra" is only true for the first `extra` gaps — i.e. the leftmost
                # ones. every gap gets the base amount; those leftmost gaps get +1 on top.
                spacesHere = equalDistribution + (1 if i < extra else 0)
                finalSentence += currentSentence[i] + " " * spacesHere

            # the last word, handled separately: no trailing gap-space follows it
            finalSentence += currentSentence[-1]
            return finalSentence

        for word in words:
            currentWordLength = len(word)
            currentSentenceLength = sum(len(w) for w in currentSentence)
            neededSpaces = len(currentSentence)  # one space before this word, unless line is empty # how many words already sitting in the line: how many single space gaps
            if currentWordLength + neededSpaces + currentSentenceLength <= maxWidth:
                currentSentence.append(word)
                wordCount += 1
            else:
                res.append(distributeSpace(currentSentence))
                wordCount = 1
                currentSentence = [word]

        # flush the last line: left-justified, single spaces, padded on the right
        print("Last Sentence", currentSentence)
        lastLine = " ".join(currentSentence)
        lastLine += " " * (maxWidth - len(lastLine))
        res.append(lastLine)

        return res


if __name__ == "__main__":
    sol = Solution()

    def show(lines):
        for line in lines:
            print(f"|{line}|")
        print()

    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    show(sol.fullJustify(words1, 16))
    # expect [
    #   "This    is    an",
    #   "example  of text",
    #   "justification.  ",
    # ]

    words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
    show(sol.fullJustify(words2, 16))
    # expect [
    #   "What   must   be",
    #   "acknowledgment  ",
    #   "shall be        ",
    # ]

    words3 = [
        "Science", "is", "what", "we", "understand", "well", "enough", "to",
        "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
        "we", "do",
    ]
    show(sol.fullJustify(words3, 20))
