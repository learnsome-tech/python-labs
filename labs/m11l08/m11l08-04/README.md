# m11l08-04 · A random size and a random place

**Lesson:** [Colours, Custom And Random](https://learnsome.tech/learn/python-course/m11l08) (lesson 11.8, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can use the many built-in colour names, build a colour of your own from red, green and blue intensities with color_rgb, and choose random values from a range with the random module's randrange function.

In the lesson: The rest of the loop body. A radius is chosen at random, then an x and a y for the centre. The circle is built at that point with that radius, filled with the random colour, and drawn. A short sleep makes the circles appear one after another rather than all at once, which is much nicer to watch. After seventy five circles, promptClose waits for a click. Look closely at these calls to randrange, because they have two arguments rather than one, and the next screens are about why.

## Files

- [`starter/randomCircles.py`](starter/randomCircles.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/randomCircles.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: A radius is chosen at random
   - Lines 4–7: filled with the random colour, and drawn
   - Lines 8: A short sleep makes the circles appear
   - Lines 9–12: promptClose waits for a click

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l08-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l08) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
