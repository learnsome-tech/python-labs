# m18l04-03 · Looking at what you have

**Lesson:** [pip, requirements, and installing packages](https://learnsome.tech/learn/python-course/m18l04) (lesson 18.4, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can install, inspect and remove packages with pip inside an activated environment, pin them in a requirements file that rebuilds the environment anywhere, and read the externally managed environment error correctly.

In the lesson: Pip list shows everything installed in this environment with its version, and the list should be short: one line per thing you deliberately asked for, plus their dependencies. Pip show asks about one package. It gives the version, a one line summary, and two lines worth knowing. Location is the folder the files were written to, inside your environment. Requires is what this package pulled in. Required-by is empty here, which tells you nothing else depends on requests, so it is safe to remove. On a dependency it would list the package that needs it, which is how you find out why something you never asked for is installed.

## Files

- [`starter/looking-at-what-you-have.txt`](starter/looking-at-what-you-have.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/looking-at-what-you-have.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
