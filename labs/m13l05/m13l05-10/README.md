# m13l05-10 · Building the whole test from smaller ones

**Lesson:** [Compound Boolean Expressions](https://learnsome.tech/learn/python-course/m13l05) (lesson 13.5, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can build conditions with and, or and not, read their precedence and short circuit behaviour, and return a Boolean expression directly instead of wrapping it in an if else.

In the lesson: That single return line is the whole of the helper. Now go back to the outer function. You call the helper once for the horizontal coordinates and once for the vertical ones, and the question arises again: how do you combine the two answers? The point has to be between the two sides and also between the top and the bottom. Both must hold at once, so the connector is and. Choosing between and and or is nearly always a matter of reading your sentence back in English and listening to which word you said.

## Files

- [`starter/building-the-whole-test-from-smaller-ones.txt`](starter/building-the-whole-test-from-smaller-ones.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/building-the-whole-test-from-smaller-ones.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l05-10` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
