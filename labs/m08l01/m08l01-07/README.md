# m08l01-07 · The rule for the type of a result

**Lesson:** [Floats, Division And Mixed Types](https://learnsome.tech/learn/python-course/m08l01) (lesson 8.1, module 8: Numbers In Depth) · Pro  
**Check:** Read along

## Goal

You can predict whether an arithmetic expression produces an int or a float, explain why floating point results are approximations, and write code that never depends on two floats being exactly equal.

In the lesson: Here is the rule, and it is short enough to memorise. Any combination of plus, minus and times, with both operands of type int, produces an int. If the operation is the single slash division, or if either operand is a float, the result is a float. That is all there is to it. One caution before we move on, because it will bite you if you read code in other languages. Java, C plus plus, and Python version two all treat the single slash between two positive integers the way modern Python treats the double slash. In those languages one divided by two is zero, so the expression on the previous screen would have come out as zero rather than three point two five. Modern Python does what you expect mathematically.

## Files

- [`starter/the-rule-for-the-type-of-a-result.txt`](starter/the-rule-for-the-type-of-a-result.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-rule-for-the-type-of-a-result.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l01-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
