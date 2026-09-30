# m09l03-04 · Slicing the word program

**Lesson:** [String Slices](https://learnsome.tech/learn/python-course/m09l03) (lesson 9.3, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

In the lesson: Predict and try each of these individually as well. Two to four gives the two characters at indices two and three. The second line mixes the two numbering schemes: start at index one, stop before minus three, the third character from the right end. That is legal, and often the clearest way to say drop the last three. Three onward runs to the end. Three to three is a slice of length zero, and Python hands back the empty string rather than complaining. And the last line takes the first character, then everything from index four on, cutting a chunk out of the middle.

## Files

- [`starter/shell-slicing-the-word-program.py`](starter/shell-slicing-the-word-program.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l03/m09l03-04/starter`
2. Read `shell-slicing-the-word-program.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   word = 'program'
   word[2:4]
   word[1:-3]
   word[3:]
   word[3:3]
   word[:1] + word[4:]
   ```
4. Run it: `python3 -i < shell-slicing-the-word-program.py`.
5. Check it from the repository root: `./check m09l03-04`.

## Expected output

```text
'og'
'rog'
'gram'
''
'pram'
```

## How to check

`./check m09l03-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-slicing-the-word-program.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
