# m14l03-14 · One loop, three reasons to change direction

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: The final variation is bounce four. It behaves exactly like bounce three but shows a different internal design decision. Bounce three had two levels of while loop in two functions, one for mouse clicks and one for bouncing. Bounce four puts all the code that changes direction inside the single animation loop. There are now three reasons to adjust the change in x and y: bouncing off the sides, bouncing off the top or bottom, or a mouse click. Notice the heading: the loop condition is just True, an intentionally endless loop.

## Files

- [`starter/bounce4.py`](starter/bounce4.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bounce4.py` alongside the lesson.
2. Notes from the lesson:
   - Line 10: An intentionally endless loop: the exit is a return, further down

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-14` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
