# m13l07-04 · The most egregious repetition

**Lesson:** [Loops And Tuples](https://learnsome.tech/learn/python-course/m13l07) (lesson 13.7, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can package related values in a tuple, unpack a tuple in a for loop heading, and replace a long repetitive if elif statement with a loop over a list of tuples.

In the lesson: Now back to improving the program, which has similar code repeating in several places. This is the most egregious example. The click is awaited, then a long if statement asks which button was hit, and finally the shape is filled. This whole if statement is repeated once for every shape the user colours, and all the conditions inside it are nearly the same. Part of the reason it was never put in a function was the large number of separate variables. But red button, yellow button and blue button all play the same role. Their names are not really important. What matters is the association: red button goes with the string red.

## Files

- [`starter/chooseButton1.py`](starter/chooseButton1.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/chooseButton1.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: The click is awaited
   - Lines 2–10: nearly the same
   - Lines 11: the shape is filled

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l07-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
