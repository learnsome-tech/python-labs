# m11l06-04 · The list, and the animation

**Lesson:** [Animation: Loops, Bouncing, Flushing](https://learnsome.tech/learn/python-course/m11l06) (lesson 11.6, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a group of shapes held in a list, move them diagonally and repeatedly with nested loops, build a shape group at any position by cloning points, and use autoflush with update to get one clean frame per step.

In the lesson: The mouth is an oval, filled red. Now the important line: the four parts are gathered into a list called faceList. That is all a group is. Then cir two is drawn, after the face, so the face will pass behind it. The animation is two calls to moveAllOnLine: the whole face five pixels right, forty six times, then five pixels left. Finally promptClose waits for a click. Trace how main, moveAllOnLine and moveAll call one another.

## Files

- [`starter/backAndForth2.py`](starter/backAndForth2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: The mouth is an oval
   - Lines 4–5: gathered into a list called faceList
   - Lines 6–9: Then cir two is drawn
   - Lines 10–12: two calls to moveAllOnLine
   - Lines 13–16: promptClose waits for a click

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l06-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
