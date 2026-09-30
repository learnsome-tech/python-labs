# m09l04-01 · Split cuts a string into a list

**Lesson:** [Split And Join](https://learnsome.tech/learn/python-course/m09l04) (lesson 9.4, module 9: Objects And Methods) · Pro  
**Check:** Read along

## Goal

You can cut a string into a list of parts with split, with or without a separator, glue a sequence of strings back together with join, and use the pair in sequence to rewrite a phrase.

In the lesson: The split method has two forms. Called on a string s with empty parentheses, it splits s at any sequence of white space, meaning blanks, newlines and tabs, and returns the remaining parts of s as a list. Called with a string separator, that separator is what gets removed from between the parts of the list. Two things are worth noticing before we try it. The first form treats a whole run of white space as one separator, however long it is, and it throws away white space at the ends. The second form is literal: it removes exactly the separator you named, and nothing else. And in both cases what comes back is a list, not a string, so the type of the answer has changed.

## Files

- [`starter/split-cuts-a-string-into-a-list.txt`](starter/split-cuts-a-string-into-a-list.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/split-cuts-a-string-into-a-list.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m09l04-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
