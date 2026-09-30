# m13l03-03 · The same function with elif

**Lesson:** [If Elif Chains](https://learnsome.tech/learn/python-course/m13l03) (lesson 13.3, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can write an if elif else chain to sort a value into any number of cases, and explain why only the first true test matters.

In the lesson: Here is the same function from the example program grade one dot py. The first test is unchanged. After that, each else and if pair collapses into a single word, elif, so the indentation never grows. The tests are all aligned down the left, and the blocks under them are all indented by the same amount. The final else catches everything none of the tests caught. Be careful of the odd Python contraction: it is elif, not elseif. Getting that wrong is a syntax error, and it is a mistake almost everyone makes at least once.

## Files

- [`starter/grade1.py`](starter/grade1.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/grade1.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: the first test is unchanged
   - Lines 4–9: each else and if pair collapses
   - Lines 10–12: the final else catches everything
3. Notes from the lesson:
   - Line 1: if, elif, elif, elif, else: all at the same indentation

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
