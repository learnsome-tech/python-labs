# Hands-on Python: Complete Video Course & Book — lesson m07l02 — Dictionaries And String Formatting
# https://learnsome.tech/courses/python-course/watch?lesson=m07l02
# © LearnSome.tech
def main():
    dictionary = createDictionary()
    numberFormat = "Count in Spanish: {one}, {two}, {three}, ..."
    withSubstitutions = numberFormat.format(**dictionary)
    print(withSubstitutions)
