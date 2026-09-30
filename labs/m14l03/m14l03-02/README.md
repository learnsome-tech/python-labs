# m14l03-02 · Imagining a concrete sequence of clicks

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: Creating a polygon is a unified activity with a clear result, so make it a function that takes a boundary rectangle and a window and returns the polygon it builds. Start by naming the objects: a polygon, called poly; a list of vertices, called vertices, initialised before anything is appended; and the latest mouse click, called pt. When the loop is not yet clear, write out a concrete case with no loop at all. Here is the sequence for a triangle: three clicks inside the rectangle, then a fourth outside. Watch how each old polygon is undrawn first, or it would leave stray lines behind.

## Files

- [`starter/polyDraft.py`](starter/polyDraft.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/polyDraft.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: Start by naming the objects
   - Lines 5–7: the latest mouse click
   - Lines 8–13: write out a concrete case
   - Lines 14–21: each old polygon is undrawn
3. Notes from the lesson:
   - Line 9: Undraw the old polygon before the one with the extra vertex appears

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
