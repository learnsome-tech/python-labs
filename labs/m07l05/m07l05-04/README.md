# m07l05-04 · Two steps combined into one

**Lesson:** [Accumulation Loops](https://learnsome.tech/learn/python-course/m07l05) (lesson 7.5, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can build a loop that accumulates a result, choose the right initial value for the accumulator, and recognise from an English description when a loop through a sequence is needed.

In the lesson: Sometimes the two general loop steps can be combined, and this is such a case. Next sum is used only once, on the very next line, so we can substitute it away and simplify. What is left is one statement in the body: sum is assigned sum plus num. The right hand side is worked out first, using the value sum has now, and the result is stored straight back into the same variable. So the running total does the work and the handover at once. Fewer moving parts means fewer places to be wrong, but do make sure you can see why this shorter version does the same thing as the longer one.

## Files

- [`starter/two-steps-combined-into-one.py`](starter/two-steps-combined-into-one.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/two-steps-combined-into-one.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
