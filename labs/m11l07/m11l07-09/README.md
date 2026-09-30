# m11l07-09 · One function for a labelled entry

**Lesson:** [Entry Objects](https://learnsome.tech/learn/python-course/m11l07) (lesson 11.7, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can put an Entry box in a graphics window with its own label, use a mouse click as the signal that typing has finished, and read or set its contents with getText and setText, converting to numbers where you need them.

In the lesson: The almost identical code for the two entries is a strong suggestion that a function would help. Here it is, from addEntries two. MakeLabeledEntry takes a centre point, a width in characters, an initial string, the label text and the window. It builds the Entry, sets its initial text and draws it. Then it places the label thirty units above by cloning the centre point and moving the clone, which is the aliasing lesson turning up again. Only the Entry is returned; the label is static, so once drawn it can be forgotten and is never even named.

## Files

- [`starter/addEntries2.py`](starter/addEntries2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/addEntries2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: Here it is, from addEntries two
   - Lines 6–9: It builds the Entry
   - Lines 10–13: places the label thirty units above
   - Lines 14: Only the Entry is returned

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l07-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
