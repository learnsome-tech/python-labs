# m07l01-04 · Trying a dictionary out in the shell

**Lesson:** [Dictionaries](https://learnsome.tech/learn/python-course/m07l01) (lesson 7.1, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can create a dictionary, add entries to it, look values up by key, recognise the KeyError a missing key raises, and test for a key with in.

In the lesson: Because the spanish dictionary is defined at the top level, the name is still there after the program finishes, so you can carry on exploring in the shell. Here we build a small one by hand. An assignment prints nothing back. Ask for the whole dictionary and Python shows the entries inside braces, each key paired with its value. Ask for one key and you get back one value. Now ask for a key that was never defined, purple, and Python raises a KeyError, naming the key it could not find. That is the trap worth remembering: a missing key is an error, not an empty answer. To ask safely, use the word in. It answers False for purple and True for red, and it never raises anything.

## Files

- [`starter/shell-trying-a-dictionary-out-in-the-shell.py`](starter/shell-trying-a-dictionary-out-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l01/m07l01-04/starter`
2. Read `shell-trying-a-dictionary-out-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   spanish = dict()
   spanish['hello'] = 'hola'
   spanish['red'] = 'rojo'
   spanish
   spanish['red']
   spanish['purple']
   'purple' in spanish
   'red' in spanish
   ```
4. Run it: `python3 -i < shell-trying-a-dictionary-out-in-the-shell.py`.
5. Check it from the repository root: `./check m07l01-04`.

## Expected output

```text
{'hello': 'hola', 'red': 'rojo'}
'rojo'
Traceback (most recent call last):
KeyError: 'purple'
False
True
```

## How to check

`./check m07l01-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-trying-a-dictionary-out-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
