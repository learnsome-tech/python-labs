# m13l06-03 · replace, with a count of how many

**Lesson:** [More String Methods](https://learnsome.tech/learn/python-course/m13l06) (lesson 13.6, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can test what a string starts with, ends with or is made of, and build up conditions from string methods such as startswith, endswith, replace and isdigit.

In the lesson: Replace takes three things: what to look for, what to put there instead, and how many occurrences at most to change. The replacement may be the empty string, which makes replace into a delete. So the first line here strips a leading minus sign. The second line runs the same call again on the result, but there is nothing left to replace, so the string comes back unchanged rather than raising an error. The third example deletes the first two dots out of four. The last one is a trap worth walking into: the leading dot counts too, so the answer is not quite what the tutorial's comment suggests. Let us look at the real values.

## Files

- [`starter/replaceDemo.py`](starter/replaceDemo.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/replaceDemo.py` alongside the lesson.
2. Notes from the lesson:
   - Line 3: nothing left to replace, so t comes back unchanged
   - Line 6: the leading dot counts too: the result starts with a space

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l06-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
