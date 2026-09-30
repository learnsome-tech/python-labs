# m08l01-05 · Where the name float comes from

**Lesson:** [Floats, Division And Mixed Types](https://learnsome.tech/learn/python-course/m08l01) (lesson 8.1, module 8: Numbers In Depth) · Pro  
**Check:** Read along

## Goal

You can predict whether an arithmetic expression produces an int or a float, explain why floating point results are approximations, and write code that never depends on two floats being exactly equal.

In the lesson: Why is the type called float rather than decimal? Two reasons, both about how it is stored. Decimal implies base ten, our normal way of writing numbers with ten digits. Computers actually work in base two, with only two symbols, the same two symbols you saw in the machine language back in the very first module. The second reason is the encoding. Floats use something like the scientific notation from science class, a number multiplied by a power of ten, as on screen. Because the exponent can change, the decimal point is free to move, or float, which is where the name comes from. Keep in mind that the base two storage makes floats inexact even in some cases where a decimal number could be written out exactly. We will prove that shortly.

## Files

- [`starter/where-the-name-float-comes-from.txt`](starter/where-the-name-float-comes-from.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/where-the-name-float-comes-from.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l01-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
