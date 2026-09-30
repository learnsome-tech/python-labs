# m14l03-04 · The last undraw, and how to cancel it

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: Follow the concrete triangle sequence and the full loop body runs only twice. On the last pass there is no undraw. So this is a line you want every time except the last, which suggests an if statement. The times you want it are the times the loop repeats, and you have just read the next point. That works, but it duplicates the test on every pass. Rather than avoiding the undraw as you leave the loop, undo it: draw the polygon one final time beyond the loop.

## Files

- [`starter/the-last-undraw-and-how-to-cancel-it.txt`](starter/the-last-undraw-and-how-to-cancel-it.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-last-undraw-and-how-to-cancel-it.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
