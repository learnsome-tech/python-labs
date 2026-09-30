# m11l02-07 · Three balloons from one loop

**Lesson:** [Sample Graphics Programs](https://learnsome.tech/learn/python-course/m11l02) (lesson 11.2, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can write a complete graphics program with the standard starting lines, build a picture from circles, lines, ovals, text and polygons, take input from mouse clicks, and close the window from inside the picture.

In the lesson: Another simple drawing, with the documentation string above the part on screen. The three balloons are built by identical steps, differing only in where each centre goes, and all three strings start from one shared base point. Whenever steps repeat like that, the answer is a loop over a list of centres. Each pass draws the string as a line from the base to the centre, then a circle of radius forty, outlined red and filled pink. The same ending closes it.

## Files

- [`starter/balloons.py`](starter/balloons.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/balloons.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: one shared base point
   - Lines 6–13: a loop over a list of centres
   - Lines 14–17: the same ending

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l02-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
