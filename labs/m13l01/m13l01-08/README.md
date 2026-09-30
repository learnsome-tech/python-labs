# m13l01-08 · A block can hold several statements

**Lesson:** [Conditions And Simple If Statements](https://learnsome.tech/learn/python-course/m13l01) (lesson 13.1, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can write a condition, say whether it is True or False, and use a simple if statement to run a block of code only when the condition holds.

In the lesson: The body is not limited to a single statement. Here is a fragment from a banking program. The heading tests whether the balance has gone negative. There are four lines indented under it, and all four run together, or none of them do. The assumption is that if an account goes negative it is brought back to zero by moving money across from a backup account. Notice that a comment sits happily inside the block at the same indentation. This is a fragment, not a whole program, so there is nothing to run here; the variables would be defined somewhere above it.

## Files

- [`starter/backup.py`](starter/backup.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backup.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: the heading tests
   - Lines 2–5: four lines indented under it

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l01-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
