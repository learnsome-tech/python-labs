# m13l03-06 · A chain with no else at all

**Lesson:** [If Elif Chains](https://learnsome.tech/learn/python-course/m13l03) (lesson 13.3, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can write an if elif else chain to sort a value into any number of cases, and explain why only the first true test matters.

In the lesson: There is one more shape. You may end a chain after the last elif and leave the else out. It is then like a simple if without an else: it is possible for no block at all to be executed, which happens when every test is false. Here the program complains only when there is something wrong with the weight. Over one hundred and twenty pounds it refuses the case, over fifty it charges, and a suitcase under fifty pounds prints nothing. So remember the pair of rules. With a final else, exactly one block runs. Without one, at most one block runs.

## Files

- [`starter/weightCheck.py`](starter/weightCheck.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/weightCheck.py` alongside the lesson.
2. Notes from the lesson:
   - Line 3: no else after this block, so a light suitcase prints nothing

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
