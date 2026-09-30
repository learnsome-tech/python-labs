# m21l02 · JSON And CSV

Module 21: Files, Formats And The Standard Library · lesson 21.2 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m21l02)

**Goal:** You can save and load Python data as JSON, say which Python types survive the trip, and read a comma separated file with the csv module instead of splitting the line yourself.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m21l02-02](m21l02-02/) | Python to text, and text back to Python | Graded |
| [m21l02-03](m21l02-03/) | What survives the trip, and what does not | Graded |
| [m21l02-04](m21l02-04/) | Straight to a file, and straight back | Graded |
| [m21l02-05](m21l02-05/) | Rows and columns: writing and reading CSV | Graded |
| [m21l02-06](m21l02-06/) | DictReader, and why you do not split yourself | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### A little address book

1. Write contacts.py that keeps a list of dictionaries with a name, a city and an age.
2. Save it as JSON with json.dump, then load it back and print each name.
3. Export the same data to a CSV file with a header row using csv.DictWriter.
4. Read the CSV back with DictReader and print the average age.

> **Hint:** Dict writer needs the field names when you create it, and a call to write header before the rows. Ages read back from CSV are strings.

## Check yourself

- What is the difference between the dumps function and the dump function?
- Which Python types change on the way through JSON, and which are refused?
- Why does a value read from a CSV file need converting before you do arithmetic?
- What does DictReader do with the first line of the file?
- Give a concrete row that breaks a hand written split on a comma.

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
