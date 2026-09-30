# m07l01-05 · spanish2.py, part one: making the dictionary

**Lesson:** [Dictionaries](https://learnsome.tech/learn/python-course/m07l01) (lesson 7.1, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can create a dictionary, add entries to it, look values up by key, recognise the KeyError a missing key raises, and test for a key with in.

In the lesson: Creating the dictionary is a well defined activity, and quite different from the use of the dictionary at the end of the code, so we can use a function to encapsulate the creating. Here is the first part of spanish two. The heading defines createDictionary, which takes no parameters. Like whole files, functions can have a documentation string of its own immediately after the heading, and it is a good idea to document the return value. Then come the same nine assignments as before, indented into the body, building a local dictionary named spanish. The last line returns it. That local name is lost when the function terminates, so the object handed back had better be caught by somebody.

## Files

- [`starter/spanish2.py`](starter/spanish2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/spanish2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: Here is the first part
   - Lines 5–7: a documentation string of its own
   - Lines 8–17: the same nine assignments
   - Lines 18: The last line returns it

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l01-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
