# m02l05-11 · Fixing a missing tkinter

**Lesson:** [First Run, And Fixing A Broken Install](https://learnsome.tech/learn/python-course/m02l05) (lesson 2.5, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can run Python three ways - the shell, a file from a terminal and a file from Idle - and diagnose the six failures that break a fresh install by naming the symptom, the cause and the fix.

In the lesson: Idle itself reports the same problem in plainer words, and those two lines are on screen. The fix depends on how Python got onto the machine. On Debian or Ubuntu, install the package whose name ends in tk with the system package manager. On Fedora the same package has tkinter in its name. With Homebrew on a Mac, install the tk package matching your Python version. On Windows, run the installer again, choose Modify, and make sure the entry naming tcl and tk is ticked. None of your own files are touched.

## Files

- [`starter/fixing-a-missing-tkinter.txt`](starter/fixing-a-missing-tkinter.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/fixing-a-missing-tkinter.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-11` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
