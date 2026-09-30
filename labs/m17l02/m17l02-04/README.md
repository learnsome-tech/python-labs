# m17l02-04 · Validating an argument, and the caller catching it

**Lesson:** [Raising, And Writing Your Own Exception](https://learnsome.tech/learn/python-course/m17l02) (lesson 17.2, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can raise a built-in exception with a useful message to refuse bad input, re-raise after logging, chain one exception to another, and define a small exception class of your own when the situation calls for it.

In the lesson: Two guards now, one for each kind of nonsense, each raising the exception a reader would expect. And here is the other half of the story: a caller who is ready. The except clause names both types in parentheses, which is how you write one handler for several exceptions, and the as clause gives us the object so the message can go into our own report. Three candidates go in, and the loop survives all three. Notice how the labour is divided. The function knows what counts as valid and says no. The caller knows what to do about a no, which here is to print a line and carry on. Neither of them needs to know the other's business.

## Files

- [`starter/setagecaught.py`](starter/setagecaught.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l02/m17l02-04/starter`
2. Read `setagecaught.py`.
3. Run it: `python3 setagecaught.py`.
4. Check it from the repository root: `./check m17l02-04`.

## Expected output

```text
accepted 30
rejected -3 - age cannot be negative: -3
rejected 'forty' - age must be a whole number
```

## How to check

`./check m17l02-04` copies `starter/` into a scratch directory and runs `python3 setagecaught.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
