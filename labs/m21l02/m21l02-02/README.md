# m21l02-02 · Python to text, and text back to Python

**Lesson:** [JSON And CSV](https://learnsome.tech/learn/python-course/m21l02) (lesson 21.2, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can save and load Python data as JSON, say which Python types survive the trip, and read a comma separated file with the csv module instead of splitting the line yourself.

In the lesson: The module is called json and the two functions you need most end in the letter s, for string. Start with a dictionary holding a title and a year. Call dump s on it and you get text: the same data written the way the whole world writes it, with double quotes around the keys. Notice what comes back is a string, not a file and not a dictionary. Going the other way, load s takes that text and gives you the Python data back. The values are real numbers again, not text that looks like a number, so you can add one to the year straight away. That round trip, data to text and text to data, is the whole idea.

## Files

- [`starter/shell-python-to-text-and-text-back-to-python.py`](starter/shell-python-to-text-and-text-back-to-python.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l02/m21l02-02/starter`
2. Read `shell-python-to-text-and-text-back-to-python.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import json
   book = {'title': 'Dune', 'year': 1965}
   json.dumps(book)
   type(json.dumps(book))
   json.loads('{"a": 1, "b": [2, 3]}')
   json.loads('{"a": 1}')['a'] + 1
   ```
4. Run it: `python3 -i < shell-python-to-text-and-text-back-to-python.py`.
5. Check it from the repository root: `./check m21l02-02`.

## Expected output

```text
'{"title": "Dune", "year": 1965}'
<class 'str'>
{'a': 1, 'b': [2, 3]}
2
```

## How to check

`./check m21l02-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-python-to-text-and-text-back-to-python.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
