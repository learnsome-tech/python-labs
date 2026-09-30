# m11l07-05 · addEntries.py: two boxes, and setText

**Lesson:** [Entry Objects](https://learnsome.tech/learn/python-course/m11l07) (lesson 11.7, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can put an Entry box in a graphics window with its own label, use a mouse click as the signal that typing has finished, and read or set its contents with getText and setText, converting to numbers where you need them.

In the lesson: The next example, addEntries, reads two numbers and adds them. The window and the instructions are as before. The first Entry is twenty five characters wide, and then something new: setText is called with the string zero, so the box does not start out empty. That was a deliberate choice. A zero in the box reinforces that a numerical value is expected, and it saves the user wondering what belongs there. Again the method name, setText, is one you already know from Text objects. Above the box, at the larger height that the upturned axis puts higher on screen, a static label reading First Number is drawn on the spot, since we never refer to it again.

## Files

- [`starter/addEntries.py`](starter/addEntries.py): the listing from the lesson
- [`starter/graphics.py`](starter/graphics.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/addEntries.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: reads two numbers and adds them
   - Lines 6–13: The window and the instructions are as before
   - Lines 14–16: setText is called with the string zero
   - Lines 17–19: a static label reading First Number

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l07-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
