# m02l02-02 · What the two Pythons actually report

**Lesson:** [Installing Python On A Mac](https://learnsome.tech/learn/python-course/m02l02) (lesson 2.2, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can install your own Python on a Mac by either the python.org installer or Homebrew, leave Apple's system python3 untouched, put yours first on PATH from your zsh profile, and confirm the result with python3 and idle3.

In the lesson: Here are three commands worth knowing, run on the Mac I am recording this on. The first asks the shell for every python three it can find, in the order it would try them. Two come back: mine from Homebrew, and Apple's underneath. The second asks Apple's copy for its version, and it says three point nine point six. The third asks the one my shell actually uses, with the doubled flag that prints build details too, and says three point fourteen point seven. Two Pythons, both fine. Whichever path prints first is the Python you get when you type python three.

## Files

- [`starter/mac-python3.sh`](starter/mac-python3.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/mac-python3.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
