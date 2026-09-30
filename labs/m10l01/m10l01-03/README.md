# m10l01-03 · How many keys? Count the braces

**Lesson:** [Mad Libs Revisited: Finding The Cues](https://learnsome.tech/learn/python-course/m10l01) (lesson 10.1, module 10: Mad Libs Revisited) · Pro  
**Check:** Read along

## Goal

You can write a function that scans a format string and returns the list of cues embedded in it, and you can follow the creative process that produced it.

In the lesson: How many times do we want to pull out a key? Once for each embedded format. So how do we count those? The count method is the obvious tool, but it counts a fixed string, and a whole cue varies, because the key in the middle is different every time. What all the cues have in common is the open brace, and an open brace has no business appearing in the ordinary text of a story. So counting braces counts the cues. That gives us a repeat loop, where the loop variable is never used in the body and the range only makes the body happen the right number of times. It is the pattern that fits, because we are creating the sequence of keys, not walking along one that already exists.

## Files

- [`starter/how-many-keys-count-the-braces.py`](starter/how-many-keys-count-the-braces.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/how-many-keys-count-the-braces.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m10l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
