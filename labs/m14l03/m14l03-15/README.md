# m14l03-15 · Exiting from the depths with return

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: The line just above the top of this screen, marked as new, checks that pt is not None, so a click really did happen. Then a click below the stop line switches direction, and a click at or above it means quit. Recall that a return statement immediately terminates a function. Here it returns no value, and a bare return is legal just to force the exit. Because the test is not done in the while condition, that condition has to be permanently True, which obscures the exit. Choosing between the two designs is a matter of taste.

## Files

- [`starter/bounce4.py`](starter/bounce4.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bounce4.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-15` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
