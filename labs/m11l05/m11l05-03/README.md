# m11l05-03 · The two animation loops

**Lesson:** [Animation: Moving One Shape](https://learnsome.tech/learn/python-course/m11l05) (lesson 11.5, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a single graphics object with a loop, a call to move and a call to time.sleep, explain why the delay and the drawing order matter, and turn a repeated animation loop into a reusable function.

In the lesson: Here is the whole animation. The first loop repeats forty six times. Each time round, cir one moves five pixels to the right and the program sleeps for five hundredths of a second. Forty six steps of five pixels is two hundred thirty pixels of travel, which carries the yellow circle across most of the window. The second loop is the same three lines with the sign of the horizontal step flipped, so the circle walks back to where it began. Then promptClose puts a message near the bottom and waits for a click, since with the axis turned up a height of twenty is twenty units above the floor of the window. Watch the yellow circle as it travels: it passes over the blue rectangle, and behind the red circle.

## Files

- [`starter/backAndForth0.py`](starter/backAndForth0.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth0.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: The first loop repeats forty six times
   - Lines 4–7: The second loop is the same three lines
   - Lines 8–11: promptClose puts a message near the bottom

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
