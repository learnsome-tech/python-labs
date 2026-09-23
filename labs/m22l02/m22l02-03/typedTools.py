# Hands-on Python: Complete Video Course & Book — lesson m22l02 — Type Hints
# https://learnsome.tech/courses/python-course/watch?lesson=m22l02
# © LearnSome.tech
def word_lengths(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


def first_even(numbers: list[int]) -> int | None:
    for number in numbers:
        if number % 2 == 0:
            return number
    return None


print(word_lengths(['hi', 'there']))
print(first_even([1, 3, 4]), first_even([1, 3]))
