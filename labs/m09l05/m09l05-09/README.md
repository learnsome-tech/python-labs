# m09l05-09 · A set can drive a for loop

**Lesson:** [Appending To Lists, Sets, Constructors](https://learnsome.tech/learn/python-course/m09l05) (lesson 9.5, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can grow a list with append inside a loop, explain why that differs from concatenation, build a set to remove duplicates, and recognise a type name used as a constructor.

In the lesson: Rebuild the set, and now the useful part: like other collections, a set can be used as the sequence in a for loop. The loop variable takes each element of the set in turn and we print one element per line. The tutorial writes this loop directly over the set, which is the shape to remember. On screen I have wrapped the set in sorted so the five lines come out in the same order every time, because a bare set may hand its elements over in any order it likes.

## Files

- [`starter/shell-a-set-can-drive-a-for-loop.py`](starter/shell-a-set-can-drive-a-for-loop.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l05/m09l05-09/starter`
2. Read `shell-a-set-can-drive-a-for-loop.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   strList = ['z', 'zz', 'c', 'z', 'bb', 'z', 'a', 'c']
   aSet = set(strList)
   for s in sorted(aSet):
       print(s)
   ```
4. Run it: `python3 -i < shell-a-set-can-drive-a-for-loop.py`.
5. Check it from the repository root: `./check m09l05-09`.

## Expected output

```text
a
bb
c
z
zz
```

## How to check

`./check m09l05-09` copies `starter/` into a scratch directory and runs `python3 -i < shell-a-set-can-drive-a-for-loop.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
