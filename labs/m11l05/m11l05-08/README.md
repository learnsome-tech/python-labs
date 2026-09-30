# m11l05-08 · Two calls instead of two loops

**Lesson:** [Animation: Moving One Shape](https://learnsome.tech/learn/python-course/m11l05) (lesson 11.5, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a single graphics object with a loop, a call to move and a call to time.sleep, explain why the delay and the drawing order matter, and turn a repeated animation loop into a reusable function.

In the lesson: With moveOnLine defined, the main function loses both loops and gains two lines. Move cir one five across, no vertical change, forty six times, with a delay of five hundredths of a second. Then the same with the horizontal step negative, to bring it home. To the user the program looks exactly as it did before, and that is the point. Make sure you can see that these two calls behave the same way as the two loops in the original main program, and that you can say which argument corresponds to which parameter. Reading a call against its definition is a skill worth practising deliberately.

## Files

- [`starter/backAndForth1.py`](starter/backAndForth1.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth1.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–16: the main function loses both loops
   - Lines 17–18: Move cir one five across
   - Lines 19–22: To the user the program looks exactly as it did before

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l05-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
