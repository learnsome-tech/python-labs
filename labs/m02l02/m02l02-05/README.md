# m02l02-05 · Install Certificates.command, and why

**Lesson:** [Installing Python On A Mac](https://learnsome.tech/learn/python-course/m02l02) (lesson 2.2, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can install your own Python on a Mac by either the python.org installer or Homebrew, leave Apple's system python3 untouched, put yours first on PATH from your zsh profile, and confirm the result with python3 and idle3.

In the lesson: One step people skip, and then lose an evening to. In that Applications folder, double click install certificates dot command. A terminal opens for a few seconds, your new Python downloads a package called certifi, and the certificate file inside the framework is pointed at it. When the words on screen appear, close the window. Why is it needed? This Python does not use the trust store that Safari and macOS use, so it trusts no certificate authority at all. Without this step, every fetch over a secure connection fails with a certificate verify failed error, and that message never points back here.

## Files

- [`starter/install-certificates-command-and-why.txt`](starter/install-certificates-command-and-why.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/install-certificates-command-and-why.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
