# m11l05-02 · Setting the scene: three shapes

**Lesson:** [Animation: Moving One Shape](https://learnsome.tech/learn/python-course/m11l05) (lesson 11.5, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a single graphics object with a loop, a call to move and a call to time.sleep, explain why the delay and the drawing order matter, and turn a repeated animation loop into a reusable function.

In the lesson: This is backAndForth zero, the first animation example. The imports are new in shape: everything from graphics, and then the time module by name. Main opens a window called Back and Forth and calls yUp, so y grows upwards. Then three shapes. A blue rectangle from two hundred, ninety to two hundred twenty, one hundred. A yellow circle called cir one, centred at forty, one hundred, with radius twenty five. And a red circle called cir two at one hundred fifty, one hundred twenty five. Each one is constructed, filled and drawn. Nothing has moved yet; this is the stage set.

## Files

- [`starter/backAndForth0.py`](starter/backAndForth0.py): the listing from the lesson
- [`starter/graphics.py`](starter/graphics.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth0.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: The imports are new in shape
   - Lines 6–9: Main opens a window
   - Lines 10–13: A blue rectangle
   - Lines 14–17: A yellow circle called cir one
   - Lines 18–21: a red circle called cir two
3. Notes from the lesson:
   - Line 5: import time, so the function is written time.sleep

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
