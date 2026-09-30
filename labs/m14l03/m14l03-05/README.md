# m14l03-05 · The finished polyHere function

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: Here is the whole function. Before the loop it sets the rectangle outline to red, draws it, starts an empty vertices list, and reads the first click. The loop appends the point, builds a new polygon from every vertex so far, draws it, reads the next click, and undraws. After the loop, poly is drawn once more to cancel that final undraw, the rectangle is undrawn, and the polygon is returned. Follow it through with three clicks inside and one outside.

## Files

- [`starter/makePoly.py`](starter/makePoly.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/makePoly.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: Here is the whole function
   - Lines 8–11: Before the loop it sets
   - Lines 12–17: The loop appends the point
   - Lines 18–20: After the loop

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
