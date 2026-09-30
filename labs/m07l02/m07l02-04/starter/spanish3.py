def main():
    dictionary = createDictionary()
    numberFormat = "Count in Spanish: {one}, {two}, {three}, ..."
    withSubstitutions = numberFormat.format(**dictionary)
    print(withSubstitutions)
