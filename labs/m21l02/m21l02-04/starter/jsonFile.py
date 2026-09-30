import json

scores = {'ada': 91, 'grace': 88, 'alan': 95}

with open('scores.json', 'w', encoding='utf-8') as out:
    json.dump(scores, out, indent=2)

print(open('scores.json', encoding='utf-8').read())

with open('scores.json', encoding='utf-8') as f:
    loaded = json.load(f)

print(loaded['grace'], type(loaded))
