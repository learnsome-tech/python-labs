# m14l03-11 · Remembering which click stopped the loop

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: Bounce three uses where the click was, not merely that there was one. Off the top of this screen, the docstring now says the last mouse click is returned. A name, pt, is given to that click, set to None before the loop and reset at the end of each pass. Then a bug fix. The ball is allowed one step beyond the boundary because the next step was sure to jump it back, unless a click at that moment changed the direction and left it stuck. So the boolean variable isInside, corrected by either boundary test, means a new click is read only when the ball is safely inside.

## Files

- [`starter/bounce3.py`](starter/bounce3.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bounce3.py` alongside the lesson.
2. Notes from the lesson:
   - Line 2: pt is initialised before the loop so the heading has something to test
   - Line 16: Only read a new click when the ball is not about to bounce back

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-11` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
