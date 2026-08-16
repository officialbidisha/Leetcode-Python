# Leetcode-Python

Python solutions to LeetCode-style DSA problems, written while learning
Python (coming from JavaScript) through hands-on practice.

## Structure

Each `solutions/dayN_*` folder groups problems by the pattern they cover.
Every solution file follows the same shape: a `Solution` class with the
method(s) to implement, and a `if __name__ == "__main__":` block with
test cases you can run directly, e.g.:

```
python3 solutions/day1_basics/two_sum.py
```

| Folder | Focus |
|---|---|
| `day1_basics` | Arrays, hashing |
| `day2_graphs` | BFS/DFS on grids, BFS with dynamic state-unlocking |
| `day8_intervals` | Interval/range problems, DP + binary search on sorted boundaries |
| `day9_strings` | String simulation, greedy line-packing |

More folders get filled in as practice continues.

## Progress

| Folder | File | Problem | Status |
|---|---|---|---|
| `day1_basics` | `two_sum.py` | Two Sum (LC 1) | done |
| `day1_basics` | `contains_duplicate.py` | Contains Duplicate (LC 217) | done |
| `day1_basics` | `contains_duplicate_ii.py` | Contains Duplicate II (LC 219) | done |
| `day1_basics` | `group_anagrams.py` | Group Anagrams (LC 49) | done |
| `day1_basics` | `top_k_frequent.py` | Top K Frequent Elements (LC 347) | done |
| `day1_basics` | `valid_anagram.py` | Valid Anagram (LC 242) | todo |
| `day1_basics` | `single_number.py` | Single Number (LC 136) | todo |
| `day1_basics` | `happy_number.py` | Happy Number (LC 202) | todo |
| `day1_basics` | `product_except_self.py` | Product of Array Except Self (LC 238) | todo |
| `day2_graphs` | `single_source_bfs.py` | Generic single-source BFS warm-up | done |
| `day2_graphs` | `rotting_oranges.py` | Rotting Oranges (LC 994) | todo |
| `day2_graphs` | `max_candies_from_boxes.py` | Max Candies from Boxes (LC 1298) | in progress |
| `day8_intervals` | `split_stay.py` | Split-Stay Listing Pairs (custom) | done |
| `day8_intervals` | `job_scheduling.py` | Maximum Profit in Job Scheduling (LC 1235) | done |
| `day9_strings` | `text_justification.py` | Text Justification (LC 68) | done |
| `day9_strings` | `print_sentences_as_table.py` | Print Sentences as Table (Text Justification variant) | done |
| `day9_strings` | `zigzag_conversion.py` | Zigzag Conversion (LC 6) | todo |

**10 done, 6 todo (1 in progress).**

## Prep notes

[`GENERIC_DSA_CHEATSHEET.md`](GENERIC_DSA_CHEATSHEET.md) — a generic senior
SWE 45-min coding-round prep doc (problem list, patterns, timed study plan).

## Requirements

Python 3, standard library only — no external dependencies.
