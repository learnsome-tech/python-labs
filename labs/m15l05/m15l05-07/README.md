# m15l05-07 · The cgi module, in three lines

**Lesson:** [Chapter Four In One Sitting](https://learnsome.tech/learn/python-course/m15l05) (lesson 15.5, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can recite the order of work for building a dynamic web page, and say what each piece of markup, each cgi module call and each error location is for.

In the lesson: The cgi module gives you three things. Create the object that processes the input with the first line on screen. Extract the first value the browser specified under a given name, or a default if there is no such value, with the second. And extract the list of all values associated with a name with the third, which is the case when you have several check boxes sharing one name and different values; that list may be empty. Those three lines, plus the names in your form matching the names in your calls, are the whole interface between a browser and your program. One caution: the cgi module was removed from the standard library in Python three point thirteen, so treat these lines as the historical form, and on a current interpreter read the query string with the URL lib parse module, or install the third party multipart package.

## Files

- [`starter/the-cgi-module-in-three-lines.py`](starter/the-cgi-module-in-three-lines.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-cgi-module-in-three-lines.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l05-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
