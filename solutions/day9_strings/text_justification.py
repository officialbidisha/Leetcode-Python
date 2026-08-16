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
            totalLength = 0
            totalWord = len(currentSentence)
            finalSentence = ""
            for word in currentSentence:
                totalLength += len(word)
            remainingSpaces = maxWidth - totalLength
            gaps = totalWord - 1
            if gaps == 0:
                # single word on the line: no gaps to distribute into (avoids
                # divide-by-zero below), so dump all leftover space after the word
                equalDistribution = remainingSpaces
                extra = 0
            else:
                equalDistribution = remainingSpaces // gaps
                extra = remainingSpaces % gaps
            # words before the last one: equal share of spaces, leftmost `extra` gaps get +1
            for i in range(gaps):
                # gap indices run left to right (0, 1, 2, ...), and extra < gaps always,
                # so "i < extra" is only true for the first `extra` gaps — i.e. the leftmost
                # ones. every gap gets the base amount; those leftmost gaps get +1 on top.
                spacesHere = equalDistribution + (1 if i < extra else 0)
                finalSentence += currentSentence[i] + " " * spacesHere

            # the last word, handled separately: no trailing gap-space follows it
            finalSentence += currentSentence[-1]

            # single-word line: no gaps existed above, so pad after the word here
            if gaps == 0:
                finalSentence += " " * equalDistribution
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
        lastLine = " ".join(currentSentence)
        lastLine += " " * (maxWidth - len(lastLine))
        res.append(lastLine)

        return res


if __name__ == "__main__":
    sol = Solution()

    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    print(sol.fullJustify(words1, 16))
    # expect [
    #   "This    is    an",
    #   "example  of text",
    #   "justification.  ",
    # ]

    words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
    print(sol.fullJustify(words2, 16))
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
    print(sol.fullJustify(words3, 20))
