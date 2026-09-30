# m13l03-04 · How a chain is read, and the rule that matters

**Lesson:** [If Elif Chains](https://learnsome.tech/learn/python-course/m13l03) (lesson 13.3, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can write an if elif else chain to sort a value into any number of cases, and explain why only the first true test matters.

In the lesson: Here is the general shape. The if line, every elif line and the final else line are all aligned, and each is followed by its own indented block. There can be as many elif lines as you like. Now the rule that matters. Python works down the chain in order and stops at the first test that is true. It runs that block, and then jumps to the end of the whole statement. The remaining tests are never evaluated at all. That is why the grade function can write at least eighty for a B without also saying below ninety: if the score were ninety or more, we would never have reached that test.

## Files

- [`starter/how-a-chain-is-read-and-the-rule-that-matter.txt`](starter/how-a-chain-is-read-and-the-rule-that-matter.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/how-a-chain-is-read-and-the-rule-that-matter.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
