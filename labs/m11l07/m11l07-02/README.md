# m11l07-02 · greet.py: setting up an Entry

**Lesson:** [Entry Objects](https://learnsome.tech/learn/python-course/m11l07) (lesson 11.7, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can put an Entry box in a graphics window with its own label, use a mouse click as the signal that typing has finished, and read or set its contents with getText and setText, converting to numbers where you need them.

In the lesson: Here is the first part of greet. Main opens a three hundred square window and turns the coordinates the right way up. The instructions are a Text object, and notice the backslash n inside the string: a Text object honours a newline, so one Text can hold two lines. Then the new part. Entry takes a centre point and a number of characters to leave room for, ten in this case, and like any other graphical object it must be drawn before you can see it. Nothing about it is filled or coloured; it is a plain box waiting for the keyboard.

## Files

- [`starter/graphics.py`](starter/graphics.py)
- [`starter/greet.py`](starter/greet.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/greet.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: Here is the first part of greet
   - Lines 6–9: Main opens a three hundred square window
   - Lines 10–13: The instructions are a Text object
   - Lines 14–16: Then the new part
3. Notes from the lesson:
   - Line 15: Entry(centrePoint, widthInCharacters)

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l07-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
