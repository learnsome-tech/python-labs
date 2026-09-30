# m09l04-03 · Predicting split with different separators

**Lesson:** [Split And Join](https://learnsome.tech/learn/python-course/m09l04) (lesson 9.4, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can cut a string into a list of parts with split, with or without a separator, glue a sequence of strings back together with join, and use the pair in sequence to rewrite a phrase.

In the lesson: Predict and test each line. Splitting on white space gives five pieces. Notice that the colon stays attached to Go, and that the double space between Go and Tear counts as one separator rather than two. Split on the colon instead and you get only two pieces, and the two leading blanks of the second piece survive, because only the colon itself is removed. Split on the two letters a and r and the separator disappears from the middle of words, leaving three ragged pieces; a separator does not have to be punctuation. The last pair of lines uses a string with newline escapes in it. Printing it shows three lines. Split with no argument treats newlines as white space, along with blanks and tabs, so five words come back.

## Files

- [`starter/shell-predicting-split-with-different-separators.py`](starter/shell-predicting-split-with-different-separators.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l04/m09l04-03/starter`
2. Read `shell-predicting-split-with-different-separators.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   line = 'Go:  Tear some strings apart!'
   seq = line.split()
   seq
   line.split(':')
   line.split('ar')
   lines = 'This includes\nsome new\nlines.'
   print(lines)
   lines.split()
   ```
4. Run it: `python3 -i < shell-predicting-split-with-different-separators.py`.
5. Check it from the repository root: `./check m09l04-03`.

## Expected output

```text
['Go:', 'Tear', 'some', 'strings', 'apart!']
['Go', '  Tear some strings apart!']
['Go:  Te', ' some strings ap', 't!']
This includes
some new
lines.
['This', 'includes', 'some', 'new', 'lines.']
```

## How to check

`./check m09l04-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-predicting-split-with-different-separators.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
