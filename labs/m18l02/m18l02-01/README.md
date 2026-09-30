# m18l02-01 · A package is a folder of modules

**Lesson:** [Packages, And Your Own Library](https://learnsome.tech/learn/python-course/m18l02) (lesson 18.2, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can lay out a project as a package of modules with a script beside it, import between those modules with absolute imports, and run any module inside the package with the dash m switch.

In the lesson: One file was a module. Once a project has six or ten files, you want them in a folder, and a folder of modules is a package. On screen is the layout we will build: a project folder holding one script, main dot py, and beside it a folder called weather holding three files. That folder is the package, and its name is the package name, so choose it as carefully as you would choose a function name. Inside the program you refer to those files with dotted names: weather dot readings means the readings module inside the weather package. The dots in an import statement are folder separators. That is really all a package is. The rest of this lesson is the details that trip people up.

## Files

- [`starter/a-package-is-a-folder-of-modules.txt`](starter/a-package-is-a-folder-of-modules.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/a-package-is-a-folder-of-modules.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l02-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
