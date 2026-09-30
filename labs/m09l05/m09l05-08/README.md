# m09l05-08 · Making a set, and predicting its size

**Lesson:** [Appending To Lists, Sets, Constructors](https://learnsome.tech/learn/python-course/m09l05) (lesson 9.5, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can grow a list with append inside a loop, explain why that differs from concatenation, build a set to remove duplicates, and recognise a type name used as a constructor.

In the lesson: The list has eight elements, but only five of them are different. Convert it to a set and ask for the length: the length is five, whatever order your interpreter chooses. Because the order is not guaranteed, I am passing the set to the sorted function to get a predictable listing on screen. Now predict this one before you run it. Six strings go in, three of them distinct. Ask how many elements the set has, and then which ones. You may not guess Python's own order, but you should get the right length and the right elements in some order.

## Files

- [`starter/shell-making-a-set-and-predicting-its-size.py`](starter/shell-making-a-set-and-predicting-its-size.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l05/m09l05-08/starter`
2. Read `shell-making-a-set-and-predicting-its-size.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   strList = ['z', 'zz', 'c', 'z', 'bb', 'z', 'a', 'c']
   aSet = set(strList)
   len(aSet)
   sorted(aSet)
   dupes = ['animal', 'food', 'animal', 'food', 'food', 'city']
   len(set(dupes))
   sorted(set(dupes))
   ```
4. Run it: `python3 -i < shell-making-a-set-and-predicting-its-size.py`.
5. Check it from the repository root: `./check m09l05-08`.

## Expected output

```text
5
['a', 'bb', 'c', 'z', 'zz']
3
['animal', 'city', 'food']
```

## How to check

`./check m09l05-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-making-a-set-and-predicting-its-size.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
