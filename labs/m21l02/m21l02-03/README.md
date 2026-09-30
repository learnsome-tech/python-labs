# m21l02-03 · What survives the trip, and what does not

**Lesson:** [JSON And CSV](https://learnsome.tech/learn/python-course/m21l02) (lesson 21.2, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can save and load Python data as JSON, say which Python types survive the trip, and read a comma separated file with the csv module instead of splitting the line yourself.

In the lesson: J son is not Python, so the mapping between them is worth knowing. A dictionary becomes an object, a list becomes an array, a string stays a string, and integers and floats stay numbers. Then three surprises. A tuple comes out as an array and comes back as a list, so the tuple you saved is not the tuple you load. True and False and None are written in lower case as true, false and null, because that is what the format calls them. And a key that was a number becomes a string key, and stays a string when you load it, because j son keys are always text. Finally, a set has no equivalent at all, and Python refuses rather than guessing, with a type error naming the type it cannot write.

## Files

- [`starter/jsonTypes.py`](starter/jsonTypes.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l02/m21l02-03/starter`
2. Read `jsonTypes.py`.
3. Run it: `python3 jsonTypes.py`.
4. Check it from the repository root: `./check m21l02-03`.

## Expected output

```text
{"when": [1, 2], "ok": true, "gone": null}
{"7": "seven"}
{'7': 'seven'}
TypeError: Object of type set is not JSON serializable
```

## How to check

`./check m21l02-03` copies `starter/` into a scratch directory and runs `python3 jsonTypes.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
