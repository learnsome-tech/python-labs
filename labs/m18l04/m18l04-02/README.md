# m18l04-02 · Installing something

**Lesson:** [pip, requirements, and installing packages](https://learnsome.tech/learn/python-course/m18l04) (lesson 18.4, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can install, inspect and remove packages with pip inside an activated environment, pin them in a requirements file that rebuilds the environment anywhere, and read the externally managed environment error correctly.

In the lesson: Here is a real install of requests, the library most people use to fetch things over the web. Read the transcript from the top. Pip collects requests, then notices that requests itself needs four other packages and collects those too, which is why you asked for one name and five arrived. Dependencies come along automatically, and that is both the convenience and the risk. The last line is the one to read: it lists every package that actually landed, with the exact version of each. Nothing outside this environment was touched. If you had not activated first, this is where things would have gone wrong, and the next few minutes cover exactly that case.

## Files

- [`starter/installing-something.txt`](starter/installing-something.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/installing-something.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
