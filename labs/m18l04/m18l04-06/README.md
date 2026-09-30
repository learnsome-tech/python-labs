# m18l04-06 · Removing, and installing your own project

**Lesson:** [pip, requirements, and installing packages](https://learnsome.tech/learn/python-course/m18l04) (lesson 18.4, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can install, inspect and remove packages with pip inside an activated environment, pin them in a requirements file that rebuilds the environment anywhere, and read the externally managed environment error correctly.

In the lesson: Uninstall takes the package name and asks for confirmation. Notice what it does not do: the four dependencies requests brought in are still there afterwards, because pip does not know whether something else wants them. Over months an environment collects those orphans, and the honest cleanup is to delete the environment and rebuild it from your requirements file, which is one more reason to keep that file good. One more form worth knowing now and using in the last module: pip install dash e followed by a dot installs the project in the current folder in editable mode, so your own package is importable from anywhere while you carry on editing it in place.

## Files

- [`starter/removing-and-installing-your-own-project.txt`](starter/removing-and-installing-your-own-project.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/removing-and-installing-your-own-project.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l04-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
