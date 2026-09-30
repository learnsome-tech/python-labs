# m10l01-06 · Finding braces, one experiment at a time

**Lesson:** [Mad Libs Revisited: Finding The Cues](https://learnsome.tech/learn/python-course/m10l01) (lesson 10.1, module 10: Mad Libs Revisited) · Pro  
**Check:** Graded

## Goal

You can write a function that scans a format string and returns the list of cues embedded in it, and you can follow the creative process that produced it.

In the lesson: Now to the shell, with the short story in a variable. The count method says there are two open braces, so two keys. The find method puts the first open brace at index five, but the key itself starts one place later, so we add one and get six. Then find on the closing brace gives twelve, which is one past the last character of the key, and one past the end is precisely what a slice wants. Take that slice and we get animal. For the second key we search onwards from the end of the first, so we hand find a starting position too, and the slice gives food. Without that, find would keep returning the very first brace.

## Files

- [`starter/shell-finding-braces-one-experiment-at-a-time.py`](starter/shell-finding-braces-one-experiment-at-a-time.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m10l01/m10l01-06/starter`
2. Read `shell-finding-braces-one-experiment-at-a-time.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   story = 'blah {animal} blah blah {food} ...'
   story.count('{')
   story.find('{')
   story.find('{') + 1
   story.find('}')
   story[6 : 12]
   story.find('{', 12) + 1
   story.find('}', 25)
   story[25 : 29]
   ```
4. Run it: `python3 -i < shell-finding-braces-one-experiment-at-a-time.py`.
5. Check it from the repository root: `./check m10l01-06`.

## Expected output

```text
2
5
6
12
'animal'
25
29
'food'
```

## How to check

`./check m10l01-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-finding-braces-one-experiment-at-a-time.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
