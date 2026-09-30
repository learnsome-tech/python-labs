# m22l04-08 · What does not belong in the repository

**Lesson:** [Shipping: scripts, entry points and git](https://learnsome.tech/learn/python-course/m22l04) (lesson 22.4, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can turn a script into a command you can run from anywhere, describe your project in a pyproject file, build and install it, and keep its history in git.

In the lesson: Not everything in the folder belongs in the history. Put the names on screen into a file called dot gitignore and git will pretend the matching files are not there. The rules are easy to remember. Anything a machine can regenerate is out: the pycache folders, compiled files, the dist folder you just built. The virtual environment is out, because it is large, machine specific and rebuildable from your dependency list. And secrets are out, permanently: a password or an interface key committed once lives in the history forever, and people do lose real money to this. Everything else, source and tests and the pyproject file and the ignore file itself, goes in.

## Files

- [`starter/what-does-not-belong-in-the-repository.txt`](starter/what-does-not-belong-in-the-repository.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/what-does-not-belong-in-the-repository.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l04-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
