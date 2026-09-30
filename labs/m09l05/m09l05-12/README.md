# m09l05-12 · What to carry forward

**Lesson:** [Appending To Lists, Sets, Constructors](https://learnsome.tech/learn/python-course/m09l05) (lesson 9.5, module 9: Objects And Methods) · Pro  
**Check:** Read along

## Goal

You can grow a list with append inside a loop, explain why that differs from concatenation, build a set to remove duplicates, and recognise a type name used as a constructor.

In the lesson: Lists are mutable, so append changes the list you call it on and returns None, the value that means nothing, while the plus sign leaves both operands alone and builds a new list you must assign somewhere. That makes the accumulation loop tidy: start with an empty list from the list constructor, append inside the loop, and return the result. Sets convert any collection and throw the repetitions away, at the price of order. And a type name used as a function is a constructor. The footnote on screen shows a list comprehension, a much shorter way to derive one list from another. The tutorial mentions it and goes no further, and neither will we.

## Files

- [`starter/what-to-carry-forward.py`](starter/what-to-carry-forward.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/what-to-carry-forward.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m09l05-12` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
