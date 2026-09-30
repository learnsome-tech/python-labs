# m21l01-08 · Why glued path strings break on other machines

**Lesson:** [Paths And Files The Modern Way](https://learnsome.tech/learn/python-course/m21l01) (lesson 21.1, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Read along

## Goal

You can open every file with a with statement, read it whole or line by line, append to it, choose an encoding on purpose, and build paths with pathlib that work on any operating system.

In the lesson: Now the reason this matters rather than being a nicer style. When you build a path by gluing strings together you have to write the separator yourself, and the separator is not the same everywhere: Windows uses a backslash where Mac and Linux use a forward slash. Worse, a backslash inside a Python string also starts an escape code, so a Windows path typed carelessly can turn a t or an n into something else entirely. A Path object knows which separator the machine it is running on uses, and prints itself correctly on each. Write the second line rather than the first, and your program moves between machines without you thinking about it once.

## Files

- [`starter/why-glued-path-strings-break-on-other-machin.py`](starter/why-glued-path-strings-break-on-other-machin.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/why-glued-path-strings-break-on-other-machin.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m21l01-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
