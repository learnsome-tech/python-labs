# m13l04-05 · bounceInBox: an if inside a for loop

**Lesson:** [Nesting Control Flow Statements](https://learnsome.tech/learn/python-course/m13l04) (lesson 13.4, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can nest if statements inside loops and loops inside if statements, and read the indentation to see which block belongs to which heading.

In the lesson: Here is the real function. Everything sits inside a repeat loop of six hundred steps. Each time round the shape moves, and then three lines ask the graphics objects where the centre of the ball now is: the get centre method returns a copy of the centre point, and get x and get y pull out its coordinates. Then come the four bounce tests. An elif avoids the wasted test for the horizontal pair, and another for the vertical pair. But look at the middle one. It is a plain if, not an elif, because the ball can reach a corner and need both directions reversed at once.

## Files

- [`starter/bounce1.py`](starter/bounce1.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bounce1.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: a repeat loop of six hundred steps
   - Lines 7–10: where the centre of the ball now is
   - Lines 11–19: the four bounce tests
3. Notes from the lesson:
   - Line 13: elif: x cannot be below the low bound and above the high one
   - Line 15: a plain if, not an elif: a corner reverses both directions

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
