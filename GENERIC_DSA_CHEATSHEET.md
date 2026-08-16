# Senior SWE — 45 min Coding Round Prep

Compiled 2026-08-15 from public interview-experience aggregator sites. See
"Sources & confidence" at the bottom. **Nothing here is an insider leak.** It
is the intersection of several independent aggregators + candidate reports.
Treat Tier 1 as "high prior", not "guaranteed".

---

## 1. What the round actually is

A 45-min slot is almost certainly the **technical phone screen** on CoderPad.

Consistently reported across sources:

- **One problem**, medium-hard to hard. Occasionally a warm-up + main problem.
- **Real, running code.** Pseudocode is not accepted. Your code is expected
  to compile and pass the interviewer's test cases in the pad.
- **You are not required to fully finish** a hard one — getting close with clean
  reasoning passes. But the code you *do* write must be real.
- This company runs a **small, stable question bank**. Targeted prep has
  unusually high ROI here compared to companies with huge rotating banks.
- Many problems are **domain-flavoured**: marketplace listings, bookings, date
  ranges, providers, payments. Same algorithms, wrapped in product language.
  Expect to spend the first 5 minutes translating a wordy product prompt into
  a clean data model. *This is graded.* Ask clarifying questions before coding.
- Follow-ups mutate the requirements ("now the listing can have gaps", "now
  support a third listing"). Structure your code so it can absorb one.

Level note: the second coding round in the onsite was replaced by a **code
review round** in 2024. Not your problem this week, but don't be surprised
later.

---

## 2. Tier 1 — drill these first (highest convergence across sources)

Ordered by confidence, highest first.

| # | Problem | Pattern |
|---|---------|---------|
| 1 | **Split-stay listing pairs** (company-original, see §3) | intervals + hashing |
| 2 | **Text Justification** — LC 68 (variants: "Print Sentences as Table", "Text Layout and Query Parsing") | string simulation, off-by-one hell |
| 3 | **Maximum Profit in Job Scheduling** — LC 1235 | DP + binary search on intervals |
| 4 | **Pour Water** — LC 755 ("water drop", "raindrops") | array simulation |
| 5 | **Maximum Candies You Can Get from Boxes** — LC 1298 | BFS with state unlocking |
| 6 | **Flatten Nested List Iterator w/ `remove()`** — LC 341 / LC 251 variant ("List of List Iterator") | iterator design, lazy eval |
| 7 | **Cheapest Flights Within K Stops** — LC 787 ("Flight Connections") | Bellman-Ford / Dijkstra+k |
| 8 | **Alien Dictionary** — LC 269 | topological sort |
| 9 | **Palindrome Pairs** — LC 336 | trie / hashing |
| 10 | **Combination Sum** — LC 39, as "Menu Combination Sum" (prices, target total) | backtracking w/ dedup |

**If you only have time for five: 1, 2, 3, 4, 5.**

Number 1 and 2 are the two I would bet on hardest. #1 because it's an original
problem for this company, recent, and repeated; #2 because every aggregator
puts it at the top and it has spawned two 2026 variants.

---

## 3. The split-stay problem, stated properly

Worth writing out because it's the one you can't just look up on LeetCode.
(A working solution to this, fully tested, lives in this repo under
`solutions/day8_intervals/split_stay.py`.)

> Each listing has availability as a sorted list of day integers.
> Given an inclusive requested range `[S, E]`, return every unordered pair of
> listings `(X, Y)` such that there exists a split point `T`, `S ≤ T < E`, where
> X covers `S..T` **consecutively** and Y covers `T+1..E` **consecutively**.
>
> Example: `A -> [1,2,3,6,7,10,11]`, `B -> [3,4,5,6,8,9,10,13]`, `C -> [7,8,9,10,11]`
> Range `[3, 11]` → valid pair is `(B, C)`.
>
> Return each pair once. Beat `O(L² · R)` where L = #listings, R = range length.

Edge cases the interviewer will push on: missing boundary days; both listings
covering the whole range (still one pair, not two); identical availability;
no valid pair; `S == E`.

The intended shape: for each listing, compute the set of split points `T` it can
serve as a *prefix* for, and the set it can serve as a *suffix* for. Then bucket
listings by `T` and pair prefix-set against suffix-set. Don't brute-force pairs.

Related variants also logged: "Find pairs to cover a split stay", "Find valid
split-stay listing combinations" (Hard), "Minimize exact layover bookings",
"Minimum canisters to hit an exact target" — the last two are the same family
as coin-change / exact-sum.

---

## 4. Tier 2 — skim, don't grind

Recognise the shape, sketch the approach, move on. Only code these if Tier 1 is done.

- **Trapping Rain Water** — LC 42
- **Smallest Common Region** — LC 1257 (lowest common ancestor in disguise)
- **Design Excel Sum Formula** — LC 631 (dependency graph + recompute)
- **Linked list intersection where either list may have a cycle** — nastier than LC 160
- **Round Prices** — round a list of prices to integers minimising total error while preserving the sum
- **Pagination / Display Page** — reorder search results so one provider doesn't dominate a page
- **Sliding Puzzle** — LC 773 (BFS on board states)
- **Word Search II** — LC 212, **Merge k Sorted Lists** — LC 23, **Regular Expression Matching** — LC 10
- **Min Cost / K-stops flight routing**, **Boggle**, **K-Edit Distance**, **CSV Parser**, **IP Range to CIDR**
- **Connect Four**, **Design a Banking System**, **Design a Translation System**
- **Infection spread time on a grid** — multi-source BFS, i.e. Rotting Oranges++

---

## 5. Your sprint plan (compressed — updated 2026-08-16)

Interview timeline moved up — now roughly 3-4 prep sessions left at ~1-2
hrs/day. Re-prioritized below against **actual** progress (not stale
checkboxes elsewhere):

**Already solid:** Two Sum, Contains Duplicate (+II), Group Anagrams, Top K
Frequent, Split-stay, Text Justification (done twice), Print Sentences as
Table (Text Justification variant, extra rep).

**Highest risk — zero progress so far:** LC 1298 (Tier 1 #5 above) and LC 631.
Note the discrepancy: this file's aggregator tiering puts 631 in Tier 2
("skim, don't grind" — §4), but a separate frequency count from a tagged-
question list calls 1298 and 631 "tied as the most-reported items."
Trusting the more concrete signal — treat 631 as must-do, not skim.

### Session 1 (today) — finish what's in flight, hit the top untouched risk
- LC 1235 Maximum Profit in Job Scheduling — finish (already in progress). 35 min.
- LC 1298 Maximum Candies from Boxes — highest-priority untouched item. 35 min.

### Session 2 — the other flagged-critical item, plus cheap wins
- LC 631 Design Excel Sum Formula. 35-40 min. Lowest acceptance rate (39.5%)
  of anything on this list — expect more edge cases (circular refs, ranges)
  than the Hard label alone suggests.
- Single Number, Happy Number — closes out Day 1's last two stubs. 10 min each.

### Session 3 — must-know two-pointer / sliding-window reps
- LC 76 Minimum Window Substring. 30 min.
- LC 42 Trapping Rain Water. 30 min.

### Day before (if it lands) — pressure + polish, no new problems
- One full 45-min mock under real conditions: talk out loud, no IDE
  autocomplete, no running until you think you're done.
- Timed cold re-solve of 2-3 already-done problems, 25 min each.
- Last hour: review your syntax/idiom notes and "Rules for the reps" below,
  not new problems.

### Rules for the reps
- **Type in a plain editor.** CoderPad has no autocomplete and no Copilot.
- **Narrate.** Communication and requirement-clarification are weighted heavily.
- **Write your own test cases before you claim done.** They will ask you to run it.
- Coming from JS: pre-load `collections.defaultdict`, `deque`, `heapq`,
  `bisect.bisect_left/right` — `sortedcontainers` is *not* available on CoderPad.
  Know `functools.lru_cache` and `@cache` for DP memoisation.

---

## 6. Sources & confidence

**High confidence** (multiple independent sources agree):
- Round format, 45–60 min, one hard problem, running code required, small question bank
- Text Justification, Job Scheduling, Pour Water, Cheapest Flights, Alien Dictionary,
  Palindrome Pairs, nested-list iterator as long-standing bank items

**Medium confidence** (single credible source, or recent aggregator log):
- Specific dates on individual aggregator entries
- LC 631 and LC 1298 named explicitly by one guide
- Split-stay wording in §3 — reconstructed from an aggregator's problem statement,
  not from an actual interviewer

**Low confidence / explicitly discount:**
- Some aggregators show "frequency %" figures that are actually a relevance
  score, not literal frequency. Used only for *ordering*, not as odds.
- An older list circulating on forums (Minimum Window Substring, etc.) — the
  commenter themself said "haven't been there in 6 years."

Source sites used (homepages only — the company-tagged pages used for
research aren't linked here on purpose):
- hellointerview.com
- prachub.com
- stealthcoder.app
- teamblind.com
- codingkaro.in
- github.com (search interview-experience repos)
- spacecomplexity.ai
- aonecode.com
