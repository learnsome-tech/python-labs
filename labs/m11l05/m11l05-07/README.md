# m11l05-07 · One function for any straight line

**Lesson:** [Animation: Moving One Shape](https://learnsome.tech/learn/python-course/m11l05) (lesson 11.5, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a single graphics object with a loop, a call to move and a call to time.sleep, explain why the delay and the drawing order matter, and turn a repeated animation loop into a reusable function.

In the lesson: The two loops in the last program were nearly identical, and that is a hint. Animating something along a straight line is one idea, so it deserves one function. Here it is, from backAndForth one. The arbitrary numbers become parameters: how far to move each step in x and in y, how many repetitions, and how long to delay. The object being moved becomes a parameter too, called shape, because there is nothing special about cir one. Any drawable object in the graphics package has a move method, so any of them will do. The body is the loop you already read, with names in place of the constants.

## Files

- [`starter/backAndForth1.py`](starter/backAndForth1.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth1.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: Here it is, from backAndForth one
   - Lines 2–4: The body is the loop you already read

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l05-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
