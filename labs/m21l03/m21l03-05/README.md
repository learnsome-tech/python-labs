# m21l03-05 · The one sentence about time zones

**Lesson:** [Dates, Times And Random](https://learnsome.tech/learn/python-course/m21l03) (lesson 21.3, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Read along

## Goal

You can make and compare dates, do arithmetic with timedelta, format and parse them with strftime and strptime, and generate random numbers you can reproduce with a seed.

In the lesson: Here is the one sentence of truth about time zones: a datetime with no zone attached does not know where it is, so the moment two places are involved you must attach a real zone or you are guessing. Everything else follows from that. A plain datetime is called naive and is perfectly fine for a shopping list of appointments on one desk. As soon as your program has users in two cities, or a clock that goes forward in spring, you want zone aware values. The professional habit is to store and calculate in coordinated universal time, usually written u t c, and convert to a local zone only when you show it to somebody. The zone info module, in the standard library, holds the real world's zones and their history of changes.

## Files

- [`starter/the-one-sentence-about-time-zones.py`](starter/the-one-sentence-about-time-zones.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-one-sentence-about-time-zones.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m21l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
