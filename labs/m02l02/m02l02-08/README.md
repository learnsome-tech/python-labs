# m02l02-08 · The profile line, and which file it goes in

**Lesson:** [Installing Python On A Mac](https://learnsome.tech/learn/python-course/m02l02) (lesson 2.2, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can install your own Python on a Mac by either the python.org installer or Homebrew, leave Apple's system python3 untouched, put yours first on PATH from your zsh profile, and confirm the result with python3 and idle3.

In the lesson: Neither route helps until your shell can find what you installed. The shell on every Mac since Catalina is zsh, and the file it reads when a terminal opens a login shell is dot z profile, in your home directory. For Homebrew, one line goes there: brew shellenv prints the settings and eval applies them, which does more than the path alone. The Python installer writes its own two lines into the same file, keeping your old one under a pysave name. Then remember the last rule on screen: a window already open read that file when it opened, and will not read it again.

## Files

- [`starter/the-profile-line-and-which-file-it-goes-in.py`](starter/the-profile-line-and-which-file-it-goes-in.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-profile-line-and-which-file-it-goes-in.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
