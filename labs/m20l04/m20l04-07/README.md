# m20l04-07 · __len__ and __getitem__ make it a sequence

**Lesson:** [Dunder Methods, And Making Objects Pythonic](https://learnsome.tech/learn/python-course/m20l04) (lesson 20.4, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can give a class a useful repr and str, define equality and hashing consistently, make an object work with len, indexing and a for loop, and reach for a dataclass when the class is plain data.

In the lesson: This is where dunder methods start to feel like a superpower. A deck holds a list of cards. Dunder len hands back the length of that list, and dunder getitem hands back one item by index. Two small methods, and look what the deck can suddenly do. The length function works. Square brackets work, including negative indexes, because we passed the index straight through to the list. The for loop works, because a for loop over an object with no other support asks for item zero, then item one, and so on until it runs out. And the in operator comes along for the ride, since it walks those same items. Your class now behaves the way every Python programmer already expects.

## Files

- [`starter/deckSequence.py`](starter/deckSequence.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l04/m20l04-07/starter`
2. Read `deckSequence.py` the way the lesson builds it:
   - Lines 1–8: Dunder len hands back
   - Lines 9–11: dunder getitem hands back
   - Lines 12–18: the length function works
3. Notes from the lesson:
   - Line 8: len(deck) now works, by asking the list inside
   - Line 11: square brackets, including negative indexes, come free
   - Line 16: a for loop needs only __getitem__: it counts up from zero
   - Line 18: and in works too, because it walks the same items
4. Run it: `python3 deckSequence.py`.
5. Check it from the repository root: `./check m20l04-07`.

## Expected output

```text
3
ace queen
ace
king
queen
True
```

## How to check

`./check m20l04-07` copies `starter/` into a scratch directory and runs `python3 deckSequence.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
