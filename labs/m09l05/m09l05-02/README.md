# m09l05-02 · Building a list with append

**Lesson:** [Appending To Lists, Sets, Constructors](https://learnsome.tech/learn/python-course/m09l05) (lesson 9.5, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can grow a list with append inside a loop, explain why that differs from concatenation, build a set to remove duplicates, and recognise a type name used as a constructor.

In the lesson: Read this and watch how the list named words changes. Start from an empty list, built by calling list with nothing in the parentheses. Ask for it and the shell shows a pair of empty brackets. Append the first word and the shell prints nothing at all, because append returns None, the value that means nothing, and the shell does not display a None result; the work is done by changing the list. Ask for words again and it is one element long. Append another, and the new element goes on the end. Append a third and the list has grown again. There has been no assignment to words anywhere after the first line, and yet its contents keep changing. It has been the same list all along.

## Files

- [`starter/shell-building-a-list-with-append.py`](starter/shell-building-a-list-with-append.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l05/m09l05-02/starter`
2. Read `shell-building-a-list-with-append.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   words = list()
   words
   words.append('animal')
   words
   words.append('food')
   words
   words.append('city')
   words
   ```
4. Run it: `python3 -i < shell-building-a-list-with-append.py`.
5. Check it from the repository root: `./check m09l05-02`.

## Expected output

```text
[]
['animal']
['animal', 'food']
['animal', 'food', 'city']
```

## How to check

`./check m09l05-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-building-a-list-with-append.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
