# m17l02-06 · raise from: this failure because of that one

**Lesson:** [Raising, And Writing Your Own Exception](https://learnsome.tech/learn/python-course/m17l02) (lesson 17.2, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can raise a built-in exception with a useful message to refuse bad input, re-raise after logging, chain one exception to another, and define a small exception class of your own when the situation calls for it.

In the lesson: One more piece of the raise statement, in a sentence. When you catch a low level exception and raise a friendlier one in its place, write raise, then your new exception, then the word from, then the caught object: that records the original as the direct cause, so nothing is lost. On screen you get two tracebacks joined by a line saying the above exception was the direct cause of the following exception. The reader learns both facts: a settings file is incomplete, and underneath, the missing key was called port. Without the word from you would still get both, but described as merely happening during handling, which is the wording you meet in the next lesson.

## Files

- [`starter/chainfrom.py`](starter/chainfrom.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l02/m17l02-06/starter`
2. Read `chainfrom.py`.
3. Run it: `python3 chainfrom.py`.
4. Check it from the repository root: `./check m17l02-06`.

## Expected output

```text
Traceback (most recent call last):
  File "chainfrom.py", line 5, in port
    return settings['port']
           ~~~~~~~~^^^^^^^^
KeyError: 'port'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "chainfrom.py", line 9, in <module>
    print(port())
          ~~~~^^
  File "chainfrom.py", line 7, in port
    raise RuntimeError('the settings file is incomplete') from err
RuntimeError: the settings file is incomplete
```

## How to check

`./check m17l02-06` copies `starter/` into a scratch directory and runs `python3 chainfrom.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
