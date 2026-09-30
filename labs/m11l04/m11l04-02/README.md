# m11l04-02 · The attempt, and why it looks right

**Lesson:** [Mutable Objects And Aliases](https://learnsome.tech/learn/python-course/m11l04) (lesson 11.4, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can explain why assigning one name from another gives two names for a single object, predict when mutating through one name is visible through the other, and use clone or a full slice to get a genuinely separate object.

In the lesson: Here is the first half of makeRectBad. The import brings in everything from the graphics module. Then comes makeRect, with a corner Point, a width and a height. The body does three things. It sets corner two from corner. It moves corner two across by the width and up by the height. Then it returns a Rectangle built from the two corners. Every line is defensible on its own, and the docstring states the contract clearly: return a new Rectangle given one corner Point and the dimensions. Notice the comment the author left on the definition line. He knew. Keep those middle three lines in mind, because that is where the trouble hides.

## Files

- [`starter/graphics.py`](starter/graphics.py)
- [`starter/makeRectBad.py`](starter/makeRectBad.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/makeRectBad.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: Here is the first half of makeRectBad
   - Lines 5–6: The import brings in
   - Lines 7–9: Then comes makeRect
   - Lines 10–12: returns a Rectangle built from the two corners
3. Notes from the lesson:
   - Line 8: The author's own comment: Incorrect!
   - Line 10: corner2 = corner copies nothing at all

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
