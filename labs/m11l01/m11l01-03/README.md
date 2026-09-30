# m11l01-03 · Importing, and a window appears

**Lesson:** [A Graphics Introduction](https://learnsome.tech/learn/python-course/m11l01) (lesson 11.1, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can open a graphics window, construct points, circles, lines and rectangles, colour them, draw them, move them and close the window, and you know why the vertical axis points the wrong way.

In the lesson: Here is the same sequence without the pauses. It opens with a documentation string saying what the file is for. Then the import line. Zelle's graphics are not part of the standard Python distribution, so the interpreter has to be told to load them, and the star form makes every type in the module available as if it were built in, like the string type or the list type. Now the last line, which does something the others did not. It builds a graph win object, and a graph win puts a window on your screen the moment it is created. Look for it, possibly underneath your other windows. It is two hundred pixels square.

## Files

- [`starter/graphIntro.py`](starter/graphIntro.py): the listing from the lesson
- [`starter/graphics.py`](starter/graphics.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/graphIntro.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: a documentation string
   - Lines 4–5: Then the import line
   - Lines 6: the last line

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
