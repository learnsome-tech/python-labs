# m10l01-04 · Get concrete, and write the indices down

**Lesson:** [Mad Libs Revisited: Finding The Cues](https://learnsome.tech/learn/python-course/m10l01) (lesson 10.1, module 10: Mad Libs Revisited) · Pro  
**Check:** Read along

## Goal

You can write a function that scans a format string and returns the list of cues embedded in it, and you can follow the creative process that produced it.

In the lesson: This is the most challenging code to date, so let us stop thinking in the abstract and look at a concrete case. Here is the beginning of a story with two rows of digits above it, put there only so we can read off the indices. The first key is animal, running from index six up to but not including index twelve. The second is food, from index twenty five to index twenty nine. So each key is a slice of the format string, and a slice needs two numbers: where the key starts and where it ends. Call them start and end. The keys are collected in a list, so call that keyList, and call the piece we pull out each time key.

## Files

- [`starter/get-concrete-and-write-the-indices-down.txt`](starter/get-concrete-and-write-the-indices-down.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/get-concrete-and-write-the-indices-down.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m10l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
