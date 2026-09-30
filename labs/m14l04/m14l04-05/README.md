# m14l04-05 · Testing a collection instead of its length

**Lesson:** [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) (lesson 14.4, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can say which values of any type Python treats as False, use the Pythonic test for an empty collection, and recognise the bugs that arise when a comparison and an or are combined carelessly.

In the lesson: A possibly useful consequence turns up in a fairly common situation, where something needs to be done with a list only if that list is nonempty. The explicit way is the first version: compare the length of the list with zero. Since an empty list converts to False and every other list converts to True, you can write the more succinct Pythonic idiom below it, naming the list itself as the condition. The two do the same work. The second one reads much more like English: if there is a list, deal with it.

## Files

- [`starter/testing-a-collection-instead-of-its-length.txt`](starter/testing-a-collection-instead-of-its-length.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/testing-a-collection-instead-of-its-length.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
