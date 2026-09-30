# m11l06-10 · The first eye and the line eye

**Lesson:** [Animation: Loops, Bouncing, Flushing](https://learnsome.tech/learn/python-course/m11l06) (lesson 11.6, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a group of shapes held in a list, move them diagonally and repeatedly with nested loops, build a shape group at any position by cloning points, and use autoflush with update to get one clean frame per step.

In the lesson: With the clone moved, the small blue circle is built at that point, filled and drawn. Eye two is a line, so it needs two endpoints, and each is made the same way: clone the point you already have and move the clone along. The first endpoint is the eye one centre shifted fifteen across; the second is that endpoint shifted a further ten. Then the Line is built from the two, given a setWidth of three so that it shows, and drawn.

## Files

- [`starter/backAndForth3.py`](starter/backAndForth3.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth3.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: the small blue circle
   - Lines 4–7: Eye two is a line
   - Lines 8–12: setWidth of three

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l06-10` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
