# m18l04-07 · The externally managed environment error

**Lesson:** [pip, requirements, and installing packages](https://learnsome.tech/learn/python-course/m18l04) (lesson 18.4, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can install, inspect and remove packages with pip inside an activated environment, pin them in a requirements file that rebuilds the environment anywhere, and read the externally managed environment error correctly.

In the lesson: Sooner or later you will forget to activate, and on a Mac with Homebrew, or on most Linux systems, you will meet this. Read it as good news. It is saying: this Python belongs to the operating system, its package manager keeps track of these files, and if I let you write here I could break other software that depends on them. Notice that the error itself tells you the fix, in three lines: make an environment, activate it, install there. There is a flag that overrides the refusal, and you will find people online recommending it. Do not use it. It exists for people packaging operating systems. Every time you see this error, the correct response is to create or activate an environment.

## Files

- [`starter/the-externally-managed-environment-error.txt`](starter/the-externally-managed-environment-error.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-externally-managed-environment-error.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l04-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
