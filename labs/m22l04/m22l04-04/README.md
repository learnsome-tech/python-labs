# m22l04-04 · pyproject.toml: describing the project

**Lesson:** [Shipping: scripts, entry points and git](https://learnsome.tech/learn/python-course/m22l04) (lesson 22.4, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can turn a script into a command you can run from anywhere, describe your project in a pyproject file, build and install it, and keep its history in git.

In the lesson: One file describes the whole project, and it is called pyproject dot toml. Toml is the configuration format we mentioned two lessons ago, and it is mostly headings in square brackets and settings underneath. The project section is the part a beginner needs: a name, a version and its dependencies, which are the packages pip must install alongside your code. Then the entry point: this line says that a command called wordcount should run the main function in the c l i module of your package, and installing the project creates that command for you. Last, the build system section names the program that does the packaging; hatchling is a fine default and you can copy those two lines unchanged.

## Files

- [`starter/pyproject.toml`](starter/pyproject.toml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pyproject.toml` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: a name, a version and its dependencies
   - Lines 7–9: the entry point
   - Lines 10–13: the build system
3. Notes from the lesson:
   - Line 6: what pip must install alongside your code
   - Line 9: the command name, then the module and function to call

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
