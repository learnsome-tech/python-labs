# m02l03-01 · Linux already has Python, and it is not yours

**Lesson:** [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) (lesson 2.3, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can add the Python pieces your Linux distribution leaves out with apt, dnf or pacman, understand why pip refuses to install into the system Python, answer that refusal with a virtual environment, and verify the result with python3 and pip3.

In the lesson: Linux is the easy platform in one way and the strict one in another. The easy part: open a terminal on almost any current distribution, ask python three for its version, and you get a real answer, because a recent Python is already installed. The strict part is why it is there. It is the system's own Python. Programs that hold the machine together are written in it, including the package manager itself on Fedora and a long list of tools on Debian and Ubuntu. So the rule here differs from Windows or a Mac: you are not installing Python, you are adding the parts your distribution left out, and never removing what is there.

## Files

- [`starter/linux-already-has-python-and-it-is-not-yours.txt`](starter/linux-already-has-python-and-it-is-not-yours.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/linux-already-has-python-and-it-is-not-yours.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
