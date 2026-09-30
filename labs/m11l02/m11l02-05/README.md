# m11l02-05 · Prompt, wait for a click, close

**Lesson:** [Sample Graphics Programs](https://learnsome.tech/learn/python-course/m11l02) (lesson 11.2, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can write a complete graphics program with the standard starting lines, build a picture from circles, lines, ovals, text and polygons, take input from mouse clicks, and close the window from inside the picture.

In the lesson: Just as with waiting for keyboard input, it is important to prompt the user before waiting for a response. In a graphics window that means drawing a text object first. The new part is a call that asks the window for its own width; there is a matching one for the height. Halving the width centres the prompt. Then get mouse waits for a mouse click, and here the position is thrown away. Then the window is closed. Text programs end by themselves, but a program that made a window does not. The call at the bottom of the file starts everything.

## Files

- [`starter/face.py`](starter/face.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/face.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: prompt the user
   - Lines 3–4: waits for a mouse click
   - Lines 5–6: the bottom of the file

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
