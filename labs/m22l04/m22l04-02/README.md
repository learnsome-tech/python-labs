# m22l04-02 · A script you can run by name

**Lesson:** [Shipping: scripts, entry points and git](https://learnsome.tech/learn/python-course/m22l04) (lesson 22.4, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can turn a script into a command you can run from anywhere, describe your project in a pyproject file, build and install it, and keep its history in git.

In the lesson: Here is a small program that counts the words in each file you name. On Mac and Linux two things make it runnable on its own. First, the very first line of the file: a hash and an exclamation mark, then the path to the program that should run it. That line is called a shebang, and the version using env finds Python wherever it happens to live on that machine. Second, the file needs permission to be executed, which the change mode command grants with plus x. Read the transcript beside it: without that permission the shell refuses, and after one chmod the same command works and prints the count.

## Files

- [`starter/wordcount.py`](starter/wordcount.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/wordcount.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: the shebang: hash, exclamation mark, then which program runs it

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
