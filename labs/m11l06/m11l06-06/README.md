# m11l06-06 · Withholding updates with autoflush

**Lesson:** [Animation: Loops, Bouncing, Flushing](https://learnsome.tech/learn/python-course/m11l06) (lesson 11.6, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a group of shapes held in a list, move them diagonally and repeatedly with nested loops, build a shape group at any position by cloning points, and use autoflush with update to get one clean frame per step.

In the lesson: Here is the refinement, from backAndForth two update. MoveAll is unchanged. MoveAllOnLine becomes moveAllOnLineUpdate, and it takes one extra parameter, the window, because it needs to talk to it. Before the loop it sets the window's autoflush to False, which tells the graphics module to store changes rather than redraw after every instruction. Inside the loop, once all the parts have moved, a call to update paints the stored changes in one go, and then the program sleeps. After the loop autoflush goes back to True. Main is not on screen; it differs only in passing win to each call.

## Files

- [`starter/backAndForth2Update.py`](starter/backAndForth2Update.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth2Update.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: MoveAll is unchanged
   - Lines 5–7: it takes one extra parameter
   - Lines 8–13: autoflush to False
   - Lines 14–16: a call to update paints the stored changes
   - Lines 17–18: autoflush goes back to True

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l06-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
