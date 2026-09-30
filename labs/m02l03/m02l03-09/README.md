# m02l03-09 · The escape hatch: source, or pyenv

**Lesson:** [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) (lesson 2.3, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can add the Python pieces your Linux distribution leaves out with apt, dnf or pacman, understand why pip refuses to install into the system Python, answer that refusal with a virtual environment, and verify the result with python3 and pip3.

In the lesson: Sometimes your distribution's Python really is too old, on a long term server release for example. Two escape hatches, one sentence each. Building from source is the honest one: install a compiler and the development libraries, run the configure script, make, and then the important word, make altinstall, which puts your new interpreter beside the system one under its full version name instead of stealing the plain python three link. The other is pyenv, which does all of that for you, building any version you name and switching between them per directory. Neither is a beginner's first move. Reach for a virtual environment first, distribution packages second, and these only when a version you need is missing.

## Files

- [`starter/the-escape-hatch-source-or-pyenv.txt`](starter/the-escape-hatch-source-or-pyenv.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-escape-hatch-source-or-pyenv.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
