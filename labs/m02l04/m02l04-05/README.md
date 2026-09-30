# m02l04-05 · The module search path, and one nasty bug

**Lesson:** [Where Python Lives: PATH And Versions](https://learnsome.tech/learn/python-course/m02l04) (lesson 2.4, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can explain how a command name becomes a program on disk, tell python, python3 and py apart on any of the three operating systems, and ask an interpreter for its own path, version and module search path.

In the lesson: That path list deserves a second look, because it explains a bug that feels like magic. When you run a file, the first entry is the folder that file is in. In an interactive shell the first entry is empty, which means the folder you happen to be sitting in. Then come the standard library folders, and last of all the site packages folder, where anything you install ends up. An import walks that list in order and takes the first hit. So a file of your own called random dot py, sitting in your own folder, is found before the standard library's random module, and every import of random in that folder gets yours instead.

## Files

- [`starter/the-module-search-path-and-one-nasty-bug.txt`](starter/the-module-search-path-and-one-nasty-bug.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-module-search-path-and-one-nasty-bug.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
