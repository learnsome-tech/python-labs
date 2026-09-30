# m17l03-02 · Four frames, from four real calls

**Lesson:** [Reading A Traceback Like A Professional](https://learnsome.tech/learn/python-course/m17l03) (lesson 17.3, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can read a multi-frame traceback bottom up, tell your own frames from a library's, recognise the errors that arrive before execution starts, and name the likely cause behind each of the common exception types.

In the lesson: Three small functions that turn text into scores and add them up. The first call works and prints eighteen. The second call brings the whole thing down, and because the calls are nested three deep the traceback has four frames. Read it as a story from the top. The module level line thirteen called report. Report called total score. Total score called parse row, inside a list comprehension. And parse row was in the middle of converting when it gave up. Notice the word in at the end of each File line: it names the function that frame is inside, and the outermost one says module, meaning the body of the file itself.

## Files

- [`starter/rowreport.py`](starter/rowreport.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l03/m17l03-02/starter`
2. Read `rowreport.py`.
3. Run it: `python3 rowreport.py`.
4. Check it from the repository root: `./check m17l03-02`.

## Expected output

```text
total is 18
Traceback (most recent call last):
  File "rowreport.py", line 13, in <module>
    report('ana,7;bo,eleven')
    ~~~~~~^^^^^^^^^^^^^^^^^^^
  File "rowreport.py", line 10, in report
    print('total is', total_score(text))
                      ~~~~~~~~~~~^^^^^^
  File "rowreport.py", line 6, in total_score
    rows = [parse_row(row) for row in text.split(';')]
            ~~~~~~~~~^^^^^
  File "rowreport.py", line 3, in parse_row
    return (name, int(score))
                  ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: 'eleven'
```

## How to check

`./check m17l03-02` copies `starter/` into a scratch directory and runs `python3 rowreport.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
