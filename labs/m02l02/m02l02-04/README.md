# m02l02-04 · Route one: the installer, step by step

**Lesson:** [Installing Python On A Mac](https://learnsome.tech/learn/python-course/m02l02) (lesson 2.2, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can install your own Python on a Mac by either the python.org installer or Homebrew, leave Apple's system python3 untouched, put yours first on PATH from your zsh profile, and confirm the result with python3 and idle3.

In the lesson: Route one. Go to the macOS downloads page on the Python website and take the current release: one universal build that runs natively on Apple silicon and on Intel. What arrives is an ordinary installer package, signed and notarised by the Python Software Foundation, so it opens without argument. Double click and work through the windows: continue, a read me naming the version and the macOS releases it supports, the licence, then install. It wants an administrator password, because this installs for every user. Three things then exist: the framework, a folder in Applications holding Idle and the Python Launcher, and links so a terminal can find the interpreter.

## Files

- [`starter/route-one-the-installer-step-by-step.txt`](starter/route-one-the-installer-step-by-step.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/route-one-the-installer-step-by-step.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
