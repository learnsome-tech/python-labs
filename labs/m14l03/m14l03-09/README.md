# m14l03-09 · Getting a direction from a mouse click

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: In bounce two the initial direction and speed of the ball are chosen graphically by the user. Two new functions do that work. getShift takes two points and returns the move needed to go from the first to the second: a change in x and a change in y. Since it works out both, it returns a tuple. Wrapped around it is getUserShift. It draws the prompt under the point, waits for a click with getMouse, undraws the prompt, and returns the shift to wherever the user clicked.

## Files

- [`starter/bounce2.py`](starter/bounce2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bounce2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: getShift takes two points
   - Lines 6–15: Wrapped around it is getUserShift

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
