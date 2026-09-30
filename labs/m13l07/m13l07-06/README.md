# m13l07-06 · Unpacking a tuple in the for heading

**Lesson:** [Loops And Tuples](https://learnsome.tech/learn/python-course/m13l07) (lesson 13.7, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can package related values in a tuple, unpack a tuple in a for loop heading, and replace a long repetitive if elif statement with a loop over a list of tuples.

In the lesson: Such tuples are neatly handled by a for statement. Imagine a function to encapsulate the colour choice, starting like this. It waits for a mouse click, then walks the list of pairs. This is the first time we have had a for loop going through a list of tuples. The loop takes one tuple from the list each time round. The first time, that tuple is the red button paired with the string red, and the heading does a multiple assignment, so rectangle refers to the red button and choice to red. Next time round rectangle refers to the yellow button and choice to yellow.

## Files

- [`starter/chooseButton2draft.py`](starter/chooseButton2draft.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/chooseButton2draft.py` alongside the lesson.
2. Notes from the lesson:
   - Line 8: one tuple per pass, unpacked into two loop variables

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l07-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
