# m10l02 · Mad Libs Revisited: The Whole Program

Module 10: Mad Libs Revisited · lesson 10.2 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m10l02)

**Goal:** You can read the revised mad lib program function by function, explain why getKeys returns a set, and name the creative problem solving steps that produced it.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m10l02-03](m10l02-03/) | One blemish left: the duplicates | Read along |
| [m10l02-04](m10l02-04/) | getKeys, now returning a set | Read along |
| [m10l02-05](m10l02-05/) | One pick, and all the picks | Read along |
| [m10l02-06](m10l02-06/) | The story teller in five lines | Read along |
| [m10l02-07](m10l02-07/) | A whole play-through | Read along |
| [m10l02-08](m10l02-08/) | An exercise in the same shape | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Substring Locations Exercise

1. Rename the example file locationsStub.py to locations.py.
2. Complete printLocations so it prints the index of each place target occurs in s.
3. Run the file: the main function tries the targets ere, er, e, eh and zx on one phrase.
4. Check that a target that never appears prints nothing at all, and does not crash.

> **Hint:** The stub already uses the count method. Add an initialisation before the loop, and inside it use find with a starting position, exactly as getKeys does.

## Check yourself

- Why does getKeys return a set rather than the list it accumulates?
- What do you give up by using a set, and why does it not matter here?
- Which function holds the story, and which function receives it as a parameter?
- Why does addPick need no return statement?
- Which creative problem solving step does initialising end to zero illustrate?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
