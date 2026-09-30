# m12l01-07 · Reading a whole file back

**Lesson:** [Files: Writing And Reading](https://learnsome.tech/learn/python-course/m12l01) (lesson 12.1, module 12: Files And Chapter Review) · Pro  
**Check:** Read along

## Goal

You can open a file for writing or reading, write strings to it with explicit newlines, read the whole file back as one string, and say why closing a file you wrote to is essential.

In the lesson: Now the other direction. Note the comment at the top: this program needs the previous one to have run first, because it expects that file to exist. Then we open with the mode r, short for read. The file should already be there, and the intention is to read from it. Read is the most common thing to do with a file, so that second argument is actually optional. The read method returns all of the file's data as a single string, here given the name contents. Then we print what came back. So one Python program has written into the file and another has read it and displayed it. Full circle.

## Files

- [`starter/printFile.py`](starter/printFile.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/printFile.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: the comment at the top
   - Lines 4–5: open with the mode r
   - Lines 6: The read method
   - Lines 7: print what came back

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m12l01-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m12l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
