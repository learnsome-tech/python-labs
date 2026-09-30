# m09l03-01 · Slices take a run of characters

**Lesson:** [String Slices](https://learnsome.tech/learn/python-course/m09l03) (lesson 9.3, module 9: Objects And Methods) · Pro  
**Check:** Read along

## Goal

You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

In the lesson: It is also useful to extract larger pieces of a string than a single character. That brings us to slices. The simplest syntax is the name of the string, square brackets, a start index, a colon, then an index past the end of what you want. The slice starts at the start index and stops just before the second index. That second number confuses almost everybody, so let us be blunt: the index after the colon is not the index of the final character. It is one place past it. So the length of the slice is the second number minus the first.

## Files

- [`starter/slices-take-a-run-of-characters.py`](starter/slices-take-a-run-of-characters.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/slices-take-a-run-of-characters.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m09l03-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
