# m21l03 · Dates, Times And Random

Module 21: Files, Formats And The Standard Library · lesson 21.3 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m21l03)

**Goal:** You can make and compare dates, do arithmetic with timedelta, format and parse them with strftime and strptime, and generate random numbers you can reproduce with a seed.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m21l03-01](m21l03-01/) | A date is a value, not a piece of text | Read along |
| [m21l03-02](m21l03-02/) | What time is it now? | Graded |
| [m21l03-03](m21l03-03/) | Building dates and doing arithmetic | Graded |
| [m21l03-04](m21l03-04/) | Printing and parsing: strftime and strptime | Graded |
| [m21l03-05](m21l03-05/) | The one sentence about time zones | Read along |
| [m21l03-06](m21l03-06/) | Random numbers, and the same ones again | Graded |
| [m21l03-07](m21l03-07/) | Shuffling, sampling and repeated choices | Graded |
| [m21l03-08](m21l03-08/) | Not for anything secret | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### A quiz that remembers when

1. Write quizTime.py that asks five addition questions with randint numbers.
2. Seed the generator from a number the user types, so a quiz can be repeated.
3. Record the start and end time and report how long the quiz took.
4. Append one line per attempt to a log file: the date, the score and the seed.

> **Hint:** Subtracting two datetime values gives a timedelta, and total seconds turns it into a number you can round.

## Check yourself

- Why is holding a date as a string a bad idea?
- What do you get when you subtract one date from another, and what can you ask it?
- Which method turns a datetime into text, and which reads text into a datetime?
- What does it mean to call a datetime naive?
- Why would you seed the random generator, and when must you not use random at all?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
