# m11l06-12 · Two faces, and a richer animation

**Lesson:** [Animation: Loops, Bouncing, Flushing](https://learnsome.tech/learn/python-course/m11l06) (lesson 11.6, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a group of shapes held in a list, move them diagonally and repeatedly with nested loops, build a shape group at any position by cloning points, and use autoflush with update to get one clean frame per step.

In the lesson: Main is where the payoff shows. One call to makeFace puts a face where the old head was, and a second call replaces the old red circle with a whole second face. Then the animation. The unnamed numbers become named values: stepsAcross, dx, dy and wait, each stated once and easy to change. The outer repeat loop runs the whole journey three times, and since moveAllOnLine holds a loop of its own, this is a nest of loops. Two of the three calls inside use a vertical step as well, so the face moves diagonally. Then promptClose waits for the closing click.

## Files

- [`starter/backAndForth3.py`](starter/backAndForth3.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth3.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–9: One call to makeFace puts a face
   - Lines 10: a whole second face
   - Lines 11–15: become named values
   - Lines 16–19: use a vertical step as well
   - Lines 20–21: waits for the closing click

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l06-12` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
