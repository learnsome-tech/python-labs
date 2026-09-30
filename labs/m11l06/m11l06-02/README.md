# m11l06-02 · moveAll and moveAllOnLine

**Lesson:** [Animation: Loops, Bouncing, Flushing](https://learnsome.tech/learn/python-course/m11l06) (lesson 11.6, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a group of shapes held in a list, move them diagonally and repeatedly with nested loops, build a shape group at any position by cloning points, and use autoflush with update to get one clean frame per step.

In the lesson: This is the top of backAndForth two. The group of shapes is held in the most basic Python container, a list, so the parameter is called shapeList. MoveAll takes that list and a step, and loops over it to move every shape by the same amount. No sleeping happens here. Then moveAllOnLine is moveOnLine with one line changed: where the old function called move on a single shape, this one calls moveAll on the whole list. The sleep happens once per repetition, after every part has moved.

## Files

- [`starter/backAndForth2.py`](starter/backAndForth2.py): the listing from the lesson
- [`starter/graphics.py`](starter/graphics.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: This is the top of backAndForth two
   - Lines 6–10: loops over it to move every shape
   - Lines 11–18: moveAllOnLine is moveOnLine with one line changed
   - Lines 19–21: The sleep happens once per repetition

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l06-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
