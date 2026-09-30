# m13l04-04 · Four tests, one for each wall

**Lesson:** [Nesting Control Flow Statements](https://learnsome.tech/learn/python-course/m13l04) (lesson 13.4, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can nest if statements inside loops and loops inside if statements, and read the indentation to see which block belongs to which heading.

In the lesson: Which test? Suppose the centre of the ball is at coordinates x and y. The window edge is at zero, but the bounce must happen while the whole ball is still on screen, so the bound sits a radius in from the edge, and we call it x low. Since the steps are small and quick, we let the ball go one small step past where it should turn, then reverse it. The first two lines on screen are that single test. There are matching bounds for the other three walls, so one way to write the collection is these four separate if statements. It works, but if the first test was true the second cannot be, so that is a wasted test.

## Files

- [`starter/bounceTests.py`](starter/bounceTests.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bounceTests.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: one step past the edge, then reverse: the eye never notices
   - Line 3: if the first test was true this one cannot be, so it is wasted

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
