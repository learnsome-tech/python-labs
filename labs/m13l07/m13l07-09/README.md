# m13l07-09 · Extract the changing data into tuples

**Lesson:** [Loops And Tuples](https://learnsome.tech/learn/python-course/m13l07) (lesson 13.7, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can package related values in a tuple, unpack a tuple in a for loop heading, and replace a long repetitive if elif statement with a loop over a list of tuples.

In the lesson: Here is the alternative, and it pays off if there are many more buttons. I extract the changing data out of the creation of the rectangles into a list called button setup. Since more than one data item differs on each original line, the list holds a tuple from each line: an x coordinate, a y coordinate and a colour, so the heading unpacks three names, not two. The loop then creates the rectangle for each colour and accumulates the rectangle and colour pairs into choice pairs. Note the double parentheses in the last line. The outer pair belongs to the method call; the inner pair makes the tuple.

## Files

- [`starter/chooseButton2draft.py`](starter/chooseButton2draft.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/chooseButton2draft.py` alongside the lesson.
2. Notes from the lesson:
   - Line 6: outer parentheses for the call, inner ones make the tuple

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l07-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
