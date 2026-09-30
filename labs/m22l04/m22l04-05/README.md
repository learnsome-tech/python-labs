# m22l04-05 · Building it into an installable package

**Lesson:** [Shipping: scripts, entry points and git](https://learnsome.tech/learn/python-course/m22l04) (lesson 22.4, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can turn a script into a command you can run from anywhere, describe your project in a pyproject file, build and install it, and keep its history in git.

In the lesson: With that file in place, one command turns your folder into the two files the Python world installs from. Run the build module and watch it work: it makes a clean environment, installs the build backend into it, and produces both a source archive, ending in tar dot g z, and a wheel, ending in dot w h l. The wheel is the fast one; it is what pip downloads for you every day. Both land in a new folder called dist. If you ever publish to the package index, those two files are what you upload. That is the whole build story, and you were one command away from it the entire time.

## Files

- [`starter/terminal`](starter/terminal): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/terminal` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
