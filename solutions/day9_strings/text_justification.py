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
        pass


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
