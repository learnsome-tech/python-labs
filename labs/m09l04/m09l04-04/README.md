# m09l04-04 · Join is roughly the reverse of split

**Lesson:** [Split And Join](https://learnsome.tech/learn/python-course/m09l04) (lesson 9.4, module 9: Objects And Methods) · Pro  
**Check:** Read along

## Goal

You can cut a string into a list of parts with split, with or without a separator, glue a sequence of strings back together with join, and use the pair in sequence to rewrite a phrase.

In the lesson: Join is roughly the reverse of split: it joins together a sequence of strings. The syntax is rather different from what you would guess, and this is the thing to fix in your memory. The separator comes first, because the separator is the piece with the right type, a string, and join is a string method. So the object before the dot is the separator, and the sequence you want glued together goes inside the parentheses. Join returns a new string obtained by joining the sequence of strings into one, interleaving the separator between the elements of the sequence. The list itself is untouched, as always.

## Files

- [`starter/join-is-roughly-the-reverse-of-split.txt`](starter/join-is-roughly-the-reverse-of-split.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/join-is-roughly-the-reverse-of-split.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m09l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
