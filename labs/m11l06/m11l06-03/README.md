# m11l06-03 · Building the face, part by part

**Lesson:** [Animation: Loops, Bouncing, Flushing](https://learnsome.tech/learn/python-course/m11l06) (lesson 11.6, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a group of shapes held in a list, move them diagonally and repeatedly with nested loops, build a shape group at any position by cloning points, and use autoflush with update to get one clean frame per step.

In the lesson: The code that constructs the face is the same as in the earlier face example. Main opens the window and puts y the right way up. The blue rectangle is drawn first, so everything else passes in front of it. Then the head, a yellow circle of radius twenty five. Then eye one, a small blue circle. Then eye two, which is a thick line rather than a circle, using setWidth of three. What is new is what we do with these four names.

## Files

- [`starter/backAndForth2.py`](starter/backAndForth2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: Main opens the window
   - Lines 4–7: The blue rectangle is drawn first
   - Lines 8–11: Then the head
   - Lines 12–15: Then eye one
   - Lines 16–19: Then eye two

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l06-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
