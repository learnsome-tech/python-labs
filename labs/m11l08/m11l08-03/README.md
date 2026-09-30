# m11l08-03 · randomCircles: a colour at random

**Lesson:** [Colours, Custom And Random](https://learnsome.tech/learn/python-course/m11l08) (lesson 11.8, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can use the many built-in colour names, build a colour of your own from red, green and blue intensities with color_rgb, and choose random values from a range with the random module's randrange function.

In the lesson: Random colours are an interesting use of that function. This is the top of randomCircles. Two modules are imported on one line, random and time, separated by a comma; that is allowed and often convenient. Main opens a window, and then a repeat loop runs seventy five times. Each time round, three random intensities are drawn, one each for red, blue and green, and the color rgb function turns them into a colour. Notice that the three values are chosen independently, so the colours are genuinely varied rather than shades of one hue.

## Files

- [`starter/graphics.py`](starter/graphics.py)
- [`starter/randomCircles.py`](starter/randomCircles.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/randomCircles.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: This is the top of randomCircles
   - Lines 5–7: Main opens a window
   - Lines 8: a repeat loop runs seventy five times
   - Lines 9–11: three random intensities are drawn
   - Lines 12: turns them into a colour
3. Notes from the lesson:
   - Line 4: Imported modules may be given as a comma separated list

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l08-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l08) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
