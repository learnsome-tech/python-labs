# m11l06-11 · The mouth, and the list that is returned

**Lesson:** [Animation: Loops, Bouncing, Flushing](https://learnsome.tech/learn/python-course/m11l06) (lesson 11.6, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a group of shapes held in a list, move them diagonally and repeatedly with nested loops, build a shape group at any position by cloning points, and use autoflush with update to get one clean frame per step.

In the lesson: The mouth needs two opposite corners, built by cloning the centre and then cloning the first corner, exactly as before. The mouth is an oval across those corners, filled red and drawn. Then the last line returns a list of the four shapes to the caller, which is what the animation functions expect. Notice how the clone method has stopped being an abstract lesson about aliases and become an ordinary working tool.

## Files

- [`starter/backAndForth3.py`](starter/backAndForth3.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/backAndForth3.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: cloning the centre and then cloning the first corner
   - Lines 5–8: The mouth is an oval
   - Lines 9–10: returns a list of the four shapes

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l06-11` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
