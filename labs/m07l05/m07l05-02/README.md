# m07l05-02 · Finding the pattern in the arithmetic

**Lesson:** [Accumulation Loops](https://learnsome.tech/learn/python-course/m07l05) (lesson 7.5, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can build a loop that accumulates a result, choose the right initial value for the accumulator, and recognise from an English description when a loop through a sequence is needed.

In the lesson: By hand you very likely did the top sequence on the screen. Two and six is eight, eight and three is eleven, eleven and eight is nineteen, and nineteen is the answer. The list could be any length, so you need a loop, and a loop means finding a pattern you can reuse with the same statements every time. Most of the sequence is a pattern already: each step takes the running total and adds the next number from the list. But the very first line breaks it. There is no previous total, and it uses two numbers from the list at once. The cure is in the lower sequence: start with a total of zero. Adding zero and two is a longer way round by hand, but it makes every single step identical.

## Files

- [`starter/finding-the-pattern-in-the-arithmetic.txt`](starter/finding-the-pattern-in-the-arithmetic.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/finding-the-pattern-in-the-arithmetic.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
