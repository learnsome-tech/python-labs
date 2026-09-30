# m02l03-06 · The right answer: a venv, or the package

**Lesson:** [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) (lesson 2.3, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can add the Python pieces your Linux distribution leaves out with apt, dnf or pacman, understand why pip refuses to install into the system Python, answer that refusal with a virtual environment, and verify the result with python3 and pip3.

In the lesson: There are two right answers and one convenience. The first is a virtual environment: you ask Python to build a small private tree, activate it, and from then on pip installs into your tree rather than the system one, with no flags and no risk. The lines on screen do exactly that. A later module is devoted to these, so treat this as the emergency version. The second is to let the distribution install the library, when it packages the one you want; that is what the error message suggested. The convenience is pipx, for programs rather than libraries: each tool gets its own environment, and only its command goes on your path.

## Files

- [`starter/the-right-answer-a-venv-or-the-package.txt`](starter/the-right-answer-a-venv-or-the-package.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-right-answer-a-venv-or-the-package.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
