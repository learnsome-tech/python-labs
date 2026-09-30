# m14l03-03 · Where to cut the circle into a loop

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: Think of many repetitions and the process is circular. The body of a Python loop, though, is linear: a first line and a last line. You can cut a circle anywhere, but there is one constraint. The test in the while heading sits between the end of one pass and the start of the next, so the continuation condition must make sense exactly where you cut. Here it is that pt is inside the rectangle. So cut after a point has been clicked, and before the next polygon is created.

## Files

- [`starter/makePoly.py`](starter/makePoly.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/makePoly.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: The continuation condition: pt is still inside the rectangle

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
