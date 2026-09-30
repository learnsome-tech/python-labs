def parse_count(text):
    try:
        return int(text)
    except ValueError:
        print('log: bad count from the user:', repr(text))
        raise

print(parse_count('12'))
print(parse_count('a few'))
