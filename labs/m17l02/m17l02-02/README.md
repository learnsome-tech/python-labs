# m17l02-02 · raise, with a built-in exception and a message

**Lesson:** [Raising, And Writing Your Own Exception](https://learnsome.tech/learn/python-course/m17l02) (lesson 17.2, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can raise a built-in exception with a useful message to refuse bad input, re-raise after logging, chain one exception to another, and define a small exception class of your own when the situation calls for it.

In the lesson: Here it is in three lines. The guard comes first: if the argument makes no sense, raise a ValueError with a message that names the bad value. Only if the guard lets the value through do we reach the ordinary return. Now run the good call and the bad one. Thirty is fine and prints. Minus three raises, and because nothing in this program handles it, you get a traceback whose bottom line is exactly the sentence we wrote. Look at the frames above it. The lower frame is the raise itself, and the frame above shows the call that supplied the bad argument, which is the line the author of that call needs to look at. That is why a specific message pays for itself.

## Files

- [`starter/setage.py`](starter/setage.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l02/m17l02-02/starter`
2. Read `setage.py` the way the lesson builds it:
   - Lines 1–3: the guard comes first
   - Lines 4: the ordinary return
   - Lines 5–7: the good call and the bad one
3. Notes from the lesson:
   - Line 3: raise, the exception type, and a message that names the bad value
4. Run it: `python3 setage.py`.
5. Check it from the repository root: `./check m17l02-02`.

## Expected output

```text
30
Traceback (most recent call last):
  File "setage.py", line 7, in <module>
    print(set_age(-3))
          ~~~~~~~^^^^
  File "setage.py", line 3, in set_age
    raise ValueError('age cannot be negative: ' + str(years))
ValueError: age cannot be negative: -3
```

## How to check

`./check m17l02-02` copies `starter/` into a scratch directory and runs `python3 setage.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
