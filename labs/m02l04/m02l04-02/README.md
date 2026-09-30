# m02l04-02 · Watching the search happen

**Lesson:** [Where Python Lives: PATH And Versions](https://learnsome.tech/learn/python-course/m02l04) (lesson 2.4, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can explain how a command name becomes a program on disk, tell python, python3 and py apart on any of the three operating systems, and ask an interpreter for its own path, version and module search path.

In the lesson: You can watch that lookup happen. On the Mac recording this course, asking which folders hold something called python three gives two answers, listed in the order the shell would try them. The first is a Python installed with Homebrew. The second is the one Apple ships. Because the Homebrew folder comes earlier on PATH, the first is the one that answers, and the versions prove it: the plain command reports three point fourteen point seven, while Apple's copy, asked directly by its full path, reports three point nine point six. Two Pythons, both perfectly real, and only one of them answering to the short name.

## Files

- [`starter/watching-the-search-happen.txt`](starter/watching-the-search-happen.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/watching-the-search-happen.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
