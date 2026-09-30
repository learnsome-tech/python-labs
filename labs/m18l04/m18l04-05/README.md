# m18l04-05 · Pinning, and the requirements file

**Lesson:** [pip, requirements, and installing packages](https://learnsome.tech/learn/python-course/m18l04) (lesson 18.4, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can install, inspect and remove packages with pip inside an activated environment, pin them in a requirements file that rebuilds the environment anywhere, and read the externally managed environment error correctly.

In the lesson: Now make the environment reproducible. Pip freeze prints exactly what is installed, with two equals signs and an exact version for each, which is called pinning. Send that to a file called requirements dot txt and commit the file. Anybody, including you on another machine next year, makes an environment and runs pip install dash r on that file, and gets byte for byte the same set of packages. Why pin? Because a library that updates itself under you is a bug that appears on a day you changed nothing. Pinning moves that decision to a moment of your choosing: you edit the version, you run the install, you run your tests, you commit. The environment is disposable. The file is the truth.

## Files

- [`starter/pinning-and-the-requirements-file.py`](starter/pinning-and-the-requirements-file.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pinning-and-the-requirements-file.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
