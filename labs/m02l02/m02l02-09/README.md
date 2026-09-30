# m02l02-09 · Idle on a Mac, and the Tk question

**Lesson:** [Installing Python On A Mac](https://learnsome.tech/learn/python-course/m02l02) (lesson 2.2, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can install your own Python on a Mac by either the python.org installer or Homebrew, leave Apple's system python3 untouched, put yours first on PATH from your zsh profile, and confirm the result with python3 and idle3.

In the lesson: Idle is written in Python, but its windows are drawn by Tk, a separate toolkit, and that is where the two routes part company. The official installer bundles a Mac build of Tk, so Idle works the moment it finishes. Homebrew does not: its Python leaves the Tk binding out, so typing idle three gives you the complaint on screen instead of a window. Nothing is broken, and reinstalling Python will not help. Install the companion package named on the third line, whose name ends with the same version as your Python, and Idle opens. The last line starts the same program as a module, naming the interpreter it belongs to.

## Files

- [`starter/idle3.sh`](starter/idle3.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/idle3.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
