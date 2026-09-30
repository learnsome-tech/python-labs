# m07l05-03 · One pass of work, and the handover

**Lesson:** [Accumulation Loops](https://learnsome.tech/learn/python-course/m07l05) (lesson 7.5, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can build a loop that accumulates a result, choose the right initial value for the accumulator, and recognise from an English description when a loop through a sequence is needed.

In the lesson: The second part of each sum is a number taken from the list, so call it num and let it be the loop variable. Then the main calculation inside the loop is the first line on the screen: next sum is sum plus num. The trick is to use that same line of code again on the next pass, which means whatever was next sum in one pass has to be sum in the pass that follows. One honest way to arrange that is the four lines below: initialise sum to zero before the loop, do the calculation, then copy next sum back into sum. Do you recognise the shape? It is exactly the successive modification pattern: initialisation, loop heading, the main work, then preparation for the next time round.

## Files

- [`starter/one-pass-of-work-and-the-handover.py`](starter/one-pass-of-work-and-the-handover.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/one-pass-of-work-and-the-handover.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
