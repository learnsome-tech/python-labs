# m14l03-10 · Unpacking the shift in bounceBall

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: Here is the part of the driver that uses them. Just above the top of this screen, one line sets center to the middle of the window, and the ball is a red disk drawn there. The prompt is a long string in triple quotes. Now look at the multiple assignment: dx and dy are both set from the tuple that getUserShift returns. That shift is far too much for one animation step, so it is scaled right down before going to bounceInBox, with the window it needs for checkMouse.

## Files

- [`starter/bounce2.py`](starter/bounce2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bounce2.py` alongside the lesson.
2. Notes from the lesson:
   - Line 8: Multiple assignment: dx and dy come from the returned tuple

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-10` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
