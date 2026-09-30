# m11l06-09 · makeFace: the head, and a relative point

**Lesson:** [Animation: Loops, Bouncing, Flushing](https://learnsome.tech/learn/python-course/m11l06) (lesson 11.6, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a group of shapes held in a list, move them diagonally and repeatedly with nested loops, build a shape group at any position by cloning points, and use autoflush with update to get one clean frame per step.

In the lesson: Here is the start of makeFace. The head is a circle of radius twenty five centred on the centre parameter itself, so nothing needs adjusting there. The first eye is the interesting one. In the original face the head centre and the first eye centre differed by minus ten across and plus five up. So clone the centre, and the comment says it well: face positions are relative to the centre. The line that moves that clone is too wide for this screen, and comes next in the file.

## Files

- [`starter/backAndForth3.py`](starter/backAndForth3.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth3.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: Here is the start of makeFace
   - Lines 5–8: The head is a circle of radius twenty five
   - Lines 9–10: clone the centre

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l06-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
