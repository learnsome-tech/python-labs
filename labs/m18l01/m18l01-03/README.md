# m18l01-03 · Choosing the form that reads best

**Lesson:** [Modules And The Import System](https://learnsome.tech/learn/python-course/m18l01) (lesson 18.1, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can split code across files with import, explain what happens the first time a module is imported, protect a file's own test code with the main guard, and say where Python looked to find a module.

In the lesson: All three forms work, so the choice is about the reader. The plain form keeps the origin visible: six months later, math dot sqrt tells you exactly where sqrt came from, and a bare sqrt does not. That is why the plain form is the default. The from form earns its place when one name is used constantly, or when you want a single thing out of a large module. The as form is for abbreviations the community has already agreed on, and for nothing else. And there is one form to avoid: from a module import star, where the star means everything. It drags in names you never asked for, and if two modules both define a function called count, the second import silently wins. Be explicit and you will never have to debug that.

## Files

- [`starter/choosing-the-form-that-reads-best.py`](starter/choosing-the-form-that-reads-best.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/choosing-the-form-that-reads-best.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
