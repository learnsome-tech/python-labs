# m11l06 · Animation: Loops, Bouncing, Flushing

Module 11: Graphics · lesson 11.6 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m11l06)

**Goal:** You can animate a group of shapes held in a list, move them diagonally and repeatedly with nested loops, build a shape group at any position by cloning points, and use autoflush with update to get one clean frame per step.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m11l06-02](m11l06-02/) | moveAll and moveAllOnLine | Read along |
| [m11l06-03](m11l06-03/) | Building the face, part by part | Read along |
| [m11l06-04](m11l06-04/) | The list, and the animation | Read along |
| [m11l06-06](m11l06-06/) | Withholding updates with autoflush | Read along |
| [m11l06-09](m11l06-09/) | makeFace: the head, and a relative point | Read along |
| [m11l06-10](m11l06-10/) | The first eye and the line eye | Read along |
| [m11l06-11](m11l06-11/) | The mouth, and the list that is returned | Read along |
| [m11l06-12](m11l06-12/) | Two faces, and a richer animation | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Nose in Face, and Faces

1. Nose in Face: save backAndForth3.py as backAndForth4.py and add a triangular nose.
2. Position the nose relative to the center parameter, and include it in the returned list.
3. Faces: write faces.py that draws a face where the user clicks, using your makeFace.
4. Use a simple repeat loop so a face appears after each of six mouse clicks.

### Moving Faces

1. Animate two faces moving in different directions at the same time, in move2Faces.py.
2. You may not use moveAllOnLine; write your own variation of it.
3. You may call moveAll separately for each face inside your own loop.

> **Hint:** Think of hand-drawn cartoons: place both, record a frame, move both a little, record again.

## Check yourself

- Why can moveOnLine not animate a face made of four shapes?
- Where exactly does the sleep belong when a whole group is moving?
- What does setting win.autoflush to False do, and what must you then call?
- Why does makeFace clone the center parameter instead of moving it?
- Which loop is the outer one in backAndForth3.py, and which is the inner one?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
