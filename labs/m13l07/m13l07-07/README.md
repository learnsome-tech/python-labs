# m13l07-07 · Return stops the loop and the function

**Lesson:** [Loops And Tuples](https://learnsome.tech/learn/python-course/m13l07) (lesson 13.7, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can package related values in a tuple, unpack a tuple in a for loop heading, and replace a long repetitive if elif statement with a loop over a list of tuples.

In the lesson: There is still a problem. We could test each rectangle inside the loop, but the original if elif statement stopped at the first true condition, whereas a for statement walks all the way through the sequence. In a function there is a simple way out. A return statement always ends the execution of a function, so once the rectangle containing the point is found, the function can return the answer immediately. Notice where the default went: the old else clause has become the statement after the loop, reached only when no condition inside was true. This function works for a list of any length and never mentions the rectangles by name.

## Files

- [`starter/chooseButton2.py`](starter/chooseButton2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/chooseButton2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: walks all the way through
   - Lines 9–10: can return the answer immediately
   - Lines 11: after the loop

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l07-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
