# m06l03-08 · Reading a traceback through nested calls

**Lesson:** [Function Parameters](https://learnsome.tech/learn/python-course/m06l03) (lesson 6.3, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function with a parameter, call it with different arguments, and explain how a formal parameter is given the value of an actual parameter at the moment of the call.

In the lesson: Now that we have nested calls, it is worth looking further at tracebacks. Add one line to main in birthday seven, passing the number two instead of a name, as in the example file birthday bad, and run it. The last lines matter most: the line number where the error was detected, the text of that line, and a description of the problem. Python will not add a number to a string. Often that is all you need. But this example shows that the genesis of a problem may be far from where it was detected. Going further up the traceback you find the sequence of calls that led there, and you can see that main called happyBirthday with the bad parameter.

## Files

- [`starter/birthdayBad.py`](starter/birthdayBad.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-08/starter`
2. Read `birthdayBad.py`.
3. Notes from the lesson:
   - Line 13: a number where the function expects a string
4. Run it: `python3 birthdayBad.py`.
5. Check it from the repository root: `./check m06l03-08`.

## Expected output

```text
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Emily.
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Andre.
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday to you!
Traceback (most recent call last):
  File "birthdayBad.py", line 15, in <module>
    main()
    ~~~~^^
  File "birthdayBad.py", line 13, in main
    happyBirthday(2)
    ~~~~~~~~~~~~~^^^
  File "birthdayBad.py", line 6, in happyBirthday
    print("Happy Birthday, dear " + person + ".")
          ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~
TypeError: can only concatenate str (not "int") to str
```

## How to check

`./check m06l03-08` copies `starter/` into a scratch directory and runs `python3 birthdayBad.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
