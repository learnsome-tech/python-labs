# m11l07-07 · Showing the answer in the window

**Lesson:** [Entry Objects](https://learnsome.tech/learn/python-course/m11l07) (lesson 11.7, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can put an Entry box in a graphics window with its own label, use a mouse click as the signal that typing has finished, and read or set its contents with getText and setText, converting to numbers where you need them.

In the lesson: One more line is too wide for the screen. Just above what you see, the answer is formatted with the string format method, using a template of the sum, then the first number, then the word plus, then the second number, then the word is and the total, with newlines between them, and locals supplying the values by name. The result is then drawn as a Text object in the middle of the window. After that, promptClose reuses the instructions object for the closing message, and the file ends by calling main.

## Files

- [`starter/addEntries.py`](starter/addEntries.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/addEntries.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: drawn as a Text object in the middle
   - Lines 2–5: the file ends by calling main

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l07-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
