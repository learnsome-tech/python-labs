# m02l02-07 · Where Homebrew puts it, and why it moved

**Lesson:** [Installing Python On A Mac](https://learnsome.tech/learn/python-course/m02l02) (lesson 2.2, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can install your own Python on a Mac by either the python.org installer or Homebrew, leave Apple's system python3 untouched, put yours first on PATH from your zsh profile, and confirm the result with python3 and idle3.

In the lesson: Homebrew keeps everything under a single prefix, and that prefix moved when Apple changed processors. On an Apple silicon Mac, which yours almost certainly is, it is opt homebrew, the first line of output on screen. On older Intel Macs it is the prefix named in the last comment line, which was already on the shell path, and that is why so much older advice does not match what you see. Do not guess: ask brew. The prefix command answers for the whole installation; add a package name and it answers for that package. The last command shows the payoff: my Homebrew Python comes first.

## Files

- [`starter/brew-where.sh`](starter/brew-where.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/brew-where.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
