# m20l04 · Dunder Methods, And Making Objects Pythonic

Module 20: Object Oriented Python · lesson 20.4 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m20l04)

**Goal:** You can give a class a useful repr and str, define equality and hashing consistently, make an object work with len, indexing and a for loop, and reach for a dataclass when the class is plain data.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m20l04-01](m20l04-01/) | What a dunder method is | Read along |
| [m20l04-02](m20l04-02/) | You have been calling dunder methods all along | Graded |
| [m20l04-03](m20l04-03/) | __repr__ for the programmer, __str__ for the reader | Graded |
| [m20l04-04](m20l04-04/) | Why every class needs at least a repr | Read along |
| [m20l04-05](m20l04-05/) | __eq__, and what defining it costs you | Graded |
| [m20l04-06](m20l04-06/) | Putting __hash__ back, consistently | Graded |
| [m20l04-07](m20l04-07/) | __len__ and __getitem__ make it a sequence | Graded |
| [m20l04-08](m20l04-08/) | dataclass, for the plain data case | Graded |

## Check yourself

- What makes a method name a dunder name, and who calls it?
- Which of __repr__ and __str__ is used when you print a list of objects?
- Why does defining __eq__ stop the object going into a set?
- Which two dunder methods let a for loop walk your object?
- When would you write the methods by hand instead of using @dataclass?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
