# m02l03-05 · The externally managed environment refusal

**Lesson:** [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) (lesson 2.3, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can add the Python pieces your Linux distribution leaves out with apt, dnf or pacman, understand why pip refuses to install into the system Python, answer that refusal with a virtual environment, and verify the result with python3 and pip3.

In the lesson: Now the error that stops more beginners on Ubuntu than anything else. You install pip, you ask it for a package, and instead of downloading it pip refuses with the message on screen: this environment is externally managed. That is neither a bug nor a permissions problem. Your distribution has marked its Python as belonging to the package manager, and pip respects the mark, because installing there can overwrite a file the package manager owns and quietly break a system tool. Read the message instead of fighting it: it names two correct answers, and the standard behind it is P E P six six eight. There is a flag that overrides the refusal. Do not use it here.

## Files

- [`starter/apt-pip.sh`](starter/apt-pip.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/apt-pip.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
