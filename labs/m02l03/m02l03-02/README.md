# m02l03-02 · Debian and Ubuntu: apt

**Lesson:** [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) (lesson 2.3, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can add the Python pieces your Linux distribution leaves out with apt, dnf or pacman, understand why pip refuses to install into the system Python, answer that refusal with a virtual environment, and verify the result with python3 and pip3.

In the lesson: On Debian, Ubuntu, Mint and their relatives the tool is apt, and the first command refreshes the list of what is available. Then one install line does the rest. Naming python three itself costs nothing when it is already there. What you are after are the extras, because Debian splits Python into pieces and installs only what the system needs. Pip, the installer for Python packages, is one package. The venv module, which makes the isolated environments you will use constantly, is another, and leaving it out causes a baffling error later. Idle is a third. The second line adds Tk, which the graphics work in this course needs, and a bundle that pulls in the rest.

## Files

- [`starter/debian-and-ubuntu-apt.txt`](starter/debian-and-ubuntu-apt.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/debian-and-ubuntu-apt.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
