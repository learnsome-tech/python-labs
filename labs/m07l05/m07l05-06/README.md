# m07l05-06 · The accumulation pattern, and its initial value

**Lesson:** [Accumulation Loops](https://learnsome.tech/learn/python-course/m07l05) (lesson 7.5, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can build a loop that accumulates a result, choose the right initial value for the accumulator, and recognise from an English description when a loop through a sequence is needed.

In the lesson: The pattern we used is certainly successive modification, of the variable sum, but this version of it deserves its own name. Call it an accumulation loop. Its outline is on the screen. Initialise the accumulation so that it includes none of the sequence yet. Then, for each item, the new value of the accumulation is that item combined with the last value of the accumulation. That initial value is not an arbitrary choice, and it is not always zero. Zero is right here because the sum of no numbers at all is zero, so before the loop begins the total is honest. Ask yourself what the answer should be for an empty sequence, and that is your initial value. This pattern works in many situations besides adding numbers.

## Files

- [`starter/the-accumulation-pattern-and-its-initial-val.txt`](starter/the-accumulation-pattern-and-its-initial-val.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-accumulation-pattern-and-its-initial-val.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l05-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
